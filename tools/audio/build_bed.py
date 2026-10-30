#!/usr/bin/env python3
"""Assemble one continuous music bed WAV from the cue library, following a cue sheet.

Usage: python3 tools/audio/build_bed.py cuesheet.json out.wav

cuesheet.json:
{
  "length": 600.0,                  # seconds, whole bed
  "xfade": 2.0,                     # default crossfade between segments (equal power)
  "segments": [
    {"cue": "curious_neutral_Dmaj_96bpm", "start": 0,   "end": 72,
     "stems": ["marimba", "pad"],   # optional; default = FULL mix
     "gain_db": 0, "offset": 0,     # offset = where inside the cue to start reading (at 'start')
     "anchor": 4.32,                # alternative to offset: timeline time of the cue's bar 1
                                    #   (keeps several segments of one cue phase-locked)
     "fade_in": 2.0, "fade_out": 2.0,  # per-side fades, centred on start/end (default xfade)
     "linear": false,               # linear fades (use between stem sets of the SAME cue);
                                    #   "linear_in"/"linear_out" override per side
     "stem_gain_db": {"pad": -3}},  # optional per-stem trims
    {"cue": "stinger_reveal_Dmaj", "start": 70.7, "end": 78, "overlay": true}   # overlay = mixed on top, no xfade
  ]
}
Looping cues are tiled seamlessly when a segment is longer than the cue.
The result is NOT loudness-normalized: the cue files are at -18 LUFS and the mix level is
set in the composition (data-volume / automation) per MIX_RULES.md. A -1 dBFS safety
check is printed.
"""
import json
import os
import sys

import numpy as np
import soundfile as sf

sys.path.insert(0, os.path.dirname(__file__))
from dsp import SR, AUDIO, db

MUSIC = os.path.join(AUDIO, "music")
NON_LOOP = ("momentum", "stinger")   # through-composed cues: never tiled


def load(cue, stems):
    d = os.path.join(MUSIC, cue)
    if not stems:
        x, _ = sf.read(os.path.join(d, f"{cue}_FULL.wav"), always_2d=True)
        return x, {}
    parts = {}
    for s in stems:
        parts[s], _ = sf.read(os.path.join(d, f"{cue}_stem_{s}.wav"), always_2d=True)
    return None, parts


def tile(x, n, offset):
    i0 = int(round(offset * SR)) % len(x)
    reps = int(np.ceil((n + i0) / len(x))) + 1
    return np.tile(x, (reps, 1))[i0:i0 + n]


if __name__ == "__main__":
    sheet = json.load(open(sys.argv[1]))
    out = sys.argv[2]
    L = int(sheet["length"] * SR)
    X = int(sheet.get("xfade", 2.0) * SR)
    bed = np.zeros((L, 2))
    for seg in sheet["segments"]:
        full, parts = load(seg["cue"], seg.get("stems"))
        sg = seg.get("stem_gain_db", {})
        overlay = seg.get("overlay", False)
        xf = 0 if overlay else int(seg.get("xfade", X / SR) * SR)
        fi = 0 if overlay else int(seg.get("fade_in", xf / SR) * SR)
        fo = 0 if overlay else int(seg.get("fade_out", xf / SR) * SR)
        a = int(round(seg["start"] * SR)) - fi // 2
        b = int(round(seg["end"] * SR)) + fo // 2
        a0, b0 = max(a, 0), min(b, L)
        n = b - a
        if full is not None:
            src = full
        else:
            src = sum(parts[k] * db(sg.get(k, 0.0)) for k in parts)
        is_loop = not overlay and not any(k in seg["cue"] for k in NON_LOOP)
        # read position (seconds into the cue) at sample a
        if "anchor" in seg:
            pos = a / SR - seg["anchor"]
        else:
            pos = seg.get("offset", 0.0) - (seg["start"] - a / SR)
        if is_loop:
            y = tile(src, n, pos)
        else:
            k = int(round(pos * SR))
            if k < 0:
                src = np.concatenate([np.zeros((-k, 2)), src])
            else:
                src = src[k:]
            y = np.pad(src, ((0, max(0, n - len(src))), (0, 0)))[:n]
        y = y * db(seg.get("gain_db", 0.0))
        lin = seg.get("linear", False)
        ramp = (lambda k: (np.arange(k) / k)[:, None]) if lin else (lambda k: np.sin(0.5 * np.pi * np.arange(k) / k)[:, None])
        lin_r = lambda k: (np.arange(k) / k)[:, None]
        sin_r = lambda k: np.sin(0.5 * np.pi * np.arange(k) / k)[:, None]
        if fi:
            y[:fi] *= (lin_r if seg.get("linear_in", lin) else sin_r)(fi)
        if fo:
            y[-fo:] *= (lin_r if seg.get("linear_out", lin) else sin_r)(fo)[::-1]
        bed[a0:b0] += y[a0 - a:b0 - a]
    pk = 20 * np.log10(np.max(np.abs(bed)) + 1e-12)
    sf.write(out, bed, SR, subtype="PCM_24")
    print(f"wrote {out}  {L/SR:.1f}s  peak {pk:.1f} dBFS" + ("  !! over -1 dBFS, lower gains" if pk > -1 else ""))
