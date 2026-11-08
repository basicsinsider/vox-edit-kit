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

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from dsp import ROOT                                    # noqa: E402
import epidemic_bed as E                                 # noqa: E402

SR = 48000
HOP = 0.1


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
    ev = E.hop_energy(vo, 0.01)[int(a / 0.01):int(b / 0.01)]
    em = E.hop_energy(os.path.join(beds, "music_bed.wav"), 0.01)[int(a / 0.01):int(b / 0.01)]
    es = E.hop_energy(os.path.join(beds, "sfx.wav"), 0.01)[int(a / 0.01):int(b / 0.01)]
    n = min(len(ev), len(em), len(es)); ev, em, es = ev[:n], em[:n], es[:n]
    lb = E.window_lufs(ev, 0.4, 0.01)[::10]          # gated integrated loudness of the VO (BS.1770, 400 ms blocks, 100 ms hop)
    z = 10 ** ((lb + 0.691) / 10)
    keep = lb > -70
    rel = -0.691 + 10 * np.log10(z[keep].mean()) - 10
    vo_lufs = -0.691 + 10 * np.log10(z[keep & (lb > rel)].mean())
    if not quiet:
        print(f"VO {vo_lufs:.1f} LUFS-I over {a:.1f}–{b:.1f} s")
    res = {}
    stride = int(round(HOP / 0.01))
    for win in (0.4, 3.0):
        lv = E.window_lufs(ev, win, 0.01)[::stride]
        lm = E.window_lufs(em, win, 0.01)[::stride]
        lms = E.window_lufs(em + es, win, 0.01)[::stride]
        t = a + np.arange(len(lv)) * HOP
        spk = lv > vo_lufs - 15
        if win == 0.4:      # 'speaking' = real speech: the VO's 0.4 s level max-held over 0.5 s within 10 LU of its LUFS-I
            from scipy.ndimage import maximum_filter1d
            hold = maximum_filter1d(lv, 5)
            spk = (hold > vo_lufs - 10) & (lv > vo_lufs - 20)
            lv = hold       # compare with the local speech level (word gaps don't count as 'music above the voice')
        else:
            spk = lv > vo_lufs - 12
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
