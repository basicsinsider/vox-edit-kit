"""NVIDIA review fix — one segment's final 4K piece (run by an assembly helper).
Fetches the segment's 4K render from git (render4k/<SEG>-v2 if it exists, else render4k/<SEG>), checks its sha256, drops the
frames inside project/nvidia/fix_cuts.json's VIDEO cuts (and the 1 spare frame some renders carry), and encodes an MPEG-TS
piece whose timestamps start at the segment's position on the NEW (cut) timeline, so the lead can join all pieces byte by byte.
  x264 medium CRF 19 capped at 30 Mbps (VBV 60M), yuv420p, GOP 48, 3840x2160 24 fps, no audio.
Output: pieces/fix/<SEG>.ts.partNNN (95 MB) + pieces/fix/<SEG>.sha256 (sha256 + md5 + frames line).
Usage: python3 tools/nv_fix_piece.py <SEG>"""
import json, os, subprocess as sp, sys, hashlib, glob
SEG = sys.argv[1]; FPS = 24
SEGS = json.load(open('project/nvidia/segments.json'))['segments']
C = json.load(open('project/nvidia/fix_cuts.json'))['cuts']
cuts = sorted((round(c['a_v'] * FPS), round(c['b_v'] * FPS)) for c in C)
s0 = sum(s['frames'] for s in SEGS[:[s['seg'] for s in SEGS].index(SEG)]); fr = [s for s in SEGS if s['seg'] == SEG][0]['frames']; s1 = s0 + fr
drop = [(max(a, s0) - s0, min(b, s1) - s0) for a, b in cuts if a < s1 and b > s0]           # segment-local [a, b)
removed_before = sum(min(b, s0) - a for a, b in cuts if a < s0)
new_start = s0 - removed_before; keep = fr - sum(b - a for a, b in drop)
url = sp.run(['git', 'remote', 'get-url', 'origin'], capture_output=True, text=True, check=True).stdout.strip()
G = f'/tmp/_src_{SEG}.git'; sp.run(['rm', '-rf', G], check=True)
sp.run(['git', 'init', '-q', '--bare', G], check=True); sp.run(['git', '-C', G, 'remote', 'add', 'origin', url], check=True)
br = None
for b in (f'render4k/{SEG}-v2', f'render4k/{SEG}'):
    if sp.run(['git', '-C', G, 'fetch', '-q', '--depth', '1', '--filter=blob:none', 'origin', b]).returncode == 0:
        ls = sp.run(['git', '-C', G, 'ls-tree', '-r', 'FETCH_HEAD', f'pieces/{SEG}/'], capture_output=True, text=True).stdout
        if '.part' in ls: br = b; break
assert br, 'no 4K render branch found'
os.makedirs('/tmp/fixsrc', exist_ok=True); src = f'/tmp/fixsrc/{SEG}.mp4'
with open(src, 'wb') as o:
    for l in ls.splitlines():
        m, t, oid, path = l.split(None, 3)
        if '.part' in path: o.write(sp.run(['git', '-C', G, 'cat-file', 'blob', oid], capture_output=True, check=True).stdout)
        elif path.endswith('.sha256'): want = sp.run(['git', '-C', G, 'cat-file', 'blob', oid], capture_output=True, text=True, check=True).stdout.split()[0]
h = hashlib.sha256(open(src, 'rb').read()).hexdigest(); assert h == want, ('sha256 mismatch', h, want)
print(f'{SEG}: source {br} sha256 OK; master frames {s0}-{s1}; drop {drop}; keep {keep}; new start frame {new_start}', flush=True)
sel = f'lt(n\\,{fr})' + ''.join(f'*not(between(n\\,{a}\\,{b - 1}))' for a, b in drop)
os.makedirs('pieces/fix', exist_ok=True); out = f'/tmp/fixsrc/{SEG}.ts'
sp.run(['nice', 'ffmpeg', '-v', 'error', '-y', '-i', src, '-vf', f"select='{sel}',setpts=N/{FPS}/TB", '-r', str(FPS),
        '-c:v', 'libx264', '-preset', 'medium', '-crf', '19', '-maxrate', '30M', '-bufsize', '60M', '-pix_fmt', 'yuv420p', '-g', '48', '-an',
        '-muxdelay', '0', '-muxpreload', '0', '-output_ts_offset', f'{new_start / FPS:.6f}', '-f', 'mpegts', out], check=True)
os.remove(src); sp.run(['rm', '-rf', G])
n = int(sp.run(['ffprobe', '-v', 'error', '-count_packets', '-select_streams', 'v', '-show_entries', 'stream=nb_read_packets,width,height',
                '-of', 'csv=p=0', out], capture_output=True, text=True, check=True).stdout.strip().split(',')[-1])
assert n == keep, ('frame count', n, keep)
d = open(out, 'rb').read(); sha, md5 = hashlib.sha256(d).hexdigest(), hashlib.md5(d).hexdigest(); del d
for p in glob.glob(f'pieces/fix/{SEG}.ts.part*'): os.remove(p)
sp.run(['split', '-b', '95m', '-d', '-a', '3', out, f'pieces/fix/{SEG}.ts.part'], check=True); os.remove(out)
open(f'pieces/fix/{SEG}.sha256', 'w').write(f'{sha}  {SEG}.ts\n{md5}  {SEG}.ts\nframes {n} start_frame {new_start} source {br}\n')
print(f'{SEG}: OK frames {n} start {new_start} sha256 {sha} md5 {md5}')
