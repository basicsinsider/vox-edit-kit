#!/bin/bash
# Fetch rendered podcast pieces from the helpers' render/pd-* branches into renders/pieces/<id>.mp4 (SHA-256 checked).
#   tools/collect_pd.sh            (all branches; pieces already present and verified are skipped)
set -e; cd "$(dirname "$0")/.."; mkdir -p renders/pieces
for b in $(git ls-remote --heads origin 'render/pd-*' | awk '{print $2}' | sed 's#refs/heads/##'); do
  git fetch -q origin "$b" || { echo "fetch $b failed"; continue; }
  for id in $(git ls-tree --name-only "origin/$b" pieces/ 2>/dev/null | sed 's#pieces/##'); do
    out=renders/pieces/$id.mp4; want=$(git show "origin/$b:pieces/$id/$id.mp4.sha256" | awk '{print $1}')
    [ -f "$out" ] && [ "$(sha256sum "$out" | awk '{print $1}')" = "$want" ] && continue
    rm -f "$out"; for p in $(git ls-tree --name-only "origin/$b" "pieces/$id/" | grep '\.part'); do git show "origin/$b:$p" >> "$out"; done
    got=$(sha256sum "$out" | awk '{print $1}'); [ "$got" = "$want" ] && echo "$id OK ($b)" || { echo "$id SHA MISMATCH ($b)"; rm -f "$out"; }
  done
done
