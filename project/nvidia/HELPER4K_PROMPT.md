# 4K render helper — NVIDIA edit (you render ONE segment in 4K and upload it; no creative decisions)
Your prompt gives you SEG, and for the gofile upload a TOKEN and FOLDER id (never write those into any file or commit).
0. Your session branch may start from the repo's DEFAULT branch: `git fetch --depth 1 origin claude/nvidia-edit && git checkout -B render4k/<SEG> FETCH_HEAD`
   and check `ls compositions/<SEG>.html tools/nv_facecam_master.py project/nvidia/segments.json` all exist.
1. `bash setup.sh > /tmp/setup.log 2>&1; tail -3 /tmp/setup.log; export PATH=~/.local/bin:$PATH; which ffmpeg zsh` (a dpkg error is fine). `df -h .`
2. FACE-CAM SEGMENTS ONLY (nvs01–nvs09 and nvs23): build the native-4K face-cam window from Krish's raw takes (downloads them from Drive):
   `A=$(python3 -c "import json;s=[x for x in json.load(open('project/nvidia/segments.json'))['segments'] if x['seg']=='<SEG>'][0];print(s['start'],s['end'])")`
   `mkdir -p assets/facecam && .venv/bin/python tools/nv_facecam_master.py assets/facecam/nvidia_facecam_master.mp4 --window $A`
   (8–20 min; must end with an `OUT … 2400.6…s` line and `ffprobe` must show 3840x2160). Other segments skip this step.
3. Dry run: `DRY=1 RES=4k PRESET=fast tools/render_piece.sh nv 2402 <SEG>` — must print "sandbox ready".
4. Render: start `RES=4k PRESET=fast tools/render_piece.sh nv 2402 <SEG> > /tmp/render_<SEG>.log 2>&1` as a tracked background job
   (run_in_background), then stay in a BLOCKING wait (until-loop: `grep -q "parts ready" /tmp/render_<SEG>.log || grep -q FAILED /tmp/render_<SEG>.log`,
   sleep 60). 4K takes 20–120 min. NEVER kill the render, never end your turn while it runs, run nothing heavy beside it.
5. Check `ffprobe -v error -select_streams v -show_entries stream=width,height,nb_frames -of csv=p=0 renders/pieces/<SEG>.mp4` → 3840,2160,…
   Upload it (retry up to 3×):
   `curl -sS -m 7200 -F "token=<TOKEN>" -F "folderId=<FOLDER>" -F "file=@renders/pieces/<SEG>.mp4;filename=<SEG>_4k.mp4" https://upload-eu-par.gofile.io/uploadfile -o /tmp/gofile.json -w "HTTP %{http_code}\n"`
   then compare `md5sum renders/pieces/<SEG>.mp4` with the "md5" in /tmp/gofile.json — they must MATCH (if not, upload again).
6. Backup to git: `git add pieces/<SEG> && git commit -m "render <SEG> 4K" && git push -u origin render4k/<SEG>` (retry 4× with backoff;
   `--force-with-lease` only if rejected because the remote branch holds an old default-branch commit).
7. Reply with: render + transcode time, frames, file size, local md5 vs gofile md5 (MATCH/MISMATCH), gofile file name, git push result, last 5 log lines.
If any step fails twice, stop and report the exact error. Never edit compositions, lib, tools or assets (except the face-cam file in step 2).
