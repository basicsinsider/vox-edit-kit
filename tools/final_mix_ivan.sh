#!/bin/bash
# Ivan final mix: VO (vo_ivan_master.wav, lossless, untouched, unity) + the script-note insert clips' own audio at their slots
# + the sound designer's three beds (amix normalize=0). Video stream-copied.
# Usage: tools/final_mix_ivan.sh <picture.mp4> <out_dir>    (insert gains in dB via env G1 G2 G3, default 0)
set -e
cd "$(dirname "$0")/.."
P=$1; O=$2; B=assets/audio/ivan; L=949.0; N=iv
G1=${G1:-0}; G2=${G2:-0}; G3=${G3:-0}
ffmpeg -v error -y -i "$P" -i vo_ivan_master.wav -i $B/music_bed.wav -i $B/sfx.wav -i $B/ambience.wav \
  -i $B/insert1.wav -i $B/insert2.wav -i $B/insert3.wav \
  -filter_complex "[1:a]aresample=48000,aformat=channel_layouts=stereo[vo];[2:a]aresample=48000[m];[3:a]aresample=48000[s];[4:a]aresample=48000[a];\
[5:a]aresample=48000,aformat=channel_layouts=stereo,volume=${G1}dB,adelay=108700:all=1[i1];\
[6:a]aresample=48000,aformat=channel_layouts=stereo,volume=${G2}dB,adelay=407900:all=1[i2];\
[7:a]aresample=48000,aformat=channel_layouts=stereo,volume=${G3}dB,adelay=532917:all=1[i3];\
[vo][m][s][a][i1][i2][i3]amix=inputs=7:normalize=0:duration=first[mix]" \
  -map 0:v -map "[mix]" -c:v copy -c:a aac -b:a 320k -t "$L" -movflags +faststart "$O/${N}_final.mp4"
ffmpeg -v error -y -i "$O/${N}_final.mp4" -vf scale=1280:720 -c:v libx264 -preset medium -crf 24 -maxrate 1100k -bufsize 2200k \
  -c:a aac -b:a 128k -movflags +faststart "review/ivan_720p.mp4"
for f in vo_ivan_master.wav "$O/${N}_final.mp4"; do echo "$f: $(ffmpeg -hide_banner -nostats -i "$f" -af ebur128=peak=true -f null - 2>&1 | grep -E '^\s+I:|^\s+Peak:' | tr -s ' ' | tr '\n' ' ')"; done
ls -la "$O/${N}_final.mp4" review/ivan_720p.mp4
