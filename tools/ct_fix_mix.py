"""US vs Cartels fix round 1 — levelling + final audio on master v2 (copy of tools/nv_fix_mix.py; Sam's review note #2
"equalize the audio… raise it when it's low and lower it when it's high", reply: "doesn't need to be one level but within a certain
range, not too much variation" — owner-approved exception to MANUAL §0 for this video, FIXES_ROUND1 rule 3; NO EQ, NO compressor):
  mix = [preroll clip audio 0…P] + VO_v2 delayed by P (mono → stereo by duplicating the channel = ffmpeg pan=stereo|c0=c0|c1=c0,
        unity — never aformat, which scales by 0.707) + music + sfx + ambience at unity (beds rebuilt on v2 by place_sound)
  then ONE slow gain ride on the whole mix from the VO's speech-gated 3 s loudness (ebur128 S at 10 Hz, gate = VO I − 13 LU):
        env = ±6 s median of the speech S, gain = clip(TARGET − env, LO, HI) with TARGET = the speech S median, ±2 s smoothing
        → quiet passages come up, loud passages go down, word-to-word dynamics inside ±6 s untouched ("within a range");
  then gain to −14 LUFS-I and a peak limiter (alimiter, −2 dBFS ceiling) → AAC 320k.
  Over the pre-roll (no VO) the ride holds its value at P.
Usage: .venv/bin/python tools/ct_fix_mix.py --vo-only            test: ride on the VO alone, print LRA / 3 s spread before → after
       .venv/bin/python tools/ct_fix_mix.py BEDS_DIR OUT.m4a [--preroll-audio clip.wav (default assets/cartels/footage/cold_open_audio.wav)] [--lo -4] [--hi 6]"""
import re, sys, json, subprocess as sp, numpy as np, soundfile as sf
sys.path.insert(0, 'tools/audio')
SR = 48000; CEIL = -2.0; TARGET_I = -14.0
def arg(k, d): return type(d)(sys.argv[sys.argv.index(k) + 1]) if k in sys.argv else d
LO, HI = arg('--lo', -4.0), arg('--hi', 6.0)
MAP = json.load(open('work/fix1/map.json')); P = float(MAP['preroll']); NEW = float(MAP['new_len']); N = round(NEW * SR)
VO = 'work/fix1/vo_v2.wav'

def ebur(path, tag):
    """short-term loudness at 10 Hz + I + LRA of a file (ffmpeg ebur128)"""
    f = f'/dev/shm/ct_mix_{tag}_S.txt'
    r = sp.run(['nice', 'ffmpeg', '-hide_banner', '-nostats', '-i', path, '-af',
                f'ebur128=metadata=1,ametadata=mode=print:key=lavfi.r128.S:file={f}', '-f', 'null', '-'], capture_output=True, text=True)
    I = float(re.findall(r'I:\s+(-?[\d.]+) LUFS', r.stderr)[-1]); LRA = float(re.findall(r'LRA:\s+(-?[\d.]+) LU', r.stderr)[-1])
    t, S, cur = [], [], None
    for l in open(f):
        m = re.search(r'pts_time:([\d.]+)', l)
        if m: cur = float(m.group(1)); continue
        m = re.search(r'r128.S=(-?[\d.]+|-inf)', l)
        if m and cur is not None: t.append(cur); S.append(float(m.group(1)) if m.group(1) != '-inf' else -120.0)
    return np.array(t), np.array(S), I, LRA

def ride(t, S, I, length):
    grid = np.arange(0, length + 0.1, 0.1)
    St = np.interp(grid, t, S); sp_ = St > I - 13
    env = np.full(len(grid), np.nan)
    for i in range(len(grid)):
        w = St[max(0, i - 60):i + 61][sp_[max(0, i - 60):i + 61]]
        if len(w) > 20: env[i] = np.median(w)
    ok = ~np.isnan(env); env = np.interp(np.arange(len(grid)), np.where(ok)[0], env[ok])
    TARGET = np.median(St[sp_])
    g = np.clip(TARGET - env, LO, HI)
    k = np.ones(41) / 41; g = np.convolve(np.pad(g, 20, mode='edge'), k, 'valid')   # ±2 s smoothing
    return grid, g, TARGET, sp_

def spread(S, mask):
    v = S[mask]; return np.percentile(v, 5), np.percentile(v, 50), np.percentile(v, 95)

def vo_only():
    x = sf.read(VO, dtype='float32')[0]; L = len(x) / SR
    t, S, I, LRA = ebur(VO, 'before')
    grid, g, TARGET, mask = ride(t, S, I, L)
    gl = np.interp(np.arange(len(x)) / SR, grid, g).astype(np.float32)
    y = x * 10 ** (gl / 20); sf.write('/dev/shm/ct_mix_vo_ridden.wav', y, SR, subtype='FLOAT')
    t2, S2, I2, LRA2 = ebur('/dev/shm/ct_mix_vo_ridden.wav', 'after')
    m = np.interp(t, grid, mask.astype(float)) > 0.5; m2 = np.interp(t2, grid, mask.astype(float)) > 0.5
    a, b = spread(S, m), spread(S2, m2)
    print(f'VO v2 alone, ride clamp {LO:+.0f}…{HI:+.0f} dB, target S {TARGET:.1f} LUFS (speech median), gate {I - 13:.1f}')
    print(f'  ride gain p5/p50/p95 {np.percentile(g, 5):+.1f}/{np.percentile(g, 50):+.1f}/{np.percentile(g, 95):+.1f} dB, '
          f'min/max {g.min():+.1f}/{g.max():+.1f}; at clamp: {(g <= LO + 0.05).mean() * 100:.1f}% low, {(g >= HI - 0.05).mean() * 100:.1f}% high')
    print(f'  BEFORE  I {I:.1f} LUFS  LRA {LRA:.1f} LU  speech 3 s S p5/p50/p95 {a[0]:.1f}/{a[1]:.1f}/{a[2]:.1f} → spread {a[2] - a[0]:.1f} LU')
    print(f'  AFTER   I {I2:.1f} LUFS  LRA {LRA2:.1f} LU  speech 3 s S p5/p50/p95 {b[0]:.1f}/{b[1]:.1f}/{b[2]:.1f} → spread {b[2] - b[0]:.1f} LU')
    # per-minute speech medians (where the passages sat)
    mins = [np.median(S[(t >= k * 60) & (t < k * 60 + 60) & m]) for k in range(int(L // 60) + 1) if ((t >= k * 60) & (t < k * 60 + 60) & m).sum() > 50]
    mins2 = [np.median(S2[(t2 >= k * 60) & (t2 < k * 60 + 60) & m2]) for k in range(int(L // 60) + 1) if ((t2 >= k * 60) & (t2 < k * 60 + 60) & m2).sum() > 50]
    print(f'  per-minute speech median range: before {min(mins):.1f}…{max(mins):.1f} ({max(mins) - min(mins):.1f} LU), '
          f'after {min(mins2):.1f}…{max(mins2):.1f} ({max(mins2) - min(mins2):.1f} LU)')
    np.savetxt('work/fix1/ride_vo_only_db.txt', np.c_[grid, g], fmt='%.1f %.2f')
    import os; os.remove('/dev/shm/ct_mix_vo_ridden.wav')

def full(BEDS, OUT):
    sys.path.insert(0, 'tools/audio'); from loudness import integrated_lufs
    def rd(p, at=0.0):
        y, sr = sf.read(p, dtype='float32', always_2d=True); assert sr == SR, (p, sr)
        if y.shape[1] == 1: y = np.repeat(y, 2, 1)         # mono → stereo duplicate (= pan=stereo|c0=c0|c1=c0), unity
        out = np.zeros((N, 2), np.float32); a = round(at * SR); m = min(N - a, len(y)); out[a:a + m] = y[:m]; return out
    vo = rd(VO, P); mix = vo.copy()
    for b in ('music_bed', 'sfx', 'ambience'): mix += rd(f'{BEDS}/{b}.wav')
    if P: mix += rd(arg('--preroll-audio', 'assets/cartels/footage/cold_open_audio.wav'))   # cts00's own clip audio, unity, at 0
    t, S, I, LRA = ebur(VO, 'mix'); t = t + P
    grid, g, TARGET, mask = ride(t, S, I, NEW)
    g[grid < P] = np.interp(P, grid, g) if P else g[grid < P]
    gl = np.interp(np.arange(N) / SR, grid, g).astype(np.float32)
    mix *= (10 ** (gl / 20))[:, None]
    lufs = integrated_lufs(mix, SR); gain = TARGET_I - lufs
    print(f'ride target S {TARGET:.1f}; clamp {LO}…{HI}; ride gain p5/p50/p95 {np.percentile(g, 5):.1f}/{np.percentile(g, 50):.1f}/{np.percentile(g, 95):.1f} dB; '
          f'mix after ride {lufs:.1f} LUFS → {gain:+.1f} dB; peak before limiter {20 * np.log10(np.abs(mix).max()) + gain:.1f} dBFS')
    mix *= 10 ** (gain / 20)
    print(f'samples over the ceiling: {(np.abs(mix) > 10 ** (CEIL / 20)).mean() * 100:.3f} %')
    np.savetxt('work/fix1/ride_db.txt', np.c_[grid, g], fmt='%.1f %.2f')
    sf.write('/dev/shm/ct_mix_v2.wav', mix, SR, subtype='FLOAT'); del mix, vo
    sp.run(['nice', 'ffmpeg', '-v', 'error', '-y', '-i', '/dev/shm/ct_mix_v2.wav', '-af',
            f'alimiter=limit={10 ** (CEIL / 20):.4f}:attack=3:release=60:level=disabled:asc=1',
            '-c:a', 'aac', '-b:a', '320k', '-ar', '48000', '-t', f'{NEW:.6f}', '-movflags', '+faststart', OUT], check=True)
    import os; os.remove('/dev/shm/ct_mix_v2.wav')

if __name__ == '__main__':
    if '--vo-only' in sys.argv: vo_only()
    else: full(sys.argv[1], sys.argv[2])
