# SEGMENTS — chunk c6 editor split + shared conventions

Three contiguous segments, cut at scene boundaries from `EDIT_NOTES.md` (C6S001–C6S107). One editor agent per segment builds
`compositions/c6sNN.html`. Read first: `project/LONGFORM.md`, `MANUAL.md` (§3–§5, §9, **§10 overrides, esp. §10.9**),
`EDITOR_BRIEF.md`, `EDIT_NOTES.md` §0 + your scenes + §14 (V1–V6) + §15, `analysis/BEATS.md` §2 (spellings/slips),
`ASSETS_NEEDED.md` (paths/usage), `DECISIONS.md`. Look at `review/intro_720p.mp4` first — that is the quality bar.

**All times in this chunk are LOCAL seconds of `vo_c6.mp3`** (0 = full audio 3277.14; c6 ends at 598.01 = 3875.12).

## 1. The split

| seg | VO range (local) | dur | scenes | acts | starts on | ends on |
|---|---|---|---|---|---|---|
| c6s01 | 0.00–201.96 | 201.96 | C6S001–C6S041 (41) | I–VII | UN GA hall, ROC delegation in soft focus (night) — continues c5's vote suspense | Chiang Kai-shek's scroll fully unrolled, "Keep on fighting." settled; whip **up** starts 201.80 (paper) |
| c6s02 | 201.96–401.41 | 199.45 | C6S042–C6S076 (35) | VIII, IX, X (first half) | whip lands (from below) on the Presidential Office footage (night) | ROC claim map: celadon only on Taiwan, BEING TAIWANESE hero; whip **down** starts 401.25 (night) |
| c6s03 | 401.41–598.01 | 196.60 | C6S077–C6S107 (31) | X (end), XI, XII, XIII | whip lands (from above) on the D04 elite bar chart (paper) | breakfast table under the lamp, BREAKFAST hero, three cards around a soy-milk bowl; held to 598.01 → c7 |

Total 107 scenes, 598.01 s, no gaps.

### Boundary hand-offs (both editors honour them)
| boundary | t | outgoing last frames | incoming first frames |
|---|---|---|---|
| c6s01→c6s02 | 201.96 | C6S041: the "Keep on fighting." line has settled by 201.6 (hold ≥ 0.3 s — the scroll + underlines finished at 201.3, so the key animation holds ≥ 0.5 s); **whip ↑** first half 201.80–201.96: frame smears upward with `blurA` 40 px, overscale 1.08 | C6S042: footage enters from below already blurred (`blurB` 40 px) and lands sharp by 202.12; same whip SFX (owned by c6s01's sfx.json, t 201.88) |
| c6s02→c6s03 | 401.41 | C6S076: BEING TAIWANESE hero settled 400.6, held; **whip ↓** first half 401.25–401.41 | C6S077: paper chart enters from above, lands sharp by 401.57; whoosh at 401.33 (c6s02's sfx.json) |
| c5→c6s01 | 0.00 | (c5 lead decides) c5 ends on the vote suspense | C6S001 starts with a 0.0 s J-cut air swell; if c5's last shot is the GA hall, c6s01 reuses its grade so the cut reads as a continuation |
| c6s03→c7 | 598.01 | C6S107 holds the lamp-lit breakfast table (no exit move) | c7 opens "We get to breakfast the next day" — c7 should open on the same table (N81) or cut on its first camera move |

## 2. Shared continuity (things that must look identical across segments)

| motif | scenes (segments) | rule | master owner |
|---|---|---|---|
| **Assembly hemicycle (D06)** | C6S007–008, C6S027 (01) | same dot size/arc, navy US side, red Beijing side, celadon ROC dot, dashed majority line; real 1971 proportions, **no numbers printed** | c6s01 |
| **Chiang Kai-shek portrait card** (N30, torn edge, halftone, celadon tape corners) | C6S039 (01); C6S043, C6S045, C6S052 inset (02) | one card element; c6s01 exports it as a snippet in `compositions/c6s01.NOTES.md` | c6s01 |
| **Dossier card V3** (manila folder, paper clip, typed fields) | C6S035 (01); C6S065, C6S067 (02) | same folder texture, clip, typed-field style (Cooper Hewitt t-label + typewriter 12 fps), lamp pool on night | c6s01 (snippet in NOTES) |
| **Taiwan relief + celadon fill (R12)** M03 | C6S040 (01); C6S062, C6S066 outline (02); C6S078 ghost (03) | same relief file/grade, celadon `#9fc7b2` fill with halftone_01_norm + 6 px glow; alpha mask | c6s01 |
| **World dark atlas** M02 (+ burn) | C6S029 (01); C6S062 (02) | same map, same ink for "switched" countries, burn_a/b seed 2900 | c6s01 |
| **Chiang Ching-kuo card / circle** (N33) | C6S043–048 (02); C6S088, C6S089 circle, C6S107 card (03) | same crop, halftone, card shadow; D15 circle 260 px ring 8 px **celadon** (he is the ROC government) | c6s02 (snippet) |
| **Young CCK + young Deng cards** (N36/N39) | C6S049, C6S051, C6S054, C6S057 (02) | 1920s sepia, same card size | c6s02 |
| **Moscow city plan** M05 | C6S053, C6S057 (02) | same map + json, tilt 12° | c6s02 |
| **Isotype pictograms** (general cap → engineer) | C6S047, C6S064 (02) | one SVG set, ink on paper; flips at 12 fps | c6s02 |
| **Cork board R9** | C6S068–069 (02) | ink string (not red), celadon pins, cork_01 credit | c6s02 |
| **D15 relationship diagram** (CCK → secretary general → telecom → Pan; classmates bracket; Fei reveal) | C6S089, C6S098–099, C6S102, C6S104–107 (03) | grey nodes `#9a958c` until named; CCK celadon ring; arrows `FX.markup.arrow`, t-label 22 px — same style as intro IS024/027 | c6s03 |
| **Secretary-general silhouette** | C6S089, C6S098, C6S106 (03) | matte cut from N80, neutral ink, **never recognisable** before 590.06; the burn reveal in C6S106 starts from exactly this matte | c6s03 |
| **Premier's memo** (D08 variation) | C6S090–091 (03) | typeset recreation, no seals/letterhead; same paper as the breakfast note | c6s03 |
| **TV sets** | C6S032 1970s Taiwanese set (01); C6S094 1960s RCA console (03) | never the same set; neither is the intro's Tatung TV20CGE unless N24 fails (then c6s01 uses it as a fallback) | each |
| **Halate (hero only)** | 01: CHINA, WITHDRAWS, DOMINO EFFECT · 02: CHIANG CHING-KUO, MILITARY, ECONOMIC POWER, BEING TAIWANESE · 03: 10, MOON, TRANSISTORS, BREAKFAST | one glowing element per frame; paper never glows | all |
| **Yellow key numbers** | `2/3` (01, C6S005), `12 YEARS` (02, C6S051), `0%` (03, C6S084) | `--yellow`; other yellow = highlighter / marker routes only | each |
| **Grid / paper grounds** | everywhere | full-frame = `_hires` Texturelabs papers, two layers (top ~90 %); never the same paper in consecutive paper scenes; K+E scans only as small cards | all |

### Palette moments per segment
| seg | grounds | accents |
|---|---|---|
| c6s01 | night press photos of the UN ↔ paper documents/charts ↔ dark maps | celadon Taiwan (ROC); **red PRC/CCP**; navy US only in the vote hemicycle + Bush split; yellow 2/3 + one highlighter |
| c6s02 | 1920s–30s sepia (Moscow, USSR) ↔ paper cards/maps ↔ lamp-lit dossiers | celadon ROC/Taiwan; red = USSR / Deng / PRC mainland (C6S049, 054, 076); yellow 12 YEARS + one marker route |
| c6s03 | paper charts ↔ night footage/maps ↔ the Moon ↔ paper diagram | celadon Taiwan; yellow 0% + freeway route; RCA neutral (vintage RCA logo in bone/ink, not its brand colours) |

## 3. Shared conventions

### 3.1 Files and ids
- Composition `compositions/c6sNN.html` (NN = 01, 02, 03); composition id **`c6sNN`**. Root:
  `<div id="root" data-composition-id="c6sNN" data-vo-start="SEG_START" data-duration="DURATION" data-width="1920" data-height="1080">`
  — `data-vo-start` is the **LOCAL** start (0.00 / 201.96 / 401.41); `data-duration` = 201.96 / 199.45 / 196.60.
  Build with `tools/build_master.py --prefix c6s --vo vo_c6.mp3 --len 598.01 --timeline assets/audio/c6/timeline.json` (lead).
- Element ids prefixed `c6sNN-`, inside a scene `c6sNN-scNNN-` (e.g. `c6s02-sc051-ledger`; NNN = the C6S scene number).
  One `<template>` with `<style>`, root div, `<script>` IIFE. No `font-family` in composition CSS (classes only). Asset URLs
  relative to the project root (`assets/…`, `vo_c6.mp3`).
- Each scene: `<div class="scene" id="c6sNN-scNNN" data-scene="C6SNNN">`, full-frame, hidden outside its window
  (`tl.set(el,{autoAlpha:1},S(start))` / `tl.set(el,{autoAlpha:0},S(end))`; initial state with `gsap.set` outside the timeline,
  §4.2); per-frame effects wrapped in `FX.gate` (wrap `FX.onFrame` while calling `FX.streaks`/`FX.weave`/`FX.roughDefs`, §4.2).
- Don't edit `lib/fx.css`, `lib/fx.js`, `lib/palette.css`; new helpers live in your script and are reported to the lead.

### 3.2 Timing
```js
const SEG = "c6s02", SEG_START = 201.96, SEG_END = 401.41, DURATION = +(SEG_END - SEG_START).toFixed(2);
const T = (s) => +(s - SEG_START).toFixed(3);   // TEXT cues (audited) — LOCAL c6 seconds in, segment seconds out
const S = T;                                     // STRUCTURAL cues (cuts, camera, objects) — not audited
const tl = gsap.timeline({ paused: true });
// FX.text.rise(tl, [el], T(248.84) - 0.06)
...
FX.mount(tl, DURATION);
window.__timelines = window.__timelines || {}; window.__timelines[SEG] = tl;
```
- Every text cue is a **literal** `T(<word start>)` from EDIT_NOTES / BEATS §4 (never `T(c)` over an array). Default −0.06 s.
- Easing: `FX.choppy(FX.ease.out|inOut|in, dur, 12)`; camera `FX.ease.cam` (smooth). Entrances 1.0–1.6 s, moves 1.2–2 s.
  No `back.out`, no short `power2/3.out` on big elements, no `expo.inOut` except the C6S055 curve cut.
- **Key animations finish and hold ≥ 0.5 s before the scene's Out** (§10.9; EDIT_NOTES §15.6 lists the tight ones).
- Transitions: `FX.whipDefs` + `FX.whip(tl, a, b, S(t), {dir, vertical})` (~0.32 s), light-flash variant for `FW`; `CA` = cut
  while the camera or a secondary element moves; `FX.focusHunt` once per scene max. **No `FX.iris`.**
- Deterministic only (`FX.rng(seed)`, seed = scene number × 100).

### 3.3 Voiceover in the segment
`<audio id="c6sNN-vo" class="temp-vo" src="vo_c6.mp3" data-start="0" data-duration="DURATION" data-media-start="SEG_START" data-volume="1">`
— the assembler strips `temp-vo` and plays one continuous VO. Never process the VO. No music/SFX audio tags in segments.
Archival footage: `<video muted …>` only. No face cam in c6.

### 3.4 SFX markers → `compositions/c6sNN.sfx.json`
Array sorted by `t`, **LOCAL c6 seconds**: `{"t": 248.82, "type": "counter_ticks", "scene": "C6S051", "dur": 0.8,
"level": "soft", "note": "12 YEARS count"}`. Start from EDIT_NOTES' SFX lines, then correct to the frame the object actually
moves. Vocabulary = intro SEGMENTS §3.4 (`whoosh_soft, whoosh, whoosh_big, air_swell, paper_slide, paper_rustle, paper_flip,
paper_tear, page_turn, pop_soft, pin_pop, map_pin, marker_scratch, marker_long, highlighter_swipe, pencil_scribble, stamp_thud,
tick_soft, counter_ticks, odometer_tick, letter_ticks, dot_ticks, dot_slide, projector_loop, projector_click, crt_click,
crt_hum, crt_off, boom_low, burn_crackle, wind, lamp_click, gate_creak, chime_soft, tone_blip`) + the §10.6 **circuit-breaker
clunk** for contrast call-outs (`type: "clunk"`) and `crowd` (very low ambience, C6S018). Loops need `dur`. `level` ∈ soft | normal.
Whips at a segment boundary belong to the outgoing segment's file.

### 3.5 Text & design rules (recap)
- Text = narration exactly; spellings fixed (George H. W. Bush, Henry Kissinger, Chiang Kai-shek, Chiang Ching-kuo, Deng Xiaoping,
  Mao Zedong, Sun Yun-suan, K. T. Li, Sarah Paine, Pan Wen-yuan, Fei Hua, RCA); no text on slips/asides (BEATS §2b); paraphrased
  quotes attributed "(paraphrased)". Labels ≥ 22 px, captions ≥ 38 px, 96 px side margins, one text animation at a time.
- Original Chinese of a slogan may appear small as decoration under the English (as an image — our fonts have no CJK glyphs).
  Real documents keep their own printed words; our overlay text = the narrator's words only.
- Palette tokens from `lib/palette.css` only; ≤ 2 accents per frame; c6 mapping (lead): `--vermilion` = PRC/CCP/Communist bloc,
  `--celadon` = Taiwan/ROC, `--navy`/`--sky` = US & allies only where contrasted; yellow only highlighter,
  marker route or the scene's key number.
- Default texture stack on every scene (grain + dust + vignette; light chromatic aberration 0.1–0.15 on photos/footage);
  copyrighted/CC BY(-SA) assets get a 13 px micro-credit bottom-right while on screen ("© AP", "UN Photo", "NASA", …).

### 3.6 Checks before hand-off
1. `npx --yes hyperframes@0.8.217 lint` → 0 errors (sandbox: `tools/make_sandbox.sh c6sNN`, then
   `cd work/c6sNN && python3 tools/build_index.py c6sNN --root .`).
2. `python3 tools/sync_audit.py compositions/c6sNN.html --transcript transcript_c6.json` → every text cue 0–120 ms before its word.
3. `npx --yes hyperframes@0.8.217 snapshot --at <every scene midpoint + each scene's last 0.6 s> --no-end -o .snap/c6sNN` and LOOK
   at every frame with the words under it (does the picture match the words? did the key animation finish and hold?).
4. `compositions/c6sNN.sfx.json` valid; `compositions/c6sNN.NOTES.md` for deviations, exported motif snippets, asset fallbacks.

## 4. Assembly (lead)
`python3 tools/build_master.py --prefix c6s --vo vo_c6.mp3 --len 598.01 --timeline assets/audio/c6/timeline.json`, lint,
contact sheet of every scene midpoint with the transcript under each frame, picture render, fix, sound pass
(`tools/audio/place_sound.py --vo vo_c6.mp3 --transcript transcript_c6.json --len 598.01 --markers 'compositions/c6s0*.sfx.json'
--cues project/c6/music_cuesheet.json --out assets/audio/c6`), final render → `renders/c6/c6_final.mp4` + `review/c6_720p.mp4`;
verify the VO loudness in the final file equals `vo_c6.mp3`.
