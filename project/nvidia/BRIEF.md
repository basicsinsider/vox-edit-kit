# Brief — "NVIDIA" documentary, Searching Lessons
Owner: Krish. Written by the NVIDIA lead session, 2026-11-16, from the session brief. Branch `claude/nvidia-edit`
(starts from `claude/podcast-aroll-edit`, the newest kit: Taiwan, Ivan, Paraguay, Podcast, §10.8 Music limits,
`references/inspo-assets/`). Process = Paraguay (`project/paraguay/`): clean the raw footage into an EDL-cut narration
(improvisation-aware), then edit. Quality bar: Paraguay / Ivan. MANUAL.md applies in full; this file adds to it.

## Inputs
Drive folder https://drive.google.com/drive/folders/1elvzZNJ_FUME1yOgDLr2Hl6QpSRakGwt — used in order part 1 → 2 → 3.
`curl -sSL -C - -o <out> "https://drive.usercontent.google.com/download?id=<ID>&export=download&confirm=t"` → `input/nvidia/` (gitignored).

| Part | File | Size | Drive id |
|---|---|---|---|
| 1 | `part 1.mp4` | 3.48 GB | 1Fx5-X_bwA6azoTCEFNML75wxW800r79o |
| 2 | `part 2.wav` | 264 MB | 15y2cCgoiDTyCubFQ3q0aXl9xt6jWPKfI |
| 3 | `part 3.mp4` | 414 MB | 1SiQrCt7tJDC975jQqI444kYHadyhqTg4 |

- **Part 2 is audio only.** Krish confirmed (2026-11-16): no face cam for part 2 → narration with edited visuals
  throughout, usual density, never a black screen. (The `.pkf` in the folder is a Premiere peak file; ignored.)
- **No script.** The narration is the script: Parakeet transcript, improvisation kept. Remove errors, ums, ahs, false
  starts, retakes, long dead pauses. Cuts only — the voice is never processed. Face cam stays in sync; punch-ins hide jump cuts.

## Krish's rules (binding)
1. **Run it like Paraguay**: full documentary edit throughout — B-roll, maps, charts, call-outs, sound design. Face cam
   (MANUAL §10.5 + Paraguay practice): no narrator on camera for the first 10 s; short 1–2 s pop-ins in the intro; then
   ≈ 35 % on camera / 65 % edit (parts 1 and 3 only; part 2 has no camera).
2. **References**: `references/inspo-assets/` (57 images, INDEX.md, assets.json, contact sheets). Use only those that fit
   this story; every visual matches the exact words under it; facts, names, numbers correct. Rebuild in our style
   (MANUAL §6/§6.1). The plan notes which reference id inspired each scene.
3. **Music much lower than the voice**: current §10.8 Music limits (≥ 20 LU under in 3 s windows, never < 18, bed VO − 22,
   no pause lifts). Measure (`vo_music_scan.py`, `act_levels.py`, `measure_mix.py`) and report the numbers with the 720p.
4. **New palette** fitting NVIDIA's story, distinct from Taiwan, Ivan, Paraguay, Podcast → `lib/palette_nvidia.css`,
   swatch `references/palette_nvidia.png`. Same three fonts. Show Krish; keep working while waiting.
5. **Deliverables**: 720p review on gofile.io first → after approval the 4K on gofile.io. Check the md5 after each upload;
   remind him to download soon.
6. **No narration captions** (MANUAL §0, Paraguay review).

## Model split (Krish: save tokens)
- Lead: transcript, EDL decisions, story structure, all plans and creative decisions, palette, reference choice, snapshot QA, final checks.
- Segment editors, asset gatherers, sound designer: Agent subagents with model "opus", each with a complete brief.
- Render helpers: `create_session` with model `claude-sonnet-5-5`; they only run `tools/render_piece.sh` and push parts.
  A helper that fails twice on one segment is retried on `claude-opus-5-5`.

## Owner rules, always
- Never assume — test, even with a tiny check, before relying on it or telling Krish.
- Never kill a running render, for any reason.
- The machine shuts down when the session goes idle: no long job between turns; blocking waits; heavy work on helpers/agents.
- Render fast via helpers (MANUAL §11/§11.1, Paraguay 4K notes). Watch the disk before every big write.
- Commit and push to `claude/nvidia-edit` often. Never commit or print keys. Never log in or create accounts.
- Epidemic Sound: network secret for www.epidemicsound.com (proxy-injected); `tools/epidemic_mcp.py` takes a dummy
  (`epidemic_live_dummy`). Tested 2026-11-16: `SearchRecordings '{"query":{"term":…},"first":2}'` returns tracks.

## Order of work
1 credentials ✅ → 2 "started" + part 2 question ✅ (answered: no face cam) → 3 download + transcribe → 4 EDL + clean
narration, report length → 5 plan → 6 palette swatch → 7 choose references → 8 editors + gatherers (Opus) → 9 sound →
10 snapshot QA → 11 render (Sonnet helpers), 720p on gofile → 12 after approval 4K on gofile.
