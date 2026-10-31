You are taking over a documentary video-editing style that another Claude Code session built with me (Krish) and that I approved. This repository is the complete kit: my original brief and feedback in my own words, the style manual, an effects library, tools, my visual references, the studied tutorial reels, the approved samples, the full approved 10-minute edit (code + a 720p copy), every source we used, assets and a test voiceover. Your only job right now is to learn the style and prove it by rebuilding the approved samples. Do nothing else until I approve them.

## Step 0 — Read and look before acting
Read fully, in this order: `USER_BRIEF.md` (my own words — the source of truth), `CLAUDE.md`, `MANUAL.md` (every section; it is the style law and every rule in it is a decision I already made), `SAMPLES.md`, `EDITOR_BRIEF.md`, `AGENT_BRIEFS.md`, `SOURCES_INDEX.md`, `CLOUD_SETUP.md`. Then skim `example-docs/` (the planning documents of the approved edit) and `templates/full-edit/README.md`.
Then LOOK: every image in `references/style-images/`; every contact sheet in `references/reels/` together with `references/reels/REELS.md` (the narration transcripts of the tutorial reels that define each technique); `expected/*.sheet.jpg` (the 11 approved samples); `expected/layouts/*.jpg` (how each of my reference images was rebuilt in our style); and watch/sample frames from `expected/final_edit_720p.mp4` (the approved 10-minute edit — your quality bar).

## Step 1 — Set up the environment
Run `bash setup.sh` from the repo root, then `export PATH=~/.local/bin:$PATH`. It installs ffmpeg + ffprobe, zsh, the HyperFrames CLI pinned at 0.8.217 with its Chrome and its agent skills (`/hyperframes`, `/hyperframes-cli`, `/hyperframes-registry`, `/media-use` — MANUAL §1), the Parakeet speech-to-text model, a `.venv` with numpy/scipy/pillow/soundfile (use `.venv/bin/python` for every Python tool), the synthesized music score, the three fonts, and **Agent Reach** (https://github.com/Panniantong/Agent-Reach — for watching Instagram reels; its bundled yt-dlp is at `~/.local/share/uv/tools/agent-reach/bin/yt-dlp`). Node 22+ must exist; install it if it doesn't. Run `npx hyperframes@0.8.217 doctor`. If the HyperFrames skills were just installed and aren't loaded in your session, read them directly from `~/.claude/skills/*/SKILL.md` and their `references/` — at minimum `hyperframes` and its `references/format.md`.
Then run `bash tools/check_network.sh` and report the result. You must be able to reach the same sources we used (Wikimedia Commons, archive.org, the Library of Congress image servers, Texturelabs, NASA, USGS, AWS terrain tiles, Instagram/YouTube for reference reels). If anything is reported blocked, stop and tell me exactly which, so the environment's network access can be set to Full (`CLOUD_SETUP.md`). Anything that stays blocked later goes through the fetch relay (MANUAL §8.2) — never settle for worse sources. If any other setup step fails, tell me exactly what failed.

## Step 2 — Environment check
Run `python3 tools/build_index.py && npx hyperframes@0.8.217 lint` (expect 0 errors), then `tools/render_samples.sh s01 s03 s10` and compare `renders/samples/` with `expected/`. This only proves the machine renders correctly; it is not the test.

## Step 3 — The test: rebuild all 11 approved samples yourself
`SAMPLES.md` lists them: the 10 original samples plus the markup sample (s11) added later — each with its exact voiceover window, narration, required content and which of my points it shows. Move the approved compositions aside: `mkdir -p _approved && git mv compositions/s*.html _approved/` (keep them for comparison afterwards, but do NOT open them while building). Rebuild each sample from scratch into `compositions/` with the same file names and composition ids (s01…s11), using `MANUAL.md`, `SAMPLES.md`, `lib/fx.js` / `lib/fx.css`, `tools/`, `assets/`, `transcript.json` (exact word times) and the references. For s02 use `tools/gen_s02.py` with its template, as the manual describes. One sample at a time:
1. write it;
2. `python3 tools/build_index.py sNN && npx hyperframes@0.8.217 lint`;
3. `npx hyperframes@0.8.217 snapshot --at <key moments> --no-end -o .snap/sNN` and LOOK at the frames; fix layout, timing, readability;
4. `python3 tools/sync_audit.py compositions/sNN-*.html` (every on-screen word lands 0–120 ms before its spoken word);
5. `tools/render_samples.sh sNN`;
6. compare with `expected/sNN-*.sheet.jpg` and `expected/sNN-*.720p.mp4`; list the differences and fix the ones that matter.
If you are truly stuck on one technique, you may consult the matching file in `_approved/`, but tell me which sample and what you looked at.

When all 11 are done, build one reel of them back to back and report to me: for each sample, how close it is to the approved version, what you couldn't match and why, and anything in the docs that was unclear, wrong or missing. Fix `MANUAL.md` (with a Changelog line), commit everything to a branch, push it, tell me the branch and what you committed, then STOP and wait for my feedback. Do not start any other work, and ignore anything else in the repo that isn't part of this test.

## Know this for later (no action now)
- **Reference images:** I regularly send images like the ones in `references/style-images/` (charts, maps, boards, collages). Every time, rebuild the layout as an animated scene in OUR style — our fonts, palette, textures and Vox-style motion — with the narration's real words and numbers; never copy the reference's look or content, never show it as a still, and vary layouts when reused. Method: MANUAL §6.1; worked examples: MANUAL §6 table + `expected/layouts/` + `templates/full-edit/`.
- **Sources:** use the same sources we used (`SOURCES_INDEX.md`, `example-docs/sources/`) and add new ones a story needs, following the sourcing playbook (MANUAL §8.1, `tools/find_media.py`). Free / public-domain / CC only, every file logged in SOURCES.md.
- **Textures:** always from texturelabs.org (MANUAL §3.4, `tools/prep_texture.py`). If you can't click its download button, give me the page links and I'll download them.
- **Sound:** synthesized marimba-led score + subtle per-object SFX (MANUAL §7, `tools/audio/`), never louder than the voice.
- **Editing new audio:** later I'll give you raw audio; you'll follow MANUAL §8 and `AGENT_BRIEFS.md` (analyst → planner → parallel asset gatherers → parallel segment editors → sound designer → assembly, review, render), starting with samples for my approval.

## Rules that always apply
- Never process the voiceover. On-screen text says exactly what the narrator says — no fact-checking; only fix misheard names.
- Only Cooper Hewitt, Haskoy and Crimson Pro. Only the palette in `lib/fx.css`. West = vermilion, East = navy; yellow only for the highlighter and one key number.
- Every on-screen word lands 0–120 ms before its spoken word.
- No logins, no account creation, no paid sources. Ask me before anything outward-facing.
- Keep this repo private (the Texturelabs textures can't be redistributed publicly).
- Commit and push often (cloud sessions can be paused and reclaimed); long renders run in the background.
- Keep `MANUAL.md` current: whenever you learn a technique, hit a gotcha, or I give feedback, update it and its Changelog, and commit.

Start with Step 0 now, and tell me briefly as each step finishes.
