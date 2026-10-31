# SEGMENTS — c3 editor split + shared conventions

Three contiguous segments of ~200 s, cut at scene boundaries from `EDIT_NOTES.md` (C3S001–C3S111). One editor agent per segment
builds `compositions/c3sNN.html`. Read first: `project/LONGFORM.md`, `MANUAL.md` (§3–§5, §9, **§10 overrides**, esp. §10.9),
`EDITOR_BRIEF.md`, `EDIT_NOTES.md` §0 + your scenes, `ASSETS_NEEDED.md` (paths/usage), `DECISIONS.md`, and the approved intro
compositions `compositions/intro0*.html` (the look and the quality bar; copy their structure and helpers).

## 1. The split

| seg | VO range (local) | full-audio range | dur | scenes | acts | starts on | ends on |
|---|---|---|---|---|---|---|---|
| c3s01 | 0.00–200.34 | 1475.72–1676.06 | 200.34 | C3S001–C3S042 (42) | I, II, III, IV (first half) | IC die macro pulling back (night) — continues c2's chip | Pan–Terman–Hewlett diagram on paper; light-flash whip begins @200.28 |
| c3s02 | 200.34–404.17 | 1676.06–1879.89 | 203.83 | C3S043–C3S077 (35) | IV (end), V, VI, VII | the bright flash frame resolving into the dark decade timeline | ROC 'recover the mainland' poster; whip → begins @404.11 |
| c3s03 | 404.17–602.02 | 1879.89–2077.72 | 197.85 | C3S078–C3S111 (34) | VIII, IX, X | the whip → landing on the dark world map (countries turning celadon) | row of five flag circles (Russia flipped to USSR), slow pull-back continuing into c4 |

Total 111 scenes, 602.02 s, no gaps. Scene density ≈ 5.4 s/scene (intro: 4.2 s) — c3 is a talkier chunk; keep every scene alive
with camera drift and 12 fps builds, never a static hold.

### Boundary hand-offs (both editors honour them)
| boundary | t (local) | outgoing last frames | incoming first frames |
|---|---|---|---|
| c2 → c3s01 | 0.00 | (c2 lead: c2 ends on "…people don't realize how big." — ideally a chip/silicon visual in motion) | C3S001: E01 die macro already pulling back (cut on action); `air_swell` J-cut at 0.00. If c2 ends on a whip, c3s01 starts mid-smear (agree with the c2 editor via the lead) |
| c3s01 → c3s02 | 200.34 | C3S042: diagram (paper) — light-flash whip starts @200.28: smear left + brightness ramp to bone (`#f2ede3`) at 200.34 | C3S043: frame 0 = full bone flash, smear decays over 0.2 s revealing the dark timeline already scrolling (streaks on) |
| c3s02 → c3s03 | 404.17 | C3S077: poster plate — whip right starts @404.11, outgoing smeared off to the right by 404.17 | C3S078: world-night map enters smeared from the left, lands sharp by 404.40; celadon fills begin @405.27 |
| c3s03 → c4 | 602.02 | C3S111: five flag circles hold (anim done 601.5), camera pull-back still moving | c4 lead: c4 opens "All of them have a veto" — continue the same five circles (export the snippet in NOTES) |

## 2. Shared continuity (things that must look identical across segments)

| motif | scenes (segments) | rule | master owner |
|---|---|---|---|
| **US night satellite map** (s02 grade) | C3S008, C3S011 (01); ghost CA outline C3S023 (01) | same basemap/grade as the approved s02; CA vermilion overlay 0.6 (MANUAL §4.2) | c3s01 |
| **Pacific ghost map** Stanford ↔ Taiwan | C3S037 (01), C3S046 (02) | same crop/grade, Stanford pin vermilion, Taiwan celadon fill, same line style; c3s02 adds radio rings | c3s01 (export snippet in NOTES) |
| **Recipe index card** | C3S035 (01), C3S047 (02) | one card element (typed lines + photo chips); c3s02 shows it with a focal call-out | c3s01 |
| **Pan Wen-Yuan portrait + circle** | C3S039, C3S040, C3S042 (01); C3S044, C3S046 (02) | same duotone (sepia→celadon), same circle size (220 px) and ring (8 px celadon) | c3s01 |
| **Terman** | C3S019, C3S026, C3S036, C3S038, C3S040 (01) | vermilion ring/label-box; c1's Terman treatment (check `compositions/c1s*` once built) | c3s01 |
| **Taiwan celadon fill** (relief, watercolour edge, halftone, 6 px glow) | C3S037, C3S044, C3S046, C3S048 (01/02); C3S054, C3S074 (02); C3S080 (03) | same mask/fill/grade from the map kit; drain animation (C3S054) = fill opacity 0.8 → 0 at 12 fps | c3s02 |
| **East Asia / China relief** (kit) | C3S054, C3S073, C3S074 (02); C3S080 (03) | one projection + json; CCP = red (`--vermilion` 0.6 + halftone, as the R12 look), ROC claim = celadon | c3s02 |
| **World night map** (kit) | C3S067–C3S068 (02); C3S078, C3S098 (03); ghost world C3S094 (03) | same projection/grade; country fills via `world_countries.svg` paths (drop antimeridian sub-paths, MANUAL §4.2); celadon 0.8 fills | c3s02 (export) |
| **Flags** (N40) as circles | C3S063, C3S065 (02); C3S079, C3S090, C3S095, C3S100, C3S110, C3S111 (03) | same circle size (160 px), 6 px bone ring, slight halftone; 1945 flags in WWII scenes (48-star US) | c3s02 |
| **UN horseshoe seats (D06)** | C3S085, C3S089 (03) | 11 seats, 5 permanent ringed, China seat celadon | c3s03 |
| **Country isotype grid (D03)** | C3S093, C3S099 (03) | same grid + square size; strings added in C3S099 | c3s03 |
| **1971 front page** (N29) | C3S052, C3S057 (02) | same grade; C3S057 uses a card crop | c3s02 |
| **Screens** | C3S003 IBM 5154, C3S018 Trinitron, C3S034 projector (01); C3S092 Tatung (03) | never the same set twice; CRT on/off per s04; light chromatic aberration 0.1–0.15 | each |
| **Papers** | all PAPER/GRID scenes | Texturelabs `_hires` for full-frame; K+E/ledger scans only as cards ≤ native; two layers (top ~90 %) on document scenes; never the same paper in consecutive paper scenes | each |
| **Halate** | hero only: the world, SILICON VALLEY, CALIFORNIA LAW, FAIRCHILD, 1965, HOOVER, HOOVER INSTITUTION (01); PAN WEN-YUAN is in 01; desperate, TAIWAN (C3S048), WORLD WAR II, FOUR POLICEMEN, SECURITY COUNCIL, CIVIL WAR, TAIWAN (C3S074) (02); ALL OF CHINA, UNITED NATIONS, the power, DECOLONIZATION, UN GENERAL ASSEMBLY, VETO (03) | one glowing element per frame; paper never glows | all |

### Palette moments per segment
| seg | grounds | accents |
|---|---|---|
| c3s01 | night chip/maps/2.5D ↔ legal documents on paper ↔ grid tree | c1 code: vermilion West/California/Stanford/SV; navy only for New York/Field (C3S013–014); celadon enters at C3S037 (Taiwan) and with Pan |
| c3s02 | night maps/newsreels ↔ newspapers, posters, diagrams | to 235.94 c1 code (vermilion SV in C3S046); from 235.94 political code: red CCP vs celadon ROC, navy US when contrasted (C3S051 SV line, C3S063) — no vermilion-as-West after 235.94 |
| c3s03 | night maps/plates ↔ paper charts (D02/D03/D04/D06) | red CCP/USSR/Warsaw Pact vs celadon ROC; navy US in contrasts (C3S090, 094, 095, 098, 099); UN/UK/Japan neutral; yellow only highlighters |

## 3. Shared conventions

### 3.1 Files and ids
- Composition `compositions/c3sNN.html` (NN = 01, 02, 03); composition id **`c3sNN`**. Root:
  `<div id="root" data-composition-id="c3sNN" data-vo-start="SEG_START" data-duration="DURATION" data-width="1920" data-height="1080">`
  with **local** `data-vo-start` (0 / 200.34 / 404.17) — `tools/build_master.py --prefix c3s --vo vo_c3.mp3 --len 602.02
  --timeline assets/audio/c3/timeline.json` reads `data-vo-start` / `data-duration`.
- Element ids prefixed `c3sNN-`, inside a scene `c3sNN-scNNN-` (NNN = the C3S number, e.g. `c3s02-sc054-taiwanfill`). One
  `<template>` with `<style>`, root div, `<script>` IIFE. No `font-family` in composition CSS. Asset URLs relative to the project
  root (`assets/…`, `vo_c3.mp3`).
- Each scene: `<div class="scene" id="c3sNN-scNNN" data-scene="C3SNNN">`, full-frame, hidden outside its window
  (`gsap.set` for the frame-0 state, MANUAL §4.2; `tl.set(el,{autoAlpha:1},S(start))` / `tl.set(el,{autoAlpha:0},S(end))`);
  per-frame effects gated with `FX.gate` (and the `FX.onFrame` wrapper for helpers, §4.2).
- Don't edit `lib/fx.css`, `lib/fx.js`, `lib/palette.css`; new helpers live in your script and are reported to the lead.

### 3.2 Timing (LOCAL seconds)
```js
const SEG = "c3s02", SEG_START = 200.34, SEG_END = 404.17, DURATION = +(SEG_END - SEG_START).toFixed(2);
const T = (s) => +(s - SEG_START).toFixed(3);   // TEXT cues (audited) — s = LOCAL c3 seconds from EDIT_NOTES
const S = T;                                     // STRUCTURAL cues (cuts, camera, objects) — not audited
const tl = gsap.timeline({ paused: true });
// FX.text.rise(tl, [el], T(257.22) - 0.06)
...
FX.mount(tl, DURATION);
window.__timelines = window.__timelines || {}; window.__timelines[SEG] = tl;
```
- Every text cue is a **literal** `T(<word start>)` from EDIT_NOTES (never `T(c)` over an array). Default −0.06 s.
- Easing: `FX.choppy(FX.ease.out|inOut|in, dur, 12)`; camera `FX.ease.cam`. Entrances 1.0–1.6 s, moves 1.2–2 s (short scenes
  flagged in EDIT_NOTES §11.6 may use 0.3–0.5 s text rises). No `back.out`; `expo.inOut` only in C3S002's curve cut.
- **Hold rule**: the scene's key animation is done by its `Done` time; nothing important animates in the last 0.5 s except the
  camera / secondary motion you cut on.
- Transitions: `FX.whipDefs` + `FX.whip(tl, a, b, S(t), {dir, vertical})` (~0.32 s), light-flash variant for `FW`; `CA`/`HC`
  = cut while both shots move; `FX.focusHunt` once per scene max. **No `FX.iris`.**
- Deterministic only (`FX.rng(seed)`, seed = scene number ×100).

### 3.3 Voiceover in the segment
`<audio id="c3sNN-vo" class="temp-vo" src="vo_c3.mp3" data-start="0" data-duration="DURATION" data-media-start="SEG_START" data-volume="1">`
— the assembler strips `temp-vo` and plays one continuous `vo_c3.mp3`. Never process the VO. No music/SFX audio tags in segments.
Footage: `<video muted …>` only. No face cam in c3.

### 3.4 SFX markers → `compositions/c3sNN.sfx.json`
Array sorted by `t`, **local c3 seconds**: `{"t": 257.20, "type": "marker_scratch", "scene": "C3S052", "dur": 0.6, "level":
"soft", "note": "box around the expels-Taipei headline"}`. Start from EDIT_NOTES' SFX lines, then correct to the frame the object
actually moves. Vocabulary (intro set + c3 additions): `whoosh_soft, whoosh, whoosh_big, air_swell, paper_slide, paper_rustle,
paper_flip, paper_tear, page_turn, pop_soft, pin_pop, map_pin, marker_scratch, marker_long, highlighter_swipe, pencil_scribble,
stamp_thud, tick_soft, counter_ticks, odometer_tick, letter_ticks, dot_ticks, dot_slide, projector_loop, projector_click,
crt_click, crt_hum, crt_off, boom_low, burn_crackle, wind, lamp_click, chime_soft, tone_blip, circuit_clunk` + **new in c3**:
`scanner_sweep` (photocopy bar, C3S015), `radio_pulse` (radio-wave rings, C3S046/C3S098), `domino_tick`, `domino_run` (C3S100),
`dial_click` (C3S102), `string_draw` (C3S019) — the sound designer maps unknown types to the nearest library sound. Loops need
`dur`. `level` ∈ soft | normal.

### 3.5 Text & design rules (recap)
- Text = narration exactly; spellings fixed (IC, Silicon Valley, Terman, Bill Hewlett, Pan Wen-Yuan, Hoover Institution, David
  Dudley Field, ROC, CCP, Warsaw Pact, UN General Assembly, "your side"); no text on slips (BEATS §2b). Labels ≥ 22 px,
  captions ≥ 38 px, 96 px side margins, one text animation at a time.
- Palette tokens only (EDIT_NOTES §0 — lead's cross-chunk mapping: c1 code to 235.94, political code after); ≤ 2 accents per frame; celadon is never a text colour.
- Default texture stack on every scene; light chromatic aberration (0.1–0.15) on photos/footage; credits: 13 px bottom-right for
  CC BY(-SA) and for fair-use press items ("© The New York Times", "UN Photo", "© HBO", "Wayne F. Miller / Magnum").
- Maps only from the kit (`assets/maps/kit/`) or the named fallbacks; never flat grey/beige relief.

### 3.6 Checks before hand-off
1. `npx --yes hyperframes@0.8.217 lint` → 0 errors (sandbox: `tools/make_sandbox.sh c3sNN`, then
   `cd work/c3sNN && python3 tools/build_index.py c3sNN --root .`).
2. `python3 tools/sync_audit.py compositions/c3sNN.html --transcript transcript_c3.json` → every text cue 0–120 ms before its word.
3. `npx --yes hyperframes@0.8.217 snapshot --at <every scene midpoint + first/last 0.1 s + Done+0.3> --no-end -o .snap/c3sNN` and LOOK
   at each frame with the words under it (picture = words? animation finished before the cut?).
4. `compositions/c3sNN.sfx.json` valid; `compositions/c3sNN.NOTES.md` (deviations, exported motif snippets, asset fallbacks).

## 4. Assembly (lead)
`python3 tools/build_master.py --prefix c3s --vo vo_c3.mp3 --len 602.02 --timeline assets/audio/c3/timeline.json --out index.html`,
lint, contact sheet of every scene midpoint with the transcript under each frame, picture render, fix, sound pass
(`.venv/bin/python tools/audio/place_sound.py --vo vo_c3.mp3 --transcript transcript_c3.json --len 602.02 --markers
'compositions/c3s0*.sfx.json' --cues project/c3/music_cuesheet.json --out assets/audio/c3`), final render → `renders/c3/c3_final.mp4`
(1080p) + `review/c3_720p.mp4`; verify VO loudness in the final = `vo_c3.mp3` (mix vs VO alone < 1 LU).
