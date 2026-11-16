"""10 ms RMS (dBFS) of the combined raw audio between A and B (global s) — to place a cut by hand. usage: fine.py A B"""
import sys, numpy as np, soundfile as sf
a, b = float(sys.argv[1]), float(sys.argv[2]); x, sr = sf.read('project/nvidia/media/raw_audio.wav', start=int(a*48000), stop=int(b*48000)); m = x.mean(1)
h = int(0.01*sr); n = len(m)//h
d = 20*np.log10(np.sqrt((m[:n*h].reshape(n,h)**2).mean(1))+1e-9)
print(' '.join(f"{a+k*0.01:.2f}:{v:.0f}" for k, v in enumerate(d)))
