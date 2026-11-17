#!/usr/bin/env python3
"""Test mix: vo10.mp3 (untouched) + the three beds -> renders/testmix_600s.wav, then measure.

Prints: LUFS of VO alone vs the mix (ffmpeg ebur128), music loudness in speech vs in VO pauses,
SFX peaks vs the VO's local peaks, ambience under speech.
"""
import os
import subprocess
import sys

import numpy as np
import soundfile as sf
from scipy import signal

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from dsp import ROOT, AUDIO                             # noqa: E402
from loudness import _B1, _A1, _B2, _A2                 # noqa: E402
import place_sound as PS                                # noqa: E402
import shutil                                           # noqa: E402

FF = shutil.which("ffmpeg") or os.path.expanduser("~/.local/bin/ffmpeg")
# usage: measure_mix.py [--vo vo_intro.mp3 --beds assets/audio/intro --len 275.06 --out renders/testmix_intro.wav]
_a = lambda k, d: sys.argv[sys.argv.index(k) + 1] if k in sys.argv else d
VO = _a("--vo", "vo10.mp3")
B = os.path.join(ROOT, _a("--beds", os.path.join(AUDIO, "bed")))
SFX_ = "" if "--beds" in sys.argv else "_600s"
OUT = _a("--out", "renders/testmix_600s.wav")
PS.VO_FILE, PS.LEN = VO, float(_a("--len", "600"))
PS.N = int(PS.LEN * PS.SR)
vo_activity = PS.vo_activity


def ebu(path):
    r = subprocess.run([FF, "-hide_banner", "-i", path, "-af", "ebur128=peak=true", "-f", "null", "-"],
                       capture_output=True, text=True).stderr
    i = [l for l in r.splitlines() if l.strip().startswith("I:")][-1].split()[1]
    p = [l for l in r.splitlines() if l.strip().startswith("Peak:")][-1].split()[1]
    return float(i), float(p)


if __name__ == "__main__":
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    subprocess.run([FF, "-v", "error", "-y", "-i", os.path.join(ROOT, VO),
                    "-i", f"{B}/music_bed{SFX_}.wav", "-i", f"{B}/sfx{SFX_}.wav", "-i", f"{B}/ambience{SFX_}.wav",
                    "-filter_complex", "[0:a]aresample=48000[v];[v][1:a][2:a][3:a]amix=inputs=4:normalize=0:duration=first",
                    "-c:a", "pcm_s24le", OUT], check=True)
    for name, p in [("VO alone", os.path.join(ROOT, VO)), ("test mix", OUT),
                    ("music bed", f"{B}/music_bed{SFX_}.wav"), ("sfx", f"{B}/sfx{SFX_}.wav"),
                    ("ambience", f"{B}/ambience{SFX_}.wav")]:
        i, pk = ebu(p)
        print(f"{name:10s} {i:6.1f} LUFS-I   true peak {pk:6.1f} dBTP")

    act, pauses, vo = vo_activity()
    SR, h = 48000, 960
    kw = lambda x: signal.lfilter(_B2, _A2, signal.lfilter(_B1, _A1, x, axis=0), axis=0)

    def fp(x):
        y = kw(x)
        n = len(y) // h
        return (y[: n * h].reshape(n, h, -1) ** 2).mean(1).sum(1)
    m = sf.read(f"{B}/music_bed{SFX_}.wav")[0]
    s = sf.read(f"{B}/sfx{SFX_}.wav")[0]
    a = sf.read(f"{B}/ambience{SFX_}.wav")[0]
    n = min(len(act), len(m) // h)
    act = act[:n]
    body = np.zeros(n, bool)
    for p0, p1 in pauses:
        body[int((p0 + 0.5) / 0.02):int((p1 - 0.3) / 0.02)] = True
    L = lambda p: -0.691 + 10 * np.log10(p.mean() + 1e-20)
    pm, pv, pa = fp(m)[:n], fp(vo[: n * h])[:n], fp(a)[:n]
    print(f"VO while speaking        {L(pv[act]):6.1f} LUFS")
    print(f"music while VO speaks    {L(pm[act]):6.1f} LUFS  ({L(pm[act]) - L(pv[act]):+.1f} LU re VO)")
    print(f"music in VO pauses       {L(pm[body]):6.1f} LUFS  ({L(pm[body]) - L(pm[act]):+.1f} dB lift, {body.sum()*0.02:.1f} s)")
    print(f"ambience while speaking  {L(pa[act]):6.1f} LUFS")
    w = SR // 2
    d = lambda x: 20 * np.log10(x + 1e-9)
    ns = min(len(vo), len(s))                   # the beds may run past the VO (designed tail): compare the common span
    vp = np.array([np.abs(vo[i:i + w]).max() for i in range(0, ns - w, w)])
    sp = np.array([np.abs(s[i:i + w]).max() for i in range(0, ns - w, w)])
    k = min(len(vp), len(sp))
    vp, sp = vp[:k], sp[:k]
    sp_on, sp_speech = sp > 1e-4, (sp > 1e-4) & (vp > 10 ** (-30 / 20))
    print(f"VO 0.5 s peaks (speech)  median {np.median(d(vp[vp > 10**(-30/20)])):6.1f}  max {d(vp.max()):6.1f} dBFS")
    print(f"SFX 0.5 s peaks          median {np.median(d(sp[sp_on])):6.1f}  p90 {np.percentile(d(sp[sp_on]), 90):6.1f}  max {d(sp.max()):6.1f} dBFS")
    print(f"SFX under VO (speech)    median {np.median(d(sp[sp_speech]) - d(vp[sp_speech])):+.1f} dB re local VO peak, "
          f"{np.median(d(sp[sp_speech])) - d(vp.max()):+.1f} dB re VO max peak")
    print(f"SFX in VO pauses         median peak {np.median(d(sp[sp_on & ~(vp > 10**(-30/20))])):6.1f} dBFS")
