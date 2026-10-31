# EDIT NOTES — CHUNK c5 "Taiwan: the chip rivalry" (Searching Lessons), VO local 0.00–598.03 (full audio 2679.14–3277.14)

Shot-by-shot plan for chunk c5. Read with `project/LONGFORM.md`, `MANUAL.md` (§10.1–10.9 override older sections; §5 effects; §6/§6.1 reference layouts), `project/c5/analysis/BEATS.md` (beats, ASR fixes, cues), `ASSETS_NEEDED.md` (IDs `E..` exist, `N..` to find, `M..` map kit, `G..` to make), `SEGMENTS.md` (who builds what) and `DECISIONS.md`. Look/quality bar = the approved intro (`review/intro_720p.mp4`, `project/intro/EDIT_NOTES.md`). Prepared 2026-10-31 by the c5 director / edit planner.

## 0. How to read this file

- **Times** = LOCAL VO seconds (`vo_c5.mp3`, `transcript_c5.json`), scene boundaries on word starts. **124 scenes, C5S001–C5S124**,
  contiguous, 0.00 → 598.03, no gaps (average 4.8 s — the intro averaged 4.2 s).
- **Text cue `@t`** = start of the spoken word; the text's first frame sits at `T(t) − 0.06`. Lines longer than one word are revealed
  **word by word** (each word its own literal `T()`), MANUAL §4.4. When a scene's FIRST cue is its first spoken word (e.g. C5S003
  "made", C5S008 "General", C5S029 "Fred"), the cut itself moves to `S(t) − 0.06` so picture and word arrive together.
- **Words** = the exact narration under the shot. **Why** = why the picture matches those words (§10.1.3). Rhetorical lines get a
  visual serving their sentence or the previous image held — never a mood shot. **No face cam** anywhere in c5.
- **Ground**: `NIGHT` (dark/cinematic/archival full-frame), `PAPER` (Texturelabs `_hires` papers, two layers, top ~90 %), `GRID` (real
  graph/ruled paper: `paper_graph_01_hires`, K+E 1960 `_hires`). Rhythm: ≤ 3 in a row on the same ground, PAPER+GRID counted together
  (checked in §11.4). Never the same paper file in two consecutive light scenes.
- **FX** = MANUAL §5 numbers + §10 craft: `W` whip (`FX.whip`, direction given), `FW` light-flash whip, `CA` cut on action, `PT` push-through,
  `PS` paper slide / torn-paper wipe, `MC` match cut, `FH` focus hunt (`FX.focusHunt`, once per scene max), `CS` `FX.chokeSettle`.
  **No iris.** Easing `FX.choppy(FX.ease.out|inOut|in, dur, 12)`; camera `FX.ease.cam`; entrances 1.0–1.6 s, moves 1.2–2 s;
  `expo.inOut` only for the curve cut C5S092.
- **Key anim done @t** = the time the scene's KEY animation (bars, route, count, stamp, pins, diagram) has finished; it then **holds
  ≥ 0.5 s before the out** starts (§10.9 — whips are centred on the boundary, so a whip's outgoing half starts 0.16 s before it). Words
  spoken in the last 0.6 s of a scene use the short 0.35 s text entrance and are never the key animation. Cut-on-action uses the
  camera or a secondary motion, never an unfinished key animation.
- **Glow**: `.halate` only on the scene's **hero** (marked "hero halate"). Everything else `.clean`. Paper/grid never glow.
- **Ref** = Krish's intro pack `D01–D15` (`references/style-images/intro/`), original refs `R1–R12` (`references/style-images/1–12`,
  stills in `expected/layouts/`) — always as VARIATIONS — or a **NEW** idea named in the scene (Pinterest-style, described in §11.3).
- **Palette** (`lib/palette.css`; **lead's cross-chunk colour decision**, LONGFORM.md end; DECISIONS #1) — c5 is a political chunk:
  **red** `--vermilion` = **PRC / CCP / the Communist bloc** (China, Mao, the USSR as hatched red) · **celadon** `#9fc7b2` = **Taiwan / ROC /
  Taiwanese government** · **navy** `#1d5c9e` (sky `#9fc3e3` on night) = **the United States and its allies, only when a contrast is
  needed** (US vs China/USSR) — otherwise the US stays neutral (outline) · everyone else neutral (ink / bone / grey: India, Pakistan, GI/TI/RCA,
  Terman, the UN) · **yellow** = highlighter + the one key number of a scene (`9 to 10%`, `2 days`, `an hour`, `2` two times). TSMC/UMC
  don't appear in c5, so red-TSMC never meets red-PRC. **Max two accents per frame** (e.g. red + celadon on the UN seat diagrams, red + navy
  on the Cold-War triangle). Flags are single-colour halftone prints in their code colour (US navy, PRC red, ROC ink — its own red field would
  break the code). Cultural Revolution posters/Mao paintings keep their red (it IS the PRC code), lightly muted.
- **Maps** only from `assets/maps/kit/` (`M..`) — rich relief / sharp satellite / vintage colour atlas; never the flat grey relief. Satellite
  credit (Esri/NASA) 13 px bottom-right.
- **Assets**: true images first (copyrighted OK — fair use, credited, logged with "© owner, fair use"); a photo/clip may repeat when the
  story needs it (§10.9) but prefer new ones. Never strip watermarks.
- **SFX** lines are object events (LOCAL VO s) → copy into `compositions/c5sNN.sfx.json` (vocabulary SEGMENTS §3.4). The sound
  designer's restraint pass (§10.8) keeps only the hero per scene + moves.


## 1. Act I — Made in Taiwan — growth, US companies, assembly work (0.00–81.76)
Music: layered bed enters soft (pad + light pulse, Melting Glass family); small lift on "big deal" 6.35; data pulse under 14–23 s; thin under the value-chain explanation 55–81. Tone: warm, curious, explanatory; light pride.

### C5S001 · 0.00–2.19 · C5B001 · NIGHT · `c5s01`
- **Words** "This actually did work, by the way."  **Why** 'This actually did work' = c4's export processing zones (EPZ) worked → the real EPZ factory c4 ended on, with a tick.
- **FX** #1 photo plate + #16 + #19 pen tick · **Ref** markup-map (s11) variation: one tick instead of a circle
- **Visual** E01 Nanzih EPZ factory photo, sepia duotone, slow push; a bone pen tick (FX.markup.pen) draws beside the gate @1.04.
- **Assets** E01
- **Text** `did work` word-by-word `did` @0.72 `work` @1.04 (t-serif-i 96px .clean)
- **Camera** push 1.00→1.05 (cam ease) · **Key anim done** @1.30 · **Out** `W→` whip right @2.19
- **SFX** 0.02 air_swell (chunk opens) · 1.02 marker_scratch (tick) · 2.14 whoosh (whip)

### C5S002 · 2.19–4.99 · C5B001 · PAPER · `c5s01`
- **Words** "In the 60s, 70s, probably 80s, 90s too,"  **Why** Four decades named one after another → a timeline that steps 60s→70s→80s→90s.
- **FX** #12 timeline (axis + travelling dot) + #13 odometer on each decade · **Ref** R7 variation (axis only, no line) — Pinterest idea: 'minimal decade ruler'
- **Visual** paper_cream + paper_lined_01_hires (90 %) two-layer ground; ink axis draws L→R; a celadon dot jumps decade to decade at 12 fps; decade labels roll in odometer-style.
- **Assets** E13
- **Text** `60s` @2.43 (t-display 140px ink) · `70s` @2.99 · `80s` @3.79 · `90s` @4.27
- **Camera** slow drift right 60 px · **Key anim done** @4.40 · **Out** `CA` cut on action @4.99
- **SFX** 2.41 odometer_tick · 2.97 odometer_tick · 3.77 odometer_tick · 4.25 odometer_tick

### C5S003 · 4.99–7.23 · C5B001 · NIGHT · `c5s01`
- **Words** "made in Taiwan was a pretty big deal."  **Why** 'Made in Taiwan … a big deal' → a real MADE IN TAIWAN label in macro; the phrase is the hero.
- **FX** #1 photo + #16 fringe + #4 film title + FH · **Ref** Pinterest idea: 'macro product label / country-of-origin stamp'
- **Visual** N30 macro of a real vintage 'MADE IN TAIWAN' stamped label (toy/radio underside), shallow depth; the camera lands on it from CA push and focus-hunts @5.4.
- **Assets** N30
- **Text** `made in Taiwan` word-by-word `made` @4.99 `in` @5.23 `Taiwan` @5.39 (t-display 150px hero halate) · `big deal` word-by-word `big` @6.35 `deal` @6.75 (t-serif-i 64px .clean)
- **Camera** push 1.05→1.12; FX.focusHunt @5.40 · **Key anim done** @6.57 · **Out** `FW` light-flash whip @7.23
- **SFX** 5.00 pop_soft (label lands) · 7.16 whoosh_soft (flash whip)

### C5S004 · 7.23–14.35 · C5B002,C5B003 · PAPER · `c5s01`
- **Words** "A lot of products like Christmas lights, radios, washers, umbrellas, textiles, they were all made in Taiwan."  **Why** Five products named, one per word → a collage of real period ads/photos pinned one per word, then the whole set stamped 'made in Taiwan'.
- **FX** #12 collage (12 fps pinning, torn edges) + rubber stamp (FX.chokeSettle) · **Ref** D07 variation (moonshine-ad collage → product-ad collage, landscape, five cards + one typographic box)
- **Visual** Cards pin in at 12 fps on paper_stained_01 (two layers): Christmas lights box/ad, transistor radio ad, washing machine ad, umbrella, textile bolts (N31a–e, tinted ink→paper, halftone multiply). Each card's caption is a t-label box. @13.31 an ink rubber stamp lands across the set three times, one word per hit — MADE @13.31, IN @13.63, TAIWAN @13.79 — (rough edge settles one 12 fps step later).
- **Assets** N31a–e, E13
- **Text** `Christmas lights` word-by-word `Christmas` @8.35 `lights` @8.75 (t-label box) · `radios` @9.23 (t-label box) · `washers` @10.03 (t-label box) · `umbrellas` @11.07 (t-label box) · `textiles` @11.87 (t-label box) · `made in Taiwan` word-by-word `made` @13.31 `in` @13.63 `Taiwan` @13.79 (stamp, Haskoy 800 ink)
- **Camera** slow pull-out 1.10→1.00 as cards fill the frame; the camera keeps moving through the cut · **Key anim done** @13.85 · **Out** `CA` cut on action @14.35
- **SFX** 8.33 paper_slide (lights) · 9.21 paper_slide (radio) · 10.01 paper_slide (washer) · 11.05 paper_slide (umbrella) · 11.85 paper_slide (textiles) · 13.29 stamp_thud (MADE IN TAIWAN) · 14.30 paper_slide (cut on the pull-out)

### C5S005 · 14.35–20.59 · C5B004 · GRID · `c5s01`
- **Words** "And because of that, Taiwanese economy grows almost nearly 9 to 10% every single year,"  **Why** 'economy grows 9 to 10 % every single year' → a bar per year, every bar landing in the same 9–10 % band.
- **FX** #2 bars (12 fps, watercolour tops) + #13 count + .label-box · **Ref** D01 variation (bars + dashed threshold + ink label box + halftone object at the base: here a halftone Taiwan factory instead of a building)
- **Visual** K+E graph sheet (ke1960_10x10_grid_black_hires, multiply) on paper_cream. ~16 ink-celadon bars rise left→right at 12 fps (stagger 0.12 s), all stopping inside a shaded 9–10 % band (dashed lines). Halftone cut-out of a Taiwan factory roof (from N39) across the base. No years, no axis numbers.
- **Assets** N39 (halftone base), E13
- **Text** `Taiwanese economy` word-by-word `Taiwanese` @15.31 `economy` @16.19 (t-serif title, ink) · `9 to 10%` word-by-word `9` @18.19 `to` @18.51 `10%` @18.67 (.label-box YELLOW key number (count 0→9, then 'to 10%')) · `every single year` word-by-word `every` @19.47 `single` @19.71 `year` @20.11 (t-label)
- **Camera** slow drift right; bars finish @19.6 · **Key anim done** @19.90 · **Out** `PS` paper slide / torn-paper wipe @20.59
- **SFX** 16.80 dot_ticks (bars rise, 2.5 s) · 18.17 counter_ticks (9 to 10%)

### C5S006 · 20.59–23.63 · C5B005 · GRID · `c5s01`
- **Words** "even after American aid to the island."  **Why** 'even after American aid' → a shaded era band labelled American aid ends while the bars keep marching past it.
- **FX** #2 era band + line through bar tops + #16 small photo card · **Ref** D05 variation (era band, here applied to the D01 bars — the band ENDS, growth continues)
- **Visual** Camera keeps moving right (cut-on-action continuation). A sepia band slides in behind the first bars with a small halftone card of the real US-aid 'clasped hands' emblem (N32) at its top; band stops; new bars keep rising beyond it; an ink line joins the bar tops and runs past the band edge.
- **Assets** N32, E13
- **Text** `American aid` word-by-word `American` @21.55 `aid` @22.19 (t-label in band) · `the island` word-by-word `the` @22.83 `island` @22.99 (t-serif-i small)
- **Camera** camera continues right 1.0→ +240 px · **Key anim done** @22.90 · **Out** `W→` whip right @23.63
- **SFX** 21.53 paper_slide (band) · 22.40 marker_long (line past band, 0.6 s) · 23.56 whoosh (whip)

### C5S007 · 23.63–29.79 · C5B006 · NIGHT · `c5s01`
- **Words** "Some of the companies during this time are some of the most popular and cutting edge companies of that time."  **Why** 'most popular and cutting edge companies of that time' → period electronics magazines/ads of the US tech giants, layered Vox-style.
- **FX** #10 Vox layered backgrounds (3 panels tinted, drifting) + #13 FX.text.rise · **Ref** s09 layered look; Pinterest idea: 'stacked 1960s tech-magazine covers'
- **Visual** Three tinted panels drift at different speeds: Electronics magazine covers / ads 1964–70 (N33a–c, FX.tintDefs ink→bone), halftone overlay. No company named yet (names come at 29.79).
- **Assets** N33a–c
- **Text** `most popular` word-by-word `most` @26.75 `popular` @27.07 (t-serif-i 72px .clean) · `cutting edge` word-by-word `cutting` @27.71 `edge` @28.19 (t-label)
- **Camera** push 1.00→1.08, last 6 frames speed up · **Key anim done** @29.00 · **Out** `CA` cut on action @29.79
- **SFX** 23.70 paper_slide (panels) · 29.70 whoosh_soft (CA)

### C5S008 · 29.79–35.15 · C5B007 · PAPER · `c5s01`
- **Words** "General **Instrument,** Texas Instrument, **RCA,** which is gonna play a big part in this story."  **Why** Three names spoken → three real annual-report covers with logos fan in on each name; RCA is pulled forward on 'big part in this story'.
- **FX** #12 cards (12 fps) + #19 pen circle · **Ref** R4 variation (logos as the heroes, but on fanned report covers instead of bars — no data was narrated)
- **Visual** On paper_cream + paper_fiber: GI, TI, RCA annual-report covers late 1960s (N35a–c) slide in as cards, each with its real logo (N34) as a crisp label underneath. @32.83 RCA's card lifts toward camera, pen circle (ink) around the RCA logo @33.95.
- **Assets** N34a–c, N35a–c
- **Text** `General Instrument` word-by-word `General` @29.79 `Instrument` @30.27 (logo + t-label) · `Texas Instruments` word-by-word `Texas` @30.83 `Instruments` @31.47 (logo + t-label) · `RCA` @32.03 (logo + t-label) · `big part` word-by-word `big` @33.95 `part` @34.19 (t-serif-i)
- **Camera** drift left; push toward RCA @32.83 · **Key anim done** @34.40 · **Out** `PS` paper slide / torn-paper wipe @35.15
- **SFX** 29.77 paper_slide (GI) · 30.81 paper_slide (TI) · 32.01 paper_slide (RCA) · 33.93 marker_scratch (circle RCA)

### C5S009 · 35.15–38.59 · C5B008 · NIGHT · `c5s01`
- **Words** "I think all of these companies are gonna play a big part later in the story,"  **Why** 'all of these companies are gonna play a big part later in the story' → the three logos ride a story timeline toward 'later'.
- **FX** #12 timeline on night + streaks #8 (low) · **Ref** R7 variation on night (axis + travelling markers) — Pinterest idea: 'chapter timeline with blurred future chapters'
- **Visual** Dark ground; a thin bone axis runs to the right into a blurred future (soft streaks at the far end); three small logo chips (GI, TI, RCA in bone) slide along it at 12 fps.
- **Assets** N34a–c
- **Text** `later` @37.47 (t-serif-i 80px .clean)
- **Camera** track right with the chips (cam ease) · **Key anim done** @37.90 · **Out** `W←` whip left @38.59
- **SFX** 35.20 dot_slide (chips travel, 1.6 s) · 38.52 whoosh (whip)

### C5S010 · 38.59–41.15 · C5B008 · NIGHT · `c5s01`
- **Words** "but all these companies set up factories in Taiwan."  **Why** 'set up factories in Taiwan' → map of Taiwan, three factory pins with the logos drop.
- **FX** #3 map (map kit) + #20 pins + celadon fill · **Ref** R12 variation (rich relief island, region fill + halftone + glow) — map from assets/maps/kit
- **Visual** M07 Taiwan hi-res relief (map kit), celadon fill with halftone + soft glow; three pins drop at 12 fps on north-west Taiwan (Taipei / Taoyuan area, no city labels), each topped with a bone logo chip.
- **Assets** M07, N34a–c, E14
- **Text** `factories` @39.87 (t-label) · `Taiwan` @40.51 (t-display 120px .clean)
- **Camera** push in 1.00→1.10 then hold · **Key anim done** @40.60 · **Out** `PT` push-through @41.15
- **SFX** 39.85 map_pin (3 pins, 0.3 s apart) · 40.49 pop_soft

### C5S011 · 41.15–45.15 · C5B009 · NIGHT · `c5s01`
- **Words** "But we do want to talk about these factories a little bit because these are not high tech factories"  **Why** 'not high tech factories' → a real Taiwanese factory floor of the era; 'high tech' written then crossed out.
- **FX** #1 footage + #14 weave + #19 cross · **Ref** markup on footage (s11 style)
- **Visual** N38 Taiwan electronics assembly footage (rows of workers, 1960s–70s), slow 0.8×. 'high tech' label then a rough bone X drawn across it @44.67.
- **Assets** N38 (🔁 E15 / intro fab_hk rows only if N38 not found — no readable HK signage)
- **Text** `not` @43.79 (t-label) · `high tech` word-by-word `high` @43.95 `tech` @44.27 (t-display 96px .clean (gets X @44.67))
- **Camera** slow push · **Key anim done** @44.65 · **Out** `CA` cut on action @45.15
- **SFX** 41.20 projector_loop (dur 3.9) · 44.65 marker_scratch (X)

### C5S012 · 45.15–48.99 · C5B009 · PAPER · `c5s01`
- **Words** "producing transistors, or you know, integrated circuits in Taiwan."  **Why** 'producing transistors … integrated circuits' → a real 1960s transistor/IC catalogue page with those words highlighted.
- **FX** #5 document page (tilted 3D, halftone) + #18 highlighter (body text) + §10.6.4 text call-out · **Ref** Pinterest idea: 'vintage datasheet with highlighter'
- **Visual** N37 page (TI/Fairchild 1960s catalogue) tilted, camera pushes; body lines 'transistors' and 'integrated circuits' highlighted yellow (stroke ≈ x-height, multiply). After 'in Taiwan' a celadon Taiwan stamp with a strike appears on the margin (they're not made there).
- **Assets** N37, E13
- **Text** `transistors` @45.55 (highlighter on body word) · `integrated circuits` word-by-word `integrated` @47.23 `circuits` @47.79 (highlighter) · `in Taiwan` word-by-word `in` @48.35 `Taiwan` @48.43 (t-label + strike)
- **Camera** push 1.0→1.15 then FX.focusHunt · **Key anim done** @48.33 · **Out** `W→` whip right @48.99
- **SFX** 45.53 highlighter_swipe · 47.21 highlighter_swipe · 48.92 whoosh (whip east→US)

### C5S013 · 48.99–51.39 · C5B010 · NIGHT · `c5s01`
- **Words** "All that stuff is still happening in the United States."  **Why** 'still happening in the United States' → a 1960s US semiconductor fab (gowned workers, diffusion furnaces).
- **FX** #1 footage + #16 + light #14 · **Ref** —
- **Visual** N41 US fab footage (TI/Fairchild/Motorola 1960s), or E10 as 🔁 (only if its origin is a US plant — check intro SOURCES).
- **Assets** N41 (🔁 E10)
- **Text** `United States` word-by-word `United` @50.51 `States` @50.91 (t-display 110px hero halate)
- **Camera** push 1.00→1.06 · **Key anim done** @50.89 · **Out** `CA` cut on action @51.39
- **SFX** 49.00 air_swell (fab hum)

### C5S014 · 51.39–55.15 · C5B010 · NIGHT · `c5s01`
- **Words** "What's really happening in Taiwan is like they're just putting stuff together."  **Why** 'What's really happening in Taiwan … just putting stuff together' → Taiwanese assembly footage inside a Taiwanese-made Tatung TV.
- **FX** #11 TV (Tatung, CRT power-on) + #14 · **Ref** §10.1.7 better screens: Tatung (Taiwanese maker) — different crop/angle from intro IS060
- **Visual** E02 Tatung TV frame (screen keyed) on a dark shelf; CRT power-on @51.45; inside, N38 second clip (hands placing parts / workers at a line).
- **Assets** E02, N38
- **Text** `Taiwan` @52.35 (t-label) · `putting stuff together` word-by-word `putting` @53.63 `stuff` @54.03 `together` @54.35 (t-serif-i 72px .clean)
- **Camera** slow push toward the screen · **Key anim done** @54.49 · **Out** `W↑` vertical whip up @55.15
- **SFX** 51.40 crt_click · 51.45 crt_hum (dur 3.7) · 55.08 whoosh

### C5S015 · 55.15–61.44 · C5B011 · PAPER · `c5s01`
- **Words** "So the lowest level of Manufacturing happening, which means Taiwan doesn't get to capture"  **Why** 'the lowest level of manufacturing' → a ladder of manufacturing levels; Taiwan's rung is the bottom one.
- **FX** #2 horizontal bars + serif title, italic emphasis · **Ref** D04 variation (horizontal bars, serif title with italic emphasis) — bars become rungs, top→bottom
- **Visual** Paper_cream + paper_graph_01_hires 90 %. Title t-serif: 'the lowest level of manufacturing' (italic 'lowest'). Four ink rungs draw in top→bottom at 12 fps; only the narrated labels: 'transistors', 'integrated circuits' (upper rungs, grey) and 'putting stuff together' on the bottom rung which fills celadon. @60.96 'capture' t-label appears beside the top rungs.
- **Assets** G02, E13
- **Text** `lowest` @55.79 (title italic) · `level` @56.35 · `of` @56.67 · `manufacturing` @57.52 · `capture` @60.96 (t-label)
- **Camera** drift down to the bottom rung · **Key anim done** @60.40 · **Out** `PS` paper slide / torn-paper wipe @61.44
- **SFX** 55.80 dot_ticks (rungs) · 57.50 pop_soft (celadon rung)

### C5S016 · 61.44–64.96 · C5B012 · GRID · `c5s01`
- **Words** "this is kind of a business term. Taiwan doesn't get to capture a lot of the profits"  **Why** 'capture … a business term … the profits' → the value-chain 'smile curve': profit high at the ends, Taiwan's dot at the bottom.
- **FX** #2 line draw-on + #19 pen bracket + .label-box · **Ref** NEW ref: Stan Shih 'smile curve' value-chain chart (Pinterest/editorial econ chart)
- **Visual** Grid paper (ke1960_10x10_grid_black). An ink U-curve draws on; the high ends shade (profit); celadon Taiwan dot pops at the bottom. Label box 'business term' beside 'capture'; 'profits' labels the shaded ends.
- **Assets** G01, E13
- **Text** `business term` word-by-word `business` @62.00 `term` @62.24 (.label-box ink) · `profits` @64.40 (t-label)
- **Camera** slow push to the dot · **Key anim done** @64.40 · **Out** `CA` cut on action @64.96
- **SFX** 61.50 marker_long (curve 1.0 s) · 64.38 pop_soft

### C5S017 · 64.96–67.44 · C5B012 · NIGHT · `c5s01`
- **Words** "because they're doing the easy work, just putting it together."  **Why** 'the easy work, just putting it together' → close-up of hands assembling parts.
- **FX** #16 hi-quality plate + FX.focusHunt · **Ref** —
- **Visual** N40 photo: hands of a Taiwanese EPZ worker assembling (1970s), fringe blur, vignette, chromaticAberration 0.12.
- **Assets** N40
- **Text** `easy work` word-by-word `easy` @65.92 `work` @66.24 (t-serif-i .clean)
- **Camera** fast push lands @65.3 → focus hunt · **Key anim done** @66.80 · **Out** `PS` paper slide / torn-paper wipe @67.44
- **SFX** 65.00 whoosh_soft (push)

### C5S018 · 67.44–74.16 · C5B013,C5B014 · PAPER · `c5s01`
- **Words** "And the reason it is happening in Taiwan is because of cheap labor. So that's an important point to come keep in mind."  **Why** 'because of cheap labor … an important point to keep in mind' → a wage ledger with 'cheap labor' boxed, then pinned as the key point.
- **FX** #18 rough reveal (chokeSettle) + #19 pen underline + .label-box · **Ref** Pinterest idea: 'ledger page with a pinned note'
- **Visual** Two paper layers: ledger_specimen_p38 (scan, native size as a card) over paper_cream_02. A worker ID photo card (N40 crop or N38 still) clipped to it. 'cheap labor' in an ink label-box chokes in; @71.52 a pen underline + a pin push it to the top of the page ('important point').
- **Assets** E13, N38/N40 still
- **Text** `cheap labor` word-by-word `cheap` @69.92 `labor` @70.24 (.label-box (chokeSettle)) · `important point` word-by-word `important` @71.52 `point` @72.16 (t-serif-i)
- **Camera** slow drift; small punch-in @71.5 · **Key anim done** @72.90 · **Out** `W↓` vertical whip down @74.16
- **SFX** 69.90 paper_slide (box) · 71.50 pin_pop (pinned) · 74.10 whoosh

### C5S019 · 74.16–81.76 · C5B015 · GRID · `c5s01`
- **Words** "That doesn't mean Taiwan doesn't want to move up the value supply chain or value chain in the supply, but that's not where they are right now."  **Why** 'move up the value chain … but that's not where they are right now' → the Taiwan dot tries to climb the smile curve, then slides back.
- **FX** #2 + #19 dashed arrow + motion · **Ref** smile curve (NEW ref) — callback of C5S016, different crop (whole curve, landscape)
- **Visual** Same smile curve (wider). A dashed ink arrow draws up the right arm from the celadon dot @75.68; the dot starts climbing at 12 fps, stops, slides back down @80.4; pen circle around it on 'right now'.
- **Assets** G01
- **Text** `move up` word-by-word `move` @75.68 `up` @75.84 (t-label) · `value chain` word-by-word `value` @77.44 `chain` @77.84 (t-serif-i)
- **Camera** slow push · **Key anim done** @81.10 · **Out** `FW` light-flash whip @81.76
- **SFX** 75.66 marker_long (arrow) · 80.40 dot_slide (dot slides back) · 81.70 whoosh_soft


## 2. Act II — The conference and Fred Terman (81.76–158.41)
Music: add a melodic layer on "very beneficial" 85.04; warm swell on "Fred Terman" 129.37; rising pulse into "up and up" 157.45. Tone: optimistic, connective, rising.

### C5S020 · 81.76–86.88 · C5B016 · NIGHT · `c5s01`
- **Words** "Now another interesting thing that happens that's actually very beneficial is"  **Why** 'another interesting thing … very beneficial' → Taiwan's industrial build-out from the air (the setting for the next idea).
- **FX** #16 aerial plate + slow push + #8 light streaks (very low) · **Ref** —
- **Visual** N39 Kaohsiung EPZ / industrial aerial (1970s), sepia duotone, light streaks low; 'very beneficial' lands.
- **Assets** N39
- **Text** `very beneficial` word-by-word `very` @84.72 `beneficial` @85.04 (t-serif-i 80px .clean)
- **Camera** push 1.00→1.10 · **Key anim done** @86.20 · **Out** `CA` cut on action @86.88
- **SFX** 81.80 air_swell

### C5S021 · 86.88–90.08 · C5B017 · NIGHT · `c5s01`
- **Words** "while all this technological factories are getting set up,"  **Why** 'while all this technological factories are getting set up' → factory pins multiply across Taiwan.
- **FX** #3 map + #20 pins (12 fps) · **Ref** R12 variation (same Taiwan relief as C5S010, wider and darker grade)
- **Visual** M07 Taiwan relief; ~12 small bone factory pins pop at 12 fps along the west coast (no labels).
- **Assets** M07
- **Text** `factories` @88.72 (t-label)
- **Camera** slow pull-out · **Key anim done** @89.40 · **Out** `PS` paper slide / torn-paper wipe @90.08
- **SFX** 87.90 map_pin (pins ×12 (vary pitch))

### C5S022 · 90.08–93.84 · C5B018 · PAPER · `c5s01`
- **Words** "someone in Taiwan starts setting up an annual conferences of people"  **Why** 'someone in Taiwan starts setting up an annual conferences' → a Taipei conference venue (period postcard) + calendar pages flipping year after year.
- **FX** #12 collage (postcard card + calendar) + 12 fps page flips · **Ref** Pinterest idea: 'tear-off calendar + travel postcard'
- **Visual** Paper ground: N42 Grand Hotel Taipei postcard (1960s–70s) pinned; beside it a blank tear-off calendar (G15) whose pages flip at 12 fps (no years printed).
- **Assets** N42, G15
- **Text** `annual` @91.84 (t-label) · `conferences` @92.32 (t-serif 80px ink)
- **Camera** drift right · **Key anim done** @93.18 · **Out** `W←` whip left @93.84
- **SFX** 90.10 paper_slide (postcard) · 91.82 paper_flip (pages ×4) · 93.78 whoosh

### C5S023 · 93.84–100.80 · C5B019 · NIGHT · `c5s01`
- **Words** "to come talk about technology and chips and all the stuff that's happening in transistors, our integrated circuits, stuff like that."  **Why** 'talk about technology and chips … transistors, integrated circuits' → the programme of talks; focus pulls to each topic as he says it.
- **FX** rack focus (D12) + #13 · **Ref** D12 variation (dark list + focus pull) — rows are talk titles, thin celadon bars for sessions
- **Visual** G03 typeset programme (Crimson Pro / Cooper Hewitt) on night: blurred rows; focus pulls to 'technology', 'chips', 'transistors', 'integrated circuits' rows in turn. Only his words are legible; the rest stays blurred.
- **Assets** G03
- **Text** `technology` @94.88 (row focus) · `chips` @95.76 (row focus) · `transistors` @98.32 (row focus) · `integrated circuits` word-by-word `integrated` @99.36 `circuits` @99.84 (row focus)
- **Camera** slow scroll up · **Key anim done** @100.20 · **Out** `CA` cut on action @100.80
- **SFX** 94.86 tick_soft · 95.74 tick_soft · 98.30 tick_soft · 99.34 tick_soft

### C5S024 · 100.80–106.24 · C5B020 · NIGHT · `c5s01`
- **Words** "So there's a conference for people who are in this field to come talk in Taiwan very regularly."  **Why** 'a conference for people in this field … in Taiwan very regularly' → a real period technical-conference audience.
- **FX** #16 plate + #14 light weave · **Ref** —
- **Visual** N43 lecture-hall audience photo (1960s–70s, engineers), sepia; a small celadon Taiwan locator chip bottom-left on 'Taiwan'.
- **Assets** N43, E14
- **Text** `conference` @101.28 (t-label) · `Taiwan` @104.56 (locator chip) · `very regularly` word-by-word `very` @105.28 `regularly` @105.52 (t-serif-i .clean)
- **Camera** slow pan right · **Key anim done** @105.58 · **Out** `W↑` vertical whip up @106.24
- **SFX** 101.26 paper_rustle (crowd murmur (very low)) · 106.18 whoosh

### C5S025 · 106.24–113.36 · C5B021 · PAPER · `c5s01`
- **Words** "And from what I can tell, this was like a big deal because all the big names were coming to Taiwan on a regular basis during this time,"  **Why** 'a big deal … all the big names were coming to Taiwan on a regular basis' → routes from US tech centres converging on Taiwan on a tilted vintage map.
- **FX** #3 tilted vintage map + route draw-on + #20 pins · **Ref** D10 variation (tilted colour atlas, many routes converging instead of one)
- **Visual** N66-style vintage colour Pacific atlas sheet (map kit) tilted rotateX 28°; 4 dashed ink routes from the US west/east coasts draw in at 12 fps and converge on a celadon Taiwan; small plane glyphs.
- **Assets** M01/N66
- **Text** `big deal` word-by-word `big` @108.32 `deal` @108.56 (t-serif-i) · `big names` word-by-word `big` @109.68 `names` @109.92 (t-label) · `Taiwan` @110.80 (t-label celadon underline)
- **Camera** track west along routes · **Key anim done** @112.70 · **Out** `CA` cut on action @113.36
- **SFX** 109.66 marker_long (routes ×4) · 110.78 map_pin

### C5S026 · 113.36–120.01 · C5B022 · GRID · `c5s01`
- **Words** "or maybe, maybe I'm misunderstanding it, but a lot of Chinese American engineers who are big names were coming, and of course."  **Why** 'a lot of Chinese American engineers who are big names were coming' → isotype of engineers flowing to Taiwan, a few lit as 'big names'.
- **FX** #2 isotype grid (12 fps) + .hl · **Ref** D03 variation (isotype grid; icons move instead of fill)
- **Visual** Grid paper; rows of engineer pictograms (G14, adapted from assets/icons) fill in order @116.16 then walk right toward a celadon Taiwan tab; 5 icons get a yellow ring ('big names').
- **Assets** G14, E16
- **Text** `Chinese American engineers` word-by-word `Chinese` @116.16 `American` @116.64 `engineers` @117.04 (t-serif title) · `big names` word-by-word `big` @117.92 `names` @118.16 (t-label (yellow ring on 5 icons))
- **Camera** slow push · **Key anim done** @119.35 · **Out** `W↓` vertical whip down @120.01
- **SFX** 116.14 dot_ticks (icons fill) · 117.90 pop_soft (rings) · 119.95 whoosh

### C5S027 · 120.01–125.13 · C5B023 · NIGHT · `c5s01`
- **Words** "Some Americans was also going there for this conference. Not every single year, but they were going."  **Why** 'Some Americans … not every single year, but they were going' → an airliner arriving + a strip of year boxes, some ticked, some empty.
- **FX** #1 footage + #13 ticks · **Ref** —
- **Visual** E04 707 jet footage (landing/takeoff section) graded; under it a dark strip of 10 empty boxes; ticks draw in some, gaps left (no years).
- **Assets** E04
- **Text** `Americans` @120.33 (t-label) · `not every single year` word-by-word `not` @122.57 `every` @123.29 `single` @123.53 `year` @123.77 (t-serif-i .clean)
- **Camera** static + slow push · **Key anim done** @124.47 · **Out** `FW` light-flash whip @125.13
- **SFX** 120.05 whoosh_soft (jet pass) · 122.55 tick_soft (ticks ×6)

### C5S028 · 125.13–129.37 · C5B024 · PAPER · `c5s01`
- **Words** "For example, one guy who went there a couple of times is the guy we have talked about,"  **Why** 'one guy who went there a couple of times … the guy we have talked about' → a callback stack of earlier-chunk (c1) images flipping back.
- **FX** #12 collage stack (12 fps flips) + two paper layers · **Ref** D07-style card stack (callback, not a new poster)
- **Visual** Cards from c1 (Stanford quad, Stanford campus, HP garage — files from templates/full-edit / example-docs sources) flip back one by one; the last card is face-down (named next).
- **Assets** E05 + c1 assets (reuse)
- **Text** `a couple of times` word-by-word `a` @127.13 `couple` @127.29 `of` @127.61 `times` @127.69 (t-label)
- **Camera** slow push into the face-down card · **Key anim done** @128.80 · **Out** `PT` push-through @129.37
- **SFX** 125.20 paper_flip (×3) · 129.20 whoosh_soft (push-through)

### C5S029 · 129.37–132.49 · C5B025 · NIGHT · `c5s01`
- **Words** "Fred **Terman,** the father of Silicon Valley."  **Why** 'Fred Terman, the father of Silicon Valley' → Terman's portrait revealed, named (accurate spelling TERMAN).
- **FX** #4 hero title + #8 streaks behind a cut-out + #16 · **Ref** s01/s10 title look
- **Visual** E05 Terman portrait cut-out (halftone, sepia) with light streaks behind; name chokes in and settles.
- **Assets** E05
- **Text** `Fred Terman` word-by-word `Fred` @129.37 `Terman` @129.69 (t-display 150px hero halate) · `father of Silicon Valley` word-by-word `father` @130.65 `of` @130.97 `Silicon` @131.13 `Valley` @131.85 (t-serif-i .clean)
- **Camera** push 1.00→1.06 · **Key anim done** @131.83 · **Out** `W→` whip right @132.49
- **SFX** 129.35 air_swell · 132.42 whoosh

### C5S030 · 132.49–137.77 · C5B026 · PAPER · `c5s01`
- **Words** "He goes there, gives talks, talks to people, networks, you know things people do at conferences."  **Why** 'He goes there, gives talks, talks to people, networks' → Vox layered: Terman lecturing, a conference crowd, name badge.
- **FX** #10 Vox layered + #13 rise · **Ref** s09 variation (paper version, warm tint)
- **Visual** N20 Terman lecturing (Stanford archives, fair use) cut-out over two tinted panels: N43 crowd (second use, different crop) and a conference badge card (G03 style).
- **Assets** N20, N43
- **Text** `gives talks` word-by-word `gives` @133.21 `talks` @133.53 (t-label) · `networks` @134.65 (t-serif-i)
- **Camera** panels drift at 3 speeds · **Key anim done** @137.00 · **Out** `CA` cut on action @137.77
- **SFX** 132.50 paper_slide (panels) · 134.63 pop_soft

### C5S031 · 137.77–141.85 · C5B027 · PAPER · `c5s01`
- **Words** "And then he also talks with the Taiwanese government directly, giving them advice,"  **Why** 'talks with the Taiwanese government directly, giving them advice' → relationship diagram Terman → Taiwanese government.
- **FX** #2 diagram + #19 arrow (FX.markup.arrow) · **Ref** D15 variation (two circles, one arrow; paper_lined ground)
- **Visual** Circle A: Terman (E05 crop, sepia). Circle B: Presidential Office Building Taipei (E09 still) with celadon ring. Ink arrow A→B draws on with label 'advice'.
- **Assets** E05, E09
- **Text** `Taiwanese government` word-by-word `Taiwanese` @139.21 `government` @139.85 (t-label under circle B) · `advice` @141.29 (arrow label)
- **Camera** slow push · **Key anim done** @141.20 · **Out** continuous (same layout, camera moves on — no cut) @141.85
- **SFX** 139.19 pop_soft (circle) · 141.27 marker_long (arrow)

### C5S032 · 141.85–146.97 · C5B028 · PAPER · `c5s01`
- **Words** "getting getting information from them as to how Taiwan is doing, what are their goals, and stuff like that."  **Why** 'getting information … how Taiwan is doing, what are their goals' → the return arrow B → A.
- **FX** #19 arrow + #13 · **Ref** D15 continued
- **Visual** Return arrow B→A draws under the first ('information'); two small chips 'goals' and a rising mini-line appear on it.
- **Assets** E05, E09
- **Text** `information` @142.81 (arrow label) · `goals` @145.61 (t-label)
- **Camera** pull-out · **Key anim done** @146.30 · **Out** `W↑` vertical whip up @146.97
- **SFX** 142.79 marker_long (arrow back) · 146.90 whoosh

### C5S033 · 146.97–153.85 · C5B029 · NIGHT · `c5s01`
- **Words** "This is definitely valuable. You know, just the fact that getting to talk to someone who did basically build the Silicon Valley in a way."  **Why** 'definitely valuable … someone who did basically build the Silicon Valley' → Silicon Valley from the air, Terman's small portrait in the corner.
- **FX** #16 plate + FH + #13 · **Ref** —
- **Visual** E06 Silicon Valley aerial (sepia grade), slow push; small Terman circle bottom-left.
- **Assets** E06, E05
- **Text** `valuable` @147.85 (t-serif-i .clean) · `build` @151.85 (t-label) · `the Silicon Valley` word-by-word `the` @152.17 `Silicon` @152.33 `Valley` @152.89 (t-display 96px .clean)
- **Camera** push lands @150.6 → focus hunt · **Key anim done** @153.20 · **Out** `CA` cut on action @153.85
- **SFX** 147.00 air_swell

### C5S034 · 153.85–158.41 · C5B030 · NIGHT · `c5s01`
- **Words** "So very, very valuable. So Taiwan is definitely on the up and up."  **Why** 'So Taiwan is definitely on the up and up' → a line rising over a ghost map of Taiwan.
- **FX** #2 dark line chart over ghost map · **Ref** D13 variation (dark line chart over ghost map; celadon line, no axis values)
- **Visual** Ghost Taiwan relief (M07 at 15 %) on night; one celadon line draws upward (shape only), end dot pulses.
- **Assets** M07
- **Text** `Taiwan` @155.85 (t-label) · `up and up` word-by-word `up` @157.45 `and` @157.69 `up` @157.93 (t-serif-i .clean)
- **Camera** track with the line · **Key anim done** @157.75 · **Out** `FW` light-flash whip @158.41
- **SFX** 155.80 marker_long (line 2 s) · 158.35 whoosh


## 3. Act III — Taiwan vs Mao's China (158.41–194.22)
Music: drop the melodic layer on "Mao Zedong" 171.37; dark drone under 176–191; a small lift back on "different direction" 193.02. Tone: contrast: satisfaction → darkness (Cultural Revolution).

### C5S035 · 158.41–163.77 · C5B031 · PAPER · `c5s01`
- **Words** "And this is even more like satisfying probably for Taiwanese leader in the point"  **Why** 'satisfying … for Taiwanese leader' → Taiwan's leader, Chiang Kai-shek (introduced in c4), in a colour portrait.
- **FX** #16 colour portrait (painting-as-B-roll rule) + #12 torn edge · **Ref** Pinterest idea: 'framed state portrait on paper, torn edge'
- **Visual** N13 Chiang Kai-shek official colour portrait as a card with torn edge on paper_cream; label only his spoken words ('Taiwanese leader').
- **Assets** N13
- **Text** `satisfying` @161.05 (t-serif-i ink) · `Taiwanese leader` word-by-word `Taiwanese` @162.25 `leader` @162.89 (t-label)
- **Camera** slow push · **Key anim done** @163.11 · **Out** `W→` whip right @163.77
- **SFX** 158.45 paper_slide · 163.70 whoosh (whip west to China)

### C5S036 · 163.77–170.65 · C5B032 · NIGHT · `c5s01`
- **Words** "because things that like China may have a bigger economy because it's just a bigger landmass, bigger population at this point."  **Why** 'China may have a bigger economy … bigger landmass, bigger population' → China (red) vs Taiwan (celadon) on a rich relief map, then population dots.
- **FX** #3 map (region fill + halftone + glow) + isotype dots (D03/R5 idea) · **Ref** R12 variation (China filled red with halftone + glowing edge — exactly the R12 look; red = PRC per the lead's colour decision)
- **Visual** M01 East Asia hi-res relief (map kit). China fills red (`--vermilion`) + halftone + soft glow @166.17; Taiwan celadon. @168.65 small bone dots stream into each (many into China, a few into Taiwan) — proportional, no numbers.
- **Assets** M01
- **Text** `bigger economy` word-by-word `bigger` @166.17 `economy` @166.49 (t-label) · `bigger landmass` word-by-word `bigger` @167.61 `landmass` @167.93 (t-label) · `bigger population` word-by-word `bigger` @168.65 `population` @169.05 (t-label)
- **Camera** slow push toward the strait · **Key anim done** @170.00 · **Out** `CA` cut on action @170.65
- **SFX** 166.15 burn_crackle (fill (soft)) · 168.63 dot_ticks (population dots)

### C5S037 · 170.65–176.30 · C5B033 · NIGHT · `c5s01`
- **Words** "But Mao Zedong is the leader, and he's just not taking good care of the Chinese."  **Why** 'But Mao Zedong is the leader, and he's just not taking good care of the Chinese' → Mao's portrait on Tiananmen Gate, in depth (2.5D #1).
- **FX** #17 2.5D + #4 hero · **Ref** 2.5D (s10) — layers: sky, gate roof, Mao portrait, foreground crowd/flag-poles
- **Visual** N11 Tiananmen Gate with Mao portrait (1960s–70s photo ≥3000 px) cut into 4 layers; dolly in; title tucked behind the gate roof.
- **Assets** N11 (2.5D layers 🛠)
- **Text** `Mao Zedong` word-by-word `Mao` @171.37 `Zedong` @171.93 (t-display 150px hero halate) · `not taking good care` word-by-word `not` @173.77 `taking` @173.93 `good` @174.33 `care` @174.49 (t-serif-i .clean)
- **Camera** dolly z −80→150, x drift 120 · **Key anim done** @175.60 · **Out** `W↓` vertical whip down @176.30
- **SFX** 170.70 air_swell · 176.24 whoosh

### C5S038 · 176.30–179.66 · C5B034 · PAPER · `c5s01`
- **Words** "The country, China, the country. You know, the cultural revolution happens."  **Why** 'the cultural revolution happens' → a real Cultural Revolution poster (painting as B-roll), muted.
- **FX** #16 poster plate + #18 rough title (chokeSettle) · **Ref** Pinterest idea: 'propaganda poster on a wall, peeled corner'
- **Visual** N23 colour poster (keeps its red — red = PRC — slightly muted −0.25, warm) pasted on a paper wall, one corner peeling; title types in.
- **Assets** N23
- **Text** `cultural revolution` word-by-word `cultural` @178.14 `revolution` @178.62 (t-display 110px ink (chokeSettle))
- **Camera** slow tilt down · **Key anim done** @179.10 · **Out** `PS` paper slide / torn-paper wipe @179.66
- **SFX** 178.12 paper_tear

### C5S039 · 179.66–183.34 · C5B035 · NIGHT · `c5s01`
- **Words** "He's just uh Yeah purging anyone he's suspicious of,"  **Why** 'purging anyone he's suspicious of' → Red Guards / purge archival footage.
- **FX** #1 footage + #14 gate weave · **Ref** —
- **Visual** N63 Red Guards rally/ parade footage 1966–67 (newsreel), sepia, weave amp 0.8.
- **Assets** N63 (or N21 stills)
- **Text** `purging` @181.26 (t-label .clean) · `suspicious` @182.46 (t-serif-i .clean)
- **Camera** static (footage moves) · **Key anim done** @182.80 · **Out** `CA` cut on action @183.34
- **SFX** 179.70 projector_loop (dur 3.6)

### C5S040 · 183.34–188.86 · C5B036 · NIGHT · `c5s01`
- **Words** "uh and he's uh he's he's like launching a war against scientists, against engineers."  **Why** 'launching a war against scientists, against engineers' → a persecuted intellectual with a placard; pen circle on the placard.
- **FX** #16 plate + #19 pen circle · **Ref** markup on photo
- **Visual** N22 photo (struggle session, placard on chest; fair use, credited) — push to the placard; bone pen circle @187.26.
- **Assets** N22
- **Text** `war` @186.62 (t-display 96px .clean) · `scientists` @187.26 (t-label) · `engineers` @188.14 (t-label)
- **Camera** push 1.00→1.12 · **Key anim done** @188.30 · **Out** `PS` paper slide / torn-paper wipe @188.86
- **SFX** 186.60 boom_low (soft) · 187.24 marker_scratch

### C5S041 · 188.86–191.10 · C5B037 · PAPER · `c5s01`
- **Words** "Anyone who's studying, he just does not like."  **Why** 'Anyone who's studying, he just does not like' → a 1960s Chinese textbook page crossed out.
- **FX** #5 page + #19 X (pen) · **Ref** —
- **Visual** N24 textbook page scan (native size as a card) on paper; rough ink X.
- **Assets** N24
- **Text** `studying` @189.42 (t-serif-i ink)
- **Camera** slight tilt · **Key anim done** @190.44 · **Out** `W→` whip right @191.10
- **SFX** 189.90 marker_scratch (X) · 191.04 whoosh

### C5S042 · 191.10–194.22 · C5B037 · NIGHT · `c5s01`
- **Words** "All the while Taiwan is taking a different direction."  **Why** 'All the while Taiwan is taking a different direction' → 1960s Taipei streets with a celadon arrow bending away (up) from the ink one.
- **FX** #1 footage + #19 arrows · **Ref** —
- **Visual** E07 Taipei boulevard (high angle); two markup arrows: a red one points down-left (China), celadon one bends up-right (Taiwan).
- **Assets** E07
- **Text** `different direction` word-by-word `different` @193.02 `direction` @193.42 (t-serif-i .clean)
- **Camera** slow push · **Key anim done** @193.56 · **Out** `FW` light-flash whip @194.22
- **SFX** 192.40 marker_long (arrows) · 194.15 whoosh_soft


## 4. Act IV — The China shock begins — Nixon and Kissinger (194.22–227.66)
Music: hit + silence on "shock" 199.50; low pulse under Nixon/Kissinger; hero sting on "Henry Kissinger" 213.26. Tone: foreboding, then intrigue (power players).

### C5S043 · 194.22–200.06 · C5B038 · NIGHT · `c5s02`
- **Words** "But unfortunately, at the start of the 70s, all of this is gonna get a big shock."  **Why** 'at the start of the 70s … a big shock' → '70s' title; on 'shock' the frame jolts and the title cracks.
- **FX** #4 hero title + #13 odometer + #8 streaks + camera shake · **Ref** s01 title variation
- **Visual** Night, streaks; '70s' rolls in odometer-style @196.62; @199.50 a 2-frame camera jolt + light flash; 'big shock' chokes in rough then settles.
- **Assets** —
- **Text** `the 70s` word-by-word `the` @196.46 `70s` @196.62 (t-display 260px hero halate (odometer)) · `big shock` word-by-word `big` @199.26 `shock` @199.50 (t-label .clean)
- **Camera** push 1.00→1.04; jolt @199.5 · **Key anim done** @199.40 · **Out** `PS` paper slide / torn-paper wipe @200.06
- **SFX** 196.60 odometer_tick · 199.48 boom_low (shock)

### C5S044 · 200.06–205.82 · C5B039 · PAPER · `c5s02`
- **Words** "A shock which is famously named the China shock. And it starts with the United States, unfortunately."  **Why** 'famously named the China shock … starts with the United States' → the name as a torn-newsprint title, then the US.
- **FX** #18 rough type on torn newsprint + #12 torn edges · **Ref** Pinterest idea: 'torn newspaper headline letters'
- **Visual** paper_torn_01 (Screen) + newsprint_01 two layers; 'CHINA SHOCK' assembled from torn newsprint letters (chokeSettle); @204.22 a navy halftone US flag (G13) slides in under it.
- **Assets** G13, E13
- **Text** `China shock` word-by-word `China` @202.22 `shock` @202.62 (t-display 200px ink (torn letters)) · `United States` word-by-word `United` @204.22 `States` @204.62 (t-label)
- **Camera** slow push · **Key anim done** @205.16 · **Out** `W→` whip right @205.82
- **SFX** 202.20 paper_tear · 204.20 paper_slide · 205.76 whoosh

### C5S045 · 205.82–209.98 · C5B040 · NIGHT · `c5s02`
- **Words** "At this point in the 70s, under the Nixon administration,"  **Why** 'under the Nixon administration' → Richard Nixon official portrait, layered over White House panels.
- **FX** #10 Vox layered + #16 · **Ref** s09 variation
- **Visual** N07 Nixon official portrait cut-out (halftone, bone) over two tinted panels (White House exterior 1971, Oval Office) drifting.
- **Assets** N07
- **Text** `Nixon administration` word-by-word `Nixon` @208.22 `administration` @209.10 (t-label .clean)
- **Camera** panels drift · **Key anim done** @209.40 · **Out** `CA` cut on action @209.98
- **SFX** 205.90 paper_slide (panels)

### C5S046 · 209.98–214.62 · C5B041 · NIGHT · `c5s02`
- **Words** "the national security advisor was the world famous Henry Kissinger."  **Why** 'national security advisor was the world famous Henry Kissinger' → Kissinger revealed and named with his title.
- **FX** #4 hero + #16 + FX.focusHunt · **Ref** Pinterest idea: 'documentary lower-third: big name + small title'
- **Visual** N01 Kissinger 1970s portrait, full frame, sepia-cool duotone; title label first, name second (the hero).
- **Assets** N01
- **Text** `national security advisor` word-by-word `national` @210.22 `security` @210.62 `advisor` @211.18 (t-label .clean) · `Henry Kissinger` word-by-word `Henry` @213.26 `Kissinger` @213.66 (t-display 140px hero halate)
- **Camera** push lands @211.6 → focus hunt · **Key anim done** @213.96 · **Out** `W↓` vertical whip down @214.62
- **SFX** 213.24 pop_soft · 214.56 whoosh

### C5S047 · 214.62–219.42 · C5B042 · PAPER · `c5s02`
- **Words** "Arguably he goes on to become the secretary of the state. At this point, he's not the secretary of the state,"  **Why** 'goes on to become the Secretary of State … At this point, he's not' → org chart: Kissinger's chip moves to a dashed future box, then back.
- **FX** #2 diagram + #19 dashed arrow · **Ref** Pinterest idea: 'vintage org chart / government organigram'
- **Visual** G16 typeset org chart on paper_graph: President on top, 'National Security Advisor' and 'Secretary of State' boxes. Kissinger chip (N01 crop) slides into the dashed SecState box @216.14, then back @218.06 ('not').
- **Assets** G16, N01
- **Text** `Secretary of State` word-by-word `Secretary` @216.14 `of` @216.62 `State` @216.86 (box label) · `not` @218.06 (t-label (pen strike on dashed box))
- **Camera** slight drift · **Key anim done** @218.70 · **Out** continuous (same layout, camera moves on — no cut) @219.42
- **SFX** 216.12 dot_slide · 218.04 dot_slide (back)

### C5S048 · 219.42–222.46 · C5B043 · PAPER · `c5s02`
- **Words** "but unfortunately, even the secretary of the state at the time"  **Why** 'even the secretary of the state at the time' → the actual Secretary of State then (William P. Rogers) fills the box.
- **FX** #2 diagram + photo chip · **Ref** org chart continued
- **Visual** N10 Rogers portrait chip pops into the SecState box (no name text — the narrator gives none).
- **Assets** N10
- **Text** `the secretary of state` word-by-word `the` @220.78 `secretary` @220.86 `of` @221.50 `state` @221.66 (t-label under chip)
- **Camera** push toward the box · **Key anim done** @221.80 · **Out** `W→` whip right @222.46
- **SFX** 220.80 pop_soft · 222.40 whoosh

### C5S049 · 222.46–227.66 · C5B044 · NIGHT · `c5s02`
- **Words** "knows Kissinger just has crazy amount of influence on the president and the policy of the United States."  **Why** 'Kissinger just has crazy amount of influence on the president and the policy of the United States' → thick influence flows from Kissinger to the president and to US policy.
- **FX** #2 Sankey flows + ghost map · **Ref** D11 variation (dark Sankey over a ghost US map; flows from one person instead of a budget)
- **Visual** Ghost US map at 12 %; Kissinger node (N01 circle) left; two thick bone flows draw right (neutral, no accent) into 'the president' (Nixon circle, N07) and 'policy' bar.
- **Assets** N01, N07
- **Text** `influence` @224.94 (t-serif-i .clean) · `the president` word-by-word `the` @225.42 `president` @225.50 (t-label) · `policy` @226.22 (t-label)
- **Camera** slow push · **Key anim done** @227.00 · **Out** `CA` cut on action @227.66
- **SFX** 224.92 marker_long (flows 1.2 s)


## 5. Act V — The secret trip (Pakistan → Beijing) and the announcement (227.66–328.38)
Music: ticking/pulse stem (Formations-like) from 227.66; near-silence under "behind the scenes" 264.19 then build; the announcement 305.82 lifts; second hit on "Nixon is gonna go to China" 326.38. Tone: spy-thriller suspense → reveal.

### C5S050 · 227.66–231.58 · C5B045 · NIGHT · `c5s02`
- **Words** "In July 1971, Kissinger goes to Pakistan."  **Why** 'In July 1971, Kissinger goes to Pakistan' → satellite globe: Washington → Pakistan, pin.
- **FX** #3 satellite globe (s02 quality) + route + #20 pin + #13 · **Ref** s02 satellite look; Pinterest idea: 'globe spin + route arc'
- **Visual** M02 globe (map kit, sharp imagery) spins from the US east coast to South Asia; a bone arc draws; pin on Pakistan.
- **Assets** M02
- **Text** `July 1971` word-by-word `July` @227.82 `1971` @228.30 (t-display 130px hero halate) · `Pakistan` @230.86 (t-label)
- **Camera** globe rotation (cam ease) · **Key anim done** @230.92 · **Out** `W←` whip left @231.58
- **SFX** 228.30 whoosh_big (globe spin) · 230.84 map_pin

### C5S051 · 231.58–236.38 · C5B046 · PAPER · `c5s02`
- **Words** "Now he's an important guy, but I doubt anyone was paying much attention to this trip."  **Why** 'I doubt anyone was paying much attention to this trip' → a busy 1971 front page where the trip is one tiny item; focal call-out finds it.
- **FX** #5 newspaper + §10.6.5 focal call-out · **Ref** Pinterest idea: 'busy front page, tiny item circled'
- **Visual** N56b 1971 newspaper page (real, fair use) or G06 typeset page (no real masthead); FX.focalBlur sweeps and finds the small 'Kissinger' item.
- **Assets** N56b/G06
- **Text** `this trip` word-by-word `this` @235.58 `trip` @235.82 (t-label)
- **Camera** push to the item · **Key anim done** @235.70 · **Out** `CA` cut on action @236.38
- **SFX** 233.00 paper_rustle · 236.30 whoosh

### C5S052 · 236.38–242.03 · C5B047 · NIGHT · `c5s02`
- **Words** "Maybe India was paying attention because, you know, US uh US uh Official going to Pakistan,"  **Why** 'Maybe India was paying attention … US official going to Pakistan' → India watches Pakistan (radio-wave rings).
- **FX** #3 map + §10.6.7 radio waves + #20 · **Ref** R11-style region fills on a satellite base
- **Visual** M03 South Asia satellite (map kit). India hatched neutral grey; Pakistan outlined bone; rings pulse from Delhi toward Pakistan.
- **Assets** M03
- **Text** `India` @236.78 (t-label) · `Pakistan` @241.39 (t-label)
- **Camera** slow push · **Key anim done** @241.40 · **Out** continuous (same layout, camera moves on — no cut) @242.03
- **SFX** 236.76 tone_blip (rings (soft, ×3))

### C5S053 · 242.03–245.07 · C5B048 · NIGHT · `c5s02`
- **Words** "but Taiwan was paying no attention to this at all."  **Why** 'but Taiwan was paying no attention to this at all' → the same map pans far east to a quiet, celadon Taiwan.
- **FX** #3 map pan + #13 · **Ref** continuation
- **Visual** Camera pans east over M01 (cross-fade at the seam) to Taiwan, celadon, still; no rings.
- **Assets** M01, M03
- **Text** `Taiwan` @242.27 (t-label) · `no attention` word-by-word `no` @243.55 `attention` @243.71 (t-serif-i .clean)
- **Camera** fast pan → settle · **Key anim done** @244.40 · **Out** `PS` paper slide / torn-paper wipe @245.07
- **SFX** 242.05 whoosh (pan)

### C5S054 · 245.07–248.83 · C5B049 · PAPER · `c5s02`
- **Words** "Out of nowhere, on this trip in Pakistan, Kissinger gets sick."  **Why** 'Out of nowhere … Kissinger gets sick' → Kissinger card with a hospital chart clipped to it: 'sick'.
- **FX** #12 cards + #18 stamp · **Ref** Pinterest idea: 'clipboard patient chart'
- **Visual** N02 Kissinger in Pakistan 1971 (news photo, fair use) as a card; a typeset patient chart (G18, only 'sick' written) clips on; ink stamp.
- **Assets** N02, G18
- **Text** `Pakistan` @246.75 (t-label) · `sick` @248.43 (stamp ink)
- **Camera** slight push · **Key anim done** @248.20 · **Out** continuous (same layout, camera moves on — no cut) @248.83
- **SFX** 245.10 paper_slide · 248.41 stamp_thud

### C5S055 · 248.83–252.83 · C5B050 · PAPER · `c5s02`
- **Words** "We get the news that he's having acute case of stomach pain,"  **Why** 'acute case of stomach pain' → the 1971 news clipping, body line highlighted.
- **FX** #5 clipping + #18 highlighter · **Ref** §10.6.6 highlighter on body text
- **Visual** N56 clipping ('Kissinger ill …', July 1971, fair use) or G06 typeset clipping; yellow highlighter across 'stomach pain'.
- **Assets** N56/G06
- **Text** `stomach pain` word-by-word `stomach` @251.87 `pain` @252.35 (highlighter on body text)
- **Camera** push to the line · **Key anim done** @252.17 · **Out** `W↑` vertical whip up @252.83
- **SFX** 251.85 highlighter_swipe · 252.77 whoosh

### C5S056 · 252.83–258.75 · C5B051 · NIGHT · `c5s02`
- **Words** "and he's gonna be canceling all his public events for the next two days while he recovers away from the media."  **Why** 'canceling all his public events for the next two days … away from the media' → his public schedule, each event struck through; '2 days'.
- **FX** D12 list + #19 strike + #13 count · **Ref** D12 variation (schedule rows instead of budget lines)
- **Visual** G04 typeset schedule (rows 'public event' with blurred details) on night; rows struck through at 12 fps; '2 days' key number.
- **Assets** G04
- **Text** `public events` word-by-word `public` @254.67 `events` @254.99 (t-label) · `two days` word-by-word `two` @255.87 `days` @256.03 (t-display YELLOW key number '2 days') · `away from the media` word-by-word `away` @257.71 `from` @258.03 `the` @258.19 `media` @258.27 (t-serif-i .clean)
- **Camera** slow scroll · **Key anim done** @258.10 · **Out** `PS` paper slide / torn-paper wipe @258.75
- **SFX** 254.70 marker_scratch (strikes ×5) · 255.85 pop_soft

### C5S057 · 258.75–263.07 · C5B052 · PAPER · `c5s02`
- **Words** "Now in reality, it was not stomachache that was keeping him away from the media."  **Why** 'in reality, it was not stomachache' → the clipping again, a rough X across it.
- **FX** #19 cross (pen) + §10.6.4 text call-out · **Ref** callback of C5S055
- **Visual** Same clipping (G06/N56), page fades to 20 %, 'stomachache' returns full strength, X drawn over it @260.35.
- **Assets** N56/G06
- **Text** `not` @260.03 (t-label) · `stomachache` @260.35 (struck)
- **Camera** punch in 10 % · **Key anim done** @262.40 · **Out** `W→` whip right @263.07
- **SFX** 260.33 marker_scratch (X) · 263.00 whoosh

### C5S058 · 263.07–267.95 · C5B053,C5B054 · NIGHT · `c5s02`
- **Words** "What was really happening behind the scenes was that Kissinger had taken a Pakistani plane to"  **Why** 'behind the scenes … Kissinger had taken a Pakistani plane' → a real PIA airliner on a night tarmac, in depth (2.5D #2).
- **FX** #17 2.5D + #8 low streaks · **Ref** 2.5D: layers sky / plane / stairs+ground crew / foreground blur
- **Visual** N44 PIA Boeing 707 photo (1960s–70s) cut into layers, night grade, rim light; dolly.
- **Assets** N44 (layers 🛠)
- **Text** `behind the scenes` word-by-word `behind` @264.19 `the` @264.43 `scenes` @264.59 (t-serif-i .clean) · `Pakistani plane` word-by-word `Pakistani` @266.67 `plane` @267.39 (t-label)
- **Camera** dolly z −60→140 · **Key anim done** @267.10 · **Out** `MC` match cut (shape/move continues) @267.95
- **SFX** 263.10 air_swell · 266.65 whoosh_soft (engine wash)

### C5S059 · 267.95–271.47 · C5B054 · PAPER · `c5s02`
- **Words** "fly into China to meet with the Chinese leadership"  **Why** 'to fly into China to meet with the Chinese leadership' → route over the Himalayas to Beijing on a tilted vintage atlas; Zhou Enlai card.
- **FX** #3 tilted vintage atlas + route draw-on + #12 card · **Ref** D10 variation (tilted colour atlas; Rawalpindi → Beijing)
- **Visual** N66 vintage colour atlas sheet of Asia, tilted; dashed ink route Pakistan → Beijing with plane glyph; @270.35 N19 Zhou Enlai portrait card pins beside Beijing ('Chinese leadership', no name text).
- **Assets** N66, N19
- **Text** `China` @268.99 (t-label) · `Chinese leadership` word-by-word `Chinese` @270.35 `leadership` @270.83 (t-label)
- **Camera** track along route · **Key anim done** @270.90 · **Out** `PS` paper slide / torn-paper wipe @271.47
- **SFX** 267.80 marker_long (route 1.1 s) · 270.33 pin_pop

### C5S060 · 271.47–276.11 · C5B055 · PAPER · `c5s02`
- **Words** "to talk about a future trip where the president of the United States visits China"  **Why** 'to talk about a future trip where the president of the United States visits China' → the real declassified Kissinger–Zhou memo; those phrases called out.
- **FX** #5 document (tilted page, halftone) + §10.6.4 text call-out + #18 highlighter · **Ref** Pinterest idea: 'declassified memo with highlighted lines'
- **Visual** N55 memcon pages (July 1971, National Security Archive, PD) as two paper layers; text call-out returns lines about the President's visit.
- **Assets** N55
- **Text** `future trip` word-by-word `future` @272.27 `trip` @272.59 (t-label) · `the president` word-by-word `the` @273.31 `president` @273.47 (highlight) · `visits China` word-by-word `visits` @275.15 `China` @275.63 (highlight)
- **Camera** push 1.0→1.2 · **Key anim done** @275.45 · **Out** `W←` whip left @276.11
- **SFX** 272.25 paper_flip · 273.45 highlighter_swipe · 276.04 whoosh

### C5S061 · 276.11–279.47 · C5B056 · NIGHT · `c5s02`
- **Words** "to meet with the president, the leader of China, Mao Zedong."  **Why** 'to meet with the president, the leader of China, Mao Zedong' → Mao in colour (portrait painting / poster), different from C5S037.
- **FX** #16 colour portrait plate (painting rule) + #13 · **Ref** —
- **Visual** N12 colour portrait of Mao (official painting), muted grade; slow push.
- **Assets** N12
- **Text** `leader of China` word-by-word `leader` @277.63 `of` @277.95 `China` @278.03 (t-label .clean) · `Mao Zedong` word-by-word `Mao` @278.43 `Zedong` @278.91 (t-display 120px hero halate)
- **Camera** push · **Key anim done** @278.90 · **Out** `CA` cut on action @279.47
- **SFX** 278.41 pop_soft

### C5S062 · 279.47–284.03 · C5B057 · GRID · `c5s02`
- **Words** "A lot of first here, by the way. US has never made official contact with the communist China."  **Why** 'A lot of first here … US has never made official contact with the communist China' → two halftone flags joined for the first time by a line.
- **FX** #2 diagram + #18 stamp · **Ref** D15 variation (two nodes, one first link)
- **Visual** Grid paper; US flag (G13, navy halftone) left, PRC flag (G13, red halftone) right; 'never' stamp in the gap; @283.0 the dashed line connects.
- **Assets** G13
- **Text** `first` @279.79 (t-label) · `never` @281.47 (stamp) · `official contact` word-by-word `official` @281.95 `contact` @282.35 (t-label)
- **Camera** slow push · **Key anim done** @283.37 · **Out** `W↓` vertical whip down @284.03
- **SFX** 281.45 stamp_thud · 283.00 marker_long (link) · 283.97 whoosh

### C5S063 · 284.03–287.63 · C5B058 · NIGHT · `c5s02`
- **Words** "This is happening while the world doesn't know. This is happening secretly, you know?"  **Why** 'while the world doesn't know … secretly' → the world at night, a tiny flight path.
- **FX** #3 night globe + route · **Ref** Pinterest idea: 'night-lights globe, faint route'
- **Visual** M05 NASA Black Marble (night lights) globe; a faint bone dotted path crosses the Himalayas.
- **Assets** M05
- **Text** `the world` word-by-word `the` @284.83 `world` @284.99 (t-label) · `secretly` @286.59 (t-serif-i .clean)
- **Camera** slow rotation · **Key anim done** @287.00 · **Out** `CA` cut on action @287.63
- **SFX** 284.05 wind (high altitude, dur 3.6)

### C5S064 · 287.63–291.07 · C5B059 · NIGHT · `c5s02`
- **Words** "He's taking a Pakistani plane so people don't find out where he's going."  **Why** 'He's taking a Pakistani plane so people don't find out where he's going' → detective board: plane card → '?'.
- **FX** #12 board (lamp pool) + string (ink thread — red is the PRC code) · **Ref** R9 variation (cork board, lamp pool — strings in bone/ink thread, since red now means PRC)
- **Visual** E12 cork; N44 plane card (second use, different crop) pinned; ink thread draws to a card with '?'.
- **Assets** E12, N44
- **Text** `Pakistani plane` word-by-word `Pakistani` @288.51 `plane` @289.23 (t-label) · `where he's going` word-by-word `where` @290.43 `he's` @290.59 `going` @290.83 (t-serif-i .clean (? card))
- **Camera** slow pan right · **Key anim done** @290.40 · **Out** continuous (same layout, camera moves on — no cut) @291.07
- **SFX** 287.65 lamp_click · 288.49 pin_pop · 289.60 marker_long (thread)

### C5S065 · 291.07–299.23 · C5B060 · NIGHT · `c5s02`
- **Words** "He's pretending to have a stomachache, so people don't find out if why he he does not have any events scheduled in Pakistan while he is in Pakistan."  **Why** 'pretending to have a stomachache … no events scheduled in Pakistan' → the board grows: stomach-ache clipping + empty schedule, tied by thread.
- **FX** #12 board continued + #19 circle · **Ref** R9 continued
- **Visual** Clipping (G06/N56 crop) and the struck schedule (G04 crop) pinned; thread links all three cards; pen circle on 'Pakistan'.
- **Assets** E12, G04, G06/N56
- **Text** `pretending` @291.31 (t-label) · `stomachache` @292.03 (t-serif-i) · `events scheduled` word-by-word `events` @296.43 `scheduled` @296.83 (t-label) · `Pakistan` @298.51 (circled)
- **Camera** slow pull-out to show the whole board · **Key anim done** @298.50 · **Out** `W→` whip right @299.23
- **SFX** 291.30 pin_pop · 293.00 pin_pop · 296.40 marker_long (thread) · 299.17 whoosh

### C5S066 · 299.23–305.82 · C5B061 · PAPER · `c5s02`
- **Words** "Now the strip happens, he comes back, he goes to the United States. No no announcement made about this at all."  **Why** 'the trip happens, he comes back … to the United States. No announcement' → route back to the US on the atlas; a blank press notice.
- **FX** #3 atlas route + #12 card · **Ref** D10 continued (wider; route back east→west across the Pacific)
- **Visual** Atlas (N66 + Pacific sheet) route draws back to the United States; @303.90 a blank typeset press-release card slides in with 'no announcement'.
- **Assets** N66, G06
- **Text** `United States` word-by-word `United` @302.43 `States` @302.75 (t-label) · `no announcement` word-by-word `no` @303.90 `announcement` @304.14 (t-serif-i ink)
- **Camera** track east · **Key anim done** @305.20 · **Out** `CA` cut on action @305.82
- **SFX** 300.40 marker_long (route back) · 303.88 paper_slide

### C5S067 · 305.82–309.66 · C5B062 · NIGHT · `c5s02`
- **Words** "A week later, a public announcement is made that,"  **Why** 'A week later, a public announcement is made' → a 1971 RCA colour TV powers on with the televised announcement.
- **FX** #11 TV (RCA set — RCA is in this story) + CRT power-on · **Ref** §10.1.7 better screens: 1970–71 RCA colour console (new set, not the intro's)
- **Visual** N36 RCA 1971 colour TV (screen keyed) in a dim living-room plate; N61 Nixon 15 July 1971 address footage inside.
- **Assets** N36, N61
- **Text** `a week later` word-by-word `a` @305.82 `week` @305.98 `later` @306.30 (t-label) · `public announcement` word-by-word `public` @307.66 `announcement` @308.06 (t-serif-i .clean)
- **Camera** slow push · **Key anim done** @309.00 · **Out** `PT` push-through @309.66
- **SFX** 305.84 crt_click · 305.90 crt_hum (dur 3.7)

### C5S068 · 309.66–314.94 · C5B063 · NIGHT · `c5s02`
- **Words** "yes, Kissinger later in the year will be going to China to meet with Mao **Zedong.**"  **Why** 'Kissinger later in the year will be going to China to meet with Mao Zedong' → push through the screen; announcement footage full frame (his words as captions).
- **FX** #1 footage + #14 weave + #13 word-by-word · **Ref** —
- **Visual** N61 footage full-frame (scanlines fade out), weave.
- **Assets** N61
- **Text** `later in the year` word-by-word `later` @311.02 `in` @311.34 `the` @311.50 `year` @311.58 (t-label .clean) · `China` @312.86 (t-label) · `Mao Zedong` word-by-word `Mao` @313.66 `Zedong` @314.14 (t-label)
- **Camera** static · **Key anim done** @314.28 · **Out** `W↓` vertical whip down @314.94
- **SFX** 314.88 whoosh

### C5S069 · 314.94–320.14 · C5B064 · PAPER · `c5s02`
- **Words** "And guess what? Just an hour before this announcement is when Taiwan is told about this trip."  **Why** 'Just an hour before this announcement is when Taiwan is told' → a clock: hands sweep back one hour; Taiwan.
- **FX** #16 object cut-out + #13 · **Ref** Pinterest idea: 'vintage wall clock, hands sweep'
- **Visual** N54 vintage wall clock cut-out on paper_stained; hands sweep back an hour at 12 fps; celadon Taiwan tab slides in @317.98.
- **Assets** N54, E14
- **Text** `an hour before` word-by-word `an` @315.90 `hour` @316.06 `before` @316.46 (t-serif 90px ink (hour = yellow key)) · `Taiwan` @317.98 (t-label) · `told` @318.70 (t-label)
- **Camera** slow push · **Key anim done** @319.40 · **Out** `PS` paper slide / torn-paper wipe @320.14
- **SFX** 315.88 tick_soft (clock ×8) · 317.96 paper_slide

### C5S070 · 320.14–325.34 · C5B065 · PAPER · `c5s02`
- **Words** "Taiwan is told, hey Kissinger has already been to China, been to Beijing, talked with the communist leaders."  **Why** 'Taiwan is told, hey Kissinger has already been to China, been to Beijing, talked with the communist leaders' → a diplomatic cable typed with exactly those words, over an old Peking map.
- **FX** #13 typewriter + #5 + #19 marker circle · **Ref** D08 variation (telegram → teletype cable on yellow flimsy) + D09 variation (old city map of Peking under it)
- **Visual** G05 typeset cable (no real seals/letterhead) types word by word; @323.10 camera slides to N65 old Peking map underneath, yellow marker circle on the city.
- **Assets** G05, N65
- **Text** `Kissinger` @321.18 (typed) · `already been to China` word-by-word `already` @321.98 `been` @322.22 `to` @322.38 `China` @322.46 (typed) · `Beijing` @323.10 (typed + map circle) · `communist leaders` word-by-word `communist` @324.30 `leaders` @324.70 (typed)
- **Camera** slide down to map · **Key anim done** @324.68 · **Out** `FW` light-flash whip @325.34
- **SFX** 321.16 letter_ticks (typing 3.5 s) · 323.08 marker_scratch (circle) · 325.28 whoosh_soft

### C5S071 · 325.34–328.38 · C5B066 · NIGHT · `c5s02`
- **Words** "Now, very soon, Nixon is gonna go to China too."  **Why** 'very soon, Nixon is gonna go to China too' → Nixon arriving in China (1972 footage).
- **FX** #1 footage + #14 · **Ref** —
- **Visual** N62 Nixon steps off Air Force One in Beijing (Feb 1972, USIA/NARA), weave.
- **Assets** N62
- **Text** `Nixon` @326.38 (t-label .clean) · `China` @327.66 (t-serif-i .clean)
- **Camera** static · **Key anim done** @327.80 · **Out** `CA` cut on action @328.38
- **SFX** 325.36 projector_loop (dur 3.0)


## 6. Act VI — The shock — Taiwan's one assumption (328.38–352.62)
Music: cut the pulse on "big shock" 329.18; sparse drone; gentle question on "why would US do that?" 351.10. Tone: shock, disbelief.

### C5S072 · 328.38–332.30 · C5B067 · NIGHT · `c5s02`
- **Words** "This is a big shock because as I said earlier, for Taiwanese leader,"  **Why** 'a big shock … for Taiwanese leader' → Chiang Kai-shek (1970s photo); hard contrast-cut punch-in.
- **FX** #16 + §10.6.3 contrast call-out (hard cut) · **Ref** —
- **Visual** N14 Chiang 1970s photo; at 'shock' a hard punch-in with lifted-black veil around his face.
- **Assets** N14
- **Text** `big shock` word-by-word `big` @328.94 `shock` @329.18 (t-display 120px .clean (chokeSettle)) · `Taiwanese leader` word-by-word `Taiwanese` @331.26 `leader` @331.82 (t-label)
- **Camera** ease-in push; hard cut on the curve @329.1 · **Key anim done** @331.60 · **Out** `W→` whip right @332.30
- **SFX** 329.10 boom_low (clunk) · 332.24 whoosh

### C5S073 · 332.30–336.70 · C5B068 · PAPER · `c5s02`
- **Words** "a lot of their foreign policy, maybe even other policies, was built on one assumption"  **Why** 'foreign policy, maybe even other policies, was built on one assumption' → blocks stacked on one pillar.
- **FX** #2 stacked blocks (12 fps) + .label-box · **Ref** NEW ref: Pinterest 'stacked blocks on one pillar' (editorial isometric)
- **Visual** Paper; ink blocks 'foreign policy', 'other policies' drop onto a single column labelled 'one assumption'.
- **Assets** —
- **Text** `foreign policy` word-by-word `foreign` @332.86 `policy` @333.26 (block label) · `other policies` word-by-word `other` @334.46 `policies` @334.78 (block label) · `one assumption` word-by-word `one` @335.98 `assumption` @336.14 (.label-box)
- **Camera** slight tilt-up · **Key anim done** @336.10 · **Out** `CA` cut on action @336.70
- **SFX** 332.84 paper_slide (block) · 334.44 paper_slide (block) · 335.96 pop_soft

### C5S074 · 336.70–342.70 · C5B069 · NIGHT · `c5s02`
- **Words** "that they had the backing of the United States, by far arguably the strongest power at the time."  **Why** 'the backing of the United States … the strongest power at the time' → Eisenhower and Chiang in Taipei (1960) — US backing, literally.
- **FX** #16 plate + #19 pen circle · **Ref** —
- **Visual** N15 Eisenhower + Chiang motorcade/handshake Taipei 1960 (PD), sepia, pen circle on Eisenhower @338.62.
- **Assets** N15
- **Text** `backing` @337.42 (t-label) · `United States` word-by-word `United` @338.62 `States` @339.02 (t-display 100px .clean) · `strongest power` word-by-word `strongest` @341.18 `power` @341.66 (t-serif-i .clean)
- **Camera** push to Eisenhower · **Key anim done** @342.00 · **Out** `PS` paper slide / torn-paper wipe @342.70
- **SFX** 338.60 marker_scratch (circle)

### C5S075 · 342.70–347.50 · C5B070,C5B071 · PAPER · `c5s02`
- **Words** "And on top of that, they they did not think they were gonna lose this backing because it's the United States. They're"  **Why** 'they did not think they were gonna lose this backing because it's the United States' → the US–ROC mutual defense treaty page; 'United States' returns in a text call-out.
- **FX** #5 document + §10.6.4 text call-out · **Ref** Pinterest idea: 'treaty page text-callout'
- **Visual** N58 Mutual Defense Treaty 1954 page (PD) two paper layers; page fades to 20 %, 'United States of America' returns.
- **Assets** N58
- **Text** `lose this backing` word-by-word `lose` @345.18 `this` @345.34 `backing` @345.58 (t-label) · `United States` word-by-word `United` @346.54 `States` @346.86 (call-out words)
- **Camera** punch in 10 % · **Key anim done** @346.70 · **Out** `W↓` vertical whip down @347.50
- **SFX** 345.16 paper_rustle · 346.52 boom_low (clunk (soft)) · 347.20 whoosh

### C5S076 · 347.50–353.02 · C5B071,C5B072 · NIGHT · `c5s02`
- **Words** "just never gonna talk to the communist. China is a communist. So why would US do that? Well,"  **Why** 'never gonna talk to the communist. China is a communist. So why would US do that?' → a wall rises between the US and communist China; '?'.
- **FX** #12 + 12 fps wall build + #13 · **Ref** Pinterest idea: 'wall between two flags'
- **Visual** Night: US flag (navy halftone) left, PRC flag (red halftone) right (G13). E11 stone-wall texture blocks stack between them @347.66; 'why would US do that?' word by word.
- **Assets** G13, E11
- **Text** `never` @347.66 (t-label) · `communist` @348.62 (t-label) · `why` @351.10 (t-serif-i) · `would` @351.34 · `US` @351.66 · `do` @352.06
- **Camera** slow push · **Key anim done** @352.30 · **Out** `CA` cut on action @353.02
- **SFX** 347.64 dot_ticks (bricks) · 351.08 pop_soft


## 7. Act VII — Why: the Cold War triangle (Kissinger diplomacy) (352.62–399.67)
Music: steady mid-tempo ostinato from 361.50; lift on "Kissinger diplomacy" 381.03; resolve on "upper hand in the Cold War" 394.39. Tone: analytical, strategic, a little grand.

### C5S077 · 353.02–361.50 · C5B072 · NIGHT · `c5s02`
- **Words** "the reason the US is doing this is because again, I don't think anyone here can argue that Nixon was pro communist or had any sympathies for the communist."  **Why** 'the reason … nobody can argue Nixon was pro communist' → Nixon jabbing at Khrushchev in the 1959 Kitchen Debate; 'pro communist' crossed out.
- **FX** #16 plate + §10.6.5 focal call-out + #19 X · **Ref** —
- **Visual** N09 Kitchen Debate photo (LOC, PD); focal blur on Nixon's pointing finger; 'pro communist' typed then X'd.
- **Assets** N09
- **Text** `reason` @353.18 (t-serif-i) · `Nixon` @357.02 (t-label) · `pro communist` word-by-word `pro` @358.30 `communist` @358.62 (t-display 90px .clean (X @359.4)) · `sympathies` @359.82 (t-label)
- **Camera** slow push; focal spot moves · **Key anim done** @360.80 · **Out** `W→` whip right @361.50
- **SFX** 359.40 marker_scratch (X) · 361.44 whoosh

### C5S078 · 361.50–368.63 · C5B073 · PAPER · `c5s02`
- **Words** "But he believed, including with Kissinger, he believed that the Soviet Union was the big Evil, you know the big evil empire."  **Why** 'he believed … the Soviet Union was the big evil empire' → world map: the USSR hatched, labelled.
- **FX** #3 map + leader-line labels · **Ref** R11 variation (muted beige world map, red-hatched region (Communist bloc), leader-line label, big serif)
- **Visual** M06 beige world map; USSR hatched red (light) draws in; leader-line label; small Nixon + Kissinger circles at the US.
- **Assets** M06, N07, N01
- **Text** `Kissinger` @363.18 (small circle label) · `Soviet Union` word-by-word `Soviet` @364.70 `Union` @365.02 (leader label) · `big evil empire` word-by-word `big` @367.19 `evil` @367.43 `empire` @367.83 (t-serif-i 80px ink)
- **Camera** slow push east · **Key anim done** @368.00 · **Out** continuous (same layout, camera moves on — no cut) @368.63
- **SFX** 364.68 paper_rustle (hatch) · 367.17 pop_soft

### C5S079 · 368.63–376.39 · C5B074 · PAPER · `c5s02`
- **Words** "And at this point, Soviet Union and China were, you know, not too friendly, even though both of them are communists. They had actually fought a war."  **Why** 'Soviet Union and China … not too friendly … They had actually fought a war' → zoom to the Sino-Soviet border; clash point flares.
- **FX** #3 map zoom + §10.6.7 rings + #20 callout · **Ref** R11 continued → border close-up
- **Visual** Same map, China fills red solid; camera zooms to the Ussuri border; rings burst at the 1969 clash site @375.35 (small card N67 optional).
- **Assets** M06, N67
- **Text** `China` @371.03 (leader label) · `not too friendly` word-by-word `not` @371.99 `too` @372.15 `friendly` @372.31 (t-serif-i) · `fought a war` word-by-word `fought` @375.35 `a` @375.75 `war` @375.91 (t-label)
- **Camera** zoom (cam ease) then FX.focusHunt · **Key anim done** @375.73 · **Out** `W↑` vertical whip up @376.39
- **SFX** 370.00 whoosh_soft (zoom) · 375.33 boom_low (rings) · 376.33 whoosh

### C5S080 · 376.39–382.63 · C5B075 · NIGHT · `c5s02`
- **Words** "So the US is hoping to implement what will I think later become known as the Kissinger diplomacy,"  **Why** 'what will … become known as the Kissinger diplomacy' → Kissinger at work (White House), the term as the hero title.
- **FX** #4 hero + #8 streaks + #16 · **Ref** s01 title look
- **Visual** N03 Kissinger at his desk/White House 1971 (PD), dark grade, streaks behind the title.
- **Assets** N03
- **Text** `the Kissinger diplomacy` word-by-word `the` @380.87 `Kissinger` @381.03 `diplomacy` @381.91 (t-display 120px hero halate)
- **Camera** push · **Key anim done** @382.00 · **Out** `CA` cut on action @382.63
- **SFX** 380.85 air_swell

### C5S081 · 382.63–389.11 · C5B076 · PAPER · `c5s02`
- **Words** "where they're trying to peel China away from the Soviet Union, weaken Soviet Union even more, because China is a big country."  **Why** 'peel China away from the Soviet Union, weaken Soviet Union … China is a big country' → triangle diagram, China peeled off the USSR.
- **FX** #2 diagram + paper-peel + scale · **Ref** D15 variation (triangle: US, Soviet Union, China; paper ground)
- **Visual** Three circles (G09): US (navy ring + halftone flag), Soviet Union (red hatched), China (red solid). China's circle peels off the USSR like a sticker @383.59; USSR circle shrinks @385.91; China circle grows @388.47.
- **Assets** G09, G13
- **Text** `peel` @383.59 (t-label) · `weaken` @385.91 (t-label) · `big country` word-by-word `big` @388.47 `country` @388.71 (t-serif-i)
- **Camera** slow push · **Key anim done** @388.50 · **Out** continuous (same layout, camera moves on — no cut) @389.11
- **SFX** 383.57 paper_tear (peel) · 385.89 dot_slide (shrink)

### C5S082 · 389.11–396.31 · C5B077 · PAPER · `c5s02`
- **Words** "If US can somehow get them against this big evil empire, well, US US gets the upper hand in the Cold War."  **Why** 'get them against this big evil empire … the upper hand in the Cold War' → the triangle tips like a seesaw: US + China up.
- **FX** #2 + seesaw motion (12 fps) · **Ref** D15 continued
- **Visual** China circle slides to the US side; the triangle base becomes a seesaw tilting the US side up @394.39.
- **Assets** G09
- **Text** `big evil empire` word-by-word `big` @391.27 `evil` @391.51 `empire` @391.91 (t-label) · `upper hand` word-by-word `upper` @394.39 `hand` @394.63 (t-serif-i) · `Cold War` word-by-word `Cold` @395.51 `War` @395.83 (t-display 90px ink)
- **Camera** tilt · **Key anim done** @395.65 · **Out** `W→` whip right @396.31
- **SFX** 394.37 dot_slide (seesaw) · 396.25 whoosh

### C5S083 · 396.31–399.67 · C5B078 · NIGHT · `c5s02`
- **Words** "So that's why US is talking with China."  **Why** 'So that's why US is talking with China' → Kissinger and Zhou Enlai talking (July 1971).
- **FX** #16 plate + FX.focusHunt · **Ref** —
- **Visual** N04 Kissinger–Zhou photo (July 1971), push.
- **Assets** N04
- **Text** `talking with China` word-by-word `talking` @398.47 `with` @398.95 `China` @399.19 (t-serif-i .clean)
- **Camera** push lands → focus hunt · **Key anim done** @399.01 · **Out** `FW` light-flash whip @399.67
- **SFX** 396.35 air_swell


## 8. Act VIII — Taiwan worried — the Strait crises flashback (399.67–454.22)
Music: thin under 399–415; rewind texture 415.43; tension drums low under the invasions 423–434; brave swell on the carrier 438.46; uneasy pad 450–454. Tone: worry → flashback tension → reassurance → worry.

### C5S084 · 399.67–405.11 · C5B079 · NIGHT · `c5s03`
- **Words** "Of course, this does not really mean that US is not supporting Taiwan anymore. That's not the question."  **Why** 'this does not really mean that US is not supporting Taiwan anymore' → US forces in Taiwan (1960s), celadon Taiwan tab.
- **FX** #10 Vox layered + #13 · **Ref** s09 variation
- **Visual** N25 US military in Taiwan (USTDC / joint exercise 1960s, PD) cut-out over tinted panels; small celadon Taiwan map tab.
- **Assets** N25, E14
- **Text** `not` @400.71 (t-label) · `supporting Taiwan` word-by-word `supporting` @402.55 `Taiwan` @402.87 (t-serif-i .clean)
- **Camera** panels drift · **Key anim done** @404.50 · **Out** `CA` cut on action @405.11
- **SFX** 399.70 paper_slide

### C5S085 · 405.11–411.11 · C5B080 · NIGHT · `c5s03`
- **Words** "But for China, every time US wants anything, China wants give up support of Taiwan."  **Why** 'every time US wants anything, China wants give up support of Taiwan' → flows: US → China 'wants anything', China → back 'give up support of Taiwan'.
- **FX** #2 Sankey + ghost map · **Ref** D11 variation (two opposing flows over a ghost Pacific map)
- **Visual** Ghost Pacific (M01 15 %). Bone (neutral) flow US→China 'anything'; red return flow China→US splits off a thin celadon strand labelled 'support of Taiwan' that snaps.
- **Assets** M01
- **Text** `anything` @407.99 (flow label) · `give up` word-by-word `give` @409.67 `up` @409.99 (t-label) · `support of Taiwan` word-by-word `support` @410.15 `of` @410.47 `Taiwan` @410.63 (t-label)
- **Camera** slow push · **Key anim done** @410.50 · **Out** `PS` paper slide / torn-paper wipe @411.11
- **SFX** 407.97 marker_long (flow) · 410.61 paper_tear (strand snaps)

### C5S086 · 411.11–415.43 · C5B081 · PAPER · `c5s03`
- **Words** "That's what China is always asking for. And that's exactly why Taiwan is worried."  **Why** 'That's what China is always asking for … that's exactly why Taiwan is worried' → an agenda where every item ends in 'Taiwan', highlighted again and again.
- **FX** #18 highlighter ×3 (body text) + .label-box · **Ref** Pinterest idea: 'meeting agenda, repeated highlight'
- **Visual** G07 typeset agenda (narrated words only, rows blurred except the repeated word 'Taiwan'); three highlighter strokes; celadon 'worried' tab.
- **Assets** G07
- **Text** `always asking` word-by-word `always` @412.07 `asking` @412.55 (t-serif-i ink) · `worried` @414.79 (.label-box celadon)
- **Camera** drift down · **Key anim done** @414.77 · **Out** `W←` whip left @415.43
- **SFX** 412.05 highlighter_swipe (×3) · 415.37 whoosh

### C5S087 · 415.43–418.79 · C5B082 · NIGHT · `c5s03`
- **Words** "Oh, by the way, one important thing I completely forgot to mention so far,"  **Why** 'one important thing I completely forgot to mention' → a Sony Trinitron rewinds (tape-rewind lines) — we go back in time.
- **FX** #11 TV (Trinitron, rewind) + #13 · **Ref** §10.1.7 screens: Trinitron (different from intro IS065 crop) — Pinterest idea: 'VHS rewind'
- **Visual** E03 Trinitron frame; inside, earlier chunk shots run backwards fast with tracking lines (G17).
- **Assets** E03, G17
- **Text** `forgot to mention` word-by-word `forgot` @417.43 `to` @417.83 `mention` @417.99 (t-serif-i .clean)
- **Camera** slow push · **Key anim done** @418.13 · **Out** `FW` light-flash whip @418.79
- **SFX** 415.45 crt_click · 415.50 crt_hum (rewind whirr, dur 3.2) · 418.72 whoosh_soft

### C5S088 · 418.79–423.19 · C5B083 · PAPER · `c5s03`
- **Words** "which is also kind of tells you why Taiwanese got so freaked out over this,"  **Why** 'why Taiwanese got so freaked out over this' → a real 1950s front page about the attacks on Taiwan's islands; 'Formosa' highlighted.
- **FX** #5 newspaper (s06 look: tilted page, sepia, halftone grows with zoom) · **Ref** s06 newspaper variation (different page, tilt the other way)
- **Visual** N59 1958 front page (Quemoy shelling, fair use) tilted; camera pushes; body-text highlight on Formosa/Taiwan.
- **Assets** N59
- **Text** `freaked out` word-by-word `freaked` @421.99 `out` @422.31 (t-serif-i ink)
- **Camera** push to headline · **Key anim done** @422.60 · **Out** `CA` cut on action @423.19
- **SFX** 418.80 paper_rustle · 421.97 highlighter_swipe

### C5S089 · 423.19–427.27 · C5B084 · NIGHT · `c5s03`
- **Words** "is there were two times when Mao **Zedong's** China tried invading Taiwan."  **Why** 'two times when Mao Zedong's China tried invading Taiwan' → satellite of the Strait, two numbered thrusts.
- **FX** #3 satellite map + #19 arrows + #13 · **Ref** D14 variation (satellite + outlined districts + marker routes) — ink arrows
- **Visual** M04 Taiwan Strait satellite (map kit, Esri credit); two red arrows (PRC) from the Fujian coast numbered 1, 2 (yellow key number 'two'); Taiwan left in natural satellite colour here (max two accents).
- **Assets** M04
- **Text** `two times` word-by-word `two` @423.83 `times` @423.99 (t-display YELLOW key number '2') · `Mao Zedong's China` word-by-word `Mao` @424.39 `Zedong's` @424.79 `China` @425.59 (t-label) · `invading` @426.23 (t-label)
- **Camera** slow push · **Key anim done** @426.60 · **Out** continuous (same layout, camera moves on — no cut) @427.27
- **SFX** 423.81 marker_long (arrow 1) · 424.40 marker_long (arrow 2)

### C5S090 · 427.27–430.86 · C5B085 · NIGHT · `c5s03`
- **Words** "Like he launched some attacks on the islands that are close to you. The mainland"  **Why** 'attacks on the islands that are close to … the mainland' → zoom to Kinmen/Matsu hugging the coast; shelling bursts.
- **FX** #3 zoom + §10.6.3 contrast call-out + §10.6.7 rings · **Ref** D14 continued
- **Visual** Zoom to Kinmen (and inset Matsu); contrast call-out isolates the islands; small red burst rings from the mainland side.
- **Assets** M04
- **Text** `the islands` word-by-word `the` @428.63 `islands` @428.71 (t-label (map labels Kinmen / Matsu small)) · `the mainland` word-by-word `the` @430.22 `mainland` @430.30 (t-label)
- **Camera** zoom then FX.focusHunt · **Key anim done** @430.30 · **Out** `PS` paper slide / torn-paper wipe @430.86
- **SFX** 428.69 boom_low (bursts (soft))

### C5S091 · 430.86–434.06 · C5B086 · PAPER · `c5s03`
- **Words** "and you know if he succeeds, he would probably keep moving forward."  **Why** 'if he succeeds, he would probably keep moving forward' → a 1950s newspaper explainer map; the arrow keeps going toward Taiwan.
- **FX** #3 vintage newspaper map + #19 dashed arrow · **Ref** R10 variation (old printed map, marker route) — Pinterest idea: '1950s newspaper war map'
- **Visual** N60 1950s newspaper map of the Formosa Strait (fair use) as a card; a dashed red arrow continues from the islands across to Taiwan.
- **Assets** N60
- **Text** `keep moving forward` word-by-word `keep` @433.10 `moving` @433.26 `forward` @433.58 (t-serif-i ink)
- **Camera** track along the arrow · **Key anim done** @433.40 · **Out** `W↑` vertical whip up @434.06
- **SFX** 431.90 marker_long (dashed arrow) · 434.00 whoosh

### C5S092 · 434.06–440.94 · C5B087 · NIGHT · `c5s03`
- **Words** "But the only reason those attacks stopped was US sent a aircraft carrier through the Taiwanese **Strait,**"  **Why** 'the only reason those attacks stopped was US sent a aircraft carrier through the Taiwan Strait' → a real US carrier; cutting-the-curve into the satellite Strait where the carrier becomes a dot.
- **FX** #15 curve cut (FX.curveCut) + #1 photo + #3 · **Ref** s07 curve cut
- **Visual** N45 US carrier (Seventh Fleet, 1950s, US Navy PD) top-down/aerial; zoom-out curve cut @439.6 to M04 satellite with the carrier as a bone dot in the Strait.
- **Assets** N45, M04
- **Text** `aircraft carrier` word-by-word `aircraft` @438.46 `carrier` @439.10 (t-label .clean) · `Taiwan Strait` word-by-word `Taiwan` @439.82 `Strait` @440.54 (t-label)
- **Camera** expo zoom (curve cut only) · **Key anim done** @440.40 · **Out** continuous (same layout, camera moves on — no cut) @440.94
- **SFX** 434.10 wind (sea, dur 3) · 439.58 whoosh_big (curve cut)

### C5S093 · 440.94–445.50 · C5B088 · NIGHT · `c5s03`
- **Words** "basically sending a message to China, hey, don't mess with Taiwan, we got it's back."  **Why** 'sending a message to China, hey, don't mess with Taiwan, we got its back' → the carrier's route drawn through the Strait in yellow marker.
- **FX** #3 + yellow marker route (D14) + #13 word-by-word · **Ref** D14 continued (yellow route)
- **Visual** Yellow rough marker route traces the carrier's path through the Strait; Taiwan glows celadon.
- **Assets** M04
- **Text** `don't` @443.10 (t-serif-i .clean) · `mess` @443.42 · `with` @443.66 · `Taiwan` @443.82
- **Camera** slow pull-out · **Key anim done** @444.90 · **Out** `CA` cut on action @445.50
- **SFX** 441.40 marker_long (route 1.4 s)

### C5S094 · 445.50–450.38 · C5B089 · PAPER · `c5s03`
- **Words** "So now that US is talking with China, China now that the US is talking with China,"  **Why** 'So now that US is talking with China' → the Nixon–Zhou handshake (1972) printed as a card.
- **FX** #12 card + #16 · **Ref** —
- **Visual** N08 Nixon–Zhou handshake photo (Feb 1972, PD) on paper_cream with a thin rule frame; no text on the repeated words.
- **Assets** N08
- **Text** `talking with China` word-by-word `talking` @446.70 `with` @447.10 `China` @447.26 (t-label)
- **Camera** slow push · **Key anim done** @449.72 · **Out** `W↓` vertical whip down @450.38
- **SFX** 445.52 paper_slide · 450.32 whoosh

### C5S095 · 450.38–454.22 · C5B090 · NIGHT · `c5s03`
- **Words** "Taiwan is getting a little worried, not sure what the future holds."  **Why** 'Taiwan is getting a little worried, not sure what the future holds' → 1960s Taipei street under rolling fog.
- **FX** #1 footage + cloud/fog layer (s02 clouds) + FH · **Ref** —
- **Visual** E08 Taipei North Gate traffic; fog (assets/maps/clouds) rolls across.
- **Assets** E08
- **Text** `worried` @451.50 (t-label .clean) · `the future` word-by-word `the` @452.86 `future` @453.02 (t-serif-i .clean)
- **Camera** slow push · **Key anim done** @453.56 · **Out** `FW` light-flash whip @454.22
- **SFX** 450.40 wind (dur 3.8)


## 9. Act IX — The UN vote and the impossible compromise (454.22–520.89)
Music: dark pad on "worst dreams" 456.86; light pizzicato/pulse under the seat diagrams 467–513 (a touch of irony at Bezos 504.33); drop on "the CCP" 519.85. Tone: dread, then ironic (both sides angry).

### C5S096 · 454.22–458.70 · C5B091 · NIGHT · `c5s03`
- **Words** "Well, very quickly they realize that their worst dreams are coming true."  **Why** 'their worst dreams are coming true' → Fuseli's The Nightmare (painting as B-roll), slow push.
- **FX** #16 painting plate + vignette · **Ref** painting-as-B-roll (§10.5)
- **Visual** N51 Fuseli, The Nightmare (1781, PD), muted; push.
- **Assets** N51
- **Text** `worst dreams` word-by-word `worst` @456.86 `dreams` @457.26 (t-serif-i .clean) · `coming true` word-by-word `coming` @457.82 `true` @458.14 (t-label)
- **Camera** push 1.0→1.08 · **Key anim done** @458.10 · **Out** `PS` paper slide / torn-paper wipe @458.70
- **SFX** 454.25 air_swell (dark)

### C5S097 · 458.70–462.62 · C5B092 · PAPER · `c5s03`
- **Words** "Because soon do you remember that vote we talked about where every single year"  **Why** 'do you remember that vote … every single year' → the UN vote motif from c3/c4 returns; dots flicker year after year.
- **FX** D06 parliament dots (12 fps) · **Ref** D06 variation (callback of the c3/c4 UN vote graphic — same dot style; lead confirms with c4)
- **Visual** Paper; UN semicircle of grey dots; a 'vote' title; the semicircle refills quickly several times (every year).
- **Assets** G11
- **Text** `vote` @460.54 (t-serif ink title)
- **Camera** static · **Key anim done** @462.00 · **Out** `CA` cut on action @462.62
- **SFX** 460.52 dot_ticks (fill ×3)

### C5S098 · 462.62–467.02 · C5B093 · NIGHT · `c5s03`
- **Words** "the CCP or one of CCP's allies brings up this vote in the UN,"  **Why** 'the CCP or one of CCP's allies brings up this vote in the UN' → the UN General Assembly in session (1960s).
- **FX** #16 plate + #13 · **Ref** —
- **Visual** N47 UN GA session photo (UN Photo, fair use, credit), desaturated.
- **Assets** N47
- **Text** `CCP` @462.78 (t-label) · `allies` @464.86 (t-label) · `the UN` word-by-word `the` @466.46 `UN` @466.54 (t-display 110px .clean)
- **Camera** slow push · **Key anim done** @466.40 · **Out** `PT` push-through @467.02
- **SFX** 462.65 paper_rustle (assembly murmur (low))

### C5S099 · 467.02–473.18 · C5B094 · PAPER · `c5s03`
- **Words** "basically saying, Hey, let's kick out Taiwan, let's give that Chinese seat to the CCP. That vote is coming up."  **Why** 'kick out Taiwan, give that Chinese seat to the CCP. That vote is coming up' → the 'CHINA' nameplate: Taiwan's chip slides out, CCP's in.
- **FX** #16 cut-out + #12 + 12 fps swaps · **Ref** Pinterest idea: 'nameplate on a desk, swapped'
- **Visual** N48 UN 'CHINA' nameplate (cut-out, halftone) on paper; celadon Taiwan chip slides off @468.38, red CCP chip slides on @470.86; 'coming up' tab.
- **Assets** N48
- **Text** `kick out Taiwan` word-by-word `kick` @468.38 `out` @468.62 `Taiwan` @468.78 (t-label) · `Chinese seat` word-by-word `Chinese` @469.82 `seat` @470.22 (t-serif-i) · `CCP` @470.86 (t-label) · `coming up` word-by-word `coming` @472.38 `up` @472.70 (t-label)
- **Camera** slow push · **Key anim done** @472.60 · **Out** `PS` paper slide / torn-paper wipe @473.18
- **SFX** 468.36 dot_slide (out) · 470.84 dot_slide (in)

### C5S100 · 473.18–478.38 · C5B095 · PAPER · `c5s03`
- **Words** "And the US is saying that, hey, we we we are not against China coming into the UN."  **Why** 'we are not against China coming into the UN' → two-seat diagram: China's seat added beside Taiwan's.
- **FX** #2 diagram (two seats) + #13 · **Ref** NEW ref: 'two-seat diagram' (D06 mini, two chairs)
- **Visual** G08 two seat icons; China's dashed seat fills red @476.62.
- **Assets** G08
- **Text** `not against` word-by-word `not` @475.74 `against` @475.98 (t-label) · `China` @476.62 (t-label) · `into the UN` word-by-word `into` @477.50 `the` @477.74 `UN` @477.82 (t-label)
- **Camera** static · **Key anim done** @477.80 · **Out** `CA` cut on action @478.38
- **SFX** 476.60 pop_soft

### C5S101 · 478.38–484.78 · C5B096 · PAPER · `c5s03`
- **Words** "What we are against is kicking out Taiwan. One thing to explain here is none of the **sides** are actually asking for this."  **Why** 'What we are against is kicking out Taiwan … none of the sides are actually asking for this' → Taiwan's seat protected; both sides shake their heads.
- **FX** #19 pen X attempt + #2 · **Ref** two-seat diagram continued
- **Visual** A pen X starts toward Taiwan's seat and is blocked (bounces); then 'none of the sides' — both seats turn away (12 fps).
- **Assets** G08
- **Text** `against` @478.94 (t-label) · `kicking out Taiwan` word-by-word `kicking` @479.58 `out` @480.06 `Taiwan` @480.30 (t-label) · `none of the sides` word-by-word `none` @482.38 `of` @482.62 `the` @482.78 `sides` @482.86 (t-serif-i)
- **Camera** pull-out · **Key anim done** @484.12 · **Out** `W→` whip right @484.78
- **SFX** 479.56 marker_scratch (blocked) · 484.72 whoosh

### C5S102 · 484.78–490.25 · C5B097 · NIGHT · `c5s03`
- **Words** "Taiwan says keep CCP out. CCP says, give me the seat, keep Taiwan out."  **Why** 'Taiwan says keep CCP out. CCP says, give me the seat, keep Taiwan out' → Vox split screen: each side's demand.
- **FX** #10 split screen + #13 word-by-word · **Ref** Pinterest idea: 'Vox split-screen claims'
- **Visual** Left: Chiang (N13 crop, celadon edge); right: Mao (N12 crop, red edge); each demand typed under its leader.
- **Assets** N13, N12
- **Text** `Taiwan says` word-by-word `Taiwan` @484.78 `says` @485.34 (t-label) · `keep CCP out` word-by-word `keep` @485.74 `CCP` @486.06 `out` @486.70 (t-serif-i) · `give me the seat` word-by-word `give` @488.25 `me` @488.49 `the` @488.65 `seat` @488.73 (t-serif-i) · `keep Taiwan out` word-by-word `keep` @489.21 `Taiwan` @489.53 `out` @489.93 (t-serif-i)
- **Camera** halves drift apart · **Key anim done** @489.70 · **Out** continuous (same layout, camera moves on — no cut) @490.25
- **SFX** 484.80 whoosh_soft (split)

### C5S103 · 490.25–493.45 · C5B098 · NIGHT · `c5s03`
- **Words** "No one is saying that, hey, let's compromise. Both of us stay in here."  **Why** 'No one is saying … let's compromise. Both of us stay in here' → the two halves slide toward each other and stop short.
- **FX** #10 split continued + 12 fps · **Ref** split continued
- **Visual** Halves move together, stop with a gap; 'compromise' types in the gap and is crossed.
- **Assets** N13, N12
- **Text** `compromise` @491.61 (t-label (X)) · `both of us` word-by-word `both` @492.25 `of` @492.49 `us` @492.57 (t-serif-i)
- **Camera** static · **Key anim done** @492.90 · **Out** `PS` paper slide / torn-paper wipe @493.45
- **SFX** 491.59 marker_scratch

### C5S104 · 493.45–498.17 · C5B099 · PAPER · `c5s03`
- **Words** "No, both of them to this very point say they are real China, the other party is the fake China."  **Why** 'both of them … say they are real China, the other party is the fake China' → two flag prints stamped REAL / FAKE.
- **FX** #18 stamps (chokeSettle) + #12 · **Ref** Pinterest idea: 'rubber stamps on two documents'
- **Visual** G13 ROC flag (ink halftone) and PRC flag (red halftone) as prints; each gets 'REAL CHINA' then the other gets 'FAKE'.
- **Assets** G13
- **Text** `real China` word-by-word `real` @496.01 `China` @496.25 (stamp) · `fake` @497.53 (stamp FAKE)
- **Camera** small punch-ins · **Key anim done** @497.51 · **Out** `W↑` vertical whip up @498.17
- **SFX** 496.00 stamp_thud · 497.51 stamp_thud · 498.11 whoosh

### C5S105 · 498.17–503.53 · C5B100 · NIGHT · `c5s03`
- **Words** "Why would they get a UN set? So US is trying to like walk between the two demands, making a compromise."  **Why** 'Why would they get a UN seat? So US is trying to … walk between the two demands' → a vintage circus tightrope poster under a spotlight.
- **FX** #16 poster plate (painting rule) + lamp pool · **Ref** Pinterest idea: 'circus poster under spotlight'
- **Visual** N52 tightrope-walker lithograph (PD circus poster), muted; two demand tabs at the rope ends.
- **Assets** N52
- **Text** `UN seat` word-by-word `UN` @498.89 `seat` @499.21 (t-label) · `walk between` word-by-word `walk` @501.21 `between` @501.61 (t-serif-i .clean) · `two demands` word-by-word `two` @502.01 `demands` @502.17 (t-label) · `compromise` @503.05 (t-label)
- **Camera** slow push · **Key anim done** @503.00 · **Out** `CA` cut on action @503.53
- **SFX** 498.20 lamp_click · 501.19 air_swell

### C5S106 · 503.53–507.69 · C5B101 · PAPER · `c5s03`
- **Words** "And what is this Jeff **Bezos** quote? Where compromise is never a good solution."  **Why** 'this Jeff Bezos quote? Where compromise is never a good solution' → painting-to-print reveal: Bezos photo → column with the pull-quote underlined word by word.
- **FX** §10.7 painting-to-print reveal + pen underline per word · **Ref** Lincoln reel (§10.7) — colour photo instead of a painting
- **Visual** N18 Bezos colour photo full-frame → 1.2 s pull-back/up-pan into G06 typeset column (caption 'JEFF BEZOS', no real masthead); pull-quote underlined word by word.
- **Assets** N18, G06
- **Text** `Jeff Bezos` word-by-word `Jeff` @504.33 `Bezos` @504.57 (caption small caps) · `compromise` @506.01 (pull-quote + underline) · `is` @506.57 · `never` @506.73 · `a` @506.97 · `good` @507.05 · `solution` @507.21
- **Camera** pull-back 504.6→505.8 then drift · **Key anim done** @507.03 · **Out** `W→` whip right @507.69
- **SFX** 504.60 paper_rustle (pull-back) · 506.00 pencil_scribble (underline ×6 (one sound)) · 507.63 whoosh

### C5S107 · 507.69–513.77 · C5B102 · GRID · `c5s03`
- **Words** "US is trying to land this compromise, where they're trying to make both sides happy, when in reality both sides are just getting more pissed off."  **Why** 'make both sides happy … both sides are just getting more pissed off' → diagram: US in the middle; 'happy' crossed out; angry scribbles on both sides.
- **FX** #2 diagram + #19 scribbles · **Ref** D15 variation (three nodes in a row: Taiwan – US – CCP)
- **Visual** Grid paper; Taiwan (celadon), US (neutral outline), CCP (red); 'happy' tags pop then get crossed; boiling angry scribbles over both side nodes @512.9 (no text on 'pissed off' — the scribbles say it).
- **Assets** G09
- **Text** `both sides` word-by-word `both` @510.57 `sides` @510.81 (t-label) · `happy` @511.05 (t-serif-i (crossed @512.6))
- **Camera** slow push · **Key anim done** @513.20 · **Out** `PS` paper slide / torn-paper wipe @513.77
- **SFX** 511.03 pop_soft · 512.60 pencil_scribble

### C5S108 · 513.77–520.89 · C5B103 · PAPER · `c5s03`
- **Words** "Now, unfortunately, US does kind of pick which side it favors more, and that side is the CCP."  **Why** 'US does kind of pick which side it favors more, and that side is the CCP' → a balance scale tipping to the CCP side.
- **FX** #16 engraving cut-out + 12 fps tilt · **Ref** Pinterest idea: 'engraved balance scale'
- **Visual** N53 PD balance-scale engraving; Taiwan chip (celadon) on one pan, CCP chip (red) on the other; US weight drops on the CCP pan @519.29.
- **Assets** N53
- **Text** `pick which side` word-by-word `pick` @516.01 `which` @516.65 `side` @516.97 (t-serif-i ink) · `the CCP` word-by-word `the` @519.85 `CCP` @520.09 (t-label)
- **Camera** tilt · **Key anim done** @520.23 · **Out** `FW` light-flash whip @520.89
- **SFX** 519.27 dot_slide (scale tips) · 520.83 whoosh_soft


## 10. Act X — Kissinger again; Bush lobbies; allies unsure (520.89–598.03)
Music: build from "United Nations" 523.37; steady pulse under Bush 532–565; thin under "who would you trust" 580–588; leave an unresolved suspended chord into c6 at 598.03. Tone: tension, uncertainty, cliff-hanger.

### C5S109 · 520.89–524.17 · C5B104 · NIGHT · `c5s03`
- **Words** "Because while this vote is about to happen at the United Nations,"  **Why** 'while this vote is about to happen at the United Nations' → the UN General Assembly hall in depth (2.5D #3).
- **FX** #17 2.5D + #4 hero · **Ref** 2.5D: layers back wall + emblem, podium, delegates' desks, foreground desk blur
- **Visual** N46 UN GA hall photo (≥3000 px, UN Photo/Commons) into 4 layers; dolly in.
- **Assets** N46 (layers 🛠)
- **Text** `United Nations` word-by-word `United` @523.37 `Nations` @523.69 (t-display 140px hero halate)
- **Camera** dolly · **Key anim done** @523.50 · **Out** `CA` cut on action @524.17
- **SFX** 520.92 air_swell

### C5S110 · 524.17–528.33 · C5B105 · NIGHT · `c5s03`
- **Words** "Henry Kissinger is once again going to China, and this time officially."  **Why** 'Henry Kissinger is once again going to China, and this time officially' → Kissinger in Beijing, Oct 1971; 'officially' stamp.
- **FX** #16 plate + #18 stamp · **Ref** —
- **Visual** N05 Kissinger at the Great Hall with Zhou Enlai (Oct 1971); ink stamp 'officially' settles.
- **Assets** N05
- **Text** `once again` word-by-word `once` @525.45 `again` @525.61 (t-label .clean) · `China` @526.33 (t-label) · `officially` @527.45 (stamp)
- **Camera** push · **Key anim done** @527.80 · **Out** `PS` paper slide / torn-paper wipe @528.33
- **SFX** 527.43 stamp_thud

### C5S111 · 528.33–532.81 · C5B106 · PAPER · `c5s03`
- **Words** "And this actually plays a big part into how the countries vote."  **Why** 'plays a big part into how the countries vote' → UN member dots waver.
- **FX** D06 dots (12 fps) · **Ref** D06 variation (dots waver between grey shades; no counts)
- **Visual** G11 semicircle; dots flicker grey ↔ red/navy (undecided) as the camera drifts.
- **Assets** G11
- **Text** `countries vote` word-by-word `countries` @531.53 `vote` @532.09 (t-serif-i ink)
- **Camera** drift · **Key anim done** @532.15 · **Out** `W↓` vertical whip down @532.81
- **SFX** 529.50 dot_ticks (flicker) · 532.75 whoosh

### C5S112 · 532.81–538.81 · C5B107 · NIGHT · `c5s03`
- **Words** "Because at this time, the US ambassador to the UN is future president George H.W. Bush."  **Why** 'the US ambassador to the UN is future president George H.W. Bush' → Bush at the UN (1971), named.
- **FX** #4 hero + #16 + FH · **Ref** lower-third look (as C5S046)
- **Visual** N16 Bush as UN ambassador (1971), portrait; title first, name hero.
- **Assets** N16
- **Text** `US ambassador to the UN` word-by-word `US` @534.09 `ambassador` @534.49 `to` @535.13 `the` @535.29 `UN` @535.37 (t-label .clean) · `future president` word-by-word `future` @536.17 `president` @536.65 (t-label) · `George H.W. Bush` word-by-word `George` @537.13 `H.W.` @537.61 `Bush` @538.33 (t-display 120px hero halate)
- **Camera** push lands → focus hunt · **Key anim done** @538.20 · **Out** `CA` cut on action @538.81
- **SFX** 537.11 pop_soft

### C5S113 · 538.81–544.33 · C5B108 · PAPER · `c5s03`
- **Words** "And he's trying his best to implement the strategy that the administration itself is saying publicly,"  **Why** 'implement the strategy that the administration itself is saying publicly' → the official US statement (State Department Bulletin, Aug 1971), lines highlighted.
- **FX** #5 document + #18 highlighter · **Ref** s06 document variation
- **Visual** N57 State Dept Bulletin page (PD) tilted; highlighter on the lines about China's representation.
- **Assets** N57
- **Text** `strategy` @541.37 (t-label) · `publicly` @543.61 (highlight)
- **Camera** push · **Key anim done** @543.70 · **Out** `PS` paper slide / torn-paper wipe @544.33
- **SFX** 541.35 paper_flip · 543.59 highlighter_swipe

### C5S114 · 544.33–548.80 · C5B109 · GRID · `c5s03`
- **Words** "where they want to bring in China to the United Nations, but they don't want to kick out Taiwan."  **Why** 'bring in China to the United Nations, but … don't want to kick out Taiwan' → the two-seat diagram returns (continuity).
- **FX** #2 two-seat diagram · **Ref** two-seat diagram (callback of C5S100)
- **Visual** G08 on grid paper: China's seat fills, Taiwan's seat stays celadon with a pen tick.
- **Assets** G08
- **Text** `bring in China` word-by-word `bring` @545.13 `in` @545.37 `China` @545.61 (t-label) · `don't` @547.21 (t-label) · `kick out Taiwan` word-by-word `kick` @547.61 `out` @547.77 `Taiwan` @547.93 (t-label)
- **Camera** static · **Key anim done** @548.14 · **Out** `W→` whip right @548.80
- **SFX** 545.11 pop_soft · 547.90 marker_scratch (tick) · 548.74 whoosh

### C5S115 · 548.80–554.00 · C5B110 · NIGHT · `c5s03`
- **Words** "So they're trying to guess some kind of compromise, and throughout the weekend before this vote,"  **Why** 'trying to … compromise, and throughout the weekend before this vote' → a desk calendar under a lamp: the weekend.
- **FX** #12 + lamp pool (R9 lighting) + #18 · **Ref** Pinterest idea: 'desk calendar under a lamp'
- **Visual** G15 desk calendar (October 1971 page, real dates) under a lamp; Saturday + Sunday get a highlighter stroke @552.32.
- **Assets** G15
- **Text** `compromise` @550.64 (t-label) · `the weekend` word-by-word `the` @552.16 `weekend` @552.32 (t-serif-i .clean)
- **Camera** slow push · **Key anim done** @553.40 · **Out** `CA` cut on action @554.00
- **SFX** 548.85 lamp_click · 552.30 highlighter_swipe

### C5S116 · 554.00–557.84 · C5B111 · NIGHT · `c5s03`
- **Words** "George Bush is Bush one is talking with all these other delegations,"  **Why** 'George Bush … is talking with all these other delegations' → Bush with delegates at the UN.
- **FX** #16 plate + §10.6.5 focal call-out · **Ref** —
- **Visual** N17 Bush among delegates (UN Photo, 1971); focal blur follows him.
- **Assets** N17
- **Text** `George Bush` word-by-word `George` @554.00 `Bush` @554.56 (t-label) · `delegations` @557.20 (t-label)
- **Camera** slow pan · **Key anim done** @557.20 · **Out** `PT` push-through @557.84
- **SFX** 554.02 paper_rustle (murmur (low))

### C5S117 · 557.84–565.52 · C5B112,C5B113 · PAPER · `c5s03`
- **Words** "telling them, hey, US policy is not abandoning Taiwan at all. We don't want to abandon Taiwan at all, so let's not vote against abandoning Taiwan."  **Why** 'telling them, hey, US policy is not abandoning Taiwan at all …' → painting-to-print: Bush in colour → a newspaper column; the quote underlined word by word.
- **FX** §10.7 painting-to-print reveal (2nd, mirrored: pan DOWN, column on the left) · **Ref** Lincoln reel (§10.7) variation
- **Visual** N16b Bush colour photo full-frame → pull-back into G06 typeset column (caption 'GEORGE H.W. BUSH'); pull-quote = his narrated words; then slow drift down the column through 'let's not vote against abandoning Taiwan'.
- **Assets** N16b, G06
- **Text** `US` @558.64 (pull-quote) · `policy` @558.96 · `is` @559.36 · `not` @559.60 · `abandoning` @560.00 · `Taiwan` @560.72 · `at` @561.12 · `all` @561.20
- **Camera** pull-back 558.0→559.2; drift down · **Key anim done** @564.86 · **Out** `W↓` vertical whip down @565.52
- **SFX** 558.00 paper_rustle (pull-back) · 558.62 pencil_scribble (underline (one sound)) · 565.46 whoosh

### C5S118 · 565.52–572.08 · C5B114 · NIGHT · `c5s03`
- **Words** "He's telling countries that, but countries are having a very hard time believing that because he's just an ambassador."  **Why** 'countries are having a very hard time believing that because he's just an ambassador' → doubtful delegates; Bush's small label 'just an ambassador'.
- **FX** #16 plate + #19 question marks · **Ref** —
- **Visual** N49 delegates listening (UN Photo 1971), sepia; two pen '?' marks; Bush chip with label.
- **Assets** N49, N16
- **Text** `hard time believing` word-by-word `hard` @568.56 `time` @568.80 `believing` @569.04 (t-serif-i .clean) · `just an ambassador` word-by-word `just` @570.64 `an` @570.80 `ambassador` @570.96 (t-label)
- **Camera** slow push · **Key anim done** @571.40 · **Out** `CA` cut on action @572.08
- **SFX** 569.00 pencil_scribble (?)

### C5S119 · 572.08–577.44 · C5B115 · GRID · `c5s03`
- **Words** "Even they know how much influence Kissinger has, and even he knows that the Kissinger is closer to the president."  **Why** 'how much influence Kissinger has … closer to the president' → two portrait-topped columns: Kissinger's rises to the president, Bush's stays short.
- **FX** #2 columns (12 fps) + portrait circles · **Ref** D02 variation (bars topped with circular portraits; two only, no numbers)
- **Visual** Grid paper; Bush circle (N16 crop) on a short column; Kissinger circle (N01 crop) on a column rising to a Nixon circle (N07) at the top.
- **Assets** N16, N01, N07, G12
- **Text** `influence` @573.04 (t-label) · `Kissinger` @573.52 (circle label) · `closer to the president` word-by-word `closer` @576.24 `to` @576.56 `the` @576.72 `president` @576.88 (t-serif-i)
- **Camera** tilt up with the column · **Key anim done** @576.78 · **Out** `W→` whip right @577.44
- **SFX** 573.02 dot_ticks (column rises) · 577.38 whoosh

### C5S120 · 577.44–580.40 · C5B116 · NIGHT · `c5s03`
- **Words** "He's part of the administration. He's going to China."  **Why** 'He's part of the administration. He's going to China' → Kissinger on his way to China (plane, 1971).
- **FX** #16 plate · **Ref** —
- **Visual** N06 Kissinger boarding/aboard plane 1971 (PD Nixon Library).
- **Assets** N06
- **Text** `administration` @578.16 (t-label) · `going to China` word-by-word `going` @579.44 `to` @579.76 `China` @579.92 (t-serif-i .clean)
- **Camera** push · **Key anim done** @579.80 · **Out** `PS` paper slide / torn-paper wipe @580.40
- **SFX** 577.46 whoosh_soft (engines)

### C5S121 · 580.40–583.76 · C5B116 · PAPER · `c5s03`
- **Words** "Who would you trust more? Would you trust the actions or would you trust this guy"  **Why** 'Who would you trust more? … the actions or … this guy' → split: Kissinger's actions vs Bush.
- **FX** #12 split cards + #13 · **Ref** Pinterest idea: 'which one? split cards'
- **Visual** Two cards on paper: left N05 crop (actions), right N16 crop ('this guy').
- **Assets** N05, N16
- **Text** `trust` @580.96 (t-serif-i) · `actions` @582.08 (t-label)
- **Camera** static · **Key anim done** @583.20 · **Out** `CA` cut on action @583.76
- **SFX** 580.42 paper_slide (×2)

### C5S122 · 583.76–588.72 · C5B117 · PAPER · `c5s03`
- **Words** "telling you hey US is not abandoning abandoning um abandoning Taiwan."  **Why** 'telling you hey US is not abandoning … Taiwan' → Bush's printed quote returns, a big pen '?' beside it.
- **FX** callback of the §10.7 column + #19 · **Ref** column callback
- **Visual** The G06 column (from C5S117) slides in as a clipping; pen question mark draws beside the pull-quote. Only the first 'abandoning' is cued (the stutter is not emphasised).
- **Assets** G06
- **Text** `not` @584.96 (t-label) · `abandoning` @585.12 (t-label) · `Taiwan` @587.92 (t-label)
- **Camera** slow push · **Key anim done** @588.10 · **Out** `PS` paper slide / torn-paper wipe @588.72
- **SFX** 586.00 pencil_scribble (?)

### C5S123 · 588.72–592.48 · C5B118 · PAPER · `c5s03`
- **Words** "That's all to say that US allies are already kinda unsure."  **Why** 'US allies are already kinda unsure' → UN dots of US allies flicker.
- **FX** D06 dots + .hl · **Ref** D06 variation (US allies ringed, flickering)
- **Visual** G11 semicircle; a group of dots ringed 'US allies' flicker navy ↔ grey at 12 fps (US allies wavering).
- **Assets** G11
- **Text** `US allies` word-by-word `US` @589.84 `allies` @590.16 (t-label) · `unsure` @591.60 (t-serif-i ink)
- **Camera** drift · **Key anim done** @591.82 · **Out** `FW` light-flash whip @592.48
- **SFX** 589.82 dot_ticks (flicker) · 592.42 whoosh_soft

### C5S124 · 592.48–598.03 · C5B119 · NIGHT · `c5s03`
- **Words** "They don't exactly know what the US is trying to do, so we don't exactly know how this vote is gonna play out."  **Why** 'nobody knows what the US is trying to do … how this vote is gonna play out' → the UN voting board, unlit and blurred; focus hunts; hand-off to c6.
- **FX** #16 plate + FX.focusHunt + rack focus · **Ref** D12-style blur on a real board
- **Visual** N50 UN GA electronic voting board (1970s), blurred; focus hunts but never resolves the tally; camera slow push into the board (continues into c6's first shot).
- **Assets** N50
- **Text** `this vote` word-by-word `this` @596.64 `vote` @596.88 (t-serif-i .clean)
- **Camera** slow push (still moving at the end = cut on action into c6) · **Key anim done** @597.40 · **Out** `CA` cut on action @598.03
- **SFX** 592.50 air_swell · 596.30 tick_soft

## 11. Coverage tables

### 11.1 Effects (MANUAL §5 + §10)
| effect | scenes |
|---|---|
| #1 B-roll photo/footage | 001, 003, 011, 013, 027, 039, 042, 068, 071, 092, 095 (11) |
| #2 charts / diagrams | 005, 006, 015, 016, 019, 026, 031, 034, 047, 048, 049, 062, 073, 081, 082, 085, 100, 101, 107, 114, 119 (21) |
| #3 maps | 010, 021, 025, 036, 050, 052, 053, 059, 063, 066, 078, 079, 089, 090, 091, 092, 093 (17) |
| #4 film-title typography (hero) | 003, 029, 037, 043, 046, 080, 109, 112 (8) |
| #5 document / newspaper | 012, 041, 051, 055, 060, 070, 075, 088, 113 (9) |
| #8 light streaks | 009, 020, 029, 043, 058, 080 (6) |
| #10 Vox layered / split | 007, 030, 045, 084, 102, 103 (6) |
| #11 TV (varied sets) | 014, 067, 087 (3) |
| #12 collage / cards / timeline / board | 002, 004, 008, 009, 022, 028, 035, 044, 054, 059, 064, 065, 066, 076, 094, 099, 104, 115, 121 (19) |
| #13 text animations (odometer, count, typewriter, word-by-word) | 002, 005, 007, 023, 027, 030, 032, 033, 043, 050, 053, 056, 061, 068, 069, 070, 076, 084, 087, 089, 093, 098, 100, 102, 121 (25) |
| #14 gate weave | 011, 013, 014, 024, 039, 068, 071 (7) |
| #15 curve cut | 092 (1) |
| #16 hi-quality plate | 001, 003, 006, 013, 017, 020, 024, 029, 033, 035, 038, 040, 045, 046, 061, 069, 072, 074, 077, 080, 083, 094, 096, 098, 099, 105, 108, 110, 112, 116, 118, 120, 124 (33) |
| #17 2.5D | 037, 058, 109 (3) |
| #18 rough reveal / highlighter / stamps | 012, 018, 038, 044, 054, 055, 060, 062, 086, 104, 110, 113, 115 (13) |
| #19 markups (pen, X, arrows, circles) | 001, 008, 011, 016, 018, 019, 031, 032, 040, 041, 042, 047, 056, 057, 065, 070, 074, 077, 089, 091, 101, 107, 118, 122 (24) |
| #20 map call-outs / pins | 010, 021, 025, 050, 052, 079 (6) |
| §10.6 call-outs (contrast / text / focal / radio waves / highlighter) | 012, 051, 052, 057, 060, 072, 075, 077, 079, 090, 116 (11) |
| §10.7 painting-to-print reveal | 106, 117, 122 (3) |
| FX.focusHunt | 003, 012, 017, 033, 046, 079, 083, 090, 095, 112, 124 (11) |
| whips / flash whips | W ×39, FW ×11 (directions vary) |
| cut on action / push-through / paper slide / match cut / continuous | CA ×35, PT ×5, PS ×23, MC ×1, cont ×10 |
| iris | none ✔ |

### 11.2 Reference layouts used (all as VARIATIONS)
| ref | scenes | variation |
|---|---|---|
| D01 — bars + dashed threshold + label box + halftone object | 005, 006 | growth bars all landing in a 9–10 % band; halftone Taiwan factory at the base |
| D02 — bars topped with portraits | 119 | two columns only (Bush vs Kissinger), no numbers, top = the president |
| D03 — isotype grid | 026, 036 | engineer pictograms that walk to Taiwan; population dots on the map |
| D04 — horizontal bars + serif title, italic emphasis | 015 | bars become rungs of a manufacturing ladder |
| D05 — line chart + era band | 006 | era band "American aid" that ENDS while growth continues |
| D06 — parliament dots + highlighted title | 097, 100, 111, 123 | UN member semicircle (callback of c3/c4), flickering = unsure |
| D07 — collage poster | 004, 028 | five product ads + "MADE IN TAIWAN" stamp |
| D08 — telegram | 070 | teletype diplomatic cable on yellow flimsy |
| D09 — old city map | 070 | old Peking map under the cable |
| D10 — tilted topo map + routes | 025, 059, 066 | vintage colour atlas: many routes converge on Taiwan; Pakistan→Beijing; back to the US |
| D11 — dark Sankey over ghost map | 049, 085 | influence flows Kissinger→president/policy; US↔China demands |
| D12 — dark list + focus pull | 023, 056, 124 | conference programme; struck-through public schedule |
| D13 — dark line chart over ghost map | 034 | celadon "up and up" line over ghost Taiwan |
| D14 — satellite + district + yellow route | 089, 090, 093 | Taiwan Strait: invasion arrows, Kinmen/Matsu call-out, carrier route in yellow marker |
| D15 — relationship diagram | 031, 032, 062, 081, 082, 107 | Terman↔government; US–USSR–China triangle (peel/seesaw); Taiwan–US–CCP row; first contact line |
| R4 — ranked bars with logos | 008 | logos on fanned annual-report covers |
| R5 — isotype | 026, 036 | (with D03) population dots |
| R7 — line/timeline | 002, 009 | decade ruler; night story timeline |
| R9 — cork board + string + lamp pool | 064, 065, 115 | the secret-trip board (ink thread) |
| R10 — old map + marker route | 091 | 1950s newspaper Strait map with dashed arrow |
| R11 — muted beige map + leader labels | 052, 078, 079 | Cold War world map: "big evil empire" |
| R12 — relief map region fill + halftone + glow | 010, 021, 036 | Taiwan pins; China ink fill vs celadon Taiwan |
| s06 newspaper — tilted page, halftone | 088, 113 | 1958 Quemoy front page; State Dept Bulletin |
| 2.5D (s10) — depth layers | 037, 058, 109 | Mao on Tiananmen; PIA 707 at night; UN General Assembly hall |
| §10.7 Lincoln reel — painting-to-print | 106, 117, 122 | Bezos; Bush (mirrored) |
| s11 markups — pen marks on photos | 001, 011, 031, 040 | tick on the EPZ; X on "high tech", placard circle, Kitchen Debate X |

D01–D15: **all 15 used** (several twice, each time varied). R1/R6/R8 are covered by their intro-pack twins D01/D04/D06; R2/R3 skipped
(owner). New scenes reuse the approved samples' code: s02 (globe/satellite), s06 (newspaper), s09 (layered), s10 (2.5D), s11 (markups).

### 11.3 NEW reference ideas (from our own search — Pinterest / Vox / editorial design), described
| idea | scene(s) | what it looks like / how we build it |
|---|---|---|
| Smile curve (Stan Shih value-chain chart) | C5S016, C5S019 | editorial economics chart: U-shaped ink curve on grid paper, high ends shaded "profits", our celadon dot at the bottom; the dot tries to climb (dashed arrow) and slides back |
| Macro country-of-origin label | C5S003 | shallow-depth macro of a real "MADE IN TAIWAN" stamp; focus hunt; title halation |
| Stacked blocks on one pillar | C5S073 | isometric-flat blocks ("foreign policy", "other policies") dropping onto one column "one assumption" (Vox explainer staple) |
| Vox split-screen claims | C5S102–C5S103 | two leaders, two demands typed under each; halves slide together and stop short ("no compromise") |
| Rubber stamps REAL / FAKE | C5S104 | two halftone flag prints, each stamped by the other side |
| Circus poster under a spotlight | C5S105 | PD tightrope lithograph lit by a lamp pool — "walk between the two demands" |
| Engraved balance scale | C5S108 | PD engraving cut-out; chips on pans; US weight drops on the CCP side |
| Detective board (R9 variant) with ink thread | C5S064–C5S065 | the secret trip's "evidence": plane, clipping, struck schedule, Pakistan — strings in bone/ink (red = PRC code) |
| Declassified memo with highlighted lines | C5S060 | the real Kissinger–Zhou memcon, two paper layers, text call-out |
| VHS rewind on a Trinitron | C5S087 | "I forgot to mention" → tape rewinds with tracking lines, back to the 1950s |
| Night-lights globe | C5S063 | NASA Black Marble — "while the world doesn't know" — a faint route over the Himalayas |
| Patient chart / desk calendar / wall clock props | C5S054, C5S115, C5S069 | real props or typeset cards, lamp-lit, matching "gets sick", "the weekend before", "an hour before" |

### 11.4 Ground rhythm (N night · P paper · G grid)
```
001N 002P 003N 004P 005G 006G 007N 008P 009N 010N 011N 012P 013N 014N 015P 016G 017N 018P 019G 020N
021N 022P 023N 024N 025P 026G 027N 028P 029N 030P 031P 032P 033N 034N 035P 036N 037N 038P 039N 040N
041P 042N 043N 044P 045N 046N 047P 048P 049N 050N 051P 052N 053N 054P 055P 056N 057P 058N 059P 060P
061N 062G 063N 064N 065N 066P 067N 068N 069P 070P 071N 072N 073P 074N 075P 076N 077N 078P 079P 080N
081P 082P 083N 084N 085N 086P 087N 088P 089N 090N 091P 092N 093N 094P 095N 096N 097P 098N 099P 100P
101P 102N 103N 104P 105N 106P 107G 108P 109N 110N 111P 112N 113P 114G 115N 116N 117P 118N 119G 120N
121P 122P 123P 124N
```
Longest same-ground run (PAPER+GRID counted together): **3** ✔ (rule ≤ 3).

### 11.5 Transitions in order (never the same type twice in a row)
W→, CA, FW, CA, PS, W→, CA, PS, W←, PT, CA, W→, CA, W↑, PS, CA, PS, W↓, FW, CA, PS, W←, CA, W↑, CA, W↓, FW, PT, W→, CA, cont, W↑, CA, FW, W→, CA, W↓, PS, CA, PS, W→, FW, PS, W→, CA, W↓, cont, W→, CA, W←, CA, cont, PS, cont, W↑, PS, W→, MC, PS, W←, CA, W↓, CA, cont, W→, CA, PT, W↓, PS, FW, CA, W→, CA, PS, W↓, CA, W→, cont, W↑, CA, cont, W→, FW, CA, PS, W←, FW, CA, cont, PS, W↑, cont, CA, W↓, FW, PS, CA, PT, PS, CA, W→, cont, PS, W↑, CA, W→, PS, FW, CA, PS, W↓, CA, PS, W→, CA, PT, W↓, CA, W→, PS, CA, PS, FW, CA ✔

### 11.6 Verification
| check | result |
|---|---|
| no face cam | ✔ none (narrator off camera after the intro) |
| key animation finished + held ≥ 0.5 s before every cut | ✔ all 124 scenes list `Key anim done` ≤ out − 0.5 s (whips: − 0.66 s) |
| ≤ 3 same-ground scenes in a row | ✔ max 3 |
| no same transition twice in a row | ✔ (§11.5) |
| text cues on word starts, inside their scene | ✔ every cue validated against `transcript_c5.json` by the planner script |
| glow only on the hero | ✔ one "hero halate" per night scene at most; none on paper/grid |
| no iris, no flat grey maps, no upscaled paper scans | ✔ |
| cohesive with the intro | ✔ same grounds (night / paper / real grid papers), same D-pack layouts, same title/halation style, Tatung + Trinitron screens, celadon Taiwan, whips + cut on action, word-by-word serif captions |

### 11.7 Palette check
| colour | meaning | scenes |
|---|---|---|
| celadon | Taiwan / ROC | 002, 005, 010, 012, 015, 016, 019, 023, 024, 025, 026, 031, 034, 036, 042, 053, 069, 084, 085, 086, 093, 099, 102, 107, 108, 114 |
| red | PRC / CCP / Communist bloc | 036, 038, 042, 062, 064, 076, 078, 079, 081, 085, 089, 090, 091, 099, 100, 102, 104, 107, 108, 111 |
| navy | US / allies (contrast only) | 044, 062, 076, 081, 111, 123 |
| yellow | highlighter / key number / marker route | 005, 012, 026, 055, 056, 060, 069, 070, 086, 088, 089, 093, 113, 115 |

No blue-UMC / red-TSMC anywhere in c5. Every frame ≤ 2 accents (checked per scene: red+celadon, red+navy, celadon+yellow, red+yellow).

## 12. Open questions (defaults in DECISIONS.md)
1. "RAC" at 32.03 → shown as **RCA** (default) — Krish/lead listen once to confirm.
2. Unnamed people (Taiwanese leader = Chiang Kai-shek; the Secretary of State = William P. Rogers; Chinese leadership = Zhou Enlai): photos
   without name text (default) or a small ID label?
3. Map labels "Kinmen" / "Matsu" as small geographic labels although he says only "the islands" (default: yes, small t-label).
4. The announcement (C5B064): narrator says Kissinger will go to meet Mao; the footage is Nixon's real 15 July 1971 address → default: show
   the real footage, captions = his words (no fact-checking).
5. Cultural Revolution colour posters / Mao painting keep their red (red = PRC per the lead's colour decision), lightly muted — OK?
6. Jeff Bezos "quote" is the narrator's paraphrase → default: show his words as a pull-quote with the caption "JEFF BEZOS" (no quotation
   marks around a claimed exact quote? — default: quotation marks kept, it is how he presents it).
7. UN dots / seat motif must match c3/c4's UN vote graphics → lead to pass c4's motif spec to the c5s03 editor.
8. Map kit (`assets/maps/kit/`) is still empty — editors wait for M01–M07 or use the intro maps as placeholders only in drafts.

