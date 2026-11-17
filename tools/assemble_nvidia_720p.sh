#!/bin/bash
# Run on a FRESH helper session (the lead's disk can't hold the master): collect the 23 1080p pieces (branches render/nvs*),
# join them frame-exact on the 24 fps grid (tools/assemble_nvidia.py), mux the lead's final mix (project/nvidia/media_git/nv_final_audio.m4a:
# VO untouched at unity + music/SFX/ambience beds), make the 720p review copy, verify, upload to gofile.io (md5 in the reply must match).
set -e
cd "$(dirname "$0")/.."
export PATH=~/.local/bin:$PATH
log(){ echo "$(date -u +%H:%M:%SZ) $*"; }
A=project/nvidia/media_git/nv_final_audio.m4a; [ -s "$A" ] || { log "missing $A"; exit 1; }
df -h . | tail -1
BRANCH_PREFIX=render ONLY=nvs tools/collect_pieces.sh
n=$(ls renders/nv/pieces/nvs*.mp4 | grep -v fixed | wc -l); [ "$n" = 23 ] || { log "only $n of 23 pieces"; exit 1; }
for p in renders/nv/pieces/nvs??.mp4; do ffprobe -v error -select_streams v -show_entries stream=width,height -of csv=p=0 "$p" | grep -q 1920,1080 || { log "$p is not 1080p"; exit 1; }; done
python3 tools/assemble_nvidia.py renders/nv/pieces renders/nv/nv_picture.mp4
rm -rf renders/nv/pieces
ffmpeg -v error -y -i renders/nv/nv_picture.mp4 -i "$A" -map 0:v -map 1:a -c copy -shortest -movflags +faststart renders/nv/nvidia_1080p.mp4
ffmpeg -v error -y -i renders/nv/nvidia_1080p.mp4 -vf scale=1280:720:flags=lanczos -c:v libx264 -preset medium -crf 20 -pix_fmt yuv420p -c:a copy -movflags +faststart renders/nv/NVIDIA_chip_ban_720p_review.mp4
ffprobe -v error -show_entries format=duration:stream=codec_name,width,height,nb_frames -of compact renders/nv/NVIDIA_chip_ban_720p_review.mp4
F=renders/nv/NVIDIA_chip_ban_720p_review.mp4; ls -la $F; df -h . | tail -1
md5sum $F; sha256sum $F
log "upload to gofile"
for i in 1 2 3; do
  curl -sS -m 7200 -F "file=@$F;filename=NVIDIA_chip_ban_720p_review.mp4" https://upload-eu-par.gofile.io/uploadfile -o gofile_720p.json -w "HTTP %{http_code} up %{size_upload}B in %{time_total}s\n" && grep -q '"status":"ok"' gofile_720p.json && break
  log "upload attempt $i failed: $(head -c 300 gofile_720p.json 2>/dev/null)"; sleep $((10*i))
done
cat gofile_720p.json; echo
