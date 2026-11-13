"""EDL for the podcast raw take (remove-list version of project/ivan/gen/build_edl.py, see MANUAL Ivan/Paraguay notes).
Input: project/podcast/raw_transcript.json, project/podcast/analysis/part*_cuts.json (word-id ranges to REMOVE, written by the
analysts + lead), project/podcast/media/raw_audio.wav (mono decode of the camera audio; only READ).
Keep ranges = everything between the removed ranges. Cut-in / cut-out: the quietest 10 ms in the gap next to the kept words
(as Ivan), then snapped to the 30 fps source frame grid choosing the quieter of the neighbouring frame edges that does not clip a word.
Pass 2: inside kept ranges every silence (< NOISE+8 dB, 50 ms hop) longer than PAUSE_MAX is cut down to PAUSE_KEEP; heads/tails keep
<= 0.3 s. Cuts only — no gain/EQ. Writes project/podcast/EDL.json + edl_frames.json (frame-exact segments + raw->edit map)."""
import json, glob, sys, numpy as np, soundfile as sf
P = 'project/podcast/'; FPS = 30
PAUSE_MAX, PAUSE_KEEP = 0.9, 0.5
w = json.load(open(P + 'raw_transcript.json'))
x, sr = sf.read(P + 'media/raw_audio.wav', dtype='float32'); D = len(x) / sr
hop = int(0.005 * sr); win = int(0.010 * sr)
c = np.cumsum(np.concatenate([[0.0], x.astype(np.float64) ** 2]))
idx = np.arange(0, len(x) - win, hop); rms = np.sqrt((c[idx + win] - c[idx]) / win)
def db(v): return 20 * np.log10(np.maximum(v, 1e-9))
NOISE = float(np.percentile(db(rms), 10))
def quiet(a, b):
    a = max(a, 0.0); i0 = int(a * sr / hop); i1 = max(int(b * sr / hop), i0 + 1); i1 = min(i1, len(rms))
    k = i0 + int(np.argmin(rms[i0:i1])); return k * hop / sr + 0.005, float(db(rms[k]))
def near_quiet(a, b, toward_end, thr_db=10.0, run=0.03):
    """the quiet point (RMS < noise+thr for >= run s) CLOSEST to the kept word inside [a,b]: scanning from b back to a when
    toward_end (cut-in: hug the word start), from a forward otherwise (cut-out: hug the word end). None if no such run.
    Trims leftover fragments ('sh', 'uh', half words) that the global-minimum rule left between the cut and the word (vo_diff)."""
    a = max(a, 0.0); i0 = int(a * sr / hop); i1 = min(max(int(b * sr / hop), i0 + 1), len(rms)); n = max(int(run * sr / hop), 1)
    q = db(rms[i0:i1]) < NOISE + thr_db
    rng = range(len(q) - n, -1, -1) if toward_end else range(0, len(q) - n + 1)
    for k in rng:
        if q[k:k + n].all():
            j = i0 + k + n // 2; return j * hop / sr + 0.005, float(db(rms[j]))
    return None
def snap(t, lo, hi):
    """nearest frame edges to t inside [lo,hi]; pick the quieter"""
    cands = [f / FPS for f in (int(np.floor(t * FPS)), int(np.ceil(t * FPS))) if lo - 1e-6 <= f / FPS <= hi + 1e-6]
    if not cands: cands = [round(t * FPS) / FPS]
    best = min(cands, key=lambda q: rms[min(int(q * sr / hop), len(rms) - 1)])
    return best, float(db(rms[min(int(best * sr / hop), len(rms) - 1)]))
cuts = []
for f in sorted(glob.glob(P + 'analysis/part*_cuts.json')):
    for q in json.load(open(f)): cuts.append((int(q['a']), int(q['b']), q.get('kind', ''), q.get('why', ''), f.split('/')[-1]))
cuts.sort(); rm = np.zeros(len(w), bool)
for a, b, *_ in cuts:
    assert 0 <= a <= b < len(w), (a, b); rm[a:b + 1] = True
END_ID = json.load(open(P + 'analysis/end.json'))['last_word_id'] if glob.glob(P + 'analysis/end.json') else len(w) - 1
rm[END_ID + 1:] = True
keep = []; i = 0
while i < len(w):
    if rm[i]: i += 1; continue
    j = i
    while j + 1 < len(w) and not rm[j + 1]: j += 1
    keep.append((i, j)); i = j + 1
segs = []
for ki, (a, b) in enumerate(keep):
    prev_keep_end = w[keep[ki - 1][1]]['end'] if ki > 0 else 0.0
    next_keep_start = w[keep[ki + 1][0]]['start'] if ki + 1 < len(keep) else D
    ws, we = w[a]['start'], w[b]['end']
    pe = w[a - 1]['end'] if a > 0 else 0.0
    ns = w[b + 1]['start'] if b + 1 < len(w) else D
    if a == 0: tin, din = 0.0, -100.0
    else:
        # abutting speech (no gap before the kept word): ASR boundaries are loose -> search back into the REMOVED words (up to half of them, 0.25 s)
        lo = max(pe, ws - 0.30) if ws - pe > 0.02 else ws - 0.08
        tin, din = quiet(lo, ws - 0.01 if ws - pe > 0.02 else ws + 0.08)
        nq = near_quiet(max(pe, ws - 0.22), ws - 0.02, True) if ws - pe > 0.06 else None
        if nq: tin, din = nq
        tin, din = snap(tin, lo, ws + 0.03)
    hi = min(ns, we + 0.40) if ns - we > 0.02 else we + 0.08
    tout, dout = quiet(we + 0.01 if ns - we > 0.02 else we - 0.08, hi)
    nq = near_quiet(we + 0.02, min(ns, we + 0.25), False) if ns - we > 0.06 else None
    if nq: tout, dout = nq
    tout, dout = snap(tout, we - 0.03, hi)
    if tout - tin < 2 / FPS: continue
    segs.append({'w': [a, b], 'in': round(tin, 4), 'out': round(tout, 4), 'in_db': round(din, 1), 'out_db': round(dout, 1)})
print('noise', round(NOISE, 1), 'cuts', len(cuts), 'keep ranges', len(segs), 'length after word cuts', round(sum(s['out'] - s['in'] for s in segs), 1))
loud = [s for s in segs if max(s['in_db'], s['out_db']) > NOISE + 22]
print('cut points louder than noise+22 dB:', len(loud))
# pass 2: dead air
h = int(0.05 * sr); TH = NOISE + 8
def sil_runs(a, b):
    i0, i1 = int(a * sr), int(b * sr); v = x[i0:i1]; n = len(v) // h
    if n == 0: return []
    d = db(np.sqrt((v[:n * h].reshape(n, h).astype(np.float64) ** 2).mean(1))) < TH
    runs = []; s = None
    for k, q in enumerate(list(d) + [False]):
        if q and s is None: s = k
        if not q and s is not None: runs.append((a + s * 0.05, a + k * 0.05)); s = None
    return runs
fr = lambda t: round(t * FPS) / FPS
out = []; trimmed = 0.0
for s in segs:
    a, b = s['in'], s['out']; pieces = []; cur = a
    for r0, r1 in sil_runs(a, b):
        if r0 <= a + 0.01 and r1 - a > 0.3 and a > 0: cur = fr(r1 - 0.3); continue
        if r1 >= b - 0.06 and b - r0 > 0.3: b = fr(r0 + 0.3); break
        if r1 - r0 > PAUSE_MAX:
            p_out, p_in = fr(r0 + PAUSE_KEEP / 2), fr(r1 - PAUSE_KEEP / 2)
            if p_in - p_out >= 3 / FPS: pieces.append((cur, p_out)); cur = p_in
    pieces.append((cur, b))
    for k, (p0, p1) in enumerate(pieces):
        if p1 - p0 < 2 / FPS: continue
        q = dict(s); q['in'], q['out'] = round(p0, 4), round(p1, 4)
        if k > 0: q['in_db'] = -100.0; q['sil'] = True
        if k < len(pieces) - 1: q['out_db'] = -100.0
        out.append(q)
# merge pieces that abut (no real cut)
m = [out[0]]
for q in out[1:]:
    if abs(q['in'] - m[-1]['out']) < 1e-6: m[-1]['out'] = q['out']; m[-1]['out_db'] = q['out_db']; m[-1]['w'] = [m[-1]['w'][0], q['w'][1]]
    else: m.append(q)
t = 0.0; frames = []
for q in m:
    f0, f1 = round(q['in'] * FPS), round(q['out'] * FPS)
    frames.append({'f0': f0, 'f1': f1, 'raw_in': f0 / FPS, 'raw_out': f1 / FPS, 'edit_in': round(t, 4), 'w': q['w'], 'in_db': q['in_db'], 'out_db': q['out_db'], 'sil': q.get('sil', False)})
    t += (f1 - f0) / FPS
json.dump({'source': 'input/aroll.mp4', 'fps': FPS, 'noise_floor_db': round(NOISE, 1), 'pause_max': PAUSE_MAX, 'pause_keep': PAUSE_KEEP, 'segments': m,
           'removed': [{'a': a, 'b': b, 'kind': k, 'why': y, 'src': f} for a, b, k, y, f in cuts]}, open(P + 'EDL.json', 'w'), indent=0)
json.dump({'fps': FPS, 'segments': frames, 'length': round(t, 4)}, open(P + 'edl_frames.json', 'w'), indent=0)
print('pass2: segments', len(m), 'edited length', round(t, 2), 's =', f'{int(t//60)}:{t%60:05.2f}', '| raw', round(D, 1))
