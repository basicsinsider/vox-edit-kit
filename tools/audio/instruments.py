"""Synth instruments: modal marimba, Karplus-Strong pizzicato, detuned-saw pad, sub boom."""
import numpy as np
from scipy import signal

from dsp import SR, lp, hp, resonator, saw_blep, midi_hz, env_ar


# ------------------------------------------------------------------ marimba
def marimba(midi, vel=0.8, rng=None, dark=0.0, maxdur=3.0):
    """Modal marimba bar: partials ~1 : 3.93 : 9.2 with fast-decaying overtones,
    a resonator-tube 'bloom' on the fundamental and a soft lowpassed mallet click.

    dark (0..1) = softer (yarn) mallet: fewer overtones, quieter click.
    """
    rng = rng or np.random.default_rng(int(midi * 100 + vel * 10))
    f = midi_hz(midi)
    tau1 = float(np.clip(0.62 * (262.0 / f) ** 0.65, 0.16, 1.25))
    nsamp = int(min(maxdur, tau1 * 7 + 0.05) * SR)
    t = np.arange(nsamp) / SR
    bright = (0.35 + 0.65 * vel) * (1 - 0.7 * dark)
    # tame overtones of high notes: they land right in the 1-4 kHz voice band
    hi_tame = float(np.clip(1.0 - (f - 500) / 1400, 0.35, 1.0))
    partials = [
        (1.0, 1.0, tau1),
        (1.0019, 0.12, tau1 * 0.8),                    # resonator beating
        (3.93, 0.30 * bright * hi_tame, tau1 / 4.2),
        (9.2, 0.15 * bright * bright, tau1 / 11.0),
        (16.0, 0.05 * bright * bright, tau1 / 20.0),
    ]
    y = np.zeros(nsamp)
    for ratio, amp, tau in partials:
        fr = f * ratio
        if fr > 16000:
            continue
        ph = rng.uniform(0, 2 * np.pi) if ratio != 1.0 else 0.0
        y += amp * np.sin(2 * np.pi * fr * t + ph) * np.exp(-t / tau)
    # resonator bloom: fundamental swells slightly after the strike
    y += 0.18 * np.sin(2 * np.pi * f * t) * (1 - np.exp(-t / 0.03)) * np.exp(-t / (tau1 * 1.3))
    # mallet: 1.2 ms rounded attack + soft click
    a = int(0.0012 * SR)
    y[:a] *= 0.5 - 0.5 * np.cos(np.pi * np.arange(a) / a)
    ck = int(0.006 * SR)
    click = rng.standard_normal(ck) * np.exp(-np.arange(ck) / (0.0012 * SR))
    click = lp(click, 2200 + 1500 * (1 - dark), 2)
    y[:ck] += click * 0.07 * vel * (1 - 0.6 * dark)
    # bright 'tick' of the mallet sits ABOVE the voice band (5-11 kHz)
    tk = int(0.003 * SR)
    tick = rng.standard_normal(tk) * np.exp(-np.arange(tk) / (0.0006 * SR))
    from dsp import bp
    y[:tk] += bp(tick, 5000, 11000, 2) * 0.10 * vel * (1 - 0.8 * dark)
    y *= vel
    return y


# ------------------------------------------------------------------ pizzicato
_BODIES = {
    "violin": [(290, 6, 0.6), (470, 7, 0.5), (1100, 5, 0.12)],
    "viola": [(230, 6, 0.6), (380, 7, 0.5), (900, 5, 0.12)],
    "cello": [(110, 6, 0.7), (190, 6, 0.6), (420, 5, 0.35)],
}


def pizz(midi, vel=0.8, body="violin", rng=None, t60=None, maxdur=2.5, tone=0.5):
    """Karplus-Strong pluck with an allpass fractional delay (accurate tuning),
    a lowpassed noise excitation (finger pluck, not pick) and a 3-mode body."""
    rng = rng or np.random.default_rng(int(midi * 77 + vel * 13))
    f = midi_hz(midi)
    P = SR / f
    N = int(np.floor(P - 0.5 - 0.1))
    d = P - 0.5 - N
    c = (1 - d) / (1 + d)
    if t60 is None:
        t60 = float(np.clip(1.4 * (110.0 / f) ** 0.5, 0.35, 1.6))
    g = 10 ** (-3.0 * P / (t60 * SR))
    a = np.zeros(N + 3)
    a[0] = 1.0
    a[1] += c
    a[N] -= g * 0.5 * c
    a[N + 1] -= g * 0.5 * (1 + c)
    a[N + 2] -= g * 0.5
    b = np.array([1.0, c])
    nsamp = int(min(maxdur, t60 * 1.2) * SR)
    exc_len = max(int(P), 8)
    exc = rng.standard_normal(exc_len)
    exc = lp(exc, min(f * (4 + 10 * tone * vel), 9000), 2)  # finger = dark pluck
    exc *= np.hanning(exc_len)
    x = np.zeros(nsamp)
    x[:exc_len] = exc
    y = signal.lfilter(b, a, x)
    # body
    out = 0.55 * y
    for fr, q, amp in _BODIES[body]:
        out += amp * resonator(y, fr, q)
    out = hp(out, 45 if body == "cello" else 140, 2)
    out = lp(out, 5200 if body != "cello" else 3200, 2)
    # finger "thup" on the attack
    k = int(0.004 * SR)
    out[:k] += lp(rng.standard_normal(k), 900, 2) * np.hanning(k) * 0.05
    e = np.ones(nsamp)
    r = int(0.05 * SR)
    e[-r:] = np.linspace(1, 0, r)
    out *= e
    pk = np.max(np.abs(out)) + 1e-9
    return out / pk * vel


# ------------------------------------------------------------------ pad / soft strings
def pad_note(midi, dur, vel=0.6, attack=1.4, release=2.2, cutoff=1300, rng=None, voices=3,
             detune_c=8.0, vibrato=0.0):
    """Detuned band-limited saws, lowpassed; returns stereo [n,2] of length dur+release."""
    rng = rng or np.random.default_rng(int(midi * 31))
    f = midi_hz(midi)
    total = dur + release
    nsamp = int(total * SR)
    t = np.arange(nsamp) / SR
    out = np.zeros((nsamp, 2))
    for v in range(voices):
        cents = (v - (voices - 1) / 2) * detune_c * 2 / max(voices - 1, 1)
        drift = 1 + 0.0006 * np.sin(2 * np.pi * (0.13 + 0.07 * v) * t + rng.uniform(0, 6.28))
        vib = 1 + vibrato * 0.004 * np.sin(2 * np.pi * 5.1 * t + rng.uniform(0, 6.28))
        fr = f * 2 ** (cents / 1200) * drift * vib
        s = saw_blep(fr, nsamp, rng.uniform(0, 1))
        p = (v - (voices - 1) / 2) / max((voices - 1) / 2, 1) * 0.8
        ang = (p + 1) * np.pi / 4
        out[:, 0] += s * np.cos(ang)
        out[:, 1] += s * np.sin(ang)
    out = lp(out, cutoff, 4)
    out = hp(out, 70, 2)
    # amp envelope: slow attack, hold, release
    env = np.ones(nsamp)
    a = int(attack * SR)
    env[:a] = np.sin(0.5 * np.pi * np.arange(a) / a) ** 2
    rs = int(dur * SR)
    if rs < nsamp:
        rr = np.arange(nsamp - rs) / SR
        env[rs:] *= np.exp(-rr / (release / 4.0))
    return out * env[:, None] * vel / voices


def boom(dur=2.5, f0=62, f1=38, vel=1.0, rng=None):
    """Sub drop: pitch-falling sine + body thump, for reveal stingers."""
    rng = rng or np.random.default_rng(3)
    nsamp = int(dur * SR)
    t = np.arange(nsamp) / SR
    fr = f1 + (f0 - f1) * np.exp(-t / 0.25)
    ph = 2 * np.pi * np.cumsum(fr) / SR
    y = np.sin(ph) * np.exp(-t / (dur / 4.0))
    y += 0.4 * np.sin(2 * ph) * np.exp(-t / 0.15)
    th = lp(rng.standard_normal(nsamp), 300, 2) * np.exp(-t / 0.03) * 0.5
    y = y + th
    a = int(0.004 * SR)
    y[:a] *= np.linspace(0, 1, a)
    return y * vel / np.max(np.abs(y))
