#!/bin/bash
# final 4K: fetch each render4k/<seg> into a throwaway bare repo in /dev/shm, join + sha256-check the piece, make its v2 part, delete the piece
cd /home/user/vox-edit-kit
URL=$(git remote get-url origin); P=/dev/shm/ct4k; T=/dev/shm/ct4k_parts; mkdir -p $P $T
log(){ echo "$(date -u +%H:%M:%SZ) $*"; }
ASM=".venv/bin/python tools/ct_fix_assemble.py --pieces $P --tmp $T --preset faster --crf 19 --replace /dev/shm/r3d/R1_v1.mp4:762 --replace /dev/shm/r3d/R4_v1.mp4:2810"
todo="cts01 cts02 cts03 cts04 cts05 cts06 cts07 cts08 cts09 cts10 cts11 cts12 cts13 cts14"
while [ -n "$todo" ]; do
  progressed=0
  for s in $todo; do
    [ -s "$T/$s.ts" ] && [ -f "$T/$s.ok" ] && { todo=$(echo $todo | sed "s/\b$s\b//"); continue; }
    git ls-remote --exit-code "$URL" "refs/heads/render4k/$s" >/dev/null 2>&1 || continue
    G=/dev/shm/g_$s; rm -rf $G; git init -q --bare $G
    git --git-dir=$G fetch -q --depth 1 "$URL" "refs/heads/render4k/$s" || { log "$s fetch failed"; rm -rf $G; continue; }
    parts=$(git --git-dir=$G ls-tree --name-only FETCH_HEAD "pieces/$s/" | grep "\.part" | sort)
    : > $P/$s.mp4; for f in $parts; do git --git-dir=$G cat-file -p "FETCH_HEAD:$f" >> $P/$s.mp4; done
    want=$(git --git-dir=$G cat-file -p "FETCH_HEAD:pieces/$s/$s.mp4.sha256" | cut -d' ' -f1); rm -rf $G
    got=$(sha256sum $P/$s.mp4 | cut -d' ' -f1)
    [ "$want" = "$got" ] || { log "$s SHA MISMATCH ($want vs $got)"; rm -f $P/$s.mp4; continue; }
    log "$s fetched ($(du -h $P/$s.mp4 | cut -f1), sha OK, $(ffprobe -v error -select_streams v -show_entries stream=width,height,nb_frames -of csv=p=0 $P/$s.mp4))"
    nice $ASM --only $s 2>&1 | tail -1 && touch $T/$s.ok && rm -f $P/$s.mp4
    log "$s part done; shm free $(df -h /dev/shm | awk 'NR==2{print $4}')"; progressed=1
    todo=$(echo $todo | sed "s/\b$s\b//")
  done
  [ -n "$(echo $todo | tr -d ' ')" ] || break
  [ $progressed = 0 ] && sleep 60
done
log "ALL PARTS DONE"
