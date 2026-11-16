"""Voiced energy inside every ASR gap > 1.5 s (Parakeet can drop whole lines) + long 'words'."""
import json, sys, numpy as np, soundfile as sf
for p in '123':
    d = json.load(open(f'work/asr/nv/p{p}/transcript.json')); w = d['words'] if isinstance(d, dict) else d
    x, sr = sf.read(f'work/asr/nv/p{p}/raw16k.wav'); h = int(0.05 * sr); n = len(x) // h
    db = 20 * np.log10(np.sqrt((x[:n * h].reshape(n, h) ** 2).mean(1)) + 1e-9)
    noise = np.percentile(db, 10); sp = np.percentile(db, 90)
    print(f'part {p}: noise {noise:.0f} speech p90 {sp:.0f} dur {len(x)/sr:.1f} last word end {w[-1]["end"]:.1f}')
    ends = [0.0] + [q['end'] for q in w]; starts = [q['start'] for q in w] + [len(x) / sr]
    for i, (a, b) in enumerate(zip(ends, starts)):
        if b - a > 1.5:
            seg = db[int(a / 0.05) + 2:int(b / 0.05) - 2]; v = (seg > noise + 18).sum() * 0.05
            print(f'  gap {a:7.1f}-{b:7.1f} ({b-a:5.1f}s) before w{i}: voiced {v:.1f}s peak {seg.max() if len(seg) else -99:.0f}')
    for q in w:
        if q['end'] - q['start'] > 1.2: print('  long word', q)
