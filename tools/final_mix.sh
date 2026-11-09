#!/bin/bash
# Final mix for one chunk: VO untouched at unity + the three pre-mixed beds (amix normalize=0), video stream-copied.
# Usage: tools/final_mix.sh <name> <vo.mp3> <len_s> <beds_dir> <picture.mp4> <out_dir>
#   e.g. tools/final_mix.sh c4 vo_c4.mp3 601.44 assets/audio/c4 renders/c4/c4_picture.mp4 renders/c4
# Writes <out_dir>/<name>_final.mp4 and review/<name>_720p.mp4 (≤ ~90 MB so it fits in git), prints loudness of VO vs mix.
set -e
cd "$(dirname "$0")/.."
N=$1; VO=$2; L=$3; B=$4; P=$5; O=$6
VOICE_CHANNELS=$(ffprobe -v error -select_streams a:0 -show_entries stream=channels -of csv=p=0 "$VO")
if [ "$VOICE_CHANNELS" = "1" ]; then
  # Keep mono dialogue at unity; downmix only the stereo beds to the source layout.
  MIX_FILTER='[1:a]aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=mono[vo];[2:a]pan=mono|c0=0.5*c0+0.5*c1[m];[3:a]pan=mono|c0=0.5*c0+0.5*c1[s];[4:a]pan=mono|c0=0.5*c0+0.5*c1[a];[vo][m][s][a]amix=inputs=4:normalize=0:duration=first[mix]'
else
  MIX_FILTER='[1:a]aresample=48000,aformat=channel_layouts=stereo[vo];[2:a]aresample=48000[m];[3:a]aresample=48000[s];[4:a]aresample=48000[a];[vo][m][s][a]amix=inputs=4:normalize=0:duration=first[mix]'
fi
ffmpeg -v error -y -i "$P" -i "$VO" -i "$B/music_bed.wav" -i "$B/sfx.wav" -i "$B/ambience.wav" \
  -filter_complex "$MIX_FILTER" \
  -map 0:v -map "[mix]" -c:v copy -c:a aac -b:a 320k -t "$L" -movflags +faststart "$O/${N}_final.mp4"
# review copy: bitrate capped so a 10-min chunk stays under ~90 MB
ffmpeg -v error -y -i "$O/${N}_final.mp4" -vf scale=1280:720 -c:v libx264 -preset medium -crf 24 -maxrate 1000k -bufsize 2000k \
  -c:a aac -b:a 128k -movflags +faststart "review/${N}_720p.mp4"
for f in "$VO" "$O/${N}_final.mp4"; do echo "$f: $(ffmpeg -hide_banner -nostats -i "$f" -af ebur128=peak=true -f null - 2>&1 | grep -E '^\s+I:|^\s+Peak:' | tr -s ' ' | tr '\n' ' ')"; done
ls -la "$O/${N}_final.mp4" "review/${N}_720p.mp4"
