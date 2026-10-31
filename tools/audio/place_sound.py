#!/usr/bin/env python3
"""Phase 2: place the sound on the finished 600 s edit -> three pre-mixed beds + timeline.json.

  assets/audio/bed/music_bed_600s.wav   music (cue sheet -> build_bed.py), ducked + carved, final level
  assets/audio/bed/sfx_600s.wav         every marker of compositions/seg0*.sfx.json, final level
  assets/audio/bed/ambience_600s.wav    projector / CRT hum / wind markers + room tone / vinyl / cloud wind
  assets/audio/timeline.json            three tracks at volume 1.0 for tools/build_master.py
  assets/audio/bed/music_cuesheet.json  the cue sheet actually rendered
  assets/audio/bed/sfx_placements.json  every marker -> sound, take, start, gain (for audit)

Run:  .venv/bin/python tools/audio/place_sound.py            (legacy 600 s edit, synthesized score)
Epidemic project mode (MANUAL §10.3 / §10.8), e.g. the intro:
      .venv/bin/python tools/audio/place_sound.py --vo vo_intro.mp3 --transcript transcript_intro.json --len 275.06 \
          --markers 'compositions/intro0*.sfx.json' --cues project/intro/music_cuesheet.json --out assets/audio/intro
  -> <out>/music_bed.wav, sfx.wav, ambience.wav, timeline.json, music_report.json, sfx_placements.json,
     sfx_hierarchy.json (the §10.8 restraint pass: which editor markers were kept / dropped and why).
  The VO loudness is MEASURED (bed = VO − bed_lu_under_vo); layers are Epidemic stems read in windows.
The VO is only READ (to find its pauses); it is never processed or written.
"""
import argparse
import shutil
import glob
import json
import os
import re
import subprocess
import sys
import tempfile

import numpy as np
import soundfile as sf

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import gen_sfx as G                                   # noqa: E402  (generator functions, no side effects)
from dsp import SR, AUDIO, ROOT, db, peaking, hp, fade, reverb, make_ir, peak_norm   # noqa: E402
from instruments import pizz                           # noqa: E402
from loudness import integrated_lufs                   # noqa: E402

LEN = 600.0
N = int(LEN * SR)
BED = os.path.join(AUDIO, "bed")
FFMPEG = shutil.which("ffmpeg") or os.path.expanduser("~/.local/bin/ffmpeg")
VO_FILE = "vo10.mp3"
WORDS_FILE = "transcript.json"
SUFFIX = "_600s"
EPIDEMIC = False
PY = sys.executable
VO_LUFS = -27.2
MUSIC_TARGET = -41.0          # integrated music bed loudness (~14 LU under the VO)


# =============================================================== VO analysis (read-only)
def vo_activity():
    with tempfile.TemporaryDirectory() as td:
        p = os.path.join(td, "vo.wav")
        subprocess.run([FFMPEG, "-v", "error", "-y", "-i", os.path.join(ROOT, VO_FILE), "-ar", "48000", p], check=True)
        x, _ = sf.read(p, always_2d=True)
    h = int(0.02 * SR)
    n = len(x) // h
    lev = 20 * np.log10(np.sqrt((x[: n * h].reshape(n, h, -1) ** 2).mean(1).max(1)) + 1e-9)
    act = lev > -45.0
    # close micro-gaps < 0.25 s (inside words)
    i = 0
    while i < n:
        if not act[i]:
            j = i
            while j < n and not act[j]:
                j += 1
            if (j - i) * 0.02 < 0.25 and i > 0 and j < n:
                act[i:j] = True
            i = j
        else:
            i += 1
    pauses = []
    i = 0
    while i < n:
        if not act[i]:
            j = i
            while j < n and not act[j]:
                j += 1
            if (j - i) * 0.02 >= 0.6:
                pauses.append((i * 0.02, j * 0.02))
            i = j
        else:
            i += 1
    return act, pauses, x


def words():
    return json.load(open(os.path.join(ROOT, WORDS_FILE)))


def density_windows(ws, win=10.0):
    st = np.array([w["start"] for w in ws])
    return {a: ((st >= a) & (st < a + win)).sum() / win for a in np.arange(0, LEN, win)}


# =============================================================== MUSIC
def music_cuesheet(dens):
    C, H, T, M, W = ("curious_neutral_Dmaj_96bpm", "historic_nostalgic_Gmaj_84bpm_3-4",
                     "tension_braindrain_Bmin_92bpm", "momentum_building_Dmaj_108bpm", "warm_resolve_Dmaj_80bpm")
    segs = []

    def thin(cue, s, e, anchor, fade_in, fade_out, dense_stems=("marimba", "pad"), full=None, li0=False, **kw):
        """Split a loop-cue segment at 10 s windows; dense narration (>=3.3 words/s) drops the pizz."""
        cuts = [s] + [a for a in np.arange(np.ceil(s / 10) * 10, e, 10)] + [e]
        parts = []
        for a, b in zip(cuts, cuts[1:]):
            d = dens.get(float(np.floor(a / 10) * 10), 0)
            st = list(dense_stems) if d >= 3.3 else full
            if parts and parts[-1][2] == st:
                parts[-1][1] = b
            else:
                parts.append([a, b, st])
        for i, (a, b, st) in enumerate(parts):
            seg = dict(cue=cue, start=round(float(a), 3), end=round(float(b), 3), anchor=anchor,
                       fade_in=fade_in if i == 0 else 1.0, fade_out=fade_out if i == len(parts) - 1 else 1.0,
                       linear_in=i > 0 or li0, linear_out=i < len(parts) - 1, **kw)
            if st:
                seg["stems"] = st
            segs.append(seg)

    # Act 0 + I --------------------------------------------------------------------------
    segs.append(dict(cue=C, start=0.0, end=4.32, anchor=4.32, stems=["pad"], fade_in=1.6, fade_out=0.1,
                     linear_out=True, note="cold open: held pad (A chord of the loop's last bar resolving to D)"))
    thin(C, 4.32, 62.49, 4.32, 0.1, 0.15, li0=True, note="Act I: marimba enters on the downbeat at 4.32")
    segs[-1]["linear_out"] = True
    segs.append(dict(cue=C, start=62.49, end=63.21, anchor=4.32, stems=["pad"], fade_in=0.15, fade_out=1.2,
                     linear_in=True, note="'completely flipped': marimba drops out"))
    segs.append(dict(cue="stinger_reveal_Dmaj", start=35.36 - 1.30, end=35.36 + 6.0, overlay=True, gain_db=-6.0,
                     note="West burn reveal (hit at 35.36)"))
    # Act II -----------------------------------------------------------------------------
    thin(H, 63.21, 99.0, 63.21, 0.2, 6.0, note="Act II: sepia nostalgia")
    segs.append(dict(cue=T, start=97.53, end=122.98, anchor=93.53, fade_in=8.0, fade_out=3.0,
                     note="brain drain creeps in from 93.53"))
    # Act III ----------------------------------------------------------------------------
    thin(C, 122.98, 214.67, 122.98, 3.0, 2.0, note="Act III: Hoover storytelling")
    segs.append(dict(cue="stinger_soft_rise_Dmaj", start=157.22, end=162.2, overlay=True, gain_db=-4.0,
                     note="'Hoover gets in'"))
    thin(H, 214.67, 249.0, 214.67, 2.0, 2.0, dense_stems=("marimba", "pad"), full=["marimba", "pizz", "pad"],
         stem_gain_db={"pad": 3.0}, note="Founding Grant / money: strings forward")
    segs.append(dict(cue=C, start=249.0, end=268.0, anchor=249.0, stems=["marimba", "pad"], fade_in=2.0, fade_out=1.0,
                     linear_out=True, note="gentle build through the GSB"))
    thin(C, 268.0, 286.84, 249.0, 1.0, 1.0, li0=True, note="build, settles on 'a good start'")
    segs.append(dict(cue="stinger_soft_rise_Dmaj", start=286.84, end=291.8, overlay=True, gain_db=-3.0,
                     note="cadence on 'a good start'"))
    # Act IV -----------------------------------------------------------------------------
    segs.append(dict(cue=C, start=287.56, end=346.07, anchor=287.56, stems=["marimba", "pizz"],
                     stem_gain_db={"pizz": -6.0}, fade_in=0.1, fade_out=2.0, note="Terman motif: marimba, light pizz"))
    # Act V ------------------------------------------------------------------------------
    segs.append(dict(cue=M, start=346.07, end=474.95, offset=8.889, fade_in=0.1, fade_out=1.5,
                     note="'already had a Silicon Valley': momentum from bar 5 (cello at 355)"))
    segs.append(dict(cue=W, start=474.95, end=491.48, anchor=474.95, stems=["pad", "marimba"],
                     stem_gain_db={"marimba": -9.0}, fade_in=1.5, fade_out=2.0, note="'mind palace': pull back to pad"))
    # Act VI -----------------------------------------------------------------------------
    segs.append(dict(cue=T, start=491.48, end=504.92, anchor=491.48, stems=["pad", "marimba"], fade_in=2.0,
                     fade_out=1.0, note="heartbreak: minor dip, pad + sparse marimba"))
    segs.append(dict(cue="stinger_reveal_Dmaj", start=505.96 - 1.30, end=505.96 + 6.0, overlay=True, gain_db=-3.0,
                     note="turn on '1938'"))
    segs.append(dict(cue=M, start=505.96, end=600.0, offset=0.0, fade_in=0.1, fade_out=0.0,
                     note="the plan: momentum builds; cliffhanger fade 598.87-600 applied in post"))
    return {"length": LEN, "xfade": 2.0, "segments": segs}


def comic_pluck(t0=143.94):
    """Two-note violin pizz 'plink-plonk' on 'fails' (D6 then A5)."""
    ir = make_ir(rt60=1.4, seed=31)
    y = np.zeros(int(1.5 * SR))
    for dt, m, v in [(0.0, 86, 0.8), (0.16, 81, 0.6)]:
        p = pizz(m, v, "violin", np.random.default_rng(m), t60=0.5)
        i = int(dt * SR)
        y[i:i + len(p)] += p[: len(y) - i]
    st = reverb(np.stack([y * 0.8, y], 1), ir, 0.2)
    return st * db(-12) / np.abs(st).max(), t0


def build_music(act, pauses, dens):
    os.makedirs(BED, exist_ok=True)
    sheet = music_cuesheet(dens)
    sp = os.path.join(BED, "music_cuesheet.json")
    json.dump(sheet, open(sp, "w"), indent=1)
    raw = os.path.join(tempfile.gettempdir(), "music_bed_raw.wav")
    subprocess.run([PY, os.path.join(HERE, "build_bed.py"), sp, raw], check=True)
    x, _ = sf.read(raw, always_2d=True)
    x = x[:N]
    pl, t0 = comic_pluck()
    i = int(t0 * SR)
    x[i:i + len(pl)] += pl[: N - i]

    # ---- speech envelope s(t) 0..1 (attack 50 ms, release 300 ms), 20 ms frames -> samples
    fr = act.astype(float)
    s = np.zeros_like(fr)
    for k in range(len(fr)):
        prev = s[k - 1] if k else 0.0
        c = 0.02 / (0.05 if fr[k] > prev else 0.30)
        s[k] = prev + (fr[k] - prev) * min(c, 1.0)
    tf = np.arange(len(s)) * 0.02 + 0.01
    ts = np.arange(N) / SR
    s_smp = np.interp(ts, tf, s)

    # ---- dynamic carve: extra -3 dB @2.5 kHz, -2 dB @1 kHz while the voice speaks
    carved = peaking(peaking(x, 2500, -3.0, 0.8), 1000, -2.0, 1.0)
    x = x * (1 - s_smp[:, None]) + carved * s_smp[:, None]

    # ---- volume envelope: lift in VO pauses, small trim in dense windows, cliffhanger fade
    pts = [(0.0, 0.0)]
    for a, b in pauses:
        L = b - a
        if a < 0.5 or b > 599.6:
            continue
        lift = 3.0 if L >= 1.2 else 1.5
        r = min(0.6, max(0.1, (L - 0.45) / 2))
        up, dn = a + 0.15 + r, b - 0.3
        if dn <= up:
            up = dn = (a + b) / 2
        pts += [(a + 0.15, 0.0), (up, lift), (dn, lift), (b - 0.05, 0.0)]
    pts.append((LEN, 0.0))
    pts.sort()
    lift = np.interp(ts, [p[0] for p in pts], [p[1] for p in pts])
    trim = np.zeros(N)
    for a, d in dens.items():
        if d >= 3.3:
            trim[int(a * SR):int(min(a + 10, LEN) * SR)] = -1.0
    k = int(2.0 * SR)
    trim = np.convolve(trim, np.ones(k) / k, "same")
    g = db(lift + trim)
    x = x * g[:, None]
    fo0, fo1 = int(598.87 * SR), N
    x[fo0:fo1] *= np.cos(0.5 * np.pi * np.arange(fo1 - fo0) / (fo1 - fo0))[:, None] ** 2
    # ---- final level
    x *= db(MUSIC_TARGET - integrated_lufs(x))
    pk = np.abs(x).max()
    out = os.path.join(BED, "music_bed_600s.wav")
    sf.write(out, x, SR, subtype="PCM_24")
    print(f"music: {out}  LUFS {integrated_lufs(x):.1f}  peak {20*np.log10(pk):.1f} dBFS  pauses lifted: {len(pauses)}")
    return x, s_smp


def speech_env(act):
    """0..1 speech envelope per sample (attack 50 ms, release 300 ms) from the 20 ms VO activity frames."""
    fr = act.astype(float)
    s = np.zeros_like(fr)
    for k in range(len(fr)):
        prev = s[k - 1] if k else 0.0
        c = 0.02 / (0.05 if fr[k] > prev else 0.30)
        s[k] = prev + (fr[k] - prev) * min(c, 1.0)
    tf = np.arange(len(s)) * 0.02 + 0.01
    return np.interp(np.arange(N) / SR, tf, s)


def build_music_epidemic(sheet, act, pauses):
    """Layered Epidemic bed (MANUAL §10.3): sum the cue-sheet layers, frequency pocket in the voice band while he speaks
    (§10.8: −4.5 dB @ 2.5 kHz, −2.5 dB @ 1.2 kHz), small lifts in VO pauses ≥ 0.6 s, normalise to VO − bed_lu_under_vo,
    then add the stingers. Writes <out>/music_bed.wav + music_report.json."""
    import epidemic_bed as E
    os.makedirs(BED, exist_ok=True)
    x, rep = E.build_layers(sheet, LEN, VO_LUFS)
    s_smp = speech_env(act)
    carved = peaking(peaking(x, 2500, -4.5, 0.7), 1200, -2.5, 1.0)
    x = x * (1 - s_smp[:, None]) + carved * s_smp[:, None]
    del carved
    ts = np.arange(N) / SR
    pts = [(0.0, 0.0)]
    for a, b in pauses:
        L = b - a
        if a < 0.5 or b > LEN - 0.4:
            continue
        lift = 2.5 if L >= 1.2 else 1.5
        r = min(0.5, max(0.1, (L - 0.45) / 2))
        up, dn = a + 0.15 + r, b - 0.3
        if dn <= up:
            up = dn = (a + b) / 2
        pts += [(a + 0.15, 0.0), (up, lift), (dn, lift), (b - 0.05, 0.0)]
    pts.append((LEN, 0.0))
    pts.sort()
    x = x * db(np.interp(ts, [p[0] for p in pts], [p[1] for p in pts]))[:, None]
    target = VO_LUFS - float(sheet.get("bed_lu_under_vo", 14.0))
    x *= db(target - integrated_lufs(x))
    x = E.place_stingers(sheet, x, LEN, VO_LUFS, target)
    pk = np.abs(x).max()
    if pk > db(-1.0):
        x *= db(-1.0) / pk
    out = os.path.join(BED, "music_bed.wav")
    sf.write(out, x, SR, subtype="PCM_24")
    json.dump(dict(vo_lufs=VO_LUFS, target_lufs=target, layers=rep, pauses_lifted=len(pauses)),
              open(os.path.join(BED, "music_report.json"), "w"), indent=1)
    print(f"music: {out}  LUFS {integrated_lufs(x):.1f} (target {target:.1f})  peak {20*np.log10(np.abs(x).max()):.1f} dBFS"
          f"  layers {len(rep)}")
    return x, s_smp


# =============================================================== SFX
LIB = os.path.join(AUDIO, "sfx")
_cache = {}


def lib(name):
    if name not in _cache:
        y, _ = sf.read(os.path.join(LIB, name + ".wav"), always_2d=True)
        if y.shape[1] == 1:
            y = np.repeat(y, 2, 1)
        _cache[name] = y
    return _cache[name]


def st(y):
    y = np.asarray(y, float)
    return np.stack([y, y], 1) if y.ndim == 1 else y


def onset(y):
    a = np.abs(y).max(1)
    return np.argmax(a > a.max() * db(-10)) / SR


def loudest(y):
    a = np.abs(y).max(1) ** 2
    w = int(0.01 * SR)
    return np.argmax(np.convolve(a, np.ones(w), "same")) / SR


def trimfit(y, dur, fout=0.05):
    k = min(len(y), int((dur + fout) * SR))
    return fade(y[:k], 0.0, fout)


# linear gains for -6 dBFS-peak sounds (MIX_RULES section 3): (soft, normal)
GAIN = {
    "pop_soft": (0.045, 0.056), "pin_pop": (0.06, 0.08), "map_pin": (0.06, 0.08), "cork_pin": (0.06, 0.08),
    "tick_soft": (0.04, 0.05), "odometer_tick": (0.045, 0.056), "counter_ticks": (0.04, 0.05),
    "letter_ticks": (0.035, 0.045), "dot_ticks": (0.035, 0.045), "dot_slide": (0.05, 0.065),
    "paper_slide": (0.06, 0.08), "paper_rustle": (0.05, 0.07), "paper_flip": (0.06, 0.08), "page_turn": (0.06, 0.08),
    "paper_tear": (0.06, 0.08), "marker_scratch": (0.06, 0.08), "marker_long": (0.06, 0.08),
    "highlighter_swipe": (0.06, 0.08), "pencil_scribble": (0.05, 0.07), "string_pull": (0.05, 0.065),
    "stamp_thud": (0.10, 0.14), "whoosh_soft": (0.06, 0.08), "whoosh": (0.08, 0.10), "whoosh_big": (0.10, 0.12),
    "air_swell": (0.06, 0.08), "shutter": (0.09, 0.11), "projector_click": (0.06, 0.08), "film_burn": (0.07, 0.09),
    "burn_crackle": (0.08, 0.10), "crt_click": (0.07, 0.09), "crt_off": (0.06, 0.08), "boom_low": (0.14, 0.18),
    "lamp_click": (0.06, 0.08), "gate_creak": (0.05, 0.07), "chime_soft": (0.05, 0.07), "tone_blip": (0.025, 0.03),
    # Epidemic-era types (SOUND_PLAN §4)
    "whip": (0.08, 0.10), "riser": (0.07, 0.09), "phone_ring": (0.05, 0.07), "phone_dial": (0.05, 0.07),
    "plane_pass": (0.08, 0.10), "teletype": (0.05, 0.07), "focus_hunt": (0.05, 0.065),
    "circuit_clunk": (0.08, 0.10),
}
LOWTYPES = {"boom_low", "stamp_thud"}
SFX_TRIM_DB = -3.0   # this VO is quiet (speech peaks ~ -16 dBFS): trims the table so SFX sit ~20 dB under local VO peaks
AMBTYPES = {"projector_loop", "crt_hum", "wind", "factory_hum", "crowd_room"}


def epi(name, start=0.0, dur=None):
    import epidemic_bed as E
    return E.read_window(E.sfx_path(name), start, dur)


def render_epidemic(m, i, rng):
    """Epidemic Sound SFX for the new types (and better booms). None = fall through to the synthesized library."""
    ty, d, note = m["type"], m.get("dur"), m.get("note", "").lower()
    seed = 20000 + i
    if ty == "whip":
        nm = ["whoosh_swoosh_light", "whoosh_swoosh_wide", "whoosh_soft"][i % 3]
        y = epi(nm)
        low = st(G.whoosh(0.5, seed, 150, 1200, 0.6))          # §10.8: a LOW whoosh under every move
        lk = loudest(y)
        buf = np.zeros((max(len(y), len(low) + int(max(0.0, lk - loudest(low)) * SR)) + 10, 2))
        buf[:len(y)] += y / (np.abs(y).max() + 1e-9)
        o = int(max(0.0, lk - loudest(low)) * SR)
        buf[o:o + len(low)] += 0.5 * low / (np.abs(low).max() + 1e-9)
        return buf, lk, f"epi:{nm} + low whoosh gen#{seed}"
    if ty == "boom_low":
        if any(k in note for k in ("morris", "biggest", "seismic")):
            nm = "boom_dark_cinematic_low_hit"
        elif any(k in note for k in ("condition", "'one'", "tsmc", "superpower", "slams", "industrialists",
                                     "export processing", "chiang")):
            nm = "boom_cinematic_deep"
        elif any(k in note for k in ("died", "sub only")):
            nm = "boom_sub_bass_clean_01"
        else:
            return None
        y = epi(nm, 0.0, 4.0 if nm == "boom_sub_bass_clean_01" else None)
        y = fade(y, 0.0, 1.0)
        return y, onset(y), f"epi:{nm}"
    if ty == "riser":
        y = epi("riser_reverse_cymbal_short")
        return y, loudest(y), "epi:riser_reverse_cymbal_short (ends on t)"
    if ty == "phone_ring":
        nm = "phone_ring_04"
        y = epi(nm)
        o = onset(y)
        y = fade(y[int(o * SR):int((o + 2.2) * SR)], 0.0, 0.4)
        return y, 0.0, f"epi:{nm} (one ring)"
    if ty == "phone_dial":
        y = fade(epi("phone_pushbutton_dial_pickup", float(rng.uniform(5, 40)), d or 1.0), 0.01, 0.1)
        return y, 0.0, "epi:phone_pushbutton_dial_pickup (excerpt)"
    if ty == "plane_pass":
        nm = "jet_pass_overhead_01" if i % 2 == 0 else "jet_pass_long_distant"
        full = epi(nm)
        lk = loudest(full)
        span = max(d or 1.0, 1.0) + 5.0
        a = max(0.0, lk - span / 2)
        y = fade(full[int(a * SR):int((a + span) * SR)], 1.5, 1.5)
        return y, (lk - a) - (d or 1.0) / 2, f"epi:{nm} (peak mid-move)"
    if ty == "teletype":
        y = fade(epi("telegraph_antique", 2.0, d or 2.0), 0.05, 0.3)
        return y, 0.0, "epi:telegraph_antique"
    if ty == "focus_hunt":
        nm = ["camera_focus_nikon_d3100", "lens_autofocus_f4_01", "lens_autofocus_f4_03"][i % 3]
        y = epi(nm)
        return y, onset(y), f"epi:{nm}"
    if ty == "paper_slide" and m.get("level") == "normal" and "drop" not in note:
        nm = ["paper_slide_wood_table", "paper_slide_wood_table_04"][i % 2]
        y = epi(nm)
        return y, onset(y), f"epi:{nm}"
    return None


def rate_shift(y, semis):
    """Pitch/rate variation (§10.8: never the same sample twice in a row)."""
    r = 2 ** (semis / 12)
    n = int(len(y) / r)
    xi = np.arange(n) * r
    return np.stack([np.interp(xi, np.arange(len(y)), y[:, c]) for c in range(y.shape[1])], 1)


def render_event(m, i, rng, wdir):
    """Return (stereo sound, seconds from file start to the sync point, label)."""
    t, ty, d, note = m["t"], m["type"], m.get("dur"), m.get("note", "").lower()
    seed = 10000 + i
    if EPIDEMIC:
        r = render_epidemic(m, i, rng)
        if r is not None:
            return r
    if ty in ("whoosh_soft", "whoosh", "whoosh_big"):
        base = {"whoosh_soft": (0.45, 400, 3000, 0.55), "whoosh": (0.8, 300, 2600, 0.62),
                "whoosh_big": (1.3, 220, 2200, 0.65)}[ty]
        dur = max(0.3, min(d or base[0], 2.0))
        y = G.whoosh(dur, seed, base[1], base[2], base[3])
        if wdir:
            y = y[:, ::-1]
        mp = re.search(r"peaks? at (?:the cut )?(\d+\.\d+)", m.get("note", ""))
        if mp:
            return y, loudest(y) - (float(mp.group(1)) - t), f"whoosh {dur:.2f}s gen#{seed} peak@{mp.group(1)}"
        if d:
            return y, 0.0, f"whoosh {dur:.2f}s gen#{seed} spans move"
        lead = {"whoosh_soft": 0.12, "whoosh": 0.25, "whoosh_big": 0.35}[ty]
        return y, loudest(y) - lead, f"whoosh {dur:.2f}s gen#{seed}"
    if ty == "air_swell":
        dur = max(0.6, d or 1.5)
        return G.air_swell(seed, dur), 0.0, f"air_swell {dur:.1f}s gen#{seed}"
    if ty == "paper_slide":
        if "drop" in note:
            y = G.photo_drop(seed)
            return y, onset(y), f"photo_drop gen#{seed}"
        y = G.paper_slide(seed, float(rng.uniform(0.5, 0.75)))
        return y, 0.1, f"paper_slide gen#{seed}"
    if ty == "paper_rustle":
        y = G.paper_rustle(seed, max(0.6, d or float(rng.uniform(0.7, 1.0))))
        return y, 0.0, f"paper_rustle gen#{seed}"
    if ty in ("paper_flip", "page_turn"):
        nm = f"kenney_paper_page_flip_0{1 + i % 3}"
        y = lib(nm)
        return y, onset(y), nm
    if ty == "paper_tear":
        y = G.paper_tear(seed, 0.4)
        return y, onset(y), f"paper_tear gen#{seed}"
    if ty == "pop_soft":
        if i % 4 == 3:
            nm = ["kenney_ui_pluck_01", "kenney_ui_drop_pop_01", "kenney_ui_drop_pop_02"][i % 3]
            y = lib(nm)
            return y, onset(y), nm
        f0 = float(rng.uniform(440, 700))
        y = G.ui_pop(seed, f0, f0 * rng.uniform(1.35, 1.6))
        return y, onset(y), f"ui_pop gen#{seed}"
    if ty == "pin_pop":
        f0 = float(rng.uniform(850, 1300))
        y = G.pop(seed, f0, f0 * rng.uniform(0.3, 0.38))
        return y, onset(y), f"map_pin_pop gen#{seed}"
    if ty == "map_pin":
        y = G.pin_drop(seed)
        return y, onset(y), f"map_pin_drop gen#{seed}"
    if ty == "cork_pin":
        y = G.cork_pin(seed)
        return y, onset(y), f"cork_pin gen#{seed}"
    if ty == "string_pull":
        y = G.string_pull(seed, d or 0.35)
        return y, 0.0, f"string_pull gen#{seed}"
    if ty in ("marker_scratch", "marker_long"):
        dur = d or (0.5 if ty == "marker_scratch" else 1.2)
        if "arrow" in note and dur >= 0.5:
            y = G.marker(seed, [(0.0, dur * 0.65), (dur * 0.72, dur * 0.12), (dur * 0.86, dur * 0.12)])
        elif "circle" in note or "loop" in note:
            y = G.marker(seed, [(0.0, dur)])
        else:
            y = G.marker(seed, [(0.0, dur)])
        return y, 0.0, f"marker {dur:.2f}s gen#{seed}"
    if ty == "highlighter_swipe":
        y = G.highlighter(seed, d or float(rng.uniform(0.45, 0.6)))
        return y, 0.0, f"highlighter gen#{seed}"
    if ty == "pencil_scribble":
        y = G.pencil(seed, d or 0.7)
        return y, 0.0, f"pencil {d or 0.7:.2f}s gen#{seed}"
    if ty == "stamp_thud":
        y = G.stamp(seed)
        return y, onset(y), f"stamp_thud gen#{seed}"
    if ty == "tick_soft":
        if i % 3 == 2:
            nm = ["kenney_ui_tick_03", "kenney_ui_tick_04"][i % 2]
            y = lib(nm)
            return y, onset(y), nm
        y = G.ui_tick(seed, float(rng.uniform(1400, 2200)))
        return y, onset(y), f"ui_tick gen#{seed}"
    if ty in ("odometer_tick", "counter_ticks"):
        dur = d or 0.8
        y = G.ticker_roll(dur, 30 if ty == "counter_ticks" else 24, 5, seed)
        return y, 0.0, f"ticker_roll_decel {dur:.2f}s gen#{seed}"
    if ty in ("letter_ticks", "dot_ticks"):
        dur = d or (0.6 if ty == "letter_ticks" else 1.5)
        rate = 16 if ty == "letter_ticks" else 8
        y = np.zeros((int((dur + 0.3) * SR), 2))
        tt = 0.0
        while tt < dur:
            tk = st(G.tick(seed + int(tt * 1000), f=float(rng.uniform(800, 1000)))) if ty == "letter_ticks" \
                else G.ui_tick(seed + int(tt * 1000), float(rng.uniform(1700, 2300)))
            G.put(y, tk, tt, float(rng.uniform(0.6, 1.0)))
            tt += 1 / rate * rng.uniform(0.8, 1.2)
        return y, 0.0, f"{ty} x{int(dur*rate)} gen#{seed}"
    if ty == "dot_slide":
        dur = d or 0.5
        y = np.zeros((int((dur + 0.5) * SR), 2))
        G.put(y, G.pencil(seed, dur) * 0.5, 0.0)
        G.put(y, G.ui_pop(seed, 600, 880), dur, 0.8)
        return y, 0.0, f"dot_slide {dur:.2f}s gen#{seed}"
    if ty == "shutter":
        nm = ["camera_shutter_mech", "camera_shutter_mech_02", "camera_shutter_mech_03"][i % 3]
        y = lib(nm)
        return y, onset(y), nm
    if ty == "projector_click":
        y = G.projector_click(seed)
        return y, onset(y), f"projector_click gen#{seed}"
    if ty in ("film_burn", "burn_crackle"):
        dur = max(1.0, d or 1.5)
        y = G.fire(dur, seed)
        return y, 0.0, f"fire {dur:.1f}s gen#{seed}"
    if ty == "crt_click":
        y = lib("crt_click")
        return y, onset(y), "crt_click"
    if ty == "crt_off":
        y = lib("crt_power_off")
        return y, onset(y), "crt_power_off"
    if ty == "boom_low":
        y = G.impact(seed, 1.6, 70, 42, 0.4) if m.get("level") != "normal" else G.impact(seed, 2.6, 58, 32, 0.6)
        return y, onset(y), f"impact_low gen#{seed}"
    if ty == "lamp_click":
        nm = ["kenney_switch_click", "kenney_metal_click"][i % 2]
        y = lib(nm)
        return y, onset(y), nm
    if ty == "gate_creak":
        y = lib("kenney_gate_creak_01")
        return y, 0.0, "kenney_gate_creak_01"
    if ty == "circuit_clunk":          # contrast veil / call-out: heavy switch latch over a short low thump
        lat = st(lib(["kenney_metal_latch", "kenney_switch_click"][i % 2]))
        th = st(G.impact(seed, 0.5, 90, 55, 0.3))
        y = np.zeros((max(len(lat), len(th)), 2))
        y[:len(lat)] += lat / (np.abs(lat).max() + 1e-9)
        y[:len(th)] += 0.6 * th / (np.abs(th).max() + 1e-9)
        return y, onset(y), f"circuit_clunk gen#{seed}"
    if ty == "chime_soft":
        y = lib("chime_soft")
        return y, onset(y), "chime_soft"
    if ty == "tone_blip":
        mf = re.search(r"(\d+)\s*hz", note)
        f = float(mf.group(1)) if mf else 880.0
        y = G.tone_blip(seed, f)
        y = trimfit(y, d or 0.2, 0.04)
        return y, onset(y), f"tone_blip {f:.0f} Hz"
    raise KeyError(ty)


def build_sfx_and_amb(markers, scenes, act, vo):
    vabs = np.abs(vo).max(1)
    sfx = np.zeros((N, 2))
    low = np.zeros((N, 2))
    amb = np.zeros((N, 2))
    rng = np.random.default_rng(2026)
    log = []
    wdir = False
    last_files = []
    for i, m in enumerate(markers):
        ty = m["type"]
        quiet = any(k in m.get("note", "").lower() for k in ("very quiet", "very soft", "very low"))
        if ty in AMBTYPES:
            continue
        if ty.startswith("whoosh"):
            nt = m.get("note", "").lower()
            wdir = True if ("left" in nt and "right" not in nt) else (False if "right" in nt else not wdir)
        y, sync, label = render_event(m, i, rng, wdir and ty.startswith("whoosh"))
        y = st(y)
        if EPIDEMIC and "gen#" not in label:
            base = label.split(" ")[0]
            if base in last_files[-2:]:
                semis = float(rng.choice([-1, 1]) * rng.uniform(1.0, 3.0))
                y = rate_shift(y, semis)
                sync /= 2 ** (semis / 12)
                label += f" ({semis:+.1f} st)"
            last_files.append(base)
        y = peak_norm(y, -6.0)
        g = GAIN[ty][1 if m.get("level") == "normal" else 0] * (db(-6) if quiet else 1.0) * db(SFX_TRIM_DB)
        if ty not in LOWTYPES:
            y = hp(y, 100, 2)
        start = m["t"] - sync
        # cap: SFX peak stays >= 20 dB under the VO's local peak (14 dB for sub-heavy hits);
        # in VO pauses the cap is an absolute -30 dBFS (-24 for sub hits)
        a0, a1 = max(int((start - 0.3) * SR), 0), min(int((start + len(y) / SR + 0.3) * SR), len(vabs))
        vloc = vabs[a0:a1].max() if a1 > a0 else 0.0
        rel, floor = (-14.0, -24.0) if ty in LOWTYPES else (-20.0, -30.0)
        if EPIDEMIC:   # §10.8: SFX −10…−20 dB under the VO by importance (hero/normal vs the rest)
            hero = m.get("level") == "normal" or ty in ("boom_low", "riser", "plane_pass")
            rel = (-10.0 if hero else -14.0) if ty in LOWTYPES else (-12.0 if hero else -18.0)
        allowed = max(vloc * db(rel), db(floor)) if vloc > db(-30) else db(floor)
        pk = np.abs(y).max() * g
        if pk > allowed:
            g *= allowed / pk
        i0 = int(round(start * SR))
        if i0 < 0:
            y = y[-i0:]
            i0 = 0
        k = min(len(y), N - i0)
        (low if ty in LOWTYPES else sfx)[i0:i0 + k] += g * y[:k]
        log.append(dict(t=m["t"], type=ty, scene=m.get("scene"), sound=label, start=round(start, 4),
                        sync_offset=round(sync, 4), gain=round(g, 4), gain_db=round(20 * np.log10(g), 1)))
    sfx = peaking(sfx, 2500, -2.0, 0.8) + low          # SFX bus: soften the voice band a touch
    sfx = fade(sfx, 0.0, 0.02)

    # ---------------- ambience
    def loop_seg(name, t0, t1, gain, fin=0.4, fout=0.6, off=None):
        y = lib(name)
        n = int((t1 - t0) * SR)
        if n <= 0:
            return
        o = int((off if off is not None else rng.uniform(0, len(y) / SR)) * SR) % len(y)
        seg = np.tile(y, (int(np.ceil((n + o) / len(y))) + 1, 1))[o:o + n]
        seg = fade(seg, min(fin, (t1 - t0) / 3), min(fout, (t1 - t0) / 3))
        i0 = int(t0 * SR)
        amb[i0:i0 + n] += gain * seg[: N - i0]

    amb_log = []
    for m in markers:
        if m["type"] not in AMBTYPES:
            continue
        d = m.get("dur", 2.0)
        quiet = any(k in m.get("note", "").lower() for k in ("very quiet", "very soft", "very low"))
        if m["type"] == "projector_loop":
            g = 0.06 * (db(-6) if quiet else 1.0)
            loop_seg("projector_loop_8s", m["t"], m["t"] + d, g, 0.15, min(0.5, d / 3))
        elif m["type"] == "crt_hum":
            g = 0.009
            loop_seg("crt_hum_loop_6s", m["t"], m["t"] + d, g, 0.2, 0.3)
        elif m["type"] in ("factory_hum", "crowd_room"):
            n_ = m.get("note", "").lower()
            if m["type"] == "factory_hum":
                nm = "factory_machine_room_electronics_hum" if any(k in n_ for k in ("fab", "cleanroom", "microscope")) \
                    else "factory_hum_light_activity_01"
                rel = -26.0
            else:
                nm = "restaurant_crowded_distant_01" if any(k in n_ for k in ("restaurant", "dinner")) \
                    else "office_aircon_people_quiet"
                rel = -25.0
            y = epi(nm, float(rng.uniform(5, 40)), d + 0.6)
            g = db(VO_LUFS + rel - integrated_lufs(y)) * (db(-4) if quiet else 1.0)   # felt, not heard (≈ −50 LUFS)
            y = fade(y, min(0.8, d / 3), min(1.2, d / 3))
            i0 = int(m["t"] * SR)
            k_ = min(len(y), N - i0)
            amb[i0:i0 + k_] += g * y[:k_]
            g = round(float(g), 4)
            amb_log.append(dict(t=m["t"], type=m["type"], dur=d, gain=g, file=nm))
            continue
        else:
            g = 0.05 if d < 3 else 0.035
            loop_seg("wind_air_loop_30s", m["t"], m["t"] + d, g, min(0.6, d / 3), min(0.8, d / 3))
        amb_log.append(dict(t=m["t"], type=m["type"], dur=d, gain=g))
    # room tone everywhere (paper scenes a touch more), vinyl under old-footage scenes, wind under cloud scenes
    for sc in scenes:
        a, b, kind, tags = sc
        loop_seg("room_tone_loop_30s", a, b, 0.011 if kind == "PAPER" else 0.008, 0.5, 0.5, off=a % 30)
        if {"sepia", "weave"} & tags:
            loop_seg("vinyl_crackle_loop_30s", a, b, 0.10, 0.8, 0.8)
            amb_log.append(dict(t=a, type="vinyl_bed", dur=round(b - a, 2), gain=0.10))
        if "cloud" in tags:
            loop_seg("wind_air_loop_30s", a, b, 0.03, 1.0, 1.0)
            amb_log.append(dict(t=a, type="wind_bed", dur=round(b - a, 2), gain=0.03))
    amb = fade(amb, 0.5, 1.2)
    for nm, x in ((f"sfx{SUFFIX}.wav", sfx), (f"ambience{SUFFIX}.wav", amb)):
        sf.write(os.path.join(BED, nm), x, SR, subtype="PCM_24")
        print(f"{nm}: peak {20*np.log10(np.abs(x).max()+1e-12):.1f} dBFS  LUFS {integrated_lufs(x):.1f}")
    json.dump({"sfx": log, "ambience": amb_log}, open(os.path.join(BED, "sfx_placements.json"), "w"), indent=1)
    return sfx, amb, log


def scenes_from_notes():
    s = open(os.path.join(ROOT, "EDIT_NOTES.md")).read()
    out = []
    for p in re.split(r"\n(?=### SC\d+)", s)[1:]:
        h = p.split("\n")[0]
        mt = re.search(r"·\s*([\d.]+)[–-]([\d.]+)\s*·[^·]*·\s*([A-Z]+)", h)
        if not mt:
            continue
        low = p.lower()
        tags = {k for k in ("sepia", "weave", "cloud") if k in low}
        out.append((float(mt.group(1)), float(mt.group(2)), mt.group(3), tags))
    return out


def measure_lufs(path):
    r = subprocess.run([FFMPEG, "-hide_banner", "-nostats", "-i", path, "-af", "ebur128", "-f", "null", "-"],
                       capture_output=True, text=True).stderr
    return float([l for l in r.splitlines() if l.strip().startswith("I:")][-1].split()[1])


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--vo", default="vo10.mp3")
    ap.add_argument("--transcript", default="transcript.json")
    ap.add_argument("--len", type=float, default=600.0)
    ap.add_argument("--markers", default="compositions/seg0*.sfx.json")
    ap.add_argument("--cues", default=None, help="JSON cue sheet of Epidemic layers (enables Epidemic mode)")
    ap.add_argument("--out", default="assets/audio/bed")
    ap.add_argument("--no-hierarchy", action="store_true", help="place every marker (skip the §10.8 restraint pass)")
    a = ap.parse_args()
    VO_FILE, WORDS_FILE, LEN = a.vo, a.transcript, a.len
    N = int(LEN * SR)
    BED = os.path.join(ROOT, a.out)
    os.makedirs(BED, exist_ok=True)
    EPIDEMIC = a.cues is not None
    markers = []
    for f in sorted(glob.glob(os.path.join(ROOT, a.markers))):
        markers += json.load(open(f))
    markers.sort(key=lambda m: m["t"])
    unknown = {m["type"] for m in markers} - set(GAIN) - AMBTYPES
    assert not unknown, unknown
    act, pauses, vo = vo_activity()
    if not EPIDEMIC:                                   # legacy 600 s edit
        dens = density_windows(words())
        build_music(act, pauses, dens)
        build_sfx_and_amb(markers, scenes_from_notes(), act, vo)
        tl = [dict(id=i, src=f"assets/audio/bed/{f}", start=0, duration=LEN, media_start=0, volume=1.0)
              for i, f in (("bed-music", "music_bed_600s.wav"), ("bed-sfx", "sfx_600s.wav"),
                           ("bed-amb", "ambience_600s.wav"))]
        json.dump(tl, open(os.path.join(AUDIO, "timeline.json"), "w"), indent=1)
        print(f"{len(markers)} markers placed; timeline.json written")
        sys.exit()
    SUFFIX = ""
    VO_LUFS = measure_lufs(os.path.join(ROOT, VO_FILE))
    SFX_TRIM_DB = -3.0 + (VO_LUFS + 27.2)          # the table was tuned for a −27.2 LUFS VO
    print(f"VO {VO_FILE}: {VO_LUFS:.1f} LUFS (measured, untouched); {len(markers)} markers; {len(pauses)} pauses")
    import epidemic_bed as E
    if not a.no_hierarchy:
        kept, dropped = E.hierarchy(markers)
        json.dump(dict(total=len(markers), kept=len(kept), dropped=dropped, kept_markers=kept),
                  open(os.path.join(BED, "sfx_hierarchy.json"), "w"), indent=1)
        print(f"hierarchy (§10.8): kept {len(kept)} / {len(markers)} markers, dropped {len(dropped)}")
        markers = kept
    sheet = json.load(open(os.path.join(ROOT, a.cues)))
    build_music_epidemic(sheet, act, pauses)
    build_sfx_and_amb(markers, [(0.0, LEN, "PAPER", set())], act, vo)
    rel = os.path.relpath(BED, ROOT)
    tl = [dict(id=i, src=f"{rel}/{f}", start=0, duration=LEN, media_start=0, volume=1.0)
          for i, f in (("bed-music", "music_bed.wav"), ("bed-sfx", "sfx.wav"), ("bed-amb", "ambience.wav"))]
    json.dump(tl, open(os.path.join(BED, "timeline.json"), "w"), indent=1)
    print(f"{len(markers)} markers placed; {rel}/timeline.json written")
