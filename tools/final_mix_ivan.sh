#!/bin/bash
# Ivan final mix: VO (vo_ivan_master.wav, lossless, untouched, unity) + the script-note insert clips' own audio at their slots
# + the sound designer's three beds (amix normalize=0). Video stream-copied.
# Usage: tools/final_mix_ivan.sh <picture.mp4> <out_dir>
#   env G1 G2 G3 = insert gains in dB (default 0; sound designer measured: G1=-22.5 G2=-12 G3=-24.5)
#   env CUT="a:b"  = remove master seconds [a,b) from the AUDIO (the picture must already have the same frames removed);
#                    joins use 15 ms fades on both sides (no overlap, so A/V stay locked). Used for the 1:18 dead-air removal.
set -e
cd "$(dirname "$0")/.."
P=$1; O=$2; B=assets/audio/ivan; L=949.0; N=iv
G1=${G1:-0}; G2=${G2:-0}; G3=${G3:-0}
ffmpeg -v error -y -i vo_ivan_master.wav -i $B/music_bed.wav -i $B/sfx.wav -i $B/ambience.wav \
  -i $B/insert1.wav -i $B/insert2.wav -i $B/insert3.wav \
  -filter_complex "[0:a]aresample=48000,aformat=channel_layouts=stereo[vo];[1:a]aresample=48000[m];[2:a]aresample=48000[s];[3:a]aresample=48000[a];\
[4:a]aresample=48000,aformat=channel_layouts=stereo,volume=${G1}dB,adelay=108700:all=1[i1];\
[5:a]aresample=48000,aformat=channel_layouts=stereo,volume=${G2}dB,adelay=407900:all=1[i2];\
[6:a]aresample=48000,aformat=channel_layouts=stereo,volume=${G3}dB,adelay=532917:all=1[i3];\
[vo][m][s][a][i1][i2][i3]amix=inputs=7:normalize=0:duration=first[mix]" \
  -map "[mix]" -t $L -c:a pcm_s24le $O/${N}_mix.wav
if [ -n "$CUT" ]; then
  .venv/bin/python - "$O/${N}_mix.wav" "$CUT" <<'PY'
import sys, numpy as np, soundfile as sf
f, cut = sys.argv[1], sys.argv[2]; a, b = map(float, cut.split(':'))
x, sr = sf.read(f, dtype='float64'); i, j = round(a * sr), round(b * sr); n = int(0.015 * sr)
A, Bq = x[:i].copy(), x[j:].copy(); A[-n:] *= np.linspace(1, 0, n)[:, None]; Bq[:n] *= np.linspace(0, 1, n)[:, None]
sf.write(f, np.concatenate([A, Bq]), sr, subtype='PCM_24'); print('audio cut', a, b, '->', (len(A) + len(Bq)) / sr, 's')
PY
fi
ffmpeg -v error -y -i "$P" -i $O/${N}_mix.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 320k -shortest -movflags +faststart "$O/${N}_final.mp4"
rm -f $O/${N}_mix.wav
ffmpeg -v error -y -i "$O/${N}_final.mp4" -vf scale=1280:720 -c:v libx264 -preset medium -crf 26 -maxrate 640k -bufsize 1280k \
  -c:a aac -b:a 96k -movflags +faststart "review/ivan_720p.mp4"
for f in vo_ivan_master.wav "$O/${N}_final.mp4"; do echo "$f: $(ffmpeg -hide_banner -nostats -i "$f" -af ebur128=peak=true -f null - 2>&1 | grep -E '^\s+I:|^\s+Peak:' | tr -s ' ' | tr '\n' ' ')"; done
ls -la "$O/${N}_final.mp4" review/ivan_720p.mp4
