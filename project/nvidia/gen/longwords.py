import json, numpy as np, soundfile as sf
for p in '123':
    d = json.load(open(f'work/asr/nv/p{p}/transcript.json')); w = d['words'] if isinstance(d, dict) else d
    x, sr = sf.read(f'work/asr/nv/p{p}/raw16k.wav'); h = int(0.05 * sr); n = len(x) // h
    db = 20 * np.log10(np.sqrt((x[:n * h].reshape(n, h) ** 2).mean(1)) + 1e-9); noise = np.percentile(db, 10)
    for q in w:
        if q['end'] - q['start'] > 1.6:
            a = q['start'] + 0.7; seg = db[int(a / 0.05):int(q['end'] / 0.05)]
            runs = []; s = None
            for k, v in enumerate(list(seg > noise + 20) + [False]):
                if v and s is None: s = k
                if not v and s is not None:
                    if k - s >= 3: runs.append((round(a + s * 0.05, 2), round(a + k * 0.05, 2)))
                    s = None
            print(p, q['id'], q['text'], q['start'], q['end'], 'voiced runs:', runs)
