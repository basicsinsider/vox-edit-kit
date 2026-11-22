# Brief — "US vs Cartels" documentary, Searching Lessons
Owner: Krish. Written by the Cartels lead session, 2026-11-22, from the session brief. Branch `claude/cartels-edit`
(starts from `claude/nvidia-edit`, the newest kit, 2026-11-18: Taiwan, Ivan, Paraguay, Podcast, NVIDIA — tools, MANUAL,
§10.8 Music limits, 4K/A-V-sync fixes, `references/inspo-assets/`). "Let it rip!": be super creative within the house style.
Same process and quality bar as NVIDIA and Paraguay. MANUAL.md applies in full; this file adds to it.

## Input (tested downloadable from the cloud on 2026-11-22)
- Voiceover only: `us vs cartels.wav` — measured 2026-11-22: 285,349,870 bytes, **48 kHz MONO 32-bit float**, 1486.155 s (24:46).
  Drive folder https://drive.google.com/drive/folders/1Pu29yhAmhRxv9cw8iNEFR-mRg0Muo6pp
- `curl -sSL -C - -o input/vo_raw.wav "https://drive.usercontent.google.com/download?id=1tOHypqD7PANnfhkc8Ybrr7gaMyfTdIS2&export=download&confirm=t"` (input/ is gitignored).
- No script. The voiceover is the narration.

## Krish's rules for this video (binding)
1. **Same process as before.** Transcribe the VO (Parakeet), allowing for improvisation, then clean it with an EDL as in
   Paraguay/NVIDIA: cut errors, ums, ahs, false starts, retakes and long dead pauses. Cuts only, in silences, with a few-ms
   crossfades. Never EQ, compress, gain or normalise the voice. If the file turns out to be an already-clean finished VO, tell
   Krish and keep the cuts minimal.
2. **NO FACE CAM in this video.** The face-cam rules (§10.5, the 35/65 split, on-camera pop-ins) are paused. The whole video is
   edited visuals. The opening still follows the house intro style: a strong cold open on the first line.
3. **Geopolitical/crime documentary: the United States vs the cartels.** B-roll: real photos, footage, news, documents, maps
   (Mexico, the border, the US, the region, in map-kit style), charts. Every visual matches the exact words under it. Facts,
   names and numbers must be correct. Copyrighted material is OK under fair use; credit it and log it in SOURCES.md.
   **Handle violence responsibly: no gore.** Imply it through framing, documents, news and maps, the way serious documentaries do.
4. **References**: `references/inspo-assets/` (INDEX.md, assets.json, img/). Use only those that fit this story, keep accuracy;
   don't try to use them all. Note which reference inspired each scene.
5. **Music stays much lower than the voice**, per the current §10.8 limits. Measure and report the numbers.
6. **Palette**: a NEW palette fitting this story, distinct from Taiwan, Ivan, Paraguay, the Podcast and NVIDIA. Same fonts
   (Cooper Hewitt, Haskoy, Crimson Pro only). Show Krish a swatch, but keep working while waiting.
7. **Deliverable for now**: a 720p version uploaded to gofile.io, md5 check after upload. Give Krish the link and remind him to
   download soon. No 4K unless he asks.
8. No narration captions (MANUAL §0).

## Model split (as in NVIDIA)
- Lead: transcript, EDL, story, plans, palette, references, QA of snapshots, final checks.
- Segment editors, asset gatherers, sound designer: Agent subagents with model "opus", each with a complete brief.
- Render helper cloud sessions: `create_session` with model "claude-sonnet-5-5"; they only run tools/render_piece.sh and push.
  A helper that fails twice on the same segment is retried on "claude-opus-5-5".

## Owner rules, always
- Never assume anything. Test it, even with a tiny check, before relying on it or telling Krish.
- Never kill a running render, for any reason.
- This cloud machine shuts down when the session goes idle: never leave a long job running between turns; blocking waits;
  heavy work on helpers/agents.
- Render fast via helpers (MANUAL §11/§11.1 and NVIDIA's notes). Watch the disk before every big write (/dev/shm notes).
- Commit and push to `claude/cartels-edit` often. Never commit or print keys. Never log in or create accounts.
- Epidemic Sound: www.epidemicsound.com is a proxy-injected connected service; `tools/epidemic_mcp.py` takes a dummy
  (`EPIDEMIC_SOUND_MCP_API_KEY=epidemic_live_dummy`). Tested 2026-11-22: `SearchRecordings '{"query":{"term":"tense documentary"}}'`
  returned tracks — no credential form was needed.

## Order of work
1 credentials ✅ → 2 "started" ✅ → 3 download ✅ + transcribe → 4 EDL + clean VO, report length and topic → 5 plan →
6 palette → 7 references → 8 editors + gatherers (Opus) → 9 sound → 10 snapshot QA → 11 render (Sonnet helpers), 720p on gofile.
