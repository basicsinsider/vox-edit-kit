#!/bin/bash
# Render segments of the Cartels master in 4K on THIS machine (no git parts): tools/render_local4k.sh <outdir> <seg> [<seg> …]
# Each: sandbox (same as render_piece.sh) → hyperframes render 3840×2160 (-q draft crf 18) → x264 fast CRF 18 → <outdir>/<seg>.mp4.
# Used when helper sessions can't hand files back (4K pieces are too big for git, helper uploads blocked). Never kill a running render.
set -e
export PATH=~/.local/bin:$PATH
OUT=$1; shift; L=1341.912
R="$(cd "$(dirname "$0")/.." && pwd)"; cd "$R"; mkdir -p "$OUT"
log(){ echo "$(date -u +%H:%M:%SZ) $*"; }
for s in "$@"; do
  [ -s "$OUT/$s.mp4" ] && { log "$s: exists, skipped"; continue; }
  tools/make_sandbox.sh qact >/dev/null 2>&1 || true
  python3 tools/build_master.py --prefix cts --vo vo_ct.mp3 --len "$L" --out index.html | tail -1
  mv index.html work/qact/index.html; git checkout -q index.html 2>/dev/null || true
  Q=work/qact/index.html; host="$s-host"
  d=$(grep "id=\"$host\"" "$Q" | grep -o 'data-duration="[0-9.]*"' | cut -d'"' -f2)
  [ -n "$d" ] || { log "segment $s not found"; exit 1; }
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
  log "$s: render start (${d}s)"; t0=$(date +%s)
  (cd "work/r_$s" && npx --yes hyperframes@0.8.217 render -w ${WORKERS:-3} -q draft --crf 18 --resolution 4k -o "$OUT/$s.draft.mp4" > "$OUT/$s.render.log" 2>&1)
  [ -s "$OUT/$s.draft.mp4" ] || { log "$s: RENDER FAILED: $(tail -c 300 $OUT/$s.render.log)"; exit 1; }
  t1=$(date +%s); log "$s: rendered in $((t1-t0))s ($(du -h $OUT/$s.draft.mp4 | cut -f1))"
  ffmpeg -v error -y -i "$OUT/$s.draft.mp4" -c:v libx264 -preset ${PRESET:-fast} -crf ${CRF:-18} -pix_fmt yuv420p -an -movflags +faststart "$OUT/$s.tmp.mp4"
  mv "$OUT/$s.tmp.mp4" "$OUT/$s.mp4"; rm -f "$OUT/$s.draft.mp4"; rm -rf "work/r_$s"
  log "$s: transcoded in $(( $(date +%s)-t1 ))s ($(du -h $OUT/$s.mp4 | cut -f1)); frames $(ffprobe -v error -count_packets -select_streams v -show_entries stream=nb_read_packets,width,height -of csv=p=0 $OUT/$s.mp4)"
done
log "ALL DONE"
