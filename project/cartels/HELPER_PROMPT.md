# Render helper — US vs Cartels (you render ONE segment; no creative decisions)
You are a render helper for the "US vs Cartels" documentary in this repo (branch `claude/cartels-edit`). SEG = the segment id in your prompt.
0. Your session branch may have been created from the repo's DEFAULT branch. First run
   `git fetch --depth 1 origin claude/cartels-edit && git checkout -B render/<SEG> FETCH_HEAD` and check that
   `ls compositions/<SEG>.html vo_ct.mp3 lib/ct_motifs.js` all exist.
1. In the repo root: `bash setup.sh > /tmp/setup.log 2>&1; tail -3 /tmp/setup.log` then `export PATH=~/.local/bin:$PATH`
   (setup.sh can print a dpkg error — fine if `which ffmpeg zsh` both exist).
2. Dry run: `DRY=1 SCALE=720 tools/render_piece.sh ct 1341.912 <SEG>` — must print "sandbox ready" (lint errors in OTHER projects'
   compositions are expected).
3. Render: start `SCALE=720 tools/render_piece.sh ct 1341.912 <SEG> > /tmp/render_<SEG>.log 2>&1` as a tracked background job
   (run_in_background), then stay in a BLOCKING wait (a Monitor/until-loop on
   `grep -q "parts ready" /tmp/render_<SEG>.log || grep -q FAILED /tmp/render_<SEG>.log`).
   NEVER kill the render, never end your turn while it runs, run nothing heavy beside it.
4. `ls -la pieces/<SEG>/` then commit ONLY `pieces/<SEG>/` and push to your branch `render/<SEG>`:
   `git add pieces/<SEG> && git commit -m "render <SEG> 720p" && git push -u origin render/<SEG>`
   (if rejected because the remote branch holds an old default-branch commit, use `--force-with-lease`; retry network errors up to 4
   times with backoff).
5. Reply with: render time, transcode time, the sha256 line from `pieces/<SEG>/<SEG>.mp4.sha256`, number of parts, frame count
   (`ffprobe -v error -count_frames -select_streams v -show_entries stream=nb_read_frames,width,height -of csv=p=0 renders/pieces/<SEG>.mp4`),
   and the last 5 lines of the log.
If anything fails twice, stop and report the exact error. Never edit compositions, lib, tools or assets.
