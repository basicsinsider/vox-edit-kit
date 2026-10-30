#!/usr/bin/env python3
"""Compose + render the original marimba / pizzicato / pad documentary score.

All cues live in one key family (D major / B minor / G major) so they crossfade.
Every cue is written as separate stems (marimba, pizz, pad[, low]) plus a full mix;
stems are rendered with the same gain as the mix, so stems summed == mix.

Run:  python3 tools/audio/gen_music.py            (all cues)
      python3 tools/audio/gen_music.py curious    (one cue)
Output: assets/audio/music/<cue>/...
"""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(__file__))
from dsp import (SR, AUDIO, Manifest, n, make_ir, reverb, pan, voice_pocket, wrap_tail,
                 write, fade, db, lp)
from instruments import marimba, pizz, pad_note, boom
from loudness import integrated_lufs

MUSIC = os.path.join(AUDIO, "music")
TARGET_LUFS = -18.0          # library level; the edit sets the real level (see MIX_RULES.md)
LICENSE = "Original composition, synthesized — no third-party material. Free to use (project-owned)."
IR = make_ir(rt60=2.1, lp_hz=5500, seed=11)
IR_SHORT = make_ir(rt60=1.2, lp_hz=6000, seed=12)


def N(*names):
    return [n(x) for x in names]


# chord = (bass, pad voicing, arp tones)
CH = {
    "Dmaj9": (n("D2"), N("D3", "A3", "C#4", "E4", "F#4"), N("D4", "F#4", "A4", "C#5", "E5", "A5")),
    "Bm11": (n("B1"), N("B2", "F#3", "A3", "D4", "E4"), N("B3", "D4", "F#4", "A4", "D5", "E5")),
    "Gmaj7": (n("G1"), N("G2", "D3", "F#3", "B3", "D4"), N("G4", "B4", "D5", "F#5", "B5", "D6")),
    "Asus4": (n("A1"), N("A2", "E3", "A3", "D4", "E4"), N("A4", "D5", "E5", "A5", "D6", "E6")),
    "A": (n("A1"), N("A2", "E3", "A3", "C#4", "E4"), N("A4", "C#5", "E5", "A5", "C#6", "E6")),
    "Em9": (n("E2"), N("E3", "B3", "D4", "F#4", "G4"), N("E4", "G4", "B4", "D5", "F#5", "B5")),
    "D/F#": (n("F#2"), N("F#3", "A3", "C#4", "D4"), N("F#4", "A4", "C#5", "D5", "F#5", "A5")),
    "A/C#": (n("C#2"), N("C#3", "E3", "A3", "E4"), N("A4", "C#5", "E5", "A5", "C#6", "E6")),
    "D": (n("D2"), N("D3", "A3", "D4", "F#4"), N("D4", "F#4", "A4", "D5", "F#5", "A5")),
    "Bm": (n("B1"), N("B2", "F#3", "B3", "D4"), N("B3", "D4", "F#4", "B4", "D5", "F#5")),
    "G": (n("G1"), N("G2", "D3", "G3", "B3", "D4"), N("G4", "B4", "D5", "G5", "B5", "D6")),
    "Em": (n("E2"), N("E3", "B3", "E4", "G4"), N("E4", "G4", "B4", "E5", "G5", "B5")),
    "F#sus": (n("F#1"), N("F#2", "C#3", "F#3", "B3", "C#4"), N("F#4", "B4", "C#5", "F#5")),
    "F#": (n("F#1"), N("F#2", "C#3", "F#3", "A#3", "C#4"), N("F#4", "A#4", "C#5", "F#5")),
    "Bm(b6)": (n("B1"), N("B2", "F#3", "G3", "D4"), N("B3", "D4", "F#4", "G4", "B4", "D5")),
    # G-major colour for the historic cue
    "Gadd9": (n("G1"), N("G2", "D3", "A3", "B3", "D4"), N("G4", "A4", "B4", "D5", "G5")),
    "Em7": (n("E2"), N("E3", "B3", "D4", "G4"), N("E4", "G4", "B4", "D5", "E5")),
    "Cmaj7": (n("C2"), N("C3", "G3", "B3", "E4"), N("C5", "E5", "G5", "B5")),
    "D7sus": (n("D2"), N("D3", "A3", "C4", "G4"), N("D5", "G5", "A5", "C6")),
    "D7": (n("D2"), N("D3", "A3", "C4", "F#4"), N("D5", "F#5", "A5", "C6")),
    "G/B": (n("B1"), N("B2", "D3", "G3", "B3", "D4"), N("G4", "B4", "D5", "G5")),
    "Am7": (n("A1"), N("A2", "E3", "G3", "C4", "E4"), N("A4", "C5", "E5", "G5")),
}
SCALE_G = [n(x) for x in ("D4", "E4", "F#4", "G4", "A4", "B4", "C5", "D5", "E5")]


class Cue:
    def __init__(self, name, bpm, beats_per_bar, seed):
        self.name, self.bpm, self.bpb = name, bpm, beats_per_bar
        self.beat = 60.0 / bpm
        self.rng = np.random.default_rng(seed)
        self.ev = {"marimba": [], "pizz": [], "pad": [], "low": []}

    def at(self, bar, beat):
        return (bar * self.bpb + beat) * self.beat

    def jitter(self, s=0.004):
        return float(self.rng.normal(0, s))

    def mar(self, t, m, v, dark=0.0, p=None):
        self.ev["marimba"].append(("mar", t + self.jitter(), m, v * self.rng.uniform(0.9, 1.05), dark, p))

    def pz(self, t, m, v, body, p=None, t60=None):
        self.ev["pizz"].append(("pz", t + self.jitter(0.006), m, v * self.rng.uniform(0.88, 1.05), body, p, t60))

    def pad(self, t, notes, dur, v=0.5, cutoff=1300, attack=1.2, release=2.2, vib=0.0):
        self.ev["pad"].append(("pad", t, notes, dur, v, cutoff, attack, release, vib))

    def roll(self, t, m, dur, v0, v1, rate=13.0, dark=0.3):
        k = int(dur * rate)
        for i in range(k):
            vv = v0 + (v1 - v0) * i / max(k - 1, 1)
            self.mar(t + i / rate + self.jitter(0.006), m, vv, dark, None)

    # ------------------------------------------------------------ render
    def render(self, length, loop=True, tail=5.0):
        total = int((length + tail) * SR)
        stems = {}
        for stem, evs in self.ev.items():
            if not evs:
                continue
            buf = np.zeros((total + SR * 8, 2))
            for e in evs:
                if e[0] == "mar":
                    _, t, m, v, dark, p = e
                    y = marimba(m, min(v, 1.0), self.rng, dark)
                    pp = p if p is not None else float(np.clip((m - 72) / 28, -0.45, 0.45))
                    y = pan(y, pp)
                elif e[0] == "pz":
                    _, t, m, v, body, p, t60 = e
                    y = pizz(m, min(v, 1.0), body, self.rng, t60=t60)
                    pp = p if p is not None else (-0.3 if body == "cello" else 0.35)
                    y = pan(y, pp)
                elif e[0] == "pad":
                    _, t, notes, dur, v, cutoff, attack, release, vib = e
                    y = sum(pad_note(m, dur, v, attack, release, cutoff, self.rng, vibrato=vib) for m in notes)
                elif e[0] == "boom":
                    _, t, dur, f0, f1, v = e
                    y = pan(boom(dur, f0, f1, v, self.rng), 0.0)
                elif e[0] == "air":
                    _, t, dur, v = e
                    y = air_swell(dur, v, self.rng)
                i0 = max(int(t * SR), 0)
                buf[i0:i0 + len(y)] += y[: len(buf) - i0]
            wet = {"marimba": 0.16, "pizz": 0.22, "pad": 0.30, "low": 0.08}[stem]
            buf = reverb(buf, IR, wet)[: total]
            buf = voice_pocket(buf) if stem != "low" else lp(buf, 400, 2)
            stems[stem] = buf
        L = int(length * SR)
        for k in stems:
            stems[k] = wrap_tail(stems[k], L) if loop else stems[k]
        return stems

    def finish(self, stems, man, purpose, tags, loop, levels=None):
        levels = levels or {}
        for k in stems:
            stems[k] = stems[k] * db(levels.get(k, 0.0))
        mix = sum(stems.values())
        if not loop:
            mix = fade(mix, 0.0, 1.5)
            stems = {k: fade(v, 0.0, 1.5) for k, v in stems.items()}
        g = db(TARGET_LUFS - integrated_lufs(mix))
        pk = np.max(np.abs(mix)) * g
        if pk > db(-1.0):
            g *= db(-1.0) / pk
        d = os.path.join(MUSIC, self.name)
        rel = lambda f: os.path.relpath(os.path.join(d, f), AUDIO)
        kind = "seamless loop" if loop else "one-shot / through-composed"
        write(os.path.join(d, f"{self.name}_FULL.wav"), mix * g)
        man.add(rel(f"{self.name}_FULL.wav"), f"{purpose} Full mix ({kind}).", "synthesized by tools/audio/gen_music.py",
                LICENSE, tags=tags)
        for k, v in stems.items():
            write(os.path.join(d, f"{self.name}_stem_{k}.wav"), v * g)
            man.add(rel(f"{self.name}_stem_{k}.wav"), f"Stem '{k}' of {self.name} (sum of stems = FULL; mute stems to thin out under dense VO).",
                    "synthesized by tools/audio/gen_music.py", LICENSE, tags=tags)
        print(f"{self.name}: {len(mix)/SR:.1f}s  LUFS(before)={integrated_lufs(mix):.1f} gain={20*np.log10(g):.1f}dB")


def air_swell(dur, v, rng):
    from dsp import shaped_noise
    def fr(t, f):
        c = 800 + 4000 * (t / dur) ** 2
        g = np.exp(-0.5 * ((np.log(f + 1) - np.log(c)) / 0.8) ** 2)
        return g * np.clip(t / dur, 0, 1) ** 2
    a = shaped_noise(dur, fr, rng)
    b = shaped_noise(dur, fr, rng)
    return np.stack([a, b], 1) * v


# ===================================================================== cues
def cue_curious(man):
    """Default bed. D major, 96 BPM, 48 bars = 120 s seamless loop."""
    c = Cue("curious_neutral_Dmaj_96bpm", 96, 4, seed=101)
    A = ["Dmaj9", "Bm11", "Gmaj7", "Asus4"]
    B = ["Em9", "Gmaj7", "D/F#", "Asus4"]
    form = (A + A + A + B) * 3                    # 48 bars
    pats = [[0, 2, 1, 3, 2, 4, 3, 1], [0, None, 2, 3, None, 1, 4, 2], [3, 2, 0, 2, 4, 2, 1, 2],
            [0, 3, 2, 4, None, 3, 1, 2]]
    acc = [1.0, 0.55, 0.8, 0.6, 0.9, 0.55, 0.8, 0.62]
    for b, ch in enumerate(form):
        bass, padn, arp = CH[ch]
        pat = pats[(b // 4) % len(pats)]
        for i, idx in enumerate(pat):
            if idx is None or c.rng.random() < 0.06:
                continue
            c.mar(c.at(b, i * 0.5), arp[idx], 0.55 * acc[i])
        if ch == "Asus4" and b % 4 == 3:            # sus -> 3rd resolution
            c.mar(c.at(b, 3.5), n("C#5"), 0.45)
        # pizz: cello root on 1 (+5th on 3 in second half of phrase), violin offbeats
        c.pz(c.at(b, 0), bass + 12, 0.75, "cello")
        if b % 2 == 1:
            c.pz(c.at(b, 2), bass + 19, 0.5, "cello")
        if (b // 8) % 2 == 1:
            c.pz(c.at(b, 1.5), arp[2] + 12 if arp[2] + 12 < n("A6") else arp[2], 0.35, "violin")
            c.pz(c.at(b, 3.5), arp[4], 0.3, "violin")
        c.pad(c.at(b, 0), padn, 4 * c.beat, v=0.32, cutoff=1150, attack=0.9)
    L = 48 * 4 * c.beat
    c.finish(c.render(L, loop=True), man,
             "Default 'curious/neutral' explainer bed: light marimba arpeggios (8ths), cello+violin pizzicato, warm saw pad underneath.",
             "curious/neutral (default) | D major | 96 BPM | 4/4 | loop 120.0 s (48 bars)", True,
             {"pad": -2.0, "pizz": 4.0})


def cue_historic(man):
    """1890s-1920s nostalgia. G major (IV of D), 3/4 waltz-ish, 84 BPM, 48 bars ~102.9 s loop."""
    c = Cue("historic_nostalgic_Gmaj_84bpm_3-4", 84, 3, seed=202)
    A = ["Gadd9", "Em7", "Cmaj7", "D7sus", "G/B", "Cmaj7", "Am7", "D7"]
    form = A * 6
    prev = n("B4")
    for b, ch in enumerate(form):
        bass, padn, arp = CH[ch]
        c.pz(c.at(b, 0), bass + 12, 0.8, "cello")
        top = [m for m in padn if m >= n("G3")][-2:]
        for bt in (1, 2):                                  # "pah-pah": violin double-stop + soft marimba
            for m in top:
                c.pz(c.at(b, bt), m + 12, 0.32, "violin", p=0.3)
        # melody on marimba (soft mallet), phrase shape repeats every 8 bars with variation
        phrase_bar = b % 8
        rh = [[(0, 2), (2, 1)], [(0, 1), (1, 1), (2, 1)], [(0, 3)], [(0, 2), (2, 1)],
              [(0, 1), (1, 2)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (2, 1)], [(0, 3)]][phrase_bar]
        if (b // 8) % 3 == 2 and phrase_bar in (1, 5):
            rh = [(0, 3)]
        for k, (st, du) in enumerate(rh):
            if st == 0:
                cands = [m + o for m in arp for o in (-12, 0) if n("D4") <= m + o <= n("D5")]
                nxt = min(cands, key=lambda m: abs(m - prev) + (0.5 if m == prev else 0))
            else:
                i = int(np.argmin([abs(s - prev) for s in SCALE_G]))
                step = int(c.rng.choice([-2, -1, 1, 1, 2]))
                if prev > n("B4"):
                    step = -abs(step)
                if prev < n("F#4"):
                    step = abs(step)
                nxt = SCALE_G[int(np.clip(i + step, 0, len(SCALE_G) - 1))]
            if du >= 2:
                c.roll(c.at(b, st), nxt, du * c.beat * 0.95, 0.3, 0.42, rate=12.0, dark=0.5)
            else:
                c.mar(c.at(b, st), nxt, 0.55, dark=0.4, p=0.1)
            prev = nxt
        c.pad(c.at(b, 0), padn, 3 * c.beat, v=0.30, cutoff=1500, attack=0.8, vib=1.0)
    L = 48 * 3 * c.beat
    c.finish(c.render(L, loop=True), man,
             "Historic/nostalgic underscore for 1890s Stanford, Hoover, 1920s: gentle 3/4, pizzicato 'oom-pah-pah', marimba melody with tremolo rolls (music-box/parlour feel), soft strings pad.",
             "historic/nostalgic 1890s-1920s | G major (same family as D) | 84 BPM | 3/4 | loop ~102.9 s (48 bars)", True,
             {"pad": -1.0, "marimba": -3.0, "pizz": 2.0})


def cue_tension(man):
    """Brain drain. B minor (relative of D), 92 BPM, 40 bars ~104.3 s loop."""
    c = Cue("tension_braindrain_Bmin_92bpm", 92, 4, seed=303)
    A = ["Bm", "G", "Em", "F#sus", "Bm", "G", "Bm(b6)", "F#"]
    form = A * 5
    ost = [0, 0, 7, 0, 0, 12, 7, 0, 0, 0, 7, 0, 8, 7, 0, 0]          # 16ths, semitones over bass
    vel = [0.9, 0.45, 0.6, 0.5, 0.75, 0.5, 0.6, 0.45, 0.85, 0.45, 0.6, 0.5, 0.7, 0.55, 0.6, 0.5]
    for b, ch in enumerate(form):
        bass, padn, arp = CH[ch]
        root = bass + 12
        for i, s in enumerate(ost):
            if i % 4 != 0 and c.rng.random() < 0.08:
                continue
            c.pz(c.at(b, i * 0.25), root + s, 0.62 * vel[i], "cello", p=-0.25, t60=0.45)
        # marimba: low, dark, dotted two-note figure
        c.mar(c.at(b, 0), arp[0], 0.55, dark=0.6, p=-0.1)
        c.mar(c.at(b, 1.5), arp[2], 0.42, dark=0.6, p=0.1)
        if b % 2 == 1:
            c.mar(c.at(b, 3), arp[1], 0.38, dark=0.6, p=0.05)
        if b % 4 == 3:
            c.pz(c.at(b, 3.5), n("F#5"), 0.3, "violin", p=0.45)
            c.pz(c.at(b, 3.75), n("G5"), 0.25, "violin", p=0.45)
        # dark strings: drone on B/F# + changing upper voice
        c.pad(c.at(b, 0), [n("B1") + 12, padn[-1], padn[-2]], 4 * c.beat, v=0.30, cutoff=850, attack=1.0, vib=0.6)
    L = 40 * 4 * c.beat
    c.finish(c.render(L, loop=True), man,
             "Tension for the 1920s brain drain (talent leaving the West): driving 16th-note cello pizzicato ostinato, dark low marimba figure, low string drone with b6 rub.",
             "tension/brain-drain | B minor (relative of D) | 92 BPM | 4/4 | loop ~104.3 s (40 bars)", True,
             {"pad": -2.0, "marimba": 1.0})


def cue_momentum(man):
    """Terman's plan. D major, 108 BPM, 64 bars ~142 s, through-composed build + ring-out."""
    c = Cue("momentum_building_Dmaj_108bpm", 108, 4, seed=404)
    prog = ["D", "A/C#", "Bm", "G"]
    form = prog * 15 + ["G", "Asus4", "A", "D"]       # 64 bars
    p8 = [0, 2, 4, 2, 1, 3, 4, 3]
    p16 = [0, 2, 4, 2, 5, 2, 4, 2, 1, 3, 4, 3, 5, 3, 4, 3]
    for b, ch in enumerate(form):
        bass, padn, arp = CH[ch]
        sec = b // 8                    # 0..7
        last = b >= 60
        if last:
            if b < 63:
                for i in range(8):
                    c.mar(c.at(b, i * 0.5), arp[[0, 2, 4, 2, 1, 3, 5, 3][i]], 0.55 + 0.05 * (b - 60))
                c.pz(c.at(b, 0), bass + 12, 0.85, "cello")
                c.pz(c.at(b, 2), bass + 12, 0.75, "cello")
                c.pad(c.at(b, 0), padn, 4 * c.beat, v=0.38, cutoff=1500, attack=0.6)
            else:
                for i, m in enumerate([n("D4"), n("F#4"), n("A4"), n("D5"), n("F#5"), n("A5")]):
                    c.mar(c.at(b, 0) + i * 0.035, m, 0.6)
                c.roll(c.at(b, 0.5), n("D5"), 3.0, 0.35, 0.05, rate=14)
                c.pz(c.at(b, 0), n("D2"), 0.95, "cello", t60=1.6)
                c.pz(c.at(b, 0), n("A5"), 0.5, "violin")
                c.pad(c.at(b, 0), CH["D"][1] + [n("A4")], 4.0, v=0.38, cutoff=1500, attack=0.3, release=3.0)
            continue
        if sec < 4:
            for i, idx in enumerate(p8):
                c.mar(c.at(b, i * 0.5), arp[idx], (0.45 + 0.04 * sec) * (1.0 if i % 2 == 0 else 0.7))
        else:
            for i, idx in enumerate(p16):
                c.mar(c.at(b, i * 0.25), arp[idx], (0.42 + 0.03 * (sec - 4)) * (1.0 if i % 4 == 0 else 0.62))
        if sec >= 1:
            c.pz(c.at(b, 0), bass + 12, 0.8, "cello")
            c.pz(c.at(b, 2), bass + 12, 0.65, "cello")
            if sec >= 3:
                c.pz(c.at(b, 1), bass + 19, 0.5, "cello")
                c.pz(c.at(b, 3), bass + 24, 0.5, "cello")
        if sec >= 2:
            c.pad(c.at(b, 0), padn, 4 * c.beat, v=0.22 + 0.03 * min(sec, 6), cutoff=1000 + 120 * sec, attack=0.7)
        if sec >= 3:
            for bt in (0.5, 1.5, 2.5, 3.5):
                c.pz(c.at(b, bt), arp[3] if bt in (0.5, 2.5) else arp[4], 0.3 + 0.03 * sec, "violin")
        if sec >= 6:   # octave doubling on marimba downbeats
            c.mar(c.at(b, 0), arp[0] + 12, 0.45)
    L = 64 * 4 * c.beat + 4.0
    c.finish(c.render(L, loop=False, tail=1.0), man,
             "Momentum/building for Terman's plan: starts as solo marimba, adds cello pizz (bar 9), pad (17), violin pizz (25), 16th-note marimba (33), octave doubling (49), cadence + ring-out on D at bar 64. Sections every 8 bars (~17.8 s) are clean edit points.",
             "momentum/building | D major | 108 BPM | 4/4 | 64 bars ~146 s, builds (not a loop)", False,
             {"pad": -3.0, "pizz": -1.5})


def cue_resolve(man):
    """Warm resolve / garage + oscillator wonder. D major, 80 BPM, 24 bars = 72 s loop, sparse."""
    c = Cue("warm_resolve_Dmaj_80bpm", 80, 4, seed=505)
    form = ["D", "Gmaj7", "Bm11", "Asus4", "D", "Gmaj7", "Em9", "Asus4"] * 3
    for b, ch in enumerate(form):
        bass, padn, arp = CH[ch]
        for i, idx in enumerate([0, 2, 4, 3]):
            c.mar(c.at(b, i), arp[idx], 0.5 if i == 0 else 0.38, dark=0.25)
        if b % 2 == 0:
            c.mar(c.at(b, 2.5), arp[5] if len(arp) > 5 else arp[-1], 0.3, dark=0.25)
        c.pz(c.at(b, 0), bass + 12, 0.7, "cello")
        if b >= 8:
            c.pz(c.at(b, 1.5), arp[1] + 12, 0.28, "violin")
        c.pad(c.at(b, 0), padn, 4 * c.beat, v=0.36, cutoff=1300, attack=1.4, vib=0.8)
    L = 24 * 4 * c.beat
    c.finish(c.render(L, loop=True), man,
             "Warm resolve: slow quarter-note marimba, soft cello pizz, prominent warm strings pad. For the Hewlett & Packard garage / audio oscillator payoff, reflective moments and the outro.",
             "warm/resolve (bonus) | D major | 80 BPM | 4/4 | loop 72.0 s (24 bars)", True,
             {"pad": -1.0})


def cue_stingers(man):
    """Short reveals. All resolve to D (or B minor) so they drop onto any bed."""
    # 1. major reveal: marimba roll on A crescendo -> D major hit + boom + pad bloom
    c = Cue("stinger_reveal_Dmaj", 120, 4, seed=606)
    c.roll(0.0, n("A4"), 1.25, 0.12, 0.7, rate=15, dark=0.2)
    c.roll(0.02, n("E5"), 1.23, 0.08, 0.55, rate=14, dark=0.2)
    c.ev["low"].append(("air", 0.0, 1.3, 0.12))
    hit = 1.3
    for i, m in enumerate([n("D4"), n("A4"), n("D5"), n("F#5"), n("A5"), n("D6")]):
        c.mar(hit + i * 0.018, m, 0.85)
    c.pz(hit, n("D2"), 1.0, "cello", t60=1.8)
    c.pz(hit, n("D3"), 0.8, "cello", t60=1.5)
    c.pz(hit + 0.01, n("F#5"), 0.6, "violin")
    c.pad(hit - 0.15, CH["Dmaj9"][1], 2.5, v=0.45, cutoff=1700, attack=0.25, release=3.0)
    c.ev["low"].append(("boom", hit, 3.0, 64, 38, 0.9))
    c.finish(c.render(7.0, loop=False, tail=0.5), man,
             "Reveal stinger: 1.3 s marimba roll swell into a D-major hit (marimba+pizz+pad+sub boom), rings out ~5 s. Hit lands at 1.30 s — place so 1.30 s is on the reveal frame.",
             "reveal/stinger | D major | hit @1.30 s | 7.5 s", False, {"low": -3.0})

    # 2. soft resolve: rising arpeggio, no boom
    c = Cue("stinger_soft_rise_Dmaj", 120, 4, seed=607)
    for i, m in enumerate([n("D4"), n("F#4"), n("A4"), n("D5"), n("F#5"), n("A5"), n("D6")]):
        c.mar(i * 0.085, m, 0.4 + 0.05 * i)
    c.pz(0.0, n("D3"), 0.7, "cello")
    c.pz(0.6, n("A5"), 0.4, "violin")
    c.pad(0.0, CH["D"][1], 1.5, v=0.32, cutoff=1500, attack=0.15, release=2.5)
    c.finish(c.render(4.5, loop=False, tail=0.5), man,
             "Soft stinger: quick rising D-major marimba arpeggio + pizz + pad bloom. For light 'aha' beats, title cards, label reveals. Peak at ~0.55 s.",
             "reveal/stinger (soft) | D major | 5 s", False)

    # 3. tension hit: B minor, low
    c = Cue("stinger_tension_Bmin", 120, 4, seed=608)
    c.ev["low"].append(("air", 0.0, 0.9, 0.10))
    hit = 0.9
    for m in [n("B2"), n("F#3"), n("B3"), n("D4")]:
        c.mar(hit, m, 0.8, dark=0.6)
    c.pz(hit, n("B1"), 1.0, "cello", t60=1.6)
    c.pz(hit, n("F#2"), 0.7, "cello", t60=1.4)
    c.pad(hit - 0.1, [n("B2"), n("F#3"), n("G3"), n("D4")], 2.0, v=0.4, cutoff=900, attack=0.2, release=2.5)
    c.ev["low"].append(("boom", hit, 3.0, 55, 33, 1.0))
    c.finish(c.render(5.5, loop=False, tail=0.5), man,
             "Tension stinger: air swell into a dark B-minor(b6) low hit with sub boom. For 'opportunities in the West were scarce' type beats. Hit at 0.90 s.",
             "reveal/stinger (tension) | B minor | hit @0.90 s | 6 s", False, {"low": -2.0})


if __name__ == "__main__":
    man = Manifest("music")
    cues = {"curious": cue_curious, "historic": cue_historic, "tension": cue_tension,
            "momentum": cue_momentum, "resolve": cue_resolve, "stingers": cue_stingers}
    sel = sys.argv[1:] or list(cues)
    for k in sel:
        cues[k](man)
    if not sys.argv[1:]:
        man.save()
