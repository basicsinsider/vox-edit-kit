"""Compare the words we meant to keep (EDL ranges of the raw transcript) with a fresh ASR of the edited VO."""
import json, sys, difflib
sys.path.insert(0, 'project/cartels/gen'); from edl_keep import resolve, norm
w = json.load(open('project/cartels/raw_transcript.json'))
want = [norm(w[i]['text']) for a, b, _ in resolve() for i in range(a, b + 1)]
v = json.load(open(sys.argv[1])); v = v['words'] if isinstance(v, dict) else v
got = [norm(x['text']) for x in v]
sm = difflib.SequenceMatcher(None, want, got, autojunk=False)
for op, a0, a1, b0, b1 in sm.get_opcodes():
    if op != 'equal':
        t = v[min(b0, len(v) - 1)]['start']
        print(f"{t:8.2f} {op:7s} want: {' '.join(want[max(a0-3,0):a1+2])!r:70.70} got: {' '.join(got[max(b0-3,0):b1+2])!r}")
print('ratio', round(sm.ratio(), 4), len(want), len(got))
