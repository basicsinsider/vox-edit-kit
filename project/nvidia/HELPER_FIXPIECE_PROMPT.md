# Assembly helper — NVIDIA review fixes (you cut + encode a few 4K segments and push them to git; no creative decisions)
Your prompt gives you a GROUP name (g1/g2/g3) and a list of SEGs. There is NO upload step: pushing the pieces to YOUR branch is the delivery
(the lead joins them and uploads the final 4K file). The pieces are ≤ 95 MB each.
0. `git fetch --depth 1 origin claude/nvidia-edit && git checkout -B render4k/fix-<GROUP> FETCH_HEAD`;
   check `ls tools/nv_fix_piece.py project/nvidia/fix_cuts.json project/nvidia/segments.json` exist. `df -h . /tmp` (need ≥ 5 GB free).
1. `bash setup.sh > /tmp/setup.log 2>&1; tail -3 /tmp/setup.log; export PATH=~/.local/bin:$PATH; which ffmpeg` (a dpkg error is fine).
2. For EACH SEG in your list, in order:
   a. start `python3 tools/nv_fix_piece.py <SEG> > /tmp/piece_<SEG>.log 2>&1; echo EXIT $? >> /tmp/piece_<SEG>.log` as a tracked background job
      (run_in_background), then stay in a BLOCKING wait (until-loop: `grep -q EXIT /tmp/piece_<SEG>.log`, sleep 60). 5–15 min per segment.
      NEVER kill it, never end your turn while it runs, run nothing heavy beside it.
   b. `tail -3 /tmp/piece_<SEG>.log` must end with `<SEG>: OK frames …` and `EXIT 0`. If not, run 2a once more; if it fails twice, stop and report.
   c. `git add pieces/fix/<SEG>.* && git commit -m "fix piece <SEG>" && git push -u origin render4k/fix-<GROUP>` (retry 4× with backoff).
3. Reply with, per SEG: the `OK frames …` line, number of parts, push result; plus total time.
Never edit tools, compositions, lib or assets. If any step fails twice, stop and report the exact error.
