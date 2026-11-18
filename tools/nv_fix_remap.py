"""NVIDIA review fix: apply project/nvidia/fix_cuts.json to the audio side.
  work/fix1/vo_v2.wav            VO with the pause cuts (sample-exact, 4 ms fades at each join; samples otherwise untouched)
  work/fix1/transcript_v2.json   word times remapped (audio map)
  work/fix1/sfx/nvsNN.sfx.json   editors' SFX markers remapped (video map: they follow picture events)
  work/fix1/music_cuesheet_v2.json  cue sheet: layer start/end + auto points + stingers remapped (audio map), length = new master
Usage: .venv/bin/python tools/nv_fix_remap.py"""
import json, glob, os, numpy as np, soundfile as sf
C = json.load(open('project/nvidia/fix_cuts.json'))['cuts']; FPS = 24
OLD_LEN = 2402.0; NEW_LEN = round(OLD_LEN - sum(c['L'] for c in C), 6)
def mk(a_key, b_key):
    cs = sorted((c[a_key], c[b_key]) for c in C)
    def M(t):
        s = 0.0
        for a, b in cs:
            if t >= b: s += b - a
            elif t > a: return a - s
        return t - s
    return M
MA, MV = mk('a_a', 'b_a'), mk('a_v', 'b_v')
os.makedirs('work/fix1/sfx', exist_ok=True)
# VO
x, sr = sf.read('project/nvidia/media/vo_nv.wav', dtype='int16', always_2d=True)
keep, prev = [], 0
for a, b in sorted((c['a_a'], c['b_a']) for c in C):
    keep.append((prev, round(a * sr))); prev = round(b * sr)
keep.append((prev, len(x)))
fd = int(0.004 * sr); parts = []
for k, (a, b) in enumerate(keep):
    p = x[a:b].astype(np.float64)
    if k > 0: p[:fd] *= np.linspace(0, 1, fd)[:, None]
    if k < len(keep) - 1: p[-fd:] *= np.linspace(1, 0, fd)[:, None]
    parts.append(np.round(p).astype(np.int16))
y = np.concatenate(parts)
sf.write('work/fix1/vo_v2.wav', y, sr, subtype='PCM_16')
print('VO', len(x) / sr, '->', len(y) / sr, 'removed', (len(x) - len(y)) / sr)
# transcript
W = json.load(open('transcript_nv.json'))
for w in W: w['start'] = round(MA(w['start']), 3); w['end'] = round(MA(w['end']), 3)
json.dump(W, open('work/fix1/transcript_v2.json', 'w'), ensure_ascii=False)
# sfx markers
n = 0
for f in sorted(glob.glob('compositions/nvs*.sfx.json')):
    m = json.load(open(f))
    for e in m: e['t'] = round(MV(e['t']), 4); n += 1
    json.dump(m, open('work/fix1/sfx/' + os.path.basename(f), 'w'), indent=1, ensure_ascii=False)
# cue sheet
cs = json.load(open('project/nvidia/music_cuesheet.json'))
cs['length'] = NEW_LEN
for L in cs['layers']:
    L['start'] = round(MA(L['start']), 4); L['end'] = round(MA(L['end']), 4)
    if 'auto' in L: L['auto'] = [[round(MA(t), 4), v] for t, v in L['auto']]
for s in cs.get('stingers', []): s['t'] = round(MA(s['t']), 4)
for key in ('ducks', 'bleeps'):
    for d in cs.get(key, []): raise SystemExit(f'{key} present: remap not implemented')
json.dump(cs, open('work/fix1/music_cuesheet_v2.json', 'w'), indent=1, ensure_ascii=False)
json.dump({'new_len': NEW_LEN, 'cuts_audio': sorted((c['a_a'], c['b_a']) for c in C), 'cuts_video': sorted((c['a_v'], c['b_v']) for c in C)},
          open('work/fix1/map.json', 'w'), indent=1)
print('markers', n, 'layers', len(cs['layers']), 'new master', NEW_LEN, 's =', round(NEW_LEN * FPS, 3), 'frames')
