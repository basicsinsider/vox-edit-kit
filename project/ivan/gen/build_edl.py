"""Build the EDL (cut points in silences) + filler scan for the Ivan raw take.
Cut-in: quietest 10 ms window in [word_start-0.30, word_start-0.01] (bounded by prev word end); cut-out: quietest in
[word_end+0.01, word_end+0.40] (bounded by next word start). Abutting words: search +-0.08 s around the boundary.
Writes project/ivan/EDL.json. No gain/EQ is ever applied; audio is only cut (5 ms crossfades at the joins)."""
import json, sys, numpy as np, soundfile as sf
sys.path.insert(0, 'project/ivan/gen'); from edl_keep import KEEP, OVERRIDES
w = json.load(open('project/ivan/raw_transcript.json'))
x, sr = sf.read('project/ivan/media/raw_audio.wav'); m = x.mean(1) if x.ndim > 1 else x
hop = int(0.005 * sr); win = int(0.010 * sr)
rms = np.sqrt(np.convolve(m ** 2, np.ones(win) / win, 'same'))[::hop]
def db(v): return 20 * np.log10(v + 1e-9)
def quiet(a, b):
    a = max(a, 0); i0, i1 = int(a * sr / hop), max(int(b * sr / hop), int(a * sr / hop) + 1)
    k = i0 + int(np.argmin(rms[i0:i1])); return k * hop / sr, db(rms[k])
segs = []
for a, b, note in KEEP:
    ws, we = w[a]['start'], w[b]['end']
    pe = w[a - 1]['end'] if a > 0 else 0.0
    ns = w[b + 1]['start'] if b + 1 < len(w) else len(m) / sr
    lo = max(pe, ws - 0.30) if ws - pe > 0.02 else ws - 0.08
    tin, din = quiet(lo, ws - 0.01 if ws - pe > 0.02 else ws + 0.08)
    hi = min(ns, we + 0.40) if ns - we > 0.02 else we + 0.08
    tout, dout = quiet(we + 0.01 if ns - we > 0.02 else we - 0.08, hi)
    o = OVERRIDES.get((a, b), {}); tin = o.get('in', tin); tout = o.get('out', tout)
    segs.append({'w': [a, b], 'in': round(tin, 3), 'out': round(tout, 3), 'in_db': round(din, 1), 'out_db': round(dout, 1), 'note': note})
# filler scan: gaps inside kept ranges > 0.30 s whose middle is voiced
noise = np.percentile(db(rms), 10)
fill = []
for s in segs:
    a, b = s['w']
    for i in range(a, b):
        g0, g1 = w[i]['end'], w[i + 1]['start']
        if g1 - g0 > 0.30:
            i0, i1 = int((g0 + 0.06) * sr / hop), int((g1 - 0.06) * sr / hop)
            pk = db(rms[i0:i1].max()) if i1 > i0 else -120
            if pk > noise + 25: fill.append({'after_w': i, 'gap': [g0, g1], 'peak_db': round(pk, 1), 'ctx': w[i]['text'] + ' _ ' + w[i + 1]['text']})
json.dump({'source': 'input/raw_facecam.mp4', 'noise_floor_db': round(noise, 1), 'segments': segs, 'filler_candidates': fill}, open('project/ivan/EDL.json', 'w'), indent=1)
print('noise', round(noise, 1), 'segments', len(segs), 'edited length', round(sum(s['out'] - s['in'] for s in segs), 1))
for s in segs:
    if max(s['in_db'], s['out_db']) > noise + 20: print('LOUD CUT', s['w'], s['in_db'], s['out_db'], s['note'][:50])
for f in fill: print('FILLER?', f)
