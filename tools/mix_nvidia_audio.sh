#!/bin/bash
# NVIDIA final AUDIO only (for the assembly): VO (project/nvidia/media/vo_nv.wav, lossless, unity — never processed, no bleeps
# in this script) + the sound designer's three beds (assets/audio/nvidia, built by place_sound; amix normalize=0)
# → project/nvidia/media/nv_final_audio.m4a (AAC 320k, 48 kHz stereo), exactly 2402.000 s = the picture master
# (the VO is 2400.617 s: padded with digital silence; the beds already run to 2402.0). Then a loudness report.
set -e
cd "$(dirname "$0")/.."
B=assets/audio/nvidia; VO=project/nvidia/media/vo_nv.wav; L=2402.000; OUT=project/nvidia/media/nv_final_audio.m4a
for f in $VO $B/music_bed.wav $B/sfx.wav $B/ambience.wav; do [ -f "$f" ] || { echo "missing $f"; exit 1; }; done
nice ffmpeg -v error -y -i $VO -i $B/music_bed.wav -i $B/sfx.wav -i $B/ambience.wav \
  -filter_complex "[0:a]aresample=48000,aformat=channel_layouts=stereo,apad=whole_dur=$L[vo];[1:a]aresample=48000[m];[2:a]aresample=48000[s];[3:a]aresample=48000[a];[vo][m][s][a]amix=inputs=4:normalize=0:duration=longest,atrim=duration=$L[mix]" \
  -map "[mix]" -t $L -c:a aac -b:a 320k -ar 48000 -movflags +faststart $OUT
for f in $VO $OUT; do echo "$f: $(ffmpeg -hide_banner -nostats -i "$f" -af ebur128=peak=true -f null - 2>&1 | grep -E '^\s+I:|^\s+Peak:' | tr -s ' ' | tr '\n' ' ')"; done
echo "duration: $(ffprobe -v error -show_entries format=duration -of csv=p=0 $OUT) s"
ls -la $OUT
