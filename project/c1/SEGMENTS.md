# SEGMENTS — chunk c1 editor split + shared conventions

Three contiguous segments of ~200 s, cut at scene boundaries from `EDIT_NOTES.md` (C1S001–C1S105). One editor agent per
segment builds `compositions/c1sNN.html`. Read first: `project/LONGFORM.md`, `MANUAL.md` (§3–§5, §9, **§10.1–10.9 override**),
`EDITOR_BRIEF.md`, `project/c1/EDIT_NOTES.md` §0 + your scenes, `ASSETS_NEEDED.md` (IDs/paths), `DECISIONS.md`. The approved
intro (`compositions/intro0*.html`, `review/intro_720p.mp4`) is the look and quality bar; the old 10-minute edit
(`templates/full-edit/seg01–06.html`) holds working code for many of these scenes (s02 map, s06 newspaper, s07/2.5D quad,
s09 reveal, s10 garage, R1/R4/R5/R9/R10/R12 layouts) — copy, re-time to the new words, upgrade to the round-2/3 rules.

All times are **LOCAL c1 seconds** (`vo_c1.mp3`, `transcript_c1.json`; full audio = local + 275.06).

## 1. The split

| seg | VO range (local) | dur | scenes | acts | starts on | ends on |
|---|---|---|---|---|---|---|
| c1s01 | 0.00–208.43 | 208.43 | C1S001–C1S034 (34) | I, II, III, IV (Terman tease → Hoover → Twitter aside) | bone flash (from the intro's IS066) fading into the orchard painting, quote word by word | tweet card stamped TRUE REALITY; whip **down** starting @208.37 |
| c1s02 | 208.43–402.83 | 194.40 | C1S035–C1S070 (36) | IV (end), V, VI (to Terman's plan) | the 1891 entrance-exam sheet landing at the end of a downward whip (grid paper) | lamp-lit cork board, red string to the blank company card; camera push continuing (cut on action) |
| c1s03 | 402.83–602.86 | 200.03 | C1S071–C1S105 (35) | VI (end), VII, VIII, IX | pictorial Peninsula map, camera already pushing toward Palo Alto | 'cannot be best at everything' bars, `everything` struck; slow drift continues (c2 opens on it) |

Total 105 scenes, 602.86 s, no gaps.

### Boundary hand-offs (both editors honour them)
| boundary | t | outgoing last frames | incoming first frames |
|---|---|---|---|
| intro→c1s01 | 0.00 | intro IS066: streaks flare to bone on the last 4 frames | C1S001: frames 0–3 bone `#f2ede3` fading (FX.ease.out 0.25 s) into the painting; grain already on |
| c1s01→c1s02 | 208.43 | C1S034: `W↓` whip — tweet card + crossed ad smear downward from 208.37 (blurA heavy) | C1S035: exam sheet smears in from the top and lands sharp by 208.70 (`FX.whip` incoming half, `vertical:true`). Both editors use `FX.whip` defaults (0.32 s) so the halves meet |
| c1s02→c1s03 | 402.83 | C1S070: cork-board push (cam ease) still moving at 402.83; red string finished by 402.3 (hold ≥ 0.5 s) | C1S071: map plane enters already moving at the same push speed (scale 1.04→, cam ease), first pin at 405.39 |
| c1s03→c2 | 602.86 | C1S105: drift continues, no fade | c2 planner decides; note the drift direction (left→right, 12 px/s) in `c1s03.NOTES.md` |

## 2. Shared continuity (things that must look identical across segments)

| motif | scenes (segment) | rule | master owner |
|---|---|---|---|
| **Terman portraits** (R01 young 1920, N01 1970s, N02 1940s, E01 1955) | C1S003, 005, 024 (01); 049, 055, 056, 061, 070 (02); 074–075, 078, 091, 097–098, 105 (03) | same halftone/duotone recipe: sepia ink on paper, bone/sepia on night; never red. Cut-outs made once in `assets/c1/cutouts/` | c1s01 makes R01/E01 cut-outs; c1s03 makes N02 cut-out |
| **Hoover** (R02 young + NARA portrait, R03 painting, R04 Commerce) | C1S026, 027 (01); 036, 038–041, 045–046, 059–060 (02) | neutral sepia; the §10.7 column style of C1S046 = the same column style as C1S003 (copy c1s01's CSS) | c1s01 (column style), c1s02 |
| **§10.7 newspaper column** (typeset recreation) | C1S003 (01), C1S046 (02) | identical typography: Crimson Pro body 22 px, Haskoy caption small caps, rule frames, sepia newsprint + halftone_01, tilt −3°. No real masthead | c1s01 (exports snippet in `c1s01.NOTES.md`) |
| **Silhouette** (N05) | C1S025 (01); C1S064 (02) | one matte style: ink `#141b24` on paper / `#2a2e33` + bone rim on night | c1s01 |
| **Dark ghost world map** (N93 kit, D13 style) | C1S007 (01); C1S043, C1S047 (02) | same projection, ghost-land opacity, Stanford/valley glow (vermilion, R12 edge glow) | c1s01 |
| **Rand McNally 1920 railroad map** (E91, R10) | C1S021 (01); C1S057 (02) | same tilt (rotateX 28°, rotateZ −6°), same fat yellow marker style, navy East pins / vermilion Stanford pin | c1s01 |
| **Graduate icons** (R5) | C1S023 (01); C1S062 (02) | same icon files, size 54 px, ink → vermilion (best) → navy (East) | c1s01 |
| **US maps (s02 system + map kit)** | C1S011–012 (01); C1S101 (03) | same basemap grade; vermilion West fill 0.6, sky East 0.8 (MANUAL §4.2) | c1s01 |
| **Tweet card** (N51) | C1S029, C1S034 (01) | one element | c1s01 |
| **Two-student cards / s09 reveal** (E07, N03) | C1S064, 066, 069 (02); C1S075 (03) | same card frames, rough borders | c1s02 |
| **D15 relationship style** | C1S055 (02), C1S078 (03) | same circle size (220 px), pen arrows (`FX.markup.pen`, boil 4), t-label 22 px | c1s02 |
| **HP 200A** (N60/E60) | C1S073, C1S085, C1S087 (03) | same photo + grade; credit CC BY-SA if E60 | c1s03 |
| **Coins** (N61) | C1S074 coin stacks, C1S080, C1S082 flip (all 03) | same coin images and halftone | c1s03 |
| **Fantasia / Disney** (N36) | C1S079, C1S085 (03) | same poster crop | c1s03 |
| **Capitol / Washington** (N23) | C1S040 (01 — White House alt), C1S098, C1S104 (03) | different photos per scene if available | c1s03 |
| **Screens** | C1S054 1950s TV (02), C1S086 scope (03), C1S094–095 radar scope (03) | never reuse a set; CRT on/off per s04 | each |
| **Papers** | GRID scenes 005, 014, 019 (01); 035, 042, 050, 058 (02); 072, 076, 088, 093, 102 (03) | `_hires` Texturelabs only for full-frame; two layers (top 90 %); never the same paper in consecutive paper scenes | each |
| **Halate (hero only)** | 01: `is here`, `greatest`, `powerful`, `Silicon Valley`; 02: `Quaker`, `1925`, `SILICON VALLEY` (title), `Great Depression`, `1938`; 03: `AUDIO OSCILLATOR`, `DISNEY`, `garage` | one glowing element per frame; paper never glows | all |
| **Yellow key numbers** | 12 (C1S009), 90 % (C1S015), 1891 (C1S027) — 01; $100 (C1S069) — 02; 25 (C1S077), 800 (C1S093) — 03 | all other yellow = highlighter | each |

### Palette per segment
| seg | grounds | accents |
|---|---|---|
| c1s01 | painting/aerial night ↔ §10.7 column paper ↔ data paper/grid ↔ archival night | vermilion West/Stanford, navy East (Eli Lilly, East coast, Bell Labs/GE); yellow 12, 90 %, 1891 |
| c1s02 | grid/ledger ↔ painting & archival night ↔ collage paper | vermilion Stanford/Terman tags, navy MIT/East; yellow $100 |
| c1s03 | map/collage paper ↔ HP/garage night ↔ wartime documents ↔ Washington night | vermilion HP/Stanford, navy Harvard; yellow 25, 800 |

## 3. Shared conventions

### 3.1 Files and ids
- Composition `compositions/c1sNN.html` (NN = 01, 02, 03); composition id **`c1sNN`**. Root:
  `<div id="root" data-composition-id="c1sNN" data-vo-start="SEG_START" data-duration="DURATION" data-width="1920" data-height="1080">`
  with `data-vo-start` in **LOCAL** c1 seconds (0.00 / 208.43 / 402.83) — `tools/build_master.py --prefix c1s --vo vo_c1.mp3 --len 602.86`.
- Element ids prefixed `c1sNN-`, inside a scene `c1sNN-scNNN-` (scene number = the C1S number, e.g. `c1s02-sc041-seats`).
  One `<template>` with `<style>`, root div, `<script>` IIFE. No `font-family` in composition CSS. Asset URLs relative to the
  project root (`assets/…`, `vo_c1.mp3`).
- Each scene `<div class="scene" id="c1sNN-scNNN" data-scene="C1SNNN">`, hidden outside its window; per-frame effects gated with `FX.gate`.
- Don't edit `lib/fx.css`, `lib/fx.js`, `lib/palette.css`; new helpers live in your script and are reported to the lead.

### 3.2 Timing
```js
const SEG = "c1s02", SEG_START = 208.43, SEG_END = 402.83, DURATION = +(SEG_END - SEG_START).toFixed(2);
const T = (s) => +(s - SEG_START).toFixed(3);   // TEXT cues, LOCAL c1 seconds (audited)
const S = T;                                     // STRUCTURAL cues (cuts, camera, objects) — not audited
const tl = gsap.timeline({ paused: true });
// FX.text.rise(tl, [el], T(213.47) - 0.06)
FX.mount(tl, DURATION);
window.__timelines = window.__timelines || {}; window.__timelines[SEG] = tl;
```
- Every text cue is a **literal** `T(<word start>)` from EDIT_NOTES (never `T(c)` over an array). Default −0.06 s.
- Easing `FX.choppy(FX.ease.out|inOut|in, dur, 12)`; camera `FX.ease.cam`. Entrances 1.0–1.6 s, moves 1.2–2 s; no `back.out`,
  no short power eases on big elements, `expo.inOut` only in the curve cuts (C1S002, C1S017).
- **Hold rule**: key animation complete + ≥ 0.5 s hold before any transition (EDIT_NOTES §11.6 lists the tight scenes).
- Transitions: `FX.whipDefs` + `FX.whip(...)`; light-flash variant for `FW`; `CA`/`HC` on camera/secondary motion; `FX.focusHunt` ≤ 1 per scene. **No `FX.iris`.**
- Deterministic only (`FX.rng(seed)`, seed = scene number × 100).

### 3.3 Voiceover in the segment
`<audio id="c1sNN-vo" class="temp-vo" src="vo_c1.mp3" data-start="0" data-duration="DURATION" data-media-start="SEG_START" data-volume="1">`
— the assembler strips `temp-vo` and plays one continuous VO. Never process the VO. No music/SFX audio tags in segments. No face cam.

### 3.4 SFX markers → `compositions/c1sNN.sfx.json`
Array sorted by `t`, LOCAL c1 seconds: `{"t": 215.13, "type": "stamp_thud", "scene": "C1S036", "dur": 0, "level": "soft", "note": "ADMITTED stamp"}`.
Start from EDIT_NOTES' SFX lines, then correct to the frame the object actually moves; add a whoosh for each whip/flash you build.
Vocabulary: `whoosh_soft, whoosh, whoosh_big, air_swell, paper_slide, paper_rustle, paper_flip, paper_tear, page_turn, pop_soft,
pin_pop, map_pin, marker_scratch, marker_long, highlighter_swipe, pencil_scribble, stamp_thud, tick_soft, counter_ticks,
odometer_tick, letter_ticks, dot_ticks, dot_slide, projector_loop, projector_click, crt_click, crt_hum, crt_off, boom_low,
burn_crackle, wind, lamp_click, gate_creak, chime_soft, tone_blip`. Loops need `dur`. `level` ∈ soft | normal. The sound pass
(`tools/audio/place_sound.py --vo vo_c1.mp3 --transcript transcript_c1.json --len 602.86 --markers 'compositions/c1s0*.sfx.json'`)
applies the §10.8 restraint pass.

### 3.5 Text & design rules (recap)
- Text = narration exactly; names fixed (Fred/Frederick Terman, Lewis Terman, Herbert Hoover, Bill Hewlett, David Packard, HP,
  Bell Labs, General Electric, Board of Trustees, World War II, drug company, east); no text on slips (BEATS §2b) — especially
  never 'company' for the family (C1S055), never 1980 (C1S027), never 'leaving West' alone (C1S023).
- Labels ≥ 22 px, captions ≥ 38 px, 96 px side margins, one text animation at a time; palette tokens only, ≤ 2 accents/frame.
- Default texture stack on every scene; CC BY(-SA) and fair-use assets get a 13 px credit bottom-right while on screen.

### 3.6 Checks before hand-off
1. `npx --yes hyperframes@0.8.217 lint` → 0 errors (sandbox: `tools/make_sandbox.sh c1sNN`).
2. `python3 tools/sync_audit.py compositions/c1sNN.html --transcript transcript_c1.json` → every text cue 0–120 ms before its word.
3. `npx --yes hyperframes@0.8.217 snapshot --at <every scene midpoint + start+0.3 + end−0.1> --no-end -o .snap/c1sNN` — LOOK at each
   frame with the words under it; check every scene's last second (animation finished + held).
4. `compositions/c1sNN.sfx.json` valid; `compositions/c1sNN.NOTES.md` (deviations, exported motif snippets, asset fallbacks).

## 4. Assembly (lead)
`python3 tools/build_master.py --prefix c1s --vo vo_c1.mp3 --len 602.86 --timeline assets/audio/c1/timeline.json`, lint, contact
sheet of every scene midpoint with the transcript under each frame, picture render, fix, final render with sound →
`renders/c1/c1_final.mp4` + `review/c1_720p.mp4`; verify the VO loudness in the final equals `vo_c1.mp3`.
