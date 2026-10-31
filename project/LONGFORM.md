# Long-form brief — "Taiwan: the chip rivalry" (Searching Lessons), first hour after the intro

The owner (Krish) approved the intro (`compositions/intro0*.html`, `review/intro_720p.mp4`) — **that is the look and the
quality bar for every chunk.** Keep the whole video cohesive with it.

Read first: `USER_BRIEF.md`, `MANUAL.md` (all; **§10.1–10.9 are Krish's latest rules and override older sections**),
`project/intro/BRIEF.md` (rules still valid unless §10.9 relaxes them), `EDITOR_BRIEF.md`, `AGENT_BRIEFS.md`.

## Chunks (VO = `input/Final Full Audio.mp3`, cut with -c copy; local times start at 0)
| chunk | full-audio range | VO file | transcript (local times) | project folder | compositions |
|---|---|---|---|---|---|
| c1 | 275.06–877.88 | vo_c1.mp3 | transcript_c1.json | project/c1/ | c1s01…c1sNN |
| c2 | 877.88–1475.72 | vo_c2.mp3 | transcript_c2.json | project/c2/ | c2s01… |
| c3 | 1475.72–2077.72 | vo_c3.mp3 | transcript_c3.json | project/c3/ | c3s01… |
| c4 | 2077.72–2679.14 | vo_c4.mp3 | transcript_c4.json | project/c4/ | c4s01… |
| c5 | 2679.14–3277.14 | vo_c5.mp3 | transcript_c5.json | project/c5/ | c5s01… |
| c6 | 3277.14–3875.12 | vo_c6.mp3 | transcript_c6.json | project/c6/ | c6s01… |
Full transcript (absolute times): `project/transcript_full.json`.

## What changed vs the intro (MANUAL §10.9)
- **Copyrighted material allowed** (fair use: documentary commentary, transformed, credited). Use the TRUE images: real
  1950s–80s photos/footage/newspapers/magazine covers/press photos of the people, companies and events, logos.
- **No face cam** after the intro (the narrator said he'd do the rest off camera).
- **No Pinterest pack for these chunks**: reuse the 15 intro refs (`references/style-images/intro/D01–D15.jpg`), the 12
  original refs (`references/style-images/1–12`) and invent tasteful VARIATIONS of them; you may look for more references
  (Pinterest, Vox videos, editorial design) — describe each new idea in the plan. Keep everything cohesive with the intro.
- **Image reuse allowed when needed** (prefer new unique images).
- **Animations finish + hold ≥ 0.5 s before a cut.** No upscaled paper scans (use `assets/textures/paper_*_01_hires.jpg`).
  **Maps from `assets/maps/kit/`** (high-quality map kit) — never flat grey/beige relief.
- Everything else from the intro stays: every visual matches the exact words; accurate spellings; text 0–120 ms before its
  word; halation only on the hero element; rough reveals settle; long smooth eases (FX.ease.* + 12 fps); cut on action; whips
  (no iris); DSLR focus hunt; Vox call-outs (§10.6); painting-to-print reveal (§10.7) for quotes; paintings/posters as B-roll;
  vintage papers; better screens (Tatung/Trinitron/IBM 5154/oscilloscope in assets/intro/screens); palette (red TSMC/Morris
  Chang, blue UMC/Robert Tsao, celadon Taiwan; for the Silicon Valley part keep using it sensibly: one accent for the West /
  Stanford, navy for the East — say the mapping in the plan; yellow = highlighter + one key number).
- Sound: layered Epidemic bed (same family as the intro: `project/intro/music_cuesheet.json`, `assets/audio/epidemic/LOG.md`),
  restraint pass (§10.8), `tools/audio/place_sound.py`.
- The c1 story (Fred Terman, Stanford, Hoover, brain drain, Hewlett & Packard) is the same as the earlier approved 10-minute
  edit (`templates/full-edit/seg01–06.html`, `example-docs/*`, `expected/final_edit_720p.mp4`, rough cut
  `work/roughcut/roughcut.mp4`) — reuse their ideas/code and `example-docs/sources/` media lists, re-timed to the NEW words.

## Delivery per chunk
`renders/cN/cN_final.mp4` (1080p, VO at unity + beds) and `review/cN_720p.mp4`, rendered and QA'd separately.
