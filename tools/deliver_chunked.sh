#!/bin/bash
# Deliver a big master as 95 MB parts on branch deliveries/$N, pushed in chunks of $C parts (each push ~C*95 MB).
set -e
cd /home/user/vox-edit-kit
F=$1; N=$2; C=${3:-14}; P=95000000; B=deliveries/$N
SIZE=$(stat -c %s "$F"); SHA=$(sha256sum "$F" | cut -d' ' -f1); K=$(( (SIZE + P - 1) / P ))
declare -a BL
for (( k=0; k<K; k++ )); do
  BL[$k]=$(tail -c +$(( k*P + 1 )) "$F" | head -c $P | git hash-object -w --stdin)
done
echo "hashed $K parts"
parent=""; IDX=$(mktemp -u /home/user/vox-edit-kit/.git/cd_index_XXXX)
for (( end=C; ; end+=C )); do
  [ $end -gt $K ] && end=$K
  export GIT_INDEX_FILE=$IDX; rm -f $IDX
  for (( k=0; k<end; k++ )); do git update-index --add --cacheinfo 100644,${BL[$k]},$N/${N}_final.mp4.part$(printf %02d $k); done
  if [ $end -eq $K ]; then
    s1=$(printf '%s  %s_final.mp4\n' "$SHA" "$N" | git hash-object -w --stdin); git update-index --add --cacheinfo 100644,$s1,$N/${N}_final.mp4.sha256
    s2=$(printf '# %s master (3840x2160, VO + beds), %s parts\nRebuild:  cat %s/%s_final.mp4.part* > %s_final.mp4\nCheck:    shasum -a 256 %s_final.mp4   (must equal %s)\n' "$N" "$K" "$N" "$N" "$N" "$N" "$SHA" | git hash-object -w --stdin)
    git update-index --add --cacheinfo 100644,$s2,README.md
  fi
  T=$(git write-tree); unset GIT_INDEX_FILE; rm -f $IDX
  CM=$(git commit-tree $T ${parent:+-p $parent} -m "deliveries: $N master, parts 0-$((end-1)) of $K

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_017jFZyMH85zsrnvzsLqBFHX")
  ok=0; for i in 1 2 3 4 5; do git push -q origin $CM:refs/heads/$B && { ok=1; break; }; sleep $((2**i)); done
  [ $ok = 1 ] || { echo "PUSH FAILED at parts 0-$((end-1))"; exit 1; }
  echo "pushed parts 0-$((end-1)) ($CM)"; parent=$CM
  [ $end -eq $K ] && break
done
git ls-remote origin $B | grep -q $parent && echo "delivered $N: $B @ $parent ($K parts, sha256 $SHA)"
