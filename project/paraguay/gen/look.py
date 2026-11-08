"""Print raw words + a 20 ms RMS profile (dB, one char per 20 ms: ' '<-70 '.'<-55 '-'<-45 '='<-35 '#'>=-35) for a raw window."""
import json, sys, numpy as np, soundfile as sf
a, b = float(sys.argv[1]), float(sys.argv[2])
w = json.load(open('project/paraguay/raw_transcript.json'))
x, sr = sf.read('project/paraguay/media/raw_audio.wav', start=int(a * 48000), stop=int(b * 48000)); m = x.mean(1)
h = int(0.02 * sr); n = len(m) // h
d = 20 * np.log10(np.sqrt((m[:n * h].reshape(n, h) ** 2).mean(1)) + 1e-9)
s = ''.join(' ' if v < -70 else '.' if v < -55 else '-' if v < -45 else '=' if v < -35 else '#' for v in d)
for k in range(0, n, 50): print(f"{a + k * 0.02:8.2f} |{s[k:k + 50]}|")
for i, q in enumerate(w):
    if q['end'] > a and q['start'] < b: print(f"  w{i} {q['start']:.2f}-{q['end']:.2f} {q['text']}")
