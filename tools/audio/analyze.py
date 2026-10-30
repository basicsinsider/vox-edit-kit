#!/usr/bin/env python3
"""'Listen' by measurement: level, loudness, band balance, loop seams, clipping.

python3 tools/audio/analyze.py [files...]   (default: every wav under assets/audio/{music,sfx})
Bands: weight <250 Hz | mud 250-1k | VOICE 1-4k | edge 4-10k | air >10k (share of energy, dB re total)
seam  = |last-first| sample jump relative to local RMS (loops: should be ~<1)
"""
import glob
import os
import sys

import numpy as np
import soundfile as sf

sys.path.insert(0, os.path.dirname(__file__))
from dsp import AUDIO
from loudness import integrated_lufs

BANDS = [(20, 250), (250, 1000), (1000, 4000), (4000, 10000), (10000, 24000)]


def bands(x, sr):
    m = x.mean(1) if x.ndim == 2 else x
    m = m[: sr * 60]
    S = np.abs(np.fft.rfft(m * np.hanning(len(m)))) ** 2
    f = np.fft.rfftfreq(len(m), 1 / sr)
    tot = S[(f > 20)].sum() + 1e-20
    return [10 * np.log10(S[(f >= a) & (f < b)].sum() / tot + 1e-12) for a, b in BANDS]


def analyze(p):
    x, sr = sf.read(p, always_2d=True)
    dur = len(x) / sr
    pk = 20 * np.log10(np.max(np.abs(x)) + 1e-12)
    lu = integrated_lufs(x, sr)
    b = bands(x, sr)
    rms = np.sqrt(np.mean(x[: int(0.05 * sr)] ** 2) + np.mean(x[-int(0.05 * sr):] ** 2)) + 1e-9
    seam = float(np.max(np.abs(x[-1] - x[0])) / rms)
    return dict(name=os.path.relpath(p, AUDIO), dur=dur, sr=sr, ch=x.shape[1], peak=pk, lufs=lu, bands=b, seam=seam)


if __name__ == "__main__":
    files = sys.argv[1:] or sorted(glob.glob(os.path.join(AUDIO, "music", "**", "*.wav"), recursive=True)
                                   + glob.glob(os.path.join(AUDIO, "sfx", "*.wav")))
    print(f"{'file':62s} {'dur':>6s} {'peak':>6s} {'LUFS':>6s} | {'<250':>5s} {'.25-1k':>6s} {'1-4k':>5s} {'4-10k':>5s} {'>10k':>5s} | seam")
    for p in files:
        r = analyze(p)
        print(f"{r['name'][:62]:62s} {r['dur']:6.2f} {r['peak']:6.1f} {r['lufs']:6.1f} | "
              + " ".join(f"{v:5.1f}" if i != 1 else f"{v:6.1f}" for i, v in enumerate(r['bands']))
              + f" | {r['seam']:.2f}" + ("  !CLIP" if r['peak'] > -0.1 else "") + ("" if r['sr'] == 48000 else "  !SR"))
