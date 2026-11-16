"""Dump a raw part transcript as timed phrases for reading (line break on gap > 0.45 s or sentence end)."""
import json, sys
p = sys.argv[1]
d = json.load(open(f'work/asr/nv/p{p}/transcript.json')); w = d['words'] if isinstance(d, dict) else d
line = []; out = []
for i, x in enumerate(w):
    line.append(x['text'])
    gap = (w[i + 1]['start'] - x['end']) if i + 1 < len(w) else 9
    if gap > 0.45 or x['text'][-1:] in '.?!':
        out.append(f"{w[i - len(line) + 1]['start']:7.1f} w{i - len(line) + 1:<4} {' '.join(line)}" + (f"  [{gap:.1f}]" if 0.8 < gap < 9 else ''))
        line = []
open(f'project/nvidia/media/dump_p{p}.txt', 'w').write('\n'.join(out)); print(p, len(w), len(out))
