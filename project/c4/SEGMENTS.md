# SEGMENTS — chunk c4 editor split + shared conventions

Three contiguous segments of ~200 s, cut at scene boundaries from `EDIT_NOTES.md` (C4S001–C4S104). One editor agent per
segment builds `compositions/c4sNN.html`. Read first: `project/LONGFORM.md`, `MANUAL.md` (§3–§5, §9, **§10.1–10.9 override**),
`EDITOR_BRIEF.md`, `project/intro/BRIEF.md`, `project/c4/EDIT_NOTES.md` §0 + your scenes, `ASSETS_NEEDED.md`, `DECISIONS.md`,
and look at `review/intro_720p.mp4` (the approved look — c4 must feel like the same film).

All times are **LOCAL** c4 seconds (`vo_c4.mp3`, `transcript_c4.json`); full-audio time = local + 2077.72.

## 1. The split

| seg | VO range (local) | dur | scenes | acts | starts on | ends on |
|---|---|---|---|---|---|---|
| c4s01 | 0.00–199.14 | 199.14 | C4S001–C4S036 (36) | A, B, C, D (to "good economy") | real Security Council chamber, VETO hero (night) | 1935 bird's-eye painting of Taiwan, slow pan, GOOD ECONOMY (night) |
| c4s02 | 199.14–399.37 | 200.23 | C4S037–C4S069 (33) | D (end), E, F, G, H (start) | dark yield line over ghost Taiwan (night) | push THROUGH the 1960s airport doors (night) |
| c4s03 | 399.37–601.44 | 202.07 | C4S070–C4S104 (35) | H, I, J | university scrapbook collage (paper) | D12 dark list TAXES / REVENUES / JOBS, slow push-out into c5 (night) |

Total 104 scenes, 601.44 s, no gaps. (c4 → c5 hand-off: c5 opens "This actually did work… made in Taiwan" — c4s03's last
frame leaves the celadon bars of the D12 list on screen for the c5 editor to pick up.)

### Boundary hand-offs (both editors honour them)
| boundary | t | outgoing last frames | incoming first frames |
|---|---|---|---|
| c3 → c4s01 | 0.00 | (c3) the five permanent members listed — US, UK, France, China, Soviet Union | C4S001 opens on the real Security Council chamber with the five seats readable; no title card, no transition gimmick — a CA on a slow push (ask the lead for c3's last frame) |
| c4s01 → c4s02 | 199.14 | C4S036: the 1935 bird's-eye painting pans right→left (cam ease), still moving at 199.14; the painting's green paddies are in the lower third | C4S037: dark ground; the same painting continues for 2 frames then dissolves (on the pan's motion) into the ghost Taiwan + paddy footage at 12–15 % — a CA on the pan. c4s01 exports the painting's crop/position at 199.14 in `compositions/c4s01.NOTES.md` |
| c4s02 → c4s03 | 399.37 | C4S069: push-through the Songshan Airport doors — by 399.37 the doors fill 120 % of frame, motion blur on | C4S070: the push continues 0.25 s (scale 1.15 → 1.0, blur 6 → 0) landing on the university scrapbook collage (paper). Shared: push easing `FX.ease.cam`, blur values; c4s02 notes the exact door scale/blur at 399.37 |

## 2. Shared continuity (things that must look identical across segments)

| motif | scenes (segments) | rule | master owner |
|---|---|---|---|
| **Taiwan celadon fill** (relief + mask, watercolour edge, halftone, 6 px glow) | C4S010, 014, 017 (01); 037, 043, 046, 049, 053, 060, 066 (02); 078–079, 082, 095, 102 (03) | `assets/intro/maps/taiwan_relief_grey.jpg` + `taiwan_celadon_fill.png` / kit masks; celadon `#9fc7b2`, never text colour; same grade as the intro's IS035 | c4s01 |
| **CCP / China red fill** (R12 look: halftone + glowing edge) | C4S007–008, 010, 014, 017–020 (01); 066 (02); 096–097 (03) | `--vermilion` `#e03f2c` at the intro's map opacity rules (§4.2); red is the CCP in c4 only | c4s01 |
| **'CHINA' seat chair icon + seat-dots** | C4S002–003, 005 (desk), 010, 020 (01) | one SVG chair (ink line, nameplate 'CHINA'); seat dots 54 px like the intro's D06 board | c4s01 |
| **War-room map** (paper atlas world plate, pins, pen front line) | C4S022, C4S025 (01) | same plate, same pin sizes (celadon / red heads), C4S025 = wider crop | c4s01 |
| **Japanese-era photo set** (railway, port, hydropower, power lines, school) | C4S034–035 (01) → small prints in C4S038 folder (02) | same crops/tints; c4s01 exports the card set (paths + tint params) in its NOTES | c4s01 |
| **D15 land-reform diagram** (landowner / farmer / factory circles, parcels) | C4S051–052, 055 (02) + C4S059 icon style (02) | one layout, camera moves over it; ring 8 px, t-label 22 px, `FX.markup.arrow` | c4s02 |
| **Isotype pictograms** (people, graduates, generals, engineers) | C4S046 (02); C4S071, 082, 084, 090 (03) | one icon family (`assets/icons/graduate*.svg` style, ink on paper / bone on night), 12 fps fills | c4s02 (makes `assets/c4/icons/`) |
| **Pacific map** | C4S049 (02, ghost Sankey); C4S078–079 (03, night route) | `assets/intro/maps/pacific_relief_grey.jpg` (+json) / kit Pacific; same Taiwan/US pin positions | c4s02 |
| **1960 'Face of Free China' footage grade** | C4S024 (01); C4S037 ghost, 039, 057 (02); C4S085, 094 (03) | same grade: sat −0.6, contrast +0.1, chromaticAberration 0.12, weave amp 0.6 (it is 1960 colour film) | c4s01 |
| **Presidential Office footage** | C4S039 (02), C4S085 (03) | different sections of `taiwan_1960_presidential_office_taipei.mp4` (C4S039 first half, C4S085 second half) | — |
| **Chiang Kai-shek** | C4S021 (01, unnamed with Eisenhower); C4S088–089 (03, named) | no name label before 507.37 | c4s03 |
| **Screens** | Tektronix scope C4S023 (01); Tatung TV C4S103 (03) | `assets/intro/screens/*` with `*_screen.json`; CRT on/off per s04; no museum TVs | — |
| **Grid / ruled papers** | C4S012, 018, 029 (01); 046, 051–052, 059, 062 (02); 071, 081, 090, 097 (03) | real K+E scans or Texturelabs `_hires` graph/lined; never upscaled small scans; never vector grids; two paper layers | each |
| **Halate (hero only)** | VETO, GENERAL ASSEMBLY, THE CHINESE SEAT, AFRICA, SEISMIC, 1890s, POSITIVES (01); 1940, INDUSTRIALISTS, WHITE TERROR (02); BRAIN DRAIN, CHIANG KAI-SHEK, ENGINEERS, LATE 60s, EXPORT PROCESSING ZONES (03) | one glowing element per frame; paper never glows | all |
| **Yellow key numbers** | `11` (C4S002, 01), `1.5 billion` (C4S049, 02), `40 years` (C4S062, 02) | `--yellow`; all other yellow = highlighter | 01, 02 |

### Palette moments per segment
| seg | grounds | accents |
|---|---|---|
| c4s01 | archival UN night ↔ paper seat diagrams ↔ dark relief maps ↔ Japanese-era posters/collage | celadon Taiwan vs red CCP (Acts A–C); Act D neutral sepia with celadon only on Taiwan |
| c4s02 | dark charts/archival ↔ paper/grid diagrams (land reform) ↔ sombre night (White Terror) | celadon dominant; red only for Mao's China (C4S066–068); yellow 1.5 billion, 40 years |
| c4s03 | paper collages / §10.7 newspaper ↔ night maps ↔ paper flow diagrams | celadon Taiwan; red China only in C4S096–097; the end leans celadon (hand-off to c5's "made in Taiwan") |

## 3. Shared conventions

### 3.1 Files and ids
- Composition `compositions/c4sNN.html` (NN = 01, 02, 03); composition id **`c4sNN`**. Root:
  `<div id="root" data-composition-id="c4sNN" data-vo-start="SEG_START" data-duration="DURATION" data-width="1920" data-height="1080">`
  where `data-vo-start` is the **local** c4 start (0, 199.14, 399.37) — `tools/build_master.py --prefix c4s --vo vo_c4.mp3 --len 601.44`
  reads `data-vo-start` / `data-duration`.
- Element ids prefixed `c4sNN-`, inside a scene `c4sNN-scNNN-` (scene number = the C4S number, e.g. `c4s02-sc049-flow`).
  One `<template>` with `<style>`, root div, `<script>` IIFE. No `font-family` in composition CSS. Asset URLs relative to the
  project root (`assets/…`, `vo_c4.mp3`).
- Each scene: `<div class="scene" id="c4sNN-scNNN" data-scene="C4SNNN">`, full-frame, hidden outside its window
  (`tl.set(el,{autoAlpha:1},S(start))` / `tl.set(el,{autoAlpha:0},S(end))`; initial state via `gsap.set` outside the
  timeline, §4.2); per-frame effects wrapped in `FX.gate`.
- Don't edit `lib/fx.css`, `lib/fx.js`, `lib/palette.css`; new helpers live in your script and are reported to the lead.
- New c4 assets go to `assets/c4/<type>/` + `SOURCES.md` per folder (gatherers); derived files `assets/c4/derived/c4sNN/`.

### 3.2 Timing (LOCAL seconds)
```js
const SEG = "c4s02", SEG_START = 199.14, SEG_END = 399.37, DURATION = +(SEG_END - SEG_START).toFixed(2);
const T = (s) => +(s - SEG_START).toFixed(3);   // TEXT cues (audited) — s = local c4 word start
const S = T;                                     // STRUCTURAL cues (cuts, camera, objects) — not audited
const tl = gsap.timeline({ paused: true });
// FX.text.rise(tl, [el], T(269.39) - 0.06)
...
FX.mount(tl, DURATION);
window.__timelines = window.__timelines || {}; window.__timelines[SEG] = tl;
```
- Every text cue is a **literal** `T(<word start>)` from EDIT_NOTES (never `T(c)` over an array). Default −0.06 s.
- Easing: `FX.choppy(FX.ease.out|inOut|in, dur, 12)`; camera `FX.ease.cam`. Entrances 1.0–1.6 s, moves 1.2–2 s. No `back.out`,
  no short `power2/3.out` on big elements, no `expo.inOut` except C4S004's curve cut.
- **Hold**: every scene's key animation completes by its "Lock" time (scene end − 0.5 s) — check the last second of every
  scene in snapshots (§10.9).
- Transitions: `FX.whipDefs` + `FX.whip(tl, a, b, S(t), {dir, vertical})` (~0.32 s), light-flash for `FW`; `CA`/`HC` = cut
  while both shots move; `FX.focusHunt` once per scene max. **No `FX.iris`.**
- Deterministic only (`FX.rng(seed)`, seed = scene number × 100).

### 3.3 Voiceover in the segment
`<audio id="c4sNN-vo" class="temp-vo" src="vo_c4.mp3" data-start="0" data-duration="DURATION" data-media-start="SEG_START" data-volume="1">`
— the assembler strips `temp-vo` and plays one continuous VO. Never process the VO. No music/SFX audio tags in segments. No
face cam.

### 3.4 SFX markers → `compositions/c4sNN.sfx.json`
Array sorted by `t`, **local c4 seconds**: `{"t": 130.14, "type": "boom_low", "scene": "C4S023", "dur": 1.2, "level": "soft",
"note": "seismograph trace spikes"}`. Start from EDIT_NOTES' SFX lines, then correct to the frame the object actually moves.
Vocabulary (intro's + c4 additions): `whoosh_soft, whoosh, whoosh_big, air_swell, paper_slide, paper_rustle, paper_flip,
paper_tear, page_turn, pop_soft, pin_pop, map_pin, marker_scratch, marker_long, highlighter_swipe, pencil_scribble,
stamp_thud, tick_soft, counter_ticks, odometer_tick, letter_ticks, dot_ticks, dot_slide, projector_loop, projector_click,
crt_click, crt_hum, crt_off, boom_low, burn_crackle, wind, lamp_click, gate_creak, chime_soft, tone_blip,` **`circuit_clunk`**
(§10.6.3 contrast call-out). Loops need `dur`. `level` ∈ soft | normal. The sound pass applies the §10.8 restraint pass.

### 3.5 Text & design rules (recap)
- Text = narration exactly; spellings fixed (Mao Zedong, Chiang Kai-shek, NTU, National Taiwan University, Security Council,
  General Assembly, Warsaw Pact, Meiji, CCP, ROC); no text on slips (BEATS §2b); **no years on screen in C4S090** (unclear
  "15, 2"). Labels ≥ 22 px, captions ≥ 38 px, 96 px side margins, one text animation at a time.
- Palette tokens only; ≤ 2 accents per frame (c4 pair = celadon + red); yellow only highlighter / the scene's key number.
- Default texture stack on every scene (grain + dust + vignette; paper scenes add two paper layers). Copyrighted/CC BY
  assets: 13 px micro-credit bottom-right while on screen (e.g. "UN Photo", "© TIME, fair use", "Esri World Imagery").
- Real-image rule: prefer the TRUE image (§10.9). Missing asset (❌): closest true substitute or a typographic/graphic
  treatment — never a blank, never an invented "archival" photo; note it in your NOTES.

### 3.6 Checks before hand-off
1. `npx --yes hyperframes@0.8.217 lint` → 0 errors (sandbox: `tools/make_sandbox.sh c4sNN`).
2. `python3 tools/sync_audit.py compositions/c4sNN.html --transcript transcript_c4.json` → every text cue 0–120 ms before its word.
3. `npx --yes hyperframes@0.8.217 snapshot --at <every scene midpoint + start+0.3 + end−0.1> --no-end -o .snap/c4sNN`
   (snapshot times are composition-relative = local − SEG_START) and LOOK at each frame with its words under it.
4. `compositions/c4sNN.sfx.json` valid; `compositions/c4sNN.NOTES.md` for deviations, exported motif snippets, fallbacks.

## 4. Assembly (lead)
`python3 tools/build_master.py --prefix c4s --vo vo_c4.mp3 --len 601.44 --timeline assets/audio/c4/timeline.json`, lint,
contact sheet of every scene midpoint with the transcript under each frame, picture render, fix, final render with sound
→ `renders/c4/c4_final.mp4` + `review/c4_720p.mp4`; verify the VO loudness in the final file equals `vo_c4.mp3`.
