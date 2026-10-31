#!/bin/bash
# deliver.sh cN : (1) review/cN_1080p_view.mp4 (<95 MB, working branch) (2) the master renders/cN/cN_final.mp4 as 95 MB
# parts on its own branch deliveries/cN — built WITHOUT extra disk: parts are cut from the END of the master and stored
# straight into git (hash-object), shrinking the master as we go; the commit is pushed by hash; on a failed push the master
# is rebuilt from the stored parts. NO_PUSH=1 = build + verify only (test).   Owner-approved (deliveries branches).
set -e
N=$1; R="$(cd "$(dirname "$0")/.." && pwd)"; cd "$R"; F=${F:-$R/renders/$N/${N}_final.mp4}; B=deliveries/$N; P=95000000
[ -f "$F" ] || { echo "no $F"; exit 1; }
if [ -z "$NO_VIEW" ] && [ ! -s review/${N}_1080p_view.mp4 ]; then
  nice -n 19 ffmpeg -v error -y -i "$F" -c:v libx264 -preset medium -crf 23 -maxrate 1150k -bufsize 2300k -c:a aac -b:a 128k -movflags +faststart review/${N}_1080p_view.mp4
fi
SIZE=$(stat -c %s "$F"); SHA=$(sha256sum "$F" | cut -d' ' -f1); K=$(( (SIZE + P - 1) / P ))
export GIT_INDEX_FILE=$(mktemp -u "$R/.git/deliver_index_XXXX"); declare -a BL
for (( k=K-1; k>=0; k-- )); do
  off=$(( k * P )); tmp="$F.cut"
  tail -c +$(( off + 1 )) "$F" > "$tmp"; BL[$k]=$(git hash-object -w "$tmp"); rm -f "$tmp"; truncate -s $off "$F"
done
for (( k=0; k<K; k++ )); do git update-index --add --cacheinfo 100644,${BL[$k]},$N/${N}_final.mp4.part$(printf %02d $k); done
s1=$(printf '%s  %s_final.mp4\n' "$SHA" "$N" | git hash-object -w --stdin); git update-index --add --cacheinfo 100644,$s1,$N/${N}_final.mp4.sha256
s2=$(printf '# %s master (1080p, VO + beds), %s parts\nRebuild:  cat %s/%s_final.mp4.part* > %s_final.mp4\nCheck:    shasum -a 256 %s_final.mp4   (must equal %s)\n' "$N" "$K" "$N" "$N" "$N" "$N" "$SHA" | git hash-object -w --stdin)
git update-index --add --cacheinfo 100644,$s2,README.md
T=$(git write-tree); rm -f "$GIT_INDEX_FILE"; unset GIT_INDEX_FILE
C=$(git commit-tree $T -m "deliveries: $N master (1080p, $K parts)

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_017jFZyLRaZgvs1oTMXrXxKe")
rebuild(){ : > "$F"; for (( k=0; k<K; k++ )); do git cat-file blob ${BL[$k]} >> "$F"; done; }
# verify the stored parts before touching the network
got=$( (for (( k=0; k<K; k++ )); do git cat-file blob ${BL[$k]}; done) | sha256sum | cut -d' ' -f1)
[ "$got" = "$SHA" ] || { rebuild; echo "VERIFY FAILED ($got vs $SHA) — master rebuilt"; exit 1; }
if [ -n "$NO_PUSH" ]; then rebuild; echo "NO_PUSH: commit $C verified ($K parts, sha ok), master rebuilt: $(sha256sum "$F" | cut -d' ' -f1)"; git prune --expire=now; exit 0; fi
for i in 1 2 3 4; do git push -q origin $C:refs/heads/$B && break; sleep $((2**i)); done
git ls-remote origin $B | grep -q $C || { rebuild; echo "PUSH FAILED — master rebuilt at $F"; exit 1; }
git update-ref -d refs/remotes/origin/$B 2>/dev/null; git reflog expire --expire=now --all; git prune --expire=now; rm -f "$F"
echo "delivered $N: $B @ $C ($K parts, sha256 $SHA)"; df -h "$R" | tail -1
