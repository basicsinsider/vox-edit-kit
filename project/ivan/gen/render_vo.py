"""Cut the raw take by EDL.json: cut points snapped to the 60 fps frame grid (audio+video stay locked, no drift),
butt joins with short fades (4 ms in silence, 12 ms where the cut is inside speech). No gain/EQ/normalisation.
Writes vo_ivan.wav (48 kHz 16-bit, the edited VO), project/ivan/edl_frames.json (frame-exact segments for ffmpeg),
and project/ivan/edl_map.json (raw->edited time map)."""
import json, numpy as np, soundfile as sf
E = json.load(open('project/ivan/EDL.json'))
x, sr = sf.read('project/ivan/media/raw_audio.wav', dtype='int16')
FPS = 60
out = []; segs = []; t_edit = 0.0
for s in E['segments']:
    f0, f1 = round(s['in'] * FPS), round(s['out'] * FPS)
    a, b = f0 * sr // FPS, f1 * sr // FPS
    seg = x[a:b].astype(np.float64)
    fin = 0.012 if s['in_db'] > -60 else 0.004; fout = 0.012 if s['out_db'] > -60 else 0.004
    ni, no = int(fin * sr), int(fout * sr)
    seg[:ni] *= np.linspace(0, 1, ni)[:, None]; seg[-no:] *= np.linspace(1, 0, no)[:, None]
    out.append(np.round(seg).astype(np.int16))
    segs.append({'w': s['w'], 'f0': f0, 'f1': f1, 'raw_in': f0 / FPS, 'raw_out': f1 / FPS, 'edit_in': round(t_edit, 4)})
    t_edit += (f1 - f0) / FPS
y = np.concatenate(out); sf.write('vo_ivan.wav', y, sr, subtype='PCM_16')
json.dump({'fps': FPS, 'segments': segs, 'length': round(t_edit, 4)}, open('project/ivan/edl_frames.json', 'w'), indent=1)
print('edited length', round(t_edit, 3), 's', len(segs), 'segments; samples', len(y), '=', len(y) / sr)
