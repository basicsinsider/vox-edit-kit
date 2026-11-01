"""Split the raw-take transcript into phrases at pauses; print index, start, end, text."""
import json, sys
w = json.load(open(sys.argv[1])); gap = float(sys.argv[2]) if len(sys.argv) > 2 else 0.3
ph = []; cur = [w[0]]
for a, b in zip(w, w[1:]):
    if b['start'] - a['end'] > gap: ph.append(cur); cur = []
    cur.append(b)
ph.append(cur)
out = []
for i, p in enumerate(ph):
    out.append({'i': i, 'w0': int(p[0]['id'][1:]), 'w1': int(p[-1]['id'][1:]), 'start': p[0]['start'], 'end': p[-1]['end'],
                'text': ' '.join(x['text'] for x in p)})
json.dump(out, open(sys.argv[3], 'w'), indent=0) if len(sys.argv) > 3 else None
for o in out:
    print(f"P{o['i']:03d} {o['start']:7.2f}-{o['end']:7.2f} w{o['w0']}-{o['w1']} | {o['text']}")
