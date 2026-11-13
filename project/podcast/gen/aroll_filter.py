"""Write the ffmpeg filter script that cuts the 4K source by edl_frames.json (frame-exact select) and applies the punch-ins:
every second EDL piece is scaled 108 % about (50 %, 30 %) so a jump cut reads as a camera change (BRIEF rule 2).
usage: aroll_filter.py <W> <H> <out.txt> [max_master_seconds]"""
import json, sys
W, H, out = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]; lim = float(sys.argv[4]) if len(sys.argv) > 4 else 1e9
F = json.load(open('project/podcast/edl_frames.json')); segs = [s for s in F['segments'] if s['edit_in'] < lim]
sel = '+'.join(f"between(n,{s['f0']},{s['f1']-1})" for s in segs)
z = []; n = 0; plan = []
for i, s in enumerate(segs):
    L = s['f1'] - s['f0']
    if i % 2 == 1: z.append(f"between(n,{n},{n+L-1})")
    plan.append({'i': i, 'master_f0': n, 'master_f1': n + L, 'zoom': 1.08 if i % 2 else 1.0}); n += L
Z = f"(1+0.08*({'+'.join(z)}))" if z else "1"
open(out, 'w').write(f"select='{sel}',setpts=N/30/TB,scale=w='trunc({W}*{Z}/2)*2':h='trunc({H}*{Z}/2)*2':eval=frame:flags=bicubic,crop={W}:{H}:(iw-{W})/2:(ih-{H})*0.3,setsar=1\n")
json.dump(plan, open('project/podcast/punch_plan.json', 'w')); print(len(segs), 'pieces', n, 'frames', n / 30, 's')
