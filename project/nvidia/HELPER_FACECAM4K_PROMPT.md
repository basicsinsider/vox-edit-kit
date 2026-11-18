# Face-cam 4K helper — NVIDIA Premiere package (you build ONE file and upload it; no creative decisions)
Your prompt gives you a TOKEN and FOLDER id for the gofile upload (never write those into any file or commit).
0. `git fetch --depth 1 origin claude/nvidia-edit && git checkout -B render4k/facecam FETCH_HEAD`; check
   `ls tools/nv_facecam_master.py project/nvidia/edl_frames.json project/nvidia/parts.json` exist. `df -h .` (need ≈ 12 GB free).
1. `bash setup.sh > /tmp/setup.log 2>&1; tail -3 /tmp/setup.log; export PATH=~/.local/bin:$PATH; which ffmpeg` (a dpkg error is fine).
2. Build the WHOLE clean face cam at native 4K (downloads Krish's raw part 1 (3.5 GB) + part 3 from Drive; part 2 = black):
   start `.venv/bin/python tools/nv_facecam_master.py work/nvidia_facecam_master_4k.mp4 --preset fast > /tmp/fc.log 2>&1` as a tracked
   background job (mkdir -p work first), then stay in a BLOCKING wait (until-loop on the process ending, sleep 60, `tail -c 300 /tmp/fc.log`).
   Takes 30–120 min. NEVER kill it, never end your turn while it runs.
3. Check: `ffprobe -v error -select_streams v -show_entries stream=width,height,r_frame_rate,nb_frames:format=duration -of compact work/nvidia_facecam_master_4k.mp4`
   → 3840x2160, 30/1, ≈ 72019 frames, duration 2400.6 s (±0.05). Grab two stills and LOOK at them (Read tool):
   `ffmpeg -v error -ss 30 -i work/nvidia_facecam_master_4k.mp4 -frames:v 1 -vf scale=960:-1 /tmp/fc30.jpg` (Krish on camera) and
   `-ss 1500` (must be black: part 2 is audio-only).
4. Upload (retry up to 3×):
   `curl -sS -m 10800 -F "token=<TOKEN>" -F "folderId=<FOLDER>" -F "file=@work/nvidia_facecam_master_4k.mp4" https://upload-eu-par.gofile.io/uploadfile -o /tmp/gofile.json -w "HTTP %{http_code}\n"`
   then compare `md5sum work/nvidia_facecam_master_4k.mp4` with the "md5" in /tmp/gofile.json — they must MATCH (else upload again).
5. Reply with: build time, ffprobe line, file size, local md5 vs gofile md5 (MATCH/MISMATCH), what the two stills show, last 5 log lines.
No git push of the video (too big). If any step fails twice, stop and report the exact error. Never edit tools, compositions or assets.
