#!/bin/bash
# Pull finished helper pieces (branches render/<seg>), verify SHA-256, place them at renders/<chunk>/pieces/<seg>.mp4
# (where tools/render_chunk.sh skips them). Prints one line per newly collected piece. Safe to run repeatedly.
R="$(cd "$(dirname "$0")/.." && pwd)"; cd "$R"
for b in $(git ls-remote --heads origin 'render/*' 2>/dev/null | awk '{print $2}' | sed 's#refs/heads/##'); do
  s=${b#render/}; ch=${s%s0*}; out="renders/$ch/pieces/$s.mp4"
  [ -s "$out" ] && continue
  T=$(mktemp -d "$R/work/_pc_XXXX")
  git fetch -q --depth 1 origin "$b" || { rm -rf "$T"; continue; }
  git archive FETCH_HEAD "pieces/$s" | tar -x -C "$T" || { echo "$s: archive failed"; rm -rf "$T"; continue; }
  mkdir -p "renders/$ch/pieces"; cat "$T/pieces/$s/$s.mp4.part"* > "$out.tmp"
  want=$(cut -d' ' -f1 "$T/pieces/$s/$s.mp4.sha256"); got=$(sha256sum "$out.tmp" | cut -d' ' -f1)
  if [ "$want" = "$got" ]; then mv "$out.tmp" "$out"; echo "$s: collected ($(ffprobe -v error -count_packets -select_streams v -show_entries stream=nb_read_packets -of csv=p=0 "$out") frames, sha ok)"
  else rm -f "$out.tmp"; echo "$s: SHA MISMATCH ($got vs $want) — not used"; fi
  rm -rf "$T"; git update-ref -d "refs/remotes/origin/$b" 2>/dev/null
done
true  # no prune here: it could race a delivery commit
