"""Combine the three raw parts into ONE raw timeline (48 kHz 16-bit stereo, bit-exact samples, no gain):
part 1 at 0, part 2 (mono -> both channels, padded with silence to a whole 60 fps frame) after it, part 3 after that.
Writes project/nvidia/media/raw_audio.wav, project/nvidia/parts.json, project/nvidia/raw_transcript.json (global word ids/times)."""
import json, math, numpy as np, soundfile as sf
FPS = 60; sr = 48000; out = []; parts = []; words = []; off = 0
for p in (1, 2, 3):
    x, r = sf.read(f'project/nvidia/media/raw_p{p}.wav', dtype='float64', always_2d=True); assert r == sr
    print(p, x.shape, 'peak', np.abs(x).max())
    assert np.abs(x).max() < 1.0, 'float clip'
    if x.shape[1] == 1: x = np.repeat(x, 2, 1)
    frames = math.ceil(len(x) / (sr // FPS)); n = frames * (sr // FPS)
    x = np.vstack([x, np.zeros((n - len(x), 2))])
    y = np.round(x * 32768).clip(-32768, 32767).astype(np.int16)
    d = json.load(open(f'work/asr/nv/p{p}/transcript.json')); w = d['words'] if isinstance(d, dict) else d
    t0 = off / sr
    parts.append({'part': p, 'offset': t0, 'frames': frames, 'dur': n / sr, 'w0': len(words), 'w1': len(words) + len(w) - 1, 'video': p != 2})
    for q in w: words.append({'id': f'w{len(words)}', 'text': q['text'], 'start': round(q['start'] + t0, 3), 'end': round(q['end'] + t0, 3), 'part': p})
    out.append(y); off += n
sf.write('project/nvidia/media/raw_audio.wav', np.vstack(out), sr, subtype='PCM_16')
json.dump(parts, open('project/nvidia/parts.json', 'w'), indent=1); json.dump(words, open('project/nvidia/raw_transcript.json', 'w'))
print(parts, len(words), off / sr)
