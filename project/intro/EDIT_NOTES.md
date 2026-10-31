# EDIT NOTES — INTRO "Taiwan: the chip rivalry" (Searching Lessons), VO 0.00–275.06

Shot-by-shot plan for the intro chunk. Read with `project/intro/BRIEF.md` (Krish's binding rules), `MANUAL.md` (§10 overrides
older sections; §5 effects; §6/§6.1 reference layouts), `project/intro/analysis/BEATS.md` (beats, ASR fixes, cues),
`ASSETS_NEEDED.md` (asset IDs `E..` = exists, `N..` = needed), `SEGMENTS.md` (who builds what) and `DECISIONS.md`.
Prepared 2026-10-31 by the director / edit planner.

## 0. How to read this file

- **Times** = VO seconds (`vo_intro.mp3`), scene boundaries on word starts from `transcript_intro.json`.
  **66 scenes, IS001–IS066**, contiguous, 0.00 → 275.06, no gaps.
- **Text cue `@t`** = start of the spoken word; the text's first frame sits at `T(t) − 0.06` (0–120 ms before the word).
  Lines longer than one word are revealed **word by word** (each word its own literal `T()`), MANUAL §4.4.
- **Words** = the exact narration under the shot. **Why** = why the picture matches those words (Krish's rule, §10.1.3).
- **Ground**: `NIGHT` (dark/cinematic/archival photo full-frame), `PAPER` (paper_cream + folds), `GRID` (real scanned
  vintage graph / ruled paper — K+E 1960 catalogue sheets, ledgers; N10), `FACE` (face cam, clean). Rhythm rule: ≤ 3 in a
  row on the same ground; GRID and PAPER are also never more than 3 in a row *combined* (checked in §11).
- **FX** = MANUAL §5 numbers + §10 craft: `W` whip (`FX.whip`, give the direction), `FW` light-flash whip, `CA` cut on
  action, `PT` push-through (camera flies into an element that becomes the next shot), `PS` paper slide/torn-paper wipe,
  `FH` focus hunt (`FX.focusHunt`, once per scene max, after a fast zoom/push lands), `CS` `FX.chokeSettle` (rough reveal
  that settles). **No iris anywhere.** Easing: `FX.ease.out/inOut/in` wrapped in `FX.choppy(…,12)`; camera `FX.ease.cam`.
- **Glow**: `.halate` only on the scene's **hero** (named per scene as "hero"). Everything else `.clean`. Paper never glows.
- **Ref** = Krish's intro pack `D01–D15` (`references/style-images/intro/`) or older `R1–R12`; when neither fits, a
  "Pinterest-style idea" names a comparable layout to look up.
- **Palette** (`lib/palette.css`, swatch `references/palette_taiwan.png`): **red** `#e03f2c` = TSMC / Morris Chang ·
  **blue** `#1d5c9e` (sky `#9fc3e3` on night) = UMC / Robert Tsao · **celadon** `#9fc7b2` = Taiwan · **yellow** = highlighter
  or the one key number of a scene · everyone/everything else neutral (ink / bone / grey). Max two accents per frame.
- **Spellings on screen**: Robert Tsao (ASR "Cao/Sao/Xiao"), Morris Chang, UMC, TSMC, Hsinchu Science Park (ASR "Shin Shu
  Park"), Sam, Searching Lessons. Everything else = his words exactly; no text on slips (BEATS §2b).
- **Morris Chang's face is never visible before "Morris" @180.69.** Before that he is the **grey silhouette** (`N38`, a
  neutral ink/grey filled head-and-shoulders matte — not recognisable, never red).
- **Asset rule**: no photo or clip more than twice in the chunk (usage counted in ASSETS_NEEDED.md). Graphics/maps that
  are motifs (Taiwan relief, D06 board dots, D15 diagram, silhouette) may recur.
- **SFX** lines are object events (absolute VO s) → copy into `compositions/introNN.sfx.json` (vocabulary SEGMENTS §3.4).
- **Face cam**: `assets/facecam/fc_<start>.mp4` pre-cuts (clip t0 = VO time in the name; confirm lip sync — face-cam
  media time = VO − 0.026 s) or `input/Face Cam.mp4` with `data-media-start = VO − 0.026`. Never graded, never textured.
  Cut-out inserts: `remove-background` → layer order **room plate (bg.webm) → our graphic → narrator (fg.webm) → text**.

## 1. Act 0 — Cold open: the insight (0.00–15.52)
Music: textural pad + light pulse (Melting Glass family), no drums; swell into "the world" @14.80.

### IS001 · 0.00–1.12 · I001 · NIGHT
- **Words** "In 1983,"  **Why** the year is the whole line → a title card of the year.
- **FX** #8 streaks + #4 film title + #13 odometer (digits roll and lock) · **Ref** Pinterest idea: "retro film-title year
  card on black with anamorphic light streaks" (our s01 look).
- **Text** `1983` t-display 300 px, **hero halate**, odometer reels lock @0.32 (lock finishes by 0.70).
- **Camera** slow push 1.00→1.04. **Out** `FW` (light-flash whip, left) @1.06 into IS002.
- **SFX** 0.05 air_swell · 0.30 odometer_tick (0.4 s) · 1.04 whoosh_soft.

### IS002 · 1.12–5.28 · I001 · PAPER
- **Words** "Robert Tsao, CEO of Taiwanese chip company UMC,"  **Why** introduces the man, his title, his country, his
  industry and his company — each gets its own panel as it is named.
- **FX** #10 Vox layered backgrounds (s09 copy) + #12 torn edges · **Ref** Pinterest idea: "Vox cut-out portrait over
  tinted newspaper panels with label boxes".
- **Visual** Tsao cut-out (E01 `tsao_portrait_cc0.jpg` → remove-background, halftone, blue duotone `#1d5c9e`→paper) centre
  right; behind him panels slide in at 12 fps: Taiwan relief panel tinted celadon @2.96 (E10), chip-die macro panel @3.68
  (E21 `footage/wafer_die_pattern_macro.mp4`, a still frame or 1 s loop), UMC logo card @4.40 (N03, blue).
- **Text** `ROBERT` @1.12 + `TSAO` @1.60 (`.label-box` blue fill, bone text) · `CEO` t-label @2.40 · UMC logo @4.40
  (logo is the text; no extra word).
- **Camera** drift right 40 px; last 6 frames push 1.0→1.3 into the chip-die panel. **Out** `CA` (cut on that push).
- **SFX** 1.10 paper_slide · 2.94 paper_slide · 3.66 paper_slide · 4.38 pop_soft.

### IS003 · 5.28–7.68 · I002 · NIGHT
- **Words** "was walking around his factory floor."  **Why** a man walking a chip factory floor — literal.
- **FX** #1 archival footage + #16 treatment (fringe blur, vignette, chromaticAberration 0.12) + #14 light gate weave
  (amp 0.6 — it is 1960s colour film) · **Ref** —.
- **Assets** E07 `assets/intro/footage/fab_floor_manager_walks_rows.mp4` (15 s, colour archival semiconductor plant: a
  manager in a cardigan walks between rows of workers at benches) — use the walking section; 1 use (+ its freeze in IS004).
- **Text** none (the image says it).  **Camera** slow push 1.00→1.06.
- **Out** freeze frame (the walking man stops mid-stride @7.68) → IS004 continues on the same frame (no cut).
- **SFX** 5.30 air_swell (factory room tone starts; ambience marker `hum`, dur 4.9).

### IS004 · 7.68–10.16 · I002 · NIGHT
- **Words** "This is when he has a unique insight."  **Why** freeze on the man at the moment of the insight; light blooms
  behind his head = the insight.
- **FX** #8 light streaks (masked behind the cut-out walker) + #4 title · `CS` on the word.
- **Visual** freeze frame of IS003 desaturates and darkens to 40 % while the walker (cut-out of that frame, 🛠 `remove-background` on one still from E07)
  stays bright; streak canvas opens behind him from @8.80 ("unique").
- **Text** `insight` t-serif-i 150 px, **hero halate**, chokeSettle reveal @9.28.
- **Out** `W` up (vertical whip, streaks smear upward) @10.10.
- **SFX** 7.70 projector_click (freeze) · 9.26 chime_soft · 10.08 whoosh.

### IS005 · 10.16–15.52 · I003 · NIGHT
- **Words** "An insight that's going to change the future of his industry and the future of the world."  **Why** two
  scales: "his industry" = a silicon wafer (the chip industry); "the world" = the planet.
- **FX** #15 cutting-the-curve match cut (`FX.curveCut`): wafer → Earth share one zoom, cut at peak velocity @13.60 ("and");
  `FH` after the zoom lands (@14.4).
- **Assets** E20 `footage/wafer_closeup_purple.mp4` (round wafer on purple, archival — its circular edge is the match shape;
  alt E22 `photos/wafer_12in.jpg`) → N07 NASA Blue Marble globe (PD; round limb matches the wafer edge).
- **Text** `his industry` word-by-word: `his` @12.72, `industry` @12.96 (clean label) · `the world` `the` @14.64 + `world`
  @14.80 (**hero halate**, bone).
- **Out** `CA` (match move): the globe keeps rotating east and tilts flat into IS006's map plane.
- **SFX** 10.20 air_swell · 13.58 whoosh_big (curve cut) · 14.78 boom_low (very soft).

## 2. Act I — The boom (15.52–35.12)
Music: add a pulse/percussion stem; numbers land on 20.96 / 23.12 / 25.52; peak on "record" 32.64.

### IS006 · 15.52–20.48 · I004 · PAPER
- **Words** "You see, just a year earlier, Taiwan's exports of telephones to the United States"  **Why** Taiwan → telephones
  → shipped to the US: a map with Taiwan lit, a telephone, and a route to the US.
- **FX** #3 map + #20 callout · **Ref D10** (tilted close-up topo map with route lines) — vintage Pacific map tilted
  rotateX 28°, rotateZ −8°, lens blur at the far edge.
- **Assets** E30 `maps/formosa_1943_japanese_aviation_map.jpg` (+json; vintage colour map of Taiwan with flight lines —
  the opening close-up, tilted) → pull out to E31 `maps/pacific_relief_grey.jpg` (+json) graded to beige/paper for the
  trans-Pacific route · N09 1980s push-button telephone cut-out.
- **Text** `TAIWAN` t-label @17.52 (celadon underline) · `telephones` serif-i @18.96 · `UNITED` @19.76 `STATES` @20.16.
- **Visual** Taiwan fills celadon (watercolour edge) @17.52; telephone cut-out pops on Taiwan @18.96; dashed route line
  draws east across the Pacific @19.76 (red? no — **ink** dashed line; celadon dot travels).
- **Camera** track east along the route (cam ease). **Out** `W` right (direction of travel) @20.44.
- **SFX** 17.50 pop_soft · 18.94 pin_pop · 19.74 marker_long (route, 0.7 s) · 20.42 whoosh.

### IS007 · 20.48–24.88 · I005 · GRID
- **Words** "went from 4 million units a year to 24 million units."  **Why** the two numbers become two bars.
- **FX** #2 chart (bars 12 fps, watercolour tops) + #13 `FX.text.count` · **Ref D01** (bars + dashed threshold + ink
  "4 %" label box + halftone object at the base) — the halftone object is the telephone (N09) instead of the building.
- **Ground** K+E graph sheet scan (N10a), multiply.
- **Visual** bar A (ink/celadon) rises to "4" @20.96; dashed threshold line at its height; bar B rises 6× taller @23.12;
  halftone telephone cut-out sits across the base like D01's building.
- **Text** `4 million` above bar A: `4` @20.96, `million` @21.36 · `a year` t-label small @22.32 · label-box on bar B
  counts 4→24 @23.12, `million` @23.84.
- **Out** `CA` punch-in (1×→2×) on the label box, mid-move (begins @24.70).
- **SFX** 20.94 pop_soft · 21.0–21.5 dot_ticks (bar) · 23.10 counter_ticks (0.6 s) · 24.70 whoosh_soft.

### IS008 · 24.88–28.08 · I006 · GRID
- **Words** "That was a 6x increase in just 12 months."  **Why** the ratio between the two bars is the 6×; twelve months =
  twelve ticks.
- **FX** #13 count (1→6, 12 fps) + #2 · **Ref D01** continued (punched-in crop of the label box).
- **Text** `6×` t-display 360 px **yellow key number** @25.52 (count 1→6) · `increase` t-label @26.40 · `12 months`
  serif-i: `12` @27.12, `months` @27.52, with 12 calendar tick marks stepping in at 12 fps along the bar's side.
- **Out** `W` down (vertical whip toward the telephone at the base) @28.02.
- **SFX** 25.50 counter_ticks · 27.10 tick_soft ×12 (dot_ticks 0.4 s) · 28.00 whoosh.

### IS009 · 28.08–31.92 · I007 · NIGHT (lamp-lit document)
- **Words** "And UMC was making the chips inside those phones."  **Why** inside the phone = the circuit board; the chip on
  it = UMC's; a vintage telephone manual + UMC datasheet show exactly that.
- **FX** #5 document treatment (tilted 3D page, halftone, push to the detail) + #19 markup circle · **Ref** R9-like lamp
  pool on a dark desk; Pinterest idea: "vintage service-manual exploded view under a desk lamp".
- **Assets** N11a telephone service-manual exploded/board illustration (Bell System Practices / push-button set manual,
  archive.org) · N11b UMC telephone-dialer IC datasheet page (UM91xx / UM95xx, archive.org/bitsavers) — fallback a typeset
  datasheet-styled card "UMC" + pinout (no fake logos beyond the real UMC logo).
- **Text** `UMC` (blue label-box) @28.40 · markup circle (blue) round the chip @29.84 · `phones` serif-i @31.28.
- **Camera** push into the chip on the board then the datasheet slides in over it (12 fps). `FH` after the push (@30.3).
- **Out** `PS` (datasheet slides up, the chart paper is underneath) @31.86.
- **SFX** 28.10 lamp_click · 28.38 pop_soft · 29.82 marker_scratch · 30.40 paper_slide · 31.84 paper_slide.

### IS010 · 31.92–35.12 · I008 · PAPER
- **Words** "So it had record profits in its first full year."  **Why** a profit line hitting a record in year one.
- **FX** #2 line chart (path draw-on, era band) + rubber stamp · **Ref D05** (line chart + shaded era band + end labels).
- **Visual** **no axis values, no years** (narration gives none): UMC line (blue) draws up steeply; shaded band = "first full
  year"; dot pops at the peak; ink stamp `RECORD` lands (stamp, rough edge, settles) @32.64.
- **Text** `record profits` stamp @32.64 (`profits` @33.12) · band label `first full year` word-by-word @34.00/34.24/34.72.
- **Out** continuous (same chart, camera slides right) → IS011.
- **SFX** 32.62 stamp_thud · 33.0 marker_long (line, 0.8 s) · 34.0 pop_soft.

### IS011 · 35.12–40.40 · I009 · PAPER
- **Words** "But quickly, the phone boom died, and UMC's sales died with it."  **Why** two lines fall: the phone boom, then
  UMC's sales following it.
- **FX** #2 D05 continued + #19 markup arrow (down) · **Ref D05** (second line, "end labels").
- **Visual** a second line (ink, "phone boom") is revealed peaking over the band, then drops @37.44; UMC's blue line follows
  it down @39.44; a rough ink arrow traces the fall.
- **Text** `phone boom` end label: `phone` @36.64, `boom` @37.04 · `UMC's sales` blue end label `UMC's` @38.08, `sales` @38.88.
  ("died" is not written — the lines falling show it.)
- **Music** pull the rhythm out on "died" @37.44.
- **Out** `CA` — both lines fall off the bottom of frame; cut on the fall @40.36.
- **SFX** 37.42 boom_low (soft) · 39.42 marker_scratch · 40.34 whoosh_soft.

## 3. Act III — The idea: a foundry (40.40–69.09)
Music: new melodic layer on "profitable" 48.96; lift on "foundry" 61.57; confident on "good idea" 68.21.

### IS012 · 40.40–47.28 · I010 · NIGHT
- **Words** "This is when he realized that as a chip factory, it made no sense to make chips just for one product."
  **Why** a real chip factory; all its output funnelled into one telephone, then crossed out = "no sense".
- **FX** #1 footage plate + #16 + #19 Vox markups (arrows, cross) · **Ref** R-markup (`expected/layouts/markup-map_SC064.jpg`);
  Pinterest idea: "Vox markup arrows funnelling on archival footage".
- **Assets** E08 `footage/fab_hk_workers_microscope_rows_a.mp4` (rows of workers at microscopes — a chip factory; markups
  ride on it, slow it to 0.6× so the arrows read) — alt still: N05 1980s fab photo (Sandia/DOE, NIST — PD).
- **Text** `chip factory` t-label @42.40 (`factory` @42.80) · `one product` serif-i @46.16 (`product` @46.48).
- **Visual** bone markup arrows sweep from across the fab photo into ONE small telephone icon (N37) @46.16; a rough
  cross is drawn over the funnel @46.70 (after "product", so it is the conclusion, not a pre-empted word).
- **Camera** slow push 1.00→1.08. **Out** `W` left @47.22.
- **SFX** 42.38 tick_soft · 45.10 marker_long (arrows, 1.0 s) · 46.70 marker_scratch (cross) · 47.20 whoosh.

### IS013 · 47.28–53.12 · I011 · PAPER
- **Words** "The factory would be much more profitable if it was able to make chips for anything that was in demand."
  **Why** many products, each with demand, all fed by one factory = "anything in demand".
- **FX** #2 horizontal bars + serif title with italic emphasis · **Ref D04** (horizontal bars on paper, serif title,
  italic emphasis word).
- **Visual** title in t-serif; rows of product icons (N37: telephone, TV, calculator, computer, watch, game) with
  horizontal ink bars (no %); the telephone row first (from IS012), the other rows pop in @51.28 and bars grow @52.08.
- **Text** title word-by-word `much` @48.56 `more` @48.72 `profitable` @48.96 (italic, blue emphasis = UMC's factory) ·
  `anything` label @51.28 · `in demand` @52.08 (`demand` @52.32).
- **Out** `CA` — bars still growing as we cut @53.06.
- **SFX** 48.94 pop_soft · 51.26 dot_ticks (rows, 0.5 s) · 52.10 paper_rustle.

### IS014 · 53.12–58.05 · I012 · GRID
- **Words** "You see, at this point in 1983, this was a novel concept."  **Why** 1983 + a new idea → an engineer's
  idea card dated 1983, the idea sketched on it, "novel concept" highlighted.
- **FX** #18 highlighter + date stamp · **Ref** Pinterest idea: "engineer's notebook spread / idea sketch on graph paper".
- **Ground** ruled/graph notebook page scan (N10b). The card = Tsao's **idea card** (motif reused in IS036, IS040).
- **Visual** pencil-style ink sketch (drawn on, 12 fps): one factory box → arrows to many product icons (callback of IS013).
- **Text** date stamp `1983` (ink stamp, rough, settles) @54.80 · `a novel concept` t-serif-i word-by-word `a` @56.40
  `novel` @56.64 `concept` @57.12, yellow highlighter swipe on `novel concept` @56.70.
- **Out** `PS` — card slides up, a dictionary page underneath @57.99.
- **SFX** 54.78 stamp_thud · 55.2 pencil_scribble (0.8 s) · 56.68 highlighter_swipe · 57.95 paper_slide.

### IS015 · 58.05–63.49 · I013 · PAPER
- **Words** "There was no such thing as a pure play chip factory or foundry as we know of today."  **Why** a definition:
  the old dictionary knows "foundry" only as metal casting — the chip meaning "as we know of today" isn't there yet.
- **FX** #5 page treatment (tilted 3D page, halftone grows with the push) + #18 highlighter + #13 · **Ref** s06 newspaper
  method on a dictionary page.
- **Assets** N12 Webster's 1913 (or other PD) dictionary page with the "foundry" entry.
- **Text** typeset card over the page: `pure-play chip factory` word-by-word `pure` @59.73 `play` @60.13 `chip` @60.53
  `factory` @60.85 · `foundry` t-display 160 px ink @61.57 (CS reveal). Highlighter on the printed "Foundry" entry @61.57.
- **Camera** push to the entry, `FH` @62.2. **Out** `FW` (flash) @63.44.
- **SFX** 58.10 page_turn · 59.70 letter_ticks (0.8 s) · 61.55 highlighter_swipe · 63.42 whoosh.

### IS016 · 63.49–65.17 · I013 · NIGHT
- **Words** "It just didn't exist in the world."  **Why** the whole world map, scanned, with nothing on it.
- **FX** #3 map + #20 · **Ref** Pinterest idea: "dark world map with scanning radar sweep, empty".
- **Assets** E11 `assets/intro/maps/world_basemap_desat.jpg` (+json, + `world_countries.svg` for borders).
- **Text** `didn't exist` clean label: `didn't` @63.89, `exist` @64.29 · a single hollow pin pulses and fades @64.85 ("world").
- **Out** `PT` — camera dives toward Taiwan and through it into IS017.
- **SFX** 63.50 tone_blip (sweep) · 64.83 pin_pop (soft) · 65.12 whoosh_soft.

### IS017 · 65.17–69.09 · I014 · NIGHT · 2.5D #1
- **Words** "But Tsao could see the future and he knew this was a good idea."  **Why** Tsao himself, camera moving
  forward with him ("see the future"), "good idea" on the word.
- **FX** #17 2.5D (s10 method) + `FH` after the dolly stops (@68.0).
- **Assets** E01 `tsao_portrait_cc0.jpg` (2nd and last use) cut into layers: backdrop (display case, subject removed +
  blurred fill), Tsao, foreground vase (N-layer set 🛠, `layout.json`). Source is 1280×1921 — gatherer A to fetch the
  larger Commons original if one exists (≥ 3000 px preferred).
- **Text** `TSAO` (blue label-box) @65.41 · `the future` serif-i `the` @66.45 `future` @66.61 tucked behind Tsao's
  shoulder layer · `good idea` `good` @68.21 `idea` @68.45 (clean).
- **Out** `W` right @69.03.
- **SFX** 65.20 air_swell · 67.9 whoosh_soft (dolly stop) · 69.00 whoosh.

## 4. Act IV — The board and the condition (69.09–120.26)
Music: steady mid-tempo; hit/stop on "one condition" 93.65; darker mysterious texture under the executive 94.61–110.45.

### IS018 · 69.09–72.93 · I015 · NIGHT (archival footage)
- **Words** "So he goes to his board of directors to ask for their permission."  **Why** a man standing at a blackboard
  presenting to men around a boardroom table = going to the board to ask.
- **FX** #1 archival footage + #14 light weave + #16 · **Ref** Pinterest idea: "archival boardroom still with a serif
  lower-third".
- **Assets** E37 `footage/boardroom_blackboard_meeting_a.mp4` (1960s colour: presenter at a blackboard, table of
  listeners) — 1 use; `_b` is the reserve for IS032 if the D06 drain needs a cut-in.
- **Text** lower third t-serif word-by-word `his` @70.05 `board` @70.21 `of` @70.45 `directors` @70.61 · `permission`
  t-label @72.21. (Nobody is labelled Tsao — the footage is a stand-in for the scene, not a portrait.)
- **Camera** slow push 1.00→1.05. **Out** `CA` — the presenter's arm moves right; cut on the gesture into IS019's dot.
- **SFX** 69.10 projector_loop (dur 3.8) · 72.20 pop_soft · 72.88 whoosh_soft.

### IS019 · 72.93–77.65 · I016 · GRID
- **Words** "UMC was still a pretty new business at this point. It had launch just a year ago,"  **Why** a short timeline:
  UMC's start one tick ("a year ago") from "now". No year printed (narration gives none).
- **FX** #12 timeline (s08 axis + travelling dot) · **Ref** Pinterest idea: "ledger-paper timeline with one tick"; s08.
- **Ground** ruled ledger page (N10c).
- **Text** UMC logo (blue) @72.93 · `new business` serif-i `new` @74.53 `business` @74.77 · tick label `a year ago`
  word-by-word `a` @76.93 `year` @77.01 `ago` @77.25 (slip "launch" not written).
- **Out** `W` up @77.60.
- **SFX** 72.91 pop_soft · 74.5 dot_slide · 77.0 tick_soft · 77.58 whoosh.

### IS020 · 77.65–82.29 · I017 · NIGHT
- **Words** "and now Tsao needed their permission to reorient the whole thing."  **Why** "reorient the whole thing" → the
  whole UMC building literally turns on a compass rose.
- **FX** #10 + #13 + `CS` · **Ref** Pinterest idea: "engraved compass rose with an object rotating on it (Vox explainer)".
- **Assets** N14 compass-rose engraving (PD) · E26 `photos/umc_fab8ab.jpg` (UMC building with the logo
  disc) cut out (hand polygon mask, `tools/cut_layers.py`), halftone, blue tint.
- **Text** `Tsao` small blue label @78.21 · `permission` t-label @79.41 · `reorient` t-display, chokeSettle @80.45 (clean;
  the hero is the rotating building — no halate on text).
- **Visual** the building rotates 90° on the compass (FX.ease.inOut, 1.6 s, 12 fps) from @80.45.
- **Out** `CA` — rotation continues, its angle matches the slope of IS021's painting.
- **SFX** 78.20 tick_soft · 80.43 gate_creak (soft, rotation) · 82.20 whoosh_soft.

### IS021 · 82.29–85.09 · I018 · NIGHT (painting)
- **Words** "He knew this was going to be an uphill battle."  **Why** the idiom made literal — Sisyphus pushing a boulder
  uphill (colour oil painting, Krish's painting rule).
- **FX** #16 painting plate (fringe, slow push) + #19 rough arrow up the slope.
- **Assets** N13 Titian, *Sisyphus* (1548–49, Prado, PD).
- **Text** `uphill battle` serif-i clean `uphill` @83.89 `battle` @84.37.
- **Out** `FW` (flash) @85.04.
- **SFX** 82.30 air_swell · 83.0 marker_long (arrow) · 85.02 whoosh.

### IS022 · 85.09–92.13 · I019 · PAPER
- **Words** "Luckily for him, though, the board was pretty excited about this new idea, and they almost told him yes on the
  spot."  **Why** the board as a semicircle of 12 seats filling blue = excited; a YES stamp hovers but doesn't land = "almost".
- **FX** #2 dot matrix + stamp + #18 · **Ref D06** (parliament semicircle + highlighted title). **Motif master** for
  IS032, IS035, IS024.
- **Visual** 12 grey seat-dots placed on the arc at 12 fps from @86.37, then fill blue clockwise @87.57.
- **Text** title word-by-word t-serif `the` @86.37 `board` @86.61 `was` @87.01 `pretty` @87.25 `excited` @87.57 (italic,
  blue) · `almost` serif-i @89.81 · `YES` ink stamp, hovering above the paper with shadow, @90.61 (never lands).
- **Out** continuous — camera tilts down off the semicircle (begins @91.9) → IS023 (segment boundary, see SEGMENTS).
- **SFX** 87.55 dot_ticks (0.8 s) · 90.60 whoosh_soft (stamp lifts) · 91.9 paper_rustle.

### IS023 · 92.13–94.61 · I020 · PAPER
- **Words** "But they ended up giving him one condition."  **Why** fine print: an asterisk and a single footnote.
- **FX** #13 + #18 · **Ref** Pinterest idea: "contract fine-print footnote, asterisk callout".
- **Visual** the hovering YES gains an asterisk `*`; camera finishes tilting to the bottom of the page where a footnote rule
  draws.
- **Text** `* one condition` t-serif-i `one` @93.65 `condition` @93.97 (yellow highlighter under it @94.0).
- **Music** hit/stop on @93.65.  **Out** `W` left @94.55.
- **SFX** 93.63 pop_soft · 94.0 highlighter_swipe · 94.53 whoosh.

### IS024 · 94.61–99.57 · I021 · PAPER
- **Words** "Some board members had been getting advice from a high level chip executive in the United States."  **Why**
  a relationship diagram: board members ← advice ← an unnamed executive ← in the US.
- **FX** #2/#19 diagram (circles, arrows drawn on) · **Ref D15** (portrait circles + arrows + labels on paper). **Motif
  master** for IS027, IS042.
- **Visual** circle 1 = three board seat-dots (from D06, blue) @94.85; circle 2 = **grey silhouette** (N38) @97.89;
  circle 3 = US outline (E12 `us_beige.svg`, neutral) @98.69; arrows drawn on (dashoffset) with labels.
- **Text** `board members` t-label `board` @94.85 `members` @95.25 · arrow label `advice` @96.29 · `chip executive`
  `chip` @97.57 `executive` @97.89 · `United States` `United` @98.69 `States` @99.01.
- **Out** `CA` — camera pushes into the silhouette circle (begins @99.3).
- **SFX** 94.84 pop_soft · 96.28 marker_long (arrow) · 97.88 pop_soft · 98.68 pop_soft.

### IS025 · 99.57–103.97 · I022 · NIGHT
- **Words** "This guy was the most respected Chinese American in the chip business in the whole world."  **Why** the
  man is a mystery — a spotlit silhouette, his reputation spelled out.
- **FX** #4 + #8 (dim streaks behind) · **Ref** Pinterest idea: "true-crime documentary mystery silhouette in a spotlight".
- **Visual** silhouette (N38) under a warm spotlight cone, ghost world map behind at 8 %.
- **Text** `most respected` serif-i `most` @100.37 `respected` @100.61 (**hero halate** on "most respected") ·
  `Chinese-` @101.25 `American` @101.73 t-label · `chip business` t-label `chip` @102.37 `business` @102.77.
- **Out** `W` down @103.91.
- **SFX** 99.58 lamp_click · 100.6 chime_soft (very low) · 103.90 whoosh.

### IS026 · 103.97–110.45 · I023 · GRID
- **Words** "He was managing a 25,000 people global chip department in one of the biggest companies in the world."
  **Why** 25,000 people as an isotype grid; then the grid shrinks into one floor of a giant (unnamed) corporation.
- **FX** #2 isotype + #13 count · **Ref D03** (isotype grid with labels; leader icon top-right).
- **Visual** 100 person icons (N38b, 1 icon = 250 people) fill row by row at 12 fps from @104.85; the leader icon (top
  right) is the grey silhouette; @108.37 the grid scales down into one lit window of a ghosted, anonymous skyscraper
  outline (no logo — narrator doesn't name the company).
- **Text** `25,000` t-display **yellow key number**, count 0→25,000 @104.85 · `people` t-label @105.81 · `global chip
  department` word-by-word `global` @106.21 `chip` @106.61 `department` @107.09 · `biggest companies` serif-i `biggest`
  @108.37 `companies` @108.93.
- **Out** `PS` (sheet slides left) @110.40.
- **SFX** 104.84 counter_ticks (1.0 s) · 104.9 dot_ticks (1.2 s) · 108.36 whoosh_soft (shrink) · 110.38 paper_slide.

### IS027 · 110.45–120.26 · I024–I025 · PAPER
- **Words** "So the board tell Tsao to go share his plan with this advisor, and if he approves, then the board will give
  him the permission. To reorient the business."  **Why** the approval chain, step by step: Tsao → plan → advisor →
  approves → board → permission.
- **FX** #19 markups (check marks) + diagram · **Ref D15** variant (camera pans along the chain; different arrangement:
  left-to-right row instead of triangle).
- **Visual** Tsao circle (E02 `tsao_advisor_cc0.jpg`, blue ring) @111.81; a folder labelled "plan" slides along the arrow
  @113.33 to the silhouette circle `advisor` @114.05; rough check ✓ @115.49; arrow to board circle, ✓ @116.61; label-box
  `permission` @117.73. On the repeated "to reorient the business" (slip) **no new text**: the small compass+building icon
  from IS020 rotates once beside "permission" (@118.82).
- **Text** `Tsao` @111.81 · `plan` @113.33 · `advisor` @114.05 · `approves` serif-i @115.49 · `board` @116.61 ·
  `permission` @117.73.
- **Camera** pans left→right with the chain (cam ease). **Out** `CA` — the folder keeps moving and becomes the plane of IS028.
- **SFX** 111.80 pop_soft · 113.30 paper_slide · 115.48 marker_scratch · 116.60 marker_scratch · 117.72 pop_soft.

## 5. Act V — New York (120.26–134.98)
Music: travelling pulse; brightest moment on "top of the world" 134.18.

### IS028 · 120.26–123.30 · I026 · PAPER
- **Words** "After hearing this, Tsao is on the very next flight to New York"  (New York lands in IS029) **Why** a flight
  line from Taiwan heading to New York.
- **FX** #3 map + `FH` after the camera whip-pan lands · **Ref D10** variant (same tilted vintage map look as IS006,
  different crop — wide North Pacific, great-circle arc to the US East Coast).
- **Assets** E31 `maps/pacific_relief_grey.jpg` (maps are motifs; same grade as IS006) · plane = our small ink airliner icon (🛠 SVG).
- **Text** `Tsao` blue label on the departing dot @121.22 · `the very next flight` word-by-word `very` @122.34 `next`
  @122.58 `flight` @122.82.
- **Out** `FW` (flash) as the plane reaches New York @123.26.
- **SFX** 120.30 paper_rustle · 122.80 whoosh_big (flight line) · 123.24 whoosh.

### IS029 · 123.30–125.30 · I026 · NIGHT (poster)
- **Words** "New York to talk with this executive."  **Why** New York as a vintage colour travel poster; the executive
  waiting in it as the silhouette.
- **FX** #16 poster plate + #10 · **Ref** Krish's "vintage poster" rule; Pinterest idea: "WPA travel poster with a
  silhouette in the window".
- **Assets** N22 PD New York poster (WPA / 1939 World's Fair, LOC via Commons).
- **Text** `NEW YORK` t-display `NEW` @123.30 `YORK` @123.54 (**hero halate**) · silhouette (N38) slides in @124.50.
- **Out** `W` right @125.24.
- **SFX** 123.28 chime_soft · 124.48 paper_slide · 125.22 whoosh.

### IS030 · 125.30–131.70 · I027 · PAPER
- **Words** "The meeting goes really well. They even have dinner together discussing Tsao's proposal in detail."
  **Why** an overhead dinner table for two: menu, plates, the proposal between them.
- **FX** #12 collage (stop-motion cards, 12 fps) · **Ref** Pinterest idea: "flat-lay dinner-table collage, overhead".
  **Motif master** for IS042.
- **Assets** N23 PD New York restaurant menu (NYPL "What's on the Menu?") + two place settings (PD photo or our
  illustration) · Tsao circle chip N02a (E01/E02 are each used twice already) · silhouette (N38) across the table.
- **Text** `meeting` t-label @125.46 · `dinner` serif-i @127.62 · `Tsao's proposal` blue label-box `Tsao's` @129.14
  `proposal` @130.02 (the proposal folder slides between the plates).
- **Out** `CA` — camera rises off the table (begins @131.4) into the sky of IS031.
- **SFX** 125.44 paper_slide · 127.60 paper_slide · 128.4 tick_soft (glass) · 130.00 paper_slide.

### IS031 · 131.70–134.98 · I028 · NIGHT
- **Words** "After the meeting, he flies back home feeling on top of the world."  **Why** a plane climbing above the
  clouds, home-bound; "on top of the world" literally above the clouds.
- **FX** #1 archival footage + #14 weave → #3 cloud fly-through (`assets/maps/clouds`) + #8 streaks.
- **Assets** E23 `footage/jet_707_takeoff_hongkong.mp4` (a 707 climbing out, archival colour — 131.70–133.8) → camera
  rises into E13 `assets/maps/clouds/` above which the hero line sits (133.8–134.98).
- **Text** `home` t-label @133.30 · `on top of the world` serif-i word-by-word `on` @134.02 `top` @134.18 `of` @134.42
  `the` @134.50 `world` @134.58 — **hero halate** on this line.
- **Out** `CA`/hard cut on the shock @134.98 (music cut) while the plane is still climbing.
- **SFX** 131.72 wind (dur 3.2) · 133.28 whoosh_soft · 134.17 chime_soft.

## 6. Act VI — The cold shoulder (134.98–157.22)
Music: cut the bed on "shock" 135.54; uneasy drone; sad resolve on "dropping" 156.02.

### IS032 · 134.98–140.74 · I029 · PAPER
- **Words** "But to his shock, when he gets back, he feels like the board is not really feeling the idea anymore."
  **Why** the same board semicircle (IS022); the blue (excited) dots drain to grey one by one.
- **FX** #2 · **Ref D06** variant (reverse fill, grey; title replaced by a single label).
- **Text** `the board` t-label @137.78 · `anymore` serif-i @140.02 (small, grey).
- **Visual** dots drain anticlockwise at 12 fps from @137.78, last one at @140.0.
- **Out** `W` left @140.68.
- **SFX** 135.52 boom_low (very soft) · 137.8 dot_ticks (2.0 s, descending) · 140.66 whoosh.

### IS033 · 140.74–144.82 · I030 · NIGHT
- **Words** "He tries to find out what had happened, but he's getting stonewalled."  **Why** literal stonewall: a stone
  wall builds in front of Tsao.
- **FX** #10 + #13 + `CS` · **Ref** Pinterest idea: "Vox cut-out vs. a wall building brick by brick".
- **Assets** E03 `photos/tsao_rally_2023.jpg` (full-figure cut-out, crop above the hand-held mic, blue duotone) · N16 stone-wall photo (layers cut per course).
- **Text** `what had happened` serif-i word-by-word `what` @141.94 `had` @142.18 `happened` @142.42 · `STONEWALLED`
  t-display rough chokeSettle on the wall @143.86 (clean, no glow).
- **Out** `CA` — the last stone slams in @144.6 → cut on its impact.
- **SFX** 142.9–144.6 stamp_thud ×4 (soft, stones) · 144.60 boom_low.

### IS034 · 144.82–149.38 · I031 · PAPER
- **Words** "He's just being told to drop the idea and run the business how he was doing already."  **Why** an
  instruction delivered as a telegram.
- **FX** #13 typewriter word reveal + document · **Ref D08** (telegram).
- **Assets** N17 typeset telegram (our fonts on paper texture; ink/blue header — never red; no seals or signatures).
- **Text** typed word-by-word: `DROP` @145.94 `THE` @146.34 `IDEA` @146.42 / `RUN` @146.98 `THE` @147.30 `BUSINESS`
  @147.38 `HOW` @147.86 `HE` @148.10 `WAS` @148.34 `DOING` @148.50 `ALREADY` @148.82 (no "STOP" — not spoken).
- **Out** `PS` (telegram slides down out of frame) @149.32.
- **SFX** 145.9–149.0 letter_ticks (typewriter, per word) · 149.30 paper_slide.

### IS035 · 149.38–154.42 · I032 · NIGHT
- **Words** "In Taiwan, especially 1984, you did not do much without your board."  **Why** Taiwan, the year, and the
  board's grip: the island with the board's seats around it.
- **FX** #3 map (R12 relief, celadon fill with halftone + glowing edge; burn reveal) + #4 · **Ref R12**.
- **Assets** E09/E10 `assets/intro/maps/taiwan_relief_grey.jpg` + `taiwan_mask.png`.
- **Text** `TAIWAN` t-label @149.54 (fill burns in celadon) · `1984` t-display **hero halate** @150.82 · @153.78 the 12
  D06 seat-dots ring the island (`board` t-label @153.78).
- **Out** `W` down @154.36.
- **SFX** 149.52 burn_crackle (1.2 s) · 150.80 chime_soft · 153.76 dot_ticks · 154.34 whoosh.

### IS036 · 154.42–157.22 · I033 · GRID
- **Words** "So Tsao ended up dropping the idea."  **Why** the idea card (IS014) is literally dropped.
- **FX** #12 card physics (12 fps) · **Ref** Pinterest idea: "paper card falling into an archive drawer".
- **Text** `Tsao` blue label @154.82 · `dropping the idea` serif-i `dropping` @156.02 `the` @156.50 `idea` @156.66.
- **Visual** the 1983 idea card un-pins and falls out of the bottom of frame from @156.02.
- **Out** `CA` — cut on the fall (@157.16).
- **SFX** 156.00 paper_flip · 157.10 paper_slide.

## 7. Act VII — The betrayal reveal (157.22–185.01)
Music: rising ostinato 157–171; near-silence under "Guess who" (face cam); hit on "Morris" 180.69, second on "TSMC" 183.89.

### IS037 · 157.22–160.74 · I034 · NIGHT
- **Words** "Then two years later, a new chip company breaks ground"  **Why** a groundbreaking ceremony — shovels in dirt.
- **FX** #1 + #14 gate weave/flicker + #4 · **Ref** Pinterest idea: "archival groundbreaking photo with a time-jump title".
- **Assets** N18 PD groundbreaking photo/footage (ceremonial shovels, no readable signage).
- **Text** `TWO YEARS LATER` t-label word-by-word `TWO` @157.54 `YEARS` @157.78 `LATER` @158.10 · `a new chip company`
  serif-i `new` @158.74 `chip` @158.98 `company` @159.38 · `breaks ground` `breaks` @159.86 `ground` @160.34.
- **Out** `W` down (with the shovel thrust) @160.68.
- **SFX** 157.30 projector_loop (dur 3.4) · 160.30 stamp_thud (shovel, soft) · 160.66 whoosh.

### IS038 · 160.74–162.74 · I034 · PAPER
- **Words** "across the street from UMC."  **Why** a street map: UMC on one side, the new site across the street.
- **FX** #3 old map + #18 yellow marker + #20 · **Ref D09** (old city map, tilted).
- **Assets** E32 `maps/hsinchu_shinchiku_1945_us_army_city_plan.jpg` (US Army city plan, PD; 3840×3243) — crop the town
  grid, tilted like D09; needs a pixel position for the UMC plot and the site across the street (gatherer C json).
- **Visual** UMC plot outlined blue @161.86; yellow marker stroke drawn across the street @160.74; the new site hatched in
  **ink with "?"** (not red — the company is unnamed until 183.89).
- **Text** `across the street` `across` @160.74 `the` @161.22 `street` @161.30 · `UMC` blue @161.86.
- **Out** `PT` — camera pulls up and the map fades into the dark ghost map of IS039.
- **SFX** 160.72 marker_long · 161.84 pin_pop.

### IS039 · 162.74–168.18 · I035 · NIGHT
- **Words** "It would make chips for anyone who wanted it, and it would never sell a product of its own."  **Why** a
  flow diagram: orders from anyone flow in, chips flow back out; its own product slot stays empty.
- **FX** #2 Sankey + #19 cross · **Ref D11** (dark Sankey money-flow over a ghost map).
- **Visual** ghost world map (E11, 6 %); one central block (neutral ink-grey, "?") ; 8 inflow ribbons from many customer
  icons (N37) @164.02, chips return along the same ribbons; @166.26 an empty dashed box "own product" gets a rough cross @167.70.
- **Text** `anyone` t-label @164.02 · `never` serif-i @166.26 · `of its own` `own` @167.70.
- **Out** `W` right @168.12.
- **SFX** 164.00 whoosh_soft (flows) · 166.24 tick_soft · 167.68 marker_scratch · 168.10 whoosh.

### IS040 · 168.18–170.98 · I036 · GRID
- **Words** "It was like Tsao's plan, bar for bar."  **Why** Tsao's idea card laid over the new company's plan — line for
  line; highlighter bars stack = "bar for bar".
- **FX** #18 highlighter + overlay · **Ref** Pinterest idea: "light-table overlay of two documents".
- **Text** `Tsao's plan` blue label `Tsao's` @168.74 `plan` @169.46 · `bar for bar` serif-i `bar` @169.86 `for` @170.26
  `bar` @170.50, each `bar` triggers a yellow highlighter bar across matching lines.
- **Out** `CA` → face cam (cards still sliding) @170.98.
- **SFX** 168.72 paper_slide · 169.84 highlighter_swipe · 170.48 highlighter_swipe.

### IS041 · 170.98–173.86 · I037 · FACE — insert 1/6 (2.88 s)
- **Words** "Guess who was the founder and CEO"  **Why** he asks the viewer directly.
- **FX** cut-out layering: room plate → graphic → narrator → text.
- **Assets** `assets/facecam/fc_170.5.mp4` → `remove-background` → `fc_170.5_fg.webm` + `_bg.webm` (N32).
- **Graphic behind him** (where the shelves are): an office-door nameplate (ink on frosted glass) reading `FOUNDER & CEO`
  with an empty name line and the grey silhouette, slides in at 12 fps @172.18.
- **Text** `founder` t-label @172.18 · `CEO` @173.14 (left third, clean).
- **Out** `W` left @173.80.
- **SFX** 172.16 paper_slide (very soft) · 173.78 whoosh.

### IS042 · 173.86–180.05 · I037–I038 · PAPER
- **Words** "of this new company? None other than that same executive that Tsao met with. In New York."  **Why** callback:
  the "?" site links to the advisor silhouette (D15), then to the New York dinner table where they met.
- **FX** #19 arrow + #12 · **Ref D15** callback → IS030 collage callback (2nd use of the dinner collage).
- **Text** `same executive` serif-i `same` @176.42 `executive` @176.74 · `Tsao` blue @177.54 · `New York` t-label `New`
  @179.25 `York` @179.57.
- **Visual** arrow drawn from the "?" to the silhouette circle @176.42; camera pans to the dinner table @178.2; silhouette
  in the chair across from Tsao glows faintly.
- **Out** `PT` — camera pushes into the silhouette until it fills the frame (@179.9) → IS043.
- **SFX** 176.40 marker_long · 178.20 whoosh_soft · 179.90 air_swell.

### IS043 · 180.05–185.01 · I039 · NIGHT — the reveal
- **Words** "His name was Morris Chang, and the new company we're talking about is TSMC."  **Why** the silhouette becomes
  Morris Chang on "Morris"; the company becomes TSMC on "TSMC".
- **FX** #3 burn reveal (red burn ring eats the silhouette, s02 burn method on the portrait) + #4 + `FH` after the burn.
- **Assets** E24 `photos/chang_2018.jpg` (1920×1280, Chang speaking — crop head & shoulders, mic kept low in frame; red
  duotone + halftone; the silhouette matte N38 is cut from this same crop so the burn reveal lines up) · N04 TSMC logo (red).
- **Text** `MORRIS` @180.69 `CHANG` @181.25 t-display **hero halate** (red-tinted halation) · TSMC logo stamps @183.89.
- **Music** hit @180.69, second hit @183.89.
- **Out** `PS` torn-paper wipe from the right (starts @184.8; segment boundary).
- **SFX** 180.67 burn_crackle (1.4 s) · 180.70 boom_low · 183.87 stamp_thud · 184.80 paper_tear.

## 8. Act VIII — The rivalry and its stakes (185.01–246.18)
Music: full layered bed; lift on "superpower" 194.29; drop under the personal lines 196–210; rebuild through Hsinchu.

### IS044 · 185.01–190.61 · I040 · PAPER
- **Words** "This betrayal gives to a rivalry that has not died down to this very day."  **Why** the two men face off —
  betrayal, then rivalry, running "to this very day".
- **FX** #12 torn edges + #13 + `CS` · **Ref** Pinterest idea: "vintage boxing / fight-card poster" (Krish's poster rule).
- **Assets** E24 `chang_2018.jpg` (2nd use) right, red · E02 `tsao_advisor_cc0.jpg` (2nd use) left, blue · torn seam between.
- **Text** `BETRAYAL` rough red-ink stamp @185.17 (chokeSettle) · replaced by `RIVALRY` @186.93 (ink, both colours
  split) · `to this very day` serif-i `to` @189.01 `this` @189.25 `very` @189.57 `day` @189.89 (slip "gives to" never written).
- **Out** `CA` — the halves slide apart; the seam becomes the two lines of IS045.
- **SFX** 185.15 stamp_thud · 186.91 paper_tear · 189.88 tick_soft · 190.50 whoosh_soft.

### IS045 · 190.61–196.61 · I041 · NIGHT
- **Words** "And that rivalry has built Taiwan superpower that we know of today."  **Why** two rival lines (red/blue)
  climbing together over Taiwan until it is a "superpower".
- **FX** #2 line draw-on + #3 ghost map · **Ref D13** (dark line chart over a ghost map). No axis values, no years.
- **Text** `rivalry` @191.17 (red/blue split letters) · `TAIWAN` celadon t-label @192.69 · `SUPERPOWER` t-display
  **hero halate** @194.29 (don't write the swallowed words) · end dot pops @196.05 ("today").
- **Out** `W` up @196.55.
- **SFX** 191.16 marker_long (lines) · 194.28 boom_low · 196.04 pop_soft · 196.53 whoosh.

### IS046 · 196.61–198.93 · I042 · FACE — insert 2/6 (2.32 s)
- **Words** "That's the story I want to share with everyone."  **Why** a personal promise to the viewer.
- **Assets** `fc_195.8.mp4` → fg/bg (N32). **Graphic behind him**: the red and blue lines of IS045 continue drawing
  across the shelf area (graphic only, no photos).
- **Text** `the story` t-serif-i @197.09 (clean, lower right).
- **Out** `CA` — the lines exit right as we cut @198.93.
- **SFX** 198.90 whoosh_soft.

### IS047 · 198.93–201.89 · I042 · NIGHT
- **Words** "It's one of the greatest business stories ever,"  **Why** a great story = an old hardcover book whose title
  is his line.
- **FX** #18 highlighter + #16 · **Ref** Pinterest idea: "vintage cloth-bound book cover, gold-stamped title".
- **Assets** N34 PD photo of an old hardcover on a dark desk (title area blank/cleaned).
- **Text** stamped title word-by-word `one` @199.17 `of` @199.33 `the` @199.49 `greatest` @199.65 `business` @200.29
  `stories` @200.77 `ever` @201.41; yellow highlighter on `greatest` @199.70.
- **Out** `FW` @201.84.
- **SFX** 199.0 lamp_click · 199.68 highlighter_swipe · 201.82 whoosh.

### IS048 · 201.89–206.77 · I043 · PAPER
- **Words** "and I think it's the story that most people don't know too much about, especially in the West."  **Why**
  people who don't know (grey icons with "?") across a beige world map, the West highlighted.
- **FX** #3 beige map + #2 people dots · **Ref R11** (muted beige map, region fill, leader labels).
- **Assets** E11 world map in beige grade (beige grade of the same file).
- **Text** `most people` t-label `most` @203.57 `people` @203.89 · `the West` serif-i `the` @206.05 `West` @206.21
  (Americas + Europe tint ink-grey; Taiwan a tiny celadon dot).
- **Out** `CA` (graphic hand-off): the map shrinks onto the shelf behind the narrator of IS049.
- **SFX** 203.55 dot_ticks · 206.20 pop_soft.

### IS049 · 206.77–209.73 · I044 · FACE — insert 3/6 (2.96 s)
- **Words** "By the end of this, I think you'll agree with me when I say"  **Why** addresses the viewer's future opinion.
- **Assets** NEW pre-cut needed: `fc_206.5.mp4` (206.5–210.0) → fg/bg (N32). **Graphic behind him**: the beige world map
  from IS048 (shrunk), which pushes into Taiwan as he speaks.
- **Text** `agree` t-label @208.53 with a small rough ✓ markup.
- **Out** `W` right @209.67.
- **SFX** 208.52 marker_scratch (✓) · 209.65 whoosh.

### IS050 · 209.73–214.37 · I044 · NIGHT · 2.5D #2
- **Words** "that Taiwan wouldn't be the country it is today if it wasn't for this rivalry."  **Why** Taiwan today
  (Taipei skyline) in depth; the rivalry colours under it.
- **FX** #17 2.5D (sky / skyline / foreground layers, dolly) + `FH` at the stop.
- **Assets** N25 modern Taipei skyline photo ≥ 3000 px + layer set 🛠.
- **Text** `Taiwan` celadon t-label @209.97 · `today` serif-i @211.97 (tucked behind the skyline layer) · `rivalry`
  @213.49 red/blue split.
- **Out** `CA` — dolly continues into IS051's panels.
- **SFX** 209.75 air_swell · 213.0 whoosh_soft.

### IS051 · 214.37–218.37 · I045 · NIGHT
- **Words** "TSMC would not be a world renowned company if it wasn't for these"  **Why** TSMC's real fabs, the TSMC name,
  "world renowned".
- **FX** #10 Vox layered backgrounds (red-tinted panels drifting) · **Ref** s09 / R- Pinterest idea "corporate
  collage of tinted building panels".
- **Assets** E27 `photos/tsmc_fab5.jpg`, E28 `photos/tsmc_fabs_hsinchu_01.jpg`, E29 `photos/tsmc_rd_night.jpg` (red-tinted
  panels) · N04 TSMC logo (2nd use).
- **Text** TSMC logo @214.37 · `world renowned` serif-i `world` @215.89 `renowned` @216.29.
- **Out** `PS` @218.31.
- **SFX** 214.35 pop_soft · 215.0 paper_slide ×2 · 218.30 paper_slide.

### IS052 · 218.37–222.93 · I045 · GRID
- **Words** "two men spending decades trying to one up each other in their businesses."  **Why** two bars topped with the
  two men's portraits, leap-frogging each other over decades.
- **FX** #2 bars with portrait circles · **Ref D02** (ranked bars topped by circular portraits) — two bars only, heights
  swap 4 times.
- **Assets** E25 `photos/chang_award.jpg` (crop to Chang, red ring) · N02b Tsao (blue ring).
- **Text** `two men` t-label `two` @218.37 `men` @218.69 · `decades` serif-i @219.73 (decade ticks along the base, no years)
  · `one up` `one` @220.69 `up` @221.09 (each jump on a 12 fps step).
- **Out** `W` up @222.87.
- **SFX** 218.36 pop_soft ×2 · 219.8–222.0 dot_ticks ×4 (jumps) · 222.85 whoosh.

### IS053 · 222.93–228.61 · I046 · NIGHT
- **Words** "And of course, if all of that did not happen, Taiwan would not have Hsinchu Park,"  **Why** from Taiwan down
  to the park itself, highlighted from above.
- **FX** #3 map push (Taiwan relief → satellite) + #20 + `FH` after the push · **Ref D14** (satellite view, highlighted
  district, yellow route).
- **Assets** E09/E10 Taiwan relief (motif) → E33 `maps/hsinchu_s2cloudless2016.jpg` (+json; EOX Sentinel-2 cloudless,
  CC BY 4.0 — on-screen credit) · park outline + UMC/TSMC plots traced from E34 `maps/hsinchu_park_osm_z16.jpg` (+json, ODbL).
- **Text** `TAIWAN` celadon @225.81 · `HSINCHU` @227.09 + `SCIENCE PARK` @228.13 (lands with "Park"; full correct name).
- **Visual** park outline fills celadon @227.09; yellow route = the main road through the park drawn on; tiny blue (UMC)
  and red (TSMC) plots inside the park (both are there — two accents only).
- **Out** `CA` — the satellite card splits into two cards (IS054).
- **SFX** 225.80 whoosh (push) · 227.08 marker_long · 228.10 pin_pop.

### IS054 · 228.61–233.49 · I047 · PAPER
- **Words** "which, according to Taiwanese leader, is a replica of the Silicon Valley."  **Why** the "replica": Hsinchu
  Science Park beside a pictorial Silicon Valley map, joined by "=".
- **FX** #12 cards + #19 · **Ref** Pinterest idea: "side-by-side pictorial map comparison, 'equals' sign".
- **Assets** N27a pictorial Silicon Valley / Palo Alto map (PD/CC) — fallback `assets/maps/old/usgs_palo_alto_1899_topo.jpg`
  · E35 `photos/hsp_40th.jpg` (Hsinchu Science Park
  40th-anniversary roadside sign/gate).
- **Text** quote attribution `— a Taiwanese leader` serif-i `Taiwanese` @229.57 `leader` @230.29 (no name) · `replica`
  t-display ink @231.17 with a drawn "=" · `Silicon Valley` `Silicon` @232.13 `Valley` @232.85.
- **Out** `FW` @233.44.
- **SFX** 228.62 paper_slide ×2 · 231.16 marker_scratch · 233.42 whoosh.

### IS055 · 233.49–240.18 · I048 · NIGHT
- **Words** "Now I'm sure you guys know this. Countless countries have tried recreating the Silicon Valley in their own
  borders."  **Why** many countries light up with little Silicon-Valley stamps inside their borders.
- **FX** #3 map + #20 · **Ref** Pinterest idea: "dark world map with many pins popping, country borders drawing".
- **Assets** E11 world map (dark) · Silicon Valley stamp icon 🛠 (from N27a).
- **Text** (aside 233.49–235.09: no text) · `countless countries` t-label `Countless` @235.09 `countries` @235.65 ·
  `recreating` serif-i @236.69 · `Silicon Valley` `Silicon` @237.49 `Valley` @238.13 · borders draw on @238.85
  (`own borders`: `own` @239.01 `borders` @239.25).
- **Out** continuous (same map) → IS056.
- **SFX** 235.08 map_pin ×12 (staggered 1.2 s) · 238.84 marker_long.

### IS056 · 240.18–247.86 · I049–I050 · NIGHT
- **Words** "And pretty much all of them have failed. And these two people were big reasons behind that. So let's get to that
  story."  **Why** the stamps get crossed out; Taiwan stays; the two men appear as the reason; then we go "to that story".
- **FX** #19 crosses + #20 + `FH` after the push to Taiwan.
- **Assets** E25 `chang_award.jpg` crop (2nd use) red circle · N02b Tsao (2nd use) blue circle.
- **Text** `failed` t-label @241.78 (rough crosses on the stamps at 12 fps from @241.8) · `these two people` serif-i
  `two` @243.14 `people` @243.54 · `big reasons` `big` @244.26 `reasons` @244.66 · "So let's get to that story": no text —
  the camera pushes into Taiwan and the two circles slide together (motion for the cut).
- **Out** `CA` → face cam @247.86.
- **SFX** 241.76 marker_scratch ×6 · 243.12 pop_soft ×2 · 246.5 whoosh_soft.

## 9. Act IX — Host intro + the joke (246.18–270.02)
Music: bed thins to a light, playful layer; title sting on "Searching Lessons" 250.02; no hits on punchlines.

### IS057 · 247.86–250.02 · I050 · FACE — insert 4/6 (2.16 s)
- **Words** "I'm your host, Sam, and this is"  **Why** self-introduction.
- **Assets** `fc_245.8.mp4` (clean — no cut-out needed).
- **Text** lower third: `host` t-label @248.26 · `SAM` t-display (bone, clean) @248.66.
- **Out** `W` left @249.96.
- **SFX** 248.64 pop_soft · 249.95 whoosh.

### IS058 · 250.02–253.30 · I050–I051 · NIGHT
- **Words** "Searching Lessons. Now, as you can tell from this intro,"  **Why** the show title; then "this intro" = a film
  strip of the intro's own shots rewinding.
- **FX** #4 film title + #13 random letters + #8 streaks · **Ref** Pinterest idea: "retro documentary title card".
- **Text** `SEARCHING` @250.02 `LESSONS` @250.74 t-display **hero halate**, random-letter reveal · film strip of IS001–IS056
  stills (N39 🛠 from our own render) slides through @252.74 ("intro").
- **Out** `CA` — strip still sliding as we cut to face @253.30.
- **SFX** 250.00 letter_ticks (0.7 s) · 250.02 chime_soft (title sting is music) · 252.72 projector_click ×6.

### IS059 · 253.30–255.38 · I051 · FACE — insert 5/6 (2.08 s)
- **Words** "my face is really built for radio."  **Why** the joke needs his face; a radio appears behind him.
- **Assets** `fc_251.0.mp4` → fg/bg (N32) · N28 vintage radio illustration (PD) slides onto the shelf behind him @254.6.
- **Text** `built for radio` t-serif-i word-by-word `built` @254.26 `for` @254.58 `radio` @254.74.
- **Out** `W` right @255.32.
- **SFX** 254.70 tick_soft (radio dial) · 255.30 whoosh.

### IS060 · 255.38–259.22 · I052–I053 · NIGHT
- **Words** "So I'm gonna do the rest of this podcast off camera. Mainly because these"  **Why** "off camera" literally: a
  screen switching off.
- **FX** #11 TV (CRT power-off) · **Ref** §10.1.7: **Tatung TV** (Taiwanese maker), screen keyed (N24a).
- **Visual** the Tatung TV shows our colour-bar card (N43 🛠) → CRT off (collapse to a line, then a dot) @257.54.
  "Mainly because these": the dot lingers and stretches into a horizontal line (motion for the next cut).
- **Text** `off camera` t-label on the TV bezel `off` @257.54 `camera` @257.86.
- **Out** CRT-line match: the line opens into the face-cam frame (reverse power-on, no grade on him) @259.22.
- **SFX** 255.40 crt_hum (dur 2.2) · 257.52 crt_off · 259.20 crt_click.

### IS061 · 259.22–261.94 · I053 · FACE — insert 6/6 (2.72 s)
- **Words** "camera lights make me sweat all the time."  **Why** the punchline on his face.
- **Assets** face cam clean: `input/Face Cam.mp4` (media-start 259.194) or `fc_256.0` + `fc_261.5` joined at 261.5.
- **Text** `sweat` t-display @260.50 with a hand-drawn sweat-drop markup (#19) beside his temple (the one sweat gag).
- **Out** `W` down (toward "below") @261.88.
- **SFX** 260.48 pop_soft · 261.86 whoosh.

### IS062 · 261.94–265.62 · I054 · NIGHT
- **Words** "And as you can tell from the timestamp below, this is gonna be a long story,"  **Why** the video's chapter
  list with timestamps; a rack focus lands on the total length; an arrow points below.
- **FX** `FH`-style rack focus + #19 arrow + #13 · **Ref D12** (dark list with blurred bars, focus pull).
- **Visual** chapter-list typeset (N41 🛠) — blurred rows of `0:00:00 …` with thin blue/red bars; focus pulls to the
  progress readout `0:04:22 / 4:26:14` (full episode length, DECISIONS #10) @263.30; rough arrow down @263.94.
- **Text** `long story` serif-i `long` @264.90 `story` @265.14; the list scrolls fast from @264.9.
- **Out** `PS` @265.56.
- **SFX** 263.28 tick_soft · 263.92 marker_scratch · 264.9 dot_slide (scroll) · 265.54 paper_slide.

### IS063 · 265.62–270.02 · I055 · PAPER
- **Words** "and I would rather not sweat and wipe sweat off my face for the rest of this podcast."  **Why** a vintage colour
  illustration of a man mopping his brow; the episode's progress bar runs long beneath it ("the rest of this podcast").
- **FX** #16 illustration plate + #13 · **Ref** Krish's illustration rule; Pinterest idea: "Puck-magazine colour cartoon".
- **Assets** N29 PD colour lithograph/cartoon of a man wiping sweat.
- **Text** none on "sweat" (already used). Progress bar along the bottom edge crawls from @268.74 ("rest").
- **Out** `CA` (bar still moving) @270.02.
- **SFX** 265.64 paper_slide · 268.72 dot_slide (dur 1.2).

## 10. Act X — Launch into the story (270.02–275.06)
Music: build from 270.02; swell on "here's the story" 273.78 into chunk 1.

### IS064 · 270.02–271.78 · I056 · PAPER
- **Words** "So enjoy the historic images and"  **Why** a collage poster of historic images.
- **FX** #12 collage (12 fps pinning) + #18 · **Ref D07** (moonshine-ad collage: photos + typographic boxes + stamps).
- **Assets** E04 `chang_1951_mit.jpg` (1st use) + N31 3–4 chunk-1 teaser historic photos of Taiwan (PD/CC).
- **Text** typographic box `historic images` `historic` @270.90 `images` @271.30.
- **Out** `FW` @271.72.
- **SFX** 270.10 paper_slide ×3 · 270.88 stamp_thud · 271.70 whoosh.

### IS065 · 271.78–273.46 · I056 · NIGHT
- **Words** "B rolls we have for you, and"  **Why** B-roll footage playing on a period screen.
- **FX** #11 TV · **Ref** §10.1.7: **Sony Trinitron** (different set from IS060), CRT power-on + flash.
- **Assets** N24b Trinitron photo, screen keyed · E36 `footage/fab_hk_workers_microscope_rows_b.mp4` (1st use;
  or `fab_corridor_wide_cleanroom.mp4`).
- **Text** `B-roll` t-label @271.78.
- **Out** `PT` — camera pushes into the screen from @273.2.
- **SFX** 271.76 crt_click · 271.8 crt_hum (dur 1.6).

### IS066 · 273.46–275.06 · I056 · NIGHT
- **Words** "now here's the story."  **Why** we fly through the screen into the story.
- **FX** #8 streaks + light-flash whip at the very end (hand-off to chunk 1).
- **Text** `here's the story` serif-i clean word-by-word `here's` @273.78 `the` @274.18 `story` @274.34.
- **Out** streaks flare to bone on the last 4 frames (chunk 1 opens from that flash).
- **SFX** 273.48 whoosh_big · 274.30 air_swell.

## 11. Coverage tables

### 11.1 Effects (MANUAL §5 + §10)
| effect | scenes |
|---|---|
| #1 B-roll footage | IS003, IS012, IS018, IS031, IS037, IS065 |
| #2 charts | IS007–008 (D01), IS010–011 (D05), IS013 (D04), IS022/032 (D06), IS024/027 (D15), IS026 (D03), IS039 (D11), IS045 (D13), IS052 (D02) |
| #3 maps (incl. burn reveal) | IS006, IS016, IS028, IS035 (burn), IS038, IS045, IS048, IS053, IS055–056 · portrait burn IS043 |
| #4 film-title typography (hero halate) | IS001, IS004, IS005, IS025, IS029, IS031, IS035, IS043, IS045, IS058 |
| #5 document/newspaper page treatment | IS009 (manual + datasheet), IS015 (dictionary) |
| #8 light streaks | IS001, IS004, IS025, IS031, IS058, IS066 |
| #10 Vox layered | IS002, IS020, IS033, IS051 |
| #11 TV (varied sets) | IS060 Tatung, IS065 Sony Trinitron |
| #12 collage / timeline / torn edges | IS019, IS030, IS036, IS042, IS044, IS054, IS064 |
| #13 text animations | odometer IS001 · count IS007/008/026 · typewriter IS034 · random IS058 · word-by-word everywhere |
| #14 gate weave | IS003, IS018, IS031, IS037 |
| #15 curve cut | IS005 |
| #16 hi-quality plate | IS003, IS012, IS021, IS029, IS047, IS063 |
| #17 2.5D | IS017 (Tsao), IS050 (Taipei) |
| #18 rough + highlighter | IS014, IS015, IS022, IS023, IS038, IS040, IS047 |
| #19 markups | IS009, IS011, IS012, IS021, IS027, IS039, IS049, IS056, IS061, IS062 |
| #20 map callouts | IS006, IS038, IS053, IS055, IS056 |
| whip `W` / flash whip `FW` | ≈20 W + 8 FW (never twice in a row; directions vary ← → ↑ ↓) |
| cut on action `CA` | ≈20 scene exits |
| push-through `PT` / paper slide `PS` | PT ×4, PS ×7 |
| focus hunt `FH` | IS005, IS009, IS015, IS017, IS028, IS043, IS050, IS053, IS056, IS062 (rack) |
| chokeSettle `CS` | IS004, IS015, IS020, IS033, IS044 |
| no iris | ✔ none |

### 11.2 Krish's intro reference pack (D01–D15): **all 15 used**
| ref | scene(s) | | ref | scene(s) |
|---|---|---|---|---|
| D01 bars + threshold + halftone object | IS007–IS008 | | D09 old city map | IS038 |
| D02 bars topped with portraits | IS052 | | D10 tilted topo map + routes | IS006, IS028 |
| D03 isotype grid | IS026 | | D11 dark Sankey over ghost map | IS039 |
| D04 horizontal bars, serif title | IS013 | | D12 dark list + focus pull | IS062 |
| D05 line chart + era band | IS010–IS011 | | D13 dark line chart over ghost map | IS045 |
| D06 parliament dots + highlighted title | IS022, IS032 (+ dots in IS024, IS035) | | D14 satellite + district + yellow route | IS053 |
| D07 collage poster | IS064 | | D15 relationship diagram | IS024, IS027, IS042 |
| D08 telegram | IS034 | | | |
Older refs reused: R12 (IS035), R11 (IS048), R9 lamp pool (IS009), markup-map (IS012). Pinterest-style ideas for the rest
are named in each scene.

### 11.3 Face-cam inserts (6; none before 10 s; all 1–3 s)
| # | scene | VO window | dur | words | treatment |
|---|---|---|---|---|---|
| 1 | IS041 | 170.98–173.86 | 2.88 | "Guess who was the founder and CEO" | cut-out; FOUNDER & CEO nameplate + silhouette behind; text founder/CEO |
| 2 | IS046 | 196.61–198.93 | 2.32 | "That's the story I want to share with everyone." | cut-out; red/blue rivalry lines behind; "the story" |
| 3 | IS049 | 206.77–209.73 | 2.96 | "By the end of this, I think you'll agree with me when I say" | cut-out; beige world map → Taiwan behind; "agree ✓" |
| 4 | IS057 | 247.86–250.02 | 2.16 | "I'm your host, Sam, and this is" | clean; lower third host / SAM |
| 5 | IS059 | 253.30–255.38 | 2.08 | "my face is really built for radio." | cut-out; vintage radio behind; "built for radio" |
| 6 | IS061 | 259.22–261.94 | 2.72 | "camera lights make me sweat all the time." | clean; "sweat" + drawn sweat drop |

### 11.4 Ground rhythm (N night · P paper · G grid · F face)
```
001N 002P 003N 004N 005N | 006P 007G 008G 009N 010P 011P | 012N 013P 014G 015P 016N 017N | 018N 019G 020N 021N
022P 023P 024P 025N 026G 027P 028P 029N 030P 031N 032P 033N 034P 035N 036G 037N 038P 039N 040G 041F
042P 043N 044P 045N 046F 047N 048P 049F 050N 051N 052G 053N 054P 055N 056N 057F 058N 059F 060N 061F 062N 063P 064P 065N 066N
```
Longest same-ground run: 3 (N 003–005, N 016–018; P 022–024; P/G light 006–008, 010–011+, 013–015, 026–028). ✔

### 11.5 Transitions in order (never the same twice in a row)
FW, CA, freeze, W↑, CA(match), W→, CA(punch), W↓, PS, cont., CA, W←, CA, PS, FW, PT, W→, CA, W↑, CA(match), FW, cont., W←,
CA, W↓, PS, CA, FW, W→, CA, hard-cut-on-action, W←, CA, PS, W↓, CA, W↓(shovel), PT, W→, CA, W←, PT, PS(torn), CA, W↑, CA, FW,
CA(graphic hand-off), W→, CA, PS, W↑, CA, FW, cont., CA, W←, CA, W→, CRT-line, W↓, PS, CA, FW, PT, flash-out. ✔

### 11.6 Palette check
Blue = Tsao/UMC only (IS002, 009, 010–011, 017, 018–020, 022, 027, 030, 033, 036, 038, 040, 044, 052–053, 056).
Red = Chang/TSMC only, **from 180.69 on** (IS043+). Before that the executive is grey. Celadon = Taiwan (IS002, 006, 035,
045, 048, 050, 053). Yellow key numbers: `6×` (IS008), `25,000` (IS026); everything else yellow = highlighter.

## 12. Open questions (defaults in DECISIONS.md)
1. Hsinchu park name — narrator says "Hsinchu Park"; show "HSINCHU SCIENCE PARK" (BRIEF rule 3)? → **yes, full name**.
2. Charts without narrated data (D05 profits/sales, D04 demand, D13 superpower, D02 leap-frog) → **shapes only, no axis
   values/years**; OK?
3. 6th face-cam insert: 206.77 (spread out) vs 265.78 ("wipe sweat", joke tail) → **206.77**.
4. US Army 1944–45 Hsinchu city plan at "across the street" (era mismatch, but a real street map) → **use, no date label**.
5. "Taiwan ‹gap› superpower" — show only TAIWAN + SUPERPOWER → **yes**.
6. Vintage datasheets (UMC databook) copyrighted but archival → **use if found on archive.org/bitsavers, log as
   "archival, rights unclear", Krish to confirm**; else typeset card.
7. Timestamp scene total length → **4:26:14** (= `input/Final Full Audio.mp3`); change if the published length differs.
8. Tsao photos are all modern (2010s–20s) for a 1983 story → **use them (identification first), halftone/duotone**; swap
   in a 1980s CC photo if one turns up.
9. D07 collage previews chunk-1 photos → **yes** (they are "historic images we have for you").
10. Sisyphus for "uphill battle" (idiom made literal) → **yes** (a colour painting, matches the words' meaning).
11. "Searching Lessons" styling → **title case, Haskoy display**, Krish to confirm.
