#!/bin/bash
# assemble_chunk.sh <chunk> <len_s> : 3 pieces in renders/<chunk>/pieces → picture → final mix → review copies → delivery.
# Disk-careful: checks free space before each step and deletes each intermediate as soon as it is used. One chunk at a time.
set -e
n=$1; L=$2; R="$(cd "$(dirname "$0")/.." && pwd)"; cd "$R"; P=renders/$n/pieces
log(){ echo "$(date -u +%Y-%m-%dT%H:%MZ) $*" | tee -a renders/render_log.txt; }
need(){ local avail=$(df --output=avail -B1 . | tail -1); [ $avail -gt $1 ] || { log "$n: NOT ENOUGH DISK (need $1, have $avail) before $2"; exit 1; }; }
segs=$(grep -o "id=\"${n}s[0-9][0-9]-host\"" work/qa${n#c}/index.html | cut -d'"' -f2 | sed 's/-host//')
for s in $segs; do [ -s $P/$s.mp4 ] || { log "$n: missing piece $s"; exit 1; }; done
sz=$(du -cb $P/${n}s[0-9][0-9].mp4 | tail -1 | cut -f1)
need $((sz + 300000000)) concat
for s in $segs; do echo "file '$R/$P/$s.mp4'"; done > $P/list.txt
ffmpeg -v error -y -f concat -safe 0 -i $P/list.txt -c copy renders/$n/${n}_picture.mp4
d=$(ffprobe -v error -show_entries format=duration -of csv=p=0 renders/$n/${n}_picture.mp4); log "$n: picture ${d}s (VO $L s)"
rm -rf $P
need $((sz + 300000000)) mix
tools/final_mix.sh $n vo_$n.mp3 $L assets/audio/$n renders/$n/${n}_picture.mp4 renders/$n 2>&1 | tee -a renders/render_log.txt
rm -f renders/$n/${n}_picture.mp4; log "$n: mixed"
need 400000000 deliver
tools/deliver.sh $n 2>&1 | tail -3 | tee -a renders/render_log.txt
log "$n: assembled + delivered"
