#!/bin/bash
# zip → new gofile folder; then cts00…cts14 4K segments into the same folder (fetched one at a time, blob-less), md5 checked each
cd /home/user/vox-edit-kit; log(){ echo "$(date -u +%H:%M:%SZ) $*"; }
up(){ # file name [token folder] → json in /dev/shm/up.json ; returns md5 compare
  for i in 1 2 3; do
    if [ -n "$3" ]; then curl -sS -m 10800 -F "token=$3" -F "folderId=$4" -F "file=@$1;filename=$2" https://upload-eu-par.gofile.io/uploadfile -o /dev/shm/up.json
    else curl -sS -m 10800 -F "file=@$1;filename=$2" https://upload-eu-par.gofile.io/uploadfile -o /dev/shm/up.json; fi
    grep -q '"ok"' /dev/shm/up.json && break; sleep 30
  done
  local m=$(md5sum "$1" | cut -d' ' -f1); local r=$(python3 -c "import json;print(json.load(open('/dev/shm/up.json'))['data']['md5'])")
  [ "$m" = "$r" ] && log "$2 uploaded, md5 $m MATCH" || log "$2 md5 MISMATCH local $m gofile $r"
}
up /dev/shm/US_vs_Cartels_Premiere_FINAL.zip US_vs_Cartels_Premiere_FINAL.zip
cp /dev/shm/up.json work/gofile_premiere_final.json
TOK=$(python3 -c "import json;print(json.load(open('work/gofile_premiere_final.json'))['data']['guestToken'])")
FOL=$(python3 -c "import json;print(json.load(open('work/gofile_premiere_final.json'))['data']['parentFolder'])")
log "folder $(python3 -c "import json;print(json.load(open('work/gofile_premiere_final.json'))['data']['downloadPage'])")"
rm -f /dev/shm/US_vs_Cartels_Premiere_FINAL.zip
up /dev/shm/ct4k/cts00.mp4 cts00_4k.mp4 "$TOK" "$FOL"
URL=$(git remote get-url origin)
for n in 01 02 03 04 05 06 07 08 09 10 11 12 13 14; do s=cts$n; G=/dev/shm/g_$s; P=/dev/shm/ct4k/$s.mp4
  rm -rf $G; git clone -q --bare --depth 1 --filter=blob:none --branch render4k/$s "$URL" $G || { log "$s clone failed"; continue; }
  : > $P; for f in $(git --git-dir=$G ls-tree --name-only HEAD pieces/$s/ | grep '\.part' | sort); do git --git-dir=$G cat-file -p HEAD:$f >> $P; done
  want=$(git --git-dir=$G cat-file -p HEAD:pieces/$s/$s.mp4.sha256 | cut -d' ' -f1); rm -rf $G
  [ "$(sha256sum $P | cut -d' ' -f1)" = "$want" ] || { log "$s SHA MISMATCH"; rm -f $P; continue; }
  up $P ${s}_4k.mp4 "$TOK" "$FOL"; rm -f $P
done
log ALL UPLOADS DONE
