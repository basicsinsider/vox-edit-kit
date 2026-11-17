# Render helper — NVIDIA edit (you render ONE segment; no creative decisions)
You are a render helper for the NVIDIA documentary in this repo (branch `claude/nvidia-edit`, sparse checkout). Do exactly this:
1. `cd` into the repo root. `bash setup.sh > /tmp/setup.log 2>&1; tail -3 /tmp/setup.log` then `export PATH=~/.local/bin:$PATH`.
   (setup.sh can print a dpkg error — fine if `which ffmpeg zsh` both exist.)
2. If your segment uses the face cam (nvs01–nvs09, nvs23): `bash input/nvidia_join.sh` (must end with `OK` from sha256sum).
3. Dry run: `DRY=1 tools/render_piece.sh nv 2402 <SEG>` — must print "sandbox ready" (lint errors in OTHER projects' compositions are expected).
4. Render: start `tools/render_piece.sh nv 2402 <SEG> > /tmp/render_<SEG>.log 2>&1` as a tracked background job (run_in_background),
   then stay in a BLOCKING wait (a Monitor/until-loop on `grep -q "parts ready" /tmp/render_<SEG>.log || grep -q FAILED /tmp/render_<SEG>.log`).
   NEVER kill the render, never end your turn while it runs, run nothing heavy beside it.
5. `ls -la pieces/<SEG>/` then commit ONLY `pieces/<SEG>/` and push to your branch `render/<SEG>`:
   `git checkout -b render/<SEG> && git add pieces/<SEG> && git commit -m "render <SEG> 1080p" && git push -u origin render/<SEG>`
   (retry the push up to 4 times with backoff on network errors).
6. Reply with: render time, transcode time, the sha256 line from `pieces/<SEG>/<SEG>.mp4.sha256`, number of parts, and the last 5 lines of the log.
If anything fails twice, stop and report the exact error. Never edit compositions, lib, tools or assets.
