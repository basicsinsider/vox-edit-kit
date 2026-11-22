"""US vs Cartels fix round 1 — picture-side assembly on master v2: the 14 segment pieces rendered on v1 (+ optional cts00
pre-roll) + project/cartels/fix1_ops.json → a frame-exact v2 picture (no audio).
  v1 layout = tools/assemble_cartels.py: piece ctsNN starts on master frame round(start*24) (segments.json); a piece longer than
  its slot is trimmed at the end, a shorter one holds its last frame. Global v1 frame g → piece-local frame g - G0.
  v2 = [cts00: round(P*24) frames, padded/trimmed] + v1 frames with every `del` [t, t+del) removed and, for every `ins` at t,
  the frame before t held ins*24 times (freeze while the restored words play).
  Each piece becomes an MPEG-TS part with -output_ts_offset = its v2 start: decoded → frames dropped/held in Python → x264 CRF 18 preset medium, NO B-frames
  (-bf 0), keyint 48. EVERY part is re-encoded (untouched ones too): a stream-copied MP4 → TS keeps
  the B-frame delay (pts +2 frames, the MP4 edit list is dropped) and a negative -output_ts_offset can't pull it back (tested on cts00:
  2 frames lost at the join). Every part must start exactly at its v2 offset (checked). The parts are byte-joined (concat: protocol) and remuxed to MP4 (+faststart).
  Checks: total frames == round(v2_len*24) and every packet pts on a strict 1/24 s step (no B-frame pts traps).
Intermediates go to /dev/shm (deleted at the end). Disk: the output ≈ the pieces' total size.
Usage: .venv/bin/python tools/ct_fix_assemble.py [--pieces renders/ct/pieces] [--ops project/cartels/fix1_ops.json]
                                                 [--out renders/ct/ct_v2_picture.mp4] [--cts00 <pieces>/cts00.mp4] [--keep-parts]
       --no-preroll: ignore fix1_ops.json "preroll" (test before cts00 is rendered)"""
import json, os, sys, glob, shutil, subprocess as sp, numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ct_fix_remap import load_ops
FPS = 24; W, H = 1280, 720
def arg(k, d):
    return sys.argv[sys.argv.index(k) + 1] if k in sys.argv else d
PIECES = arg('--pieces', 'renders/ct/pieces'); OPS = arg('--ops', 'project/cartels/fix1_ops.json')
OUT = arg('--out', 'renders/ct/ct_v2_picture.mp4'); TMP = arg('--tmp', '/dev/shm/ct_fix_assemble')
SEG = json.load(open('project/cartels/segments.json'))
V1_FRAMES = 32206   # the delivered v1 720p (segments.json length 1341.912 → assemble_cartels pads to 32206 frames)

def nframes(p):
    return int(sp.check_output(['ffprobe', '-v', 'error', '-count_packets', '-select_streams', 'v:0', '-show_entries',
                                'stream=nb_read_packets', '-of', 'csv=p=0', p]).split()[0])
def min_pts(p):
    return min(float(l.strip(',')) for l in sp.check_output(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'packet=pts_time',
                                                             '-of', 'csv=p=0', p]).decode().split() if l.strip(','))
def probe_wh(p):
    s = sp.check_output(['ffprobe', '-v', 'error', '-select_streams', 'v', '-show_entries', 'stream=width,height', '-of', 'csv=p=0', p]).decode()
    return tuple(map(int, s.strip().split(',')[:2]))

def v2_sources(ops, P_frames):
    """list of v2 frames → (piece_id, local frame) ; v1 global frames first, pre-roll handled separately"""
    keep = np.ones(V1_FRAMES, np.int32)            # how many times each v1 frame appears in v2
    for o in ops:
        f = round(o['t'] * FPS)
        if 'del' in o: keep[f:f + round(o['del'] * FPS)] = 0
        else: keep[max(f - 1, 0)] += round(o['ins'] * FPS)
    return keep

def main():
    J, ops = load_ops(OPS); P = 0.0 if '--no-preroll' in sys.argv else float(J.get('preroll', 0)); PF = round(P * FPS)
    segs = SEG['segments']; G0 = [round(s['start'] * FPS) for s in segs] + [V1_FRAMES]
    keep = v2_sources(ops, PF); total = PF + int(keep.sum())
    os.makedirs(TMP, exist_ok=True); parts = []; pos = 0
    plan = []
    if PF:
        c0 = arg('--cts00', f'{PIECES}/cts00.mp4'); assert os.path.exists(c0), f'preroll {P} s but no {c0}'
        n = nframes(c0); cnt = np.ones(n, np.int32)
        if n > PF: cnt[PF:] = 0
        elif n < PF: cnt[-1] += PF - n
        plan.append(('cts00', c0, cnt))
    elif os.path.exists(f'{PIECES}/cts00.mp4'): print('note: cts00.mp4 present but preroll = 0 → not used')
    for i, s in enumerate(segs):
        p = f"{PIECES}/{s['id']}.mp4"; n = nframes(p); slot = G0[i + 1] - G0[i]
        cnt = np.zeros(n, np.int32); k = keep[G0[i]:G0[i + 1]]
        m = min(n, slot); cnt[:m] = k[:m]
        if slot > n: cnt[n - 1] += int(k[n:].sum())  # piece shorter than its slot: its last frame holds (as assemble_cartels)
        plan.append((s['id'], p, cnt))
    for sid, p, cnt in plan:
        ts = f'{TMP}/{sid}.ts'; off = pos / FPS; nout = int(cnt.sum())
        # every part is re-encoded: a stream-copied MP4 → TS keeps the B-frame delay (pts +2 frames, MP4 edit list dropped) and a
        # negative -output_ts_offset cannot pull it back (tested on cts00: 2 frames lost at the join) → no stream copy
        untouched = False
        if untouched:   # stream copy; B-frame trap: the TS copy ignores the MP4 edit list (pts start +2 frames) → measure, re-offset
            shift = 0.0
            for _ in range(2):
                sp.run(['ffmpeg', '-v', 'error', '-y', '-i', p, '-map', '0:v:0', '-c', 'copy', '-bsf:v', 'h264_mp4toannexb',
                        '-output_ts_offset', f'{off - shift:.6f}', '-muxdelay', '0', '-muxpreload', '0', '-f', 'mpegts', ts], check=True)
                p0 = min_pts(ts)
                if abs(p0 - off) < 1e-3: break
                shift += p0 - off
            assert abs(min_pts(ts) - off) < 1e-3, (sid, min_pts(ts), off)
        else:
            w, h = probe_wh(p); fs = w * h * 3 // 2
            dec = sp.Popen(['ffmpeg', '-v', 'error', '-i', p, '-map', '0:v:0', '-f', 'rawvideo', '-pix_fmt', 'yuv420p', '-'], stdout=sp.PIPE)
            enc = sp.Popen(['nice', 'ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'yuv420p', '-s', f'{w}x{h}', '-r', str(FPS),
                            '-i', '-', '-c:v', 'libx264', '-preset', 'medium', '-crf', '18', '-bf', '0', '-g', '48', '-pix_fmt', 'yuv420p',
                            '-r', str(FPS), '-output_ts_offset', f'{off:.6f}', '-muxdelay', '0', '-muxpreload', '0', '-f', 'mpegts', ts], stdin=sp.PIPE)
            wrote = 0
            for k in range(len(cnt)):
                fr = dec.stdout.read(fs); assert len(fr) == fs, (sid, k, 'short read')
                for _ in range(int(cnt[k])): enc.stdin.write(fr); wrote += 1
            dec.stdout.close(); dec.wait(); enc.stdin.close(); assert enc.wait() == 0 and dec.returncode == 0, sid
            assert wrote == nout
        got = nframes(ts); assert got == nout, (sid, got, nout)
        assert abs(min_pts(ts) - off) < 1e-3, (sid, 'pts start', min_pts(ts), off)
        print(f'{sid}: v2 frames {pos}–{pos + nout - 1} ({nout}; piece {len(cnt)}, dropped {int((cnt == 0).sum())}, '
              f'held +{int(np.maximum(cnt - 1, 0).sum())}) {"copy" if untouched else "re-encoded"}', flush=True)
        parts.append(ts); pos += nout
    assert pos == total, (pos, total)
    sp.run(['ffmpeg', '-v', 'error', '-y', '-i', 'concat:' + '|'.join(parts), '-map', '0:v:0', '-c', 'copy', '-movflags', '+faststart', OUT], check=True)
    n = nframes(OUT)
    pts = np.array([float(l.strip(',')) for l in sp.check_output(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'packet=pts_time',
                                                         '-of', 'csv=p=0', OUT]).decode().split() if l.strip(',')])
    pts.sort(); dif = np.diff(pts)
    ok_pts = bool(np.all(np.abs(dif - 1 / FPS) < 1e-3) and abs(pts[0]) < 1e-3)
    print(f'{OUT}: {n} frames, want {total} (v2 {total / FPS:.6f} s); pts start {pts[0]:.4f}, step min/max {dif.min():.5f}/{dif.max():.5f} '
          f'→ {"PTS OK" if ok_pts else "PTS PROBLEM"}')
    json.dump({'out': OUT, 'frames': n, 'want': total, 'pts_ok': ok_pts, 'preroll_frames': PF,
               'parts': [(sid, int(c.sum())) for sid, _, c in plan]}, open(OUT + '.json', 'w'), indent=1)
    assert n == total and ok_pts, 'frame count / pts check failed: parts kept in ' + TMP
    if '--keep-parts' not in sys.argv: shutil.rmtree(TMP)
if __name__ == '__main__': main()
