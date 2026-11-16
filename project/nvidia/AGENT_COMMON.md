# NVIDIA project — rules every agent follows (lead: the NVIDIA session; owner: Krish, channel "Searching Lessons")

Video: "Is the chip ban actually working?" — a 40:01 documentary about the US chip export ban on China (NVIDIA GPUs, smuggling,
the AI lead, Huawei, the Malaysia renting loophole). Narrator: Sam. The cut narration with master times is
`project/nvidia/script_clean.txt` (word timings `transcript_nv.json`, audio `vo_nv.mp3`). Read `project/nvidia/BRIEF.md` first.

Binding rules
- Never assume — test every claim/tool/file with a small check before relying on it or reporting it.
- No fact-checking of the narration: on-screen text and visuals follow what Sam says. But every visual must be the TRUE thing he
  names (right person, right chip, right place, right year) with names/numbers spelled correctly.
- Sources: free/PD/CC first; copyrighted news photos, press images, product shots, article screenshots, TV frames are allowed as
  fair use for this channel (MANUAL §10.9) — credit + log them. Never log in, never create accounts, never pay, never strip
  watermarks, never use AI-generated images, never fabricate a "real" headline, document, tweet or screenshot.
- LOOK at every file you save (Read the image / a contact sheet) and reject wrong subject, watermarks, < 1600 px long side
  (portraits/logos may be smaller if sharp). Footage: h264 ≤ 1080p, 24 fps, no audio, trims of 3–10 s, scene-detect for hidden cuts.
- Log EVERY file in the folder's `SOURCES.md`: file, subject, URL, licence or "© owner, fair use", author, date, size.
- Work only inside your assigned output folders. Keep scratch scripts/downloads in your OWN scratch dir `work/<your-agent-name>/`
  (gitignored) and delete big temp files when done. Disk is tight: keep your total output under the cap given in your brief.
- The box has 4 shared CPU cores and other agents are running: no heavy parallel jobs, `nice` anything long.
- Network notes (MANUAL §1, §8.1, §10.5): Commons API often 429 → `python3 tools/find_media.py commons-html "<q>"` and
  `tools/commons_thumb.sh "File name.jpg" out.jpg 1920` (only widths 960/1280/1920/3840); YouTube/Instagram/Vimeo block this IP
  (list anything you could not fetch under "NEEDS RELAY" in your report with the exact URL); X/Twitter media via
  `curl -sS https://api.fxtwitter.com/<user>/status/<id>`; news-site article images usually download directly.
- Do not commit or push (the lead commits). Do not touch `lib/`, `tools/`, MANUAL.md or other agents' folders.
- Finish with a short report: what you produced (paths), what is missing/substituted, anything the lead must decide.
