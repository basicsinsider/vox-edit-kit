# ivs06 — NOTES (master 675.59–781.38, 105.79 s, 25 scenes)

Plan: `project/ivan/EDIT_NOTES_ivs06.md`. Built from `project/ivan/gen/ivs06_template.html` →
`python3 project/ivan/gen/build_ivs06.py` (inlines the grey-man path and the map borders) → `compositions/ivs06.html`.
**Edit the template, not the built file.** Derived assets: `project/ivan/gen/ivs06_assets.py`.

## Checks
- Lint (0.8.217, sandbox): **0 errors** for ivs06 (19× `nested_media_start_basis_ambiguous` + file-size warnings, same as every segment).
- `sync_audit.py compositions/ivs06.html --transcript transcript_iv.json`: **0 flagged**. Every text cue is `T(word) − 0.06`.
- Headless harness (gsap + fx.js + template, seek 0→105.7): no errors, `tl.duration()` = **105.790**, no tween past the end.
- Snapshots of every scene (start/middle/end + transitions) looked at against the words. Contrast checked: night captions sit
  over a bottom scrim; face-cam text is always in an ink box (the wall is bright); Mamoń's name gets a stronger corner scrim.
- Hold rule (§10.9): key animations finish ≥ 0.5 s before their cut (highlighter 682.55 / whip 683.11; stamps 695.5; card split
  705.75; map fills 719.89 / whip 720.39; double agent 726.24; last bubble 745.8; police brackets 761.65 / whip 762.18; torch
  772.65, car exit 773.38 is the cut-on-action).

## Face cam: 36.0 s of 105.79 s = **34 %**
10 shots, framing changes each time: sc001 medium 1.25 · sc003 close 1.5 · sc007 medium 1.3 · sc008 wide 1.0 with a graphic
behind him (remove-background) · sc009 close 1.55 · sc012 wide 1.06 · sc015 medium 1.35 · sc018 medium 1.25 · sc022 close 1.55 ·
sc024 wide 1.0→1.04. Slow 2–4 % push inside every shot. No texture/grain on him (grain/dust/vignette off in face scenes).
Face-cam `<video>`s use `assets/facecam/ivan_facecam_master.mp4` with `data-media-start` = master second of the scene start
(no offsets added — lead measures lip sync).

## Effects / layouts used
Slide (paper over face cam), whips ×9 (left/right/vertical), light-flash whips ×3, hard cuts on action, push-through a print
into a map, case-file card + typewriter + body-size highlighter (ref 9 variation), framed "phone video" print, passport stamp
page (new layout: exit → abroad → entry stamps, our own drawings, no words or real marks), face-cam ink label boxes (§10.5),
**graphic behind the narrator** (grey man splitting azure | oxblood = "working for Russian intelligence, too?"), night map
(padded Eastern-Europe kit: Warsaw pin, dashed route, travelling dots, Ukraine sky fill, Russia oxblood fill), isotype row of
7 grey men with CCTV focus brackets and an oxblood flip (ref 5 variation), lower-third name, typeset phone (unanswered thread,
date dividers, typing dots, reply bubble glow — ours, no real app UI), photo focus brackets, **X-ray scanner** reveal of the
package in the boot (hero glow) + **torch focal call-out** that never reaches the boot, car exits on action, final slow push.
Palette: oxblood = Russia (Kaliningrad/Russia fill, Russian authorities, double agent), azure/sky = Ukraine (Ukraine fill,
"Ukraine", "Ukrainian"), brass only for the highlighter, Ivan always ash.

## First / last scene (hand-off)
- First (675.59): face cam medium, fresh shot, static slow push. ivs05 ends however it likes — this opens clean.
- Last (777.38–781.38): Ivan's silhouette on the ferry, slow push-in still moving at 781.38 (1.0→1.1); ivs07 opens fresh.

## Text decisions
- ASR fixes on screen: "devil agent" → **double agent**; "Mamon" → **Marcin Mamoń** (Haskoy renders ń — checked in a snapshot).
- No text on "I'm pretty sure" (only "Russia's security services"), nor on the slip "He had met Russian who…" (map caption
  "helping volunteers"). "Marcin" in the name label is not spoken — it is a name label on his first on-screen appearance.

## Assets (all logged in `assets/ivan/ivs06/SOURCES.md`, 24 MB)
9 BBC "Shadowmen" clips (cropped to remove logo, AI-anonymisation tags and burned subtitles), Commons police photo
(CC BY-SA 4.0, credited on screen) and Lada side view (CC0), padded EE night map + borders, Lada cut-out + X-ray plate,
face-cam remove-background pair for sc008.

## For the lead
- **`tools/build_index.py` does not pick up `ivs*` compositions** (its regex is `(?:seg|intro|c\d+s)\d+`): the sandbox
  index came out empty ("[] total -0.5") and every snapshot was blank. I used a private copy with `ivs` added
  (`/tmp/ivs06/build_index_iv.py`); please add `ivs` to the regex in `tools/build_index.py` (I did not edit shared tools).
- `tools/make_sandbox.sh` does not link `vo_iv.mp3` / `transcript_iv.json` into the sandbox (lint error `audio_src_not_found`);
  I symlinked `work/ivs06/vo_iv.mp3` by hand.
- Gotcha for MANUAL §4.2: **never name a class `tx`** — fx.css `.tx` is the texture overlay (`position:absolute; inset:-40px`);
  label text inside a box jumped 40 px up/left. (Same family as the `.hl` collision.)
- Gotcha: `hyperframes remove-background … -b bg.webm` returns the **full original frame** as bg (the person is still in it),
  not an empty room plate — fine for the "plate → graphic → fg" stack as long as the graphic sits beside, not behind, the body.
- remove-background ran at 0.3 fps here (129 frames in 469 s) on the shared box — budget ~8 min per 4 s.
- SFX markers: `compositions/ivs06.sfx.json` (56 markers, one hero per scene). New marker type used: `scanner_sweep` (exists for c3).
