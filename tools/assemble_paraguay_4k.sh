#!/bin/bash
# Run on a fresh helper session with a big disk: collect the 13 4K pieces (branches render4k/pys*), join them on the 24 fps master
# grid (tools/assemble_paraguay.py), mux the final mix (assets/audio/paraguay/py_mix_final.m4a — VO untouched except the 3 bleeps,
# made by the lead with tools/final_mix_paraguay.sh's mix), verify, upload to gofile.io (md5 in the reply must match); DELIVER_GIT=1 also pushes 95 MB parts to deliveries/paraguay.
set -e
cd "$(dirname "$0")/.."
export PATH=~/.local/bin:$PATH
log(){ echo "$(date -u +%H:%M:%SZ) $*"; }
df -h . | tail -1
BRANCH_PREFIX=render4k ONLY=pys tools/collect_pieces.sh
n=$(ls renders/py/pieces/pys*.mp4 | grep -v fixed | wc -l); [ "$n" = 13 ] || { log "only $n of 13 pieces"; exit 1; }
for p in renders/py/pieces/pys??.mp4; do ffprobe -v error -select_streams v -show_entries stream=width,height -of csv=p=0 "$p" | grep -q 3840,2160 || { log "$p is not 4K"; exit 1; }; done
python3 tools/assemble_paraguay.py renders/py/pieces renders/py/py_4k_picture.mp4
rm -rf renders/py/pieces
ffmpeg -v error -y -i renders/py/py_4k_picture.mp4 -i assets/audio/paraguay/py_mix_final.m4a -map 0:v -map 1:a -c copy -movflags +faststart renders/py/paraguay_final.mp4
rm -f renders/py/py_4k_picture.mp4
ffprobe -v error -show_entries format=duration:stream=codec_name,width,height,nb_frames -of compact renders/py/paraguay_final.mp4
ls -la renders/py/paraguay_final.mp4; df -h . | tail -1
sha256sum renders/py/paraguay_final.mp4; md5sum renders/py/paraguay_final.mp4
log "upload to gofile (Krish: deliver as a gofile.io link)"
for i in 1 2 3; do
  curl -sS -m 7200 -F "file=@renders/py/paraguay_final.mp4;filename=Paraguay_4K_final.mp4" https://upload-eu-par.gofile.io/uploadfile -o gofile_4k.json -w "HTTP %{http_code} up %{size_upload}B in %{time_total}s\n" && grep -q '"status":"ok"' gofile_4k.json && break
  log "upload attempt $i failed: $(head -c 300 gofile_4k.json 2>/dev/null)"; sleep $((10*i))
done
cat gofile_4k.json; echo
[ -n "$DELIVER_GIT" ] && tools/deliver_chunked.sh renders/py/paraguay_final.mp4 paraguay 14 || true
