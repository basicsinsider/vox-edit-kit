#!/bin/bash
# US vs Cartels final AUDIO only (for the assembly): VO (project/cartels/media/vo_ct.wav, lossless, unity — never processed, no bleeps
# in this script) + the sound designer's three beds (assets/audio/cartels, built by place_sound; amix normalize=0)
# → project/cartels/media/ct_final_audio.m4a (AAC 320k, 48 kHz stereo), exactly 1341.917 s (32206 frames) = the picture master
# (the VO is 1341.912 s: padded with digital silence). Then a loudness report.
set -e
cd "$(dirname "$0")/.."
B=assets/audio/cartels; VO=project/cartels/media/vo_ct.wav; L=1341.917; OUT=project/cartels/media/ct_final_audio.m4a
for f in $VO $B/music_bed.wav $B/sfx.wav $B/ambience.wav; do [ -f "$f" ] || { echo "missing $f"; exit 1; }; done
nice ffmpeg -v error -y -i $VO -i $B/music_bed.wav -i $B/sfx.wav -i $B/ambience.wav \
  -filter_complex "[0:a]aresample=48000,pan=stereo|c0=c0|c1=c0,apad=whole_dur=$L[vo];[1:a]aresample=48000[m];[2:a]aresample=48000[s];[3:a]aresample=48000[a];[vo][m][s][a]amix=inputs=4:normalize=0:duration=longest,atrim=duration=$L[mix]" \
  -map "[mix]" -t $L -c:a aac -b:a 320k -ar 48000 -movflags +faststart $OUT
for f in $VO $OUT; do echo "$f: $(ffmpeg -hide_banner -nostats -i "$f" -af ebur128=peak=true -f null - 2>&1 | grep -E '^\s+I:|^\s+Peak:' | tr -s ' ' | tr '\n' ' ')"; done
echo "duration: $(ffprobe -v error -show_entries format=duration -of csv=p=0 $OUT) s"
ls -la $OUT
