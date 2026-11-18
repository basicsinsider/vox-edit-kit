"""NVIDIA review fix: choose pause cuts (VO pauses >= MIN s trimmed to ~0.35-0.5 s) on the 24 fps grid, picking the
position that minimises the visual jump (720p review render). Writes project/nvidia/fix_cuts.json:
  cuts: [{a_a, b_a (audio cut, s), a_v, b_v (video cut, s, frame grid), L}], same L for audio and video.
Usage: .venv/bin/python tools/nv_fix_cuts.py work/review/review720.mp4"""
import json, subprocess as sp, sys, numpy as np
SRC = sys.argv[1]; FPS = 24; MIN = 0.9; PRE, POST = 0.12, 0.15; RMIN, RMAX = 0.30, 0.50
P = [tuple(p) for p in json.load(open('work/fix1/pauses.json')) if p[1] - p[0] >= MIN]
# checked by re-transcribing ±2–4 s with and without each cut (parakeet): these "pauses" hold quiet speech → never cut
EXCLUDE = {497.98: 'the weakest and this is (whispered)', 667.32: '…market-place tail + whip', 768.58: 'because',
           805.36: 'to China', 963.28: 'system is'}
P = [p for p in P if round(p[0], 2) not in EXCLUDE]
MANUAL = {  # look-aways flagged in review: video cut ends on the next shot, graphic covers the A/V offset
  845.72: dict(a_v=845.75, b_v=846.875, b_a=847.04),   # face cam → card wipe settles at 846.875
  2306.38: dict(a_v=None, b_v=2307.625, a_a=2306.55)}
def frames(t0, t1):
    w, h = 64, 36
    out = sp.run(['ffmpeg', '-v', 'error', '-ss', f'{t0:.3f}', '-i', SRC, '-t', f'{t1 - t0:.3f}', '-vf', f'scale={w}:{h},format=gray',
                  '-f', 'rawvideo', '-'], capture_output=True, check=True).stdout
    return np.frombuffer(out, np.uint8).reshape(-1, h, w).astype(np.float32)
def d(x, y): return float(np.abs(x - y).mean())
cuts = []
for p0, p1 in P:
    f0 = int(np.floor(p0 * FPS)) - 1; f1 = int(np.ceil(p1 * FPS)) + 1
    F = frames(f0 / FPS, (f1 + 1) / FPS); idx = lambda fr: fr - f0
    jumps = [d(F[i], F[i + 1]) for i in range(len(F) - 1)]
    key = round(p0, 2)
    if key in MANUAL:
        m = MANUAL[key]
        if m.get('a_v') is not None:   # picture cut fixed at both ends; audio cut of the same length ends at b_a
            av = round(m['a_v'] * FPS); bv = round(m['b_v'] * FPS)
            L = bv - av; ba = m['b_a']; aa = ba - L / FPS
        else:
            bv = round(m['b_v'] * FPS); aa = m['a_a']
            L = round((p1 - POST - 0.05 - aa) * FPS); av = bv - L; ba = aa + L / FPS
        cuts.append(dict(p0=p0, p1=p1, a_v=av / FPS, b_v=bv / FPS, a_a=round(aa, 6), b_a=round(ba, 6), L=L / FPS, cost=None, manual=True)); continue
    best = None
    for a in range(int(np.ceil((p0 + PRE) * FPS)), int((p1 - POST) * FPS) + 1):
        for b in range(a + 1, int((p1 - POST) * FPS) + 1):
            R = (p1 - p0) - (b - a) / FPS
            if not (RMIN <= R <= RMAX): continue
            # jump between last kept frame (a-1) and first kept frame (b); an existing cut inside counts as a cut
            seg = jumps[idx(a - 1):idx(b)]; big = [i for i, j in enumerate(seg) if j > 12]
            if big:
                c = idx(a - 1) + big[0]; cost = d(F[idx(a - 1)], F[c]) + d(F[c + 1], F[idx(b)])
            else: cost = d(F[idx(a - 1)], F[idx(b)])
            cost += 0.5 * abs(R - 0.38) * 10
            if best is None or cost < best[0]: best = (cost, a, b)
    c, a, b = best
    cuts.append(dict(p0=p0, p1=p1, a_v=a / FPS, b_v=b / FPS, a_a=a / FPS, b_a=b / FPS, L=(b - a) / FPS, cost=round(c, 2), manual=False))
tot = sum(c['L'] for c in cuts)
json.dump(dict(fps=FPS, min_pause=MIN, total_cut=tot, cuts=cuts), open('project/nvidia/fix_cuts.json', 'w'), indent=1)
for c in cuts: print(f"{c['p0']:8.2f}-{c['p1']:8.2f}  video {c['a_v']:.3f}-{c['b_v']:.3f}  audio {c['a_a']:.3f}-{c['b_a']:.3f}  L {c['L']:.3f}  cost {c['cost']}")
print(len(cuts), 'cuts, total', round(tot, 3), 's')
