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
GATE_DB = -45.0               # VO activity gate (20 ms RMS); Epidemic mode sets it relative to the measured VO (Ivan VO = −36.8 LUFS)
AMB_SCALE = 1.0               # Epidemic mode: db(min(0, VO_LUFS + 25)) — keeps room tone / library loops ≈ 30 LU under a quiet VO
DUCKS = []                    # cue-sheet "ducks": [{"start","end","db","ramp","sfx_db"}] — insert clips (music thinned, SFX/amb muted)


# =============================================================== VO analysis (read-only)
def vo_activity():
    with tempfile.TemporaryDirectory() as td:
        p = os.path.join(td, "vo.wav")
        subprocess.run([FFMPEG, "-v", "error", "-y", "-i", os.path.join(ROOT, VO_FILE), "-ar", "48000", p], check=True)
        x, _ = sf.read(p, always_2d=True)
    h = int(0.02 * SR)
    n = len(x) // h
    lev = 20 * np.log10(np.sqrt((x[: n * h].reshape(n, h, -1) ** 2).mean(1).max(1)) + 1e-9)
    act = lev > GATE_DB
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
        if any(a < d["end"] + 0.5 and b > d["start"] - 0.5 for d in DUCKS):
            continue                       # no lift around an insert clip (its own audio is the foreground)
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
    if DUCKS:
        x = x * db(duck_env(DUCKS, "db"))[:, None]
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


def duck_env(ducks, key, default=-12.0):
    """dB envelope over the whole timeline: 0 outside, ducks[key] inside each window, linear ramps of `ramp` s."""
    ts = np.arange(N) / SR
    pts = [(0.0, 0.0)]
    for d in sorted(ducks, key=lambda d: d["start"]):
        r = float(d.get("ramp", 0.6))
        v = float(d.get(key, default))
        pts += [(d["start"] - r, 0.0), (d["start"], v), (d["end"], v), (d["end"] + r, 0.0)]
    pts.append((LEN, 0.0))
    pts.sort()
    return np.interp(ts, [p[0] for p in pts], [p[1] for p in pts])


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
    "switch_click": (0.06, 0.08), "card_flip": (0.06, 0.08), "rewind": (0.07, 0.09), "clock_tick": (0.04, 0.05),
    "typewriter": (0.05, 0.065), "medal_ring": (0.05, 0.07), "solder_hiss": (0.04, 0.05),
    # c3 types (photocopier, red string, radio rings, dominoes, rotary dial)
    "scanner_sweep": (0.05, 0.065), "string_draw": (0.05, 0.065), "radio_pulse": (0.035, 0.045),
    "domino_tick": (0.06, 0.08), "domino_run": (0.06, 0.08), "dial_click": (0.05, 0.065),
    # Ivan types (project/ivan/SOUND_PLAN.md §4) — Epidemic recordings, cut per event
    "radio_static": (0.045, 0.06), "phone_vibrate": (0.06, 0.08), "message_ping": (0.035, 0.045),
    "drone_buzz": (0.05, 0.07), "explosion_distant": (0.12, 0.16), "train_pass": (0.07, 0.09),
    "car_engine": (0.06, 0.08), "car_door": (0.07, 0.09), "keyboard": (0.045, 0.06), "heartbeat": (0.10, 0.13),
    "glitch": (0.035, 0.045), "fire_crackle": (0.06, 0.08), "siren_distant": (0.04, 0.05), "door_knock": (0.06, 0.08),
    # Paraguay types (project/paraguay/SOUND_PLAN.md §4) — Epidemic recordings, cut per event
    "app_notify": (0.035, 0.045), "app_error": (0.035, 0.045), "cash_register": (0.06, 0.08), "coins": (0.05, 0.07),
    "card_swipe": (0.05, 0.065), "atm": (0.045, 0.06), "rubber_stamp": (0.08, 0.11), "music_box": (0.025, 0.035),
    "gavel": (0.08, 0.10), "camera_flash": (0.05, 0.07), "handcuffs": (0.05, 0.065), "stadium_crowd": (0.04, 0.055),
    "crack": (0.07, 0.09),   # ice crack (number/glass splitting)
    "bleep": (1.0, 1.0),   # not used: bleeps are placed at a fixed level re the VO (place_bleeps)
}
LOWTYPES = {"boom_low", "stamp_thud", "explosion_distant", "heartbeat"}
SFX_TRIM_DB = -3.0   # this VO is quiet (speech peaks ~ -16 dBFS): trims the table so SFX sit ~20 dB under local VO peaks
AMBTYPES = {"projector_loop", "crt_hum", "wind", "factory_hum", "crowd_room", "tube_hum", "city_night",
            "crowd_chant", "crowd_murmur", "newsroom"}          # Paraguay: protest chants, indoor walla, newsroom


def epi(name, start=0.0, dur=None):
    import epidemic_bed as E
    return E.read_window(E.sfx_path(name), start, dur)


_GAVEL = [1]


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
                                     "export processing", "chiang", "traitorous", "integrated circuit",
                                     "silicon valley")):
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
    # ---------------- Ivan types (project/ivan/SOUND_PLAN.md §4)
    if ty == "stamp_thud" and any(k in note for k in ("passport", "rubber", "visa", "document")):
        y = epi("rubber_stamp_document_01")
        return y, onset(y), "epi:rubber_stamp_document_01"
    if ty == "shutter" and any(k in note for k in ("zenit", "film", "soviet", "old", "surveil", "cctv", "spy")):
        nm = ["shutter_zenit_01", "shutter_zenit_02", "shutter_canon_5d"][i % 3]
        y = epi(nm)
        return y, onset(y), f"epi:{nm}"
    if ty == "radio_static":
        nm = ["radio_static_lost_signal_01", "radio_am_tuning_glitchy_01"][i % 2]
        dur = max(0.4, d or 1.2)
        y = fade(epi(nm, float(rng.uniform(1.0, 12.0)), dur), 0.03, min(0.3, dur / 3))
        return y, 0.0, f"epi:{nm} {dur:.1f}s"
    if ty == "phone_vibrate":
        if d and d > 1.0:
            y = fade(epi("phone_vibrate_call_loop", 0.0, min(d, 3.2)), 0.01, 0.15)
            return y, 0.0, "epi:phone_vibrate_call_loop"
        nm = ["phone_vibrate_hand_01", "phone_vibrate_hand_02"][i % 2]
        y = epi(nm)
        return y, onset(y), f"epi:{nm}"
    if ty == "message_ping":
        nm = ["message_text_ping_01", "message_text_ping_02"][i % 2]
        y = epi(nm)
        return y, onset(y), f"epi:{nm}"
    if ty == "drone_buzz":
        nm = ["drone_rc_motor_medium", "drone_rc_fly_around"][i % 2]
        dur = max(1.0, d or 2.5)
        full = epi(nm)
        a = float(rng.uniform(0.5, max(0.6, len(full) / SR - dur - 0.5)))
        y = fade(full[int(a * SR):int((a + dur) * SR)], min(0.6, dur / 3), min(0.8, dur / 3))
        return y, 0.0, f"epi:{nm} {dur:.1f}s"
    if ty == "explosion_distant":
        nm = ["explosion_distant_01", "boom_distant_explosion_03", "explosion_distant_03"][i % 3]
        y = epi(nm)
        o = onset(y)
        y = fade(y[max(0, int((o - 0.05) * SR)):int((o + 5.0) * SR)], 0.02, 1.5)
        return y, 0.05, f"epi:{nm}"
    if ty == "train_pass":
        nm = ["train_locomotive_pass_night", "train_locomotive_pass_dawn"][i % 2]
        full = epi(nm)
        lk = loudest(full)
        span = max(d or 3.0, 2.0) + 3.0
        a = max(0.0, lk - span / 2)
        y = fade(full[int(a * SR):int((a + span) * SR)], 1.2, 1.5)
        return y, (lk - a) - (d or 3.0) / 2, f"epi:{nm} (peak mid-move)"
    if ty == "car_engine":
        nm = "car_w108_start_idle_stop" if (i % 2 or "idle" in note) else "car_start_idle_rover"
        dur = max(1.0, d or 3.0)
        y = epi(nm)
        o = onset(y)
        y = fade(y[int(max(0, o - 0.05) * SR):int((o + dur) * SR)], 0.01, min(0.8, dur / 3))
        return y, 0.05, f"epi:{nm} {dur:.1f}s"
    if ty == "car_door":
        nm = "car_trunk_close" if any(k in note for k in ("trunk", "boot", "inspect")) else "car_door_close_hard"
        y = epi(nm)
        return y, onset(y), f"epi:{nm}"
    if ty == "keyboard":
        nm = ["keyboard_typing_apple", "keyboard_typing_17s"][i % 2]
        dur = max(0.4, d or 1.0)
        full = epi(nm)
        a = float(rng.uniform(0.2, max(0.3, len(full) / SR - dur - 0.2)))
        y = fade(full[int(a * SR):int((a + dur) * SR)], 0.02, 0.1)
        return y, 0.0, f"epi:{nm} {dur:.1f}s"
    if ty == "heartbeat":
        nm = "heartbeat_evil_fat_bass" if "evil" in note or "fat" in note else "heartbeat_cinematic_54bpm"
        dur = max(1.2, d or 3.0)
        y = fade(epi(nm, 2.0, dur), 0.3, min(1.0, dur / 3))
        return y, 0.0, f"epi:{nm} {dur:.1f}s"
    if ty == "glitch":
        nm = ["glitch_data_06", "glitch_data_12"][i % 2]
        y = epi(nm, 0.0, d) if d else epi(nm)
        return fade(y, 0.005, 0.08), onset(y), f"epi:{nm}"
    if ty == "fire_crackle":
        dur = max(1.0, d or 2.0)
        y = fade(epi("fire_burning_crackles", float(rng.uniform(1, 25)), dur), 0.4, min(0.8, dur / 3))
        return y, 0.0, f"epi:fire_burning_crackles {dur:.1f}s"
    if ty == "siren_distant":
        dur = max(2.0, d or 4.0)
        y = fade(epi("police_siren_distant", float(rng.uniform(2, 40)), dur), 1.0, min(1.5, dur / 3))
        return y, 0.0, f"epi:police_siren_distant {dur:.1f}s"
    if ty == "door_knock":
        y = epi("door_knock_apartment")
        y = y[:int(min(len(y) / SR, d or 1.6) * SR)]
        return fade(y, 0.0, 0.1), onset(y), "epi:door_knock_apartment"
    # ---------------- Paraguay types (project/paraguay/SOUND_PLAN.md §4)
    if ty == "app_notify":
        nm = ["notification_tone_02", "notification_app_general_01"][i % 2]
        y = epi(nm)
        return y, onset(y), f"epi:{nm}"
    if ty == "app_error":
        nm = ["app_error_04", "app_error_01"][i % 2]
        y = epi(nm)
        return y, onset(y), f"epi:{nm}"
    if ty == "cash_register":
        y = epi("cash_register_kaching")
        return y, loudest(y), "epi:cash_register_kaching (bell on t)"
    if ty == "coins":
        nm = "coins_handful_drop_wood" if any(k in note for k in ("handful", "pile", "many", "pour")) else "coins_drop_01"
        y = epi(nm)
        return fade(y, 0.0, 0.3), onset(y), f"epi:{nm}"
    if ty == "card_swipe":
        nm = ["card_swipe_03", "card_swipe_04"][i % 2]
        y = epi(nm)
        return y, onset(y), f"epi:{nm}"
    if ty == "atm":                     # button beeps / cash flap excerpt of the ATM recording
        dur = max(0.6, d or 1.5)
        y = fade(epi("atm_cash_buttons_beep", float(rng.uniform(1.0, 20.0)), dur), 0.01, min(0.3, dur / 3))
        return y, 0.0, f"epi:atm_cash_buttons_beep {dur:.1f}s"
    if ty == "rubber_stamp" or (ty == "stamp_thud" and any(k in note for k in ("rubber", "approved", "rejected", "stamp"))):
        nm = ["rubber_stamp_document_01", "stamp_hand_press_short"][i % 2]
        y = epi(nm) if nm == "rubber_stamp_document_01" else epi(nm, 0.0, 1.2)
        o = onset(y)
        if nm == "stamp_hand_press_short":
            y = fade(y[max(0, int((o - 0.02) * SR)):int((o + 0.6) * SR)], 0.005, 0.15)
            o = 0.02
        return y, o, f"epi:{nm}"
    if ty == "music_box":               # carousel / merry-go-round hint: very low, high-passed by the bus
        if (d or 0) > 4.5:
            y = fade(epi("music_box_antique_melody", float(rng.uniform(2.0, 40.0)), d), min(1.0, d / 3), min(1.5, d / 3))
            return y, 0.0, f"epi:music_box_antique_melody {d:.1f}s"
        y = epi("music_box_wind_up")
        y = fade(y[:int(min(len(y) / SR, d or 4.5) * SR)], 0.05, 0.6)
        return y, 0.0, "epi:music_box_wind_up"
    if ty == "crack":
        nm = ["ice_crack_medium_long_01", "ice_crack_medium"][i % 2]
        y = epi(nm)
        return fade(y, 0.0, 0.3), onset(y), f"epi:{nm}"
    if ty == "gavel":
        _GAVEL[0] += 1                     # alternate the single takes in order of use (never the same knock twice)
        nm = "gavel_x2" if any(k in note for k in ("twice", "x2", "double")) else ["gavel_single_01", "gavel_single_02"][_GAVEL[0] % 2]
        y = epi(nm)
        return y, onset(y), f"epi:{nm}"
    if ty == "camera_flash":            # press photographers: a burst for dur > 1 s, else one modern flash
        if (d or 0) > 1.0:
            dur = min(d, 8.0)
            y = fade(epi("press_paparazzi_flashes_medium", float(rng.uniform(0.0, max(0.0, 8.0 - dur))), dur), 0.3, min(0.8, dur / 3))
            return y, 0.0, f"epi:press_paparazzi_flashes_medium {dur:.1f}s"
        y = epi("camera_flash_modern_01")
        return y, onset(y), "epi:camera_flash_modern_01"
    if ty == "handcuffs":
        y = epi("handcuffs_click_slow")
        o = onset(y)
        y = fade(y[max(0, int((o - 0.02) * SR)):int((o + min(d or 1.2, 3.0)) * SR)], 0.005, 0.2)
        return y, 0.02, "epi:handcuffs_click_slow"
    if ty == "stadium_crowd":           # World Cup: distant stadium cheer, swells on t
        dur = max(1.5, d or 3.0)
        full = epi("stadium_cheer_goal_01")
        lk = loudest(full)
        a = max(0.0, lk - 0.8)
        y = fade(full[int(a * SR):int((a + dur + 1.0) * SR)], 0.5, min(1.5, dur / 2))
        return y, lk - a, f"epi:stadium_cheer_goal_01 {dur:.1f}s"
    if ty == "typewriter":
        nm = ["typewriter_hermes_03", "typewriter_hermes_01"][i % 2]
        dur = max(0.4, d or 1.2)
        full = epi(nm)
        a = float(rng.uniform(0.2, max(0.3, len(full) / SR - dur - 0.2)))
        y = fade(full[int(a * SR):int((a + dur) * SR)], 0.01, 0.1)
        return y, 0.0, f"epi:{nm} {dur:.1f}s"
    if ty == "burn_crackle" and (d or 0) >= 2.0:
        y = fade(epi("fire_burning_crackles", float(rng.uniform(1, 25)), d), 0.4, min(0.8, d / 3))
        return y, 0.0, f"epi:fire_burning_crackles {d:.1f}s"
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
    if ty == "switch_click":           # light switch / toggle
        nm = ["kenney_switch_click", "kenney_metal_click"][i % 2]
        y = lib(nm)
        return y, onset(y), nm
    if ty == "card_flip":              # playing card: short snappy paper flick + a tiny snap
        y = st(G.paper_slide(seed, float(rng.uniform(0.18, 0.28))))
        tk = st(G.ui_tick(seed, float(rng.uniform(2200, 3000))))
        k_ = int(0.6 * len(y)) if len(y) > len(tk) else 0
        y[k_:k_ + len(tk)] += 0.35 * tk[: len(y) - k_] * np.abs(y).max() / (np.abs(tk).max() + 1e-9)
        return y, 0.6 * len(y) / SR, f"card_flip gen#{seed}"
    if ty == "rewind":                 # tape rewind: reversed whoosh (+ fast ticker under longer ones)
        dur = max(0.35, d or 0.4)
        y = st(G.whoosh(min(dur, 2.5), seed, 300, 3200, 0.3))[::-1]
        if dur >= 1.0:
            tk = st(G.ticker_roll(min(dur, 2.5), 40, 18, seed))
            n_ = min(len(y), len(tk))
            y[:n_] += 0.4 * tk[:n_] * np.abs(y).max() / (np.abs(tk).max() + 1e-9)
        return y, 0.0, f"rewind {dur:.2f}s gen#{seed}"
    if ty == "clock_tick":
        dur = d or 1.0
        y = G.ticker_roll(dur, 14, 7, seed)
        return y, 0.0, f"clock_tick {dur:.2f}s gen#{seed}"
    if ty == "typewriter":
        dur = d or 0.6
        y = trimfit(st(lib("typewriter_burst_12keys")), dur, 0.05)
        return y, onset(y), f"typewriter_burst {dur:.2f}s"
    if ty == "medal_ring":             # metal medal: light plate impact + soft chime
        a_ = st(lib("kenney_impact_plate_light_01"))
        b_ = st(lib("chime_soft"))
        y = np.zeros((max(len(a_), len(b_)), 2))
        y[:len(a_)] += a_ / (np.abs(a_).max() + 1e-9)
        y[:len(b_)] += 0.35 * b_ / (np.abs(b_).max() + 1e-9)
        return y, onset(y), "medal_ring (plate + chime)"
    if ty == "solder_hiss":            # soldering iron touch: short bright hiss
        n_ = int(0.55 * SR)
        z = hp(np.random.default_rng(seed).standard_normal((n_, 2)) * 0.3, 2500, 2)
        z *= np.exp(-np.arange(n_) / (0.18 * SR))[:, None]
        return fade(z, 0.01, 0.08), 0.0, f"solder_hiss gen#{seed}"
    if ty == "scanner_sweep":          # photocopier light bar: bright band-passed sweep over a faint motor hum
        dur = max(0.3, d or 0.5)
        y = st(G.whoosh(dur, seed, 900, 5000, 0.5))
        n_ = len(y)
        hum = 0.08 * np.sin(2 * np.pi * 120 * np.arange(n_) / SR) * np.hanning(n_)
        y = y / (np.abs(y).max() + 1e-9) + np.stack([hum, hum], 1)
        return y, 0.0, f"scanner_sweep {dur:.2f}s gen#{seed}"
    if ty == "string_draw":            # red string drawn across the board
        y = G.string_pull(seed, d or 0.6)
        return y, 0.0, f"string_draw {d or 0.6:.2f}s gen#{seed}"
    if ty == "radio_pulse":            # radio rings: 3 soft sonar-like blips spread over the move, fading
        dur = max(0.6, d or 1.5)
        y = np.zeros((int((dur + 1.2) * SR), 2))
        for k_, (dt, f, a_) in enumerate([(0.0, 1180, 1.0), (dur / 3, 1060, 0.7), (2 * dur / 3, 940, 0.5)]):
            G.put(y, st(G.tone_blip(seed + k_, f)), dt, a_)
        y = G.room(y, 0.25) if hasattr(G, "room") else y
        return st(y), 0.0, f"radio_pulse x3 {dur:.1f}s gen#{seed}"
    if ty == "domino_tick":            # first domino tips: light wood knock
        y = lib("kenney_impact_wood_light_01")
        return y, onset(y), "kenney_impact_wood_light_01"
    if ty == "domino_run":             # the row follows suit: accelerating wood clicks over `dur`
        dur = max(0.4, d or 0.7)
        y = np.zeros((int((dur + 0.4) * SR), 2))
        tt, k_, gap = 0.0, 0, 0.12
        while tt < dur:
            G.put(y, st(G.tick(seed + k_, f=float(rng.uniform(1100, 1600)), bright=0.7)), tt, float(rng.uniform(0.7, 1.0)))
            tt += gap * rng.uniform(0.85, 1.1)
            gap = max(0.05, gap * 0.85)
            k_ += 1
        return y, 0.0, f"domino_run x{k_} {dur:.2f}s gen#{seed}"
    if ty == "dial_click":             # rotary dial: ratchet ticks slowing as the dial returns
        dur = d or 1.5
        y = G.ticker_roll(dur, 18, 9, seed)
        return y, 0.0, f"dial_click {dur:.2f}s gen#{seed}"
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
        gain *= AMB_SCALE                       # library loops were tuned for a ≈ −25 LUFS VO
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
        elif m["type"] == "tube_hum":   # vacuum-tube rack: CRT hum + a little electronics room tone
            g = 0.012 * (1.4 if m.get("level") == "normal" else 1.0)
            loop_seg("crt_hum_loop_6s", m["t"], m["t"] + d, g, 0.3, 0.5)
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
        elif m["type"] in ("crowd_chant", "crowd_murmur", "newsroom"):     # Paraguay (SOUND_PLAN §4): felt, not heard
            n_ = m.get("note", "").lower()
            if m["type"] == "crowd_chant":
                nm = "protest_distant_drums_chants" if any(k in n_ for k in ("drum", "street", "march")) else \
                    ("protest_chanting_02" if any(k in n_ for k in ("close", "near", "loud")) else "protest_distant_chanting_walla")
                rel = -22.0
            elif m["type"] == "crowd_murmur":
                nm, rel = "crowd_walla_indoor_large_02", -25.0
            else:
                nm, rel = "office_small_group_keyboard", -26.0
            y = epi(nm, float(rng.uniform(3, 50)), d + 0.6)
            g = db(VO_LUFS + rel - integrated_lufs(y)) * (db(-4) if quiet else 1.0)
            y = fade(y, min(1.0, d / 3), min(1.5, d / 3))
            i0 = int(m["t"] * SR)
            k_ = min(len(y), N - i0)
            amb[i0:i0 + k_] += g * y[:k_]
            amb_log.append(dict(t=m["t"], type=m["type"], dur=d, gain=round(float(g), 4), file=nm))
            continue
        elif m["type"] == "city_night" or (m["type"] == "wind" and EPIDEMIC and
                                             any(k in m.get("note", "").lower() for k in ("winter", "snow", "moscow", "cold"))):
            nm = "city_night_distant_traffic_01" if m["type"] == "city_night" else "wind_winter_08"
            if m["type"] == "city_night" and any(k in m.get("note", "").lower() for k in ("asunci", "paraguay", "tropic", "insect")):
                nm = "city_night_rooftop_insects"           # warm night, distant traffic + insects (Asunción)
            y = epi(nm, float(rng.uniform(3, 40)), d + 0.6)
            g = db(VO_LUFS - 24.0 - integrated_lufs(y)) * (db(-4) if quiet else 1.0)   # felt, not heard
            y = fade(y, min(0.8, d / 3), min(1.2, d / 3))
            i0 = int(m["t"] * SR)
            k_ = min(len(y), N - i0)
            amb[i0:i0 + k_] += g * y[:k_]
            amb_log.append(dict(t=m["t"], type=m["type"], dur=d, gain=round(float(g), 4), file=nm))
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
    if DUCKS:                                   # insert clips: their own audio is the foreground — SFX/ambience out
        inner = [dict(d, start=d["start"] + 0.3, end=d["end"] - 0.3, ramp=0.3) for d in DUCKS]   # whips on the boundary survive
        env = db(duck_env(inner, "sfx_db", -60.0))[:, None]
        sfx, amb = sfx * env, amb * env
    for nm, x in ((f"sfx{SUFFIX}.wav", sfx), (f"ambience{SUFFIX}.wav", amb)):
        sf.write(os.path.join(BED, nm), x, SR, subtype="PCM_24")
        print(f"{nm}: peak {20*np.log10(np.abs(x).max()+1e-12):.1f} dBFS  LUFS {integrated_lufs(x):.1f}")
    json.dump({"sfx": log, "ambience": amb_log}, open(os.path.join(BED, "sfx_placements.json"), "w"), indent=1)
    return sfx, amb, log


def place_bleeps(sfx, bleeps):
    """TV-style censor bleep over a muted word (Krish's request, project/paraguay/DECISIONS.md §3): a 1 kHz sine of exactly
    the word's length (5 ms ramps), loudness ≈ VO − 3 LU (a stereo sine of amplitude A reads ≈ 20·log10(A) LUFS), added
    to the SFX bus after the restraint pass and the caps. The VO word itself is muted by the lead in the final mix."""
    out = []
    for b in bleeps:
        t, d = float(b["t"]), max(0.08, float(b.get("dur", 0.3)))
        f = float(b.get("hz", 1000.0))
        n = int(round(d * SR))
        y = np.sin(2 * np.pi * f * np.arange(n) / SR)
        r = int(0.005 * SR)
        y[:r] *= np.linspace(0, 1, r)
        y[-r:] *= np.linspace(1, 0, r)
        a = float(db(VO_LUFS + float(b.get("rel_lu", -3.0))))
        i0 = int(round(t * SR))
        k = min(n, N - i0)
        if k <= 0:
            continue                       # beyond --len (test builds of a part)
        sfx[i0:i0 + k] += a * np.stack([y[:k], y[:k]], 1)
        out.append(dict(t=t, dur=d, hz=f, amp_dbfs=round(20 * np.log10(a), 1), note=b.get("note", "")))
    return out


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
    ALIAS = {"clunk": "circuit_clunk", "crowd": "crowd_room",     # c6 editor names
             # Ivan: likely editor spellings -> SOUND_PLAN §4 types
             "static": "radio_static", "radio": "radio_static", "phone_buzz": "phone_vibrate", "vibrate": "phone_vibrate",
             "phone_vibration": "phone_vibrate", "ping": "message_ping", "notification": "message_ping",
             "message": "message_ping", "msg_ping": "message_ping", "message_tick": "message_ping", "drone": "drone_buzz",
             "explosion": "explosion_distant", "blast": "explosion_distant", "train": "train_pass",
             "car": "car_engine", "engine": "car_engine", "typing": "keyboard", "keyboard_typing": "keyboard",
             "keys": "keyboard", "heartbeat_low": "heartbeat", "pulse_low": "heartbeat", "camera_shutter": "shutter",
             "glitch_digital": "glitch", "digital_glitch": "glitch", "siren": "siren_distant", "knock": "door_knock",
             "fire": "fire_crackle", "city": "city_night", "city_ambience": "city_night",
             # Paraguay: likely editor spellings -> SOUND_PLAN §4 types
             "censor": "bleep", "beep_censor": "bleep", "censor_bleep": "bleep", "notification_app": "app_notify",
             "app_ping": "app_notify", "error": "app_error", "error_tone": "app_error", "app_fail": "app_error",
             "kaching": "cash_register", "cash": "cash_register", "register": "cash_register", "coin": "coins",
             "coin_drop": "coins", "card": "card_swipe", "swipe": "card_swipe", "atm_beep": "atm", "cash_machine": "atm",
             "stamp": "rubber_stamp", "stamp_paper": "rubber_stamp", "musicbox": "music_box", "carousel": "music_box",
             "merry_go_round": "music_box", "hammer": "gavel", "flash": "camera_flash", "camera_flashes": "camera_flash",
             "paparazzi": "camera_flash", "press_flash": "camera_flash", "cuffs": "handcuffs", "handcuff": "handcuffs",
             "stadium": "stadium_crowd", "cheer": "stadium_crowd", "crowd_cheer": "stadium_crowd",
             "protest": "crowd_chant", "chant": "crowd_chant", "chants": "crowd_chant", "protest_chant": "crowd_chant",
             "murmur": "crowd_murmur", "walla": "crowd_murmur", "office": "newsroom", "newsroom_amb": "newsroom",
             "marker_short": "marker_scratch", "crack_glass": "crack", "ice_crack": "crack", "glass_crack": "crack"}
    for m in markers:
        m["type"] = ALIAS.get(m["type"], m["type"])
        if m.get("level") in ("loud", "hero", "high"):
            m["level"] = "normal"                 # editors' spellings of the louder level
    markers.sort(key=lambda m: m["t"])
    unknown = {m["type"] for m in markers} - set(GAIN) - AMBTYPES
    assert not unknown, unknown
    if not EPIDEMIC:                                   # legacy 600 s edit
        act, pauses, vo = vo_activity()
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
    AMB_SCALE = float(db(min(0.0, VO_LUFS + 25.0)))
    GATE_DB = min(-45.0, VO_LUFS - 13.5)          # quiet VO (Ivan −36.8 LUFS): −45 dBFS misses half the speech frames
    act, pauses, vo = vo_activity()
    sheet = json.load(open(os.path.join(ROOT, a.cues)))
    DUCKS = sheet.get("ducks", [])
    # sound designer's edits of editor markers (cue sheet "marker_edits": drop / retype one marker by t + type)
    for ed in sheet.get("marker_edits", []):
        hit = [m for m in markers if m["type"] == ed["type"] and abs(m["t"] - ed["t"]) < 0.02]
        if not hit:
            print(f"  !! marker_edit matched nothing: {ed}")
            continue
        for m in hit:
            if ed["action"] == "drop":
                markers.remove(m)
            else:
                m["type"] = ed["to"]
                m["note"] = (m.get("note", "") + " | " + ed.get("note", "")).strip(" |")
                if "dur" in ed:
                    m["dur"] = ed["dur"]
        print(f"marker_edit {ed['action']} {ed['type']}@{ed['t']}" + (f" -> {ed['to']}" if ed["action"] != "drop" else ""))
    if DUCKS:                                     # no SFX inside an insert clip (editor rule) — drop and report them
        ins = [m for m in markers if any(d["start"] + 0.1 < m["t"] < d["end"] - 0.1 for d in DUCKS)]
        markers = [m for m in markers if m not in ins]
        if ins:
            print(f"dropped {len(ins)} markers inside insert windows: " + ", ".join(f"{m['type']}@{m['t']}" for m in ins))
    st_t = [float(x["t"]) for x in sheet.get("stingers", [])]
    dup = [m for m in markers if m["type"] in ("boom_low", "riser") and any(abs(m["t"] - t) <= 0.6 for t in st_t)]
    if dup:                                       # the cue sheet's stinger already hits that word: no double hits
        markers = [m for m in markers if m not in dup]
        print(f"dropped {len(dup)} boom/riser markers duplicating a stinger: " + ", ".join(f"{m['type']}@{m['t']}" for m in dup))
    bleeps = [dict(b) for b in sheet.get("bleeps", [])]
    for m in [m for m in markers if m["type"] == "bleep"]:
        markers.remove(m)
        if not any(abs(float(b["t"]) - m["t"]) <= 0.3 for b in bleeps):
            bleeps.append(dict(t=m["t"], dur=m.get("dur", 0.3), note=f"editor marker {m.get('scene', '')}"))
    SFX_TRIM_DB = -3.0 + (VO_LUFS + 27.2)          # the table was tuned for a −27.2 LUFS VO
    print(f"VO {VO_FILE}: {VO_LUFS:.1f} LUFS (measured, untouched); {len(markers)} markers; {len(pauses)} pauses")
    import epidemic_bed as E
    if not a.no_hierarchy:
        kept, dropped = E.hierarchy(markers)
        json.dump(dict(total=len(markers), kept=len(kept), dropped=dropped, kept_markers=kept),
                  open(os.path.join(BED, "sfx_hierarchy.json"), "w"), indent=1)
        print(f"hierarchy (§10.8): kept {len(kept)} / {len(markers)} markers, dropped {len(dropped)}")
        markers = kept
    build_music_epidemic(sheet, act, pauses)
    sfx, _amb, _log = build_sfx_and_amb(markers, [(0.0, LEN, "PAPER", set())], act, vo)
    if bleeps:                                    # added after the SFX bus is written: rewrite it with the bleeps on top
        bl = place_bleeps(sfx, bleeps)
        sf.write(os.path.join(BED, "sfx.wav"), sfx, SR, subtype="PCM_24")
        pl = json.load(open(os.path.join(BED, "sfx_placements.json")))
        pl["bleeps"] = bl
        json.dump(pl, open(os.path.join(BED, "sfx_placements.json"), "w"), indent=1)
        print(f"bleeps: {len(bl)} placed at " + ", ".join(f"{b['t']:.2f}+{b['dur']:.2f}s" for b in bl))
    rel = os.path.relpath(BED, ROOT)
    tl = [dict(id=i, src=f"{rel}/{f}", start=0, duration=LEN, media_start=0, volume=1.0)
          for i, f in (("bed-music", "music_bed.wav"), ("bed-sfx", "sfx.wav"), ("bed-amb", "ambience.wav"))]
    json.dump(tl, open(os.path.join(BED, "timeline.json"), "w"), indent=1)
    print(f"{len(markers)} markers placed; {rel}/timeline.json written")
