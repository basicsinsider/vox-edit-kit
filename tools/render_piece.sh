#!/bin/bash
# Render ONE segment of a chunk on a helper cloud session and publish it as git-friendly parts (MANUAL §11, option C).
#   tools/render_piece.sh <chunk> <len_s> <segment>      e.g. tools/render_piece.sh c4 601.44 c4s01
#   DRY=1 tools/render_piece.sh …   → prepare everything, skip the render (setup test)
#   DROP="1872-1951,2349-2356" → remove those LOCAL frames [a,b) in the transcode (word/dead-air cuts; audio is cut to match by final_mix_ivan.sh CUT)
#   SCALE=720 tools/render_piece.sh …  → render 1080p, transcode the piece to 1280×720 (lanczos) — smaller pieces for 720p deliveries
#   RES=4k PRESET=fast tools/render_piece.sh …  → 3840×2160 (Chrome DPR 2; compositions unchanged), faster transcode for 4K
# Output: pieces/<segment>/<segment>.mp4.partNN + .sha256 (x264 medium CRF 18, no audio) — commit + push them; the lead
# fetches, joins (cat parts), concats the segments, mixes and delivers. Never kill the render.
set -e
export PATH=~/.local/bin:$PATH
n=$1; L=$2; s=$3
R="$(cd "$(dirname "$0")/.." && pwd)"; cd "$R"
log(){ echo "$(date -u +%H:%M:%SZ) $*"; }
[ -f "vo_$n.mp3" ] || { [ -f input/join.sh ] && bash input/join.sh >/dev/null 2>&1 || true; }
tools/make_sandbox.sh "qa${n#c}" >/dev/null 2>&1 || true
python3 tools/build_master.py --prefix "${n}s" --vo "vo_$n.mp3" --len "$L" --out index.html | tail -1
mv index.html "work/qa${n#c}/index.html"; git checkout -q index.html 2>/dev/null || true
Q="work/qa${n#c}/index.html"; host="$s-host"
d=$(grep "id=\"$host\"" "$Q" | grep -o 'data-duration="[0-9.]*"' | cut -d'"' -f2)
[ -n "$d" ] || { log "segment $s not found in $Q"; exit 1; }
tools/make_sandbox.sh "r_$s" >/dev/null 2>&1 || true
python3 - "$Q" "work/r_$s/index.html" "$host" "$d" <<'PY'
import sys, re
src, dst, host, d = sys.argv[1:]
h = open(src).read()
h = '\n'.join(l for l in h.split('\n') if not re.search(r'-host"|id="vo-main"', l) or f'id="{host}"' in l)
h = re.sub(r'(id="root"[^>]*data-duration=")[0-9.]+', lambda m: m.group(1) + d, h)
h = re.sub(r'(id="' + host + r'"[^>]*data-start=")[0-9.]+', lambda m: m.group(1) + '0.000', h)
open(dst, 'w').write(h)
PY
log "$s: sandbox ready (${d}s, $(nproc) cores, $(free -g | awk '/Mem/{print $2}') GB RAM, $(df -h . | awk 'NR==2{print $4}') free)"
(cd "work/r_$s" && npx --yes hyperframes@0.8.217 lint 2>&1 | grep -E "error\(s\)") || true
[ "${DRY:-0}" = 1 ] && { log "DRY run: stopping before render"; exit 0; }
mkdir -p renders/pieces; t0=$(date +%s)
(cd "work/r_$s" && npx --yes hyperframes@0.8.217 render -w ${WORKERS:-3} -q draft --crf 18 ${RES:+--resolution $RES} -o "../../renders/pieces/$s.draft.mp4" > render.log 2>&1)
[ -s "renders/pieces/$s.draft.mp4" ] || { log "RENDER FAILED: $(tail -c 300 work/r_$s/render.log)"; exit 1; }
t1=$(date +%s); log "$s: rendered in $((t1-t0))s"
VF=""; if [ -n "$DROP" ]; then EX=$(echo "$DROP" | tr ',' '\n' | awk -F- '{printf "%sbetween(n\\,%s\\,%s)", (NR>1?"+":""), $1, $2-1}'); VF="-vf select=not($EX),setpts=N/24/TB"; log "$s: dropping frames $DROP"; fi
if [ -n "$SCALE" ]; then SC="scale=-2:${SCALE}:flags=lanczos"; if [ -n "$VF" ]; then VF="${VF},${SC}"; else VF="-vf $SC"; fi; log "$s: scaling to ${SCALE}p"; fi
ffmpeg -v error -y -i "renders/pieces/$s.draft.mp4" $VF -c:v libx264 -preset ${PRESET:-medium} -crf ${CRF:-18} -pix_fmt yuv420p -an -movflags +faststart "renders/pieces/$s.mp4"
rm -f "renders/pieces/$s.draft.mp4"; log "$s: transcoded in $(( $(date +%s)-t1 ))s ($(du -h renders/pieces/$s.mp4 | cut -f1))"
mkdir -p "pieces/$s"; (cd renders/pieces && sha256sum "$s.mp4") > "pieces/$s/$s.mp4.sha256"
split -b 95m -d -a 2 "renders/pieces/$s.mp4" "pieces/$s/$s.mp4.part"
log "$s: total $(( $(date +%s)-t0 ))s; parts ready in pieces/$s/ — commit and push them"
