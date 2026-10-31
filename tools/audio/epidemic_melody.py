#!/usr/bin/env python3
"""Derive the MELODY stem the API can't deliver (MANUAL §10.3): melody = full − (bass + drums + instruments).
Streams in 10 s blocks (low memory), writes <name>_melody_derived.wav (24-bit) next to the stems and reports the
residual level so you can tell if the stems were sample-aligned (a clean melody stem is musical, not a comb-filtered mess).

  .venv/bin/python tools/audio/epidemic_melody.py assets/audio/epidemic/<name> [...]
"""
import os
import sys

import numpy as np
import soundfile as sf

for d in sys.argv[1:]:
    name = os.path.basename(d.rstrip("/"))
    full = os.path.join(d, f"{name}_full.wav")
    parts = [os.path.join(d, f"{name}_{s}.wav") for s in ("bass", "drums", "instruments")]
    parts = [p for p in parts if os.path.exists(p)]
    out = os.path.join(d, f"{name}_melody_derived.wav")
    F = sf.SoundFile(full)
    P = [sf.SoundFile(p) for p in parts]
    W = sf.SoundFile(out, "w", F.samplerate, F.channels, "PCM_24")
    blk = F.samplerate * 10
    e_full = e_mel = 0.0
    while True:
        a = F.read(blk, always_2d=True)
        if len(a) == 0:
            break
        m = a.copy()
        for p in P:
            b = p.read(len(a), always_2d=True)
            m[: len(b)] -= b
        W.write(np.clip(m, -1, 1))
        e_full += float((a ** 2).sum())
        e_mel += float((m ** 2).sum())
    W.close()
    print(f"{name}: melody_derived energy = {10*np.log10(e_mel/e_full+1e-12):+.1f} dB re full -> {out}")
