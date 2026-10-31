# EDIT NOTES — CHUNK c1 “Taiwan: the chip rivalry” (Searching Lessons), LOCAL VO 0.00–602.86 (full audio 275.06–877.88)

Shot-by-shot plan for chunk c1 (the Silicon Valley origin story). Read with `project/LONGFORM.md`, `MANUAL.md` (§10.1–10.9 override older
sections; §5 effects; §6/§6.1 layouts), `project/c1/analysis/BEATS.md`, `ASSETS_NEEDED.md` (IDs), `SEGMENTS.md`, `DECISIONS.md`.
Prepared 2026-10-31 by the director / edit planner. Generated from `project/c1/gen/scenes_data.py` by `gen_edit.py` (which also
validates every cue against `transcript_c1.json` and runs the rhythm checks in §11) — **edit the data file and re-run** rather than this file.

## 0. How to read this file

- **Times** = LOCAL c1 seconds (`vo_c1.mp3`, `transcript_c1.json`); add 275.06 for the full audio. **105 scenes, C1S001–C1S105**, contiguous 0.00 → 602.86, every boundary on a word start.
- **Text cue `@t`** = start of the spoken word; first frame at `T(t) − 0.06`. Multi-word lines are revealed **word by word** (each word its own literal `T()`). Backticks = exact on-screen text; the word list after it gives each word's cue.
- **Words** = exact narration under the shot (ASR fixes in bold). **Why** = why the picture matches those words (§10.1.3).
- **Ground**: `NIGHT` (dark/cinematic/archival full-frame), `PAPER` (Texturelabs `_hires` papers, two layers, top ~90 %), `GRID` (graph/ruled/blueprint/ledger papers — `_hires` full-frame, K+E scans only as cards ≤ native size). ≤ 3 same ground in a row and PAPER+GRID ≤ 3 combined (checked §11.4).
- **FX** = MANUAL §5 numbers + §10 craft. Transitions: `W←/→/↑/↓` whip (`FX.whip`), `FW` light-flash whip, `CA` cut on action (camera/secondary motion — never an unfinished key animation), `HC` hard cut on action (the reel's variant), `PT` push-through, `PS` paper slide / torn-paper wipe, `MC` match cut (an element carries into the next shot), `CRT` CRT power-on cut, `cont` = same world continues (no cut). **No iris.** `FH` focus hunt (once per scene max), `CS` chokeSettle.
- **Hold rule (§10.9)**: the scene's key animation finishes and HOLDS ≥ 0.5 s before the out-transition starts. Column ‘hold’ in §11.6 = time from the last text cue to the cut; scenes under 0.9 s are flagged: their last word must use a short entrance (≤ 0.3 s rise) and the cut rides a camera move.
- **Glow**: `.halate` only on the scene's hero (marked ‘hero halate’); everything else `.clean`; paper never glows.
- **Ref** = Krish's intro pack `D01–D15` (`references/style-images/intro/`) or the originals `R1–R12` (`references/style-images/1–12`, built examples in `expected/layouts/`), each used as a **variation** (colour lead, orientation, density, entry). `s01–s11` = approved samples (`compositions/sNN-*.html`); `old SCnnn` = scene of the approved 10-minute edit (`templates/full-edit/segNN.html`, `example-docs/EDIT_NOTES.md`). New reference ideas are named “Pinterest idea: …”.
- **Palette (Silicon Valley mapping, decided here)**: `--west` = vermilion **= the West / California / Stanford / Terman's Silicon Valley / HP**; `--east` = navy (sky on night) **= the East coast, MIT, Harvard, Bell Labs, GE, Eli Lilly**; yellow = highlighter + the scene's one key number (12, 90 %, 1891, $100, 25, 800); celadon (Taiwan) unused in c1. People are neutral sepia/ink (Hoover is NOT red — red later means Morris Chang/TSMC; vermilion only as Stanford/West tags, bars, routes). Max two accents per frame.
- **No face cam** in c1 (§10.9). **Copyrighted images allowed** (fair use, credited in SOURCES.md + 13 px on-screen credit where customary). Image reuse allowed when needed (prefer new).
- **Maps** from `assets/maps/kit/` (N93) — never flat grey/beige relief; approved s02 satellite US map is the bar. Old-map scans (Rand McNally 1920, USGS) stay as the vintage-atlas D10/R10 look.
- **SFX** lines = object events (LOCAL s) → `compositions/c1sNN.sfx.json` (vocabulary SEGMENTS §3.4). Sound only the hero event per scene (§10.8 restraint); transition whooshes are added by the editor where a whip/flash lands.
- Hand-off IN: the intro ends with streaks flaring to bone (IS066); C1S001's first 4 frames are that bone flash fading into the painting.

## 1. Act I — Cold open: Terman's quote and the claim (0.00–46.13)
Music: soft textural pad continuing from the intro's flash; first pulse under 'father of Silicon Valley' 16.08; lift on 'copy it' 44.93.

### C1S001 · 0.00–7.20 · C1B001 · NIGHT · §10.7 phase A
- **Words** “When we set out to create a community of technical scholars in Silicon Valley, there wasn't much here.”  **Why** the quote describes an empty valley → a colour painting of the pre-war orchard valley, the quote set word by word over it.
- **FX** §10.7 painting-to-print (part A) + #16 plate + #13 rise · **Ref** Lincoln reel (§10.7)
- **Visual** Opens out of the intro's bone flash (first 4 frames bone → painting). Full-frame colour painting of the Santa Clara Valley orchards (N30), slow upward pan. Serif quote, left third, opening quote mark.
- **Assets** N30 (see ASSETS_NEEDED)
- **Text** `“a community` `a`@1.44 `community`@1.60 · `of technical scholars` `of`@2.08 `technical`@2.32 `scholars`@2.88 · `in Silicon Valley,` `in`@3.44 `Silicon`@3.68 `Valley`@4.48 · `there wasn't much here.”` `there`@5.28 `wasn't`@5.52 `much`@6.16 `here`@6.48 (serif-i, .clean, word by word)
- **Camera** pan up 0→−120 px (cam ease). **Out** `PT` @7.20.
- **SFX** 0.00 air_swell (from the intro flash) · 4.46 tick_soft · 7.10 whoosh_soft

### C1S002 · 7.20–12.96 · C1B002 · NIGHT
- **Words** “And the rest of the world looked awfully big. Now a lot of the rest of the world is here.”  **Why** 'the rest of the world looked awfully big' → a big painted globe dwarfs the valley; 'now … is here' → the globe's curve match-cuts into today's valley.
- **FX** #15 curve cut (globe limb → valley aerial, cut at peak ≈10.0) + #16 · **Ref** Pinterest idea: 'antique globe → satellite match cut'
- **Visual** Painted vintage globe (N31) huge in frame, a tiny vermilion dot for the valley; expo zoom into the dot; cut at peak velocity into the modern Silicon Valley aerial (E13), FH after landing.
- **Assets** N31, E13 (see ASSETS_NEEDED)
- **Text** `awfully big` `awfully`@8.88 `big`@9.44 (serif-i) · `is here` `is`@12.08 `here`@12.40 (hero halate)
- **Camera** expo zoom 8.9→10.0, FX.focusHunt @10.4. **Out** `CA` @12.96.
- **SFX** 9.6 whoosh_big (curve cut) · 10.05 air_swell

### C1S003 · 12.96–21.84 · C1B003–04 · PAPER · §10.7 phase B
- **Words** “That's a quote from Fred Terman, the father of Silicon Valley. And he's saying that in 1974.”  **Why** 'That's a quote from Fred Terman, the father of Silicon Valley … in 1974' → pull-back reveals the painting + aerial printed in a newspaper column with Terman's photo and a pull-quote; the date stamp lands on '1974'.
- **FX** §10.7 painting-to-print reveal + #5 page + #19 pen underline + #18 stamp · **Ref** Lincoln reel (§10.7) — typeset recreation, no real masthead
- **Visual** Eased 1.2 s pull-back + upward pan: the aerial is a halftone picture in a typeset column (two paper layers, top 90 %); Terman portrait (N01, fallback E01) in the next column; pull-quote in bold serif (the quote he just read); caption small caps. Rubber date stamp on the column.
- **Assets** N01, E01, E95 (see ASSETS_NEEDED)
- **Text** `quote` none · `FRED TERMAN` caption `Fred`@14.32 `Terman`@14.88 · `the father of Silicon Valley` `the`@15.92 `father`@16.08 `of`@16.56 `Silicon`@16.80 `Valley`@17.60 (pen underline per word) · stamp `1974`@20.24
- **Camera** pull-back 1.0→0.42 + pan up (cam ease), then slow drift. **Out** `W↑` @21.84.
- **SFX** 13.0 paper_rustle · 14.30 pop_soft · 16.0 pencil_scribble (underline) · 20.20 stamp_thud · 21.78 whoosh

### C1S004 · 21.84–28.88 · C1B005 · NIGHT
- **Words** “After he has achieved one of the greatest human feat anyone has ever achieved.”  **Why** 'one of the greatest human feats' → the finished thing: Silicon Valley at dusk, the scale of the feat.
- **FX** #16 plate + #8 streaks + #4 hero word · **Ref** —
- **Visual** Modern Silicon Valley dusk/night aerial (N13; fallback E13 graded), streak canvas low behind the sky, chromaticAberration 0.12.
- **Assets** N13, E13 (see ASSETS_NEEDED)
- **Text** `greatest`@24.72 (hero halate, t-display) · `human feat` `human`@25.60 `feat`@26.16 (serif-i) · `ever achieved` `ever`@27.76 `achieved`@28.00
- **Camera** slow push 1.0→1.08. **Out** `CA` @28.88.
- **SFX** 21.9 air_swell · 24.70 boom_low (soft)

### C1S005 · 28.88–34.13 · C1B006 · GRID
- **Words** “He. could arguably be put claim to building the Silicon Valley.”  **Why** 'put claim to building the Silicon Valley' → the words SILICON VALLEY being drafted on a blueprint, Terman's cut-out as the draughtsman.
- **FX** #18 rough + FX.chokeSettle + #19 pen (construction lines) · **Ref** Pinterest idea: 'architectural blueprint title lettering'
- **Visual** paper_blueprint_01_hires full-frame (two layers). Construction lines draw on, then the letters SILICON VALLEY are inked stroke by stroke; Terman halftone cut-out (E01) at left edge, bone on blue.
- **Assets** E95, E01 (see ASSETS_NEEDED)
- **Text** `building`@32.45 (t-label) · `SILICON`@33.01 `VALLEY`@33.57 (drafted, chokeSettle)
- **Camera** slight rotateX 8° plane, drift right. **Out** `PS` @34.13.
- **SFX** 28.9 paper_slide · 32.4 pencil_scribble (lines) · 33.0 marker_long

### C1S006 · 34.13–38.61 · C1B007 · PAPER
- **Words** “You see, before him, there wasn't much technical industry in the West at all.”  **Why** 'before him … not much technical industry in the West' → an illustrated California/West map with orchards and nothing industrial on it.
- **FX** #3 map (tilted illustrated map) + #20 call-out · **Ref** D10 variant (tilted pictorial map instead of topo; warmer, fewer routes)
- **Visual** Pictorial California map (N32) tilted rotateX 30°, rotateZ −6°, far-edge lens blur; a contrast call-out (§10.6.3) hard-cuts on the West coast: everything else veiled.
- **Assets** N32 (see ASSETS_NEEDED)
- **Text** `before him` `before`@34.69 `him`@35.17 · `technical industry` `technical`@36.37 `industry`@36.93 · `the West` `the`@37.57 `West`@37.73 (vermilion tag)
- **Camera** push 1.0→1.15 (ease-in, contrast cut at peak). **Out** `CA` @38.61.
- **SFX** 34.2 paper_slide · 37.70 stamp_thud (contrast cut, soft)

### C1S007 · 38.61–46.13 · C1B008 · NIGHT
- **Words** “And after him, we have something that's so powerful that countries around the world want to copy it.”  **Why** 'after him … so powerful that countries around the world want to copy it' → the blueprint card of SC005 copied (carbon copies) and landing across a dark world map.
- **FX** #3 map + #20 + #13 · **Ref** D13 variant (dark ghost map) + R12 glow on the valley; Pinterest idea: 'photocopy stack infographic'
- **Visual** Dark world map (N93 kit, ghost style). Valley glows vermilion (R12 glow edge); from 42.61 copies of the blueprint card fly out at 12 fps to 8–10 countries (no names), each lands with a small stamp.
- **Assets** N93 (see ASSETS_NEEDED)
- **Text** `after him` `after`@38.93 `him`@39.33 · `so powerful` `so`@41.09 `powerful`@41.41 (hero halate) · `countries around the world` `countries`@42.61 · `copy it` `copy`@44.93 `it`@45.49
- **Camera** slow pull-out. **Out** `W→` @46.13.
- **SFX** 38.7 air_swell · 42.6 dot_ticks (copies) · 44.9 stamp_thud soft · 46.05 whoosh

## 2. Act II — The trillion-dollar West (46.13–78.77)
Music: pulse + light percussion stem; hits on 12 (52.45) and 11 (65.41); playful pluck on apples/oranges.

### C1S008 · 46.13–52.45 · C1B009 · PAPER
- **Words** “Now, let me just paint you a picture. There are right now, as I'm recording this, in October 2026,”  **Why** 'let me just paint you a picture … October 2026' → a watercolour brush stroke paints the frame; the date lands.
- **FX** #13 odometer + watercolour wipe · **Ref** Pinterest idea: 'brush-stroke reveal title'
- **Visual** Paper ground; a wide watercolour stroke (watercolour_edge_mask) paints across; OCTOBER 2026 in ink as a dateline.
- **Assets** E95 (see ASSETS_NEEDED)
- **Text** `paint you a picture` `paint`@47.25 `you`@47.65 `a`@47.81 `picture`@47.89 (serif-i) · `OCTOBER`@50.93 `2026`@51.41 (odometer)
- **Camera** static, stroke moves. **Out** `CA` @52.45.
- **SFX** 47.2 paper_rustle (brush) · 50.9 odometer_tick

### C1S009 · 52.45–56.69 · C1B010 · NIGHT
- **Words** “12 companies in the United States that are worth more than a trillion dollars.”  **Why** '12 companies in the United States … worth more than a trillion dollars' → the approved s01 card.
- **FX** #4 film title + #8 streaks + #13 count · **Ref** s01 (approved)
- **Visual** s01 layout re-timed: streaks + warm glow; big yellow 12 (the scene's key number) counts up.
- **Text** `12`@52.45 (yellow, count) · `companies`@53.01 · `in the United States` `in`@53.41 `the`@53.49 `United`@53.65 `States`@53.97 · `$1 TRILLION` `trillion`@55.41
- **Camera** slow push. **Out** `MC` @56.69.
- **SFX** 52.40 counter_ticks · 55.40 tick_soft · 56.6 whoosh (12 flies to the kicker)

### C1S010 · 56.69–64.13 · C1B011 · PAPER
- **Words** “That number changes of course depending on the market, you know? Like now it's 12, some days it's probably less, some days it's more.”  **Why** 'that number changes … depending on the market … some days less, some days more' → the ranked chart breathes; a bar dips on 'less', a ghost bar on 'more'.
- **FX** #2 chart · **Ref** R4 variant — **horizontal** ranked bars, logos at the bar ends (old SC006 was vertical)
- **Visual** 12 horizontal vermilion bars ranked top→down with circular logo badges (E70); Eli Lilly's bar navy (East); dashed $1 T threshold vertical; bars breathe ±3 % (12 fps) from 57.33.
- **Assets** E70 (see ASSETS_NEEDED)
- **Text** kicker `12` (inherited) · `changes`@57.33 · `the market` `the`@58.77 `market`@58.93 · `12`@60.93 (kicker re-pops) · `less`@62.53 (Micron bar dips behind the line) · `more`@63.73 (ghost bar)
- **Camera** drift down; last 6 frames tilt down toward the base line. **Out** `CA` @64.13.
- **SFX** 56.7 pop_soft ×12 (soft) · 62.5 tick_soft · 63.7 pop_soft

### C1S011 · 64.13–68.77 · C1B012 · NIGHT
- **Words** “But out of those 12, 11 companies are west of the Mississippi River.”  **Why** 'out of those 12, 11 … west of the Mississippi River' → the approved s02 map.
- **FX** #3 map (burn reveal, river draw, pins, clouds) · **Ref** s02 (approved) — basemap upgraded from the map kit
- **Visual** s02 re-timed: West burns in vermilion, river draws, 11 HQ pins pop, clouds.
- **Assets** E90, N93 (see ASSETS_NEEDED)
- **Text** `12`@64.85 · `11`@65.41 · `WEST`@66.77 · `Mississippi River` `Mississippi`@67.41 `River`@68.29
- **Camera** push east. **Out** `cont` @68.77.
- **SFX** 64.9 counter_ticks · 65.4 burn_crackle · 66.0 map_pin ×9 · 67.4 marker_long (river)

### C1S012 · 68.77–73.89 · C1B013 · NIGHT
- **Words** “And the one hold out is of course Eli Lilly, which is a **drug** company in Indianapolis.”  **Why** 'the one holdout … Eli Lilly, a drug company in Indianapolis' → push into Indiana, Eli Lilly card.
- **FX** #20 map callout + #19 circle + #16 card · **Ref** R12 variant (navy Indiana) — approved R12b
- **Visual** Camera continues from SC011 to Indiana (navy halftone + glowing edge), pen circle on Indianapolis, Eli Lilly HQ card with logo.
- **Assets** E90 (see ASSETS_NEEDED)
- **Text** `one`@69.01 · `Eli Lilly` `Eli`@70.37 `Lilly`@70.93 · `drug company` `drug`@71.81 `company`@72.21 · `Indianapolis`@72.77
- **Camera** push to Indiana, FH on landing @70.6. **Out** `W↓` @73.89.
- **SFX** 70.35 pop_soft · 72.75 marker_scratch · 73.8 whoosh

### C1S013 · 73.89–78.77 · C1B014 · PAPER
- **Words** “Now of course this is not a fair comparison. It's like comparing apples to oranges”  **Why** 'not a fair comparison … apples to oranges' → an apple and an orange pinned as cards with ≠.
- **FX** #12 collage · **Ref** old SC010 (re-timed)
- **Visual** Two halftone cut-outs on torn paper cards (N71), stop-motion pins; hand-drawn ≠ between them.
- **Assets** N71 (see ASSETS_NEEDED)
- **Text** `not a fair comparison` `not`@75.09 `a`@75.25 `fair`@75.41 `comparison`@75.81 · `apples`@77.49 · `oranges`@78.13
- **Camera** static, cards wobble 12 fps. **Out** `PT` @78.77.
- **SFX** 73.9 paper_slide · 77.45 pin_pop · 78.10 pin_pop · 78.7 whoosh

## 3. Act III — A century ago: the lopsided East and the brain drain (78.77–143.72)
Music: drop the pulse on 'rewind' 79.25; sepia drone + melodic layer; tension texture under 'brain drain' 138.52.

### C1S014 · 78.77–86.93 · C1B015 · GRID
- **Words** “but if you rewind a hundred years ago, that equation is basically like very lopsided.”  **Why** 'rewind a hundred years … that equation … very lopsided' → years rewind 2026→1926 on a counter, then a balance scale drops hard to one side.
- **FX** #13 count + #2 diagram · **Ref** Pinterest idea: 'balance-scale infographic on graph paper' (variation of the old SC012 equation)
- **Visual** paper_graph_01_hires ground. Odometer 2026 rewinds (tape-rewind feel); an ink balance scale (WEST pan vermilion / EAST pan navy) tips heavily East on 'lopsided'.
- **Assets** E95 (see ASSETS_NEEDED)
- **Text** `rewind`@79.25 · `a hundred years` `a`@80.05 `hundred`@80.21 `years`@80.69 · `equation`@82.05 · `lopsided`@85.81 (rough, chokeSettle)
- **Camera** static; scale swings (ease inOut 12 fps). **Out** `CA` @86.93.
- **SFX** 79.2 counter_ticks (rewind) · 85.8 stamp_thud soft

### C1S015 · 86.93–94.68 · C1B016 · PAPER
- **Words** “Roughly 90% of the US GDP was happening in the east, like really far east on the on the coast.”  **Why** 'roughly 90% of US GDP … in the east … far east on the coast' → the scale's East pan becomes a tall navy bar, a stub for the West, East-coast skyline at the base.
- **FX** #2 chart + #18 highlighter · **Ref** R1/D01 variant (approved SC013, now navy watercolour tops + skyline cut-out)
- **Visual** R1 restyle: navy East bar rises to 90 % with watercolour top, vermilion West stub; dashed line + ink label box; halftone NYC 1921 skyline cut-out (`assets/archival/cutouts/nyc_skyline_1921_halftone.png`).
- **Assets** E95 (see ASSETS_NEEDED)
- **Text** `90%`@87.33 (label-box, yellow number) · `of US GDP` `US`@88.21 `GDP`@88.61 · `in the east` `east`@90.77 · `far east` serif-i `far`@91.89 `east`@92.29 (highlighter body-size) · `coast`@93.65
- **Camera** drift right. **Out** `MC` @94.68.
- **SFX** 87.3 counter_ticks · 88.2 pop_soft ×2 · 91.9 highlighter_swipe

### C1S016 · 94.68–99.96 · C1B017 · NIGHT
- **Words** “And Silicon Valley single handedly has changed that equation a lot.”  **Why** 'Silicon Valley single handedly has changed that equation' → the modern valley at night with the West bar shooting up over it.
- **FX** #8 streaks + #4 + #16 · **Ref** —
- **Visual** Night: E13 aerial (different crop from SC002) graded dark; the vermilion West bar from SC015 rises as a glowing column over the valley; the East bar shrinks to its side.
- **Assets** E13 (see ASSETS_NEEDED)
- **Text** `Silicon Valley` `Silicon`@95.16 `Valley`@95.96 (hero halate) · `single handedly` `single`@96.52 `handedly`@97.00 · `changed`@97.96
- **Camera** push 1.0→1.06. **Out** `W↑` @99.96.
- **SFX** 95.1 air_swell · 97.9 whoosh_soft

### C1S017 · 99.96–105.80 · C1B018 · NIGHT
- **Words** “So it's definitely interesting to see how Silicon Valley was birthed, because in the 1920s,”  **Why** 'how Silicon Valley was birthed … in the 1920s' → curve cut from today's valley back to its 1920s orchards.
- **FX** #15 curve cut + #14 weave · **Ref** old SC011 (re-timed)
- **Visual** A: modern aerial (E13) expo push → cut at peak ≈103.6 → B: 1920s orchard plate (E83), sepia, gate weave + flicker.
- **Assets** E13, E83 (see ASSETS_NEEDED)
- **Text** `birthed`@103.40 · `1920s`@104.68 (t-display, bone)
- **Camera** expo zoom then slow drift. **Out** `CA` @105.80.
- **SFX** 103.3 whoosh_big · 103.6 projector_click · 103.7 projector_loop (dur 2)

### C1S018 · 105.80–112.92 · C1B019 · PAPER
- **Words** “if you were a bright young engineer in California, let's say you studied at UC Berkeley or you studied at Stanford,”  **Why** 'a bright young engineer in California … UC Berkeley or … Stanford' → a collage poster of 1920s engineering students with the two campuses.
- **FX** #12 collage · **Ref** D07 variant (collage poster: photos + typographic boxes + stamps; ours in ink/paper with a vermilion Stanford stamp)
- **Visual** Paper collage: 1920s engineering students card (N15), Berkeley Campanile card (N14) @110.28, Stanford Quad card (E10 crop) @112.20; typographic box `bright young engineer`.
- **Assets** N15, N14, E10 (see ASSETS_NEEDED)
- **Text** `bright young engineer` `bright`@106.52 `young`@107.00 `engineer`@107.40 · `California`@108.12 · `UC Berkeley` `UC`@110.28 `Berkeley`@110.84 · `Stanford`@112.20 (vermilion stamp)
- **Camera** drift left. **Out** `PS` @112.92.
- **SFX** 106.5 paper_slide · 110.25 pin_pop · 112.18 stamp_thud

### C1S019 · 112.92–119.80 · C1B020 · GRID
- **Words** “which wasn't a powerhouse university back then, by the way, Stanford. Usually Berkeley was, but not Stanford.”  **Why** 'Stanford wasn't a powerhouse … Berkeley was, but not Stanford' → a two-bar ranking: Berkeley tall, Stanford short.
- **FX** #2 chart · **Ref** D02 variant (ranked bars topped with **campus-tower cut-outs** instead of portraits; only 2 bars, rank circles ①②)
- **Visual** K+E grid sheet card on stained paper (two layers). Bar ① Berkeley (ink) rises tall with Campanile cut-out on top; bar ② Stanford (vermilion) rises only a little with Memorial Church cut-out. Shapes only, no values.
- **Assets** N14, R11, E95 (see ASSETS_NEEDED)
- **Text** `powerhouse`@114.44 (serif-i) · `Berkeley was` `Berkeley`@117.88 `was`@118.28 · `not Stanford` `not`@118.76 `Stanford`@118.92
- **Camera** slow push. **Out** `CA` @119.80.
- **SFX** 114.4 pop_soft · 117.9 pop_soft · 118.9 tick_soft

### C1S020 · 119.80–125.48 · C1B021 · NIGHT
- **Words** “But if you studied at either of these universities, you had to leave Western United States”  **Why** 'you had to leave Western United States' → a 1920s train pulling out of a California station.
- **FX** #1 footage + #14 weave · **Ref** —
- **Visual** Archival 1920s train departure (N17), weave + flicker, vignette.
- **Assets** N17 (see ASSETS_NEEDED)
- **Text** `leave`@123.40 (serif-i, .clean)
- **Camera** train moves right = East. **Out** `W→` @125.48.
- **SFX** 119.8 projector_loop (dur 5.6) · 125.3 whoosh

### C1S021 · 125.48–129.88 · C1B022 · PAPER
- **Words** “and go all the way to the east to New York, New Jersey, Massachusetts,”  **Why** 'go all the way to the east to New York, New Jersey, Massachusetts' → yellow marker route across a 1920s railroad map, three numbered pins.
- **FX** #3 map + #20 + #19 marker · **Ref** R10 variant (approved R10b: tilted railroad map; now a there-only route with numbered pins ① ② ③)
- **Visual** Rand McNally 1920 map (E91) tilted, desaturated toward paper; fat yellow marker line from California east; pins pop at NY/NJ/MA (navy).
- **Assets** E91 (see ASSETS_NEEDED)
- **Text** `east`@127.08 · `New York` `New`@127.56 `York`@127.72 · `New Jersey` `New`@128.04 `Jersey`@128.20 · `Massachusetts`@128.76
- **Camera** track east along the line. **Out** `PT` @129.88.
- **SFX** 125.5 marker_long (dur 1.6) · 127.55 map_pin · 128.0 map_pin · 128.75 map_pin

### C1S022 · 129.88–135.88 · C1B023 · NIGHT
- **Words** “to work in major technological companies like Bell **Labs,** General Electric. Okay?”  **Why** 'major technological companies like Bell Labs, General Electric' → the real buildings, whip-chained, with the logos.
- **FX** #16 plates + whips (#9 retired)  · **Ref** —
- **Visual** Plate 1 Bell Labs West St (E16) → light-flash whip @133.25 → plate 2 GE Schenectady (R16/N16) → whip @134.2; logo cards.
- **Assets** E16, R16, N16 (see ASSETS_NEEDED)
- **Text** `major technological companies` `major`@131.08 `technological`@131.72 `companies`@132.68 · `Bell Labs` `Bell`@133.32 · `General Electric` `General`@134.28 (+ GE logo)
- **Camera** slow pushes on each plate. **Out** `CA` @135.88.
- **SFX** 133.2 whoosh · 134.15 whoosh

### C1S023 · 135.88–143.72 · C1B024 · PAPER
- **Words** “They were basically it was kind of a brain drain that was happening. All the smart people were leaving West.”  **Why** 'kind of a brain drain … all the smart people were leaving West' → BRAIN DRAIN title; graduate figures file out of California toward the East.
- **FX** #18 rough title (chokeSettle) + #2 isotype · **Ref** R5 variant (graduate pictograms walking single file across a halftone US silhouette)
- **Visual** Halftone US silhouette on paper; BRAIN DRAIN chokes in; graduate icons (assets/icons/graduate_*.svg) walk out of California eastward at 12 fps and turn navy as they cross.
- **Text** `BRAIN`@138.52 `DRAIN`@139.00 (t-display ink) · `smart people` `smart`@140.52 `people`@140.92 · `leaving`@141.64
- **Camera** drift east. **Out** `W→` @143.72.
- **SFX** 138.5 marker_scratch · 140.5 dot_ticks (dur 2) · 143.6 whoosh

## 4. Act IV — Herbert Hoover at Stanford, with the Twitter aside (143.72–277.60)
Music: mid-tempo storytelling; thin to a light playful layer 176.67–208.43 (no hits on the joke); stinger on 'admitted' 215.15; warm build 250–277.

### C1S024 · 143.72–151.08 · C1B025 · NIGHT
- **Words** “Now this setup bothered a lot of people, including Fred **Terman,** who we'll get to in just a second.”  **Why** 'this setup bothered a lot of people, including Fred Terman, who we'll get to in just a second' → Terman's card under a lamp, then pushed aside 'for a second'.
- **FX** #16 + §10.6.5 focal blur · **Ref** R9 lamp-pool look (no cork)
- **Visual** Lamp-pool desk: several 1920s faculty portraits (blurred); focal blur moves to Terman's young card (R01) on 'Fred Terman'; on 'second' the card slides out of frame.
- **Assets** R01 (see ASSETS_NEEDED)
- **Text** `bothered`@145.64 · `Fred Terman` `Fred`@147.64 `Terman`@148.12
- **Camera** slow drift, focal move. **Out** `CA` @151.08.
- **SFX** 145.6 paper_rustle · 147.6 lamp_click · 150.3 paper_slide

### C1S025 · 151.08–159.55 · C1B026 · NIGHT
- **Words** “But before Fred **Terman,** there was another formidable individual who was at the top of Stanford, and he did not like what he was seeing.”  **Why** 'another formidable individual … at the top of Stanford … did not like what he was seeing' → an unnamed dark silhouette looming over Stanford's arcades.
- **FX** #10 Vox layered + silhouette · **Ref** s09 (approved) layered panels
- **Visual** Tinted layered panels of Stanford c1900 (E10, R11) drifting; a neutral silhouette (N05) rises at the top; never recognisable.
- **Assets** E10, R11, N05 (see ASSETS_NEEDED)
- **Text** `formidable individual` `formidable`@153.24 `individual`@153.96 · `top of Stanford` `top`@155.64 `of`@155.96 `Stanford`@156.75 · `did not like` `did`@157.87 `not`@158.03 `like`@158.19
- **Camera** panels drift at 3 speeds. **Out** `FW` @159.55.
- **SFX** 153.2 paper_slide · 155.6 paper_slide · 159.5 whoosh_big (flash)

### C1S026 · 159.55–164.91 · C1B027 · PAPER
- **Words** “And that individual was none other than the future president of the United States, **Herbert** Hoover.”  **Why** 'the future president of the United States, Herbert Hoover' → the 1928 'HOOVER WINS' front page, his portrait clip slides in on 'Herbert'.
- **FX** #5 newspaper + §10.6.4 text call-out · **Ref** s06 (approved)
- **Visual** s06 re-timed: NYT 7 Nov 1928 (E40) on a tilted 3D page, sepia + halftone growing with zoom; text call-out on the body paragraph; portrait clip (R02).
- **Assets** E40, R02 (see ASSETS_NEEDED)
- **Text** `future president` `future`@161.71 `president`@162.11 · `United States` `United`@162.75 `States`@163.07 · `HERBERT HOOVER` `Herbert`@163.55 `Hoover`@164.11 (chokeSettle)
- **Camera** push to the headline. **Out** `PT` @164.91.
- **SFX** 159.6 paper_rustle · 161.7 highlighter_swipe · 163.5 paper_slide

### C1S027 · 164.91–172.75 · C1B028 · NIGHT · 2.5D #1
- **Words** “You see, Hoover himself was actually in the first class of Stanford in 1980, *(slip)* 1891.”  **Why** 'Hoover … in the first class of Stanford in 1891' → the approved 2.5D Main Quad with 1891 tucked behind the arch.
- **FX** #17 2.5D · **Ref** 2.5D-quad (approved SC023/s07)
- **Visual** Main Quad layers (E10, hoover/layers_quad re-made), dolly; young Hoover small card at 165.31.
- **Assets** E10, R02 (see ASSETS_NEEDED)
- **Text** `Hoover`@165.31 (t-label) · `first class` `first`@168.67 `class`@168.91 · `Stanford`@169.47 · `1891`@171.47 (yellow key number, behind the arch)
- **Camera** dolly z −80→150, FH at the stop @171.9. **Out** `CA` @172.75.
- **SFX** 165.0 air_swell · 171.45 boom_low (soft)

### C1S028 · 172.75–176.67 · C1B029 · NIGHT
- **Words** “He went to school when the campus was still under construction.”  **Why** 'he went to school when the campus was still under construction' → real construction photos of the Quad.
- **FX** #14 weave + #16 · **Ref** —
- **Visual** Stanford construction photo(s) 1887–91 (N10), weave + flicker + dust, slow push.
- **Assets** N10 (see ASSETS_NEEDED)
- **Text** `under construction` `under`@175.31 `construction`@175.63
- **Camera** push 1.0→1.06. **Out** `W↓` @176.67.
- **SFX** 172.8 projector_loop (dur 3.8) · 176.6 whoosh

### C1S029 · 176.67–181.23 · C1B030 · PAPER
- **Words** “And low key, there is a joke on Twitter where people say, like back in the day,”  **Why** 'there is a joke on Twitter … back in the day' → a tweet card (typeset, no real account) drops onto paper.
- **FX** #13 typewriter + #12 card · **Ref** Pinterest idea: 'tweet screenshot printed on textured paper'
- **Visual** Tweet card (N51) printed on paper, generic avatar; words appear as he says them.
- **Assets** N51 (see ASSETS_NEEDED)
- **Text** `joke`@178.67 · `Twitter`@179.15 · `back in the day` `back`@180.59 `in`@180.75 `the`@180.91 `day`@180.99
- **Camera** slight drift. **Out** `CA` @181.23.
- **SFX** 176.7 paper_slide · 178.6 tick_soft

### C1S030 · 181.23–185.79 · C1B031 · PAPER
- **Words** “you just hear these crazy stories of like some guy just not trying all his life,”  **Why** 'some guy just not trying all his life' → a vintage colour cartoon of a man asleep in a hammock.
- **FX** #16 illustration plate + #19 pen circle · **Ref** Krish's illustration rule (§10.5)
- **Visual** Puck-style colour lithograph (N34) on paper, pen circle around the snoozing man on 'not trying'.
- **Assets** N34 (see ASSETS_NEEDED)
- **Text** `crazy stories` `crazy`@182.03 `stories`@182.43 · `not trying` `not`@184.27 `trying`@184.51
- **Camera** slow push. **Out** `HC` @185.79.
- **SFX** 184.2 pencil_scribble

### C1S031 · 185.79–192.03 · C1B032 · NIGHT
- **Words** “and then all of a sudden some flip switches in his mind, and he's like, you know what? I'm gonna go try in my life,”  **Why** 'some flip switches in his mind … I'm gonna go try in my life' → a light switch flips, a bulb blooms.
- **FX** #1 footage + #8 streaks · **Ref** —
- **Visual** Macro of an old toggle switch (N63) flipping on 'flip'; bulb blooms into streak light.
- **Assets** N63 (see ASSETS_NEEDED)
- **Text** `flip switches` `flip`@187.31 `switches`@187.79 · `I'm gonna go try` `I'm`@189.79 `gonna`@190.03 `go`@190.43 `try`@190.67 (serif-i, .clean)
- **Camera** punch-in 1→1.3 on the switch. **Out** `W→` @192.03.
- **SFX** 187.28 lamp_click · 187.4 air_swell · 191.95 whoosh

### C1S032 · 192.03–198.19 · C1B033 · NIGHT
- **Words** “and they just have like this golden opportunity of like working at some crazy hedge fund company”  **Why** 'a golden opportunity … at some crazy hedge fund company' → a trading floor in layered panels, 'golden' pops yellow.
- **FX** #10 Vox layered + #13 fill · **Ref** —
- **Visual** Trading-floor photos (N25) tinted dark/bone in 3 drifting panels.
- **Assets** N25 (see ASSETS_NEEDED)
- **Text** `golden opportunity` `golden`@193.79 (FX.text.fill yellow → bone) `opportunity`@194.35 · `hedge fund` `hedge`@196.91 `fund`@197.39
- **Camera** panels drift. **Out** `CA` @198.19.
- **SFX** 192.1 paper_slide · 193.75 pop_soft

### C1S033 · 198.19–203.47 · C1B034 · PAPER
- **Words** “or working at some world leading company who was hiring people who had achieved nothing in life,”  **Why** 'a world leading company who was hiring people who had achieved nothing' → a real vintage HELP WANTED classified column, the line called out.
- **FX** #5 newspaper + §10.6.4 text call-out + #18 highlighter (body-size) · **Ref** Pinterest idea: 'classified-ads close-up with highlighter'
- **Visual** Classified page (N47), slight tilt; the ad paragraph returns at full strength; highlighter on 'no experience' line.
- **Assets** N47 (see ASSETS_NEEDED)
- **Text** `world leading company` `world`@199.39 `leading`@199.79 `company`@200.19 · `hiring`@200.91 · `achieved nothing` `achieved`@202.27 `nothing`@202.75
- **Camera** punch in 10 %. **Out** `HC` (planner rhythm fix — editor may pick another non-repeating type) @203.47.
- **SFX** 198.2 paper_rustle · 202.2 highlighter_swipe

### C1S034 · 203.47–208.43 · C1B035 · PAPER
- **Words** “and that kind of opportunity doesn't exist. It's kind of a meme, but it's a true reality, too,”  **Why** 'that kind of opportunity doesn't exist … kind of a meme, but a true reality' → the ad is crossed out, the tweet card returns stamped.
- **FX** #19 cross + #18 stamp · **Ref** s11 markups
- **Visual** Pen X over the ad; the tweet card (N51) slides back in; rubber stamp on it.
- **Assets** N47, N51 (see ASSETS_NEEDED)
- **Text** `doesn't exist` `doesn't`@204.75 `exist`@205.07 · `meme`@206.35 · `true reality` `true`@207.23 `reality`@207.47 (stamp)
- **Camera** static. **Out** `W↓` @208.43.
- **SFX** 204.7 marker_scratch · 206.3 paper_slide · 207.2 stamp_thud · 208.35 whoosh

### C1S035 · 208.43–212.83 · C1B036 · GRID
- **Words** “because Hoover failed all his exams when he was applying to Stanford,”  **Why** 'Hoover failed all his exams when he was applying to Stanford' → the 1891 entrance exam sheet, crossed subject by subject.
- **FX** #19 markups (cross)  · **Ref** s11 / old SC024
- **Visual** Entrance-exam recreation (R42) on ledger paper; quick pen crosses on each subject line.
- **Assets** R42, E95 (see ASSETS_NEEDED)
- **Text** `Hoover`@208.83 · `failed all his exams` `failed`@209.63 `all`@210.11 `his`@210.35 `exams`@210.59 · `Stanford`@212.11
- **Camera** slight push. **Out** `CA` @212.83.
- **SFX** 209.6 marker_scratch · 210.2 pencil_scribble ×4

### C1S036 · 212.83–216.59 · C1B037 · NIGHT
- **Words** “but he was a Quaker. So he got admitted to Stanford.”  **Why** 'but he was a Quaker. So he got admitted' → a colour painting of a Quaker meeting, then the admission card stamped.
- **FX** #16 painting plate + #18 stamp (chokeSettle) · **Ref** —
- **Visual** Quaker-meeting painting (N35) full frame, fringe blur; admission card (R42) slides on top, ADMITTED stamp.
- **Assets** N35, R42 (see ASSETS_NEEDED)
- **Text** `Quaker`@213.47 (hero halate) · `admitted`@215.15 (stamp)
- **Camera** slow pan. **Out** `W←` (planner rhythm fix — editor may pick another non-repeating type) @216.59.
- **SFX** 213.4 air_swell · 215.1 stamp_thud · 216.53 whoosh (transition)

### C1S037 · 216.59–220.40 · C1B038 · PAPER
- **Words** “And again, back then Stanford wasn't the university it is now.”  **Why** 'back then Stanford wasn't the university it is now' → two printed photos: 1890s Stanford vs today, a pen circle on 'now'.
- **FX** #19 markups · **Ref** markup-map variant (two prints on paper, pen circle + arrow)
- **Visual** Left: 1890s Quad print (E10); right: modern Stanford aerial (R12).
- **Assets** E10, R12 (see ASSETS_NEEDED)
- **Text** `back then` `back`@217.07 `then`@217.23 · `now`@219.63
- **Camera** drift. **Out** `PS` @220.40.
- **SFX** 217.0 paper_slide · 219.6 marker_scratch

### C1S038 · 220.40–224.08 · C1B039 · PAPER
- **Words** “But he got into this university and he met his wife.”  **Why** 'he got into this university and he met his wife' → Hoover and Lou Henry cards slide together.
- **FX** #12 collage · **Ref** old SC028
- **Visual** Two torn-edge cards (R02 young Hoover, R05 Lou Henry), small pen loop joining them.
- **Assets** R02, R05 (see ASSETS_NEEDED)
- **Text** `this university` `this`@221.52 `university`@221.76 · `his wife` `his`@223.36 `wife`@223.52
- **Camera** static. **Out** `W←` @224.08.
- **SFX** 220.4 paper_slide · 223.3 pin_pop · 223.95 whoosh

### C1S039 · 224.08–229.60 · C1B040 · NIGHT
- **Words** “He, you know, became uh became like a very successful person later in his life.”  **Why** 'became … a very successful person later in his life' → Hoover in public life, newsreel.
- **FX** #14 weave + #1 · **Ref** —
- **Visual** Hoover 1928 newsreel (E80), weave + flicker.
- **Assets** E80 (see ASSETS_NEEDED)
- **Text** `very successful` `very`@227.12 `successful`@227.52
- **Camera** —. **Out** `CA` @229.60.
- **SFX** 224.1 projector_loop (dur 5.4)

### C1S040 · 229.60–233.68 · C1B041 · NIGHT
- **Words** “By the 20s, he was secretary of commerce on his way to the White House.”  **Why** 'By the 20s … secretary of commerce on his way to the White House' → Commerce-era photo with a nameplate, whip to the White House.
- **FX** #16 + whip + #13 · **Ref** Pinterest idea: 'brass door-plate title'
- **Visual** Hoover Commerce photo (R04) with a brass-plate label; whip → White House 1920s plate (N23 alt / LOC).
- **Assets** R04, N23 (see ASSETS_NEEDED)
- **Text** `the 20s` `the`@229.76 `20s`@229.84 · `secretary of commerce` `secretary`@230.64 `of`@231.28 `commerce`@231.52 · `White House` `White`@233.04 `House`@233.28
- **Camera** push each. **Out** `FW` @233.68.
- **SFX** 230.6 tick_soft · 232.9 whoosh_big

### C1S041 · 233.68–240.48 · C1B042 · PAPER
- **Words** “And at the same time, he was sitting on Stanford's board of **trustee(s),** where he was kind of running the place.”  **Why** 'sitting on Stanford's board of trustees … running the place' → a seat diagram of the board with Hoover's seat dominant.
- **FX** #2 chart + #18 highlighter · **Ref** D06 variant (half-ring of seat dots; one seat enlarged with Hoover's portrait; highlighted phrase in the serif title)
- **Visual** Semicircle of 15 seat dots (generic count, no label), fills 12 fps; one seat swells and carries a Hoover circle (R02). Title serif with highlighter on 'running the place'.
- **Assets** R02, N49 (see ASSETS_NEEDED)
- **Text** `Stanford's Board of Trustees` `Stanford's`@235.52 `board`@236.40 `of`@236.72 `trustee(s)`@236.88 · `running the place` `running`@239.60 `the`@240.00 `place`@240.16 (highlighter)
- **Camera** slow push. **Out** `CA` @240.48.
- **SFX** 235.5 dot_ticks · 239.6 highlighter_swipe

### C1S042 · 240.48–245.28 · C1B043 · GRID
- **Words** “You know, he he was making all the decisions. He was figuring out how Stanford can sustain itself.”  **Why** 'making all the decisions … how Stanford can sustain itself' → a ledger with a pen ticking decision after decision.
- **FX** #19 pen ticks · **Ref** Pinterest idea: 'ledger with handwritten ticks'
- **Visual** Ledger scan card (`assets/intro/papers/ledger_specimen_p38.jpg`, native size) on paper_lined_01_hires; pen ticks down the column.
- **Assets** E95 (see ASSETS_NEEDED)
- **Text** `all the decisions` `all`@241.60 `the`@241.76 `decisions`@241.92 · `sustain itself` `sustain`@244.24 `itself`@244.64
- **Camera** tilt down the ledger. **Out** `PS` (planner rhythm fix — editor may pick another non-repeating type) @245.28.
- **SFX** 241.6 pencil_scribble ×5 · 245.20 paper_slide (transition)

### C1S043 · 245.28–250.64 · C1B044 · NIGHT
- **Words** “He figured out how to get the money, he he he put people he trusted in charge of the university.”  **Why** 'how to get the money … put people he trusted in charge' → dark money-flow streams into Stanford, ending at three trusted portraits.
- **FX** #2 flow chart · **Ref** D11 variant (Sankey money flow → Stanford, over a ghost California map; ends in portrait circles)
- **Visual** Dark ghost map (N93); bone/vermilion streams flow into a STANFORD box; out the other side into 3 portrait circles (N04 + 2 generic) on 'in charge'.
- **Assets** N93, N04 (see ASSETS_NEEDED)
- **Text** `the money` `the`@246.32 `money`@246.48 · `people he trusted` `people`@248.00 `he`@248.32 `trusted`@248.56 · `in charge` `in`@249.04 `charge`@249.20
- **Camera** drift right. **Out** `W↑` @250.64.
- **SFX** 246.4 dot_slide (dur 1.5) · 249.0 pop_soft ×3 · 250.55 whoosh

### C1S044 · 250.64–255.92 · C1B045 · NIGHT
- **Words** “And then in 1925, he built Stanford's business graduate program.”  **Why** 'in 1925, he built Stanford's business graduate program' → 1925 title, the business school's first building/bulletin.
- **FX** #4 hero + #16 · **Ref** —
- **Visual** 1925 odometer over a 1920s Stanford building plate (N18).
- **Assets** N18 (see ASSETS_NEEDED)
- **Text** `1925`@251.44 (hero halate, odometer) · `business graduate program` `business`@254.08 `graduate`@254.56 `program`@255.20 (serif-i) + object label `Stanford Graduate School of Business`
- **Camera** slow push. **Out** `CA` @255.92.
- **SFX** 251.4 odometer_tick · 254.0 paper_slide

### C1S045 · 255.92–262.00 · C1B046 · NIGHT · §10.7 phase A
- **Words** “His argument for this was pretty simple, and that's the argument we're gonna see for **Terman** make very soon.”  **Why** 'his argument … pretty simple … the argument we'll see Terman make' → Hoover's colour painted portrait full frame (the quote is coming).
- **FX** §10.7 painting phase + #16 · **Ref** Lincoln reel (§10.7)
- **Visual** Greene's 1956 painted portrait (R03), full frame, slow push; a small Terman stamp-photo slides into the corner on 'Terman'.
- **Assets** R03, E01 (see ASSETS_NEEDED)
- **Text** `argument`@256.32 · `pretty simple` `pretty`@257.52 `simple`@257.76 · `Terman`@260.48 (t-label, small)
- **Camera** push 1.0→1.05. **Out** `cont` @262.00.
- **SFX** 255.9 air_swell

### C1S046 · 262.00–270.08 · C1B047 · PAPER · §10.7 phase B
- **Words** “His argument is like I don't want all these young Californians going **east** just for business training and not coming back. And because of that, he set this up.”  **Why** Hoover's argument in his words → pull-back: the painting is printed in a newspaper column with a bold pull-quote, underlined word by word as spoken.
- **FX** §10.7 painting-to-print + #19 pen underline · **Ref** Lincoln reel (§10.7) — typeset recreation
- **Visual** 1.2 s pull-back + upward pan; caption small caps `HERBERT HOOVER`; pull-quote in bold serif; body text columns (sepia, halftone).
- **Assets** R03, E95 (see ASSETS_NEEDED)
- **Text** pull-quote word by word: `I`@263.12 `don't`@263.20 `want`@263.36 `all`@263.52 `these`@263.76 `young`@263.92 `Californians`@264.24 `going`@264.88 `east`@265.20 `just`@265.68 `for`@265.84 `business`@266.08 `training`@266.40 `and`@266.72 `not`@266.88 `coming`@267.12 `back.`@267.44 (pen underline per word)
- **Camera** pull-back then drift. **Out** `CA` @270.08.
- **SFX** 262.0 paper_rustle · 263.1 pencil_scribble (dur 4.3)

### C1S047 · 270.08–277.60 · C1B048 · NIGHT
- **Words** “Now the same argument is gonna be used by other people all around the world, but this was who were who first started saying this in the West.”  **Why** 'the same argument … used by other people all around the world, but … first … in the West' → radio-wave rings from Stanford on a world map, later echoes elsewhere.
- **FX** #3 map + §10.6.7 radio waves · **Ref** D13 variant (dark ghost world map; rings instead of a line)
- **Visual** Dark world map (N93); rings pulse from Stanford (vermilion); fainter rings later pop on other continents; Stanford ring brightest on 'first'.
- **Assets** N93 (see ASSETS_NEEDED)
- **Text** `all around the world` `all`@273.36 `around`@273.52 `the`@273.84 `world`@273.92 · `first`@275.76 · `the West` `the`@276.96 `West`@277.04
- **Camera** slow push on California. **Out** `FW` @277.60.
- **SFX** 270.1 tone_blip ×3 · 275.7 tone_blip · 277.5 whoosh_big

## 5. Act V — Enter Frederick Terman (277.60–357.32)
Music: title stinger on 'Frederick' 284.63; light under 1900/2000; melancholy pad under 'breaking his heart' 330.87/348.44.

### C1S048 · 277.60–283.91 · C1B049 · NIGHT
- **Words** “And then we get to The main guy, the father of the Silicon Valley, which is kind of spoiling the story, but nonetheless.”  **Why** 'the main guy, the father of the Silicon Valley' → a film-title card.
- **FX** #4 film title + #8 streaks + #13 random · **Ref** s01 look
- **Visual** Warm streaks; THE FATHER OF SILICON VALLEY title with random-letter reveal.
- **Text** `the main guy` `the`@279.03 `main`@279.27 `guy`@279.51 · `the father of` `the`@279.91 `father`@279.99 `of`@280.23 · `SILICON VALLEY` `Silicon`@280.39 `Valley`@281.11 (hero halate)
- **Camera** slow push. **Out** `CA` @283.91.
- **SFX** 279.0 letter_ticks · 280.4 air_swell

### C1S049 · 283.91–287.43 · C1B050 · PAPER
- **Words** “That guy is Frederick **Terman.** He was born in the 1900s.”  **Why** 'That guy is Frederick Terman. He was born in the 1900s.' → Terman cut-out on tinted Stanford panels, name in a label box, 1900 counts.
- **FX** #10 Vox layered (paper variant) + #13 count · **Ref** s09 variant on paper
- **Visual** Paper: two tinted Stanford 1920s panels (R11) + Terman cut-out (R01 or N01) on top; label box.
- **Assets** R01, R11 (see ASSETS_NEEDED)
- **Text** `FREDERICK TERMAN` `Frederick`@284.63 `Terman`@285.19 (label-box) · `born`@286.07 · `1900`@286.47 (count)
- **Camera** drift. **Out** `MC` @287.43.
- **SFX** 284.6 pop_soft · 286.4 counter_ticks

### C1S050 · 287.43–296.47 · C1B051–52 · GRID
- **Words** “Very lucky year to be born. It's like being born in 2000, like my brother. Where very easy to calculate how old you are. But uh yeah.”  **Why** 'very lucky year … like being born in 2000 … easy to calculate how old you are' → 1900 rolls to 2000 on an odometer; a pen tick for 'easy'.
- **FX** #13 odometer + #19 pen · **Ref** Pinterest idea: 'slot-machine year counter on graph paper'
- **Visual** Graph paper card; 1900 → 2000 odometer; pen tick on 'easy'.
- **Assets** E95 (see ASSETS_NEEDED)
- **Text** `lucky year` `lucky`@287.59 `year`@287.91 · `2000`@289.51 · `easy`@292.07
- **Camera** static. **Out** `PS` @296.47.
- **SFX** 287.6 tick_soft · 289.5 odometer_tick · 292.0 pencil_scribble

### C1S051 · 296.47–299.83 · C1B053 · NIGHT
- **Words** “He he he's from a very successful family.”  **Why** 'he's from a very successful family' → Terman family portrait plate.
- **FX** #16 plate · **Ref** —
- **Visual** Terman family / Lewis Terman with son photo (R06 search), fringe blur, dust.
- **Assets** R06 (see ASSETS_NEEDED)
- **Text** `successful family` `successful`@298.55 `family`@299.27
- **Camera** slow push. **Out** `CA` @299.83.
- **SFX** 296.5 air_swell

### C1S052 · 299.83–303.59 · C1B054 · PAPER
- **Words** “His father, **Lewis** Terman, was a s a Stanford psychologist”  **Why** 'his father, Lewis Terman … a Stanford psychologist' → Lewis Terman card with label.
- **FX** #12 collage + label box · **Ref** —
- **Visual** Lewis Terman card (R06) halftone on paper, label box.
- **Assets** R06 (see ASSETS_NEEDED)
- **Text** `his father` `his`@299.83 `father`@300.07 · `LEWIS TERMAN` `Lewis`@300.39 `Terman`@300.79 · `Stanford psychologist` `Stanford`@301.99 `psychologist`@302.55
- **Camera** push into the card's book. **Out** `PT` @303.59.
- **SFX** 299.8 paper_slide · 300.35 pop_soft

### C1S053 · 303.59–306.07 · C1B055 · PAPER
- **Words** “who actually invented the IQ test”  **Why** 'who actually invented the IQ test' → the 1916 book and its IQ tables.
- **FX** #5 document + #18 highlighter · **Ref** old SC050
- **Visual** Measurement of Intelligence title page (R41) → page turn to the IQ classification table, highlighter on a body line.
- **Assets** R41 (see ASSETS_NEEDED)
- **Text** `invented`@304.39 · `IQ test` `IQ`@305.11 `test`@305.75
- **Camera** 3D tilt, push. **Out** `CRT` @306.07.
- **SFX** 303.6 page_turn · 305.1 highlighter_swipe

### C1S054 · 306.07–308.71 · C1B055 · NIGHT
- **Words** “that you have ha you and I have probably taken.”  **Why** 'that you and I have probably taken' → a classroom taking a test, on a 1950s TV.
- **FX** #11 TV (1950s set) · **Ref** §10.1.7 — new 1950s set (N69), not the museum TVs
- **Visual** Classroom-test footage (E81) inside the keyed TV (N69), CRT power-on.
- **Assets** E81, N69 (see ASSETS_NEEDED)
- **Text** `you and I` `you`@306.95 `and`@307.11 `I`@307.19
- **Camera** slow push to screen. **Out** `W→` @308.71.
- **SFX** 306.0 crt_click · 306.1 crt_hum (dur 2.5) · 308.6 whoosh

### C1S055 · 308.71–313.19 · C1B056 · PAPER
- **Words** “So yeah, he was a very, very powerful, powerful company.”  **Why** 'a very, very powerful, powerful [family]' → father and son circles joined, D15-style.
- **FX** #2 diagram · **Ref** D15 variant (two-node family diagram; double ring)
- **Visual** Lewis (R06) and Fred (R01) portrait circles, pen arrow between, small family crest-like frame.
- **Assets** R06, R01 (see ASSETS_NEEDED)
- **Text** `very powerful` `very`@310.95 `powerful`@311.27
- **Camera** static. **Out** `CA` @313.19.
- **SFX** 309.0 pop_soft ×2 · 311.2 marker_scratch

### C1S056 · 313.19–318.79 · C1B057 · NIGHT · 2.5D #2
- **Words** “By 24 years old, **Terman** had gotten his undergrad degree in Stanford,”  **Why** 'by 24 … undergrad degree in Stanford' → 1920 Stanford group photo in depth, young Terman picked out.
- **FX** #17 2.5D + #13 count · **Ref** 2.5D-campus variant (approved SC047 look)
- **Visual** Theta Xi 1920 group (R01) cut into layers; dolly; ring call-out on Terman.
- **Assets** R01 (see ASSETS_NEEDED)
- **Text** `24`@313.43 (count) · `undergrad degree` `undergrad`@316.07 `degree`@316.71 · `Stanford`@317.91 (vermilion tag)
- **Camera** dolly, FH at stop. **Out** `FW` (planner rhythm fix — editor may pick another non-repeating type) @318.79.
- **SFX** 313.4 counter_ticks · 316.0 air_swell · 318.73 whoosh (transition)

### C1S057 · 318.79–325.43 · C1B058 · PAPER
- **Words** “went to East to get his doctorate, graduate degree, and MIT, came back to Stanford to teach radio engineering.”  **Why** 'went to East … doctorate … MIT, came back to Stanford to teach radio engineering' → route there and back on the railroad map; his Radio Engineering book lands.
- **FX** #3 map + #20 + #19 marker · **Ref** R10 variant (route there-and-back, pins ①MIT ②Stanford)
- **Visual** Rand McNally map (E91) wider crop; yellow marker to Boston (navy MIT pin), returns; book cover (N44) slides in on 'radio engineering'.
- **Assets** E91, N44 (see ASSETS_NEEDED)
- **Text** `East`@319.35 · `doctorate`@320.07 · `MIT`@321.83 · `came back` `came`@322.47 `back`@322.71 · `radio engineering` `radio`@324.07 `engineering`@324.55
- **Camera** track. **Out** `CA` @325.43.
- **SFX** 319.3 marker_long · 321.8 map_pin · 322.5 marker_long · 324.0 paper_slide

### C1S058 · 325.43–332.15 · C1B059 · GRID
- **Words** “And in the first ten years of his teaching career, he's seeing something that's just breaking his heart.”  **Why** 'first ten years of his teaching career … breaking his heart' → a line chart with a ten-year band; the 'staying West' line falls and cracks.
- **FX** #2 line chart · **Ref** D05/R7 variant (era band = his first ten years; shapes only)
- **Visual** Grid card; band shades; line draws and falls; a crack splits it on 'heart'.
- **Assets** E95 (see ASSETS_NEEDED)
- **Text** `first ten years` `first`@325.99 `ten`@326.31 `years`@326.71 · `teaching career` `teaching`@327.59 `career`@328.23 · `breaking his heart` `breaking`@330.87 `his`@331.43 `heart`@331.59
- **Camera** drift. **Out** `W→` @332.15.
- **SFX** 326.0 dot_slide · 330.8 paper_tear

### C1S059 · 332.15–338.47 · C1B060 · NIGHT
- **Words** “And it's the same thing that **Hoover** saw when he was at the head, by the way, who are very quickly becomes the president, and then we”  **Why** 'the same thing that Hoover saw … very quickly becomes the president' → Hoover's 1929 inauguration.
- **FX** #14 weave + #1 · **Ref** —
- **Visual** Inauguration photo/newsreel (N20).
- **Assets** N20 (see ASSETS_NEEDED)
- **Text** `Hoover`@333.11 · `president`@337.35
- **Camera** slow push. **Out** `CA` @338.47.
- **SFX** 332.2 projector_loop (dur 6.3)

### C1S060 · 338.47–344.84 · C1B061 · NIGHT
- **Words** “have the Great Depression where people. blame on Herbert Hoover for some reason, but nonetheless, that's a different topic.”  **Why** 'the Great Depression where people blame Herbert Hoover … different topic' → Hooverville / breadline photos whip-chained, the last one tossed aside.
- **FX** #16 + whips · **Ref** —
- **Visual** 2–3 Depression photos (N21), whip between; on 'different topic' the photo is flicked out of frame.
- **Assets** N21 (see ASSETS_NEEDED)
- **Text** `Great Depression` `Great`@338.95 `Depression`@339.35 (hero halate) · `blame`@341.00
- **Camera** pushes. **Out** `PS` @344.84.
- **SFX** 339.0 boom_low · 340.9 whoosh · 343.7 paper_slide

### C1S061 · 344.84–349.40 · C1B062 · PAPER
- **Words** “But Terman is saying the same thing for the first ten years and it's breaking his heart.”  **Why** 'Terman … the same thing for the first ten years … breaking his heart' → Terman card with ten pen tallies.
- **FX** #19 pen + #12 card · **Ref** —
- **Visual** Terman card (R01) on paper; ten tally marks drawn one by one.
- **Assets** R01 (see ASSETS_NEEDED)
- **Text** `Terman`@345.32 · `ten years` `ten`@347.48 `years`@347.72
- **Camera** static. **Out** `CA` @349.40.
- **SFX** 345.3 pop_soft · 347.4 pencil_scribble ×10

### C1S062 · 349.40–357.32 · C1B063 · PAPER
- **Words** “His best students are graduating and leaving this area going back east, you know? And he wanted that to stop.”  **Why** 'his best students are graduating and leaving … going back east … he wanted that to stop' → graduate icons walk east; a STOP bar slams down.
- **FX** #2 isotype + #18 stamp · **Ref** R5 variant (row of graduates; the best turn vermilion and walk right)
- **Visual** Row of graduate icons; best ones vermilion walk off right; a rough STOP bar drops on 'stop'.
- **Text** `best students` `best`@349.72 `students`@350.20 · `leaving`@352.28 · `back east` `back`@353.72 `east`@353.96 · `STOP`@356.68
- **Camera** drift right. **Out** `W↑` @357.32.
- **SFX** 349.7 pop_soft · 352.2 dot_slide · 356.6 stamp_thud

## 6. Act VI — Hewlett & Packard and Terman's plan (357.32–436.03)
Music: momentum layer enters on 'Bill' 378.28; hit on 'HP' 384.20; build under the plan.

### C1S063 · 357.32–361.72 · C1B064 · NIGHT
- **Words** “So by nineteen thirty eight, we're almost twelve years ahead in our story,”  **Why** 'by 1938 … twelve years ahead in our story' → 1938 title.
- **FX** #4 hero + #8 streaks + #13 odometer · **Ref** s01 look
- **Visual** Streaks; 1938 odometer, small label.
- **Text** `1938`@357.88 (hero halate) · `twelve years ahead` `twelve`@359.64 `years`@360.12 `ahead`@360.44 (t-label)
- **Camera** push. **Out** `CA` @361.72.
- **SFX** 357.8 odometer_tick · 357.9 air_swell

### C1S064 · 361.72–369.96 · C1B065 · NIGHT
- **Words** “he finds two students that are just so good that he wasn't willing to get them go to East. That's how much he liked them.”  **Why** 'he finds two students … so good … wasn't willing to let them go to East' → two silhouettes in layered panels; an eastward arrow blocked.
- **FX** #10 Vox layered (s09) · **Ref** s09 (approved) part 1
- **Visual** Two silhouette cards (N05) over tinted Stanford panels; rough arrow East hits a pen bar.
- **Assets** N05, E10 (see ASSETS_NEEDED)
- **Text** `two students` `two`@362.36 `students`@362.68 · `so good` `so`@364.28 `good`@364.60 · `East`@367.96
- **Camera** drift. **Out** `cont` @369.96.
- **SFX** 362.3 paper_slide ×2 · 367.9 marker_scratch

### C1S065 · 369.96–377.16 · C1B066 · PAPER
- **Words** “And you might have heard their names, especially if you're in the tech industry, especially if you're I think I'm watching a story about Silicon Valley.”  **Why** 'you might have heard their names … tech industry … a story about Silicon Valley' → two blank name tags waiting to be filled.
- **FX** #13 typewriter (blank) · **Ref** —
- **Visual** Paper: two 1930s name tags, blank; small tag 'Silicon Valley'.
- **Text** `their names` `their`@370.84 `names`@371.00 · `tech industry` `tech`@372.36 `industry`@372.68 · `Silicon Valley` `Silicon`@376.12 `Valley`@376.68
- **Camera** static. **Out** `CA` @377.16.
- **SFX** 370.8 paper_slide · 376.1 tick_soft

### C1S066 · 377.16–381.08 · C1B067 · NIGHT
- **Words** “The students' name were Bill Hewlett and David Packard.”  **Why** 'Bill Hewlett and David Packard' → the approved reveal: silhouettes become the two men.
- **FX** #10 Vox cut-out (s09) · **Ref** s09 (approved) part 2
- **Visual** Silhouettes reveal Hewlett (E07/N03) and Packard.
- **Assets** E07, N03 (see ASSETS_NEEDED)
- **Text** `BILL HEWLETT` `Bill`@378.28 `Hewlett`@378.60 · `DAVID PACKARD` `David`@379.48 `Packard`@379.96
- **Camera** drift. **Out** `MC` @381.08.
- **SFX** 378.2 pop_soft · 379.4 pop_soft

### C1S067 · 381.08–385.64 · C1B068 · PAPER
- **Words** “Two people who go on to found the famous company HP.”  **Why** 'go on to found the famous company HP' → HP logo builds.
- **FX** #13 random letters + logo · **Ref** —
- **Visual** HP logo (N62) built from the two name tags merging.
- **Assets** N62 (see ASSETS_NEEDED)
- **Text** `found`@382.60 · `famous company` `famous`@383.16 `company`@383.64 · `HP`@384.20
- **Camera** static. **Out** `W→` @385.64.
- **SFX** 384.2 chime_soft · 385.5 whoosh

### C1S068 · 385.64–390.52 · C1B069 · NIGHT
- **Words** “Now, by this time Packard was already gone. He was working at General Electric,”  **Why** 'Packard was already gone … working at General Electric' → GE Schenectady 1930s plate with logo.
- **FX** #16 plate · **Ref** —
- **Visual** GE 1930s plate (N16/R16) + GE logo; Packard card (E07) slides in.
- **Assets** N16, R16, E07, E16 (see ASSETS_NEEDED)
- **Text** `Packard`@386.92 · `already gone` `already`@387.80 `gone`@388.12 · `General Electric` `General`@389.24 `Electric`@389.72
- **Camera** push. **Out** `CA` @390.52.
- **SFX** 386.9 paper_slide

### C1S069 · 390.52–395.56 · C1B070 · PAPER
- **Words** “making around hundred dollars a month, and Hewlett was planning on going,”  **Why** 'making around hundred dollars a month, and Hewlett was planning on going' → a pay envelope with $100, then Hewlett's card with a ticket east.
- **FX** #12 collage + #13 count · **Ref** —
- **Visual** Pay envelope halftone (N50) with the count; Hewlett card + rail ticket (old ticket recreation).
- **Assets** N50, E07 (see ASSETS_NEEDED)
- **Text** `$100 a month` `hundred`@391.16 (yellow key number, count) `dollars`@391.56 `a`@391.96 `month`@392.20 · `Hewlett`@393.24 · `going`@395.08
- **Camera** drift. **Out** `PS` @395.56.
- **SFX** 391.1 counter_ticks · 393.2 paper_slide

### C1S070 · 395.56–402.83 · C1B071–72 · NIGHT
- **Words** “and this is when Terman comes up with a plan. Where the plan is basically to convince these two people to start some kind of company.”  **Why** 'Terman comes up with a plan … convince these two … start some kind of company' → a lamp-lit cork board: strings from two photos to a blank company card.
- **FX** #12 + #19 strings · **Ref** R9 variant (smaller board, 3 items, string forms a triangle)
- **Visual** Cork (E96) under lamp; Terman card, two student cards; red string drawn to an empty card '?'.
- **Assets** E96, R01, E07 (see ASSETS_NEEDED)
- **Text** `Terman`@396.28 · `plan`@397.88 · `convince`@399.95 · `start`@401.39 · `company`@402.35
- **Camera** slow push. **Out** `CA` @402.83.
- **SFX** 395.6 lamp_click · 399.9 marker_long (string)

### C1S071 · 402.83–408.27 · C1B073 · PAPER
- **Words** “Any company just started here here in California, started in Palo Alto.”  **Why** 'any company … here in California, started in Palo Alto' → the pictorial Peninsula map, a pin on Palo Alto.
- **FX** #3 map + #20 · **Ref** D09 variant (old city map → pictorial colour map, pin + circle)
- **Visual** Pictorial map (E33) tilted, push to Palo Alto, pen circle.
- **Assets** E33 (see ASSETS_NEEDED)
- **Text** `California`@405.39 · `Palo Alto` `Palo`@406.91 `Alto`@407.47
- **Camera** push. **Out** `PT` @408.27.
- **SFX** 405.3 paper_slide · 406.9 map_pin · 407.4 marker_scratch

### C1S072 · 408.27–414.51 · C1B074 · GRID
- **Words** “And the idea for this company was actually something that Hewlett himself had done his thesis on.”  **Why** 'the idea … something that Hewlett himself had done his thesis on' → his thesis title page.
- **FX** #5 document + §10.6.4 · **Ref** old SC087
- **Visual** Thesis title recreation (R43) on grid desk, text call-out on the title.
- **Assets** R43, E95 (see ASSETS_NEEDED)
- **Text** `idea`@408.99 · `Hewlett`@411.23 · `thesis`@413.39
- **Camera** 3D tilt push. **Out** `CA` @414.51.
- **SFX** 408.3 paper_slide · 413.3 tick_soft

### C1S073 · 414.51–418.75 · C1B075 · NIGHT
- **Words** “And this was something an audio oscillator. Okay? That was the idea.”  **Why** 'an audio oscillator. That was the idea.' → the HP 200A itself.
- **FX** #16 hero plate + #19 call-outs · **Ref** old SC088
- **Visual** 200A photo (N60/E60), fringe blur; pen call-out arrow to the dial.
- **Assets** N60, E60 (see ASSETS_NEEDED)
- **Text** `AUDIO OSCILLATOR` `audio`@416.27 `oscillator`@416.75 (hero halate) · `the idea` `the`@418.03 `idea`@418.19
- **Camera** slow push. **Out** `W↓` @418.75.
- **SFX** 416.2 air_swell · 418.6 whoosh

### C1S074 · 418.75–428.59 · C1B076–77 · PAPER
- **Words** “And on top of that, Terman somehow figured out a fellowship for them where they got some money, some money, some money, some money from this fellowship to start this company.”  **Why** 'Terman figured out a fellowship … some money, some money, some money … to start this company' → fellowship letter + a coin stack per 'some money'.
- **FX** #12 collage + #13 · **Ref** —
- **Visual** Fellowship letter (R43) pinned; halftone coins (N61) stack one per 'some money' (423.63, 424.43, 425.31, 426.19).
- **Assets** R43, N61 (see ASSETS_NEEDED)
- **Text** `Terman`@419.87 · `fellowship`@421.95 · `some money` `some`@423.63 `money`@423.87 (once) · `start this company` `start`@427.79 `this`@428.11 `company`@428.27
- **Camera** static. **Out** `CA` @428.59.
- **SFX** 421.9 paper_slide · 423.6 pop_soft ×4 (coins)

### C1S075 · 428.59–436.03 · C1B078 · NIGHT
- **Words** “And on top of that, he put his own money, he gave his own money to his students so they can, you know, get the funding they need.”  **Why** 'he gave his own money to his students … funding they need' → Terman's cash passes to the two cards.
- **FX** #10 Vox layered · **Ref** —
- **Visual** Tinted 1930s banknote engravings (N50) drifting; Terman cut-out hands a note across to the two student cards.
- **Assets** N50, R01, E07 (see ASSETS_NEEDED)
- **Text** `his own money` `his`@430.11 `own`@430.35 `money`@430.67 · `students`@432.67 · `funding`@434.43
- **Camera** drift. **Out** `W↓` (planner rhythm fix — editor may pick another non-repeating type) @436.03.
- **SFX** 430.1 paper_slide · 434.4 tick_soft · 435.97 whoosh (transition)

## 7. Act VII — HP is born: Disney, the coin flip, the garage, the oscillator (436.03–516.54)
Music: playful pizz/marimba-like layer for the coin flip; warm swell on 'garage' 478.14; light ticking texture under the oscillator explanation.

### C1S076 · 436.03–438.91 · C1B079 · GRID
- **Words** “He told them to build this oscillator thing.”  **Why** 'he told them to build this oscillator thing' → Hewlett's patent drawing draws itself on blueprint paper.
- **FX** #19 pen trace + #5 · **Ref** —
- **Visual** Patent drawing sheet (N45) on paper_blueprint_01_hires; lines trace on.
- **Assets** N45, E95 (see ASSETS_NEEDED)
- **Text** `build`@437.15 · `oscillator`@437.79
- **Camera** push. **Out** `CA` @438.91.
- **SFX** 437.1 pencil_scribble (dur 1.5)

### C1S077 · 438.91–443.47 · C1B079 · NIGHT
- **Words** “He gave them a list of 25 companies that might actually buy it.”  **Why** 'a list of 25 companies that might actually buy it' → a dark blurred list of 25 rows, focus pull.
- **FX** #13 count + rack focus · **Ref** D12 variant (blurred rows, focus pull; rows unnamed — never invented)
- **Visual** 25 ruled rows with ink scribbles (no readable names) in bone, blurred; counter 25 yellow.
- **Text** `list`@439.63 · `25`@440.03 (yellow count) · `companies`@440.75 · `buy it` `buy`@442.59 `it`@443.07
- **Camera** focus pull. **Out** `PT` (planner rhythm fix — editor may pick another non-repeating type) @443.47.
- **SFX** 440.0 counter_ticks · 442.5 tick_soft

### C1S078 · 443.47–449.39 · C1B080 · PAPER
- **Words** “And then on top of that, on top of that, he actually pulled his connections to”  **Why** 'on top of that … he pulled his connections' → a relationship diagram: Terman hub, pen spokes to blank nodes.
- **FX** #2 diagram + #19 · **Ref** D15 variant (hub-and-spoke, blank nodes)
- **Visual** Terman circle centre; pen lines draw to 6 blank circles.
- **Assets** R01 (see ASSETS_NEEDED)
- **Text** `connections`@447.71
- **Camera** static. **Out** `W←` @449.39.
- **SFX** 447.7 marker_long

### C1S079 · 449.39–455.95 · C1B081 · NIGHT
- **Words** “basically find the first buyers for this product that they are producing, which is gonna be Disney, by the way.”  **Why** 'find the first buyers … which is gonna be Disney' → Disney's Fantasia-era poster / studio.
- **FX** #16 poster B-roll · **Ref** §10.5 posters as B-roll
- **Visual** Fantasia 1940 poster (N36), fringe blur, slow push.
- **Assets** N36 (see ASSETS_NEEDED)
- **Text** `first buyers` `first`@450.67 `buyers`@450.99 · `DISNEY`@454.75 (hero halate)
- **Camera** push. **Out** `CA` @455.95.
- **SFX** 454.7 chime_soft

### C1S080 · 455.95–462.78 · C1B082 · NIGHT
- **Words** “And the company name is apparently gonna be. Uh decided by a coin flip. So it's the name is decided.”  **Why** 'the company name … decided by a coin flip' → a 1930s coin flips in slow motion.
- **FX** 3D coin (CSS rotateX 12 fps) + #8 · **Ref** —
- **Visual** Coin (N61) obverse/reverse flipping in light.
- **Assets** N61 (see ASSETS_NEEDED)
- **Text** `company name` `company`@456.27 `name`@456.67 · `coin flip` `coin`@460.38 `flip`@460.70 · `decided`@462.30
- **Camera** track coin. **Out** `W→` (planner rhythm fix — editor may pick another non-repeating type) @462.78.
- **SFX** 460.3 tick_soft + whoosh_soft (coin) · 462.72 whoosh (transition)

### C1S081 · 462.78–468.78 · C1B083 · PAPER
- **Words** “It's gonna be the last name of Bill Hewlett and David Packard. They're gonna combine the **last** *(ASR “NAS”)* name, but which one goes first?”  **Why** 'the last name of Bill Hewlett and David Packard … which one goes first?' → two surname blocks swap places.
- **FX** #13 odometer swap · **Ref** —
- **Visual** HEWLETT / PACKARD letterpress blocks swap order.
- **Text** `last name` `last`@463.42 `name`@463.66 · `Hewlett`@464.22 · `Packard`@465.42 · `which one goes first?` `which`@467.50 `one`@467.74 `goes`@467.98 `first`@468.22
- **Camera** static. **Out** `MC` @468.78.
- **SFX** 466.4 paper_slide ×2

### C1S082 · 468.78–476.22 · C1B084 · NIGHT
- **Words** “Well, they just flipped a coin, and that's why we have HP computers, HP printers, anything else you can think of. Everything HP.”  **Why** 'they flipped a coin … HP computers, HP printers … everything HP' → coin lands, then modern HP products in layered panels.
- **FX** #10 Vox layered + #13 · **Ref** —
- **Visual** Coin lands showing the result; panels: HP laptop (N62), HP printer; HP logo.
- **Assets** N61, N62 (see ASSETS_NEEDED)
- **Text** `flipped a coin` `flipped`@469.66 `coin`@470.14 · `HP computers` `HP`@471.42 `computers`@471.90 · `HP printers` `HP`@472.46 `printers`@472.94 · `Everything HP` `Everything`@474.86 `HP`@475.50
- **Camera** drift. **Out** `FW` @476.22.
- **SFX** 469.6 tick_soft · 471.4 paper_slide · 472.4 paper_slide · 476.1 whoosh_big

### C1S083 · 476.22–483.02 · C1B085 · NIGHT · 2.5D #3
- **Words** “And this started in a garage. Like everything in Silicon Valley, the first company”  **Why** 'this started in a garage … the first company in Silicon Valley' → the approved 2.5D garage.
- **FX** #17 2.5D · **Ref** s10 (approved)
- **Visual** Garage layers (E19), dolly, title behind hedge.
- **Assets** E19 (see ASSETS_NEEDED)
- **Text** `garage`@478.14 (hero halate) · `first company` `first`@482.06 `company`@482.46
- **Camera** dolly. **Out** `cont` @483.02.
- **SFX** 476.3 air_swell

### C1S084 · 483.02–488.62 · C1B086 · NIGHT
- **Words** “in Silicon Valley, which again, we don't have Silicon Valley yet, but it started in the garage.”  **Why** 'we don't have Silicon Valley yet, but it started in the garage' → over the garage, SILICON VALLEY with 'yet' struck.
- **FX** #4 + #19 pen strike · **Ref** —
- **Visual** Garage world continues (slower dolly), title card SILICON VALLEY; pen strike + `not yet`.
- **Assets** E19 (see ASSETS_NEEDED)
- **Text** `Silicon Valley` `Silicon`@485.02 `Valley`@485.58 · `yet`@485.90 (pen strike)
- **Camera** dolly. **Out** `PS` @488.62.
- **SFX** 485.9 marker_scratch

### C1S085 · 488.62–493.18 · C1B087 · PAPER
- **Words** “Disney was the first client. An audio oscillator, let me explain a little bit what it is.”  **Why** 'Disney was the first client. An audio oscillator …' → Disney card and the 200A card side by side.
- **FX** #12 collage · **Ref** —
- **Visual** Fantasia card (N36) + 200A card (E60) joined by an arrow.
- **Assets** N36, E60 (see ASSETS_NEEDED)
- **Text** `Disney`@488.62 · `first client` `first`@489.42 `client`@489.66 · `audio oscillator` `audio`@490.22 `oscillator`@490.62
- **Camera** push into the 200A dial. **Out** `PT` @493.18.
- **SFX** 488.6 paper_slide · 490.2 pin_pop

### C1S086 · 493.18–496.78 · C1B088 · NIGHT
- **Words** “It creates different levels of sound that you can control.”  **Why** 'it creates different levels of sound that you can control' → a scope screen whose waveform changes as the dial turns.
- **FX** #11 screen (oscilloscope) · **Ref** §10.1.7 — 1940s oscilloscope (N68)
- **Visual** Scope (N68; fallback Tektronix) with an SVG sine changing frequency/amplitude.
- **Assets** N68 (see ASSETS_NEEDED)
- **Text** `different levels of sound` `different`@493.90 `levels`@494.30 · `control`@496.30
- **Camera** slow push. **Out** `CA` @496.78.
- **SFX** 493.2 crt_click · 493.3 crt_hum (dur 3.4) · 494.3 tone_blip

### C1S087 · 496.78–505.10 · C1B089–90 · PAPER
- **Words** “Like you can create a specific level of sound, and then if you're someone who's building sound equipment, you can test if your sound equipment is catching that sound or not.”  **Why** 'a specific level of sound … building sound equipment … test if your equipment is catching that sound' → oscillator → speaker → meter, checked.
- **FX** #2 diagram + #19 · **Ref** Pinterest idea: 'patent-style signal-flow diagram'
- **Visual** Oscillator icon → ink signal line → radio-cabinet halftone (N64) → meter needle; ✓ on 'catching'.
- **Assets** N64, E60 (see ASSETS_NEEDED)
- **Text** `specific level` `specific`@497.58 `level`@497.98 · `sound equipment` `sound`@500.22 `equipment`@500.62 · `test`@501.42 · `catching`@503.58
- **Camera** drift. **Out** `W→` @505.10.
- **SFX** 497.5 dot_slide · 501.4 tick_soft · 503.5 marker_scratch

### C1S088 · 505.10–511.90 · C1B091 · GRID
- **Words** “So it was it was basically like a B2B company where they would sell this testing equipment”  **Why** 'basically like a B2B company … sell this testing equipment' → B → B diagram and a real HP catalogue page.
- **FX** #5 document + #2 · **Ref** —
- **Visual** Two factory icons B→B on grid; HP catalogue page (N46) slides in.
- **Assets** N46, E95 (see ASSETS_NEEDED)
- **Text** `B2B`@507.18 · `testing equipment` `testing`@510.70 `equipment`@511.26
- **Camera** push. **Out** `CA` @511.90.
- **SFX** 507.1 pop_soft · 510.6 paper_slide

### C1S089 · 511.90–516.54 · C1B092 · NIGHT
- **Words** “to other people who are creating test uh sound products.”  **Why** 'to other people who are creating … sound products' → 1940 radio factory testers in headphones.
- **FX** #14 weave + #1 · **Ref** old SC090
- **Visual** Radio factory footage (E82).
- **Assets** E82 (see ASSETS_NEEDED)
- **Text** `sound products` `sound`@515.10 `products`@515.74
- **Camera** —. **Out** `FW` @516.54.
- **SFX** 511.9 projector_loop (dur 4.6) · 516.4 whoosh_big

## 8. Act VIII — World War II and federal money (516.54–591.62)
Music: cut to low drone + pulse on 'the war' 519.10; dark pulses under the secret lab; release on 'Dean' 550.57; triumphant build into 'federal money' 586.90.

### C1S090 · 516.54–522.97 · C1B093 · PAPER
- **Words** “Now as soon as things are just getting going, the war interrupts everything. World War **II.**”  **Why** 'the war interrupts everything. World War II.' → a real wartime front page.
- **FX** #5 newspaper · **Ref** s06 variant (different paper, flat-lay instead of tilt)
- **Visual** WWII front page (N48), contrast call-out on the headline area.
- **Assets** N48 (see ASSETS_NEEDED)
- **Text** `the war` `the`@519.10 `war`@519.34 · `interrupts everything` `interrupts`@519.82 `everything`@520.62 · `World War II` `World`@521.61 `War`@522.09 `II`@522.41
- **Camera** push. **Out** `CA` @522.97.
- **SFX** 516.6 paper_rustle · 519.3 boom_low

### C1S091 · 522.97–528.97 · C1B094 · NIGHT
- **Words** “**Terman** is one of the foremost minds when it comes to radio stuff.”  **Why** 'Terman is one of the foremost minds … radio' → Terman 1940s + radio valves layered.
- **FX** #10 Vox layered · **Ref** —
- **Visual** Terman 1940s (N02) cut-out over tinted tube photos (N65).
- **Assets** N02, N65 (see ASSETS_NEEDED)
- **Text** `Terman`@522.97 · `foremost minds` `foremost`@524.65 `minds`@525.45 · `radio`@527.37
- **Camera** drift. **Out** `W→` @528.97.
- **SFX** 523.0 paper_slide · 528.9 whoosh

### C1S092 · 528.97–532.17 · C1B095 · PAPER
- **Words** “So he's tapped by the military to run a secret lab”  **Why** 'he's tapped by the military to run a secret lab' → a wartime telegram (his words), SECRET stamp.
- **FX** #13 typewriter + #18 stamp · **Ref** D08 variant (telegram — wartime Western Union ground)
- **Visual** Telegram (N52) typed word by word; SECRET stamp.
- **Assets** N52 (see ASSETS_NEEDED)
- **Text** `tapped`@529.69 · `military`@530.49 · `secret lab` `secret`@531.45 `lab`@531.77 (stamp)
- **Camera** static. **Out** `CA` @532.17.
- **SFX** 529.6 letter_ticks (typing) · 531.4 stamp_thud

### C1S093 · 532.17–534.81 · C1B095 · GRID
- **Words** “of about 800 people in Harvard.”  **Why** 'about 800 people in Harvard' → an isotype grid filling to 800, Harvard tag.
- **FX** #2 isotype + #13 count · **Ref** D03 variant (person pictograms, 1 icon = 10 people, legend)
- **Visual** 80 person icons fill at 12 fps; navy Harvard tag.
- **Assets** N22 (see ASSETS_NEEDED)
- **Text** `800`@532.57 (yellow count) · `people`@533.21 · `Harvard`@533.69 (navy tag)
- **Camera** static. **Out** `HC` (planner rhythm fix — editor may pick another non-repeating type) @534.81.
- **SFX** 532.5 dot_ticks (dur 1)

### C1S094 · 534.81–541.21 · C1B096 · NIGHT
- **Words** “And the job of this team is basically to figure out how the United States can fool enemy radars.”  **Why** 'figure out how the United States can fool enemy radars' → WWII radar antenna + PPI scope.
- **FX** #11 screen (radar PPI) + #1 · **Ref** §10.1.7 — radar scope (N66)
- **Visual** Radar footage (N84) → PPI scope screen sweeping (N66).
- **Assets** N84, N66 (see ASSETS_NEEDED)
- **Text** `United States` `United`@538.57 `States`@539.05 · `fool`@539.53 · `enemy radars` `enemy`@540.01 `radars`@540.41
- **Camera** push to scope. **Out** `CA` @541.21.
- **SFX** 534.8 crt_hum (dur 6) · 539.5 tone_blip

### C1S095 · 541.21–544.57 · C1B097 · NIGHT
- **Words** “Jam it, hide from it, whatever you want to do, right?”  **Why** 'jam it, hide from it' → the scope fills with jamming noise; chaff clouds fall from bombers.
- **FX** #1 + #8 noise · **Ref** —
- **Visual** Jamming noise on the scope; whip to chaff photo (N67).
- **Assets** N66, N67 (see ASSETS_NEEDED)
- **Text** `jam it` `jam`@541.21 `it`@541.69 · `hide from it` `hide`@542.01 `from`@542.49 `it`@542.81
- **Camera** shake. **Out** `W↑` @544.57.
- **SFX** 541.2 tone_blip (jamming) · 544.5 whoosh

### C1S096 · 544.57–548.09 · C1B098 · PAPER
- **Words** “So he does this work all throughout, all throughout World War II.”  **Why** 'all throughout World War II' → a bracket spans the war on a timeline, a dot travels the length.
- **FX** #12 timeline · **Ref** old s08 timeline
- **Visual** Timeline axis, bracket labelled.
- **Text** `all throughout` `all`@545.85 `throughout`@546.09 · `World War II` `World`@547.29 `War`@547.53 `II`@547.77
- **Camera** track. **Out** `CA` @548.09.
- **SFX** 545.8 dot_slide (dur 2)

### C1S097 · 548.09–552.17 · C1B099 · NIGHT
- **Words** “By the end of it, he comes back to Stanford as Dean of Engineering.”  **Why** 'comes back to Stanford as Dean of Engineering' → Stanford 1940s plate, brass nameplate.
- **FX** #16 + nameplate · **Ref** —
- **Visual** Stanford Quad 1940s (R11) + Terman (N02).
- **Assets** R11, N02 (see ASSETS_NEEDED)
- **Text** `Stanford`@549.77 · `Dean of Engineering` `Dean`@550.57 `of`@550.97 `Engineering`@551.21
- **Camera** push. **Out** `W←` (planner rhythm fix — editor may pick another non-repeating type) @552.17.
- **SFX** 550.5 tick_soft · 552.11 whoosh (transition)

### C1S098 · 552.17–557.61 · C1B100 · NIGHT
- **Words** “Importantly, though, he has built a lot of connections in Washington because of everything he has done,”  **Why** 'a lot of connections in Washington' → 1940s Capitol aerial, pen lines connecting Terman to it.
- **FX** #19 markups on photo · **Ref** s11 (approved markups) variant
- **Visual** Capitol/Washington photo (N23) with pen lines + nodes.
- **Assets** N23, N02 (see ASSETS_NEEDED)
- **Text** `connections`@554.49 · `Washington`@555.45
- **Camera** push. **Out** `PS` @557.61.
- **SFX** 554.4 marker_long · 557.5 paper_slide

### C1S099 · 557.61–564.49 · C1B101 · PAPER
- **Words** “and those connections are gonna pay very handsomely, and I mean that literally, they're gonna pay very handsomely.”  **Why** 'those connections are gonna pay very handsomely … literally' → a Treasury cheque, money pouring.
- **FX** #18 + #13 · **Ref** —
- **Visual** Cheque/banknote halftones (N50) cascade; highlighter on memo line.
- **Assets** N50 (see ASSETS_NEEDED)
- **Text** `pay`@559.29 · `very handsomely` `very`@559.77 `handsomely`@560.01 · `literally`@561.93
- **Camera** static. **Out** `CA` @564.49.
- **SFX** 559.2 paper_slide · 561.9 highlighter_swipe

### C1S100 · 564.49–570.41 · C1B102 · NIGHT
- **Words** “So he's like he convinces the military. Did they have Pentagon back then? I don't know if they did,”  **Why** 'he convinces the military. Did they have Pentagon back then?' → the Pentagon aerial with a hand-drawn ?.
- **FX** #16 + #19 · **Ref** —
- **Visual** Pentagon aerial (N24), pen '?' beside it (no date).
- **Assets** N24 (see ASSETS_NEEDED)
- **Text** `convinces`@566.25 · `military`@567.05 · `Pentagon`@568.65
- **Camera** push. **Out** `W→` @570.41.
- **SFX** 568.6 marker_scratch · 570.3 whoosh

### C1S101 · 570.41–578.25 · C1B103 · PAPER
- **Words** “but he convinces the military to basically set up research labs, but let's do it in Stanford, you know? Let's do it out west.”  **Why** 'set up research labs … in Stanford … out west' → map: arrow from Washington to Stanford, labs pinned.
- **FX** #3 map + #20 · **Ref** R11 variant (map kit relief, labelled route)
- **Visual** US relief (N93) with a pen route East→West.
- **Assets** N93 (see ASSETS_NEEDED)
- **Text** `research labs` `research`@572.89 `labs`@573.37 · `Stanford`@575.77 · `out west` `out`@577.37 `west`@577.53
- **Camera** track west. **Out** `CA` @578.25.
- **SFX** 572.8 map_pin · 575.7 marker_long

### C1S102 · 578.25–584.58 · C1B104 · GRID
- **Words** “And the theory was that. If you give the money, he can figure out how to push everything ahead, ahead, ahead.”  **Why** 'if you give the money, he can push everything ahead, ahead, ahead' → $ → Terman → three arrows.
- **FX** #2 diagram · **Ref** —
- **Visual** Graph paper; three pen arrows, one per 'ahead'.
- **Text** `the money` `the`@580.66 `money`@580.90 · `push everything` `push`@582.50 `everything`@582.82 · arrows on `ahead`@583.14 `ahead`@583.62 `ahead`@584.10
- **Camera** static. **Out** `PS` (planner rhythm fix — editor may pick another non-repeating type) @584.58.
- **SFX** 583.1 marker_scratch ×3 · 584.50 paper_slide (transition)

### C1S103 · 584.58–591.62 · C1B105 · NIGHT
- **Words** “So that that solved the one big problem. The federal money started flowing in to set up research labs at Stanford.”  **Why** 'solved the big problem. The federal money started flowing in to set up research labs at Stanford' → satellite Stanford, labs districts light, a yellow money route.
- **FX** #3 map + #20 · **Ref** D14 variant (satellite + highlighted districts + yellow route)
- **Visual** Stanford satellite (N26), districts vermilion overlay; yellow route.
- **Assets** N26 (see ASSETS_NEEDED)
- **Text** `one big problem` `one`@585.78 · `federal money` `federal`@586.90 `money`@587.30 · `flowing`@588.26 · `research labs at Stanford` `research`@589.38 `labs`@589.78 `at`@590.18 `Stanford`@590.42
- **Camera** push. **Out** `CA` @591.62.
- **SFX** 585.3 marker_scratch · 586.9 dot_slide (dur 2)

## 9. Act IX — The catch, hand-off to c2 (591.62–602.86)
Music: thin to one sustained layer; leave it hanging into c2.

### C1S104 · 591.62–596.02 · C1B106 · NIGHT
- **Words** “But even with the strongest government in the world backing you,”  **Why** 'even with the strongest government in the world backing you' → the Capitol dome, low angle.
- **FX** #16 + #8 · **Ref** —
- **Visual** Capitol (N23) low angle.
- **Assets** N23 (see ASSETS_NEEDED)
- **Text** `strongest government` `strongest`@593.46 `government`@594.10 · `backing you` `backing`@595.14 `you`@595.62
- **Camera** push. **Out** `PS` @596.02.
- **SFX** 593.4 air_swell

### C1S105 · 596.02–602.86 · C1B107 · PAPER
- **Words** “Terman very quickly this, or maybe he knew this already, is like Stanford cannot be best at everything.”  **Why** 'Terman … Stanford cannot be best at everything' → horizontal bars, title word by word, 'everything' struck.
- **FX** #2 chart + #19 · **Ref** D04/R6 variant (horizontal bars, italic emphasis word)
- **Visual** Unlabelled bars; most stay short.
- **Text** `Terman`@596.02 · `Stanford`@600.18 · `cannot be best at everything` `cannot`@600.98 `be`@601.38 `best`@601.62 `at`@601.94 `everything`@602.18
- **Camera** drift. **Out** `end` @602.86.
- **SFX** 600.9 marker_scratch

## 11. Coverage tables and checks

### 11.1 Effects (MANUAL §5 + §10)

| effect | scenes |
|---|---|
| #1 B-roll footage | C1S020, C1S031, C1S039, C1S059, C1S089, C1S094, C1S095 |
| #2 charts/diagrams | C1S010, C1S014, C1S015, C1S019, C1S023, C1S041, C1S043, C1S055, C1S058, C1S062, C1S078, C1S087, C1S088, C1S093, C1S102, C1S105 |
| #3 maps | C1S006, C1S007, C1S011, C1S021, C1S047, C1S057, C1S071, C1S101, C1S103 |
| #4 film-title hero | C1S004, C1S009, C1S016, C1S044, C1S048, C1S063, C1S084 |
| #5 newspaper/document | C1S003, C1S026, C1S033, C1S053, C1S072, C1S076, C1S088, C1S090 |
| #8 light streaks | C1S004, C1S009, C1S016, C1S031, C1S048, C1S063, C1S080, C1S095, C1S104 |
| #10 Vox layered | C1S025, C1S032, C1S049, C1S064, C1S066, C1S075, C1S082, C1S091 |
| #11 screens (TV/scope/radar) | C1S054, C1S086, C1S094 |
| #12 collage/timeline | C1S013, C1S018, C1S029, C1S038, C1S052, C1S061, C1S069, C1S070, C1S074, C1S085, C1S096 |
| #13 text animations (count/odometer/random/typewriter) | C1S001, C1S007, C1S008, C1S009, C1S014, C1S029, C1S032, C1S040, C1S048, C1S049, C1S050, C1S056, C1S063, C1S065, C1S067, C1S069, C1S074, C1S077, C1S081, C1S082, C1S092, C1S093, C1S099 |
| #14 gate weave | C1S017, C1S020, C1S028, C1S039, C1S059, C1S089 |
| #15 curve cut | C1S002, C1S017 |
| #16 hi-quality plate | C1S001, C1S002, C1S004, C1S012, C1S016, C1S022, C1S024, C1S028, C1S030, C1S036, C1S040, C1S044, C1S045, C1S051, C1S060, C1S068, C1S073, C1S079, C1S097, C1S100, C1S104 |
| #17 2.5D | C1S027, C1S056, C1S083 |
| #18 rough/stamp/highlighter | C1S003, C1S005, C1S015, C1S023, C1S033, C1S034, C1S036, C1S041, C1S053, C1S062, C1S092, C1S099 |
| #19 markups (pen, circle, cross, strings) | C1S003, C1S005, C1S012, C1S021, C1S030, C1S034, C1S035, C1S037, C1S042, C1S046, C1S050, C1S057, C1S061, C1S070, C1S073, C1S076, C1S078, C1S084, C1S087, C1S098, C1S100, C1S105 |
| #20 map call-outs | C1S006, C1S007, C1S012, C1S021, C1S057, C1S071, C1S101, C1S103 |
| §10.7 painting-to-print | C1S001, C1S003, C1S045, C1S046 |
| §10.6 call-outs (contrast/text/focal/radio waves) | C1S024, C1S026, C1S033, C1S047, C1S072 |
| whips / FW / CA / HC / PT / PS / MC | see §11.5 |

No iris anywhere ✔. Screens vary: 1950s TV (C1S054), 1940s oscilloscope (C1S086), WWII radar PPI scope (C1S094–095) — none of the four museum TVs, no Tatung/Trinitron (those are 1980s Taiwan).

### 11.2 Reference layouts (each a variation of its earlier use)

| ref | scene(s) | variation vs earlier use |
|---|---|---|
| D01 | C1S015 | with R1: navy watercolour East bar + skyline, label-box 90 % |
| D02 | C1S019 | 2 bars only, campus-tower cut-outs instead of portraits |
| D03 | C1S093 | person pictograms = 10 people each, count to 800 |
| D04 | C1S105 | unlabelled field bars, title word by word, 'everything' struck |
| D05 | C1S058 | era band = his first ten years; line falls and cracks |
| D06 | C1S041 | board seats, one seat swells with Hoover's portrait |
| D07 | C1S018 | collage poster of 1920s engineers + two campus cards, Stanford stamp |
| D08 | C1S092 | wartime telegram on Western Union ground + SECRET stamp |
| D09 | C1S071 | pictorial colour city map (not B/W), pin + pen circle |
| D10 | C1S006 | tilted *pictorial* California map + contrast call-out |
| D11 | C1S043 | Sankey into Stanford → ends in portrait circles |
| D12 | C1S077 | 25 unnamed ruled rows, yellow count, rack focus |
| D13 | C1S007, C1S047 | dark ghost world map: copies landing (C1S007), radio-wave rings (C1S047) |
| D14 | C1S103 | Stanford campus satellite, lab districts + yellow money route |
| D15 | C1S055, C1S078 | family two-node (C1S055); hub-and-spoke connections (C1S078) |
| R1 | C1S015 | see D01 |
| R4 | C1S010 | horizontal orientation |
| R5 | C1S023, C1S062 | graduates walking single file (C1S023), row + STOP (C1S062) |
| R6 | C1S105 | see D04 |
| R7 | C1S058 | see D05 |
| R9 | C1S024, C1S070 | small 3-card plan board |
| R10 | C1S021, C1S057 | railroad map: there-only route with 3 pins (C1S021), there-and-back (C1S057) |
| R11 | C1S101 | map-kit relief, pen route East→West |
| R12 | C1S007, C1S012 | Indiana navy (approved R12b), glowing valley on world map |
| markup-map | C1S037 | 1890s Stanford vs modern Stanford prints |
| s01 | C1S009, C1S048, C1S063 | 1938 & 12 cards |
| s02 | C1S011 | re-timed, map-kit basemap |
| s06 | C1S026, C1S090 | re-timed |
| s09 | C1S025, C1S049, C1S064, C1S066 | two-part (silhouettes → reveal) |
| s10 | C1S083 | re-timed |
| s11 | C1S034, C1S035, C1S098 | Washington lines, crosses |

All 15 intro refs (D01–D15) used; all original refs except R2 (optional) / R3 (skipped) and R8 (= D06 family, used via D06). New Pinterest-style ideas named in the scenes: antique globe → satellite match cut, blueprint title lettering, brush-stroke reveal, balance-scale infographic, tweet printed on paper, classified-ads highlighter, ledger ticks, brass door-plate title, slot-machine year counter, patent-style signal-flow diagram.

### 11.3 2.5D (3 moments)
C1S027 Main Quad 1891 (approved) · C1S056 1920 Stanford group with young Terman · C1S083–084 the HP garage (approved s10).

### 11.4 Ground rhythm (N night · P paper · G grid)
```
001N 002N 003P 004N 005G 006P 007N 008P 009N 010P 011N 012N 013P 014G 015P 016N
017N 018P 019G 020N 021P 022N 023P 024N 025N 026P 027N 028N 029P 030P 031N 032N
033P 034P 035G 036N 037P 038P 039N 040N 041P 042G 043N 044N 045N 046P 047N 048N
049P 050G 051N 052P 053P 054N 055P 056N 057P 058G 059N 060N 061P 062P 063N 064N
065P 066N 067P 068N 069P 070N 071P 072G 073N 074P 075N 076G 077N 078P 079N 080N
081P 082N 083N 084N 085P 086N 087P 088G 089N 090P 091N 092P 093G 094N 095N 096P
097N 098N 099P 100N 101P 102G 103N 104N 105P
```
Checked by the generator: no run of the same ground > 3; PAPER+GRID combined ≤ 3. ✔

### 11.5 Transitions in order (never the same type twice in a row — checked ✔)

PT, CA, W↑, CA, PS, CA, W→, CA, MC, CA, cont, W↓, PT, CA, MC, W↑, CA, PS, CA, W→, PT, CA, W→, CA, FW, PT, CA, W↓, CA, HC, W→, CA, HC, W↓, CA, W←, PS, W←, CA, FW, CA, PS, W↑, CA, cont, CA, FW, CA, MC, PS, CA, PT, CRT, W→, CA, FW, CA, W→, CA, PS, CA, W↑, CA, cont, CA, MC, W→, CA, PS, CA, PT, CA, W↓, CA, W↓, CA, PT, W←, CA, W→, MC, FW, cont, PS, PT, CA, W→, CA, FW, CA, W→, CA, HC, CA, W↑, CA, W←, PS, CA, W→, CA, PS, CA, PS, end

### 11.6 Hold before the cut (§10.9) — last text cue → scene end

Scenes where the last word lands < 0.9 s before the cut (editor: short entrance ≤ 0.3 s, the key animation of the scene must already be finished — e.g. bars/route/count complete before the last label; cut on the camera move): C1S001 (0.72 s), C1S002 (0.56 s), C1S004 (0.88 s), C1S005 (0.56 s), C1S006 (0.88 s), C1S007 (0.64 s), C1S010 (0.40 s), C1S011 (0.48 s), C1S013 (0.64 s), C1S018 (0.72 s), C1S019 (0.88 s), C1S026 (0.80 s), C1S029 (0.24 s), C1S032 (0.80 s), C1S033 (0.72 s), C1S035 (0.72 s), C1S037 (0.77 s), C1S038 (0.56 s), C1S040 (0.40 s), C1S041 (0.32 s), C1S042 (0.64 s), C1S044 (0.72 s), C1S047 (0.56 s), C1S051 (0.56 s), C1S053 (0.32 s), C1S056 (0.88 s), C1S057 (0.88 s), C1S058 (0.56 s), C1S062 (0.64 s), C1S065 (0.48 s), C1S068 (0.80 s), C1S069 (0.48 s), C1S070 (0.48 s), C1S071 (0.80 s), C1S073 (0.56 s), C1S074 (0.32 s), C1S077 (0.40 s), C1S080 (0.48 s), C1S081 (0.56 s), C1S082 (0.72 s), C1S083 (0.56 s), C1S086 (0.48 s), C1S088 (0.64 s), C1S089 (0.80 s), C1S090 (0.56 s), C1S092 (0.40 s), C1S094 (0.80 s), C1S096 (0.32 s), C1S101 (0.72 s), C1S102 (0.48 s), C1S104 (0.40 s), C1S105 (0.68 s).

Key animations that must complete + hold 0.5 s (explicit): C1S009 count 12 done by 53.6; C1S010 bars done by 58.0; C1S011 burn + pins done by 67.0, river by 68.6 (scene continues); C1S015 bar + count done by 89.2; C1S021 route done by 129.2; C1S027 1891 rise done by 172.1; C1S041 seat fill done by 239.0; C1S043 flows done by 249.9; C1S057 route + book done by 324.9; C1S058 line + crack done by 331.6 (cut 332.15); C1S069 $100 count done by 392.7; C1S077 count 25 done by 440.8; C1S093 isotype 800 done by 533.6; C1S103 route + districts done by 591.0; C1S105 strike done by 602.5 (chunk end 602.86).

### 11.7 Palette check
Vermilion = West/Stanford/HP/Terman's tags, routes and bars; navy = East (NY/NJ/MA, MIT, Harvard, Bell Labs, GE, Eli Lilly); yellow key numbers: 12 (C1S009), 90 % (C1S015), 1891 (C1S027), $100 (C1S069), 25 (C1S077), 800 (C1S093); all other yellow = highlighter. No red portrait duotones (red will mean Morris Chang/TSMC from c2 on). No celadon.

### 11.8 Verification summary
- No face cam ✔ · no iris ✔ · every scene has words + why ✔ · cues validated against the transcript ✔ · ≤ 3 same ground ✔ · no transition type twice in a row ✔ · every D01–D15 used ✔ · all §5 effects used (#6/#7 sound/texture everywhere) ✔ · 3 × 2.5D ✔ · holds listed ✔.

## 12. Open questions (defaults in DECISIONS.md)
1. Palette mapping for Silicon Valley (vermilion West/Stanford, navy East) — default yes.
2. 'born in the 1900s' → show `1900` (his meaning) — default yes.
3. 'powerful company' slip (= family) — never caption 'company' — default yes.
4. Hoover painted portrait for §10.7 (Greene 1956) — default yes.
5. Twitter-joke aside visuals (tweet card typeset, no handle; Puck cartoon; switch; trading floor; classifieds) — default yes.
6. 'Did they have Pentagon back then?' → Pentagon + hand-drawn ? (no answer) — default yes.
7. 12 trillion-dollar list date (Oct 29 2026 snapshot) — default keep.
8. Fantasia poster as 'Disney' (fair use) — default yes.

