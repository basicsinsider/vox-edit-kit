#!/bin/bash
# Paraguay final AUDIO only (for the 4K assembly on a helper): VO (vo_py.wav, unity, only the 3 bleep words muted — Krish's request)
# + the 3 beds (amix normalize=0) → assets/audio/paraguay/py_mix_final.m4a (AAC 384k, 48 kHz) + loudness report.
set -e
cd "$(dirname "$0")/.."
B=assets/audio/paraguay; L=1621.867; T=renders/py; mkdir -p $T
.venv/bin/python - "$T/vo_bleeped.wav" <<'PY'
import sys, numpy as np, soundfile as sf
x, sr = sf.read('vo_py.wav', dtype='int16'); y = x.astype(np.float64); f = int(0.005 * sr)
for a, d in [(1104.58, 0.32), (1159.43, 0.16), (1600.60, 0.24)]:
    i, j = round(a * sr), round((a + d) * sr)
    g = np.ones(j - i + 2 * f); g[:f] = np.linspace(1, 0, f); g[f:-f] = 0; g[-f:] = np.linspace(0, 1, f)
    y[i - f:j + f] *= g[:, None]
sf.write(sys.argv[1], np.round(y).astype(np.int16), sr, subtype='PCM_16')
d = (y != x).any(1); print('VO samples changed:', int(d.sum()), '=', round(d.sum() / sr, 3), 's (bleep windows only)')
PY
ffmpeg -v error -y -i $T/vo_bleeped.wav -i $B/music_bed.wav -i $B/sfx.wav -i $B/ambience.wav \
  -filter_complex "[0:a]aresample=48000,aformat=channel_layouts=stereo[vo];[1:a]aresample=48000[m];[2:a]aresample=48000[s];[3:a]aresample=48000[a];[vo][m][s][a]amix=inputs=4:normalize=0:duration=first[mix]" \
  -map "[mix]" -t $L -c:a aac -b:a 384k -ar 48000 $B/py_mix_final.m4a
rm -f $T/vo_bleeped.wav
for f in vo_py.wav $B/py_mix_final.m4a; do echo "$f: $(ffmpeg -hide_banner -nostats -i "$f" -af ebur128=peak=true -f null - 2>&1 | grep -E '^\s+I:|^\s+Peak:' | tr -s ' ' | tr '\n' ' ')"; done
ls -la $B/py_mix_final.m4a
