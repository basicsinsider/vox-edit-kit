"""Cut the raw audio by edl_frames.json (30 fps grid: 1470 samples/frame at 44.1 kHz, so picture and sound never drift).
Butt joins with short fades (4 ms in silence, 12 ms where a cut point is louder than noise+10 dB). No gain/EQ/normalisation.
Writes project/podcast/media/vo_pd.wav (44.1 kHz mono 16-bit = the camera audio decoded, cut only), vo_pd.mp3 (preview for
compositions/sound tools) and transcript_pd.json (kept words in MASTER seconds)."""
import json, subprocess, numpy as np, soundfile as sf
P = 'project/podcast/'
F = json.load(open(P + 'edl_frames.json')); E = json.load(open(P + 'EDL.json')); NOISE = E['noise_floor_db']
x, sr = sf.read(P + 'media/raw_audio.wav', dtype='int16'); spf = sr // F['fps']; assert spf * F['fps'] == sr
out = []
for s in F['segments']:
    seg = x[s['f0'] * spf:s['f1'] * spf].astype(np.float64)
    ni = int((0.012 if s['in_db'] > NOISE + 10 else 0.004) * sr); no = int((0.012 if s['out_db'] > NOISE + 10 else 0.004) * sr)
    if s['f0'] > 0: seg[:ni] *= np.linspace(0, 1, ni)
    seg[-no:] *= np.linspace(1, 0, no)
    out.append(np.round(seg).astype(np.int16))
y = np.concatenate(out); sf.write(P + 'media/vo_pd.wav', y, sr, subtype='PCM_16')
print('vo_pd.wav', len(y) / sr, 's; expected', F['length'])
w = json.load(open(P + 'raw_transcript.json')); segs = F['segments']; k = 0; tw = []
for q in w:
    m = (q['start'] + q['end']) / 2
    while k < len(segs) - 1 and m >= segs[k]['raw_out']: k += 1
    s = segs[k]
    if not (s['raw_in'] <= m < s['raw_out']) or not (s['w'][0] <= q['id'] <= s['w'][1]): continue
    d = s['edit_in'] - s['raw_in']
    tw.append({'id': f"w{len(tw)}", 'text': q['text'], 'start': round(max(q['start'], s['raw_in']) + d, 3), 'end': round(min(q['end'], s['raw_out']) + d, 3), 'raw_id': q['id']})
json.dump(tw, open('transcript_pd.json', 'w'))
print('transcript_pd.json', len(tw), 'words')
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', P + 'media/vo_pd.wav', '-c:a', 'libmp3lame', '-b:a', '128k', 'vo_pd.mp3'], check=True)
