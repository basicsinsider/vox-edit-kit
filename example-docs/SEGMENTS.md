# SEGMENTS — parallel editor split + shared conventions

Six contiguous segments, cut at scene boundaries from `EDIT_NOTES.md`. One editor agent per segment builds
`compositions/segNN.html`. Read first: `MANUAL.md` (§3–§5, §9), `EDIT_NOTES.md` §0 (text policy), your scenes in
`EDIT_NOTES.md`, the samples listed in your scenes' **Copy** field, and `ASSETS_NEEDED.md` for paths.

## 1. The split

| seg | VO range | dur | scenes | acts | starts on | ends on |
|---|---|---|---|---|---|---|
| seg01 | 0.00–100.25 | 100.25 | SC001–SC017 (17) | 0, I, II (first half) | streaks, night | R11 beige map, paper (iris closes on NY @100.10) |
| seg02 | 100.25–206.27 | 106.02 | SC018–SC034 (17) | II (end), III (Hoover origin + power) | shutter montage, night | Stanford-today curve cut, night |
| seg03 | 206.27–296.23 | 89.96 | SC035–SC047 (13) | III (reforms), IV (Terman intro) | R6 tuition chart, paper | 2.5D campus + FREDERICK TERMAN, night |
| seg04 | 296.23–398.46 | 102.23 | SC048–SC062 (15) | IV, V (the Eastern blueprint, part 1) | "born 1900", paper | MIT VI-A bulletin, paper |
| seg05 | 398.46–496.92 | 98.46 | SC063–SC077 (15) | V (part 2: Bush, taboo, mind palace), VI (return West) | curve cut lab→factory, night | graduation footage (heartbreak), night |
| seg06 | 496.92–600.00 | 103.08 | SC078–SC094 (17) | VI (1938, Hewlett & Packard, the plan) | R5 isotype students, paper | fade/hold on garage, night |

Total 94 scenes, 600.00 s, no gaps. Segment boundaries are hard cuts already planned in EDIT_NOTES (the outgoing
scene's "Motion → next" describes the hand-off; the incoming editor builds the first frames to match it).

### Boundary hand-offs (both editors must honour them)

| boundary | t | outgoing last frames | incoming first frames |
|---|---|---|---|
| seg01→seg02 | 100.25 | SC017: shutter iris closes on the navy New York fill (shutter SFX @100.10) | SC018: iris **opens** on the NYC 1921 skyline (use `FX.iris` with the iris already closed at local t=0, opening over 0.15 s) |
| seg02→seg03 | 206.27 | SC034: Stanford-today aerial still zooming, a paper card begins sliding in from the right in the last 6 frames | SC035: paper chart card finishing that slide (start it at x=+180 px, settle in 0.3 s) |
| seg03→seg04 | 296.23 | SC047: 2.5D dolly, hard cut on "He" | SC048: paper, clean hard cut in |
| seg04→seg05 | 398.46 | SC062: camera pushing into the GE cut-in photo (A30) | SC063: curve cut starts on **the same photo** at the matching scale (A30 at ~1.6×) |
| seg05→seg06 | 496.92 | SC077: a graduate silhouette freezes | SC078: the same silhouette (as an A39 pictogram) is the first icon of the row |

## 2. Shared continuity (things that must look identical across segments)

| motif | scenes (segments) | rule | owner of the "master" |
|---|---|---|---|
| **US map camera space** (Blue Marble desat, us_overlay paths, Mississippi, West/East regions) | SC007, SC008 (seg01); SC032 (seg02); SC042, SC043 (seg03); SC075 (seg05) | same basemap file, same CSS grade `brightness(0.82) contrast(1.08) saturate(0.7)`, same overlay colours (West vermilion overlay 0.55, East navy overlay 0.5), same pin style (bone dot + halo, Stanford/Lilly yellow ring), same cloud set. Copy s02's camera div and grade verbatim. | seg01 (SC007) — export the map CSS/pin markup as a snippet in seg01 notes; others copy |
| **Grey relief map (R12)** | SC008 (seg01), SC075 (seg05) | same A43 relief file + grade; the filled state uses halftone_01_norm + a 6 px glow (`filter: drop-shadow`) — Indiana **navy**, California **vermilion** | seg01 |
| **R10 old maps** | SC053, SC056 (seg04), SC085 (seg06) | same yellow marker (`--yellow`, multiply, rough filter, 28 px stroke, 12 fps draw), same yellow circle and vermilion numbered pin (Haskoy number on vermilion disc, bone ring), same 3D tilt (rotateX 18°, rotateZ −6°) | seg04 |
| **SILICON VALLEY title** | SC002 (seg01), SC055 (seg04) | identical lettering: `t-display halate`, 200 px, tracking 0.02em, centred; SC055 is the same element then roughens/chokes away | seg01 |
| **BRAIN DRAIN lettering + dot flow** | SC020, SC032 (seg02) | same rough ink lettering; same dot size/speed; dots turn navy when they cross the Mississippi line | seg02 |
| **Graduate pictogram (R5)** | SC033 (seg02), SC078 (seg06) | the same A39 SVG, same size (56 px), same three colour states (ink/vermilion/navy, grey for "stays") | seg02 makes `assets/cutouts/icons/graduate.svg`; seg06 reuses |
| **Shutter montage of Eastern companies** | SC018 (seg02), SC084 (seg06) | same plates and grade; SC084 is faster (iris every ~1.7 s) | seg02 |
| **Stanford timeline axis** (ink axis + travelling vermilion dot + tick labels in `t-label`) | SC041, SC044 (seg03), SC052 (seg04) | same y-position (top 935 px), same dot (24 px vermilion), same tick style (s08) | seg03 |
| **Cork board (R9)** | SC066, SC074 (seg05) | one board layout: SC066 is the close-up crop of SC074's wide board — build SC074's full board once and frame SC066 as a camera crop of it | seg05 |
| **2.5D worlds** | SC023 (seg02), SC047 (seg03), SC086 + SC094 (seg06) | same perspective (1200 px), same layer math `{z, scale:(P−z)/P}`, same haze/ray treatment; each dolly ≤ 8 s | s10 is the reference |
| **TV sets** | SC015 (seg01) Predicta · SC030 (seg02) 1930s cabinet · SC051 (seg04) 1950s portable · SC067 (seg05) 1940s console | never reuse a set; same CRT treatment (power-on scaleY 0.012→1 + white flash, scanlines, chromaticAberration, crtCurvature, glare), same `crt_click`/`crt_hum`/`crt_off` SFX | s04 |
| **Hoover photos** | seg02 (SC021–SC034) | young = `hoover_young_1898.jpg`; public figure = NARA portrait; 1920s = Commerce photos. Same sepia grade as s07 | seg02 |
| **Terman photo** | SC047 (seg03), SC052, SC065, SC066, SC074 (seg04–05) | one portrait source (A21 young Terman, else 1955) and one card style (s08) everywhere | seg03 picks the file; others reuse |
| **Hewlett / Packard** | SC080, SC081, SC083, SC093 (seg06) | same cutouts as s09 | seg06 |
| **Halate yellow** | key numbers only: 12 (SC005), 90% (SC013 box), 1891 (SC023), late 1910s (SC040), HERE (SC043), a good start (SC046), 1938 (SC079), $100 (SC082), money (SC092) | `.halate.yellow` / `--yellow`; never more than one yellow element per frame | all |

### Palette moments (per segment)

| seg | dominant ground mix | accent emphasis |
|---|---|---|
| seg01 | night titles/maps ↔ paper charts | vermilion West rises (bars, burn); one navy (Lilly); yellow: 12, 90% |
| seg02 | warm sepia nights (archival Hoover) ↔ paper collage | vermilion markups (X, stamp); navy for East destinations; yellow highlighter on NYT, 1891 |
| seg03 | historic: documents & money on paper ↔ dark weave | vermilion tuition bar, strike-throughs; yellow: late 1910s, HERE, good start |
| seg04 | cooler, East-tinted (navy family) — MIT, Boston | yellow marker lines (R10); navy pins for East institutions |
| seg05 | cork + paper ↔ dark labs | red string (vermilion); warm lamp at "mind palace"; vermilion California returns at the end |
| seg06 | minor dip → momentum; garage warmth | vermilion for Stanford/Palo Alto; navy for Packard leaving East; yellow: 1938, $100, money |

## 3. Shared conventions (every editor)

### 3.1 Files and ids
- Composition file: `compositions/segNN.html` (NN = 01…06). Composition id: `segNN`. Root:
  `<div id="root" data-composition-id="segNN" data-vo-start="SEG_START" data-duration="DURATION" data-width="1920" data-height="1080">` (the assembler `tools/build_master.py` reads `data-vo-start` and `data-duration`).
- **Every element id** is prefixed `segNN-` and, inside a scene, `segNN-scNNN-` (e.g. `seg03-sc041-axis`). CSS ids follow the same names.
- One `<template>` with `<style>`, root div, `<script>` IIFE (copy any sample's skeleton). No `font-family` in composition CSS — use
  fx.css classes. Asset URLs relative to project root (`assets/…`).
- Each scene is a container `<div class="scene" id="segNN-scNNN" data-scene="SCNNN">` absolutely positioned full-frame; visibility is
  driven by the one segment timeline (`tl.set(el,{autoAlpha:1},T(start))` / `tl.set(el,{autoAlpha:0},T(end))`). Keep scenes outside
  their window hidden so layout/paint cost stays low.
- New per-segment assets you make go to the folders given in ASSETS_NEEDED.md; do not edit `lib/fx.css` / `lib/fx.js` — if a new
  helper is needed, put it in your segment's script and tell the lead (it may be promoted to fx.js later).

### 3.2 Timing: the `T()` cue helper
```js
const SEG = "seg03", SEG_START = 206.27, SEG_END = 296.23, DURATION = +(SEG_END - SEG_START).toFixed(2);
const T = (s) => +(s - SEG_START).toFixed(3);      // VO seconds → local timeline seconds
const tl = gsap.timeline({ paused: true });
// text lands 0–120 ms before its word:  FX.text.rise(tl, [el], T(220.19) - 0.06)
// scene windows:  scene(SC036, 214.67, 225.63)
...
FX.mount(tl, DURATION);
window.__timelines = window.__timelines || {};
window.__timelines[SEG] = tl;
```
- Write **every** cue as `T(<VO seconds>)` using the word-start times in EDIT_NOTES (they come from `transcript.json`); subtract
  0.04–0.08 s for text. Never write local seconds by hand. `python3 tools/sync_audit.py compositions/segNN.html` must pass.
- Per-frame procedural effects (`FX.grain`, `FX.dust`, `FX.weave`, `FX.streaks`, rough boils) register with `FX.onFrame` **before**
  `FX.mount`; gate them to their scene window (`if (t < T(a) || t > T(b)) return;`) so 17 scenes don't all compute every frame.
- Deterministic only: `FX.rng(seed)`, seeds unique per scene (use the scene number, e.g. 41, 4101…).
- 12 fps "posterize time" (`FX.choppy`) on Vox-style pops/bars/markups; camera moves smooth.

### 3.3 Voiceover in the segment
- For standalone checks each segment carries its own slice, exactly like the samples:
  `<audio id="segNN-vo" class="temp-vo" src="vo10.mp3" data-start="0" data-duration="DURATION" data-media-start="SEG_START" data-volume="1">` — the `class="temp-vo"` is required: the assembler strips it and plays one continuous VO instead. Preview a segment with `python3 tools/build_index.py` style: put only your segment in index.html (see MANUAL §4.3).
- At assembly the lead **removes** the six `segNN-vo` elements and mounts one full VO in `index.html` (MANUAL §4.1). Do not put
  music or SFX in the segment — the sound agent works from your SFX list.
- Never process, re-time or re-gain the VO.

### 3.4 Per-object SFX markers → `compositions/segNN.sfx.json`
The sound designer places SFX only from these files. One JSON array per segment, sorted by `t`, times in **absolute VO seconds**:
```json
[
  {"t": 35.36, "type": "burn_crackle", "scene": "SC007", "dur": 1.5, "level": "soft", "note": "West region burn reveal"},
  {"t": 36.10, "type": "map_pin",      "scene": "SC007", "level": "soft", "note": "pin 3/9 (Seattle)"},
  {"t": 102.35,"type": "shutter",      "scene": "SC018", "level": "normal", "note": "iris closes 0.15 s before Bell Labs"}
]
```
- `t` = the exact moment the object event happens in your timeline (the frame the pin lands / iris closes / stamp hits), not the
  word time. Start from EDIT_NOTES' SFX lines, then correct to what you actually built.
- `type` vocabulary (use only these; ask the lead to add one): `whoosh_soft, whoosh, whoosh_big, air_swell, paper_slide,
  paper_rustle, paper_flip, paper_tear, page_turn, pop_soft, pin_pop, cork_pin, map_pin, string_pull, marker_scratch, marker_long,
  highlighter_swipe, pencil_scribble, stamp_thud, tick_soft, counter_ticks, odometer_tick, letter_ticks, dot_ticks, dot_slide,
  shutter, projector_loop, projector_click, film_burn, crt_click, crt_hum, crt_off, boom_low, burn_crackle, wind, lamp_click,
  gate_creak, chime_soft, tone_blip`.
- Loops/beds (`projector_loop`, `crt_hum`, `wind`) need `dur`. `level` ∈ `soft | normal` (everything stays far under the VO).
- Music is the sound agent's job, following EDIT_NOTES' **Music** lines; editors don't add music markers.

### 3.5 Text & design rules (recap)
- Text follows the narration exactly (EDIT_NOTES §0); only ASR name spellings are corrected; no emphasis on slips/repeats.
- Fonts: classes only (`t-display`, `t-label`, `t-serif`, `t-serif-i`, `halate*`, `.label-box`, `.hl`). Labels ≥ 22 px, captions ≥ 38 px,
  96 px side margins. One text animation at a time on screen.
- Palette tokens only; West = vermilion, East = navy; ≤ 2 accents per frame; yellow only for highlighter / the key number.
- Default texture stack on every scene (grain + dust + vignette; paper scenes add paper-tex + folds). Keep it subtle.
- CC-BY(-SA) images carry a 13 px micro-credit bottom-right (s02 style) while on screen.

### 3.6 Checks before hand-off (per segment)
1. `npx hyperframes lint` → 0 errors (build a temporary index with only your segment; the lead will add seg entries to
   `tools/build_index.py`, or copy its output pattern with `data-composition-src="compositions/segNN.html"`).
2. `python3 tools/sync_audit.py compositions/segNN.html` → every text cue 0–120 ms before its word.
3. `npx hyperframes snapshot --at <every scene midpoint, local seconds> --no-end -o .snap/segNN` and **look** at every frame
   (readability, palette, no repeats, no empty frames at boundaries; also snapshot the first and last 0.1 s).
4. `compositions/segNN.sfx.json` complete and valid JSON.
5. A short `compositions/segNN.NOTES.md` only if something deviates from EDIT_NOTES (asset fallback used, timing moved).

## 4. Assembly (lead)
- `index.html` mounts seg01…seg06 back to back on one track (`data-start` = SEG_START, `data-duration` = DURATION), plus one
  `<audio>` for `vo10.mp3` (0–600) at unity, plus the sound agent's music/SFX tracks.
- Then: lint, a contact sheet of every scene midpoint, render, watch for sync / readability / repetition across segment borders.
