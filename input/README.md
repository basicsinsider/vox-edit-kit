# Inputs to edit

- `Face Cam.mp4` — 1920×1080 H.264 face-cam footage, 4 min 35 s (with audio).
- `Final Full Audio.mp3` — the final full voiceover, 4 h 26 min, MP3 192 kbps.

They are stored as byte-exact parts in `parts/` (GitHub's file limit is 100 MB). Rebuild them first:

    bash input/join.sh      # writes input/Face Cam.mp4 and input/Final Full Audio.mp3, then verifies SHA-256

Never re-encode or process the voiceover: trim with `ffmpeg -ss … -t … -c copy` only (MANUAL §0).
Krish will say which part(s) to edit and how the face-cam footage should be used.
