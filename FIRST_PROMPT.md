You are taking over a documentary video-editing style that another Claude Code session built and the owner (Krish) approved. This repository is the complete kit: the style manual, an effects library, tools, Krish's visual references, studied tutorial reels, templates, assets and a test voiceover. Your only job for now is to learn the style and prove it by rebuilding the approved samples. Do nothing else until I approve them.

## Step 0 — Read before acting
Read these fully, in order: `CLAUDE.md`, `MANUAL.md` (every section — it is the style law; every rule in it is a decision I already made), `SAMPLES.md`, `EDITOR_BRIEF.md`. Then skim `example-docs/` and `templates/full-edit/` (the planning documents and code of the approved 10-minute edit — the quality bar). Look at every image in `references/style-images/` and every contact sheet in `references/reels/` (with `references/reels/REELS.md`, the narration transcripts of the tutorial reels that define each technique). Then look at `expected/*.sheet.jpg` (the approved samples) and `expected/layouts/*.jpg` (how each of my reference images was rebuilt in our style).

## Step 1 — Set up the environment
Run `bash setup.sh` from the repo root, then `export PATH=~/.local/bin:$PATH`. It installs: ffmpeg + ffprobe, zsh, the HyperFrames CLI pinned at 0.8.217 plus its Chrome and its agent skills (`/hyperframes`, `/hyperframes-core`, `/general-video`, `/hyperframes-animation`, `/media-use`, `/hyperframes-audio`, `/hyperframes-cli`), the Parakeet speech-to-text model, a `.venv` with numpy/scipy/pillow/soundfile (use `.venv/bin/python` for every Python tool), the three fonts, and **Agent Reach** (https://github.com/Panniantong/Agent-Reach — used to download and watch Instagram reels through its bundled yt-dlp at `~/.local/share/uv/tools/agent-reach/bin/yt-dlp`). Node 22+ must exist; install it if it doesn't. Then run `npx hyperframes@0.8.217 doctor`. If the HyperFrames skills were just installed and aren't loaded in your session, read them directly from `~/.claude/skills/*/SKILL.md` and their `references/` — at minimum `hyperframes-core`.
If anything fails (cloud sandboxes often block sites such as Instagram, archive.org, Wikimedia or the HyperFrames registry), tell me exactly what failed and continue with what the repo already contains: every reel is already studied in `references/reels/` and every sample asset is in `assets/`.

## Step 2 — Environment check
Run `python3 tools/build_index.py && npx hyperframes@0.8.217 lint` (expect 0 errors), then `tools/render_samples.sh s01 s03 s10` and compare the results in `renders/samples/` with `expected/`. This only proves the machine renders correctly; it is not the test.

## Step 3 — The test: rebuild all 11 approved samples yourself
`SAMPLES.md` lists them: the 10 original samples plus the markup sample (s11) added later — each with its exact voiceover window, narration, required content and which of my points it shows. Move the approved compositions aside first: `mkdir -p _approved && git mv compositions/s*.html _approved/` (keep them for comparison afterwards, but do NOT open them while building). Then rebuild each sample from scratch into `compositions/` with the same file names and composition ids (s01…s11), using `MANUAL.md`, `SAMPLES.md`, `lib/fx.js` / `lib/fx.css`, `tools/`, `assets/`, `transcript.json` (exact word times) and the references. For s02 use `tools/gen_s02.py` with its template, as the manual describes. Work one sample at a time:
1. write it;
2. `python3 tools/build_index.py sNN && npx hyperframes@0.8.217 lint`;
3. `npx hyperframes@0.8.217 snapshot --at <key moments> --no-end -o .snap/sNN` and LOOK at the frames; fix layout, timing and readability;
4. `python3 tools/sync_audit.py compositions/sNN-*.html` (every on-screen word lands 0–120 ms before its spoken word);
5. `tools/render_samples.sh sNN`;
6. compare with `expected/sNN-*.sheet.jpg` and `expected/sNN-*.720p.mp4`; list the differences and fix the ones that matter.
If you are truly stuck on one technique, you may consult the matching file in `_approved/`, but tell me which sample and what you looked at.

When all 11 are done, build one reel of them (back to back, as the manual describes) and report to me: for each sample, how close it is to the approved version, what you couldn't match and why, and anything in `MANUAL.md` that was unclear or wrong. Fix the manual (with a Changelog line), commit everything to a branch, tell me what you committed, and then STOP and wait for my feedback. Do not start any other work.

## Things you need to know for later (no action now)
- I often send reference images (charts, maps, boards, collages — like the 12 in `references/style-images/`). Every time, you rebuild their layout as an animated scene in OUR style — our fonts, palette, textures and Vox-style motion — using the narration's real words and numbers, never copying the reference's look or content and never showing it as a still. The method is `MANUAL.md` §6.1, and §6's table plus `expected/layouts/` show how each of my first 12 references was done. Always vary a layout when it's reused.
- Later I will give you raw audio to edit; the full process is `MANUAL.md` §8 and you'll follow it then, starting with samples for my approval.

## Rules that always apply
- Never process the voiceover. On-screen text says exactly what the narrator says — no fact-checking; only fix misheard names.
- Only Cooper Hewitt, Haskoy and Crimson Pro. Only the palette in `lib/fx.css`. West = vermilion, East = navy; yellow only for the highlighter and one key number.
- Every on-screen word lands 0–120 ms before its spoken word.
- No logins, no account creation, no paid sources. Ask me before anything outward-facing.
- Keep this repo private (the Texturelabs textures can't be redistributed publicly).
- Keep `MANUAL.md` current: whenever you learn a technique, hit a gotcha, or I give feedback, update it and its Changelog, and commit.

Start with Step 0 now, and tell me briefly as each step finishes.
