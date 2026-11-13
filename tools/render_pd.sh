#!/bin/bash
# Render podcast compositions (pdNN) one by one at 30 fps and publish each as git-friendly parts (MANUAL §11/§11.1, podcast variant).
#   tools/render_pd.sh pd04 pd05 pd06          RES=4k PRESET=fast tools/render_pd.sh pd01   (3840x2160)
# Each composition is rendered alone from its own local 0 (tools/build_index.py pdNN), --fps 30, -w 3 -q draft --crf 18, then
# transcoded to x264 CRF 18 without audio and trimmed/padded to exactly round(DUR*30) frames (project/podcast/sections.json).
# Output: pieces/<id>/<id>.mp4.partNN + .sha256 — commit + push them. Finished pieces are skipped on re-run. Never kill a render.
set -e
export PATH=~/.local/bin:$PATH
R="$(cd "$(dirname "$0")/.." && pwd)"; cd "$R"
log(){ echo "$(date -u +%H:%M:%SZ) $*" | tee -a renders/render_pd.log; }
mkdir -p renders/pieces
[ -f assets/facecam/pd_facecam_intro.mp4 ] || { [ -f input/pd_join.sh ] && bash input/pd_join.sh || true; }
for s in "$@"; do
  [ -f "pieces/$s/$s.mp4.sha256" ] && { log "$s: already done, skipping"; continue; }
  N=$(python3 -c "import json;print(round([x for x in json.load(open('project/podcast/sections.json'))['sections'] if x['id']=='$s'][0]['dur']*30))")
  tools/make_sandbox.sh "r_$s" >/dev/null 2>&1 || true
  (cd "work/r_$s" && python3 tools/build_index.py "$s" --root . >/dev/null && sed -i 's/data-fps="24"/data-fps="30"/' index.html)
  (cd "work/r_$s" && npx --yes hyperframes@0.8.217 lint 2>&1 | grep -E "error\(s\)" | head -1) || true
  t0=$(date +%s); log "$s: render start ($N frames expected, $(nproc) cores, $(df -h . | awk 'NR==2{print $4}') free)"
  (cd "work/r_$s" && npx --yes hyperframes@0.8.217 render -w ${WORKERS:-3} -q draft --crf 18 --fps 30 ${RES:+--resolution $RES} -o "../../renders/pieces/$s.draft.mp4" > render.log 2>&1) || true
  [ -s "renders/pieces/$s.draft.mp4" ] || { log "$s: RENDER FAILED: $(tail -c 300 work/r_$s/render.log)"; continue; }
  t1=$(date +%s); G=$(ffprobe -v error -count_packets -select_streams v -show_entries stream=nb_read_packets -of csv=p=0 "renders/pieces/$s.draft.mp4")
  log "$s: rendered $G frames in $((t1-t0))s"
  ffmpeg -v error -y -i "renders/pieces/$s.draft.mp4" -vf "tpad=stop_mode=clone:stop=30,trim=end_frame=$N,setpts=N/30/TB" -r 30 -c:v libx264 -preset ${PRESET:-medium} -crf ${CRF:-18} -pix_fmt yuv420p -an -movflags +faststart "renders/pieces/$s.mp4"
  rm -f "renders/pieces/$s.draft.mp4"
  F=$(ffprobe -v error -count_packets -select_streams v -show_entries stream=nb_read_packets -of csv=p=0 "renders/pieces/$s.mp4")
  [ "$F" = "$N" ] || log "$s: WARNING frame count $F != $N"
  mkdir -p "pieces/$s"; (cd renders/pieces && sha256sum "$s.mp4") > "pieces/$s/$s.mp4.sha256"; echo "$F" > "pieces/$s/$s.frames"
  split -b 95m -d -a 2 "renders/pieces/$s.mp4" "pieces/$s/$s.mp4.part"
  log "$s: done, $F frames, $(du -h renders/pieces/$s.mp4 | cut -f1), total $(( $(date +%s)-t0 ))s"
done
