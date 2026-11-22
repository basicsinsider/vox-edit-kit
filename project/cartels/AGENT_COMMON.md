# US vs Cartels — rules every agent follows (lead: the Cartels session; owner: Krish, channel "Searching Lessons")

Video: "US vs Cartels" — a ~25-min geopolitical/crime documentary: what America is actually doing in Mexico against the cartels
(the Nov 2026 capture of Fausto Isidro Meza Flores "El Chapo Isidro" in Guasave, Sinaloa; the Feb 2026 killing of El Mencho in
Tapalpa; the CIA in Chihuahua; boat strikes; Maduro; Ecuador; is it working?). Narrator: Sam. Script: `project/cartels/script.txt`
(the VO may improvise; on-screen text follows what he SAYS). Links: `project/cartels/links.txt`. Read `project/cartels/BRIEF.md`.

Binding rules
- Never assume — test every claim/tool/file with a small check before relying on it or reporting it.
- Every visual is the TRUE thing he names (right person, place, date, vehicle, document) with names/numbers spelled correctly.
- **No gore, ever.** No bodies, blood, corpses, executions, wounded people, hanging/dismembered remains, cartel propaganda videos.
  Imply violence through framing: smoke on a skyline, burnt-out vehicles (empty), roadblocks, police tape, soldiers on patrol,
  documents, headlines, maps. Reject any file that shows a dead or injured person, even small or blurred.
- No AI-generated images. In particular: the viral photo of El Mencho with the influencer is reported to be AI — never use it.
  Do not show the influencer's face or name her (the narration doesn't name her); no cartel banners.
- Sources: free/PD/CC first; copyrighted news photos/footage, government (SEDENA, Gabinete de Seguridad, FBI, DEA, DoD, White House)
  material, article screenshots, TV frames are allowed as fair use for this channel (MANUAL §10.9) — credit + log. Never log in,
  never create accounts, never pay, never strip watermarks, never fabricate a headline, document, tweet or screenshot.
- LOOK at every file you save (Read the image / a contact sheet) and reject wrong subject, watermarks over the subject, low res
  (< 1600 px long side for full-frame photos). Footage: h264 ≤ 1080p, 24 fps, no audio, trims of 3–15 s, scene-detect for cuts.
- Log EVERY file in its folder's `SOURCES.md`: file, subject, URL, licence or "© owner, fair use", author, date, size.
- Work only inside your assigned folders; scratch in `work/<your-agent-name>/` (gitignored), delete big temp files when done.
  Disk is tight (~12 GB free on the box, shared): stay under the cap in your brief.
- 4 shared CPU cores: no heavy parallel jobs, `nice` anything long.
- Network notes (MANUAL §1, §8.1, §10.5): Commons API often 429 → `python3 tools/find_media.py commons-html "<q>"` and
  `tools/commons_thumb.sh "File name.jpg" out.jpg 1920`; YouTube/Instagram/Vimeo block this IP (list anything you could not fetch
  under "NEEDS RELAY" with the exact URL); X/Twitter media via `curl -sS https://api.fxtwitter.com/<user>/status/<id>` →
  `tweet.media.videos[].url` (video.twimg.com downloads directly) — find X posts through news articles; news-site images usually
  download directly; DVIDS (dvidshub.net, US military, PD) and gob.mx press pages are good free sources.
- Do not commit or push (the lead commits). Do not touch `lib/`, `tools/`, MANUAL.md or other agents' folders.
- Finish with a short report: what you produced (paths), what is missing/substituted, anything the lead must decide.
