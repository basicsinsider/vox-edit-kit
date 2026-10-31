# SEGMENTS — chunk c5 editor split + shared conventions

Three contiguous segments of ~200 s, cut at scene boundaries from `EDIT_NOTES.md` (C5S001–C5S124). One editor agent per segment builds `compositions/c5sNN.html`. Read first: `project/LONGFORM.md` (incl. the lead's **cross-chunk colour decision** at its end), `MANUAL.md` (§3–§5, §9, **§10.1–10.9 override**), `EDITOR_BRIEF.md`, `project/c5/EDIT_NOTES.md` §0 + your scenes, `ASSETS_NEEDED.md`, `DECISIONS.md`, and the approved intro (`compositions/intro0*.html`, `review/intro_720p.mp4`) — copy its code for every effect it already solved.

## 1. The split

| seg | VO range (local) | dur | scenes | acts | starts on | ends on |
|---|---|---|---|---|---|---|
| c5s01 | 0.00–194.22 | 194.22 | C5S001–C5S042 (42) | I, II, III | C5S001 Nanzih EPZ photo + pen tick (night) — cut-on-action continuation from c4's last EPZ shot | C5S042 1960 Taipei boulevard with diverging red/celadon arrows; light-flash whip begins @194.06 |
| c5s02 | 194.22–399.67 | 205.45 | C5S043–C5S083 (41) | IV, V, VI, VII | C5S043 "the 70s" odometer title on night, born out of the flash | C5S083 Kissinger–Zhou Enlai photo (July 1971); light-flash whip begins @399.51 |
| c5s03 | 399.67–598.03 | 198.36 | C5S084–C5S124 (41) | VIII, IX, X | C5S084 US forces in Taiwan (Vox layered) out of the flash | C5S124 blurred UN voting board, camera still pushing at 598.03 (c6 opens on the same board/hall) |

Total 124 scenes, 598.03 s, no gaps. (Full-audio offsets: c5s01 = 2679.14, c5s02 = 2873.36, c5s03 = 3078.81.)

### Boundary hand-offs (both editors honour them)
| boundary | t (local) | outgoing last frames | incoming first frames |
|---|---|---|---|
| c4→c5s01 | 0.00 | (c4's last shot — EPZ factory / export zone; the lead passes c4's last frame) | C5S001 opens on E01 Nanzih EPZ photo already pushing (1.00→1.05) so the chunk join reads as one continuous move; if c4's last shot is the same photo, match its scale/grade exactly |
| c5s01→c5s02 | 194.22 | C5S042: Taipei boulevard + arrows; `FW` light-flash whip starts @194.06 — smear right, peak bone flash on the boundary frame | C5S043: starts at the flash peak (bone frame) and resolves to the night "the 70s" title over 0.16 s; streaks already running. Share the flash curve (`FX.whip` light variant, seed 4300) |
| c5s02→c5s03 | 399.67 | C5S083: Kissinger–Zhou photo, `FW` starts @399.51 (smear up) | C5S084: lands from the same flash, panels drifting up (same direction). Seed 8400 |
| c5s03→c6 | 598.03 | C5S124: UN voting board, focus never resolves, push continues to the last frame | c6 planner/editor: open on the UN hall / board still moving (cut on action) — lead passes the last frame |

## 2. Shared continuity (things that must look identical across segments)

| motif | scenes (segments) | rule | master owner |
|---|---|---|---|
| **Colour code** (lead decision) | all | red `--vermilion` = PRC/CCP/Communist bloc (USSR = red hatch); celadon = Taiwan/ROC; navy = US & allies only where a contrast is needed; others neutral; yellow = highlighter / one key number. ≤ 2 accents per frame | all |
| **Taiwan relief + celadon fill** (map kit M07) | C5S010, C5S021, C5S034 ghost (01); C5S053 (02); Strait maps C5S089–093 (03) | same file, same grade, celadon fill + halftone + 6 px glow; ghost version at 15 % | c5s01 |
| **China red fill** (R12 look on M01) | C5S036 (01); C5S079 (02, beige map) | red fill + halftone + soft glow on the relief; on the beige R11 map flat red at 0.6 with watercolour edge | c5s01 (M01) / c5s02 (M06) |
| **Smile curve** (G01) | C5S016, C5S019 (01) | one SVG, same line weight; C5S019 is a wider crop | c5s01 |
| **D15 circles** (G09) | C5S031–032 (01); C5S062, C5S081–082 (02); C5S107 (03) | intro D15 style: 260 px circles, 8 px rings, `FX.markup.arrow`, t-label 22 px; ring colours by the code | c5s01 |
| **Halftone flags** (G13) | C5S044, C5S062, C5S076, C5S081 (02); C5S104 (03) | single-colour halftone (US navy, PRC red, ROC ink), same dot size, slight paper show-through | c5s02 |
| **Kissinger photo set** (N01–N06) | 02: C5S046, 049, 054, 078, 080, 083; 03: C5S110, 119, 120, 121 | one grade (cool sepia duotone), never the same photo in consecutive Kissinger scenes; crops for circles exported by c5s02 in its NOTES | c5s02 |
| **Secret-trip evidence** (PIA plane N44, clipping G06/N56, schedule G04) | C5S055–C5S065 (02) | the same three props reappear on the R9 board — build once, reuse | c5s02 |
| **Org chart / Sankey** (G16, G10) | C5S047–049 (02); C5S085 (03) | same flow width/opacity; c5s03 copies c5s02's Sankey snippet | c5s02 |
| **Newspaper column** (G06, §10.7) | C5S106 Bezos, C5S117 Bush, C5S122 callback (03) | one typeset column style (Crimson Pro body, Haskoy pull-quote, thin rules); no real masthead; C5S117 mirrors C5S106 (pan down, column left) | c5s03 |
| **UN seats / dots** (G08, G11) | C5S097, 099–101, 111, 114, 123 (03) | must match c3/c4's UN vote graphic (lead passes c4's spec); grey undecided dots, red CCP, celadon Taiwan | c5s03 |
| **Mao** | N11 2.5D C5S037 (01); N12 C5S061 (02), C5S102 (03) | red is allowed on him (PRC code); never the same image twice in a row | — |
| **Chiang Kai-shek** | N13 C5S035 (01), C5S102 (03); N14 C5S072 (02) | no name text (narrator says "Taiwanese leader") | — |
| **TV sets** | Tatung C5S014 (01), RCA C5S067 (02), Trinitron C5S087 (03) | never the same set twice in the chunk; CRT on/off per s04; scanlines off when pushing through | each |
| **Grid / ruled papers** | GRID scenes 005–006, 016, 019, 026 (01); 062 (02); 107, 114, 119 (03) | real scans `_hires` only; never the same paper file in consecutive light scenes | each |
| **Halate (hero only)** | made in Taiwan, United States, Fred Terman, Mao Zedong (01); the 70s, Henry Kissinger, July 1971, Mao Zedong, the Kissinger diplomacy (02); United Nations, George H.W. Bush (03) | one glowing element per frame; paper never glows | all |
| **Yellow key numbers** | `9 to 10%` C5S005 (01); `2 days` C5S056, `an hour` C5S069 (02); `2` C5S089 (03) | `--yellow` in a label box; everything else yellow = highlighter / the D14 marker route | each |

## 3. Shared conventions

### 3.1 Files and ids
- Composition `compositions/c5sNN.html` (NN = 01, 02, 03); composition id **`c5sNN`**. Root:
  `<div id="root" data-composition-id="c5sNN" data-vo-start="SEG_START" data-duration="DURATION" data-width="1920" data-height="1080">`
  with **SEG_START in LOCAL c5 seconds** (0.00 / 194.22 / 399.67). Build: `tools/build_master.py --prefix c5s --vo vo_c5.mp3 --len 598.03 --timeline assets/audio/c5/timeline.json`.
- Element ids prefixed `c5sNN-`, inside a scene `c5sNN-scNNN-` (scene number = the C5S number, e.g. `c5s02-sc058-plane`). One `<template>` with
  `<style>`, root div, `<script>` IIFE. No `font-family` in composition CSS (classes only). Asset URLs relative to the project root.
- Each scene: `<div class="scene" id="c5sNN-scNNN" data-scene="C5SNNN">`, full-frame, shown/hidden with `tl.set(…,{autoAlpha:1},S(start))` /
  `S(end)`; initial state with `gsap.set` outside the timeline (MANUAL §4.2); per-frame effects gated with `FX.gate` (wrap `FX.onFrame` while
  calling `FX.streaks`/`FX.weave`/`FX.roughDefs`).
- Don't edit `lib/fx.css`, `lib/fx.js`, `lib/palette.css`; new helpers live in your script and are reported to the lead.

### 3.2 Timing (LOCAL seconds)
```js
const SEG = "c5s02", SEG_START = 194.22, SEG_END = 399.67, DURATION = +(SEG_END - SEG_START).toFixed(2);
const T = (s) => +(s - SEG_START).toFixed(3);   // TEXT cues (audited) — s = LOCAL c5 time from EDIT_NOTES / transcript_c5.json
const S = T;                                     // STRUCTURAL cues (cuts, camera, objects) — not audited
const tl = gsap.timeline({ paused: true });
// FX.text.rise(tl, [el], T(213.26) - 0.06)
FX.mount(tl, DURATION);
window.__timelines = window.__timelines || {}; window.__timelines[SEG] = tl;
```
- Every text cue is a **literal** `T(<word start>)` from EDIT_NOTES; default −0.06. Word-by-word lines = one literal `T()` per word.
- When a scene's first cue is its first word, put that scene's cut at `S(word) − 0.06`.
- Easing `FX.choppy(FX.ease.out|inOut|in, dur, 12)`; camera `FX.ease.cam`; entrances 1.0–1.6 s, moves 1.2–2 s; last-0.6 s words use a 0.35 s entrance.
  No `back.out`, no short `power2/3.out` on big elements, `expo.inOut` only for C5S092's curve cut.
- **Key animation done + 0.5 s hold before every out** (EDIT_NOTES "Key anim done @t"). Check the last second of every scene in snapshots.
- Transitions: `FX.whipDefs` + `FX.whip(tl,a,b,S(t),{dir,vertical})` (~0.32 s, centred on the boundary), light-flash variant for `FW`;
  `CA` = cut while both shots move; `FX.focusHunt` once per scene max. **No `FX.iris`.** Deterministic only (`FX.rng(seed)`, seed = scene number × 100).

### 3.3 Voiceover in the segment
`<audio id="c5sNN-vo" class="temp-vo" src="vo_c5.mp3" data-start="0" data-duration="DURATION" data-media-start="SEG_START" data-volume="1">`
— the assembler strips `temp-vo` and plays one continuous `vo_c5.mp3`. Never process the VO. No music/SFX audio tags in segments. No face cam.

### 3.4 SFX markers → `compositions/c5sNN.sfx.json`
Array sorted by `t`, **LOCAL c5 seconds**: `{"t": 439.58, "type": "whoosh_big", "scene": "C5S092", "dur": 0.6, "level": "normal",
"note": "curve cut carrier → Strait"}`. Start from EDIT_NOTES' SFX lines, then correct to the frame the object actually moves. Vocabulary
(same as the intro): `whoosh_soft, whoosh, whoosh_big, air_swell, paper_slide, paper_rustle, paper_flip, paper_tear, page_turn, pop_soft, pin_pop,
map_pin, marker_scratch, marker_long, highlighter_swipe, pencil_scribble, stamp_thud, tick_soft, counter_ticks, odometer_tick, letter_ticks,
dot_ticks, dot_slide, projector_loop, projector_click, crt_click, crt_hum, crt_off, boom_low, burn_crackle, wind, lamp_click, gate_creak,
chime_soft, tone_blip`. Loops need `dur`. `level` ∈ soft | normal. The sound pass (`place_sound.py --vo vo_c5.mp3 --transcript transcript_c5.json
--len 598.03 --markers 'compositions/c5s0*.sfx.json' --out assets/audio/c5`) applies the §10.8 restraint pass.

### 3.5 Text & design rules (recap)
- Text = narration exactly; spellings fixed (General Instrument, Texas Instruments, RCA, Fred Terman, Mao Zedong, Henry Kissinger, Secretary of
  State, Taiwan Strait, Jeff Bezos, George H.W. Bush, CCP); no text on slips (BEATS §2b). Labels ≥ 22 px, captions ≥ 38 px, 96 px margins,
  one text animation at a time. Real documents keep their own printed words; our overlay text = his words only.
- Copyrighted material OK (fair use): credit 13 px bottom-right while on screen ("© owner"); CC BY(-SA) the same. Never strip watermarks.
- Default texture stack on every scene; light chromatic aberration 0.1–0.15 on photos/footage; no flat solid colour (fills under texture).

### 3.6 Checks before hand-off
1. `npx --yes hyperframes@0.8.217 lint` → 0 errors (sandbox: `tools/make_sandbox.sh c5sNN`).
2. `python3 tools/sync_audit.py compositions/c5sNN.html --transcript transcript_c5.json` → every text cue 0–120 ms before its word.
3. `npx --yes hyperframes@0.8.217 snapshot --at <every scene start+0.3, midpoint, end−0.6> --no-end -o .snap/c5sNN` and LOOK at each frame with
   the words under it (picture = words? key animation finished and holding before the cut?).
4. `compositions/c5sNN.sfx.json` valid; `compositions/c5sNN.NOTES.md` (deviations, exported motif snippets, asset fallbacks, photos used).

## 4. Assembly (lead)
`python3 tools/build_master.py --prefix c5s --vo vo_c5.mp3 --len 598.03 --timeline assets/audio/c5/timeline.json`, lint, contact sheet of every
scene midpoint with the transcript under each frame, picture render, fix, final render with sound → `renders/c5/c5_final.mp4` +
`review/c5_720p.mp4`; verify VO loudness in the final file equals `vo_c5.mp3`.

## 5. Scene list per segment

**c5s01** (0.00–194.22): C5S001 0.00, C5S002 2.19, C5S003 4.99, C5S004 7.23, C5S005 14.35, C5S006 20.59, C5S007 23.63, C5S008 29.79, C5S009 35.15, C5S010 38.59, C5S011 41.15, C5S012 45.15, C5S013 48.99, C5S014 51.39, C5S015 55.15, C5S016 61.44, C5S017 64.96, C5S018 67.44, C5S019 74.16, C5S020 81.76, C5S021 86.88, C5S022 90.08, C5S023 93.84, C5S024 100.80, C5S025 106.24, C5S026 113.36, C5S027 120.01, C5S028 125.13, C5S029 129.37, C5S030 132.49, C5S031 137.77, C5S032 141.85, C5S033 146.97, C5S034 153.85, C5S035 158.41, C5S036 163.77, C5S037 170.65, C5S038 176.30, C5S039 179.66, C5S040 183.34, C5S041 188.86, C5S042 191.10

**c5s02** (194.22–399.67): C5S043 194.22, C5S044 200.06, C5S045 205.82, C5S046 209.98, C5S047 214.62, C5S048 219.42, C5S049 222.46, C5S050 227.66, C5S051 231.58, C5S052 236.38, C5S053 242.03, C5S054 245.07, C5S055 248.83, C5S056 252.83, C5S057 258.75, C5S058 263.07, C5S059 267.95, C5S060 271.47, C5S061 276.11, C5S062 279.47, C5S063 284.03, C5S064 287.63, C5S065 291.07, C5S066 299.23, C5S067 305.82, C5S068 309.66, C5S069 314.94, C5S070 320.14, C5S071 325.34, C5S072 328.38, C5S073 332.30, C5S074 336.70, C5S075 342.70, C5S076 347.50, C5S077 353.02, C5S078 361.50, C5S079 368.63, C5S080 376.39, C5S081 382.63, C5S082 389.11, C5S083 396.31

**c5s03** (399.67–598.03): C5S084 399.67, C5S085 405.11, C5S086 411.11, C5S087 415.43, C5S088 418.79, C5S089 423.19, C5S090 427.27, C5S091 430.86, C5S092 434.06, C5S093 440.94, C5S094 445.50, C5S095 450.38, C5S096 454.22, C5S097 458.70, C5S098 462.62, C5S099 467.02, C5S100 473.18, C5S101 478.38, C5S102 484.78, C5S103 490.25, C5S104 493.45, C5S105 498.17, C5S106 503.53, C5S107 507.69, C5S108 513.77, C5S109 520.89, C5S110 524.17, C5S111 528.33, C5S112 532.81, C5S113 538.81, C5S114 544.33, C5S115 548.80, C5S116 554.00, C5S117 557.84, C5S118 565.52, C5S119 572.08, C5S120 577.44, C5S121 580.40, C5S122 583.76, C5S123 588.72, C5S124 592.48

