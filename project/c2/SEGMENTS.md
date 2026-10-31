# SEGMENTS — chunk c2 editor split + shared conventions

Three contiguous segments of ~200 s, cut at scene boundaries from `EDIT_NOTES.md` (C2S001–C2S128). One editor agent per
segment builds `compositions/c2sNN.html`. Read first: `project/LONGFORM.md`, `MANUAL.md` (§3–§5, §9, **§10 overrides, §10.9
long-form rules**), `project/intro/BRIEF.md`, `EDITOR_BRIEF.md`, `EDIT_NOTES.md` §0 + your scenes, `ASSETS_NEEDED.md`
(paths), `DECISIONS.md`, `analysis/BEATS.md` §2 (spellings/slips). Look at `review/intro_720p.mp4` first — it is the bar.

## 1. The split

| seg | VO range (local) | full-audio range | dur | scenes | acts | starts on | ends on |
|---|---|---|---|---|---|---|---|
| c2s01 | 0.00–198.43 | 877.88–1076.31 | 198.43 | C2S001–C2S042 (42) | I, II, III | Stanford quad + struck-out field list (night) | dark world map, rings pulsing, camera gliding toward North America |
| c2s02 | 198.43–403.13 | 1076.31–1281.01 | 204.70 | C2S043–C2S087 (45) | IV, V, VI (part 1) | same world-map camera arriving on the ghost US map, NJ glowing sky-blue | missile cutaway covered in ✗ marks (paper), sliding up as a card |
| c2s03 | 403.13–597.86 | 1281.01–1475.72 | 194.73 | C2S088–C2S128 (41) | VI (part 2), VII, VIII | the ✗-covered "problem" card pinned to the lab door at night | Silicon Valley aerial pulling back onto a chip die (still moving into c3) |

Total 128 scenes, 597.86 s, no gaps. Inside each segment, scenes are layers gated by `FX.gate` and `display:none` outside
their window (MANUAL §4.4 "long segments") — keep heavy overlays (2.5D, footage) to one scene at a time.

### Boundary hand-offs (both editors honour them)
| boundary | t | outgoing last frames | incoming first frames |
|---|---|---|---|
| c1 → c2s01 | 0.00 | (c1 owner) last scene over "Stanford cannot be best at everything" | C2S001: Stanford Main Quad c.1896 plate (E40) + a dense list of ~30 field names; **lead aligns with the c1 planner** — if c1 ends on another image, C2S001's first 6 frames match it and the list fades in over it |
| c2s01 → c2s02 | 198.43 | C2S042: map-kit world basemap (dark), radio-wave rings fading, camera gliding (cam ease) toward the US, reaching scale 1.6 centred on 39°N 98°W at 198.43 | C2S043: same basemap file and grade (K03→K02 ghost US view), camera continues the glide from scale 1.6 → 2.4 while NJ glows sky-blue @199.95. c2s01 exports camera end-state (scale, lon/lat → px, grade filter string) in `compositions/c2s01.NOTES.md` |
| c2s02 → c2s03 | 403.13 | C2S087: missile cutaway (ink on paper_cream) with ~200 ✗ marks, the whole sheet shrinking to a 520×360 card and sliding **up** from 402.90 | C2S088: the same card (export as PNG `assets/c2/derived/c2s02/problem_card.png`) enters from the bottom and pins to the lab door; c2s03 starts it at the exported position/scale |
| c2s03 → c3 | 597.86 | C2S128: pull-back from the valley into a chip die, still moving | c3 (next chunk) continues "how big it was" — c3 planner may cut on that move |

## 2. Shared continuity (things that must look identical across segments)

| motif | scenes (segments) | rule | master owner |
|---|---|---|---|
| **Palette mapping** | all | red `--vermilion` = West/Stanford/Terman/Palo Alto/Industrial Park; navy/sky = East/Bell Labs/NJ/Washington; neutral = Shockley, eight, Fairchild, Noyce, companies; yellow = highlighter + one key number per scene; no celadon (BEATS §7) | all |
| **Steeple/pillar motif** | S003→S004 spire tips, S011 red light-pillars (01) | same red, same 4 count | c2s01 |
| **Four field cards + silicon card** | S007, S009, S010 (01); S119 callback (03) | one card style (paper_lined_01, typewriter t-label, photo window, red paper clip on the silicon card). c2s01 exports HTML/CSS snippet + the silicon card PNG in its NOTES; c2s03 reuses it at S119 | c2s01 |
| **Crystal lattice + electron dots** | S008 (01); S122 (03) | one SVG lattice (bone hairlines, 12 fps draw-on), dot size 6 px, flow speed; S122 is a side-view variant | c2s01 (exports SVG) |
| **Transistor cut-out (N12)** | S019, S023, S032 (01); S081 (02); S109 (03) | same cut-out PNG, rim light on night, halftone on paper | c2s01 makes `assets/c2/cutouts/transistor_early.png` |
| **Switch schematic** | S019 (01); S082 (02) | same bone pen symbol (stroke 5 px, pen boil 4/s) | c2s01 |
| **Nobel medal** | S034 (01); S046 (02) | same photo crop (N24), same gold-neutral grade | c2s01 |
| **Shockley portrait circles / D15 node style** | S012 (01); S043, S047, S070–071, S075 (02); S093–094 (03) | circle 220 px, ring 8 px (red West, navy East, ink neutral), arrows `FX.markup.arrow`, labels t-label 22 px | c2s02 |
| **Terman likeness** | S010, S012 (01); S043, S054, S063 (02) | same photo (N06 hi-res) / cut-out; red ring | c2s02 makes the cut-out; c2s01 uses the card crop |
| **Palo Alto old map** | S051–052 (02); S097 (03, different 1961 quad) | same warm sepia grade + pin style (`pin_vermilion_top.svg` company, ink home); S097 uses numbered pins + yellow marker | c2s02 |
| **"Problem" card + headache tangle** | S084, S087 (02); S088, S100, S102 (03) | pen tangle path exported as SVG from c2s02; the ✗ dot drawing exported as PNG | c2s02 |
| **Unlit → lit SILICON VALLEY sign** | S080 (02) unlit; S127 (03) lit | same letters (t-display, outline 3 px bone), same position/size; S127 adds fill + **hero halate** | c2s02 builds, c2s03 copies verbatim |
| **Traitorous Eight photo** | S095 2.5D (03), S099 flat (03); S093 circles cropped from it (03) | same file N65, same duotone | c2s03 |
| **Fairchild film footage** (Prelinger reel) | S101, S105, S110 (03); S123 scope (03) | `assets/intro/footage/*` with chromaticAberration 0.12, weave light; no intro TV sets | c2s03 |
| **Screens** | S085 1950s TV (02); S123 Tektronix 475A (03) | never the intro's Tatung/Trinitron; CRT power-on per s04 | each |
| **Grid / ruled papers** | S002–003, S018, S022 (01); S044, S064, S070–071, S082–083 (02); S107, S116–117, S126 (03) | `_hires` only; never the same paper file in consecutive scenes; rule colour desaturated toward ink-grey | each, same files |
| **Halate** | hero only: silicon, 1947, transistor, hot, Nobel Prize (01); William Shockley, Leland Stanford, finagling, Stanford Industrial Park (02); nightmare, Traitorous Eight, Robert Noyce, integrated circuit, insane, Silicon Valley (03) | one glowing element per frame; paper never glows | all |
| **Yellow key numbers** | `8,000` S057, `99` S067, `10,000` S086 (02); `100,000` S116 (03) | `--yellow`; all other yellow = highlighter / R10 marker route | 02, 03 |

### Palette moments per segment
| seg | grounds | accents |
|---|---|---|
| c2s01 | night specimen/vitrine + archival plates ↔ grid isotypes ↔ paper documents/ads | red Stanford/Terman (act I), navy Bell Labs (act II–III), yellow highlighters only (no key number) |
| c2s02 | maps (US, Palo Alto, Stanford lands, satellite) ↔ paper documents/forms ↔ night plates & 2.5D | red West dominates; navy only in S043, S047–048 (East→West move); yellow 8,000 / 99 / 10,000 |
| c2s03 | night footage (Fairchild reel) + portraits ↔ paper patents/charts | mostly neutral + red highlights (IC bar, semi-); yellow 100,000 and the marker route |

## 3. Shared conventions

### 3.1 Files and ids
- Composition `compositions/c2sNN.html` (NN = 01, 02, 03); composition id **`c2sNN`**. Root:
  `<div id="root" data-composition-id="c2s02" data-vo-start="198.43" data-duration="204.70" data-width="1920" data-height="1080">`
  — **`data-vo-start` is LOCAL** (seconds into `vo_c2.mp3`); the chunk assembler
  (`tools/build_master.py --prefix c2s --vo vo_c2.mp3 --len 597.86 --timeline assets/audio/c2/timeline.json`) reads
  `data-vo-start` / `data-duration`.
- Element ids prefixed `c2sNN-`, inside a scene `c2sNN-scNNN-` (scene number = the C2S number, e.g. `c2s02-sc065-park`).
  One `<template>` with `<style>`, root div, `<script>` IIFE. No `font-family` in composition CSS. Asset URLs relative to the
  project root (`assets/…`, `vo_c2.mp3`).
- Each scene: `<div class="scene" id="c2sNN-scNNN" data-scene="C2SNNN">`, full-frame, hidden outside its window
  (`tl.set(el,{autoAlpha:1},S(start))` / `tl.set(el,{autoAlpha:0},S(end))`; initial state with `gsap.set` outside the
  timeline, §4.2); per-frame effects wrapped in `FX.gate` (gate `FX.streaks`/`FX.weave`/boil via the `FX.onFrame` wrapper).
- New derived files go to `assets/c2/<type>/` (+ `SOURCES.md`); per-segment derived files to `assets/c2/derived/c2sNN/`.
- Don't edit `lib/fx.css`, `lib/fx.js`, `lib/palette.css`; new helpers live in your script and are reported to the lead.

### 3.2 Timing (LOCAL seconds)
```js
const SEG = "c2s02", SEG_START = 198.43, SEG_END = 403.13, DURATION = +(SEG_END - SEG_START).toFixed(2);
const T = (s) => +(s - SEG_START).toFixed(3);   // TEXT cues (audited) — literal LOCAL word starts from EDIT_NOTES
const S = T;                                     // STRUCTURAL cues (cuts, camera, objects) — not audited
const tl = gsap.timeline({ paused: true });
// FX.text.rise(tl, [el], T(292.21) - 0.06)
...
FX.mount(tl, DURATION);
window.__timelines = window.__timelines || {}; window.__timelines[SEG] = tl;
```
- Every text cue is a **literal** `T(<local word start>)` (never `T(c)` over an array). Default −0.06 s.
- Easing: `FX.choppy(FX.ease.out|inOut|in, dur, 12)`; camera `FX.ease.cam`. Entrances 1.0–1.6 s, moves 1.2–2 s. No `back.out`,
  no short `power2/3.out` on big elements; `expo.inOut` only in S027→S028's curve cut.
- Transitions: `FX.whipDefs` + `FX.whip(tl, a, b, S(t), {dir, vertical})`, light-flash variant for `FW`; `CA`/`HC` = cut while
  both shots move. **No `FX.iris`.** `FX.focusHunt` once per scene max.
- **Hold rule**: every scene's key animation completes ≥ 0.5 s (12 frames) before its out-transition starts (EDIT_NOTES gives
  "done by" times); check the last second of every scene in snapshots.
- Deterministic only (`FX.rng(seed)`, seed = scene number × 100).

| seg | SEG_START | SEG_END | DURATION |
|---|---|---|---|
| c2s01 | 0.00 | 198.43 | 198.43 |
| c2s02 | 198.43 | 403.13 | 204.70 |
| c2s03 | 403.13 | 597.86 | 194.73 |

### 3.3 Voiceover in the segment
`<audio id="c2sNN-vo" class="temp-vo" src="vo_c2.mp3" data-start="0" data-duration="DURATION" data-media-start="SEG_START" data-volume="1">`
— the assembler strips `temp-vo` and plays one continuous `vo_c2.mp3`. Never process the VO. No music/SFX audio tags in
segments. Footage `<video muted …>` only.

### 3.4 SFX markers → `compositions/c2sNN.sfx.json`
Array sorted by `t`, **LOCAL** VO seconds of `vo_c2.mp3`: `{"t": 431.83, "type": "boom_low", "scene": "C2S095", "dur": 0,
"level": "soft", "note": "Traitorous Eight title"}`. Start from EDIT_NOTES' SFX lines, then correct to the frame the object
actually moves. Vocabulary (intro set): `whoosh_soft, whoosh, whoosh_big, air_swell, paper_slide, paper_rustle, paper_flip,
paper_tear, page_turn, pop_soft, pin_pop, map_pin, marker_scratch, marker_long, highlighter_swipe, pencil_scribble,
stamp_thud, tick_soft, counter_ticks, odometer_tick, letter_ticks, dot_ticks, dot_slide, projector_loop, projector_click,
crt_click, crt_hum, crt_off, boom_low, burn_crackle, wind, lamp_click, gate_creak, chime_soft, tone_blip` **+ new for c2**:
`switch_click, tube_hum, solder_hiss, typewriter, card_flip, clock_tick, rewind, medal_ring` (sound designer maps them —
Epidemic SFX or generated). Loops need `dur`. `level` ∈ soft | normal. Mark one hero per scene + each camera move/entrance
(restraint pass §10.8 thins the rest).

### 3.5 Text & design rules (recap)
- Text = narration exactly; spellings fixed (John Bardeen, Walter Brattain, Terman, Traitorous Eight, Fairchild Semiconductor,
  Robert Noyce, Leland Stanford, Stanford Industrial Park, Lockheed, Varian, HP, General Electric); no text on slips (BEATS §2b).
  Labels ≥ 22 px, captions ≥ 38 px, 96 px side margins, one text animation at a time.
- Palette tokens from `lib/palette.css` only; ≤ 2 accents per frame.
- Default texture stack on every scene (grain + dust + vignette; paper adds paper-tex + folds, two paper layers top ≈ 90 %).
  Light chromatic aberration (0.10–0.15) on photos/footage. Every fill sits under texture.
- Credits: CC BY(-SA) and copyrighted (fair use) assets get a 13 px micro-credit bottom-right while on screen
  (e.g. "Photo: Wayne Miller / Magnum Photos").

### 3.6 Checks before hand-off
1. `npx --yes hyperframes@0.8.217 lint` → 0 errors (sandbox: `tools/make_sandbox.sh c2sNN`, then
   `cd work/c2sNN && python3 tools/build_index.py c2sNN --root .`).
2. `python3 tools/sync_audit.py compositions/c2sNN.html --transcript transcript_c2.json` → every text cue 0–120 ms before its word.
3. `npx --yes hyperframes@0.8.217 snapshot --at <every scene midpoint + each scene's last 0.5 s + first/last 0.1 s> --no-end
   -o .snap/c2sNN` and LOOK at each frame with the words under it (does the picture match the words? did the key animation
   finish before the cut?).
4. `compositions/c2sNN.sfx.json` valid; `compositions/c2sNN.NOTES.md` for deviations, exported motif snippets, asset fallbacks.

## 4. Assembly (lead)
`python3 tools/build_master.py --prefix c2s --vo vo_c2.mp3 --len 597.86 --timeline assets/audio/c2/timeline.json`, lint,
contact sheet of every scene midpoint with the transcript under each frame, picture render, fix, sound pass
(`tools/audio/place_sound.py --vo vo_c2.mp3 --transcript transcript_c2.json --len 597.86 --markers 'compositions/c2s0*.sfx.json'
--cues project/c2/music_cuesheet.json --out assets/audio/c2`), final render → `renders/c2/c2_final.mp4` + `review/c2_720p.mp4`;
verify the VO loudness in the final file equals `vo_c2.mp3`.
