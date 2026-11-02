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

## Fix round 1 (Krish, 2026-11-02 — `project/ivan/FIXES_ROUND1.md`)
- **Map labels (sc011, Warsaw → Ukraine):** POLAND, UKRAINE, RUSSIA in Haskoy 800 caps (+0.04 em), bone with a soft dark
  shadow, at the visual centre of each country in the final 0.6 framing (inside the map camera, so they stay on the land while the
  camera drifts), fade/rise 0.7 s at 12 fps from 716.85 and held to the cut; WARSAW city label (t-label beside the pin) kept.
  Belarus/Kyiv not labelled (not narrated). RUSSIA label is on Russian land before and after the oxblood fill (checked).
- **Crimea:** the Ukraine fill/outline uses the kit's `#c-ukraine` (includes Crimea) + `#c-crimea`; `#c-russia` excludes it.
  In this framing Crimea lies below the frame (frame bottom ≈ 47.4°N), so it is never seen; nothing in frame puts it in Russia.
- **Markers at full res:** sc013 focus brackets drifted ~38 px left of the double agent (bracket moved faster than the row) →
  now locked to the row's drift (centred, checked at 50.0 / 51.4 s local). sc021 officer and car brackets checked at full res: on target.
- **Face-cam edges:** every shot's first 0.35 s and last 0.75 s checked frame by frame at master time — no mouse reach, screen
  glance or post-line settling inside any shot. But two take joins of the trimmed VO fell inside shots (found by frame diff):
  master **706.450** (inside sc008) and **709.734** (inside sc009). Fixed: sc008 → sc009 hard cut moved to 706.465 (first 24 fps
  frame of the new take; sc009 media-start 706.465, lip sync unchanged) and the sc009 → sc010 whip moved to 709.70 (outgoing
  hidden at 709.742, before the join). sc010 starts 0.29 s earlier (Warsaw cue unchanged). The other joins (720.334, 773.733)
  are just before sc012 / sc024 start. Every face-cam `<video>` `data-duration` now ends at its scene's cut (timed media can
  outlive a hidden scene), so no frame of the next take can leak.
- SFX: the whip marker moved 709.99 → 709.70. Timeline still 105.790 s (headless check); lint 0 errors; sync_audit 0 flagged.
