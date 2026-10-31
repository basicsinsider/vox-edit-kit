#!/bin/bash
# deliver.sh cN : (1) review/cN_1080p_view.mp4 (<95 MB, main branch) (2) master renders/cN/cN_final.mp4 split into 95 MB parts on branch `deliveries`
set -e
N=$1; R="$(cd "$(dirname "$0")/.." && pwd)"; F=$R/renders/$N/${N}_final.mp4; B=deliveries
cd $R
[ -f $F ] || { echo "no $F"; exit 1; }
nice -n 19 ffmpeg -v error -y -i $F -c:v libx264 -preset medium -crf 23 -maxrate 1150k -bufsize 2300k -c:a aac -b:a 128k -movflags +faststart review/${N}_1080p_view.mp4
ls -la review/${N}_1080p_view.mp4
W=$R/work/_deliv_wt; rm -rf $W
if git ls-remote --exit-code --heads origin $B >/dev/null 2>&1; then
  git fetch -q origin $B:$B 2>/dev/null || true; git worktree add -q $W $B
else
  git worktree add -q --detach $W; (cd $W && git checkout -q --orphan $B && git rm -rq . && rm -rf ./* ./.[!.]* 2>/dev/null; true)
fi
cd $W; mkdir -p $N; split -b 95m -d -a 2 $F $N/${N}_final.mp4.part
( cd $N && sha256sum $F | sed "s#$F#${N}_final.mp4#" > ${N}_final.mp4.sha256 )
cat > README.md <<'R'
# Deliveries — full-quality 1080p masters, split into 95 MB parts
Rebuild each chunk:  cat cN/cN_final.mp4.part* > cN_final.mp4   (check: shasum -a 256 cN_final.mp4 vs cN/cN_final.mp4.sha256)
This branch is temporary and will be deleted after the files are pulled.
R
git add -A; git commit -qm "deliveries: $N master (1080p, split)

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_017jFZyLRaZgvs1oTMXrXxKe"
for i in 1 2 3 4; do git push -q -u origin $B && break; sleep $((2**i)); done
H=$(git rev-parse HEAD); git ls-remote origin $B | grep -q $H || { echo "PUSH FAILED — master kept at $F"; exit 1; }
cd $R; git worktree remove --force $W; git branch -D $B -q
git reflog expire --expire=now --all; nice -n 19 git prune --expire=now
rm -f $F   # the master is safe on the deliveries branch; frees disk for the next chunk
echo "delivered $N"; df -h $R | tail -1
