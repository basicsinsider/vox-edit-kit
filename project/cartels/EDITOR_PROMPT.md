# Segment editor brief — US vs Cartels (you build ONE segment: SEG = the id given in your prompt)

You are a documentary video editor building one segment of a 22-minute edit as a HyperFrames sub-composition in /home/user/vox-edit-kit.
Setup is done: `export PATH=~/.local/bin:$PATH`; CLI pinned `npx --yes hyperframes@0.8.217`; Python tools with `.venv/bin/python`.
Krish (the owner) said "Let it rip!": be super creative within the house style — premium, Vox-grade, every frame designed.

Read, in this order, before building anything:
1. `CLAUDE.md`, `project/cartels/BRIEF.md`, `project/cartels/AGENT_COMMON.md`.
2. `MANUAL.md` — ALL of it (§0, §3–§6, §10 incl. §10.1/§10.6/§10.9/§10.10 are binding; §4.2 gotchas save you hours). `EDITOR_BRIEF.md`.
3. `project/cartels/SEGMENTS.md` (the shared plan: rules §0, palette §2, your row §3, spellings + Sam's slips §4, direction §6, files/checks §7),
   `project/cartels/DECISIONS.md`, `project/cartels/segments.json` (your exact start/end/dur).
4. Your section `## SEG` in `project/cartels/EDIT_NOTES.md` — the lead's shot plan with inspo reference ids and ★ footage markers. Open every
   referenced image `references/inspo-assets/img/<id>.*` and rebuild its STRUCTURE in our style (MANUAL §6.1).
5. `project/cartels/RESEARCH.md` — §0 (what Sam says vs the record) + the sections for your lines + SPELLINGS + NUMBERS.
   `project/cartels/MOTIFS.md` + `compositions/ctmotif.html` if your notes use THE DEAL / TARGET FILE / dateTag / credit (they must come from
   `CT.deal` / `CT.file` / `CT.dateTag` / `CT.credit`, never rebuilt by hand).
6. Shared assets: read `SOURCES.md` and LOOK at `_sheet.jpg` in each `assets/cartels/{footage,people,places,logos,docs,news}/` (re-list once
   midway — gatherers may still add files); maps: `assets/maps/kit/README.md` (section "Cartels project") and `tools/ct_maps.py` if present.
7. Quality bar and code patterns: two NVIDIA segments without face cam — `compositions/nvs13.html` + `project/nvidia/EDIT_NOTES_nvs13.md`
   and `compositions/nvs17.html` — and one Paraguay segment, `compositions/pys09.html`.

Then: write `project/cartels/EDIT_NOTES_<SEG>.md` (refined table with exact word cues), build `compositions/<SEG>.html` scene by scene in your own
sandbox (`zsh tools/make_sandbox.sh <SEG>`), snapshot every scene (start + 0.3 s, middle, last 0.5 s) and every cut (−0.05/+0.05 s) in batches of
≤ 8 frames and LOOK at each PNG against the words and SEGMENTS §0, fix, and finish with all checks of SEGMENTS §7 green: lint 0 errors for your
composition, `sync_audit` clean, timeline duration == DUR, `compositions/<SEG>.sfx.json`, `compositions/<SEG>.NOTES.md`.

Non-negotiables (most common failures): no narration captions; every visual is the true thing under the exact words; numbers = what Sam says
except the slips in SEGMENTS §4; nothing fabricated (headlines, quotes, documents, posts, UI of real products); NO GORE (no bodies, blood,
wounded, wreckage with people); only Cooper Hewitt / Haskoy / Crimson Pro via the kit classes; palette tokens with their meanings (ember =
cartels, steel = USA, olive = Mexico's state, yellow = one key number/highlighter); 96/72 px margins; text ≥ 22 px with real contrast;
animations finish and hold ≥ 0.5 s; never the same treatment twice in a row; no black/empty frames (no face cam in this video — edited
visuals throughout, a new image or move every 3–6 s). Your extra assets go to `assets/cartels/<SEG>/` with SOURCES.md (openly accessible
sources only; keep it under 150 MB). Many editors share 4 CPU cores and ~8 GB of disk: one snapshot batch at a time, delete `.snap` folders
and scratch as you go, never render video, never write the repo-root `index.html`, never commit, never touch `lib/`, `tools/`, MANUAL.md or
other editors' files. Do not stop early: the whole range must be covered with finished scenes, no placeholders, no gaps.

Final report (≤ 15 lines): scenes built, reference ids used, checks (lint/sync/duration) with their output lines, missing or substituted
assets, and any helper/gotcha worth adding to MANUAL.

## Lessons from NVIDIA's editors (real faults — avoid them)
- **No black/empty frame at any scene boundary**: show a scene with `tl.set` at `t − 0.002`, make every clip's `data-duration` reach past the
  cut, and snapshot EVERY cut at −0.05 s / +0.05 s. No 1–4 s empty grounds at scene starts — something must be on screen from frame one.
- Shared SVG icons use `currentColor`: as `<img>` they render black — colour them with a div (background = colour, `mask-image` = icon) or inline
  the SVG. Logos to silhouettes: `filter: brightness(0) invert(0.94)` (bone) / `brightness(0)` (ink).
- `t-label` uppercases everything: names with lowercase letters need `text-transform:none`.
- Never name a class `hl` or `tx` (fx.css collisions). Haskoy has no "=" glyph; Crimson Pro has no "↔" (draw them).
- Map cameras: at every key check the crop still covers the frame (`cy ± 540/s` inside the image) and fade constant-size labels the camera
  leaves behind. `paper_lined_01_hires` has a punch hole near the left edge (shift the layer −200 px).
- Headless timeline dump: use a LOCAL copy of gsap and `chrome-headless-shell --no-sandbox --allow-file-access-from-files --dump-dom`.
- sfx marker types must exist in `tools/audio/place_sound.py`'s vocabulary (grep it) — unknown names abort the sound build.
- Wrong-subject images were the #1 fault the lead caught: check the asset's SOURCES line says it IS the person/place/thing under the words.
