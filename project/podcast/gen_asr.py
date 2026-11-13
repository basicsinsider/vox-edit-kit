"""Transcribe the raw take in ~10-min chunks split at the quietest point near each boundary (Parakeet, word times).
Writes project/podcast/raw_transcript.json (list of {id,text,start,end} in raw seconds). Usage: .venv/bin/python project/podcast/gen_asr.py"""
import json, os, subprocess, numpy as np, soundfile as sf
W = 'work/asr/raw16k.wav'; x, sr = sf.read(W, dtype='float32'); D = len(x) / sr
hop = int(0.05 * sr); n = len(x) // hop
rms = np.sqrt((x[:n * hop].reshape(n, hop) ** 2).mean(1))
sm = np.convolve(rms, np.ones(8) / 8, 'same')          # 0.4 s smoothing
cuts = [0.0]
t = 600.0
while t < D - 120:
    i0, i1 = int((t - 20) / 0.05), int((t + 20) / 0.05); k = i0 + int(np.argmin(sm[i0:i1])); cuts.append(k * 0.05); t = cuts[-1] + 600.0
cuts.append(D); json.dump(cuts, open('work/asr/cuts.json', 'w'))
env = dict(os.environ, PATH=os.path.expanduser('~/.local/bin') + ':' + os.environ['PATH'])
words = []
for i in range(len(cuts) - 1):
    d = f'work/asr/c{i:02d}'; os.makedirs(d, exist_ok=True)
    if not os.path.exists(d + '/transcript.json'):
        sf.write(d + '/w.wav', x[int(cuts[i] * sr):int(cuts[i + 1] * sr)], sr, subtype='PCM_16')
        subprocess.run(['npx', '--yes', 'hyperframes@0.8.217', 'transcribe', 'w.wav', '--engine', 'parakeet', '--dir', '.'], cwd=d, env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        os.remove(d + '/w.wav')
    t = json.load(open(d + '/transcript.json')); t = t['words'] if isinstance(t, dict) else t
    for w in t: words.append({'id': len(words), 'text': w['text'], 'start': round(cuts[i] + w['start'], 3), 'end': round(cuts[i] + w['end'], 3)})
    print(i, round(cuts[i], 1), len(t), 'words', flush=True)
json.dump(words, open('project/podcast/raw_transcript.json', 'w'))
print('total', len(words), 'words', D)
