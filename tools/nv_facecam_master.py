"""Build the NVIDIA face-cam master from Krish's RAW takes at native resolution (3840x2160) — same timing as the 1080p master
(assets/facecam/nvidia_facecam_master.mp4: frame at master t = media time t, 30 fps, 2400.6167 s; black where part 2 is audio-only).
  --window A B  : only master seconds [A, B] get real picture (everything else black) — fast, for one render helper's segment.
  (no window)   : the whole master (for the Premiere package).
Raw parts are downloaded from Krish's Drive into input/nvidia/ if missing (ids in project/nvidia/BRIEF.md). The EDL is
project/nvidia/edl_frames.json (60 fps raw frame ranges on the combined timeline) + project/nvidia/parts.json.
Usage: python3 tools/nv_facecam_master.py OUT.mp4 [--window A B] [--crf 18] [--height 2160]"""
import json, math, os, subprocess as sp, sys
args = sys.argv[1:]; OUT = args[0]
win = None; crf = '18'; H = 2160
if '--window' in args: i = args.index('--window'); win = (float(args[i + 1]), float(args[i + 2]))
if '--crf' in args: crf = args[args.index('--crf') + 1]
if '--height' in args: H = int(args[args.index('--height') + 1])
W = H * 16 // 9
DRIVE = {1: '1Fx5-X_bwA6azoTCEFNML75wxW800r79o', 3: '1SiQrCt7tJDC975jQqI444kYHadyhqTg4'}
F = json.load(open('project/nvidia/edl_frames.json')); P = {p['part']: p for p in json.load(open('project/nvidia/parts.json'))}
LEN = F['length']; FPS = 60
off = {k: round(v['offset'] * FPS) for k, v in P.items()}
def part_of(f0): return 1 if f0 < off[2] else 2 if f0 < off[3] else 3
a, b = win if win else (0.0, LEN)
a = max(0.0, a - 0.5); b = min(LEN, b + 0.5)          # half a second of slack each side
fa, fb = math.floor(a * 30) * 2, math.ceil(b * 30) * 2   # master 60 fps frame window, on the 30 fps grid (even 60 fps frames)
fb = min(fb, round(LEN * FPS))
# raw frame ranges (per part, part-local) that map into the window, in master order
runs = []
for s in F['segments']:
    m0 = round(s['edit_in'] * FPS); n = s['f1'] - s['f0']; m1 = m0 + n
    lo, hi = max(m0, fa), min(m1, fb)
    if lo >= hi: continue
    p = part_of(s['f0'])
    if p == 2: runs.append((2, lo, hi, None, None)); continue
    r0 = s['f0'] - off[p] + (lo - m0); runs.append((p, lo, hi, r0, r0 + (hi - lo)))
os.makedirs('input/nvidia', exist_ok=True)
def raw(p):
    f = f'input/nvidia/part{p}.mp4'
    if not (os.path.exists(f) and os.path.getsize(f) > 1e8):
        sp.run(['curl', '-sSL', '-C', '-', '--retry', '5', '-o', f, f'https://drive.usercontent.google.com/download?id={DRIVE[p]}&export=download&confirm=t'], check=True)
    return f
# build one video stream per contiguous part run, black for part 2, then concat + pad to the full master length
inputs, chains, labels = [], [], []
groups = []
for r in runs:
    if groups and groups[-1][0] == r[0] and groups[-1][-1][2] == r[1]: groups[-1].append(r)
    else: groups.append([r[0], r])
# groups: [part, run, run, ...] contiguous in master time
k = 0; t_cursor = fa
for g in groups:
    p, rs = g[0], g[1:]
    lo, hi = rs[0][1], rs[-1][2]
    if p == 2:
        chains.append(f'color=c=black:s={W}x{H}:r=60:d={(hi - lo) / FPS:.6f},format=yuv420p[g{k}]')
    else:
        first = rs[0][3]; S = max(0, first // FPS - 1)          # input seek to a whole second before the first frame
        inputs += ['-ss', str(S), '-i', raw(p)]
        sel = '+'.join(f'between(n\\,{r[3] - S * FPS}\\,{r[4] - S * FPS - 1})' for r in rs)
        idx = len(inputs) // 4 - 1
        chains.append(f"[{idx}:v]select='{sel}',setpts=N/60/TB,scale={W}:{H}:flags=bicubic,format=yuv420p,setsar=1[g{k}]")
    labels.append(f'[g{k}]'); k += 1
lead = fa / FPS; tail = LEN - fb / FPS
fc = ';'.join(chains) + ';' + ''.join(labels) + f'concat=n={len(labels)}:v=1:a=0[c];' \
     f'[c]tpad=start_duration={lead:.6f}:stop_duration={max(tail, 0):.6f}:color=black,fps=30,trim=duration={LEN:.6f}[v]'
script = OUT + '.filter.txt'; open(script, 'w').write(fc)
cmd = ['nice', 'ffmpeg', '-v', 'error', '-y', *inputs, '-filter_complex_script', script, '-map', '[v]', '-an',
       '-c:v', 'libx264', '-preset', 'ultrafast' if win else 'medium', '-crf', crf, '-g', '60', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', OUT]
print('window', win, 'master frames', fa, fb, 'groups', [(g[0], g[1][1], g[-1][2]) for g in groups]); sys.stdout.flush()
sp.run(cmd, check=True); os.remove(script)
d = float(sp.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', OUT]))
print('OUT', OUT, f'{d:.3f}s (master {LEN:.3f}s)', os.path.getsize(OUT) // 1_000_000, 'MB')
