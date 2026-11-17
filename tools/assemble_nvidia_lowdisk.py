"""Lead-side, disk-light 720p assembly of the NVIDIA edit (when a helper can't run): for each segment in order, fetch its 1080p piece
from render/<seg> (blob by blob), verify SHA-256, re-encode to 720p with the same lead/tail frame-grid correction as assemble_nvidia.py,
delete the 1080p piece and prune git; then concat the 720p parts (stream copy) and mux the final mix (stream copy).
Usage: .venv/bin/python tools/assemble_nvidia_lowdisk.py   → renders/nv/NVIDIA_chip_ban_720p_review.mp4"""
import glob, hashlib, os, re, subprocess as sp
FPS = 24; L = 2402.0; D = 'renders/nv/p720'; os.makedirs(D, exist_ok=True)
A = 'project/nvidia/media_git/nv_final_audio.m4a'; OUT = 'renders/nv/NVIDIA_chip_ban_720p_review.mp4'
starts = {}
for f in sorted(glob.glob('compositions/nvs[0-9][0-9].html')):
    m = re.search(r'data-composition-id="(nvs\d\d)"[^>]*data-vo-start="([\d.]+)"', open(f).read()); starts[m.group(1)] = float(m.group(2))
segs = sorted(starts)
def run(*a, **k): return sp.run(list(a), check=True, **k)
def frames(p): return int(sp.check_output(['ffprobe', '-v', 'error', '-count_packets', '-select_streams', 'v', '-show_entries', 'stream=nb_read_packets', '-of', 'csv=p=0', p]).strip())
pos = 0; parts = []
for i, s in enumerate(segs):
    q = f'{D}/{s}.mp4'; want = round(starts[s] * FPS); nxt = round(starts[segs[i + 1]] * FPS) if i + 1 < len(segs) else round(L * FPS)
    total = nxt - want
    if os.path.exists(q) and frames(q) == total:
        parts.append(os.path.abspath(q)); pos += total; print(s, 'done already'); continue
    b = f'render/{s}'; run('git', 'fetch', '-q', '--depth', '1', 'origin', b)
    names = sorted(n for n in sp.check_output(['git', 'ls-tree', '--name-only', 'FETCH_HEAD', f'pieces/{s}/'], text=True).split() if '.part' in n)
    p = f'{D}/{s}.1080.mp4'
    with open(p, 'wb') as fh:
        for n in names: fh.write(sp.check_output(['git', 'cat-file', 'blob', f'FETCH_HEAD:{n}']))
    wantsha = sp.check_output(['git', 'cat-file', 'blob', f'FETCH_HEAD:pieces/{s}/{s}.mp4.sha256'], text=True).split()[0]
    got = hashlib.sha256(open(p, 'rb').read()).hexdigest(); assert got == wantsha, (s, 'SHA MISMATCH')
    n = frames(p); lead = want - pos; tail = nxt - (want + n)
    vf = []
    if lead < 0: vf += [f'trim=start_frame={-lead}', 'setpts=PTS-STARTPTS']
    if lead > 0: vf.append(f'tpad=start={lead}:start_mode=clone')
    if tail > 0: vf.append(f'tpad=stop={tail}:stop_mode=clone')
    vf += [f'trim=end_frame={total}', 'setpts=PTS-STARTPTS', 'scale=1280:720:flags=lanczos']
    run('nice', 'ffmpeg', '-v', 'error', '-y', '-i', p, '-vf', ','.join(vf), '-c:v', 'libx264', '-preset', 'medium', '-crf', '20',
        '-pix_fmt', 'yuv420p', '-r', '24', '-g', '48', '-an', q)
    os.remove(p); run('git', 'update-ref', '-d', f'refs/remotes/origin/{b}'); sp.run(['git', 'prune', '--expire=now'])
    g = frames(q); assert g == total, (s, g, total)
    print(f'{s}: piece {n} frames, lead {lead:+d}, tail {tail:+d} → {total} frames 720p', flush=True)
    parts.append(os.path.abspath(q)); pos += total
assert pos == round(L * FPS), pos
open(f'{D}/list.txt', 'w').write(''.join(f"file '{x}'\n" for x in parts))
run('ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', f'{D}/list.txt', '-i', A, '-map', '0:v', '-map', '1:a', '-c', 'copy', '-movflags', '+faststart', OUT)
print('OUT', OUT, frames(OUT), 'frames; master', round(L * FPS))
