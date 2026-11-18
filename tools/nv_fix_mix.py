"""NVIDIA review fix — final audio v2 (owner request 2026-11-18: "raise the volume whenever it's low", whole video):
  mix = VO_v2 + music + sfx + ambience at unity (the approved balance, beds rebuilt on the cut timeline by place_sound),
  then ONE slow gain ride on the whole mix that brings every passage's speech to the same short-term level
  (VO 3 s loudness, speech-gated, ±6 s median, ±2 s smoothing, clamp −3…+9 dB), then gain to −14 LUFS-I and a
  peak limiter (ffmpeg alimiter, −1.5 dBFS ceiling) → AAC 320k. No EQ, no compression beyond the limiter's peaks.
Usage: .venv/bin/python tools/nv_fix_mix.py BEDS_DIR OUT.m4a"""
import re, sys, subprocess as sp, numpy as np, soundfile as sf
sys.path.insert(0, 'tools/audio')
from loudness import integrated_lufs
BEDS, OUT = sys.argv[1], sys.argv[2]; SR = 48000
NEW = float(__import__('json').load(open('work/fix1/map.json'))['new_len']); N = round(NEW * SR)
def rd(p):
    y, sr = sf.read(p, dtype='float32', always_2d=True); assert sr == SR, (p, sr)
    if y.shape[1] == 1: y = np.repeat(y, 2, 1)
    out = np.zeros((N, 2), np.float32); m = min(N, len(y)); out[:m] = y[:m]; return out
mix = rd('work/fix1/vo_v2.wav')
for b in ('music_bed', 'sfx', 'ambience'): mix += rd(f'{BEDS}/{b}.wav')
# speech loudness envelope from the VO's short-term loudness (ffmpeg ebur128, 10 Hz)
t, S = [], []
cur = None
for l in open('work/fix1/vo_v2_S.txt'):
    m = re.search(r'pts_time:([\d.]+)', l)
    if m: cur = float(m.group(1)); continue
    m = re.search(r'r128.S=(-?[\d.]+|-inf)', l)
    if m and cur is not None: t.append(cur); S.append(float(m.group(1)) if m.group(1) != '-inf' else -120)
t, S = np.array(t), np.array(S)
grid = np.arange(0, NEW + 0.1, 0.1)
St = np.interp(grid, t, S); sp_ = St > -45
env = np.full(len(grid), np.nan)
for i in range(len(grid)):
    w = St[max(0, i - 60):i + 61][sp_[max(0, i - 60):i + 61]]
    if len(w) > 20: env[i] = np.median(w)
ok = ~np.isnan(env); env = np.interp(np.arange(len(grid)), np.where(ok)[0], env[ok])
TARGET = np.percentile(St[sp_], 75)                     # bring quiet passages up to the louder passages' level
g = np.clip(TARGET - env, -3, 9)
k = np.ones(41) / 41; g = np.convolve(np.pad(g, 20, mode='edge'), k, 'valid')   # ±2 s smoothing
gl = np.interp(np.arange(N) / SR, grid, g).astype(np.float32)
mix *= (10 ** (gl / 20))[:, None]
lufs = integrated_lufs(mix, SR); gain = -14.0 - lufs
print(f'ride target S {TARGET:.1f}; ride gain p5/p50/p95 {np.percentile(g,5):.1f}/{np.percentile(g,50):.1f}/{np.percentile(g,95):.1f} dB; '
      f'mix after ride {lufs:.1f} LUFS → +{gain:.1f} dB; peak before limiter {20*np.log10(np.abs(mix).max())+gain:.1f} dBFS')
mix *= 10 ** (gain / 20)
over = (np.abs(mix) > 10 ** (-1.5 / 20)).mean() * 100
print(f'samples over the −1.5 dBFS ceiling: {over:.3f} %')
np.savetxt('work/fix1/ride_db.txt', np.c_[grid, g], fmt='%.1f %.2f')
sf.write('/dev/shm/mix_v2.wav', mix, SR, subtype='FLOAT')
sp.run(['ffmpeg', '-v', 'error', '-y', '-i', '/dev/shm/mix_v2.wav', '-af', 'alimiter=limit=0.8414:attack=3:release=60:level=disabled:asc=1',
        '-c:a', 'aac', '-b:a', '320k', '-ar', '48000', '-t', f'{NEW:.6f}', '-movflags', '+faststart', OUT], check=True)
