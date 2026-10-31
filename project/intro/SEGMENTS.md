# SEGMENTS — intro editor split + shared conventions

Three contiguous segments, cut at scene boundaries from `EDIT_NOTES.md` (IS001–IS066). One editor agent per segment builds
`compositions/introNN.html`. Read first: `project/intro/BRIEF.md`, `MANUAL.md` (§3–§5, §9, **§10 overrides**),
`EDITOR_BRIEF.md`, `EDIT_NOTES.md` §0 + your scenes, `ASSETS_NEEDED.md` (paths/usage), `DECISIONS.md`.

## 1. The split

| seg | VO range | dur | scenes | acts | starts on | ends on |
|---|---|---|---|---|---|---|
| intro01 | 0.00–92.13 | 92.13 | IS001–IS022 (22) | 0, I, II, III, IV (first half) | `1983` odometer title, night | D06 board semicircle, blue "excited", YES stamp hovering; camera starts tilting down (paper) |
| intro02 | 92.13–185.01 | 92.88 | IS023–IS043 (21) | IV (end), V, VI, VII | footnote "* one condition" at the bottom of the same paper | Morris Chang reveal + TSMC logo; torn-paper wipe entering from the right (night) |
| intro03 | 185.01–275.06 | 90.05 | IS044–IS066 (23) | VIII, IX, X | torn-paper fight poster BETRAYAL → RIVALRY (paper) | through the Trinitron screen into streaks; flash-out to chunk 1 (night) |

Total 66 scenes, 275.06 s, no gaps.

### Boundary hand-offs (both editors honour them)
| boundary | t | outgoing last frames | incoming first frames |
|---|---|---|---|
| intro01→intro02 | 92.13 | IS022: D06 semicircle (all blue) with the YES stamp hovering; camera tilt **down** begins @91.9 (y +0 → +180 px by 92.13, cam ease) | IS023: same paper sheet, same semicircle visible at the **top** of frame (offset −180 px), the tilt continues down to the footnote over 0.6 s. intro01 exports the semicircle + stamp markup/CSS as a snippet in `compositions/intro01.NOTES.md`; intro02 copies it verbatim |
| intro02→intro03 | 185.01 | IS043: Chang portrait (red) + TSMC logo; a torn paper edge (`FX.roughDefs` torn-edge mask, paper_cream) starts entering from the right @184.80 and covers ~35 % of frame by 185.01 | IS044: the same torn paper edge at 35 % finishing its slide to cover the frame in 0.25 s, revealing the fight-poster layout. Share the torn-edge mask file and seed (`seed 4344`) |

## 2. Shared continuity (things that must look identical across segments)

| motif | scenes (segments) | rule | master owner |
|---|---|---|---|
| **Board semicircle (D06)** — 12 seat-dots | IS022 (01); IS032, IS035 ring (02); IS024 board circle uses 3 of the dots (02) | same dot size (54 px), arc radius, spacing; grey `#9a958c` empty → blue `#1d5c9e` excited → back to grey; same t-serif title style; 12 fps fills | intro01 |
| **Silhouette of the executive** (N38) | IS024, IS025, IS027, IS029, IS030, IS041 (FC1 nameplate), IS042 (02/03) → becomes Chang at IS043 | one SVG/PNG matte, neutral ink `#141b24` on paper / `#2a2e33` with bone rim-light on night; **never red, never a recognisable face** before 180.69. The IS043 burn reveal starts from exactly this matte over E24 `chang_2018.jpg` | intro02 (makes `assets/intro/cutouts/silhouette_exec.png`) |
| **Relationship diagram (D15)** | IS024, IS027, IS042 (02) | same circle size (260 px), ring colours (blue Tsao, grey board/executive, neutral US), same arrow + label style (`FX.markup.arrow`, t-label 22 px) | intro02 |
| **Tsao idea card** (grid-paper card, "1983" stamp, factory→products sketch, "novel concept" highlight) | IS014 (01); IS036, IS040 (02) | one card element; IS036 drops it; IS040 overlays it on the new company's plan. intro01 exports the card as a self-contained snippet (HTML+CSS) in its NOTES | intro01 |
| **Tilted vintage Pacific map (D10)** | IS006 (01), IS028 (02) | same map files (E30 formosa 1943 close-up, E31 pacific relief) + json, same tilt (rotateX 28°, rotateZ −8°), same dashed ink route style and celadon Taiwan fill; IS028 uses a wider crop | intro01 |
| **Taiwan relief (R12) + celadon fill** | IS002 panel (01); IS035 (02); IS053, IS049 behind FC3 (03) | `assets/intro/maps/taiwan_relief_grey.jpg` + mask; celadon `#9fc7b2` fill with halftone_01_norm + 6 px glow; same grade | intro02 (IS035) — intro01 uses a flat crop |
| **Dinner-table collage (NY)** | IS030, IS042 (02) | build once (IS030), IS042 is a camera move over the same layout | intro02 |
| **Red/blue rivalry lines (D13)** | IS045, IS046 FC2 behind him, IS050 "rivalry" split word (03) | same two stroke colours/weights; red `#e03f2c` Chang/TSMC, blue sky `#9fc3e3` on night | intro03 |
| **Chang / Tsao portrait circles** | IS052, IS056 (03) | same crops, ring widths (8 px), halftone; Chang red, Tsao blue | intro03 |
| **Progress bar / chapter list** | IS062, IS063 (03) | same bar style, total `4:26:14` | intro03 |
| **TV sets** | IS060 Tatung, IS065 Sony Trinitron (03) | never reuse a set (and not the four museum TVs of the 10-min edit); CRT on/off per s04; **the face cam never goes inside a TV** (no grade on him) | intro03 |
| **Grid / ruled papers** | IS007–008, IS014 (01); IS019 (01); IS026, IS036, IS040 (02); IS052 (03) | real scans from `assets/intro/papers/` (N10a–c); multiply over paper_cream; never a vector-drawn grid | each, same files |
| **Face cam** | IS041, IS046, IS049, IS057, IS059, IS061 | clean (no texture/grade/vignette on the face-cam layers — put the scene's grain/dust *under* the narrator cut-out or omit); text uses `.clean`; graphics behind him only between bg plate and fg | intro02 (#1), intro03 (#2–#6) |
| **Halate** | hero only: 1983, insight, the world (01); most respected, NEW YORK, on top of the world, 1984, MORRIS CHANG (02); SUPERPOWER, SEARCHING LESSONS (03) | one glowing element per frame; paper never glows | all |
| **Yellow key numbers** | `6×` (IS008), `25,000` (IS026) | `--yellow`; all other yellow is highlighter | 01, 02 |

### Palette moments per segment
| seg | grounds | accents |
|---|---|---|
| intro01 | night titles + 1960s archival plant footage ↔ grid-paper charts ↔ paper diagrams | blue Tsao/UMC dominates; celadon Taiwan; yellow 6× + highlighters; **no red** |
| intro02 | paper diagrams ↔ dark mystery (silhouette) ↔ posters/maps | blue Tsao; grey executive; celadon Taiwan 1984; **red appears only at 180.69** |
| intro03 | red vs blue everywhere; face cam; night maps; paper collage | red + blue pairs (max two accents — celadon only where neither red nor blue is on screen, except the two tiny park plots in IS053) |

## 3. Shared conventions

### 3.1 Files and ids
- Composition `compositions/introNN.html` (NN = 01, 02, 03); composition id `introNN`. Root:
  `<div id="root" data-composition-id="introNN" data-vo-start="SEG_START" data-duration="DURATION" data-width="1920" data-height="1080">`
  (`tools/build_master.py --prefix intro --vo vo_intro.mp3 --len 275.06` reads `data-vo-start` / `data-duration`).
- Element ids prefixed `introNN-`, inside a scene `introNN-scNNN-` (e.g. `intro02-sc035-relief`). One `<template>` with
  `<style>`, root div, `<script>` IIFE. No `font-family` in composition CSS (classes only). Asset URLs relative to the
  project root (`assets/…`, `vo_intro.mp3`).
- Each scene: `<div class="scene" id="introNN-scNNN" data-scene="ISNNN">`, full-frame, hidden outside its window
  (`tl.set(el,{autoAlpha:1},S(start))` / `tl.set(el,{autoAlpha:0},S(end))`); per-frame effects wrapped in `FX.gate`.
- Don't edit `lib/fx.css`, `lib/fx.js`, `lib/palette.css`; new helpers live in your script and are reported to the lead.

### 3.2 Timing
```js
const SEG = "intro02", SEG_START = 92.13, SEG_END = 185.01, DURATION = +(SEG_END - SEG_START).toFixed(2);
const T = (s) => +(s - SEG_START).toFixed(3);   // TEXT cues (audited)
const S = T;                                     // STRUCTURAL cues (cuts, camera, objects) — not audited
const tl = gsap.timeline({ paused: true });
// FX.text.rise(tl, [el], T(93.65) - 0.06)
...
FX.mount(tl, DURATION);
window.__timelines = window.__timelines || {}; window.__timelines[SEG] = tl;
```
- Every text cue is a **literal** `T(<word start>)` from EDIT_NOTES (never `T(c)` over an array). Default −0.06 s.
- Easing: `FX.choppy(FX.ease.out|inOut|in, dur, 12)`; camera `FX.ease.cam` (smooth). Entrances 1.0–1.6 s, moves 1.2–2 s.
  No `back.out`, no short `power2/3.out` on big elements, no `expo.inOut` except IS005's curve cut.
- Transitions: `FX.whipDefs` + `FX.whip(tl, a, b, S(t), {dir, vertical})` (~0.32 s), light-flash variant for `FW`; `CA`
  = cut while both shots move; `FX.focusHunt` once per scene max. **No `FX.iris`.**
- Deterministic only (`FX.rng(seed)`, seed = scene number ×100).

### 3.3 Voiceover in the segment
`<audio id="introNN-vo" class="temp-vo" src="vo_intro.mp3" data-start="0" data-duration="DURATION" data-media-start="SEG_START" data-volume="1">`
— the assembler strips `temp-vo` and plays one continuous VO. Never process the VO. No music/SFX audio tags in segments.
Face-cam video: `<video muted …>` (the VO is the only voice track), `data-media-start` = VO time − 0.026 s for
`input/Face Cam.mp4`, or the pre-cut's local offset (clip `fc_X.mp4` starts at VO X — verify lip sync in a snapshot pair).

### 3.4 SFX markers → `compositions/introNN.sfx.json`
Array sorted by `t`, absolute VO seconds: `{"t": 180.67, "type": "burn_crackle", "scene": "IS043", "dur": 1.4,
"level": "soft", "note": "silhouette burns into Morris Chang"}`. Start from EDIT_NOTES' SFX lines, then correct to the frame
the object actually moves. Vocabulary: `whoosh_soft, whoosh, whoosh_big, air_swell, paper_slide, paper_rustle, paper_flip,
paper_tear, page_turn, pop_soft, pin_pop, map_pin, marker_scratch, marker_long, highlighter_swipe, pencil_scribble,
stamp_thud, tick_soft, counter_ticks, odometer_tick, letter_ticks, dot_ticks, dot_slide, projector_loop, projector_click,
crt_click, crt_hum, crt_off, boom_low, burn_crackle, wind, lamp_click, gate_creak, chime_soft, tone_blip`. Loops need `dur`.
`level` ∈ soft | normal. (No `shutter` — the iris is retired.)

### 3.5 Text & design rules (recap)
- Text = narration exactly; spellings fixed (Robert Tsao, Morris Chang, UMC, TSMC, Hsinchu Science Park, Sam, Searching
  Lessons); no text on slips (BEATS §2b). Labels ≥ 22 px, captions ≥ 38 px, 96 px side margins, one text animation at a time.
- Palette tokens from `lib/palette.css` only; ≤ 2 accents per frame; yellow only highlighter / the scene's key number.
- Default texture stack on every non-face scene; CC BY(-SA) assets get a 13 px micro-credit bottom-right while on screen.
- Photos/clips: check the usage column in ASSETS_NEEDED before reusing anything (max 2 per chunk).

### 3.6 Checks before hand-off
1. `npx --yes hyperframes@0.8.217 lint` → 0 errors (sandbox: `tools/make_sandbox.sh introNN`).
2. `python3 tools/sync_audit.py compositions/introNN.html --transcript transcript_intro.json` → every text cue 0–120 ms before its word.
3. `npx --yes hyperframes@0.8.217 snapshot --at <every scene midpoint + first/last 0.1 s> --no-end -o .snap/introNN` and LOOK
   at each frame with the words under it (does the picture match the words?).
4. `compositions/introNN.sfx.json` valid; `compositions/introNN.NOTES.md` for deviations, exported motif snippets, asset fallbacks.

## 4. Assembly (lead)
`python3 tools/build_master.py --prefix intro --vo vo_intro.mp3 --len 275.06 --timeline assets/audio/intro/timeline.json`,
lint, contact sheet of every scene midpoint with the transcript under each frame, picture render, fix, final render with
sound; verify the VO loudness in the final file equals `vo_intro.mp3`.
