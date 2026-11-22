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
        p = os.path.join(EPI, L["file"]) if L.get("file") else stem_path(L["track"], L["stem"])   # "file": e.g. sfx/heartbeat_….wav
        if not os.path.exists(p):
            log(f"  !! missing {p} — layer skipped")
            continue
        y = read_window(p, float(L.get("offset", 0.0)), e - s)
        target = vo_lufs + float(L["rel_lu"])
        if L.get("file"):
            from loudness import integrated_lufs
            lu = integrated_lufs(read_window(p, float(L.get("offset", 0.0)), max(e - s, 3.0)))
        else:
            lu = stem_lufs(L["track"], L["stem"])
        g_db = L.get("gain_db", target - lu)
        y = y * db(g_db)
        env = _env(len(y), s, L.get("auto"))
        if env is not None:
            y = y * env[:, None]
        y = fade(y, min(L.get("fade_in", 1.5), (e - s) / 2), min(L.get("fade_out", 1.5), (e - s) / 2))
        i0 = int(round(s * SR))
        k = min(len(y), N - i0)
        bed[i0:i0 + k] += y[:k]
        rep.append(dict(cue=L.get("cue"), layer=L.get("file") or f"{L['track']}/{L['stem']}", start=s, end=e,
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
MOVES = {"whip", "whoosh_soft", "whoosh", "whoosh_big", "air_swell", "rewind"}
AMB = {"projector_loop", "crt_hum", "wind", "factory_hum", "crowd_room", "tube_hum", "city_night",
       "crowd_chant", "crowd_murmur", "newsroom",                      # Paraguay ambience types
       "stadium_walla", "night_insects", "sea", "wind_pines"}          # Cartels ambience types
ALWAYS = {"boom_low", "riser", "plane_pass", "phone_ring", "teletype", "explosion_distant"}
RANK = {"helicopter": 7, "gunfire_distant": 6, "vehicle_fire": 6, "walkie": 4, "uav_drone": 6, "plane_takeoff": 8,   # Cartels types
        "boat_engine": 7, "folder_drop": 6, "cell_door": 8, "door_kick": 7, "convoy": 6,
        "crack": 7, "gavel": 8, "cash_register": 7, "handcuffs": 7, "app_error": 6, "rubber_stamp": 7, "camera_flash": 5,
        "stadium_crowd": 6, "atm": 5, "card_swipe": 5, "coins": 5, "app_notify": 5, "music_box": 4,   # Paraguay types
        "boom_low": 10, "riser": 9, "explosion_distant": 9, "train_pass": 8, "heartbeat": 7, "drone_buzz": 7,
        "car_engine": 6, "car_door": 6, "phone_vibrate": 6, "message_ping": 5, "radio_static": 5, "siren_distant": 5,
        "door_knock": 6, "keyboard": 4, "glitch": 4, "fire_crackle": 6, "stamp_thud": 8, "phone_ring": 8, "plane_pass": 8, "teletype": 7, "burn_crackle": 7,
        "film_burn": 7, "medal_ring": 7, "domino_run": 7, "domino_tick": 5, "radio_pulse": 5, "dial_click": 5, "scanner_sweep": 4, "string_draw": 3, "circuit_clunk": 6, "switch_click": 5, "typewriter": 5, "clock_tick": 5, "card_flip": 4, "solder_hiss": 4, "map_pin": 6, "paper_tear": 6, "highlighter_swipe": 6, "counter_ticks": 5, "odometer_tick": 5,
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


# ---------------------------------------------------------------- MANUAL §0 "Music never drowns the voice": VO-driven duck
def hop_energy(x, hop=0.01, chunk_s=30.0):
    """K-weighted (BS.1770), channel-summed energy per `hop` s, computed in chunks with carried filter state (memory-light).
    x = stereo array or a WAV path (read in chunks)."""
    from scipy import signal
    from loudness import _B1, _A1, _B2, _A2
    h = int(round(hop * SR))
    if isinstance(x, str):
        info = sf.info(x)
        assert info.samplerate == SR, (x, info.samplerate)
        n = info.frames
        get = lambda a, b: sf.read(x, start=a, frames=b - a, dtype="float64", always_2d=True)[0][:, :2]
    else:
        n = len(x)
        get = lambda a, b: np.asarray(x[a:b], np.float64).reshape(b - a, -1)[:, :2]
    z1 = z2 = None
    out = np.zeros(n // h + 1)
    step = int(chunk_s * SR) // h * h
    for a in range(0, n, step):
        b = min(n, a + step)
        y = get(a, b)
        if z1 is None:
            z1 = np.zeros((2, y.shape[1])); z2 = np.zeros((2, y.shape[1]))
        y, z1 = signal.lfilter(_B1, _A1, y, axis=0, zi=z1)
        y, z2 = signal.lfilter(_B2, _A2, y, axis=0, zi=z2)
        p = (y ** 2).sum(1)
        k = len(p) // h
        out[a // h:a // h + k] = p[:k * h].reshape(k, h).sum(1)
        if len(p) > k * h:
            out[a // h + k] += p[k * h:].sum()
    return out


def window_lufs(e, win, hop=0.01):
    """Loudness of `win`-s windows centred on each hop, from hop energies."""
    c = np.concatenate([[0.0], np.cumsum(e)])
    w = max(1, int(round(win / hop)))
    k = np.arange(len(e))
    a = np.clip(k - w // 2, 0, len(e))
    b = np.clip(k + (w - w // 2), 0, len(e))
    m = (c[b] - c[a]) / (np.maximum(b - a, 1) * hop * SR)
    return -0.691 + 10 * np.log10(m + 1e-20)


def apply_gain_db(x, g_db, hop=0.01, chunk_s=30.0):
    """x *= db(gain curve sampled every hop), in place and in chunks."""
    ts = np.arange(len(g_db)) * hop
    step = int(chunk_s * SR)
    for a in range(0, len(x), step):
        b = min(len(x), a + step)
        x[a:b] *= db(np.interp(np.arange(a, b) / SR, ts, g_db))[:, None]
    return x


def vo_duck(music, vo, vo_lufs, gap=20.0, gap_fast=18.0, margin=0.7, attack=0.05, release=0.4, max_cut=-30.0, ceiling=20.0,
            passes=3, log=print):
    """Sidechain the MUSIC bed from the VO (the VO is only read). Limits (Krish 2026-11-13, MANUAL §10.8 "Music limits"):
    wherever he speaks, the music's short-term (3 s) loudness stays ≥ `gap` (20) LU under the VO's short-term loudness and its
    momentary (0.4 s) loudness ≥ `gap_fast` (18) LU under the VO's local speech level (0.4 s loudness max-held over 0.5 s, so word
    gaps don't pump); EVERYWHERE — pauses and between sections included — the music's 3 s loudness stays ≥ `ceiling` (20) LU under
    the VO's integrated loudness (0.4 s: ceiling − 3). Gain every 10 ms, 50 ms look-ahead, attack `attack` s, release `release` s,
    never more than `max_cut` dB. Modifies `music` in place (chunked, memory-light). Returns (music, report, gain curve dB per 10 ms)."""
    from scipy.ndimage import maximum_filter1d, minimum_filter1d
    hop = 0.01
    ev = hop_energy(vo, hop)
    lv4, lv3 = window_lufs(ev, 0.4, hop), window_lufs(ev, 3.0, hop)
    hold = maximum_filter1d(lv4, int(0.5 / hop))
    speak4, speak3 = hold > vo_lufs - 10, lv3 > vo_lufs - 12
    a_c, r_c = 1 - np.exp(-hop / attack), 1 - np.exp(-hop / release)
    total = None
    for _ in range(passes):
        em = hop_energy(music, hop)
        n = min(len(em), len(ev))
        lm4, lm3 = window_lufs(em, 0.4, hop)[:n], window_lufs(em, 3.0, hop)[:n]
        need = np.zeros(n)
        need = np.where(speak4[:n], np.minimum(need, hold[:n] - gap_fast - margin - lm4), need)
        need = np.where(speak3[:n], np.minimum(need, lv3[:n] - gap - margin - lm3), need)
        if ceiling is not None:                                   # absolute cap, also in pauses / between sections
            need = np.minimum(need, vo_lufs - ceiling - margin - lm3)
            need = np.minimum(need, vo_lufs - (ceiling - 3.0) - margin - lm4)
        need = minimum_filter1d(np.minimum(need, 0.0), int(0.1 / hop))   # centred → 50 ms look-ahead
        need = np.maximum(need, max_cut - (total if total is not None else 0.0))   # total cut never beyond max_cut
        g = np.zeros(n)
        cur = 0.0
        for k in range(n):                                     # one-pole in dB: fast down, slow up
            cur += (need[k] - cur) * (a_c if need[k] < cur else r_c)
            g[k] = cur
        apply_gain_db(music, g, hop)
        total = g if total is None else total + g
    d = total < -0.5
    rep = dict(gap=gap, gap_fast=gap_fast, ceiling=ceiling, attack=attack, release=release, max_cut=max_cut, ducked_pct=round(float(d.mean() * 100), 1),
               mean_cut_db_while_ducked=round(float(total[d].mean()), 2) if d.any() else 0.0, max_cut_db=round(float(total.min()), 2))
    log(f"vo_duck: 3 s ≥{gap:g} LU / 0.4 s ≥{gap_fast:g} LU under the VO, ceiling VO−{ceiling} — ducked {rep['ducked_pct']}% of the time, mean {rep['mean_cut_db_while_ducked']} dB "
        f"while ducked, max {rep['max_cut_db']} dB")
    return music, rep, total


def sfx_limit(sfx, music, vo, vo_lufs, gap=14.0, margin=1.0, max_cut=-30.0, passes=3, log=print):
    """Gain-ride the SFX bus (never the VO, never the music) so that wherever he speaks the 3 s loudness of music+SFX stays
    ≥ `gap` (14) LU under the VO's 3 s loudness — the MANUAL §10.8 "Music limits" SFX row, measured exactly as
    vo_music_scan.py does it (K-weighted hop energies, 3 s windows, speaking = VO 3 s > VO_LUFS − 12). Needed for a quiet VO
    (NVIDIA −29.8 LUFS): the per-event peak caps keep each SFX under the local VO PEAK, but sustained types (ticks, scribbles,
    keyboard, loops) in a soft passage still add up. `music` = stereo array or WAV path (read chunked). Modifies `sfx` in place.
    Returns (sfx, report)."""
    from scipy.ndimage import minimum_filter1d, uniform_filter1d
    hop = 0.01
    w = int(round(3.0 / hop))
    ev = hop_energy(vo, hop)
    em = hop_energy(music, hop)
    lv3 = window_lufs(ev, 3.0, hop)
    speak = lv3 > vo_lufs - 12
    total = None
    for _ in range(passes):
        es = hop_energy(sfx, hop)
        n = min(len(ev), len(em), len(es))
        mean = lambda e: 10 ** ((window_lufs(e[:n], 3.0, hop) + 0.691) / 10)     # mean-square of the 3 s window
        tgt = 10 ** ((lv3[:n] - gap - margin + 0.691) / 10)
        Em, Es = mean(em), mean(es)
        over = speak[:n] & (Em + Es > tgt) & (Es > 1e-14)
        G = np.ones(n)
        G[over] = np.clip((tgt[over] - Em[over]) / Es[over], 10 ** (max_cut / 10), 1.0)
        need = 10 * np.log10(G)                                   # dB needed for the window centred on each hop
        need = minimum_filter1d(need, w + 1)                       # every hop inside a too-loud window gets that cut
        need = uniform_filter1d(need, int(0.05 / hop))             # 50 ms smoothing (no clicks)
        need = np.maximum(need, max_cut - (total if total is not None else 0.0))
        if need.min() > -0.05:
            break
        apply_gain_db(sfx, need, hop)
        total = need if total is None else total + need
    if total is None:
        total = np.zeros(1)
    d = total < -0.5
    rep = dict(gap=gap, margin=margin, cut_pct=round(float(d.mean() * 100), 2),
               mean_cut_db_while_cut=round(float(total[d].mean()), 2) if d.any() else 0.0, max_cut_db=round(float(total.min()), 2))
    log(f"sfx_limit: music+SFX 3 s ≥{gap:g} LU under the VO while he speaks — SFX bus cut {rep['cut_pct']}% of the time, "
        f"mean {rep['mean_cut_db_while_cut']} dB while cut, max {rep['max_cut_db']} dB")
    return sfx, rep
