"""Paraguay assembly: concat the 13 segment pieces so EVERY piece starts on its nearest 24 fps master frame.
Segment boundaries (e.g. 213.60 s = frame 5126.4) are not on the master grid and each piece is rendered from its own 0, so a plain
concat drifts up to ~1.4 frames. For each piece we compare where it would land with round(SEG_START*24) and duplicate (tpad clone)
or drop its first frame(s); untouched pieces are stream-copied. Output: renders/py/py_picture.mp4 (exactly round(1621.867*24) frames).
Usage: .venv/bin/python tools/assemble_paraguay.py [pieces_dir] [out]"""
import json, re, subprocess, sys, os, glob
P = sys.argv[1] if len(sys.argv) > 1 else 'renders/py/pieces'
OUT = sys.argv[2] if len(sys.argv) > 2 else 'renders/py/py_picture.mp4'
L = 1621.867; FPS = 24
starts = {}
for f in sorted(glob.glob('compositions/pys[0-9][0-9].html')):
    s = open(f).read(); m = re.search(r'data-composition-id="(pys\d\d)"[^>]*data-vo-start="([\d.]+)"', s)
    starts[m.group(1)] = float(m.group(2))
segs = sorted(starts)
def frames(p): return int(subprocess.check_output(['ffprobe', '-v', 'error', '-count_packets', '-select_streams', 'v', '-show_entries', 'stream=nb_read_packets', '-of', 'csv=p=0', p]).strip())
pos = 0; parts = []
for i, s in enumerate(segs):
    p = f'{P}/{s}.mp4'; n = frames(p)
    want = round(starts[s] * FPS); nxt = round(starts[segs[i + 1]] * FPS) if i + 1 < len(segs) else round(L * FPS)
    lead = want - pos            # >0: duplicate first frame(s); <0: drop that many first frames
    tail = nxt - (want + n)     # frames to add/drop at the end so the next piece starts on time
    print(f'{s}: start {starts[s]:.3f} want frame {want}, at {pos}, piece {n} frames, lead {lead:+d}, tail {tail:+d}')
    vf = []
    if lead < 0: vf.append(f'trim=start_frame={-lead}'); vf.append('setpts=PTS-STARTPTS')
    if lead > 0: vf.append(f'tpad=start={lead}:start_mode=clone')
    if tail > 0: vf.append(f'tpad=stop={tail}:stop_mode=clone')
    total = n + lead + tail
    if vf or tail < 0:
        q = f'{P}/{s}.fixed.mp4'
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', p, '-vf', ','.join(vf + [f'trim=end_frame={total}', 'setpts=PTS-STARTPTS']),
                        '-c:v', 'libx264', '-preset', 'medium', '-crf', '18', '-pix_fmt', 'yuv420p', '-r', '24', '-an', q], check=True)
        p = q
    got = frames(p); assert got == total, (s, got, total)
    parts.append(os.path.abspath(p)); pos += total
open(f'{P}/list.txt', 'w').write(''.join(f"file '{x}'\n" for x in parts))
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', f'{P}/list.txt', '-c', 'copy', '-movflags', '+faststart', OUT], check=True)
print('picture', OUT, frames(OUT), 'frames; master', round(L * FPS))
