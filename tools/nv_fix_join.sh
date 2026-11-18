#!/bin/bash
# NVIDIA review fix — lead-side final join: the 23 MPEG-TS pieces (pieces/fix/<SEG>.ts.part* locally, or from the helpers' branches
# render4k/fix-g1..g3 via a blob:none fetch, streamed blob by blob) are joined byte by byte (their timestamps are already on the new
# timeline), checked against each piece's sha256, and muxed with project/nvidia/media/nv_final_audio_v2.m4a → $OUT (MP4, faststart).
# Usage: tools/nv_fix_join.sh /dev/shm/NVIDIA_chip_ban_4K.mp4
set -e; cd "$(dirname "$0")/.."; OUT=$1; URL=$(git remote get-url origin)
SEGS=$(python3 -c "import json;print(' '.join(s['seg'] for s in json.load(open('project/nvidia/segments.json'))['segments']))")
G=/dev/shm/_join.git; rm -rf $G; git init -q --bare $G; git -C $G remote add origin "$URL"
for g in g1 g2 g3; do git -C $G fetch -q --depth 1 --filter=blob:none origin render4k/fix-$g:refs/heads/fix-$g; done
piece() {  # $1 = SEG → its TS bytes on stdout
  if [ -e pieces/fix/$1.ts.part000 ]; then cat pieces/fix/$1.ts.part*
  else  # one throwaway repo per segment in RAM (lazy blob fetches land there, not on the small root disk), removed after
    B=$(branch $1); P=/dev/shm/_jp.git; rm -rf $P; git init -q --bare $P; git -C $P remote add origin "$URL"
    git -C $P fetch -q --depth 1 --filter=blob:none origin render4k/$B:refs/heads/$B
    for o in $(git -C $P ls-tree $B pieces/fix/ | grep "$1.ts.part" | awk '{print $3}'); do git -C $P cat-file blob $o; done
    rm -rf $P; fi; }
branch() { for g in g1 g2 g3; do git -C $G ls-tree --name-only fix-$g pieces/fix/ | grep -q "/$1.sha256" && { echo fix-$g; return; }; done; }
want() { if [ -e pieces/fix/$1.sha256 ]; then head -1 pieces/fix/$1.sha256; else git -C $G show $(branch $1):pieces/fix/$1.sha256 | head -1; fi | cut -d' ' -f1; }
for s in $SEGS; do [ -e pieces/fix/$s.sha256 ] || [ -n "$(branch $s)" ] || { echo "MISSING $s"; exit 1; }; done
echo "all 23 pieces present"
for s in $SEGS; do piece $s | tee >(sha256sum | cut -d' ' -f1 > /tmp/_sha_$s); done \
  | ffmpeg -v error -y -f mpegts -i pipe:0 -i project/nvidia/media/nv_final_audio_v2.m4a -map 0:v -map 1:a -c copy -movflags +faststart "$OUT"
sleep 5; bad=0
for s in $SEGS; do [ "$(cat /tmp/_sha_$s)" = "$(want $s)" ] && echo "$s sha256 OK" || { echo "$s sha256 MISMATCH"; bad=1; }; done
rm -rf $G; [ $bad = 0 ] || exit 1
ffprobe -v error -show_entries stream=codec_type,width,height,r_frame_rate,nb_frames,duration:format=duration,size -of compact "$OUT"
# A/V sync guard: video pts must be exactly 0, 1/24, 2/24 … (no duplicates, no gaps, first = 0) — the audio starts at 0
ffprobe -v error -select_streams v -show_entries packet=pts_time -of csv=p=0 "$OUT" | sort -n | awk '{if(NR==1&&$1!=0)b++; if(NR>1){d=$1-p; if(d<0.0415||d>0.0418)b++}; p=$1} END{print "pts check: packets",NR,"first..last ok =",(b==0?"YES":"NO, "b" bad"),"last",p; exit b>0}'
md5sum "$OUT"
