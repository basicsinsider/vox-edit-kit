#!/usr/bin/env python3
"""Assemble the podcast master: the cut A-roll with the rendered compositions dropped in at their master frames.

  python3 tools/assemble_pd.py --aroll renders/pd_aroll_720.mp4 --pieces renders/pieces --h 720 --out renders/pd_720_video.mp4
  python3 tools/assemble_pd.py … --audio renders/pd_mix.m4a          (mux the final mix; video stream-copied)

Every section in project/podcast/sections.json whose piece exists (renders/pieces/<id>.mp4, exactly round(dur*30) frames) replaces
the A-roll frames [round(start*30), round(end*30)). The A-roll between pieces and the pieces themselves are encoded with identical
x264 settings (30 fps, yuv420p) into parts and joined with the concat demuxer (stream copy), so the total frame count equals the
A-roll's. Missing pieces are reported and left as A-roll. Parts are cached in <work>/ (re-run after replacing one piece = only that part)."""
import argparse, json, os, subprocess, sys, hashlib

ap = argparse.ArgumentParser()
ap.add_argument('--aroll', required=True); ap.add_argument('--pieces', default='renders/pieces'); ap.add_argument('--h', type=int, default=720)
ap.add_argument('--out', required=True); ap.add_argument('--work', default='work/assemble'); ap.add_argument('--crf', default='20'); ap.add_argument('--preset', default='veryfast')
ap.add_argument('--audio'); ap.add_argument('--only', help='comma list of ids to use (default: all that exist)')
o = ap.parse_args()
FPS = 30; W = o.h * 16 // 9
S = json.load(open('project/podcast/sections.json')); os.makedirs(o.work, exist_ok=True)
def frames(p):
    return int(subprocess.check_output(['ffprobe', '-v', 'error', '-count_packets', '-select_streams', 'v', '-show_entries', 'stream=nb_read_packets', '-of', 'csv=p=0', p]).split()[0])
TOTAL = frames(o.aroll); print('A-roll frames', TOTAL, '=', TOTAL / FPS, 's; master length', S['length'])
only = set(o.only.split(',')) if o.only else None
plan = []; cur = 0; missing = []
for s in S['sections']:
    f0, f1 = round(s['start'] * FPS), round(s['end'] * FPS); p = f"{o.pieces}/{s['id']}.mp4"
    if not os.path.exists(p) or (only and s['id'] not in only): missing.append(s['id']); continue
    n = frames(p)
    if n != f1 - f0: print(f"!! {s['id']}: piece has {n} frames, slot is {f1 - f0} — fix the piece"); sys.exit(1)
    if f0 > cur: plan.append(('a', cur, f0))
    plan.append(('p', p, s['id'])); cur = f1
if cur < TOTAL: plan.append(('a', cur, TOTAL))
print('pieces used', sum(1 for x in plan if x[0] == 'p'), '| missing (A-roll kept):', ' '.join(missing) or 'none')
enc = ['-c:v', 'libx264', '-preset', o.preset, '-crf', o.crf, '-pix_fmt', 'yuv420p', '-r', str(FPS), '-g', '60', '-video_track_timescale', '15360', '-an']
lst = []
for x in plan:
    if x[0] == 'a':
        _, a, b = x; name = f"{o.work}/a_{a:06d}_{b:06d}_{o.h}.mp4"
        if not (os.path.exists(name) and frames(name) == b - a):
            subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', f'{max(a / FPS - 5, 0):.4f}', '-i', o.aroll, '-vf',
                            f"trim=start_frame={a - round(max(a / FPS - 5, 0) * FPS)}:end_frame={b - round(max(a / FPS - 5, 0) * FPS)},setpts=N/{FPS}/TB,scale={W}:{o.h}:flags=bicubic,setsar=1",
                            *enc, name], check=True)
            assert frames(name) == b - a, (name, frames(name), b - a)
    else:
        _, p, sid = x; st = os.stat(p); key = hashlib.md5(f"{p}{st.st_size}{st.st_mtime}".encode()).hexdigest()[:8]
        name = f"{o.work}/p_{sid}_{o.h}_{key}.mp4"
        if not os.path.exists(name):
            subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', p, '-vf', f"scale={W}:{o.h}:flags=lanczos,setsar=1,setpts=N/{FPS}/TB", *enc, name], check=True)
    lst.append(name); print(' ', os.path.basename(name), flush=True)
open(f"{o.work}/concat_{o.h}.txt", 'w').write(''.join(f"file '{os.path.abspath(n)}'\n" for n in lst))
cmd = ['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', f"{o.work}/concat_{o.h}.txt"]
if o.audio: cmd += ['-i', o.audio, '-map', '0:v', '-map', '1:a', '-c:a', 'copy']
cmd += ['-c:v', 'copy', '-movflags', '+faststart', o.out]
subprocess.run(cmd, check=True)
n = frames(o.out); print('assembled', o.out, n, 'frames', '(OK)' if n == TOTAL else f'!! expected {TOTAL}')
