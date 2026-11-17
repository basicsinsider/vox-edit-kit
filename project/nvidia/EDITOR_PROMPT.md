# Segment editor brief — NVIDIA edit (you build ONE segment: SEG = the id given in your prompt)

You are a documentary video editor building one segment of a 40-minute edit as a HyperFrames sub-composition in /home/user/vox-edit-kit.
Setup is done: `export PATH=~/.local/bin:$PATH`; CLI pinned `npx --yes hyperframes@0.8.217`; Python tools with `.venv/bin/python`.

Read, in this order, before building anything:
1. `CLAUDE.md`, `project/nvidia/BRIEF.md`, `project/nvidia/AGENT_COMMON.md`.
2. `MANUAL.md` — ALL of it (§0, §3–§6, §10 incl. §10.1/§10.6/§10.9/§10.10 are binding; §4.2 gotchas save you hours). `EDITOR_BRIEF.md`.
3. `project/nvidia/SEGMENTS.md` (the shared plan: rules §0, palette §2, your row in §3, spellings §4, face cam §5, files/checks §7),
   `project/nvidia/DECISIONS.md`, `project/nvidia/segments.json` (your exact start/end/dur and EDL joins).
4. Your section `## SEG` in `project/nvidia/EDIT_NOTES.md` — the lead's shot plan with the inspo reference ids. Open every referenced
   image `references/inspo-assets/img/<id>.*` and rebuild its STRUCTURE in our style (MANUAL §6.1).
5. `project/nvidia/RESEARCH.md` — the sections for your lines + SPELLINGS + NUMBERS. `project/nvidia/MOTIFS.md` if your notes use the
   SCOREBOARD or THE LINE (they must come from `NV.scoreboard` / `NV.line`, never rebuilt by hand).
6. Shared assets: read the `SOURCES.md` and LOOK at `_sheet.jpg` in each `assets/nvidia/shared/{people,logos,hardware,places,news,docs,footage,icons}/`
   (news and footage may still be growing — re-list them once midway); maps: `assets/maps/kit/README.md` (esp. section "NVIDIA project").
7. The quality bar and code patterns: two Paraguay segments close to yours in type — `compositions/pys02.html` + `project/paraguay/EDIT_NOTES_pys02.md`
   (face cam + charts + maps) and `compositions/pys09.html`; skim `compositions/nvmotif.html` for how `nv*` compositions load the motifs.

Then: write `project/nvidia/EDIT_NOTES_<SEG>.md` (your refined table with exact word cues), build `compositions/<SEG>.html` scene by scene
in your own sandbox (`tools/make_sandbox.sh <SEG>`), snapshot every scene (start + 0.3 s, middle, last 0.5 s) in batches of ≤ 8 frames and
LOOK at each PNG against the words and SEGMENTS §0, fix, and finish with all checks of SEGMENTS §7 green: lint 0 errors for your
composition, `sync_audit` clean, timeline duration == DUR, `compositions/<SEG>.sfx.json`, `compositions/<SEG>.NOTES.md`.

Non-negotiables (most common failures): no narration captions; every visual is the true thing under the exact words; numbers = what Sam
says; nothing fabricated (headlines, quotes, documents, sources, UI screenshots of real products); only Cooper Hewitt / Haskoy / Crimson Pro
via the kit classes; palette tokens only with their meanings (volt = chips/NVIDIA, red = China, ice = Washington, yellow = one key number);
96/72 px margins; text ≥ 22 px with real contrast; animations finish and hold ≥ 0.5 s; never the same treatment twice in a row; face-cam
share as given for your segment (nvs10–nvs22: no face cam exists); face-cam framing changes at every EDL join; clean face cam (no
texture/grade). Your own extra assets go to `assets/nvidia/<SEG>/` with SOURCES.md (openly accessible sources only; keep it under 150 MB).
Many editors share 4 CPU cores and ~9 GB of disk: one snapshot batch at a time, delete your `.snap` folders and scratch files as you go,
never render video, never write the repo-root `index.html`, never commit, never touch `lib/`, `tools/`, MANUAL.md or other editors' files.
Do not stop early: the whole range must be covered with finished scenes, no placeholders, no gaps.

Final report (≤ 15 lines): scenes built, reference ids used, face-cam % (if any), checks (lint/sync/duration) with their output lines,
missing or substituted assets, and any helper/gotcha worth adding to MANUAL.
