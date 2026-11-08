#!/bin/bash
# Paraguay final mix: VO (vo_py.wav, lossless, unity — only the 3 bleeped words muted, Krish's request in the take, DECISIONS #3)
# + the sound designer's three beds (the bleep tones live in sfx.wav) via amix normalize=0. Video stream-copied.
# Usage: tools/final_mix_paraguay.sh <picture.mp4> <out_dir> [name]      (name default py; review copy → review/<name>_720p.mp4)
set -e
cd "$(dirname "$0")/.."
P=$1; O=$2; N=${3:-py}; B=assets/audio/paraguay; L=1621.867
mkdir -p "$O" review
# mute exactly the bleeped words (master seconds = edited-VO seconds; 5 ms fades in/out, no gain change anywhere else)
.venv/bin/python - "$O/${N}_vo_bleeped.wav" <<'PY'
import sys, numpy as np, soundfile as sf
x, sr = sf.read('vo_py.wav', dtype='int16'); y = x.astype(np.float64); f = int(0.005 * sr)
for a, d in [(1104.58, 0.32), (1159.43, 0.16), (1600.60, 0.24)]:
    i, j = round(a * sr), round((a + d) * sr)
    g = np.ones(j - i + 2 * f); g[:f] = np.linspace(1, 0, f); g[f:-f] = 0; g[-f:] = np.linspace(0, 1, f)
    y[i - f:j + f] *= g[:, None]
sf.write(sys.argv[1], np.round(y).astype(np.int16), sr, subtype='PCM_16')
d = (y != x).any(1); print('VO samples changed:', int(d.sum()), '=', round(d.sum() / sr, 3), 's (bleep windows only)')
PY
ffmpeg -v error -y -i "$O/${N}_vo_bleeped.wav" -i $B/music_bed.wav -i $B/sfx.wav -i $B/ambience.wav \
  -filter_complex "[0:a]aresample=48000,aformat=channel_layouts=stereo[vo];[1:a]aresample=48000[m];[2:a]aresample=48000[s];[3:a]aresample=48000[a];[vo][m][s][a]amix=inputs=4:normalize=0:duration=first[mix]" \
  -map "[mix]" -t $L -c:a pcm_s24le "$O/${N}_mix.wav"
rm -f "$O/${N}_vo_bleeped.wav"
ffmpeg -v error -y -i "$P" -i "$O/${N}_mix.wav" -map 0:v -map 1:a -c:v copy -c:a aac -b:a 384k -shortest -movflags +faststart "$O/${N}_final.mp4"
rm -f "$O/${N}_mix.wav"
ffmpeg -v error -y -i "$O/${N}_final.mp4" -vf scale=1280:720:flags=lanczos -c:v libx264 -preset medium -crf 23 -maxrate 2500k -bufsize 5000k \
  -c:a aac -b:a 160k -movflags +faststart "review/${N}_720p.mp4"
for f in vo_py.wav "$O/${N}_final.mp4"; do echo "$f: $(ffmpeg -hide_banner -nostats -i "$f" -af ebur128=peak=true -f null - 2>&1 | grep -E '^\s+I:|^\s+Peak:' | tr -s ' ' | tr '\n' ' ')"; done
ls -la "$O/${N}_final.mp4" "review/${N}_720p.mp4"
