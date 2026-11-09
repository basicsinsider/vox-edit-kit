#!/bin/bash
# Render each frame-aligned podcast segment separately; never kill a running render.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
export PATH="$HOME/.local/bin:$PATH"
mkdir -p renders/pod5/pieces work/pod5tmp work/pod5cache review
export TMPDIR="$ROOT/work/pod5tmp" HYPERFRAMES_EXTRACT_CACHE_DIR="$ROOT/work/pod5cache"
if [ -n "${POD5_HF_BIN:-}" ]; then CLI=("$POD5_HF_BIN"); else CLI=(npx --yes hyperframes@0.8.217); fi
for s in 01 02; do
  out="$ROOT/renders/pod5/pieces/pod5s${s}.mp4"
  if [ -s "$out" ]; then echo "$(date -u) pod5s${s}: existing completed piece, skipping"; continue; fi
  echo "$(date -u) pod5s${s}: render starting"
  (cd "$ROOT/work/pod5render${s}" && "${CLI[@]}" render -f 24 -w 3 -q draft --crf 18 -o "$ROOT/renders/pod5/pieces/pod5s${s}.draft.mp4" > "$ROOT/renders/pod5/pieces/pod5s${s}.log" 2>&1)
  test -s "$ROOT/renders/pod5/pieces/pod5s${s}.draft.mp4"
  echo "$(date -u) pod5s${s}: transcoding"
  ffmpeg -v error -y -i "$ROOT/renders/pod5/pieces/pod5s${s}.draft.mp4" -c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p -an -movflags +faststart "$ROOT/renders/pod5/pieces/pod5s${s}.tmp.mp4"
  mv "$ROOT/renders/pod5/pieces/pod5s${s}.tmp.mp4" "$out"
  rm "$ROOT/renders/pod5/pieces/pod5s${s}.draft.mp4"
  echo "$(date -u) pod5s${s}: complete"
done
printf "file '%s'\nfile '%s'\n" "$ROOT/renders/pod5/pieces/pod5s01.mp4" "$ROOT/renders/pod5/pieces/pod5s02.mp4" > "$ROOT/renders/pod5/pieces/list.txt"
ffmpeg -v error -y -f concat -safe 0 -i "$ROOT/renders/pod5/pieces/list.txt" -c copy "$ROOT/renders/pod5/pod5_picture.mp4"
echo "$(date -u) picture complete; mixing"
tools/final_mix.sh pod5_codex input/BB_podcast_v2_first5min.mp4 299 assets/audio/pod5_codex renders/pod5/pod5_picture.mp4 renders/pod5
echo "$(date -u) QUEUE COMPLETE"
