#!/bin/bash
# Pull finished helper pieces (branches render/<seg>), verify SHA-256, place them at renders/<chunk>/pieces/<seg>.mp4
# (where tools/render_chunk.sh skips them). Prints one line per newly collected piece. Safe to run repeatedly.
R="$(cd "$(dirname "$0")/.." && pwd)"; cd "$R"
ONLY=${ONLY:-}
for b in $(git ls-remote --heads origin "${BRANCH_PREFIX:-render}/${ONLY}*" 2>/dev/null | awk '{print $2}' | sed 's#refs/heads/##'); do
  s=${b#${BRANCH_PREFIX:-render}/}; ch=${s%s[0-9][0-9]}; out="renders/$ch/pieces/$s.mp4"
  [ -s "$out" ] && continue
  avail=$(df --output=avail -B1 . | tail -1); [ $avail -gt 1200000000 ] || { echo "$s: skipped — only $avail bytes free"; continue; }
  T=$(mktemp -d "$R/work/_pc_XXXX")
  git fetch -q --depth 1 origin "$b" || { rm -rf "$T"; continue; }
  # blob-by-blob (not `git archive`): on a blob:none partial clone, archive lazily fetched the WHOLE tree (~7.7 GB, Paraguay 4K)
  mkdir -p "renders/$ch/pieces"; : > "$out.tmp"
  for f in $(git ls-tree --name-only FETCH_HEAD "pieces/$s/" | grep '\.part' | sort); do git cat-file blob "FETCH_HEAD:$f" >> "$out.tmp" || { echo "$s: blob $f failed"; break; }; done
  want=$(git cat-file blob "FETCH_HEAD:pieces/$s/$s.mp4.sha256" | cut -d' ' -f1); got=$(sha256sum "$out.tmp" | cut -d' ' -f1)
  if [ "$want" = "$got" ]; then mv "$out.tmp" "$out"; echo "$s: collected ($(ffprobe -v error -count_packets -select_streams v -show_entries stream=nb_read_packets -of csv=p=0 "$out") frames, sha ok)"
  else rm -f "$out.tmp"; echo "$s: SHA MISMATCH ($got vs $want) — not used"; fi
  rm -rf "$T"; git update-ref -d "refs/remotes/origin/$b" 2>/dev/null
done
true  # no prune here: it could race a delivery commit
