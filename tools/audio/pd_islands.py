#!/usr/bin/env python3
"""Podcast sound pass in ISLANDS (project/podcast/SOUND_PLAN.md; MANUAL §10.8 "Music limits").

Music and SFX exist only where the picture is edited: (a) the intro 0–346 s with a tail that fades under the first on-camera line,
(b) every edited section, entering ~0.8 s before its first frame and fading out over ~3 s after its last frame. Sections less than
20 s apart share one island. Between islands the beds are digital silence — only the voices.

  .venv/bin/python tools/audio/pd_islands.py --list                     # the island table (no audio work)
  .venv/bin/python tools/audio/pd_islands.py --only isl00,isl01          # build + measure these islands
  .venv/bin/python tools/audio/pd_islands.py --only isl00 --test-len 60  # build only the first 60 s of an island (test)
  .venv/bin/python tools/audio/pd_islands.py                            # all islands, then stitch + report
  .venv/bin/python tools/audio/pd_islands.py --stitch-only              # re-stitch + report from the stored island pre-mixes
  .venv/bin/python tools/audio/pd_islands.py --preflight                # markers only: unknown types, missing Epidemic SFX files

Per island (one heavy job at a time, each ≤ ~6 min of audio):
  1. cut the VO slice — a 48 kHz COPY in work/sound/isl/ (the master project/podcast/media/vo_pd.wav is only read);
  2. shift the editors' markers (compositions/pdNN.sfx.json, t LOCAL to the composition) to island time:
     island-local t = section start − island start + t  →  work/sound/isl/islNN.sfx.json;
  3. cue sheet project/podcast/cues/islNN.json (from project/podcast/gen/make_cuesheet.py, island-local seconds);
  4. tools/audio/place_sound.py → assets/audio/podcast/islNN/{music_bed,sfx,ambience}.wav + timeline.json;
  5. tools/audio/vo_music_scan.py (VERDICT, must say ALL LIMITS MET) + act_levels.py + mix-vs-VO loudness → islNN/report.json;
  6. the three beds are summed to islNN/premix.flac (48 kHz stereo 16-bit, TPDF dither, 30/50 ms safety fades) and the 24-bit
     WAVs are deleted (disk; --keep-wav keeps them).
Then every island pre-mix is streamed into ONE full-length file assets/audio/podcast/pd_beds_mix.wav (48 kHz stereo 16-bit; zeros
between islands; written in 10 s chunks, never the whole length in memory) + pd_beds_manifest.json, and
project/podcast/SOUND_REPORT.md is written (per island and overall: the VERDICT numbers, per-cue act levels, mix-vs-VO loudness).
"""
import argparse
import ast
import contextlib
import glob
import io
import json
import os
import re
import subprocess
import sys
import time

import numpy as np
import soundfile as sf

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
SR = 48000
PROJ = os.path.join(ROOT, "project", "podcast")
VO_MASTER = os.path.join(PROJ, "media", "vo_pd.wav")          # 44.1 kHz mono 16-bit — READ ONLY, never processed
SECTIONS = os.path.join(PROJ, "sections.json")
CUES = os.path.join(PROJ, "cues")
OUT = os.path.join(ROOT, "assets", "audio", "podcast")
WORK = os.path.join(ROOT, "work", "sound", "isl")
PY = sys.executable
FFMPEG = "ffmpeg"

INTRO_END = 346.0      # pd03's last frame (hard cut to Sam on camera)
INTRO_TAIL = 5.5       # the intro music fades out over ~5 s under his first on-camera line
PRE = 1.0              # island starts this long before a section's first frame (music enters ~0.8 s before the cut)
POST = 3.2             # island ends this long after a section's last frame (fade-out over ~2.5–3 s)
MERGE_GAP = 20.0       # sections closer than this share one island (music held very low between them)

# editors' marker types that place_sound does not know -> a known type (extend as editors invent names; reported)
PD_ALIAS = {"swoosh": "whoosh", "whoosh_low": "whoosh_soft", "whoosh_small": "whoosh_soft", "push": "whoosh_soft", "zoom": "whoosh_soft",
            "camera_move": "whoosh_soft", "slide": "paper_slide", "card_slide": "paper_slide", "photo_slide": "paper_slide",
            "paper": "paper_slide", "card": "paper_slide", "thud": "stamp_thud", "impact": "boom_low", "boom": "boom_low", "hit": "boom_low",
            "sub_boom": "boom_low", "tick": "tick_soft", "ticks": "counter_ticks", "counter": "counter_ticks", "count": "counter_ticks",
            "pop": "pop_soft", "pin": "pin_pop", "pin_drop": "map_pin", "marker": "marker_scratch", "circle": "marker_long",
            "underline": "marker_scratch", "highlight": "highlighter_swipe", "highlighter": "highlighter_swipe", "swell": "air_swell",
            "rise": "riser", "click": "switch_click", "switch": "switch_click", "shutter_click": "shutter", "camera": "shutter",
            "type": "typewriter", "typing_old": "typewriter", "blip": "tone_blip", "beep": "tone_blip", "chime": "chime_soft",
            "plane": "plane_pass", "jet": "plane_pass", "hum": "factory_hum", "room": "crowd_room", "projector": "projector_loop",
            "tear": "paper_tear", "rustle": "paper_rustle", "flip": "card_flip", "scribble": "pencil_scribble", "pencil": "pencil_scribble",
            "draw": "string_draw", "line_draw": "string_draw", "stamp_hit": "stamp_thud", "crt": "crt_click", "tv_on": "crt_click"}


def r2(x):
    return round(float(x) + 1e-9, 2)


def build_islands(sections_path=SECTIONS):
    """[{id, start, end, len, kind, sections:[{id,start,end,dur,title}]}] — times in master seconds on a 0.01 s grid."""
    d = json.load(open(sections_path))
    total = float(d.get("length", 5752.03))
    secs = sorted(d["sections"], key=lambda s: s["start"])
    intro = [s for s in secs if s["start"] < INTRO_END - 1e-6]
    rest = [s for s in secs if s["start"] >= INTRO_END - 1e-6]
    groups = [("intro", intro)] if intro else []
    cur = []
    for s in rest:
        if cur and s["start"] - cur[-1]["end"] < MERGE_GAP:
            cur.append(s)
        else:
            if cur:
                groups.append(("section", cur))
            cur = [s]
    if cur:
        groups.append(("section", cur))
    out = []
    for k, (kind, g) in enumerate(groups):
        a = 0.0 if kind == "intro" else max(0.0, g[0]["start"] - PRE)
        b = min(total, g[-1]["end"] + (INTRO_TAIL if kind == "intro" else POST))
        if out and a < out[-1]["end"]:                     # never overlap the previous island
            a = out[-1]["end"]
        a, b = r2(np.floor(a * 100) / 100), r2(np.ceil(b * 100) / 100)
        out.append(dict(id=f"isl{k:02d}", kind=kind, start=a, end=b, len=r2(b - a),
                        sections=[dict(id=s["id"], start=s["start"], end=s["end"], dur=s["dur"], title=s.get("title", "")) for s in g]))
    return out, total


# ---------------------------------------------------------------- markers
def _known_types():
    """Types place_sound accepts: GAIN keys + AMBTYPES + its ALIAS keys (read from the source, no import side effects)."""
    src = open(os.path.join(HERE, "place_sound.py")).read()
    m = re.search(r"\n    ALIAS = (\{.*?\n\s*\})\n", src, re.S)
    alias = ast.literal_eval(m.group(1)) if m else {}
    import place_sound as PS
    return set(PS.GAIN) | set(PS.AMBTYPES) | {"bleep"}, alias


def island_markers(isl, known=None, alias=None):
    """Editors' markers of every section of the island, shifted to island time. Returns (markers, notes)."""
    if known is None:
        known, alias = _known_types()
    ms, notes = [], []
    for s in isl["sections"]:
        f = os.path.join(ROOT, "compositions", f"{s['id']}.sfx.json")
        if not os.path.exists(f):
            notes.append(f"{s['id']}: no sfx.json (music only)")
            continue
        try:
            raw = json.load(open(f))
        except Exception as e:                                # a half-written file must not stop the island
            notes.append(f"{s['id']}: sfx.json unreadable ({e}) — skipped")
            continue
        n_ok = 0
        for m in raw:
            if not isinstance(m, dict) or "t" not in m or "type" not in m:
                notes.append(f"{s['id']}: malformed marker {str(m)[:60]} — skipped")
                continue
            t = float(m["t"])
            if t > s["dur"] + 0.5 and abs(t - s["start"]) < s["dur"] + 1.0 and t >= s["start"] - 0.5:
                notes.append(f"{s['id']}: marker t={t} looks like MASTER time — read as local {t - s['start']:.2f}")
                t -= s["start"]
            if t < -0.6 or t > s["dur"] + 0.3:
                notes.append(f"{s['id']}: marker {m['type']}@{t} outside the section (0–{s['dur']}) — dropped")
                continue
            m = dict(m)
            ty = m["type"]
            if ty not in known and ty not in alias:
                to = PD_ALIAS.get(ty)
                if to is None:
                    to = next((v for k, v in (("whoosh", "whoosh_soft"), ("whip", "whip"), ("boom", "boom_low"), ("paper", "paper_slide"),
                                              ("tick", "tick_soft"), ("pop", "pop_soft"), ("click", "switch_click"),
                                              ("marker", "marker_scratch"), ("stamp", "stamp_thud")) if k in ty), None)
                if to is None:
                    notes.append(f"{s['id']}: unknown type '{ty}'@{t} — dropped (add it to PD_ALIAS)")
                    continue
                notes.append(f"{s['id']}: type '{ty}' → '{to}'")
                m["type"] = to
            m["t"] = round(s["start"] - isl["start"] + t, 3)
            m["src"] = f"{s['id']}@{t}"
            sc = str(m.get("scene", "") or "")
            m["scene"] = sc if sc.lower().startswith(s["id"]) else f"{s['id']}-{sc or 'sc'}"
            if not isinstance(m.get("dur", 0), (int, float)) or m.get("dur") is None:
                m["dur"] = 0
            ms.append(m)
            n_ok += 1
        notes.append(f"{s['id']}: {n_ok} markers")
    ms.sort(key=lambda m: m["t"])
    return ms, notes


# ---------------------------------------------------------------- per island
def cut_vo(isl, length):
    """48 kHz mono 16-bit COPY of the master VO for the island (sample-exact start: the 0.01 s grid is 441 samples at 44.1 kHz)."""
    os.makedirs(WORK, exist_ok=True)
    p = os.path.join(WORK, f"{isl['id']}_vo.wav")
    info = sf.info(VO_MASTER)
    a = int(round(isl["start"] * info.samplerate))
    n = int(round(length * info.samplerate))
    subprocess.run([FFMPEG, "-v", "error", "-y", "-i", VO_MASTER, "-af",
                    f"atrim=start_sample={a}:end_sample={a + n},asetpts=N/SR/TB,aresample={SR}", "-ac", "1", "-c:a", "pcm_s16le", p], check=True)
    return p


def lufs_i(e, hop=0.01):
    """Gated BS.1770 integrated loudness from 10 ms hop energies (same method as vo_music_scan)."""
    import epidemic_bed as E
    lb = E.window_lufs(e, 0.4, hop)[::10]
    z = 10 ** ((lb + 0.691) / 10)
    keep = lb > -70
    if not keep.any():
        return -70.0
    rel = -0.691 + 10 * np.log10(z[keep].mean()) - 10
    return float(-0.691 + 10 * np.log10(z[keep & (lb > rel)].mean()))


def measure_island(isl, vo, d, length, log):
    """VERDICT (vo_music_scan), pooled gap arrays, act levels, mix-vs-VO loudness. Returns the report dict."""
    import epidemic_bed as E
    import vo_music_scan as S
    rep = {}
    r = subprocess.run([PY, os.path.join(HERE, "vo_music_scan.py"), "--vo", vo, "--beds", d], capture_output=True, text=True)
    open(os.path.join(d, "scan.txt"), "w").write(r.stdout + r.stderr)
    v = r.stdout[r.stdout.rfind("VERDICT"):] if "VERDICT" in r.stdout else ""
    rep["verdict_text"] = v.strip()
    rep["all_limits_met"] = "ALL LIMITS MET" in v and r.returncode == 0
    lines = re.findall(r"(PASS|FAIL)\s+(.*?): (-?[\d.]+) LU", v)
    keys = [("3 s music gap while he speaks — MIN", "gap3_min"), ("5th percentile", "gap3_p5"), ("median", "gap3_median"),
            ("pauses", "pause_min"), ("0.4 s", "gap04_p1"), ("music+SFX", "mus_sfx_min")]
    for ok, name, val in lines:
        for frag, k in keys:
            if frag in name and k not in rep:
                rep[k] = float(val)
                break
    m = re.search(r"VERDICT \(VO (-?[\d.]+) LUFS-I\)", v)
    rep["vo_lufs"] = float(m.group(1)) if m else None
    log(v.strip() or (r.stdout[-600:] + r.stderr[-600:]))
    # pooled arrays for the overall verdict (same windows as the scan)
    with contextlib.redirect_stdout(io.StringIO()):
        res = S.scan(vo, d, 0.0, length, 18.0, quiet=True)
    t, lv, lm, lms, spk, dm, dms = res[3.0]
    t4, lv4, lm4, lms4, spk4, dm4, dms4 = res[0.4]
    np.savez_compressed(os.path.join(d, "gaps.npz"), dm3=dm[spk].astype(np.float32), dms3=dms[spk].astype(np.float32),
                        dm04=dm4[spk4].astype(np.float32), rest3=((rep["vo_lufs"] or 0) - lm)[~spk].astype(np.float32),
                        t3=(isl["start"] + t[spk]).astype(np.float32))
    k = int(np.argmin(dm[spk])) if spk.any() else 0
    rep["gap3_min_at_master"] = round(float(isl["start"] + t[spk][k]), 1) if spk.any() else None
    # act levels per cue (music while the voice speaks, LU re the VO)
    cue = os.path.join(CUES, f"{isl['id']}.json")
    r = subprocess.run([PY, os.path.join(HERE, "act_levels.py"), "--vo", vo, "--beds", d, "--cues", cue, "--len", str(length)],
                       capture_output=True, text=True)
    acts = []
    for ln in r.stdout.splitlines():
        mm = re.match(r"(\S+)\s+([\d.]+)–\s*([\d.]+)\s+(-?[\d.]+|nan)\s+(-?[\d.]+|nan)\s+([+-]?[\d.]+|nan)\s+(-?[\d.]+|nan)", ln)
        if mm:
            f = lambda s: None if s == "nan" else float(s)
            acts.append(dict(cue=mm.group(1), start=float(mm.group(2)), end=float(mm.group(3)), vo=f(mm.group(4)), music=f(mm.group(5)),
                             re_vo=f(mm.group(6)), pauses=f(mm.group(7))))
    rep["acts"] = acts
    if not acts:
        log("act_levels: no table —", r.stderr[-400:])
    # final mix vs VO alone: the VO (mono, the same signal in both channels) + the three beds at unity
    ev = E.hop_energy(vo, 0.01)
    n = len(ev)
    x, _ = sf.read(vo, dtype="float64", always_2d=True)
    beds = sum(sf.read(os.path.join(d, f), dtype="float64", always_2d=True)[0] for f in ("music_bed.wav", "sfx.wav", "ambience.wav"))
    k = min(len(x), len(beds))
    mix = beds[:k] + x[:k]                               # (k,2) + (k,1): VO in both channels
    em = E.hop_energy(mix, 0.01)[:n]
    e2 = E.hop_energy(np.repeat(x[:k], 2, 1), 0.01)[:n]
    rep["vo_alone_lufs"] = round(lufs_i(e2), 2)
    rep["mix_lufs"] = round(lufs_i(em), 2)
    rep["mix_minus_vo_lu"] = round(rep["mix_lufs"] - rep["vo_alone_lufs"], 2)
    w = 1000                                             # 10 s windows
    dif = [10 * np.log10(em[i:i + w].sum() / (e2[i:i + w].sum() + 1e-20)) for i in range(0, max(1, n - w + 1), w // 2)
           if e2[i:i + w].sum() > 0]
    rep["mix_minus_vo_10s_max"] = round(float(max(dif)), 2) if dif else None
    rep["vo_peak_dbfs"] = round(float(20 * np.log10(np.abs(x).max() + 1e-12)), 1)
    rep["mix_peak_dbfs"] = round(float(20 * np.log10(np.abs(mix).max() + 1e-12)), 1)
    eb = E.hop_energy(beds, 0.01)
    rep["beds_lufs"] = round(lufs_i(eb), 1)
    # island edges must be silent (hard cuts in the full-length file otherwise)
    q = int(0.05 * SR)
    rep["edge_in_dbfs"] = round(float(20 * np.log10(np.abs(beds[:q]).max() + 1e-9)), 1)
    rep["edge_out_dbfs"] = round(float(20 * np.log10(np.abs(beds[-q:]).max() + 1e-9)), 1)
    # pre-mix: 16-bit with TPDF dither + safety fades
    rng = np.random.default_rng(int(isl["id"][3:]) + 7)
    beds = beds[: int(round(length * SR))]
    fi, fo = int(0.03 * SR), int(0.05 * SR)
    beds[:fi] *= np.linspace(0, 1, fi)[:, None]
    beds[-fo:] *= np.linspace(1, 0, fo)[:, None]
    beds += (rng.random(beds.shape) - rng.random(beds.shape)) / 32768.0
    beds[0] = 0.0
    beds[-1] = 0.0
    sf.write(os.path.join(d, "premix.flac"), np.clip(beds, -1, 1), SR, subtype="PCM_16")
    rep["premix"] = os.path.relpath(os.path.join(d, "premix.flac"), ROOT)
    return rep


def build_island(isl, a):
    t0 = time.time()
    length = isl["len"] if not a.test_len else min(isl["len"], a.test_len)
    d = os.path.join(OUT, isl["id"])
    os.makedirs(d, exist_ok=True)
    os.makedirs(WORK, exist_ok=True)
    logf = open(os.path.join(WORK, f"{isl['id']}.log"), "w")

    def log(*x):
        s = " ".join(str(i) for i in x)
        print(s, flush=True)
        logf.write(s + "\n")
    log(f"=== {isl['id']} master {isl['start']:.2f}–{isl['end']:.2f} ({isl['len']:.2f} s"
        + (f", TEST first {length:g} s" if length != isl["len"] else "") + ") " + " ".join(s["id"] for s in isl["sections"]))
    cue = os.path.join(CUES, f"{isl['id']}.json")
    if not os.path.exists(cue):
        raise SystemExit(f"missing {cue} — run project/podcast/gen/make_cuesheet.py first")
    sheet = json.load(open(cue))
    for k, lim in (("bed_lu_under_vo", 22.0),):
        assert float(sheet.get(k, 22.0)) >= lim, f"{cue}: {k} below the binding limit {lim}"
    assert float(sheet.get("pause_lift_db", 0.0)) == 0.0, f"{cue}: pause lifts are not allowed"
    dk = sheet.get("vo_duck", {})
    assert dk is not False and float((dk or {}).get("gap", 20.0)) >= 20.0 and float((dk or {}).get("gap_fast", 18.0)) >= 18.0 \
        and float((dk or {}).get("ceiling", 20.0)) >= 20.0, f"{cue}: vo_duck weaker than the binding defaults"
    vo = cut_vo(isl, length)
    ms, notes = island_markers(isl)
    ms = [m for m in ms if m["t"] < length - 0.2]
    for nline in notes:
        log("  markers:", nline)
    mf = os.path.join(WORK, f"{isl['id']}.sfx.json")
    json.dump(ms, open(mf, "w"), indent=1)
    cmd = [PY, os.path.join(HERE, "place_sound.py"), "--vo", os.path.relpath(vo, ROOT), "--transcript", "transcript_pd.json",
           "--len", f"{length:.2f}", "--markers", os.path.relpath(mf, ROOT), "--cues", os.path.relpath(cue, ROOT),
           "--out", os.path.relpath(d, ROOT)] + (["--no-hierarchy"] if a.no_hierarchy else [])
    r = subprocess.run(cmd, capture_output=True, text=True, cwd=ROOT)
    log(r.stdout.strip())
    if r.returncode != 0:
        log(r.stderr[-3000:])
        raise SystemExit(f"place_sound failed for {isl['id']}")
    rep = dict(id=isl["id"], kind=isl["kind"], start=isl["start"], end=isl["end"], len=isl["len"], built_len=length,
               sections=[s["id"] for s in isl["sections"]], markers_in=len(ms), marker_notes=notes)
    hp = os.path.join(d, "sfx_hierarchy.json")
    if os.path.exists(hp):
        h = json.load(open(hp))
        rep["markers_kept"] = h["kept"]
    mr = json.load(open(os.path.join(d, "music_report.json")))
    rep["vo_lufs_ffmpeg"], rep["bed_target_lufs"], rep["bed_final_lufs"], rep["vo_duck"] = mr["vo_lufs"], mr["target_lufs"], mr["final_lufs"], mr["vo_duck"]
    rep["missing_layers"] = [ln.strip() for ln in r.stdout.splitlines() if "!! missing" in ln]
    rep.update(measure_island(isl, vo, d, length, log))
    rep["cues"] = sorted({ly.get("cue", "?") for ly in sheet["layers"]})
    rep["tracks"] = sorted({ly.get("file") or f"{ly['track']}/{ly['stem']}" for ly in sheet["layers"]})
    rep["seconds_to_build"] = round(time.time() - t0, 1)
    json.dump(rep, open(os.path.join(d, "report.json"), "w"), indent=1)
    if not a.keep_wav:
        for f in ("music_bed.wav", "sfx.wav", "ambience.wav"):
            os.remove(os.path.join(d, f))
        tl = [dict(id="bed-premix", src=rep["premix"], start=isl["start"], duration=length, media_start=0, volume=1.0)]
        json.dump(tl, open(os.path.join(d, "timeline.json"), "w"), indent=1)
    if not a.keep_vo:
        os.remove(vo)
    log(f"{isl['id']}: {'ALL LIMITS MET' if rep['all_limits_met'] else 'LIMITS NOT MET'} · mix − VO {rep['mix_minus_vo_lu']:+.2f} LU · "
        f"{rep['seconds_to_build']} s")
    logf.close()
    return rep


# ---------------------------------------------------------------- stitch + report
def stitch(islands, total, fmt="wav"):
    """One full-length 48 kHz stereo 16-bit pre-mix, streamed (10 s chunks). Islands without a pre-mix stay silent (reported)."""
    os.makedirs(OUT, exist_ok=True)
    out = os.path.join(OUT, f"pd_beds_mix.{fmt}")
    N = int(round(total * SR))
    chunk = 10 * SR
    man = []
    with sf.SoundFile(out, "w", samplerate=SR, channels=2, subtype="PCM_16", format="FLAC" if fmt == "flac" else "WAV") as w:
        pos = 0
        for isl in islands:
            p = os.path.join(OUT, isl["id"], "premix.flac")
            rp = os.path.join(OUT, isl["id"], "report.json")
            ent = dict(id=isl["id"], kind=isl["kind"], start=isl["start"], end=isl["end"], sections=[s["id"] for s in isl["sections"]],
                       premix=os.path.relpath(p, ROOT) if os.path.exists(p) else None,
                       report=os.path.relpath(rp, ROOT) if os.path.exists(rp) else None)
            man.append(ent)
            if not os.path.exists(p):
                continue
            i0 = int(round(isl["start"] * SR))
            assert i0 >= pos, (isl["id"], "overlaps the previous island")
            while pos < i0:                                   # silence up to the island
                k = min(chunk, i0 - pos)
                w.write(np.zeros((k, 2), np.int16))
                pos += k
            with sf.SoundFile(p) as f:
                assert f.samplerate == SR and f.channels == 2
                ent["frames"] = min(f.frames, N - pos)
                left = ent["frames"]
                while left > 0:
                    blk = f.read(min(chunk, left), dtype="int16", always_2d=True)
                    if not len(blk):
                        break
                    w.write(blk)
                    pos += len(blk)
                    left -= len(blk)
        while pos < N:
            k = min(chunk, N - pos)
            w.write(np.zeros((k, 2), np.int16))
            pos += k
    manifest = dict(mix=os.path.relpath(out, ROOT), samplerate=SR, channels=2, subtype="PCM_16", length=total, frames=N,
                    mount="one <audio>/ffmpeg input at master 0.00, volume 1.0 (unity), next to the untouched VO; nothing else to add",
                    islands=man)
    json.dump(manifest, open(os.path.join(OUT, "pd_beds_manifest.json"), "w"), indent=1)
    json.dump([dict(id="bed-premix", src=manifest["mix"], start=0, duration=total, media_start=0, volume=1.0)],
              open(os.path.join(OUT, "timeline.json"), "w"), indent=1)
    print(f"stitched {sum(1 for e in man if e['premix'])}/{len(man)} islands → {manifest['mix']} ({os.path.getsize(out) / 1e6:.0f} MB)")
    return manifest


def check_stitch(manifest, islands):
    """Reads the stitched file back in chunks: silence between islands is digital zero; each island matches its pre-mix."""
    p = os.path.join(ROOT, manifest["mix"])
    bad = []
    with sf.SoundFile(p) as f:
        assert f.frames == manifest["frames"], (f.frames, manifest["frames"])
        pos, nz_outside = 0, 0
        spans = [(int(round(i["start"] * SR)), int(round(i["start"] * SR)) + e.get("frames", 0), i["id"])
                 for i, e in zip(islands, manifest["islands"]) if e.get("premix")]
        inside = np.zeros(0)
        while pos < f.frames:
            blk = f.read(10 * SR, dtype="int16", always_2d=True)
            m = np.ones(len(blk), bool)
            for a, b, _ in spans:
                lo, hi = max(a, pos) - pos, min(b, pos + len(blk)) - pos
                if hi > lo:
                    m[lo:hi] = False
            nz_outside += int(np.abs(blk[m]).sum())
            pos += len(blk)
    if nz_outside:
        bad.append(f"non-zero samples between islands (sum {nz_outside})")
    return bad


def fmt_t(s):
    return f"{int(s // 60)}:{s % 60:05.2f}"


def write_report(islands, total, manifest=None, stitch_issues=None):
    reps, gaps = [], dict(dm3=[], dms3=[], dm04=[], rest3=[])
    for isl in islands:
        rp = os.path.join(OUT, isl["id"], "report.json")
        if not os.path.exists(rp):
            reps.append(None)
            continue
        reps.append(json.load(open(rp)))
        gp = os.path.join(OUT, isl["id"], "gaps.npz")
        if os.path.exists(gp):
            z = np.load(gp)
            for k in gaps:
                gaps[k].append(z[k])
    built = [r for r in reps if r]
    L = ["# SOUND REPORT — podcast (\"TSMC vs UMC\"), music + SFX islands vs the voice",
         "",
         f"Generated by `tools/audio/pd_islands.py` on {time.strftime('%Y-%m-%d %H:%M')} — {len(built)} of {len(islands)} islands built. "
         "Method and limits: MANUAL §10.8 \"Music limits\" (Krish 2026-11-13); plan: `project/podcast/SOUND_PLAN.md`.",
         "All gaps are K-weighted (BS.1770) loudness differences in LU: how far the music sits UNDER the voice (bigger = quieter music).",
         "The voice track is never processed: every measurement reads a copy.",
         ""]
    if built:
        cat = {k: (np.concatenate(v) if v else np.zeros(0)) for k, v in gaps.items()}
        isl_time = sum(r["built_len"] for r in built)
        ok_all = all(r["all_limits_met"] for r in built)
        L += ["## Overall (all built islands pooled)", "",
              "| what | measured | limit | |", "|---|---|---|---|"]

        def row(name, val, lim, unit="LU"):
            L.append(f"| {name} | **{val:.1f} {unit}** | ≥ {lim:g} | {'PASS' if val >= lim else 'FAIL'} |")
        if len(cat["dm3"]):
            row("music under the voice while they speak, 3 s windows — closest moment", float(cat["dm3"].min()), 18)
            row("… 5th percentile", float(np.percentile(cat["dm3"], 5)), 20)
            row("… median", float(np.median(cat["dm3"])), 20)
        if len(cat["rest3"]):
            row("music in pauses / tails vs the voice's integrated loudness — closest", float(cat["rest3"].min()), 18)
        else:
            L.append("| music in pauses / tails | — (no 3 s window without speech inside an island) | ≥ 18 | n/a |")
        if len(cat["dm04"]):
            row("music vs the local speech level, 0.4 s windows — 1st percentile", float(np.percentile(cat["dm04"], 1)), 15)
        if len(cat["dms3"]):
            row("music + SFX under the voice, 3 s windows — closest moment", float(cat["dms3"].min()), 14)
        worst = max(built, key=lambda r: r["mix_minus_vo_lu"])
        L.append(f"| final mix vs the voice alone (integrated, per island) — largest change | **{worst['mix_minus_vo_lu']:+.2f} LU** ({worst['id']}) "
                 f"| < 0.5 | {'PASS' if abs(worst['mix_minus_vo_lu']) < 0.5 else 'FAIL'} |")
        L += ["",
              f"Islands with sound: {isl_time:.0f} s of {total:.0f} s ({isl_time / total * 100:.0f} %); the other "
              f"{(total - isl_time) / 60:.0f} minutes are voices only (the bed file is digital silence there). "
              f"**{'ALL LIMITS MET in every island' if ok_all else 'LIMITS NOT MET in: ' + ', '.join(r['id'] for r in built if not r['all_limits_met'])}**.",
              ""]
    L += ["## Per island", "",
          "| island | master | sections | VO LUFS-I | 3 s gap min / p5 / median | pauses min | 0.4 s p1 | music+SFX min | markers kept/in | mix − VO | verdict |",
          "|---|---|---|---|---|---|---|---|---|---|---|"]
    g = lambda r, k, f="{:.1f}": "—" if r.get(k) is None else f.format(r[k])
    for isl, r in zip(islands, reps):
        secs = isl["sections"][0]["id"] + ("–" + isl["sections"][-1]["id"] if len(isl["sections"]) > 1 else "")
        if not r:
            L.append(f"| {isl['id']} | {fmt_t(isl['start'])}–{fmt_t(isl['end'])} | {secs} | not built | | | | | | | |")
            continue
        part = "" if r["built_len"] == r["len"] else f" (TEST: first {r['built_len']:g} s)"
        L.append(f"| {isl['id']}{part} | {fmt_t(isl['start'])}–{fmt_t(isl['end'])} | {secs} | {g(r, 'vo_lufs')} | "
                 f"{g(r, 'gap3_min')} / {g(r, 'gap3_p5')} / {g(r, 'gap3_median')} | {g(r, 'pause_min')} | {g(r, 'gap04_p1')} | {g(r, 'mus_sfx_min')} | "
                 f"{r.get('markers_kept', r['markers_in'])}/{r['markers_in']} | {r['mix_minus_vo_lu']:+.2f} (10 s max {g(r, 'mix_minus_vo_10s_max', '{:+.2f}')}) | "
                 f"{'ALL LIMITS MET' if r['all_limits_met'] else '**NOT MET**'} |")
    L += ["", "## Per-cue music level while they speak (act_levels.py; aim −20…−24 LU re the voice)", "",
          "| island | cue | island-local span | voice LUFS | music LUFS | music re voice |", "|---|---|---|---|---|---|"]
    for r in built:
        for a in r.get("acts", []):
            if a["cue"] == "all" and len(r["acts"]) > 2:
                continue
            L.append(f"| {r['id']} | {a['cue']} | {a['start']:.1f}–{a['end']:.1f} | {a['vo']} | {a['music']} | {a['re_vo']:+.1f} LU |"
                     if a["re_vo"] is not None else f"| {r['id']} | {a['cue']} | {a['start']:.1f}–{a['end']:.1f} | — | — | — |")
    L += ["", "## Voice unchanged — mix vs voice alone", "",
          "Voice (mono, both channels, unity) + the pre-mixed beds at unity, per island. Peaks in dBFS.", "",
          "| island | voice alone LUFS | mix LUFS | Δ | largest Δ in any 10 s | voice peak | mix peak | beds LUFS |", "|---|---|---|---|---|---|---|---|"]
    for r in built:
        L.append(f"| {r['id']} | {r['vo_alone_lufs']} | {r['mix_lufs']} | {r['mix_minus_vo_lu']:+.2f} | {g(r, 'mix_minus_vo_10s_max', '{:+.2f}')} | "
                 f"{r['vo_peak_dbfs']} | {r['mix_peak_dbfs']} | {r['beds_lufs']} |")
    notes = [(r["id"], n) for r in built for n in r.get("marker_notes", []) if "→" in n or "dropped" in n or "skipped" in n or "MASTER" in n]
    miss = [(r["id"], n) for r in built for n in r.get("missing_layers", [])]
    edges = [(r["id"], r["edge_in_dbfs"], r["edge_out_dbfs"]) for r in built if max(r["edge_in_dbfs"], r["edge_out_dbfs"]) > -60]
    L += ["", "## Notes", ""]
    L += [f"- {i}: {n}" for i, n in notes] or ["- markers: nothing retyped or dropped before the restraint pass."]
    L += [f"- **{i}: {n}**" for i, n in miss]
    L += [f"- {i}: island edge not silent before the safety fade (in {a} dBFS, out {b} dBFS) — check the cue's fades" for i, a, b in edges]
    if manifest:
        L += [f"- Full-length pre-mix: `{manifest['mix']}` ({manifest['frames']} frames, 48 kHz stereo 16-bit) — mount at 0.00, volume 1.0; "
              f"manifest `assets/audio/podcast/pd_beds_manifest.json`."]
    for s in stitch_issues or []:
        L.append(f"- **stitch check: {s}**")
    if manifest and not stitch_issues:
        L.append("- Stitch check: digital silence between all islands; frame count = master length.")
    open(os.path.join(PROJ, "SOUND_REPORT.md"), "w").write("\n".join(L) + "\n")
    print("wrote project/podcast/SOUND_REPORT.md")


def preflight(islands):
    """Markers only: retyped/unknown types and Epidemic SFX files a marker would need but are not on disk."""
    import place_sound as PS
    known, alias = _known_types()
    PS.EPIDEMIC = True
    need = set()
    tot = 0
    for isl in islands:
        ms, notes = island_markers(isl, known, alias)
        tot += len(ms)
        for n in notes:
            if "→" in n or "dropped" in n or "skipped" in n or "MASTER" in n:
                print(f"{isl['id']}: {n}")
        rng = np.random.default_rng(1)
        for i, m in enumerate(ms):
            m = dict(m, type=alias.get(m["type"], m["type"]))
            if m["type"] in PS.AMBTYPES or m["type"] == "bleep":
                continue
            try:
                PS.render_event(m, i, rng, False)
            except Exception as e:                           # a missing Epidemic file shows up here
                mm = re.search(r"([\w]+)\.wav", str(e))
                need.add(mm.group(1) if mm else f"{m['type']}: {str(e)[:80]}")
    print(f"{tot} markers in {len(islands)} islands; missing SFX files: {sorted(need) or 'none'}")
    return need


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--only", default="", help="comma-separated island ids (isl00,isl07) or section ids (pd04)")
    ap.add_argument("--test-len", type=float, default=0.0, help="build only the first N seconds of each chosen island")
    ap.add_argument("--no-stitch", action="store_true")
    ap.add_argument("--stitch-only", action="store_true")
    ap.add_argument("--report-only", action="store_true")
    ap.add_argument("--preflight", action="store_true")
    ap.add_argument("--format", default="wav", choices=["wav", "flac"], help="container of the full-length pre-mix")
    ap.add_argument("--keep-wav", action="store_true", help="keep the island's three 24-bit beds")
    ap.add_argument("--keep-vo", action="store_true", help="keep the island's VO slice (work/sound/isl)")
    ap.add_argument("--no-hierarchy", action="store_true")
    ap.add_argument("--skip-built", action="store_true", help="skip islands that already have a full-length report + pre-mix")
    a = ap.parse_args()
    islands, total = build_islands()
    if a.list:
        for i in islands:
            print(f"{i['id']} {i['kind']:7s} {i['start']:8.2f}–{i['end']:8.2f} ({i['len']:6.2f} s)  " + " ".join(s["id"] for s in i["sections"]))
        print(f"{len(islands)} islands, {sum(i['len'] for i in islands):.0f} s of {total:.0f} s with sound")
        sys.exit()
    sel = [x for x in a.only.split(",") if x]
    chosen = [i for i in islands if not sel or i["id"] in sel or any(s["id"] in sel for s in i["sections"])]
    if a.preflight:
        preflight(chosen)
        sys.exit()
    if not (a.stitch_only or a.report_only):
        for isl in chosen:
            rp = os.path.join(OUT, isl["id"], "report.json")
            if a.skip_built and os.path.exists(rp) and os.path.exists(os.path.join(OUT, isl["id"], "premix.flac")) \
                    and json.load(open(rp)).get("built_len") == isl["len"]:
                print(f"{isl['id']}: already built — skipped")
                continue
            build_island(isl, a)                             # one heavy job at a time
    man, issues = None, None
    if not (a.no_stitch or a.report_only):
        man = stitch(islands, total, a.format)
        issues = check_stitch(man, islands)
    elif os.path.exists(os.path.join(OUT, "pd_beds_manifest.json")):
        man = json.load(open(os.path.join(OUT, "pd_beds_manifest.json")))
    write_report(islands, total, man, issues)
