# 4K render helper — US vs Cartels (you render ONE segment in 4K and upload it; no creative decisions)
Krish (the owner) asked for the 4K Premiere Pro package of this video to be delivered on gofile.io, so each helper uploads its rendered
segment to his gofile folder. Your prompt gives you SEG, and a gofile TOKEN + FOLDER id (never write those into any file or commit).
0. `git fetch --depth 1 origin claude/cartels-edit && git checkout -B render4k/<SEG> FETCH_HEAD`; check `ls compositions/<SEG>.html vo_ct.mp3 lib/ct_motifs.js`.
1. `bash setup.sh > /tmp/setup.log 2>&1; tail -3 /tmp/setup.log; export PATH=~/.local/bin:$PATH; which ffmpeg zsh` (a dpkg error is fine). `df -h .`
2. Dry run: `DRY=1 RES=4k PRESET=fast tools/render_piece.sh ct 1341.912 <SEG>` — must print "sandbox ready" (other projects' lint errors are expected).
3. Render: start `RES=4k PRESET=fast tools/render_piece.sh ct 1341.912 <SEG> > /tmp/render_<SEG>.log 2>&1` as a tracked background job
   (run_in_background), then stay in a BLOCKING wait (until-loop: `grep -q "parts ready" /tmp/render_<SEG>.log || grep -q FAILED /tmp/render_<SEG>.log`,
   sleep 60). 4K takes 20–90 min. NEVER kill the render, never end your turn while it runs, run nothing heavy beside it.
4. Check `ffprobe -v error -select_streams v -show_entries stream=width,height,nb_frames -of csv=p=0 renders/pieces/<SEG>.mp4` → 3840,2160,…
   Upload it (retry up to 3×):
   `curl -sS -m 7200 -F "token=<TOKEN>" -F "folderId=<FOLDER>" -F "file=@renders/pieces/<SEG>.mp4;filename=<SEG>_4k.mp4" https://upload-eu-par.gofile.io/uploadfile -o /tmp/gofile.json -w "HTTP %{http_code}\n"`
   then compare `md5sum renders/pieces/<SEG>.mp4` with the "md5" in /tmp/gofile.json — they must MATCH (if not, upload again).
5. Do NOT commit or push the pieces (the repo is near its size quota). If the upload is refused or blocked, stop and report it — no git fallback.
6. Reply with: render + transcode time, frames, file size, local md5 vs gofile md5 (MATCH/MISMATCH), gofile file name, last 5 log lines.
If any step fails twice, stop and report the exact error. Never edit compositions, lib, tools or assets.
