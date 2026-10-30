#!/usr/bin/env python3
"""Synthesize the SFX palette (48 kHz / 24-bit WAV, every file peak-normalized to -6 dBFS).

Run:  python3 tools/audio/gen_sfx.py           -> assets/audio/sfx/*.wav
Everything is procedural (noise shaping, modal synthesis, impulse trains); seeds are fixed
so re-running reproduces the same files.
"""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(__file__))
from dsp import (SR, AUDIO, Manifest, lp, hp, bp, resonator, peaking, shaped_noise, noise, pan,
                 make_ir, reverb, xfade_loop, peak_norm, write, fade, db, env_ar)
from instruments import boom

SFX = os.path.join(AUDIO, "sfx")
LIC = "Original, synthesized (project-owned, no third-party material)."
SRC = "synthesized by tools/audio/gen_sfx.py"
man = Manifest("sfx")
ROOM = make_ir(rt60=0.35, lp_hz=7000, seed=21, early=True)


def R(seed):
    return np.random.default_rng(seed)


def trim_tail(y, floor_db=-62.0):
    """Drop the silent reverb tail (below floor relative to peak), then a 15 ms fade."""
    a = np.abs(y).max(axis=1) if y.ndim == 2 else np.abs(y)
    idx = np.where(a > a.max() * db(floor_db))[0]
    end = min(len(y), idx[-1] + int(0.01 * SR)) if len(idx) else len(y)
    return fade(y[:end], 0.0, 0.015)


def save(name, y, purpose, tags="", loop=False):
    y = np.asarray(y, float)
    if not loop:
        y = trim_tail(y)
    y = peak_norm(y, -6.0)
    write(os.path.join(SFX, name + ".wav"), y)
    man.add(f"sfx/{name}.wav", purpose, SRC, LIC, tags=tags)
    print(f"{name:34s} {len(y)/SR:6.2f}s")


def blank(dur, st=False):
    k = int(dur * SR)
    return np.zeros((k, 2)) if st else np.zeros(k)


def put(buf, y, t, g=1.0):
    i = int(t * SR)
    if i >= len(buf):
        return buf
    k = min(len(y), len(buf) - i)
    buf[i:i + k] += g * y[:k]
    return buf


def burst(rng, dur, lo, hi, tau, order=2):
    k = max(int(dur * SR), 8)
    x = rng.standard_normal(k) * np.exp(-np.arange(k) / (tau * SR))
    return bp(x, lo, hi, order)


def modal(freqs, amps, taus, dur, rng=None, phase=True):
    t = np.arange(int(dur * SR)) / SR
    y = np.zeros_like(t)
    rng = rng or R(0)
    for f, a, ta in zip(freqs, amps, taus):
        y += a * np.sin(2 * np.pi * f * t + (rng.uniform(0, 6.28) if phase else 0)) * np.exp(-t / ta)
    return y


def room(y, wet=0.12):
    st = y if y.ndim == 2 else pan(y, 0)
    return reverb(st, ROOM, wet)


def logbell(f, c, w):
    return np.exp(-0.5 * ((np.log(f + 1.0) - np.log(c)) / w) ** 2)


# ======================================================================= whooshes
def whoosh(dur, seed, lo=250, hi=2600, peak_at=0.62, width=0.75):
    rng = R(seed)

    def fr(t, f):
        u = np.clip(t / dur, 0, 1)
        shape = np.where(u < peak_at, (u / peak_at) ** 2.2, np.exp(-((u - peak_at) / (1 - peak_at)) * 4.0))
        c = lo * (hi / lo) ** shape
        tilt = (f + 200.0) ** -0.35
        return logbell(f, c, width) * shape * tilt

    L = shaped_noise(dur, fr, rng)
    Rr = shaped_noise(dur, fr, rng)
    u = np.linspace(-1, 1, len(L))
    p = 0.6 * np.tanh(2 * u)       # moves left -> right
    a = (p + 1) * np.pi / 4
    y = np.stack([L * np.cos(a) + 0.3 * Rr * np.sin(a), Rr * np.sin(a) + 0.3 * L * np.cos(a)], 1)
    y = hp(y, 90, 2)
    return fade(y, 0.01, 0.03)


# ======================================================================= paper
def friction(dur, rng, lo, hi, rate_lo=25, rate_hi=110, grit=0.5):
    """Paper/felt friction: band noise with fast random AM + micro grit."""
    k = int(dur * SR)
    x = bp(noise(k, rng, "pink"), lo, hi, 2)
    am = lp(rng.standard_normal(k), rate_hi, 2)
    am = np.abs(am) / (np.std(am) + 1e-9)
    am = (1 - grit) + grit * am
    grains = (rng.random(k) < 400 / SR) * rng.standard_normal(k)
    grains = bp(grains, max(lo, 1500), min(hi * 1.3, 15000), 2) * 4
    return x * am + grains * grit


def paper_slide(seed, dur=0.75):
    rng = R(seed)
    k = int(dur * SR)
    y = friction(dur, rng, 700, 9000, grit=0.35)
    t = np.arange(k) / SR
    env = np.clip(t / 0.12, 0, 1) ** 1.5 * np.clip((dur - t) / 0.18, 0, 1) ** 1.2
    y = y * env
    y = peaking(y, 2500, -4, 0.8)                       # keep the voice band soft
    tap = burst(rng, 0.02, 200, 2500, 0.004)
    y = put(y, tap, dur - 0.06, 0.6 * np.max(np.abs(y)) / (np.max(np.abs(tap)) + 1e-9))
    return room(y, 0.08)


def paper_rustle(seed, dur=1.0, rate=70):
    rng = R(seed)
    y = blank(dur)
    t = 0.0
    while t < dur - 0.03:
        u = t / dur
        dens = rate * np.sin(np.pi * u) ** 0.7 + 5
        t += rng.exponential(1 / dens)
        g = burst(rng, rng.uniform(0.003, 0.018), rng.uniform(900, 2500), rng.uniform(5000, 11000), rng.uniform(0.002, 0.006))
        put(y, g, t, rng.uniform(0.2, 1.0) * np.sin(np.pi * min(u, 1)) ** 0.5)
    bed = friction(dur, rng, 600, 7000, grit=0.2) * 0.15 * np.sin(np.pi * np.linspace(0, 1, len(y))) ** 1.5
    y = y / (np.max(np.abs(y)) + 1e-9) + bed
    return room(peaking(y, 2500, -3, 0.8), 0.1)


def photo_drop(seed, dur=0.5):
    rng = R(seed)
    y = blank(dur)
    puff = lp(rng.standard_normal(int(0.035 * SR)), 700, 2) * np.hanning(int(0.035 * SR)) * 0.4
    put(y, puff, 0.0)
    slap_t = 0.03
    body = modal([170, 390, 820], [1.0, 0.5, 0.25], [0.025, 0.015, 0.008], 0.15, rng)
    put(y, body, slap_t, 0.9)
    put(y, burst(rng, 0.006, 3000, 9000, 0.0012), slap_t, 0.5)
    put(y, burst(rng, 0.03, 300, 3000, 0.006), slap_t, 0.6)
    put(y, body * 0.3, slap_t + 0.055 + rng.uniform(0, 0.02))           # tiny bounce/settle
    put(y, burst(rng, 0.004, 3000, 9000, 0.001), slap_t + 0.058, 0.12)
    return room(y, 0.12)


def tape_rip(seed, dur=0.6):
    rng = R(seed)
    y = blank(dur)
    t, k = 0.0, 0
    while t < dur - 0.05:
        rate = 140 + 400 * (t / dur)
        t += rng.exponential(1 / rate)
        g = burst(rng, 0.0025, 1800, 10000, 0.0006)
        put(y, g, t, rng.uniform(0.3, 1.0) * min(1, t / 0.05))
    squeal = bp(noise(len(y), rng, "pink"), 2000, 7000, 2) * 0.08
    y = (y + squeal) * np.clip((dur - np.arange(len(y)) / SR) / 0.08, 0, 1)
    return room(peaking(y, 2800, -3, 0.9), 0.06)


def sticker_press(seed):
    rng = R(seed)
    y = blank(0.3)
    put(y, modal([140, 310], [1, 0.4], [0.03, 0.015], 0.12, rng), 0.0, 0.8)
    put(y, burst(rng, 0.03, 1500, 8000, 0.005), 0.0, 0.35)
    put(y, friction(0.12, rng, 1500, 8000, grit=0.4) * np.hanning(int(0.12 * SR)) * 0.25, 0.03)
    return room(y, 0.1)


# ======================================================================= map pins
def pop(seed, f0=950, f1=300, dur=0.18):
    rng = R(seed)
    k = int(dur * SR)
    t = np.arange(k) / SR
    f = f1 + (f0 - f1) * np.exp(-t / 0.012)
    y = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.035)
    a = int(0.002 * SR)
    y[:a] *= np.linspace(0, 1, a)
    put(y, burst(rng, 0.004, 2000, 8000, 0.0008), 0.0, 0.15)
    return room(y, 0.1)


def pin_drop(seed):
    rng = R(seed)
    y = blank(0.35)
    put(y, pop(seed, 1100, 380, 0.2)[:, 0], 0.0)
    put(y, modal([240, 610], [0.6, 0.25], [0.02, 0.01], 0.08, rng), 0.004)       # lands on the map board
    put(y, modal([3400, 5100], [0.08, 0.05], [0.03, 0.02], 0.1, rng), 0.004)     # tiny pin 'tink'
    return room(y, 0.1)


# ======================================================================= marker / highlighter
def felt_stroke(rng, dur, lo=1800, hi=8000, squeak=True, smooth=0.0):
    k = int(dur * SR)
    t = np.arange(k) / SR
    y = friction(dur, rng, lo, hi, rate_hi=160, grit=0.55 * (1 - smooth))
    if squeak:
        f = rng.uniform(2800, 4200)
        y = y + 0.6 * resonator(y, f, 14) + 0.3 * resonator(y, f * 1.5, 10)
    speed = np.sin(np.pi * np.clip(t / dur, 0, 1)) ** 0.6
    return y * speed


def marker(seed, strokes):
    """strokes: list of (start, dur)."""
    rng = R(seed)
    end = max(s + d for s, d in strokes) + 0.1
    y = blank(end)
    for s, d in strokes:
        put(y, felt_stroke(rng, d), s, rng.uniform(0.8, 1.0))
        put(y, burst(rng, 0.01, 400, 3000, 0.002), s, 0.25)      # tip touches paper
    y = peaking(y, 2500, -3, 0.7)
    return room(y, 0.06)


def highlighter(seed, dur=0.55):
    rng = R(seed)
    y = felt_stroke(rng, dur, 1200, 6500, squeak=False, smooth=0.6)
    y = lp(y, 7000, 2) + 0.15 * felt_stroke(rng, dur, 3000, 9000, squeak=True, smooth=0.7)
    y = put(y, burst(rng, 0.012, 300, 2000, 0.003), 0.0, 0.3)
    return room(peaking(y, 2500, -3, 0.7), 0.06)


# ======================================================================= typewriter
def type_key(seed):
    rng = R(seed)
    y = blank(0.22)
    put(y, burst(rng, 0.006, 300, 2500, 0.0015) + modal([150, 330], [0.4, 0.2], [0.012, 0.006], 0.006, rng)[:288], 0.0, 0.6)
    st = 0.012 + rng.uniform(0, 0.008)
    bar = modal([1850 * rng.uniform(0.95, 1.05), 2950, 4400, 6200], [0.5, 0.35, 0.25, 0.15],
                [0.02, 0.014, 0.01, 0.006], 0.08, rng)
    imp = burst(rng, 0.004, 1500, 12000, 0.0005)
    platen = modal([115, 260], [1.0, 0.4], [0.02, 0.01], 0.06, rng)
    put(y, imp, st)
    put(y, bar, st, 0.55)
    put(y, platen, st, 0.7)
    put(y, burst(rng, 0.004, 800, 5000, 0.001), st + 0.06 + rng.uniform(0, 0.02), 0.2)   # key release
    return room(y, 0.1)


def type_ding():
    rng = R(77)
    f = 2350
    y = modal([f, f * 2.76, f * 5.4, f * 0.5], [1.0, 0.4, 0.15, 0.08], [0.9, 0.35, 0.15, 0.4], 1.6, rng)
    y[:int(0.0015 * SR)] *= np.linspace(0, 1, int(0.0015 * SR))
    y = put(y, burst(rng, 0.004, 3000, 12000, 0.0006), 0.0, 0.4)
    return room(y, 0.15)


def type_return():
    rng = R(78)
    y = blank(0.75)
    t = 0.0
    while t < 0.45:
        t += 1 / rng.uniform(55, 75)
        put(y, burst(rng, 0.004, 1200, 7000, 0.0008) + 0 * t, t, 0.4 + 0.3 * t)
    put(y, friction(0.45, rng, 300, 3000, grit=0.3) * 0.2, 0.0)
    put(y, modal([95, 210, 1300], [1, 0.5, 0.2], [0.05, 0.03, 0.02], 0.2, rng), 0.5, 1.6)   # carriage thunk
    put(y, burst(rng, 0.006, 1000, 8000, 0.0012), 0.5, 0.6)
    return room(y, 0.12)


def type_burst(n=12, seed=500):
    rng = R(seed)
    y = blank(0.11 * n + 0.3, st=True)
    t = 0.0
    for i in range(n):
        k = type_key(seed + 1 + i)
        put(y, k, t, rng.uniform(0.7, 1.0))
        t += rng.uniform(0.075, 0.14)
    return y


# ======================================================================= ticker / odometer
def tick(seed, f=900, bright=1.0):
    rng = R(seed)
    y = burst(rng, 0.03, 2000, 7000, 0.0007) * bright
    y = y + 0.8 * resonator(burst(rng, 0.03, 300, 4000, 0.001), f, 12) * 3
    y += modal([f * 2.3], [0.15], [0.006], 0.03, rng)
    return y


def ticker_roll(dur, r0, r1, seed):
    rng = R(seed)
    y = blank(dur + 0.05)
    t, i = 0.0, 0
    while t < dur:
        u = t / dur
        rate = r0 * (r1 / r0) ** u
        put(y, tick(seed + i, f=880 + rng.uniform(-40, 40)), t, rng.uniform(0.75, 1.0) * (1 - 0.3 * u))
        t += 1 / rate
        i += 1
    return room(y, 0.08)


# ======================================================================= camera
def shutter_mech(seed=900, advance=False):
    rng = R(seed)
    dur = 0.95 if advance else 0.4
    y = blank(dur)
    # mirror up: thwack + body
    put(y, burst(rng, 0.006, 1500, 11000, 0.0009), 0.0, 0.8)
    put(y, modal([210, 470, 1150], [1.0, 0.5, 0.25], [0.03, 0.02, 0.01], 0.12, rng), 0.0, 0.9)
    # first curtain, second curtain (1/15 s)
    put(y, burst(rng, 0.004, 2500, 12000, 0.0006), 0.012, 0.6)
    put(y, burst(rng, 0.005, 2500, 12000, 0.0007), 0.078, 0.75)
    put(y, modal([260, 640], [0.6, 0.3], [0.02, 0.01], 0.08, rng), 0.078, 0.6)
    # mirror return + damped bounce
    put(y, modal([180, 420, 980], [1.0, 0.45, 0.2], [0.035, 0.02, 0.01], 0.15, rng), 0.105, 1.0)
    put(y, burst(rng, 0.006, 1200, 9000, 0.001), 0.105, 0.6)
    put(y, modal([200, 450], [0.3, 0.1], [0.02, 0.01], 0.06, rng), 0.135, 0.5)
    if advance:   # film-advance lever ratchet
        t = 0.36
        for i in range(13):
            put(y, resonator(burst(rng, 0.02, 1500, 9000, 0.0008), 1400, 8) * 3, t, 0.35 + 0.02 * i)
            t += 0.024 + rng.uniform(-0.003, 0.003)
        put(y, friction(0.32, rng, 500, 4000, grit=0.3) * 0.015, 0.36)
        put(y, modal([190, 520], [0.6, 0.2], [0.03, 0.012], 0.1, rng), t + 0.02, 0.8)
    y = hp(y, 60, 2)
    return room(y, 0.1)


# ======================================================================= projector
def projector(dur, seed=1000, spinup=False):
    rng = R(seed)
    k = int(dur * SR)
    t = np.arange(k) / SR
    if spinup:
        fps = 24 * (1 - np.exp(-t / 0.55))
    else:
        fps = np.full(k, 24.0)
    phase = np.cumsum(fps) / SR
    frames = np.floor(phase)
    y = np.zeros(k)
    idx = np.where(np.diff(frames) > 0)[0]
    half = np.where(np.diff(np.floor(phase + 0.5)) > 0)[0]
    claw = burst(rng, 0.02, 600, 5000, 0.0018) + resonator(burst(rng, 0.02, 200, 3000, 0.002), 520, 6) * 2
    sh = burst(rng, 0.008, 1500, 6000, 0.0012) * 0.4
    for i in idx:
        put(y, claw * rng.uniform(0.75, 1.0), i / SR)
    for i in half:
        put(y, sh * rng.uniform(0.6, 1.0), i / SR)
    run = np.clip(fps / 24, 0, 1)
    motor = sum(a * np.sin(2 * np.pi * f * t) for f, a in [(50, 0.25), (100, 0.35), (150, 0.12), (200, 0.08)])
    rattle = bp(noise(k, rng, "pink"), 500, 3000, 2) * (0.5 + 0.5 * np.abs(np.sin(np.pi * 24 * t)))
    fan = lp(noise(k, rng, "brown"), 900, 2) * 0.6
    y = y * 0.9 + (motor * 0.12 + rattle * 0.12) * run + fan * 0.12 * run
    y = peaking(y, 2500, -3, 0.8)
    st = np.stack([y + 0.15 * np.roll(y, 211), y + 0.15 * np.roll(y, 397)], 1)
    return st


# ======================================================================= CRT
def crt_on():
    rng = R(1100)
    dur = 2.4
    k = int(dur * SR)
    t = np.arange(k) / SR
    y = np.zeros(k)
    put(y, modal([85, 190, 900], [1, 0.4, 0.15], [0.06, 0.03, 0.01], 0.3, rng), 0.0, 1.0)     # relay clunk
    put(y, burst(rng, 0.008, 1000, 9000, 0.0015), 0.0, 0.7)
    # degauss 'thrum': 60 Hz buzz burst with harmonics, decaying
    dg = np.zeros(k)
    for h, a in [(1, 1), (2, 0.6), (3, 0.35), (4, 0.2), (6, 0.1)]:
        dg += a * np.sin(2 * np.pi * 60 * h * t)
    dg = np.tanh(2.5 * dg) * np.exp(-np.maximum(t - 0.08, 0) / 0.35) * (t > 0.08)
    y += dg * 0.45
    # HV crackle + 'tsiu'
    cr = (rng.random(k) < 600 / SR) * rng.standard_normal(k)
    cr = bp(cr, 2000, 12000, 2) * np.exp(-np.maximum(t - 0.25, 0) / 0.12) * (t > 0.25) * 3
    y += cr
    f = 1800 + 9000 * np.clip((t - 0.25) / 0.25, 0, 1)
    ts = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-np.maximum(t - 0.25, 0) / 0.08) * (t > 0.25) * 0.05
    y += ts
    # flyback whine 15.7 kHz (subtle) + settling hum
    wh = np.sin(2 * np.pi * 15734 * t) * np.clip((t - 0.3) / 0.4, 0, 1) * 0.02
    hum = (np.sin(2 * np.pi * 60 * t) * 0.6 + np.sin(2 * np.pi * 120 * t) * 0.3) * np.clip((t - 0.3) / 0.6, 0, 1) * 0.06
    y += wh + hum
    y = fade(y, 0.0, 0.5)
    return room(y, 0.08)


def crt_hum(dur=6.0):
    rng = R(1101)
    k = int(dur * SR)
    t = np.arange(k) / SR
    hum = np.sin(2 * np.pi * 60 * t) * 0.5 + np.sin(2 * np.pi * 120 * t) * 0.35 + np.sin(2 * np.pi * 180 * t) * 0.12
    hum *= 1 + 0.05 * np.sin(2 * np.pi * 0.3 * t)
    hiss = bp(noise(k, rng, "pink"), 3000, 12000, 2) * 0.04
    wh = np.sin(2 * np.pi * 15734 * t) * 0.012
    return np.stack([hum * 0.25 + hiss + wh, hum * 0.25 + np.roll(hiss, 999) + wh], 1)


def crt_off():
    rng = R(1102)
    dur = 0.7
    k = int(dur * SR)
    t = np.arange(k) / SR
    f = 3000 * np.exp(-t / 0.08) + 80
    y = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.12) * 0.3
    y += bp(rng.standard_normal(k), 2000, 10000, 2) * np.exp(-t / 0.04) * 0.3
    y = put(y, modal([90, 200], [1, 0.4], [0.05, 0.02], 0.2, rng), 0.0, 0.8)
    return room(y, 0.1)


# ======================================================================= UI
def ui_pop(seed, f0=520, f1=780):
    rng = R(seed)
    dur = 0.12
    k = int(dur * SR)
    t = np.arange(k) / SR
    f = f0 + (f1 - f0) * (1 - np.exp(-t / 0.015))
    y = np.sin(2 * np.pi * np.cumsum(f) / SR) * env_ar(k, 0.003, 0.03)
    y += 0.25 * np.sin(2 * np.pi * np.cumsum(2 * f) / SR) * env_ar(k, 0.002, 0.012)
    return room(y, 0.08)


def ui_tick(seed, f=1600):
    rng = R(seed)
    y = modal([f, f * 2.4], [1, 0.3], [0.012, 0.005], 0.06, rng)
    y[:int(0.0008 * SR)] *= np.linspace(0, 1, int(0.0008 * SR))
    put(y, burst(rng, 0.004, 4000, 10000, 0.0007), 0.0, 0.2)
    return room(y, 0.06)


# ======================================================================= impacts / risers
def impact(seed, dur, f0, f1, punch=0.5):
    rng = R(seed)
    y = boom(dur, f0, f1, 1.0, rng)
    y = put(y, burst(rng, 0.05, 80, 1200, 0.01), 0.0, punch)
    st = room(y, 0.15)
    return lp(st, 2500, 2)


def riser(dur, seed):
    rng = R(seed)

    def fr(t, f):
        u = np.clip(t / dur, 0, 1)
        c = 400 * (7000 / 400) ** (u ** 1.3)
        return logbell(f, c, 0.7) * (0.05 + u ** 2.5)
    nz = np.stack([shaped_noise(dur, fr, rng), shaped_noise(dur, fr, rng)], 1)
    k = int(dur * SR)
    t = np.arange(k) / SR
    u = t / dur
    f = 180 * 2 ** (2.2 * u ** 1.4)
    from dsp import saw_blep
    tone = (saw_blep(f, k) + saw_blep(f * 1.007, k) + saw_blep(f * 1.5, k) * 0.5) * (u ** 2.2)
    tone = lp(tone, 2200, 2)
    y = nz * 0.8 + pan(tone * 0.25, 0)
    y = peaking(y, 2500, -3, 0.8)
    return fade(y, 0.05, 0.02)


# ======================================================================= fire / wind / beds
def crackles(dur, rng, rate_fn, lo=1200, hi=9000):
    y = blank(dur)
    t = 0.0
    while t < dur:
        t += rng.exponential(1 / max(rate_fn(t), 0.5))
        if t >= dur:
            break
        a = rng.pareto(2.5) * 0.3
        g = burst(rng, rng.uniform(0.002, 0.012), rng.uniform(lo, lo * 2), rng.uniform(hi * 0.6, hi), rng.uniform(0.0006, 0.003))
        put(y, g, t, min(a, 1.5))
    return y


def fire(dur, seed, swell=True):
    rng = R(seed)
    k = int(dur * SR)
    t = np.arange(k) / SR
    env = np.sin(np.pi * np.clip(t / dur, 0, 1)) ** 0.8 if swell else np.ones(k)
    roar = lp(noise(k, rng, "brown"), 700, 2) * (0.6 + 0.4 * lp(np.abs(rng.standard_normal(k)), 4, 1) * 2)
    rate = (lambda tt: 8 + 90 * np.sin(np.pi * min(tt / dur, 1)) ** 0.8) if swell else (lambda tt: 45)
    cr = crackles(dur, rng, rate)
    flick = bp(noise(k, rng, "pink"), 800, 5000, 2) * lp(np.abs(rng.standard_normal(k)), 10, 1) * 2
    L = roar * 0.18 + cr * 1.8 + flick * 0.08
    cr2 = crackles(dur, rng, rate)
    Rr = np.roll(roar, 1234) * 0.18 + cr2 * 1.8 + np.roll(flick, 777) * 0.08
    y = np.stack([L, Rr], 1) * env[:, None]
    if swell:   # ignition whoosh at the head
        y = put(y, whoosh(0.6, seed + 1, 200, 1800, 0.35) * 0.6, 0.0)
    return peaking(y, 2500, -3, 0.8)


def wind(dur, seed):
    rng = R(seed)
    gust_a = lp(rng.standard_normal(int(dur * 50) + 10), 0.15, 1, sr=50)
    gust_a = (gust_a - gust_a.min()) / (np.ptp(gust_a) + 1e-9)

    def fr(t, f):
        g = np.interp(t, np.arange(len(gust_a)) / 50, gust_a)
        c = 280 + 650 * g
        return logbell(f, c, 0.9) * (0.35 + 0.65 * g) * (f + 50) ** -0.4
    y = np.stack([shaped_noise(dur, fr, rng, hop=512, nfft=4096), shaped_noise(dur, fr, rng, hop=512, nfft=4096)], 1)
    return lp(hp(y, 60, 2), 3000, 2)


def room_tone(dur, seed):
    rng = R(seed)
    k = int(dur * SR)
    y = np.stack([noise(k, rng, "brown") * 0.6 + noise(k, rng, "pink") * 0.15,
                  noise(k, rng, "brown") * 0.6 + noise(k, rng, "pink") * 0.15], 1)
    y = lp(hp(y, 40, 2), 2500, 2)
    return y


def vinyl(dur, seed):
    rng = R(seed)
    k = int(dur * SR)
    t = np.arange(k) / SR
    out = []
    for ch in range(2):
        hiss = bp(noise(k, rng, "pink"), 1500, 12000, 2) * 0.05
        dust = crackles(dur, rng, lambda tt: 180, 2500, 12000) * 0.25
        pops = crackles(dur, rng, lambda tt: 3, 300, 5000) * 0.8
        rumble = lp(noise(k, rng, "brown"), 60, 2) * 0.25 * (1 + 0.3 * np.sin(2 * np.pi * (33.333 / 60) * t))
        out.append(hiss + dust + pops + rumble)
    return np.stack(out, 1)


# ======================================================================= radio / oscillator
def radio_static(dur, seed):
    rng = R(seed)
    k = int(dur * SR)
    out = []
    for ch in range(2):
        s = bp(noise(k, rng, "white"), 300, 5500, 2)
        am = 0.6 + 0.4 * lp(rng.standard_normal(k), 18, 1) * 3
        cr = crackles(dur, rng, lambda tt: 25, 600, 5000) * 0.6
        out.append(np.tanh(1.5 * s * am) * 0.5 + cr)
    return np.stack(out, 1)


def radio_tune(dur=2.6, seed=1300):
    rng = R(seed)
    k = int(dur * SR)
    t = np.arange(k) / SR
    st = radio_static(dur, seed)[:, 0]
    u = t / dur
    fh = 3200 * np.exp(-6 * u) + 0.1
    whistle = np.sin(2 * np.pi * np.cumsum(fh) / SR) * 0.25 * np.clip(1 - u * 1.2, 0, 1)
    lock = np.clip((u - 0.7) / 0.15, 0, 1)
    carrier = np.sin(2 * np.pi * 440 * t) * 0.3 * lock
    y = st * (1 - 0.85 * lock) + whistle + carrier
    return fade(y, 0.05, 0.25)


def oscillator(kind):
    """Wien-bridge-style audio oscillator (HP 200A): near-pure sine, trace of 2nd/3rd harmonic,
    slow amplitude 'bounce' of the lamp stabilizer on frequency changes."""
    if kind == "sweep":
        dur = 3.5
        t = np.arange(int(dur * SR)) / SR
        f = 110 * (2000 / 110) ** np.clip(t / 3.0, 0, 1)
    elif kind == "steps":
        dur = 3.0
        t = np.arange(int(dur * SR)) / SR
        steps = np.array([200, 400, 800, 1600])
        tgt = steps[np.minimum((t / 0.75).astype(int), 3)]
        f = np.copy(tgt).astype(float)
        a = np.exp(-1 / (0.03 * SR))   # quick glide like turning the dial
        from scipy.signal import lfilter
        f = lfilter([1 - a], [1, -a], tgt.astype(float), zi=[tgt[0] * a])[0]
    else:
        dur = 4.0
        t = np.arange(int(dur * SR)) / SR
        f = np.full(len(t), 440.0)
    ph = 2 * np.pi * np.cumsum(f) / SR
    y = np.sin(ph) + 0.006 * np.sin(2 * ph) + 0.003 * np.sin(3 * ph)
    y *= 1 + 0.02 * np.sin(2 * np.pi * 1.7 * t) * np.exp(-t / 1.5)
    y += 0.002 * noise(len(t), R(5), "pink")   # tube/valve hiss floor
    return fade(y, 0.04, 0.2)



# ======================================================================= Phase-2 vocabulary additions
def pencil(seed, dur=0.7):
    """Graphite pencil scribble: lighter, drier and brighter than the felt marker, back-and-forth strokes."""
    rng = R(seed)
    k = int(dur * SR)
    t = np.arange(k) / SR
    y = friction(dur, rng, 2500, 11000, rate_hi=220, grit=0.75)
    rate = rng.uniform(5, 8)
    strokes = np.abs(np.sin(np.pi * rate * t + rng.uniform(0, 3))) ** 0.7
    y = y * (0.35 + 0.65 * strokes) * np.clip(t / 0.03, 0, 1) * np.clip((dur - t) / 0.05, 0, 1)
    return room(peaking(y, 3000, -3, 0.8), 0.05)


def string_pull(seed, dur=0.35):
    """Red string pulled taut between pins: quick fibre zip + tiny low twang."""
    rng = R(seed)
    from instruments import pizz
    y = blank(dur + 0.4)
    z = friction(dur, rng, 1200, 6000, rate_hi=300, grit=0.5)
    z *= np.linspace(0.2, 1, len(z)) ** 1.5
    put(y, z, 0.0, 0.5)
    tw = pizz(int(rng.integers(40, 46)), 0.6, "cello", rng, t60=0.25, maxdur=0.4)
    put(y, tw, dur - 0.02, 0.35 * np.max(np.abs(z)) / (np.max(np.abs(tw)) + 1e-9) * 2)
    return room(y, 0.08)


def cork_pin(seed):
    """Push-pin into a cork board: soft cork thock, short squeak of the pin, tiny metal tink."""
    rng = R(seed)
    y = blank(0.3)
    put(y, modal([300 * rng.uniform(0.9, 1.1), 720, 1500], [1, 0.4, 0.15], [0.02, 0.01, 0.006], 0.1, rng), 0.0)
    put(y, burst(rng, 0.03, 900, 3500, 0.008), 0.0, 0.35)
    put(y, modal([4300 * rng.uniform(0.95, 1.05)], [0.06], [0.02], 0.06, rng), 0.002)
    return room(y, 0.1)


def stamp(seed):
    """Rubber stamp hitting paper on a desk: thud + rubber slap + paper."""
    rng = R(seed)
    y = blank(0.6)
    put(y, boom(0.45, 120, 70, 1.0, rng), 0.0, 0.8)
    put(y, burst(rng, 0.04, 200, 2500, 0.008), 0.0, 0.8)
    put(y, modal([180, 420], [0.6, 0.3], [0.03, 0.015], 0.1, rng), 0.0, 0.6)
    put(y, burst(rng, 0.008, 2500, 9000, 0.0015), 0.002, 0.25)
    return room(y, 0.12)


def paper_tear(seed, dur=0.45):
    rng = R(seed)
    y = blank(dur + 0.05)
    t = 0.0
    while t < dur:
        t += rng.exponential(1 / (500 + 900 * t / dur))
        put(y, burst(rng, 0.0025, 1000, 9000, 0.0006), t, rng.uniform(0.3, 1.0))
    body = friction(dur, rng, 600, 6000, grit=0.5) * 0.3
    put(y, body, 0.0)
    y *= np.clip((dur + 0.05 - np.arange(len(y)) / SR) / 0.05, 0, 1) * np.clip(np.arange(len(y)) / SR / 0.02, 0, 1)
    return room(peaking(y, 2500, -3, 0.8), 0.06)


def chime_soft(seed=1400):
    """Soft vibraphone-like chime, D6 + A6 (in the score's key)."""
    rng = R(seed)
    y = blank(2.6)
    for i, f in enumerate([1174.66, 1760.0]):
        k = int(2.4 * SR)
        t = np.arange(k) / SR
        v = (np.sin(2 * np.pi * f * t) + 0.08 * np.sin(2 * np.pi * 4 * f * t) * np.exp(-t / 0.2)) * np.exp(-t / 0.9)
        v *= 1 + 0.15 * np.sin(2 * np.pi * 5.5 * t)
        v[:int(0.002 * SR)] *= np.linspace(0, 1, int(0.002 * SR))
        put(y, v, 0.07 * i, 0.8 - 0.25 * i)
    return room(y, 0.25)


def tone_blip(seed=1401, f=880):
    k = int(0.16 * SR)
    t = np.arange(k) / SR
    y = np.sin(2 * np.pi * f * t) + 0.01 * np.sin(4 * np.pi * f * t)
    return room(fade(y, 0.008, 0.04), 0.08)


def projector_click(seed):
    rng = R(seed)
    y = blank(0.25)
    put(y, burst(rng, 0.02, 600, 5000, 0.0018) + resonator(burst(rng, 0.02, 200, 3000, 0.002), 520, 6) * 2, 0.0)
    put(y, burst(rng, 0.02, 600, 5000, 0.0015) * 0.6, 1 / 24)
    put(y, modal([140, 330], [0.5, 0.2], [0.03, 0.01], 0.1, rng), 0.0)
    return room(y, 0.1)


def crt_click(seed=1103):
    """Short CRT power switch: relay clunk + click + brief degauss thrum (0.5 s)."""
    return crt_on()[: int(0.55 * SR)] * np.linspace(1, 0, int(0.55 * SR))[:, None] ** 2


def air_swell(seed, dur):
    rng = R(seed)

    def fr(t, f):
        u = np.clip(t / dur, 0, 1)
        env = np.sin(np.pi * u) ** 1.5 * (0.6 + 0.4 * u)
        c = 500 + 1500 * u
        return logbell(f, c, 1.0) * env * (f + 100.0) ** -0.3
    y = np.stack([shaped_noise(dur, fr, rng), shaped_noise(dur, fr, rng)], 1)
    return fade(lp(hp(y, 120, 2), 6000, 2), 0.05, 0.1)


# ======================================================================= main
if __name__ == "__main__":
    os.makedirs(SFX, exist_ok=True)
    save("whoosh_short_0p4s", whoosh(0.4, 11, 400, 3000, 0.55), "Soft short whoosh (moves L->R) for quick slides, label moves, small transitions.", "whoosh")
    save("whoosh_med_0p8s", whoosh(0.8, 12, 300, 2600), "Soft medium whoosh for scene pushes / image swaps.", "whoosh")
    save("whoosh_long_1p5s", whoosh(1.5, 13, 220, 2200, 0.65, 0.85), "Soft long airy whoosh for big moves (map zooms, camera flies).", "whoosh")
    for nm, args in [("short_0p4s", (0.4, 11, 400, 3000, 0.55)), ("med_0p8s", (0.8, 12, 300, 2600)),
                     ("long_1p5s", (1.5, 13, 220, 2200, 0.65, 0.85))]:
        save(f"whoosh_{nm}_RtoL", whoosh(*args)[:, ::-1], "Mirror of the L->R whoosh (moves right -> left) for leftward motion.", "whoosh")
    save("paper_slide_01", paper_slide(21), "Paper/photo sliding across a table (cutouts entering frame). Ends with a light tap.", "paper")
    save("paper_slide_02", paper_slide(22, 0.55), "Shorter paper slide variant.", "paper")
    save("paper_rustle_01", paper_rustle(31), "Paper rustle/handling (newspaper or document appearing).", "paper")
    save("paper_rustle_02", paper_rustle(32, 0.7, 90), "Shorter, busier rustle variant.", "paper")
    save("photo_drop_01", photo_drop(41), "Photo/card dropped flat on a table (image lands in collage).", "paper impact")
    save("photo_drop_02", photo_drop(42), "Photo drop variant (alternate so repeated drops don't sound identical).", "paper impact")
    save("tape_rip", tape_rip(51), "Tape pulled off a roll (tape strip on collage).", "tape")
    save("sticker_press", sticker_press(52), "Sticker / tape pressed down (cutout sticks on).", "tape")
    save("map_pin_pop_01", pop(61, 950, 300), "Soft bubble pop for map pins / markers appearing.", "map ui")
    save("map_pin_pop_02", pop(62, 1250, 420), "Higher pop variant (for second/third pins).", "map ui")
    save("map_pin_drop", pin_drop(63), "Pin dropping onto the map board: pop + tiny board tap + tink.", "map")
    save("marker_circle", marker(71, [(0.0, 0.85)]), "Felt-tip marker drawing a callout circle (one continuous scratchy stroke, ~0.85 s).", "marker")
    save("marker_arrow", marker(72, [(0.0, 0.5), (0.58, 0.14), (0.76, 0.14)]), "Marker drawing an arrow: shaft stroke then two short head strokes.", "marker")
    save("marker_underline", marker(73, [(0.0, 0.4)]), "Quick marker underline / tick stroke.", "marker")
    save("highlighter_swipe", highlighter(81), "Highlighter swipe across newspaper text (smooth, wider felt).", "marker")
    save("highlighter_swipe_short", highlighter(82, 0.35), "Short highlighter swipe (single word).", "marker")
    for i in range(6):
        save(f"typewriter_key_{i+1:02d}", type_key(100 + i), "Single typewriter keystroke (round-robin 01-06 for letter-by-letter text).", "typewriter")
    save("typewriter_ding", type_ding(), "Typewriter margin bell (end of a typed line/title).", "typewriter")
    save("typewriter_return", type_return(), "Carriage return: ratchet zip + thunk.", "typewriter")
    save("typewriter_burst_12keys", type_burst(), "12 keystrokes in a row (~1.4 s) for quick typed labels.", "typewriter")
    for i, f in enumerate([880, 940, 820]):
        save(f"ticker_tick_{i+1:02d}", room(tick(200 + i, f), 0.06), "Single odometer/ticker tick (mechanical counter digit flip).", "ticker")
    save("ticker_roll_fast_1s", ticker_roll(1.0, 26, 26, 210), "Constant fast odometer roll, 26 ticks/s (rolling numbers).", "ticker")
    save("ticker_roll_decel_2s", ticker_roll(2.0, 30, 4, 220), "Odometer roll that slows down and settles (30 -> 4 ticks/s): numbers counting up and landing.", "ticker")
    save("camera_shutter_mech", shutter_mech(900), "Mechanical SLR shutter: mirror slap, two curtains (1/15 s), mirror return. Better replacement for assets/sfx/shutter.wav.", "camera transition")
    save("camera_shutter_advance", shutter_mech(901, True), "Shutter + film-advance lever ratchet (~0.95 s) for a 'next photo' transition.", "camera transition")
    save("projector_loop_8s", xfade_loop(projector(8.5), int(0.5 * SR)), "Old 16mm film projector running at 24 fps: claw clatter, motor hum, fan. Seamless 8.0 s loop (192 frames).", "archival loop", loop=True)
    save("projector_start", projector(2.5, 1001, spinup=True), "Projector spinning up from stop to 24 fps (2.5 s) - start of an archival segment; crossfade into projector_loop_8s.", "archival")
    save("crt_power_on", crt_on(), "CRT TV power-on: relay clunk, degauss thrum, HV crackle, whine + hum settling.", "crt")
    save("crt_hum_loop_6s", xfade_loop(crt_hum(6.5), int(0.5 * SR)), "CRT running hum (60 Hz + faint 15.7 kHz flyback whine). Seamless 6.0 s loop.", "crt loop", loop=True)
    save("crt_power_off", crt_off(), "CRT power-off zap.", "crt")
    for i, (a, b) in enumerate([(520, 780), (660, 990), (440, 600)]):
        save(f"ui_pop_{i+1:02d}", ui_pop(300 + i, a, b), "Soft UI pop (label/number appearing).", "ui")
    for i, f in enumerate([1600, 2100]):
        save(f"ui_tick_{i+1:02d}", ui_tick(310 + i, f), "Soft wooden UI tick (list items, small labels).", "ui")
    save("impact_low_soft", impact(400, 1.6, 70, 42, 0.4), "Subtle low impact for big reveals (years/numbers) - mostly sub, little transient.", "impact")
    save("impact_low_deep", impact(401, 2.6, 58, 32, 0.6), "Deeper boom with longer tail for the biggest reveals.", "impact")
    save("impact_thud_short", impact(402, 0.6, 95, 55, 0.7), "Short tight thud (number lands / stamp).", "impact")
    save("riser_1s", riser(1.0, 500), "1 s riser (noise + tone) ending hard on the cut: place so its END is on the reveal frame.", "riser")
    save("riser_2s", riser(2.0, 501), "2 s riser; END lands on the cut.", "riser")
    save("fire_burn_reveal_3s", fire(3.0, 600), "Map film-burn reveal: ignition whoosh, crackle swell, roar, fade (3 s).", "fire map")
    save("fire_crackle_loop_8s", xfade_loop(fire(8.6, 601, swell=False), int(0.6 * SR)), "Steady fire crackle bed, seamless 8.0 s loop (under longer burn shots).", "fire loop", loop=True)
    save("wind_air_loop_30s", xfade_loop(wind(32.0, 700), int(2.0 * SR)), "Soft wind/air with slow gusts for drifting clouds over maps. Seamless 30 s loop.", "bed loop", loop=True)
    save("room_tone_loop_30s", xfade_loop(room_tone(31.0, 701), int(1.0 * SR)), "Neutral room tone (very low, dark). Seamless 30 s loop - glue under silent visuals.", "bed loop", loop=True)
    save("vinyl_crackle_loop_30s", xfade_loop(vinyl(31.6, 702), int(1.0 * SR)), "Vinyl surface noise: dust ticks, rare pops, hiss, 33 rpm rumble. Seamless 30.6 s loop (17 revolutions) for archival sections.", "bed loop archival", loop=True)
    save("radio_static_loop_6s", xfade_loop(radio_static(6.5, 1200), int(0.5 * SR)), "AM radio static, seamless 6 s loop.", "radio loop", loop=True)
    save("radio_tuning_sweep", radio_tune(), "Radio dial tuning: static + heterodyne whistle sweeping down, locks onto a clean 440 Hz carrier.", "radio")
    save("oscillator_sweep", oscillator("sweep"), "HP 200A-style audio oscillator sine sweeping 110 Hz -> 2 kHz (3 s) - 'the audio oscillator' beat.", "oscillator")
    save("oscillator_steps", oscillator("steps"), "Oscillator dial clicked through 200/400/800/1600 Hz (octave steps).", "oscillator")
    save("oscillator_tone_440", oscillator("tone"), "Steady 440 Hz test tone with soft fades (4 s).", "oscillator")
    # --- Phase 2 vocabulary additions
    for i, d in enumerate([0.7, 1.4]):
        save(f"pencil_scribble_{i+1:02d}", pencil(1500 + i, d), "Graphite pencil scribble/crosses/doodles (lighter than the marker).", "pencil")
    for i in range(2):
        save(f"string_pull_{i+1:02d}", string_pull(1510 + i), "Red string pulled taut between cork-board pins (zip + tiny twang).", "corkboard")
    for i in range(3):
        save(f"cork_pin_{i+1:02d}", cork_pin(1520 + i), "Push-pin into cork board.", "corkboard")
    for i in range(2):
        save(f"stamp_thud_{i+1:02d}", stamp(1530 + i), "Rubber stamp lands on paper (FLIPPED / POSTGRADUATE / card stamps).", "stamp impact")
    save("paper_tear_01", paper_tear(1540), "Paper tear / ticket rip.", "paper")
    save("chime_soft", chime_soft(), "Soft vibraphone chime D6+A6 (in key) - 'a good start' type button.", "chime")
    save("tone_blip", tone_blip(), "Short 880 Hz sine blip (oscillator/UI beep).", "oscillator ui")
    save("projector_click", projector_click(1550), "Single projector claw clack (cut into / out of film).", "archival")
    save("crt_click", crt_click(), "Short CRT power switch (relay clunk + click + brief thrum).", "crt")
    for d, nm in [(1.0, "1s"), (2.5, "2p5s"), (5.0, "5s")]:
        save(f"air_swell_{nm}", air_swell(1560, d), "Soft airy swell (room/air movement under fades, dollies, cross-dissolves).", "air")
    save("camera_shutter_mech_02", shutter_mech(902), "Shutter take 2 (round-robin with camera_shutter_mech).", "camera transition")
    save("camera_shutter_mech_03", shutter_mech(903), "Shutter take 3.", "camera transition")
    man.save()
