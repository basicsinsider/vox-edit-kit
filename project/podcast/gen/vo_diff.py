"""Re-transcribe the EDITED VO in chunks and diff against the kept words (transcript_pd.json) — finds leaked fragments, chopped
or doubled words at joins (Paraguay method). Prints diffs that lie within 1.5 s of an EDL join."""
import json, os, re, subprocess, difflib, numpy as np, soundfile as sf
P = 'project/podcast/'; d = 'work/asr/vo'; os.makedirs(d, exist_ok=True)
x, sr = sf.read(P + 'media/vo_pd.wav', dtype='float32'); D = len(x) / sr
F = json.load(open(P + 'edl_frames.json')); joins = [s['edit_in'] for s in F['segments'][1:]]
env = dict(os.environ, PATH=os.path.expanduser('~/.local/bin') + ':' + os.environ['PATH'])
# chunk boundaries far from joins, at quiet points
h = int(0.05 * sr); n = len(x) // h; rms = np.sqrt((x[:n * h].reshape(n, h) ** 2).mean(1))
cuts = [0.0]; t = 600.0
while t < D - 120:
    i0, i1 = int((t - 20) / 0.05), int((t + 20) / 0.05); c = [(rms[k], k * 0.05) for k in range(i0, i1) if min(abs(k * 0.05 - j) for j in joins) > 2]
    cuts.append(min(c)[1]); t = cuts[-1] + 600.0
cuts.append(D); ws = []
for i in range(len(cuts) - 1):
    c = f'{d}/c{i:02d}'; os.makedirs(c, exist_ok=True)
    if not os.path.exists(c + '/transcript.json'):
        seg = x[int(cuts[i] * sr):int(cuts[i + 1] * sr)]
        sf.write(c + '/w44.wav', seg, sr, subtype='PCM_16')
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', c + '/w44.wav', '-ar', '16000', c + '/w.wav'], check=True); os.remove(c + '/w44.wav')
        subprocess.run(['npx', '--yes', 'hyperframes@0.8.217', 'transcribe', 'w.wav', '--engine', 'parakeet', '--dir', '.'], cwd=c, env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        os.remove(c + '/w.wav')
    t = json.load(open(c + '/transcript.json')); t = t['words'] if isinstance(t, dict) else t
    ws += [{'text': q['text'], 'start': cuts[i] + q['start']} for q in t]
    print('chunk', i, len(t), flush=True)
json.dump(ws, open(d + '/vo_words.json', 'w'))
A = json.load(open('transcript_pd.json')); norm = lambda s: re.sub(r'[^a-z0-9]', '', s.lower())
a = [norm(q['text']) for q in A]; b = [norm(q['text']) for q in ws]
sm = difflib.SequenceMatcher(None, a, b, autojunk=False); rep = []
for tag, i1, i2, j1, j2 in sm.get_opcodes():
    if tag == 'equal': continue
    t0 = A[min(i1, len(A) - 1)]['start']; near = min(abs(t0 - j) for j in joins)
    if near <= 1.5:
        rep.append(f"{t0:8.2f} join±{near:.2f} raw_id {A[min(i1,len(A)-1)]['raw_id']}: kept[{' '.join(q['text'] for q in A[max(i1-3,0):i1])} «{' '.join(q['text'] for q in A[i1:i2])}» {' '.join(q['text'] for q in A[i2:i2+3])}]  heard[«{' '.join(q['text'] for q in ws[j1:j2])}»]")
open(P + 'analysis/vo_diff.txt', 'w').write('\n'.join(rep)); print(len(rep), 'diffs near joins ->', P + 'analysis/vo_diff.txt')
