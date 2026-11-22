"""Cut the raw VO by project/cartels/EDL.json. No picture -> cut points on a 1 ms grid. Butt joins with short fades
(4 ms in silence, 12 ms where the cut is inside speech). No gain/EQ/normalisation: samples are copied as float32.
Writes project/cartels/media/vo_ct.wav (48 kHz mono float32), project/cartels/edl_map.json (raw->edited time map)."""
import json, numpy as np, soundfile as sf
E = json.load(open('project/cartels/EDL.json'))
x, sr = sf.read('input/vo_raw.wav', dtype='float32')
out = []; segs = []; t = 0.0
for s in E['segments']:
    a, b = round(s['in'] * 1000) * sr // 1000, round(s['out'] * 1000) * sr // 1000
    seg = x[a:b].copy()
    ni = int((0.012 if s['in_db'] > -60 else 0.004) * sr); no = int((0.012 if s['out_db'] > -60 else 0.004) * sr)
    seg[:ni] *= np.linspace(0, 1, ni, dtype=np.float32); seg[-no:] *= np.linspace(1, 0, no, dtype=np.float32)
    out.append(seg)
    segs.append({'w': s['w'], 'raw_in': a / sr, 'raw_out': b / sr, 'edit_in': round(t, 5), 'note': s['note']})
    t += (b - a) / sr
y = np.concatenate(out); sf.write('project/cartels/media/vo_ct.wav', y, sr, subtype='FLOAT')
json.dump({'segments': segs, 'length': round(t, 5)}, open('project/cartels/edl_map.json', 'w'), indent=1)
print('edited length', round(t, 3), 's', len(segs), 'segments')
