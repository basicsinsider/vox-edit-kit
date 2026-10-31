"""Epidemic Sound helpers for place_sound.py (MANUAL §10.3, §10.8).

- read_window(): windowed, resampled reads of any WAV (never loads a whole 11-minute stem).
- build_layers(): sums the layers of a JSON cue sheet (project/intro/music_cuesheet.json) into one stereo bed.
- hierarchy(): the §10.8 restraint pass over the editors' SFX markers (hero event per scene + moves + ambience).
"""
import json
import os

import numpy as np
import soundfile as sf
from scipy.signal import resample_poly

from dsp import SR, AUDIO, db, fade

EPI = os.path.join(AUDIO, "epidemic")
_ANA = None


def analysis():
    global _ANA
    if _ANA is None:
        p = os.path.join(EPI, "ANALYSIS.json")
        _ANA = json.load(open(p)) if os.path.exists(p) else {}
    return _ANA


def read_window(path, start_s=0.0, dur_s=None):
    """Stereo float array at SR from path[start_s : start_s + dur_s] (dur None = to the end)."""
    info = sf.info(path)
    sr = info.samplerate
    a = max(0, int(round(start_s * sr)))
    frames = -1 if dur_s is None else max(0, int(round(dur_s * sr)) + 2)
    y, _ = sf.read(path, start=a, frames=frames, always_2d=True, dtype="float32")
    if y.shape[1] == 1:
        y = np.repeat(y, 2, 1)
    y = y[:, :2].astype(np.float64)
    if sr != SR and len(y):
        g = np.gcd(sr, SR)
        y = resample_poly(y, SR // g, sr // g, axis=0)
    if dur_s is not None:
        n = int(round(dur_s * SR))
        if len(y) < n:
            y = np.pad(y, ((0, n - len(y)), (0, 0)))
        y = y[:n]
    return y


def sfx_path(name):
    return os.path.join(EPI, "sfx", name + ".wav")


def stem_path(track, stem):
    return os.path.join(EPI, track, f"{track}_{stem}.wav")


def stem_lufs(track, stem):
    try:
        return analysis()[track]["stems"][stem]["lufs"]
    except KeyError:
        from loudness import integrated_lufs
        return integrated_lufs(read_window(stem_path(track, stem), 30.0, 60.0))


def _env(n, t0, auto):
    """dB envelope for a segment that starts at timeline t0 (auto points in timeline seconds)."""
    if not auto:
        return None
    ts = t0 + np.arange(n) / SR
    xs = [p[0] for p in auto]
    ys = [p[1] for p in auto]
    return db(np.interp(ts, xs, ys))


def build_layers(sheet, length, vo_lufs, log=print):
    """Sum every layer of the cue sheet. Returns (stereo bed, per-layer report)."""
    N = int(length * SR)
    bed = np.zeros((N, 2))
    rep = []
    for L in sheet["layers"]:
        s, e = float(L["start"]), min(float(L["end"]), length)
        if e <= s:
            continue
        p = stem_path(L["track"], L["stem"])
        if not os.path.exists(p):
            log(f"  !! missing {p} — layer skipped")
            continue
        y = read_window(p, float(L.get("offset", 0.0)), e - s)
        target = vo_lufs + float(L["rel_lu"])
        g_db = L.get("gain_db", target - stem_lufs(L["track"], L["stem"]))
        y = y * db(g_db)
        env = _env(len(y), s, L.get("auto"))
        if env is not None:
            y = y * env[:, None]
        y = fade(y, min(L.get("fade_in", 1.5), (e - s) / 2), min(L.get("fade_out", 1.5), (e - s) / 2))
        i0 = int(round(s * SR))
        k = min(len(y), N - i0)
        bed[i0:i0 + k] += y[:k]
        rep.append(dict(cue=L.get("cue"), layer=f"{L['track']}/{L['stem']}", start=s, end=e,
                        offset=L.get("offset", 0.0), gain_db=round(g_db, 1)))
    return bed, rep


def place_stingers(sheet, bed, length, vo_lufs, bed_lufs):
    """Stingers are mixed onto the (already normalised) bed, `rel_lu` relative to the VO, synced on their loudest point."""
    from loudness import integrated_lufs
    N = len(bed)
    for st in sheet.get("stingers", []):
        y = read_window(sfx_path(st["file"]))
        a = np.abs(y).max(1) ** 2
        w = int(0.02 * SR)
        pk = np.argmax(np.convolve(a, np.ones(w), "same")) / SR if st.get("sync", "loudest") == "loudest" else 0.0
        y = y * db(vo_lufs + st.get("rel_lu", -20) - integrated_lufs(y))
        i0 = int(round((st["t"] - pk) * SR))
        if i0 < 0:
            y, i0 = y[-i0:], 0
        k = min(len(y), N - i0)
        if k > 0:
            bed[i0:i0 + k] += fade(y[:k], 0.0, 0.05)
    return bed


# ---------------------------------------------------------------- §10.8 hierarchy & restraint
MOVES = {"whip", "whoosh_soft", "whoosh", "whoosh_big", "air_swell"}
AMB = {"projector_loop", "crt_hum", "wind", "factory_hum", "crowd_room"}
ALWAYS = {"boom_low", "riser", "plane_pass", "phone_ring", "teletype"}
RANK = {"boom_low": 10, "riser": 9, "stamp_thud": 8, "phone_ring": 8, "plane_pass": 8, "teletype": 7, "burn_crackle": 7,
        "film_burn": 7, "circuit_clunk": 6, "map_pin": 6, "paper_tear": 6, "highlighter_swipe": 6, "counter_ticks": 5, "odometer_tick": 5,
        "marker_long": 5, "paper_slide": 5, "phone_dial": 5, "pin_pop": 4, "marker_scratch": 4, "crt_click": 4,
        "crt_off": 4, "projector_click": 4, "shutter": 4, "focus_hunt": 4, "cork_pin": 4, "string_pull": 3,
        "lamp_click": 3, "gate_creak": 3, "paper_flip": 3, "page_turn": 3, "paper_rustle": 3, "pencil_scribble": 3,
        "chime_soft": 2, "dot_slide": 2, "dot_ticks": 2, "letter_ticks": 1, "pop_soft": 1, "tick_soft": 1, "tone_blip": 1}
TEXTURES = {"paper_slide", "paper_rustle", "paper_flip", "page_turn", "focus_hunt"}   # may stack on a move


def _score(m):
    s = RANK.get(m["type"], 2) + (1.5 if m.get("level") == "normal" else 0.0)
    n = m.get("note", "").lower()
    if any(k in n for k in ("hero", "biggest", "key number", "reveal")):
        s += 3
    if "optional" in n or "very low" in n:
        s -= 1
    return s


def hierarchy(markers, min_gap=0.25, per_scene_extra_every=6.0):
    """Keep: every move (whoosh/whip/swell), ambience, ALWAYS types; per scene the hero event (+1 more per 6 s of scene,
    ≥ 1.5 s apart); a texture within 0.3 s of a kept move (stacked on purpose). Then never two non-stacked hits within
    `min_gap` s, and no two moves within 0.35 s. Returns (kept, dropped-with-reasons)."""
    ms = sorted(markers, key=lambda m: m["t"])
    keep, drop = set(), {}
    for i, m in enumerate(ms):
        if m["type"] in MOVES | AMB | ALWAYS:
            keep.add(i)
    scenes = {}
    for i, m in enumerate(ms):
        scenes.setdefault(m.get("scene", "?"), []).append(i)
    for sc, idx in scenes.items():
        cand = [i for i in idx if i not in keep]
        if not cand:
            continue
        t0 = min(ms[i]["t"] for i in idx)
        t1 = max(ms[i]["t"] + ms[i].get("dur", 0) for i in idx)
        n_allow = 1 + int((t1 - t0) // per_scene_extra_every)
        big = [ms[i]["t"] for i in idx if ms[i]["type"] in ALWAYS]   # a boom/riser/plane carries its moment
        chosen = []
        for i in sorted(cand, key=lambda i: -_score(ms[i])):
            if len(chosen) >= n_allow:
                break
            if any(abs(ms[i]["t"] - b) < 1.0 for b in big):
                continue
            if all(abs(ms[i]["t"] - ms[j]["t"]) >= 1.5 for j in chosen):
                chosen.append(i)
        keep.update(chosen)
        for i in cand:
            if i not in chosen:
                # texture stacked on a kept move?
                if ms[i]["type"] in TEXTURES and any(
                        ms[j]["type"] in MOVES and abs(ms[j]["t"] - ms[i]["t"]) <= 0.3 for j in keep):
                    keep.add(i)
                else:
                    drop[i] = f"restraint: not the hero of {sc} (kept {', '.join(ms[j]['type'] for j in chosen)})"
    # collisions
    k = sorted(keep, key=lambda i: ms[i]["t"])
    final = []
    for i in k:
        m = ms[i]
        clash = None
        for j in final[-4:]:
            dt = abs(ms[j]["t"] - m["t"])
            both_moves = m["type"] in MOVES and ms[j]["type"] in MOVES
            layered = ((m["type"] in MOVES) != (ms[j]["type"] in MOVES) or {m["type"], ms[j]["type"]} & (AMB | {"riser"}))
            if (both_moves and dt < 0.35) or (not layered and dt < min_gap):
                clash = j
                break
        if clash is None:
            final.append(i)
            continue
        if _score(m) > _score(ms[clash]):
            final.remove(clash)
            drop[clash] = f"collision with {m['type']} @{m['t']}"
            final.append(i)
        else:
            drop[i] = f"collision with {ms[clash]['type']} @{ms[clash]['t']}"
    kept = [ms[i] for i in sorted(final, key=lambda i: ms[i]["t"])]
    dropped = [dict(ms[i], why=w) for i, w in sorted(drop.items(), key=lambda kv: ms[kv[0]]["t"]) if i not in final]
    return kept, dropped
