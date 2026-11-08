# Prompt for Codex / Antigravity — edit the first 5 minutes of the Taiwan podcast in the house style

Copy everything between the two lines into Codex or Antigravity.

---

You are a documentary video editor working for Krish (channel: Searching Lessons). Your job: take the FIRST 5 MINUTES of
our latest Taiwan podcast cut and turn it into a fully edited Vox-style documentary segment — B-roll, maps, charts,
animated typography, call-outs, sound design — in exactly the house style we use, using the tools, assets and manual in
our GitHub repo. This is a test of whether you can match our quality, so follow the repo's manual to the letter.

## 1. Get everything (do this first, and check each item actually works — never assume)

**Repo 1 — the editing kit (private):** `https://github.com/basicsinsider/vox-edit-kit`, branch **`claude/paraguay-edit`**
(the newest kit: every tool, the full MANUAL, map kit, effects library, fonts, sound tools, render scripts). Clone it:
`git clone --depth 1 --branch claude/paraguay-edit https://github.com/basicsinsider/vox-edit-kit` (≈4 GB checkout).
Work on a NEW branch named `external/taiwan-pod-5min` and push your work there. Never push to any other branch.

**The source video (5 minutes):** `BB_podcast_v2_first5min.mp4` — the first 4:59 of our latest Taiwan podcast
cut (0:00–0:07 Sam and Sanket side by side, then Sam; it ends on a sentence): 1080p, 24 fps, two cameras edited together (Sam = host/narrator, Sanket = guest). The audio is already cleaned and
levelled. Download link: **https://gofile.io/d/Md3nAL2U** (156 MB, 4:59.000, md5 `db7c0d7ecdeebfa02551bb49ef6b3565` — check it after downloading). If you can't download it, ask Krish to put it at
`vox-edit-kit/input/BB_podcast_v2_first5min.mp4` — do not create accounts anywhere to get it.

**Epidemic Sound (music + SFX):** the API key is in the environment variable `EPIDEMIC_SOUND_MCP_API_KEY` (Krish sets it
as a secret in your environment settings). `tools/epidemic_mcp.py` reads it from there (or from `~/.secrets/epidemic_key`).
`.mcp.json` also defines the Epidemic MCP server (`https://www.epidemicsound.com/a/mcp-service/mcp`, header
`Authorization: Bearer ${EPIDEMIC_SOUND_MCP_API_KEY}`) if your tool supports MCP. Test one small search call first.
**Never write the key into any file, commit, log or message.**

**Tooling:** from `vox-edit-kit/` run `bash setup.sh` then `export PATH=~/.local/bin:$PATH`. It installs ffmpeg, zsh,
the Python venv (`.venv/bin/python` runs our Python tools), the pinned HyperFrames CLI (`npx --yes hyperframes@0.8.217 …`
— ALWAYS this exact version), its headless Chrome, its skills, and the Parakeet speech-to-text model (word timestamps).
Needs Node 22+, ~20 GB free disk, and network access to npm, cdn.jsdelivr.net, github.com, commons.wikimedia.org,
upload.wikimedia.org, archive.org, loc.gov, www.epidemicsound.com and the Esri/map tile hosts listed in MANUAL.
Report anything that fails to install instead of working around it silently.

## 2. Read before editing (in this order, fully)
1. `CLAUDE.md` — hard rules (they apply to you too).
2. `USER_BRIEF.md` — Krish's own words.
3. `MANUAL.md` — the style law. §0 non-negotiables; §4 HyperFrames gotchas; §5 effects catalogue; §6/§6.1 rebuilding
   reference layouts; **§10.1–§10.10 = Krish's latest rules and they override older sections** (§10.5 face-cam rules,
   §10.6 call-outs, §10.7 painting-to-print, §10.8 sound system, §10.10 design notes: grid placement, clean meaningful
   text, contrast); §11/§11.1 rendering. Read the Changelog — every line is a lesson already paid for.
4. `EDITOR_BRIEF.md`, `AGENT_BRIEFS.md`, `project/LONGFORM.md`.
5. Worked examples: `project/intro/` + `compositions/intro01–03.html` (the Taiwan intro — **this tells the same story as
   the first minutes of the podcast**: Robert Tsao, UMC, the foundry idea, the board, Morris Chang, TSMC, Hsinchu), then
   `project/ivan/` and `project/paraguay/` (raw face-cam → finished documentary, the newest process), and
   `compositions/c2s02.html` with its NOTES.
6. Watch the approved look: make contact sheets (ffmpeg) of `review/intro_720p.mp4` and `review/c1_720p.mp4`, and look
   at them. That is the quality bar.

## 3. The job
1. **The 5-minute file is your narration.** Use it as delivered. It's already cleaned: do NOT process its audio
   (no EQ/compression/gain/normalising — MANUAL §0). Never cut inside a word.
2. **Transcribe it** with Parakeet (`npx --yes hyperframes@0.8.217 transcribe …`, see MANUAL) to get word timings.
   - Fix ASR misspellings of names only: Robert Tsao, Morris Chang, UMC, TSMC, Hsinchu Science Park, Sam, Sanket,
     "Searching Lessons". On-screen text = exactly what is said, no fact-checking.
3. **Plan it like our projects:** BEATS, EDIT_NOTES (every scene: words → picture), SEGMENTS (~2.5-min segments),
   ASSETS_NEEDED, DECISIONS, in `project/pod5/`, copying the format of `project/intro/`.
   - Reuse the Taiwan intro's assets, motifs and ideas wherever the podcast says the same thing, but rebuild every scene
     to the podcast's exact words and timings.
   - Use the Taiwan palette `lib/palette.css`: red = TSMC/Morris Chang, blue = UMC/Robert Tsao, celadon = Taiwan,
     yellow = highlighter + one key number.
4. **On-camera rules** (the podcast cameras are the "face cam"):
   - No one on camera for the first 10 s.
   - In the first 1–2 min the speakers pop in on camera often, but only for 1–2 s each.
   - After that: ~35 % on camera, ~65 % edit (B-roll/graphics).
   - When someone is on camera, show whoever is speaking (Sanket whenever he speaks or reacts, as in the podcast cut); keep the cameras clean and modern (MANUAL §10.5).
5. **Edit in HyperFrames** (`compositions/pod5s01.html`, `pod5s02.html` …) using `lib/fx.js` / `lib/fx.css` effects,
   the map kit (`assets/maps/kit/`), the reference layouts, real archival images/footage (copyrighted OK under fair use,
   credited; log every asset in its folder's `SOURCES.md`), vintage papers.
   - Every visual must match the exact words under it.
   - Every on-screen word lands 0–120 ms before it is spoken (check with `tools/sync_audit.py`).
   - Halation only on each scene's hero element; rough reveals settle.
   - Long smooth eases; whip transitions (never the iris); cuts on action; DSLR focus hunts; every key animation
     finishes and holds ≥ 0.5 s before a cut.
   - Fonts: only Cooper Hewitt, Haskoy, Crimson Pro.
6. **QA:** lint 0 errors (`npx --yes hyperframes@0.8.217 lint`), sync audit clean, and LOOK at snapshots of every scene
   (start, middle, end) and fix what's wrong before rendering.
7. **Sound:** layered Epidemic bed, never one single track, in the "Melting Glass" family the Taiwan edit used (see
   `assets/audio/epidemic/LOG.md`, `project/intro/music_cuesheet.json`, MANUAL §10.8).
   - SFX are placed from each composition's `.sfx.json` markers with `tools/audio/place_sound.py`, then given a
     restraint pass.
   - Music sits ~14 LU under the voice; the voice's loudness must not change in the mix (measure it with
     `tools/audio/measure_mix.py`).
8. **Render fast and safely:** render each segment separately with `-w 3 -q draft --crf 18` (MANUAL §11), transcode,
   concatenate, then `tools/final_mix.sh` (VO at unity + beds).
   - Never kill a render for any reason.
   - Watch disk space before every big write.
9. **Deliver:**
   - Push the plan, compositions, notes and tools you add to `external/taiwan-pod-5min`.
   - Final 1080p MP4 + a 720p review copy: upload both to gofile.io (the owner's standing delivery rule — pick a server from
     `https://api.gofile.io/servers`, then `curl -F file=@… https://<server>.gofile.io/contents/uploadfile`), check the
     uploaded md5, and give Krish the links.
   - Never commit video files over 95 MB.
10. **Report:** what you built, scene list, assets used and what was missing, timings (setup, edit, render), and anything
    in the kit that didn't work for you.

## 4. Always
- Never assume — test every step, even with a tiny check, before relying on it or reporting it.
- Never log in to anything or create accounts.
- Never alter the voice audio.
- Never commit secrets.
- If something in the kit is unclear or broken, say exactly what and where instead of guessing.

---
