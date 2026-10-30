#!/bin/bash
# Side-by-side check of a rebuilt sample against the approved one: N frames of A (top row) over B (bottom row).
# Usage: tools/compare_expected.sh renders/samples/s03-gdp.mp4 expected/s03-gdp.720p.mp4 out.jpg [N=7]
A=$1; B=$2; O=$3; N=${4:-7}
d=$(mktemp -d)
for v in A B; do f=${!v}; dur=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$f")
  for i in $(seq 0 $((N-1))); do t=$(python3 -c "print(round(($i+0.5)*$dur/$N,2))")
    ffmpeg -v error -ss $t -i "$f" -frames:v 1 -vf "scale=400:-1,drawtext=text='$v $t':fontcolor=yellow:fontsize=14:x=4:y=4" -y $d/$v-$i.png; done; done
montage $d/A-*.png $d/B-*.png -tile ${N}x2 -geometry +2+2 -background '#222' "$O"; rm -r $d
