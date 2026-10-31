#!/usr/bin/env python3
"""Per-act music level re the VO (MANUAL §10.8 balance check for a layered Epidemic bed).

  .venv/bin/python tools/audio/act_levels.py --vo vo_c1.mp3 --beds assets/audio/c1 --cues project/c1/music_cuesheet.json --len 602.86

Acts = the cue labels of the cue sheet, in order of their first layer; act i runs from its first layer start to the next
act's first start. For each act: K-weighted music loudness while the VO speaks, minus the VO's loudness while it speaks
in the same span (target ≈ −11…−20 LU, most acts −13…−16), and the music in the VO pauses. Reads only; writes nothing.
"""
import argparse
import json
import os
import sys

import numpy as np
import soundfile as sf
from scipy import signal

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from dsp import ROOT                                    # noqa: E402
from loudness import _B1, _A1, _B2, _A2                 # noqa: E402
import place_sound as PS                                # noqa: E402

ap = argparse.ArgumentParser()
ap.add_argument("--vo", required=True)
ap.add_argument("--beds", required=True)
ap.add_argument("--cues", required=True)
ap.add_argument("--len", type=float, required=True)
a = ap.parse_args()
PS.VO_FILE, PS.LEN = a.vo, a.len
PS.N = int(a.len * PS.SR)
act, pauses, vo = PS.vo_activity()
h = 960


def frames(x):
    y = signal.lfilter(_B2, _A2, signal.lfilter(_B1, _A1, x, axis=0), axis=0)
    n = len(y) // h
    return (y[: n * h].reshape(n, h, -1) ** 2).mean(1).sum(1)


pv = frames(vo)
del vo
m, _ = sf.read(os.path.join(ROOT, a.beds, "music_bed.wav"), dtype="float32")
pm = frames(m.astype(np.float64))
del m
n = min(len(pv), len(pm), len(act))
pv, pm, act = pv[:n], pm[:n], act[:n]
L = lambda p: -0.691 + 10 * np.log10(p.mean() + 1e-20) if len(p) else float("nan")
sheet = json.load(open(os.path.join(ROOT, a.cues)))
first, seen = {}, {}
for k, ly in enumerate(sheet["layers"]):
    c = ly.get("cue", "?")
    first[c] = min(first.get(c, 1e9), float(ly["start"]))
    seen.setdefault(c, k)
order = sorted(first, key=lambda c: (first[c], seen[c]))
order = [c for k, c in enumerate(order) if k + 1 == len(order) or first[order[k + 1]] > first[c]]   # same start: last wins
print(f"{'act':8s} {'span':>15s}  {'VO spk':>7s} {'music spk':>9s} {'re VO':>6s} {'pauses':>7s}")
for k, c in enumerate(order):
    t0 = first[c]
    t1 = first[order[k + 1]] if k + 1 < len(order) else a.len
    i0, i1 = int(t0 / 0.02), min(int(t1 / 0.02), n)
    sp = act[i0:i1]
    v, mu = L(pv[i0:i1][sp]), L(pm[i0:i1][sp])
    mp = L(pm[i0:i1][~sp])
    print(f"{c:8s} {t0:6.1f}–{t1:6.1f}  {v:7.1f} {mu:9.1f} {mu - v:+6.1f} {mp:7.1f}")
print(f"{'all':8s} {0:6.1f}–{a.len:6.1f}  {L(pv[act]):7.1f} {L(pm[act]):9.1f} {L(pm[act]) - L(pv[act]):+6.1f} {L(pm[~act]):7.1f}")
