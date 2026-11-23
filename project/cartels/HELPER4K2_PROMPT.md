# 4K render helper (final 4K, 2026-11-23) — US vs Cartels: render ONE segment in 4K, then wait for the hand-off instruction
SEG is in your prompt. No creative decisions; never edit compositions, lib, tools or assets.
0. `git fetch --depth 1 origin claude/cartels-edit && git checkout -B render4k/<SEG> FETCH_HEAD`; check `ls compositions/<SEG>.html vo_ct.mp3 lib/ct_motifs.js`.
1. `bash setup.sh > /tmp/setup.log 2>&1; tail -3 /tmp/setup.log; export PATH=~/.local/bin:$PATH; which ffmpeg zsh` (a dpkg error is fine). `df -h .`
2. Dry run: `DRY=1 RES=4k CRF=20 PRESET=medium tools/render_piece.sh ct 1341.912 <SEG>` — must print "sandbox ready" (other projects' lint errors are expected).
3. Render: start `RES=4k CRF=20 PRESET=medium tools/render_piece.sh ct 1341.912 <SEG> > /tmp/render_<SEG>.log 2>&1` as a tracked background
   job (run_in_background), then stay in a BLOCKING wait (until-loop: `grep -q "parts ready" /tmp/render_<SEG>.log || grep -q FAILED /tmp/render_<SEG>.log`,
   sleep 60). 4K takes 20–90 min. NEVER kill the render, never end your turn while it runs, run nothing heavy beside it.
4. Check `ffprobe -v error -select_streams v -show_entries stream=width,height,nb_frames -of csv=p=0 renders/pieces/<SEG>.mp4` → 3840,2160,…
   and `ls -la pieces/<SEG>/`.
5. Do NOT commit, push or upload yet. Reply with: render + transcode time, frames, file size, sha256 (pieces/<SEG>/<SEG>.mp4.sha256), number of
   parts, last 5 log lines — then end your turn. The lead will send the hand-off instruction (git branch or upload) as a follow-up message.
If any step fails twice, stop and report the exact error.
