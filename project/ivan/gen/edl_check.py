import json, sys
sys.path.insert(0, 'project/ivan/gen'); from edl_keep import KEEP
w = json.load(open('project/ivan/raw_transcript.json'))
prev = None; tot = 0
for a, b, n in KEEP:
    assert prev is None or a > prev, (a, prev)
    gin = w[a]['start'] - (w[a-1]['end'] if a > 0 else 0)
    gout = (w[b+1]['start'] if b+1 < len(w) else 9e9) - w[b]['end']
    flag = ' <<' if min(gin, gout) < 0.1 else ''
    print(f"{a:5d}-{b:5d} in-gap {gin:5.2f} out-gap {gout:5.2f}{flag} | {w[a]['text']} … {w[b]['text']}")
    tot += w[b]['end'] - w[a]['start']; prev = b
print('speech total', round(tot, 1))
