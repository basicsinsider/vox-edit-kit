"""Shared DSP helpers for the taiwan-edit sound library (48 kHz, numpy/scipy only).

Everything here is deterministic given a seed, so the generators can be re-run
and produce bit-identical files.
"""
import json
import os

import numpy as np
import soundfile as sf
from scipy import signal

SR = 48000
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
AUDIO = os.path.join(ROOT, "assets", "audio")


# ---------------------------------------------------------------- basics
def t_axis(dur, sr=SR):
    return np.arange(int(round(dur * sr))) / sr


def db(x):
    return 10 ** (x / 20.0)


def midi_hz(m):
    return 440.0 * 2 ** ((m - 69) / 12.0)


NOTE = {"C": 0, "C#": 1, "Db": 1, "D": 2, "D#": 3, "Eb": 3, "E": 4, "F": 5, "F#": 6,
        "Gb": 6, "G": 7, "G#": 8, "Ab": 8, "A": 9, "A#": 10, "Bb": 10, "B": 11}


def n(name):
    """'D4' -> midi number."""
    if name[1:2] in ("#", "b"):
        p, o = name[:2], name[2:]
    else:
        p, o = name[:1], name[1:]
    return 12 * (int(o) + 1) + NOTE[p]


def env_ar(nsamp, attack, release_tau, sr=SR):
    """Raised-cosine attack then exponential decay (tau seconds)."""
    t = np.arange(nsamp) / sr
    a = max(int(attack * sr), 1)
    e = np.exp(-np.maximum(t - attack, 0) / max(release_tau, 1e-4))
    e[:a] *= 0.5 - 0.5 * np.cos(np.pi * np.arange(min(a, nsamp)) / a)
    return e


def fade(x, fin=0.0, fout=0.0, sr=SR):
    x = x.copy()
    if fin > 0:
        k = min(int(fin * sr), x.shape[0])
        x[:k] *= (np.sin(0.5 * np.pi * np.arange(k) / k) ** 2)[:, None] if x.ndim == 2 else np.sin(0.5 * np.pi * np.arange(k) / k) ** 2
    if fout > 0:
        k = min(int(fout * sr), x.shape[0])
        r = np.cos(0.5 * np.pi * np.arange(k) / k) ** 2
        x[-k:] *= r[:, None] if x.ndim == 2 else r
    return x


# ---------------------------------------------------------------- filters
def _sos(kind, f, order=2, sr=SR):
    return signal.butter(order, f, btype=kind, fs=sr, output="sos")


def lp(x, f, order=2, sr=SR):
    return signal.sosfilt(_sos("lowpass", min(f, sr * 0.49), order, sr), x, axis=0)


def hp(x, f, order=2, sr=SR):
    return signal.sosfilt(_sos("highpass", f, order, sr), x, axis=0)


def bp(x, lo, hi, order=2, sr=SR):
    return signal.sosfilt(_sos("bandpass", [lo, min(hi, sr * 0.49)], order, sr), x, axis=0)


def peaking(x, f0, gain_db, q=1.0, sr=SR):
    """RBJ peaking EQ."""
    A = 10 ** (gain_db / 40)
    w0 = 2 * np.pi * f0 / sr
    alpha = np.sin(w0) / (2 * q)
    b = [1 + alpha * A, -2 * np.cos(w0), 1 - alpha * A]
    a = [1 + alpha / A, -2 * np.cos(w0), 1 - alpha / A]
    return signal.lfilter(np.array(b) / a[0], np.array(a) / a[0], x, axis=0)


def highshelf(x, f0, gain_db, sr=SR):
    A = 10 ** (gain_db / 40)
    w0 = 2 * np.pi * f0 / sr
    alpha = np.sin(w0) / 2 * np.sqrt(2)
    cw = np.cos(w0)
    b = [A * ((A + 1) + (A - 1) * cw + 2 * np.sqrt(A) * alpha), -2 * A * ((A - 1) + (A + 1) * cw),
         A * ((A + 1) + (A - 1) * cw - 2 * np.sqrt(A) * alpha)]
    a = [(A + 1) - (A - 1) * cw + 2 * np.sqrt(A) * alpha, 2 * ((A - 1) - (A + 1) * cw),
         (A + 1) - (A - 1) * cw - 2 * np.sqrt(A) * alpha]
    return signal.lfilter(np.array(b) / a[0], np.array(a) / a[0], x, axis=0)


def resonator(x, f0, q, sr=SR):
    """Narrow 2-pole bandpass resonance (constant 0 dB peak)."""
    b, a = signal.iirpeak(f0, q, fs=sr)
    return signal.lfilter(b, a, x, axis=0)


def voice_pocket(x):
    """The static 'leave room for the narrator' EQ every music file gets.

    Gentle, wide dips — the dynamic carve in HyperFrames does the rest.
    """
    x = hp(x, 38, 2)
    x = peaking(x, 1300, -2.0, 0.9)
    x = peaking(x, 2800, -4.5, 0.8)
    x = highshelf(x, 6000, 4.0)   # give back sparkle ABOVE the voice band so the marimba stays bright
    return x


# ---------------------------------------------------------------- noise
def noise(nsamp, rng, color="white"):
    w = rng.standard_normal(nsamp)
    if color == "white":
        return w
    W = np.fft.rfft(w)
    f = np.fft.rfftfreq(nsamp, 1 / SR)
    f[0] = f[1]
    if color == "pink":
        W /= np.sqrt(f)
    elif color == "brown":
        W /= f
    y = np.fft.irfft(W, nsamp)
    return y / (np.std(y) + 1e-12)


def shaped_noise(dur, frames, rng, hop=256, nfft=2048):
    """Time-varying spectral noise.

    frames(t, f) -> magnitude; called with t shaped [1, T] and f shaped [F, 1]
    (broadcasting), result is broadcast to [F, T].
    Random phase per bin; overlap-add via ISTFT.
    """
    nsamp = int(dur * SR)
    nfr = nsamp // hop + 2
    f = np.fft.rfftfreq(nfft, 1 / SR)
    t = np.arange(nfr) * hop / SR
    mag = np.broadcast_to(frames(t[None, :], f[:, None]), (len(f), len(t))).astype(float)
    ph = rng.uniform(0, 2 * np.pi, mag.shape)
    _, y = signal.istft(mag * np.exp(1j * ph), fs=SR, nperseg=nfft, noverlap=nfft - hop)
    y = y[:nsamp]
    if len(y) < nsamp:
        y = np.pad(y, (0, nsamp - len(y)))
    return y / (np.max(np.abs(y)) + 1e-12)


# ---------------------------------------------------------------- oscillators
def saw_blep(freq, nsamp, phase0=0.0, sr=SR):
    """Band-limited saw (polyBLEP), freq scalar or array."""
    dt = np.broadcast_to(np.asarray(freq, float) / sr, (nsamp,))
    ph = (phase0 + np.cumsum(dt)) % 1.0
    y = 2 * ph - 1
    m1 = ph < dt
    tt = ph[m1] / dt[m1]
    y[m1] -= tt + tt - tt * tt - 1
    m2 = ph > 1 - dt
    tt = (ph[m2] - 1) / dt[m2]
    y[m2] -= tt * tt + tt + tt + 1
    return y


# ---------------------------------------------------------------- reverb
def make_ir(rt60=1.8, dur=None, predelay=0.012, lp_hz=6000, seed=7, width=1.0, early=True):
    rng = np.random.default_rng(seed)
    dur = dur or rt60 * 1.1
    ns = int(dur * SR)
    t = np.arange(ns) / SR
    env = np.exp(-6.91 * t / rt60)
    irs = []
    for ch in range(2):
        w = rng.standard_normal(ns) * env
        # darker tail: lowpass increases over time by mixing two filtered versions
        dark = lp(w, lp_hz * 0.35, 2)
        bright = lp(w, lp_hz, 2)
        mixw = np.clip(t / rt60, 0, 1)
        w = bright * (1 - mixw) + dark * mixw
        w = hp(w, 120, 2)
        if early:
            er = np.zeros(ns)
            for k in range(10):
                pos = int((0.004 + rng.uniform(0, 0.05)) * SR)
                er[pos] += rng.uniform(-0.6, 0.6) * (1 - k / 12)
            w = w + er * 2.0
        pd = np.zeros(int(predelay * SR))
        irs.append(np.concatenate([pd, w]))
    ir = np.stack(irs, 1)
    m = ir.mean(1, keepdims=True)
    ir = m + (ir - m) * width
    return ir / np.sqrt(np.sum(ir ** 2) / 2)


def reverb(x, ir, wet=0.2):
    """x: stereo [n,2]. Returns dry + wet with tail appended."""
    if x.ndim == 1:
        x = np.stack([x, x], 1)
    tail = ir.shape[0]
    y = np.zeros((x.shape[0] + tail - 1, 2))
    for c in range(2):
        y[:, c] = signal.fftconvolve(x[:, c], ir[:, c])
    out = np.zeros_like(y)
    out[: x.shape[0]] += x
    return out + wet * y


def pan(x, p):
    """mono -> stereo, p in [-1, 1], equal-power."""
    a = (p + 1) * np.pi / 4
    return np.stack([x * np.cos(a), x * np.sin(a)], 1)


# ---------------------------------------------------------------- loops / io
def wrap_tail(x, loop_len):
    """Fold everything after loop_len back onto the start => seamless loop."""
    y = x[:loop_len].copy()
    rest = x[loop_len:]
    while len(rest):
        k = min(len(rest), loop_len)
        y[:k] += rest[:k]
        rest = rest[k:]
    return y


def xfade_loop(x, overlap):
    """Make a seamless loop of len(x)-overlap by crossfading the end into the start."""
    k = overlap
    body = x[:-k].copy()
    end = x[-k:]
    w = np.sin(0.5 * np.pi * np.arange(k) / k)
    if x.ndim == 2:
        w = w[:, None]
    body[:k] = body[:k] * w + end * np.sqrt(1 - w ** 2)
    return body


def peak_norm(x, target_db=-6.0):
    pk = np.max(np.abs(x))
    return x * (db(target_db) / pk) if pk > 0 else x


def write(path, x, sr=SR):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    x = np.asarray(x, dtype=np.float64)
    if np.max(np.abs(x)) > 1.0:
        raise ValueError(f"{path} would clip: peak {np.max(np.abs(x)):.3f}")
    sf.write(path, x, sr, subtype="PCM_24")


class Manifest:
    """Each generator records metadata for LIBRARY.md."""

    def __init__(self, name):
        self.path = os.path.join(ROOT, "tools", "audio", "_manifests", f"{name}.json")
        self.items = []

    def add(self, rel, purpose, source, license_, attribution="", tags=""):
        self.items.append(dict(file=rel, purpose=purpose, source=source, license=license_,
                               attribution=attribution, tags=tags))

    def save(self):
        with open(self.path, "w") as f:
            json.dump(self.items, f, indent=1)
