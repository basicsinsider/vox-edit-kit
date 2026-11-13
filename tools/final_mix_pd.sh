#!/bin/bash
# Final mix for the podcast (BRIEF rule 4 / MANUAL §10.8 "Music limits"): the cut voice stays EXACTLY as recorded —
# project/podcast/media/vo_pd.wav (44.1 kHz mono, cut only) duplicated to L = R at unity, like the camera's dual-mono —
# and the island pre-mix (music + SFX + ambience, already ducked and measured) is resampled to 44.1 kHz and added with
# amix normalize=0. No gain, EQ, compression or limiting on anything that touches the voice.
#   tools/final_mix_pd.sh [beds.flac] [out.m4a]
set -e; cd "$(dirname "$0")/.."
BEDS=${1:-assets/audio/podcast/pd_beds_mix.flac}; OUT=${2:-renders/pd_mix.m4a}
VO=project/podcast/media/vo_pd.wav
ffmpeg -v error -y -i "$VO" -i "$BEDS" -filter_complex \
 "[0:a]pan=stereo|c0=c0|c1=c0[v];[1:a]aresample=44100:resampler=soxr,aformat=channel_layouts=stereo[b];[v][b]amix=inputs=2:normalize=0:duration=first:dropout_transition=0[m]" \
 -map "[m]" -c:a aac -b:a 320k "$OUT"
echo "mix: $OUT"
ffmpeg -v error -i "$VO" -filter_complex "pan=stereo|c0=c0|c1=c0,ebur128=peak=true" -f null - 2>&1 | true
for f in "$VO" "$OUT"; do printf '%s  ' "$f"; ffmpeg -nostats -i "$f" -filter_complex "$( [ "$f" = "$VO" ] && echo 'pan=stereo|c0=c0|c1=c0,' )ebur128=peak=true" -f null - 2>&1 | grep -E "^\s+(I:|Peak:)" | tr -s ' ' | tr '\n' ' '; echo; done
