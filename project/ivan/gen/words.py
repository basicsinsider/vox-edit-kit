import json,sys
w=json.load(open('project/ivan/raw_transcript.json'))
ph={p['i']:p for p in json.load(open('project/ivan/media/phrases.json'))}
for a in sys.argv[1:]:
    p=ph[int(a)]
    print(f"P{a}: "+' '.join(f"{i}:{w[i]['text']}" for i in range(p['w0'],p['w1']+1)))
