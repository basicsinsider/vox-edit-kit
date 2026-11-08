# pys06 — NOTES (segment editor, 2026-11-08)
Master 595.60–706.20 (110.60 s), composition `pys06`, 23 scenes. Plan: `project/paraguay/EDIT_NOTES_pys06.md` (scene table, words → picture).
Checks: lint 0 errors for pys06 (warnings only: duplicate_media_discovery for the repeated ueno logo / facecam src, file size);
`sync_audit` 0 flagged — every text cue is a literal `T(word start − 0.06)` and was cross-checked against the INTENDED word
(not only the nearest); timeline = 110.60 (FX.mount); snapshots of every scene (start/middle/end) looked at in `work/pys06/.snap/b1…b11`.

## Scenes (first / last)
- **First**: sc001 face cam W, fresh shot. The EDL join at 595.683 changes the picture at 595.725 (3 frames into the segment) → the first
  3 frames show a still of the face cam at 595.75 (`assets/paraguay/pys06/derived/facecam_595_75.jpg`); video starts at local 0.125.
- **Last**: sc023 — the Peña ↔ Ueno board pulled wide, plum government agencies stream deposits (teal coins) into the bank, camera pushing
  (power2.in) into the president ↔ bank string at the cut (hand-off motion into pys07 "with the benefit of hindsight").

## Effects / layouts used
light-flash whip ×3, whip ←/→ ×4, vertical whip ×3, hard cut / cut on action ×10 (never the same transition twice in a row) ·
**2.5D** (sc003: Peña cut-out in sash, title "PEÑA" tucked behind his shoulder, blurred plum far plate + DOF mid plate, parallax dolly,
focus hunt) · 3D card flip (sc002 capital → real cash, plum → teal banknote with guilloche) · flow diagram with seek-safe coins along
pre-sampled paths (sc004 paper, sc017 night, sc023 night) · isotype vault + stop-motion pinned rule cards + pen ring + blocked arrow
(sc007) · waffle 10×10 → one bank → 10 % cap → deal into 10 banks → one bank collapses (sc010, camera pull-back) · pie with a cracking
10 % cap line and a slice swelling to 30 % with a yellow counter (sc012) · typeset rule sheet: pen strike-throughs, word-by-word typing,
stop-motion "super, super, super" stamps (sc014), then the same sheet struck and pushed aside to reveal the money still flowing (sc017) ·
photo plates with duotone tint + pen circle on the real IPS sign (sc005), pen growth line on the ueno sign (sc016) · night connection board
(rings, gradient plum→teal string, sc021) · light streaks (sc002, sc021, gated) · texture stack (grain/dust/vignette per ground, none on face).
Yellow only on "10%" (sc010) and "30%" (sc012). Halate only on the one hero per night scene (real cash, PEÑA, IPS, 30%).

## Face cam — 35.96 s of 110.60 = **32.5 %**
sc001 W 4.60 · sc006 M 2.72 · sc008 W 6.40 · sc009 C 2.42 · sc011 M 2.08 · sc013 W 1.92 · sc015 M 5.38 · sc018 W 4.48 · sc020 M 2.56 ·
sc022 C 3.40. No face shot crosses an EDL join (joins 595.683, 619.333, 657.733, 659.733, 681.133 — 619.333/657.733/659.733 sit exactly
at face-shot edges, 681.133 inside B-roll). Shot edges checked frame by frame (all mid-speech; no reaching/settling). sc013 is 1.92 s
(it lives between two joins 2.0 s apart). Text on W/M shots = lower-left lower-third on a scrim (Ivan pattern), none on C.

## Deviations / decisions
- On-screen numbers are his words: "10%" and "roughly 30%" (press: IPS ≈ 11 % — RESEARCH §1). IPS shown as "IPS" + the real sign.
- "Two years ago … protesting": a real Oct 2024 protest at IPS (Corriente Sindical Clasista, against IPS money going to ueno while Peña was a
  ueno Holding shareholder — ABC Color 16 Oct 2024) — matches both the date and the subject. New asset, logged in `assets/paraguay/pys06/SOURCES.md`.
- The "rule sheet" (sc014/sc017) is a typeset prop in our type with HIS words ("cannot have 10% of the whole fund with any single bank",
  "a condition … cannot really put your money with banks that are not super, super, super safe") — not a recreation of the real law.
- sc015 text "really big / and stable" skips "really, you know," (filler) — the words shown are his, in order.
- Asset reuse across segments: `pena_sash_crop.jpg` is also a small card in pys05 sc004 and (duotone) in pys07 sc002; `pena_portrait_reuters.jpg`
  is pys05 sc005. Here they are the 2.5D hero and the board portrait — lead may want to vary pys07's opening card.

## For the lead / MANUAL gotchas
- `tools/build_index.py` only discovers `seg|intro|ivs|c\d+s` composition ids — **`pys*` is not found** (the sandbox index comes out empty).
  I ran a patched copy (regex `(?:seg|intro|ivs|pys|c\d+s)\d+`) from my scratchpad instead of editing the shared tool; please add `pys` (and `py`)
  to the regex in `tools/build_index.py`.
- Lint flags `getPointAtLength` inside callbacks: for objects flowing along curves, sample each path into 61 points at build time (on a
  temporary path in the defs svg) and interpolate in a proxy tween's onUpdate — seek-safe and lint-clean (`flow()` in pys06).
- A coin/particle loop driven by `u = (t·speed + offset) mod 1` must stay hidden until `u` first wraps through 0 (`live = u_total ≥ (1−offset) mod 1`),
  otherwise particles pop up mid-path on the first frame.
- `remove-background` on a single portrait photo ran in 0.7 s (1.4 fps) — fine for 2.5D subjects; feather the cut-out's side edges with a
  linear mask when the source photo crops the arms, and give the mid (DOF) plate a radial mask or its rectangle shows.
- An EDL join a few frames after a segment start: cover the frames before it with a still of the first post-join frame (no lip-sync shift).

## SFX
`compositions/pys06.sfx.json` — 57 markers (master seconds), one HERO per scene + whips/pushes/entrances. Types used: whoosh, whoosh_soft,
whoosh_big, card_flip, boom_low, air_swell, pop_soft, marker_long, marker_scratch, dot_ticks, dot_slide, pin_pop, stamp_thud, paper_slide,
paper_rustle, paper_tear, gate_creak, counter_ticks, typewriter, crowd (= crowd_room alias). No bleeps in this segment.
