"""US vs Cartels final 4K master in ONE pass (2026-11-23): fetch each 4K piece (render4k/<seg>, SHA-256 checked) into /dev/shm one at a time,
apply project/cartels/fix1_ops.json exactly as tools/ct_fix_assemble.py (v2 = cts00 pre-roll + v1 frames minus `del`, `ins` = held frames),
splice Krish's 3D renders (--replace FILE:G0, conformed by tools/ct_conform_3d.py), and stream every frame into ONE x264 encode muxed with
the final audio → OUT.mp4 (no TS parts, no faststart rewrite: peak disk ≈ the final + one piece; 4K pieces are ~68 Mbps).
Usage: .venv/bin/python tools/ct_final4k_stream.py OUT.mp4 AUDIO.m4a [--crf 21] [--preset faster] [--replace F:G0 …] [--cts00 /dev/shm/ct4k/cts00.mp4]"""
import json, os, sys, time, threading, subprocess as sp, hashlib, numpy as np
sys.path.insert(0, 'tools')
from ct_fix_remap import load_ops
FPS, W, H = 24, 3840, 2160; FS = W * H * 3 // 2; V1_FRAMES = 32206
OUT, AUD = sys.argv[1], sys.argv[2]
def arg(k, d): return sys.argv[sys.argv.index(k) + 1] if k in sys.argv else d
CRF, PRESET, C00 = arg('--crf', '21'), arg('--preset', 'faster'), arg('--cts00', '/dev/shm/ct4k/cts00.mp4')
PD = '/dev/shm/ct4k'; URL = sp.check_output(['git', 'remote', 'get-url', 'origin']).decode().strip()
def nframes(p): return int(sp.check_output(['ffprobe', '-v', 'error', '-count_packets', '-select_streams', 'v:0', '-show_entries', 'stream=nb_read_packets', '-of', 'csv=p=0', p]).split()[0])
def log(*a): print(time.strftime('%H:%M:%SZ', time.gmtime()), *a, flush=True)
REPL = [(int(g), int(g) + nframes(f), f) for f, g in (a.rsplit(':', 1) for i, a in enumerate(sys.argv) if i and sys.argv[i - 1] == '--replace')]

def fetch(s):
    """render4k/<s> → PD/<s>.mp4 (SHA-256 checked); waits for the branch to exist"""
    p = f'{PD}/{s}.mp4'
    if os.path.exists(p + '.ok'): return p
    while sp.run(['git', 'ls-remote', '--exit-code', URL, f'refs/heads/render4k/{s}'], capture_output=True).returncode:
        log(s, 'waiting for branch'); time.sleep(60)
    G = f'/dev/shm/g_{s}'   # blob-less bare clone: only the piece's blobs are downloaded, lazily (a plain depth-1 fetch pulls the whole
    for k in range(4):       # repo snapshot — several GB into /dev/shm — and got the encoder OOM-killed on 2026-11-23)
        sp.run(['rm', '-rf', G])
        if sp.run(['git', 'clone', '-q', '--bare', '--depth', '1', '--filter=blob:none', '--branch', f'render4k/{s}', URL, G]).returncode == 0: break
        time.sleep(10 * 2 ** k)
    names = sorted(n for n in sp.check_output(['git', f'--git-dir={G}', 'ls-tree', '--name-only', 'HEAD', f'pieces/{s}/']).decode().split() if '.part' in n)
    with open(p, 'wb') as o:
        for n in names:
            sp.run(['git', f'--git-dir={G}', 'cat-file', '-p', f'HEAD:{n}'], stdout=o, check=True); o.flush()
    want = sp.check_output(['git', f'--git-dir={G}', 'cat-file', '-p', f'HEAD:pieces/{s}/{s}.mp4.sha256']).decode().split()[0]
    sp.run(['rm', '-rf', G]); got = sp.check_output(['sha256sum', p]).decode().split()[0]
    assert got == want, (s, 'SHA MISMATCH', got, want)
    open(p + '.ok', 'w').close(); log(s, f'fetched {os.path.getsize(p) / 1e6:.0f} MB, sha OK'); return p

J, ops = load_ops('project/cartels/fix1_ops.json'); PF = round(float(J['preroll']) * FPS)
keep = np.ones(V1_FRAMES, np.int32)
for o in ops:
    f = round(o['t'] * FPS)
    if 'del' in o: keep[f:f + round(o['del'] * FPS)] = 0
    else: keep[max(f - 1, 0)] += round(o['ins'] * FPS)
SEG = json.load(open('project/cartels/segments.json'))['segments']; G0 = [round(s['start'] * FPS) for s in SEG] + [V1_FRAMES]
total = PF + int(keep.sum()); log('v2 frames', total, f'({total / FPS:.3f} s)')
ad = float(sp.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', AUD]))
assert abs(ad - total / FPS) < 0.05, ('audio length', ad, total / FPS)
enc = sp.Popen(['nice', 'ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'yuv420p', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-', '-i', AUD,
                '-map', '0:v', '-map', '1:a', '-c:v', 'libx264', '-preset', PRESET, '-crf', CRF, '-pix_fmt', 'yuv420p', '-g', '48',
                '-color_primaries', 'bt709', '-color_trc', 'bt709', '-colorspace', 'bt709', '-c:a', 'copy', OUT], stdin=sp.PIPE)
wrote = 0
def frames(p):
    d = sp.Popen(['ffmpeg', '-v', 'error', '-i', p, '-map', '0:v:0', '-f', 'rawvideo', '-pix_fmt', 'yuv420p', '-'], stdout=sp.PIPE)
    while True:
        fr = d.stdout.read(FS)
        if len(fr) < FS: break
        yield fr
    d.wait()
# pre-roll
last = None
for k, fr in enumerate(frames(C00)):
    if k >= PF: break
    enc.stdin.write(fr); wrote += 1; last = fr
while wrote < PF: enc.stdin.write(last); wrote += 1
log('cts00 pre-roll', PF)
# replacement readers
rd = {f: frames(f) for _, _, f in REPL}; rpos = {f: a for a, _, f in REPL}
def repl(g):
    for a, b, f in REPL:
        if a <= g < b:
            while rpos[f] < g: next(rd[f]); rpos[f] += 1
            rpos[f] += 1; return next(rd[f])
    return None
nxt = {}
def prefetch(s): nxt[s] = fetch(s)
for i, s in enumerate(SEG):
    sid = s['id']; p = nxt.pop(sid, None) or fetch(sid)
    t = None
    if i + 1 < len(SEG): t = threading.Thread(target=prefetch, args=(SEG[i + 1]['id'],)); t.start()
    slot = G0[i + 1] - G0[i]; k_ = keep[G0[i]:G0[i + 1]]; n = 0; last = None; out0 = wrote
    for k, fr in enumerate(frames(p)):
        if k >= slot: break
        n += 1; last = fr; g = G0[i] + k
        if k_[k]:
            r = repl(g); fr = r if r is not None else fr
            for _ in range(int(k_[k])): enc.stdin.write(fr); wrote += 1
    assert n > 0
    if n < slot:                                      # short piece: hold its last frame (as assemble_cartels)
        for _ in range(int(k_[n:].sum())): enc.stdin.write(last); wrote += 1
    log(f'{sid}: piece {n} frames (slot {slot}), wrote {wrote - out0} → total {wrote}/{total}')
    os.remove(p); os.remove(p + '.ok')
    if t: t.join()
enc.stdin.close(); assert enc.wait() == 0
assert wrote == total, (wrote, total)
nf = nframes(OUT); log(OUT, 'frames', nf, 'want', total, 'OK' if nf == total else 'MISMATCH', f'{os.path.getsize(OUT) / 1e9:.2f} GB')
