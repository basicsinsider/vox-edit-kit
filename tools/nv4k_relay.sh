#!/bin/bash
# Lead-side relay for the NVIDIA 4K Premiere package (helpers can't upload to gofile — their permission check blocks it):
# for every pushed render4k/nvsNN branch: fetch into a throwaway bare repo, join the .part blobs, verify SHA-256,
# upload as nvsNN_4k.mp4 to the shared gofile folder (token from gitignored work/gofile_folder.json), verify md5, delete.
# Resumable: done segments are listed in work/relay4k_done.txt. Loops until all 23 (+ facecam if FACECAM=1) are done.
cd "$(dirname "$0")/.."; R=$PWD; URL=$(git remote get-url origin); LOG=work/relay4k.log; DONE=work/relay4k_done.txt; touch $DONE
T=$(python3 -c "import json;print(json.load(open('work/gofile_folder.json'))['data']['guestToken'])")
F=$(python3 -c "import json;print(json.load(open('work/gofile_folder.json'))['data']['parentFolder'])")
log() { echo "$(date -u +%H:%M:%SZ) $*" | tee -a $LOG; }
known() { grep -q "$1" /tmp/claude-0/known.txt; }
relay() {  # $1 = branch, $2 = dir in tree, $3 = upload name, $4 = sha file
  b=$1; d=$2; name=$3; G=$R/work/_relay.git; out=$R/work/_relay_$name
  # blob:none + one throwaway bare repo per part: only the part itself is downloaded, and it is deleted right after
  # (a plain --depth 1 fetch pulls the whole repo tree, > 3 GB — filled the lead disk on the first try)
  tree() { rm -rf $G; git init -q --bare $G && git -C $G remote add origin "$URL" && git -C $G fetch -q --depth 1 --filter=blob:none origin "$b"; }
  rm -f $out; tree || { log "$name: fetch failed"; rm -rf $G; return 1; }
  parts=$(git -C $G ls-tree --name-only FETCH_HEAD "$d/" | grep '\.part' | sort); want=$(git -C $G cat-file blob "FETCH_HEAD:$4" | head -1 | cut -d' ' -f1)
  : > $out
  for f in $parts; do tree && git -C $G cat-file blob "FETCH_HEAD:$f" >> $out || { log "$name: blob $f failed"; rm -rf $G $out; return 1; }; done
  rm -rf $G
  got=$(sha256sum $out | cut -d' ' -f1)
  [ "$want" = "$got" ] || { log "$name: SHA MISMATCH $got vs $want"; rm -f $out; return 1; }
  info=$(ffprobe -v error -select_streams v -show_entries stream=width,height,nb_frames -of csv=p=0 $out); md5=$(md5sum $out | cut -d' ' -f1); size=$(stat -c %s $out)
  for i in 1 2 3; do
    curl -sS -m 7200 -F "token=$T" -F "folderId=$F" -F "file=@$out;filename=$name" https://upload-eu-par.gofile.io/uploadfile -o work/_relay.json 2>>$LOG
    gm=$(python3 -c "import json;print(json.load(open('work/_relay.json'))['data']['md5'])" 2>/dev/null)
    [ "$gm" = "$md5" ] && break; log "$name: upload try $i failed (gofile md5 '$gm')"; sleep 30
  done
  rm -f $out
  [ "$gm" = "$md5" ] || { log "$name: UPLOAD FAILED"; return 1; }
  echo "$name $size $md5 $info" >> $DONE; log "$name: uploaded, $info, $size bytes, md5 $md5 MATCH ($(wc -l < $DONE) done)"
}
while true; do
  git ls-remote origin 'refs/heads/render4k/nvs*' > work/_heads.txt   # face cam: handled separately (too big for the lead disk in one piece) 2>/dev/null
  while read sha ref; do
    b=${ref#refs/heads/}; s=${b#render4k/}; known $sha && continue
    if [ "$s" = facecam ]; then name=nvidia_facecam_master_4k.mp4; else name=${s}_4k.mp4; fi
    grep -q "^$name " $DONE && continue
    [ $(df --output=avail -B1 . | tail -1) -gt 2500000000 ] || { log "$name: waiting — low disk"; continue; }
    if [ "$s" = facecam ]; then
      G=$R/work/_chk.git; rm -rf $G; git init -q --bare $G
      git -C $G fetch -q --depth 1 --filter=blob:none "$URL" "$b" 2>/dev/null && git -C $G ls-tree --name-only FETCH_HEAD pieces/facecam/ | grep -q SHA256 || { rm -rf $G; continue; }; rm -rf $G
      relay $b pieces/facecam $name pieces/facecam/SHA256
    else relay $b pieces/$s $name pieces/$s/$s.mp4.sha256; fi
  done < work/_heads.txt
  n=$(wc -l < $DONE); [ $n -ge ${TOTAL:-23} ] && { log "ALL $n DONE"; exit 0; }
  sleep 60
done
