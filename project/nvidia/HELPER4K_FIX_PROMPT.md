# 4K re-render helper — NVIDIA review fixes (you render ONE segment in 4K and push it to git; no creative decisions)
Your prompt gives you SEG. There is NO gofile/upload step: the lead relays from git. Pushing the video parts to YOUR branch is the job.
0. `git fetch --depth 1 origin claude/nvidia-edit && git checkout -B render4k/<SEG>-v2 FETCH_HEAD`;
   check `ls compositions/<SEG>.html tools/nv_facecam_master.py project/nvidia/segments.json` exist and `git log -1 --oneline` shows
   "NVIDIA review fixes" (or a later commit). `df -h .`
1. `bash setup.sh > /tmp/setup.log 2>&1; tail -3 /tmp/setup.log; export PATH=~/.local/bin:$PATH; which ffmpeg zsh` (a dpkg error is fine).
2. FACE-CAM SEGMENTS ONLY (nvs04, nvs05, nvs09): build the native-4K face-cam window from Krish's raw takes (downloads them from Drive):
   `A=$(python3 -c "import json;s=[x for x in json.load(open('project/nvidia/segments.json'))['segments'] if x['seg']=='<SEG>'][0];print(s['start'],s['end'])")`
   `mkdir -p assets/facecam && .venv/bin/python tools/nv_facecam_master.py assets/facecam/nvidia_facecam_master.mp4 --window $A`
   (8–20 min; must end with an `OUT … 2400.6…s` line and `ffprobe` must show 3840x2160). nvs11 and nvs16 skip this step.
3. Dry run: `DRY=1 RES=4k PRESET=fast tools/render_piece.sh nv 2402 <SEG>` — must print "sandbox ready".
4. Render: start `RES=4k PRESET=fast tools/render_piece.sh nv 2402 <SEG> > /tmp/render_<SEG>.log 2>&1` as a tracked background job
   (run_in_background), then stay in a BLOCKING wait (until-loop: `grep -q "parts ready" /tmp/render_<SEG>.log || grep -q FAILED /tmp/render_<SEG>.log`,
   sleep 60). 4K takes 20–120 min. NEVER kill the render, never end your turn while it runs, run nothing heavy beside it.
5. Check `ffprobe -v error -select_streams v -show_entries stream=width,height,nb_frames -of csv=p=0 renders/pieces/<SEG>.mp4` → 3840,2160,…
   Grab one still at the time your prompt names and LOOK at it (Read tool):
   `ffmpeg -v error -ss <T> -i renders/pieces/<SEG>.mp4 -frames:v 1 -vf scale=960:-1 /tmp/still.jpg`
6. Push to git (this IS the delivery — the lead approved it; the parts are ≤ 95 MB each):
   `git add pieces/<SEG> && git commit -m "render <SEG> 4K (review fixes)" && git push -u origin render4k/<SEG>-v2` (retry 4× with backoff).
7. Reply with: render time, frames, file size, `md5sum renders/pieces/<SEG>.mp4`, what the still shows, push result, last 5 log lines.
If any step fails twice, stop and report the exact error. Never edit compositions, lib, tools or assets (except the face-cam file in step 2).
