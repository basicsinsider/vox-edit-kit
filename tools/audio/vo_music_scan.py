#!/usr/bin/env python3
"""Window scan: is the music ever too close to the voice? (MANUAL §0 "Music never drowns the voice", §10.8)

  .venv/bin/python tools/audio/vo_music_scan.py --vo vo_py.wav --beds assets/audio/paraguay [--gap 12] [--from 0 --to 1621.87]

K-weighted (BS.1770) loudness of the VO, the music bed and music+sfx in sliding windows of 0.4 s (momentary) and 3 s (short-term),
every 0.1 s, only where the VO speaks (VO momentary > VO_LUFS − 15 LU). Lists every span where the music (or music+sfx) is less than
`--gap` LU under the VO, the worst windows, per-minute minima and the loudest music moments. Reads only; writes nothing.
"""
import argparse
import os
import sys

import numpy as np
import soundfile as sf
from scipy import signal

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from dsp import ROOT                                    # noqa: E402
from loudness import _B1, _A1, _B2, _A2   # noqa: E402

SR = 48000
HOP = 0.1


def kpow(path, a, b):
    """K-weighted channel-summed power per sample (float32) for path[a:b] seconds."""
    x, sr = sf.read(path, start=int(a * SR), frames=int((b - a) * SR), dtype="float32", always_2d=True)
    assert sr == SR, (path, sr)
    y = signal.lfilter(_B2, _A2, signal.lfilter(_B1, _A1, x, axis=0), axis=0)
    return (y.astype(np.float64) ** 2).sum(1)


def win_lufs(p, win):
    c = np.concatenate([[0.0], np.cumsum(p)])
    w, h = int(win * SR), int(HOP * SR)
    starts = np.arange(0, len(p) - w, h)
    m = (c[starts + w] - c[starts]) / w
    return -0.691 + 10 * np.log10(m + 1e-20), (starts + w / 2) / SR


def spans(mask, t, min_len=0.0):
    out, i = [], 0
    while i < len(mask):
        if mask[i]:
            j = i
            while j < len(mask) and mask[j]:
                j += 1
            if t[j - 1] - t[i] >= min_len:
                out.append((i, j))
            i = j
        else:
            i += 1
    return out


def scan(vo, beds, a, b, gap, quiet=False):
    pv = kpow(vo, a, b)
    pm = kpow(os.path.join(beds, "music_bed.wav"), a, b)
    ps = kpow(os.path.join(beds, "sfx.wav"), a, b)
    # gated integrated loudness of the VO from its 400 ms blocks (BS.1770 gating), reusing the K-weighted power
    lb, _ = win_lufs(pv, 0.4)
    z = 10 ** ((lb + 0.691) / 10)
    z1 = z[lb > -70]
    rel = -0.691 + 10 * np.log10(z1.mean()) - 10
    vo_lufs = -0.691 + 10 * np.log10(z1[lb[lb > -70] > rel].mean())
    if not quiet:
        print(f"VO {vo_lufs:.1f} LUFS-I over {a:.1f}–{b:.1f} s")
    res = {}
    for win in (0.4, 3.0):
        lv, t = win_lufs(pv, win)
        lm, _ = win_lufs(pm, win)
        lms, _ = win_lufs(pm + ps, win)
        t = t + a
        spk = lv > vo_lufs - 15
        dm, dms = lv - lm, lv - lms
        res[win] = (t, lv, lm, lms, spk, dm, dms)
        if quiet:
            continue
        for name, d in (("music", dm), ("music+sfx", dms)):
            bad = spk & (d < gap)
            sp = spans(bad, t)
            print(f"\n[{win:.1f} s windows, {name}] VO speaking {spk.mean()*100:.0f}% · median gap {np.median(d[spk]):.1f} LU · "
                  f"p5 {np.percentile(d[spk], 5):.1f} · min {d[spk].min():.1f} · windows < {gap:g} LU: {bad.sum()} "
                  f"({bad.sum()/max(1,spk.sum())*100:.1f}%) in {len(sp)} spans")
            worst = sorted(sp, key=lambda s: d[s[0]:s[1]].min())[:25]
            for i, j in sorted(worst):
                k = i + int(np.argmin(d[i:j]))
                print(f"   {t[i]:8.1f}–{t[j-1]:8.1f}  min gap {d[k]:5.1f} LU at {t[k]:.1f}  (VO {lv[k]:.1f}, {name} {(lm if name=='music' else lms)[k]:.1f})")
    if not quiet:
        t, lv, lm, lms, spk, dm, dms = res[3.0]
        print("\n[3 s] loudest music moments (LUFS-S):")
        idx = np.argsort(-lm)
        shown = []
        for k in idx:
            if all(abs(t[k] - s) > 5 for s in shown):
                shown.append(t[k])
                print(f"   {t[k]:8.1f}  music {lm[k]:.1f}  VO {lv[k]:.1f}  gap {dm[k]:.1f}")
            if len(shown) >= 12:
                break
        print("\n[3 s] per-minute min gap (music / music+sfx) while he speaks:")
        row = []
        for m0 in np.arange(np.floor(a / 60) * 60, b, 60):
            s = spk & (t >= m0) & (t < m0 + 60)
            if s.any():
                row.append(f"{int(m0//60):02d}:{dm[s].min():4.1f}/{dms[s].min():4.1f}")
        for i in range(0, len(row), 7):
            print("   " + "  ".join(row[i:i + 7]))
    return res


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--vo", default="vo_py.wav")
    ap.add_argument("--beds", default="assets/audio/paraguay")
    ap.add_argument("--gap", type=float, default=12.0)
    ap.add_argument("--from", dest="a", type=float, default=0.0)
    ap.add_argument("--to", dest="b", type=float, default=None)
    o = ap.parse_args()
    vo = os.path.join(ROOT, o.vo)
    b = o.b or sf.info(vo).duration
    scan(vo, os.path.join(ROOT, o.beds), o.a, b, o.gap)
