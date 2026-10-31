#!/bin/bash
# THE render process for every chunk (MANUAL §11). Speed-first, restart-proof, never kills anything.
#
#   tools/render_chunk.sh <chunk> <len_s> [<chunk> <len_s> ...]      e.g. tools/render_chunk.sh c2 597.86 c4 601.44
#   Launch it DETACHED (it outlives the tool shell):  tools/render_launch.sh c2 597.86 c4 601.44
#
# Per chunk (assembled master in work/qa<N>/index.html, built with tools/build_master.py):
#   1. split the master into its segments (one sandbox per segment: work/r_<seg>/index.html, segment at t=0, no VO)
#   2. render each segment ALONE with the fast settings  -w 3 -q draft --crf 18
#      (parallel beginframe capture streamed to an ultrafast encoder: ~7.5 fps on 4 cores vs ~2 fps with the defaults)
#   3. right after each segment: transcode to x264 medium CRF 18 (small, same look), delete the draft file
#   4. finished segments are kept in renders/<chunk>/pieces/ and SKIPPED on a re-run → a container restart costs at most
#      the one segment that was rendering; just launch the same command again
#   5. concat (stream copy) → final mix (tools/final_mix.sh: VO untouched at unity + 3 beds) → review copies → delivery
# Rules: one render at a time; nothing else heavy runs while it renders; NEVER kill a render or its parent process.
export PATH=~/.local/bin:$PATH
R="$(cd "$(dirname "$0")/.." && pwd)"
LOG="$R/renders/render_log.txt"; mkdir -p "$R/renders"
log(){ echo "$(date -u +%Y-%m-%dT%H:%MZ) $*" | tee -a "$LOG"; }
# wait for any other render to finish first (never two at once, never kill)
while ps -eo cmd | grep -q "hyperframes@0.8.217 [r]ender"; do sleep 30; done

while [ $# -ge 2 ]; do
  n=$1; L=$2; shift 2
  Q="$R/work/qa${n#c}/index.html"; P="$R/renders/$n/pieces"; mkdir -p "$P"
  [ -f "$Q" ] || { log "$n: no assembled master at $Q — run tools/build_master.py first"; continue; }
  ok=1
  for host in $(grep -o "id=\"${n}s0[0-9]-host\"" "$Q" | cut -d'"' -f2); do
    s=${host%-host}; out="$P/$s.mp4"
    if [ -s "$out" ]; then log "$s: already rendered, skipping"; continue; fi
    d=$(grep "id=\"$host\"" "$Q" | grep -o 'data-duration="[0-9.]*"' | cut -d'"' -f2)
    (cd "$R" && tools/make_sandbox.sh "r_$s" >/dev/null 2>&1)
    python3 - "$Q" "$R/work/r_$s/index.html" "$host" "$d" <<'PY'
import sys, re
src, dst, host, d = sys.argv[1:]
h = open(src).read()
h = '\n'.join(l for l in h.split('\n') if not re.search(r'-host"|id="vo-main"', l) or f'id="{host}"' in l)
h = re.sub(r'(id="root"[^>]*data-duration=")[0-9.]+', lambda m: m.group(1) + d, h)
h = re.sub(r'(id="' + host + r'"[^>]*data-start=")[0-9.]+', lambda m: m.group(1) + '0.000', h)
open(dst, 'w').write(h)
PY
    rm -rf "$P/.$s"* "$P"/work-* "$P/$s.draft.mp4"
    t0=$(date +%s); log "$s: render start (${d}s)"
    (cd "$R/work/r_$s" && npx --yes hyperframes@0.8.217 render -w 3 -q draft --crf 18 -o "$P/$s.draft.mp4" > render.log 2>&1)
    if [ ! -s "$P/$s.draft.mp4" ]; then log "$s: RENDER FAILED — $(tail -c 300 "$R/work/r_$s/render.log" | tr '\n' ' ')"; ok=0; break; fi
    log "$s: rendered in $(( $(date +%s) - t0 ))s; transcoding"
    ffmpeg -v error -y -i "$P/$s.draft.mp4" -c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p -an -movflags +faststart "$P/$s.tmp.mp4" \
      && mv "$P/$s.tmp.mp4" "$out" && rm -f "$P/$s.draft.mp4"
    log "$s: done in $(( $(date +%s) - t0 ))s total ($(du -h "$out" | cut -f1))"
  done
  [ $ok = 1 ] || { log "$n: stopped — fix and re-run (finished segments are kept)"; continue; }
  ls "$P"/${n}s0*.mp4 | grep -v -e draft -e tmp | sort | sed "s#^#file '#; s#\$#'#" > "$P/list.txt"
  ffmpeg -v error -y -f concat -safe 0 -i "$P/list.txt" -c copy "$R/renders/$n/${n}_picture.mp4" \
    && log "$n: picture $(ffprobe -v error -show_entries format=duration -of csv=p=0 "$R/renders/$n/${n}_picture.mp4")s (VO $L s)"
  (cd "$R" && tools/final_mix.sh "$n" "vo_$n.mp3" "$L" "assets/audio/$n" "renders/$n/${n}_picture.mp4" "renders/$n") >> "$LOG" 2>&1 \
    && rm -rf "$R/renders/$n/${n}_picture.mp4" "$P" && log "$n: mixed → renders/$n/${n}_final.mp4 + review/${n}_720p.mp4"
  [ -x "$R/tools/deliver.sh" ] && (cd "$R" && tools/deliver.sh "$n" >> "$LOG" 2>&1) && log "$n: delivered (review/${n}_1080p_view.mp4 + deliveries branch)"
done
log "queue finished"
