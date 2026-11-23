"""Conform Krish's 3D renders (Google Doc comments, 2026-11-23) to the Cartels v1 master timeline: 3840×2160, 24 fps, exactly one
frame per v1 frame g in [G0, G1). Used by tools/ct_fix_assemble.py --replace OUT:G0 (the fix1 ops then cut them like everything else).
  R4 (29.97 fps, 4K, carries our v1 VO): its audio matched vo_ct.wav sample-exactly in 4 pieces (FFT cross-correlation, 1 s chunks):
     R4 t∈[0,41.5) → v1 t+117.0857 · [41.5,48.1) → +117.3021 · [48.1,55.4554) → +117.2281 · [55.4554,end) → +117.3147
     (the animator nudged 3 pauses by +0.216/−0.074/+0.087 s); gaps hold the last frame, the overlap is skipped → picture locked to the words.
  R1 (24 fps, 1080p, silent): v1 = t + 27.3 (Isidro's face on "El Chapo Isidro" 36.24, the El Chapo mugshot on "the famous El Chapo" 41.0),
     used from v1 31.75 (R1 4.45 s, lasers on the man at the window) to 44.208 ("They are just as accomplished" = our edit again); lanczos 2×.
Usage: .venv/bin/python tools/ct_conform_3d.py R4 /dev/shm/r3d/R4.bin OUT.mp4 | R1 /dev/shm/r3d/R1.bin OUT.mp4"""
import sys, math, subprocess as sp
which, src, out = sys.argv[1:4]
W, H, FPS = 3840, 2160, 24
if which == 'R4':
    SRC_FPS = 30000 / 1001; G0, G1 = 2810, 4794          # v1 117.0833 (“To answer that”) → 199.75 (before “This war is where…”)
    SEGS = [(0.0, 41.5, 117.0857), (41.5, 48.1, 117.3021), (48.1, 55.4554, 117.2281), (55.4554, 99.0, 117.3147)]
    def src_t(T):
        last = 0.0
        for a, b, off in SEGS:
            if T < a + off: break                           # in a gap before this segment: hold the previous one's last frame
            if T < b + off: return max(T - off, 0.0)        # first match wins → the 0.074 s overlap (B/C) is skipped, not repeated
            last = b - 1e-6
        return last
    vf = None
else:
    SRC_FPS = 24.0; G0, G1 = 762, 1061                    # v1 31.75 → 44.208
    def src_t(T): return T - 27.3
    vf = f'scale={W}:{H}:flags=lanczos'
NSRC = int(sp.check_output(['ffprobe', '-v', 'error', '-count_packets', '-select_streams', 'v:0', '-show_entries', 'stream=nb_read_packets',
                            '-of', 'csv=p=0', src]).split()[0])
idx = [min(max(int(math.floor(src_t(g / FPS) * SRC_FPS + 0.5)), 0), NSRC - 1) for g in range(G0, G1)]
assert all(b >= a for a, b in zip(idx, idx[1:])), 'non-monotonic'
fs = W * H * 3 // 2
dec = sp.Popen(['ffmpeg', '-v', 'error', '-i', src] + (['-vf', vf] if vf else []) + ['-f', 'rawvideo', '-pix_fmt', 'yuv420p', '-s', f'{W}x{H}', '-'], stdout=sp.PIPE)
enc = sp.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'yuv420p', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                '-c:v', 'libx264', '-preset', 'fast', '-crf', '14', '-pix_fmt', 'yuv420p', '-color_primaries', 'bt709', '-color_trc', 'bt709',
                '-colorspace', 'bt709', '-movflags', '+faststart', out], stdin=sp.PIPE)
cur, fr = -1, None
for k in idx:
    while cur < k: fr = dec.stdout.read(fs); assert len(fr) == fs, ('short read', cur); cur += 1
    enc.stdin.write(fr)
dec.kill(); enc.stdin.close(); assert enc.wait() == 0
print(which, 'frames', len(idx), 'v1', G0, G1, f'({G0 / FPS:.4f}–{G1 / FPS:.4f} s)', 'src frames used', idx[0], '…', idx[-1], 'held', len(idx) - len(set(idx)))
