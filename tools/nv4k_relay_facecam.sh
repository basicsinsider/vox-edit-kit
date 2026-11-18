#!/bin/bash
# Relay the 4K face cam (render4k/facecam, pieces/facecam/*.partNNN + SHA256 with sha256 and md5 lines) to gofile WITHOUT a
# local copy (too big for the lead disk): parts are streamed blob by blob into curl (curl buffers stdin in RAM, so the file
# must fit in free memory), and gofile's md5 must equal the helper's md5. Usage: tools/nv4k_relay_facecam.sh
cd "$(dirname "$0")/.."; R=$PWD; URL=$(git remote get-url origin); G=$R/work/_fc.git; b=render4k/facecam; LOG=work/relay4k.log
T=$(python3 -c "import json;print(json.load(open('work/gofile_folder.json'))['data']['guestToken'])")
F=$(python3 -c "import json;print(json.load(open('work/gofile_folder.json'))['data']['parentFolder'])")
tree() { rm -rf $G; git init -q --bare $G && git -C $G remote add origin "$URL" && git -C $G fetch -q --depth 1 --filter=blob:none origin $b; }
tree || exit 1
parts=$(git -C $G ls-tree --name-only FETCH_HEAD pieces/facecam/ | grep '\.part' | sort)
git -C $G cat-file blob FETCH_HEAD:pieces/facecam/SHA256 > work/_fc_sums.txt; cat work/_fc_sums.txt
want_md5=$(awk 'length($1)==32{print $1}' work/_fc_sums.txt); want_sha=$(awk 'length($1)==64{print $1}' work/_fc_sums.txt)
echo "$(echo $parts | wc -w) parts"
for f in $parts; do tree >&2 && git -C $G cat-file blob "FETCH_HEAD:$f"; done \
  | tee >(sha256sum | cut -d' ' -f1 > work/_fc_sha.txt) \
  | curl -sS -m 10800 -F "token=$T" -F "folderId=$F" -F "file=@-;filename=nvidia_facecam_master_4k.mp4" https://upload-eu-par.gofile.io/uploadfile -o work/_fc.json
rm -rf $G; sleep 5
gm=$(python3 -c "import json;print(json.load(open('work/_fc.json'))['data']['md5'])" 2>/dev/null)
echo "stream sha256 $(cat work/_fc_sha.txt) (helper $want_sha) · gofile md5 $gm (helper $want_md5)"
if [ "$gm" = "$want_md5" ] && [ "$(cat work/_fc_sha.txt)" = "$want_sha" ]; then echo "$(date -u +%H:%M:%SZ) nvidia_facecam_master_4k.mp4: uploaded, md5 $gm MATCH" | tee -a $LOG
else echo "$(date -u +%H:%M:%SZ) nvidia_facecam_master_4k.mp4: UPLOAD FAILED / MISMATCH" | tee -a $LOG; exit 1; fi
