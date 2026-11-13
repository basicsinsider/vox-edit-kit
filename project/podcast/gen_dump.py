"""Dump the raw transcript as timed lines (new line at gaps > 0.6 s or sentence ends). usage: gen_dump.py [a b]"""
import json, sys, glob
ws = json.load(open('project/podcast/raw_transcript.json')) if len(sys.argv) < 4 else None
a = float(sys.argv[1]) if len(sys.argv) > 1 else 0; b = float(sys.argv[2]) if len(sys.argv) > 2 else 1e9
line = []; out = []
for i, w in enumerate(ws):
    if w['start'] < a or w['start'] > b: continue
    if line and (w['start'] - ws[i - 1]['end'] > 0.6 or ws[i - 1]['text'][-1:] in '.?!'):
        out.append(f"[{line[0]['id']} {line[0]['start']:.1f}] " + ' '.join(x['text'] for x in line)); line = []
    line.append(w)
if line: out.append(f"[{line[0]['id']} {line[0]['start']:.1f}] " + ' '.join(x['text'] for x in line))
print('\n'.join(out))
