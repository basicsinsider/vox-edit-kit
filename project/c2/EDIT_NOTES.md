# EDIT NOTES — CHUNK c2 "Taiwan: the chip rivalry" (Searching Lessons), VO local 0.00–597.86 (full audio 877.88–1475.72)

Shot-by-shot plan for chunk c2 (steeples of excellence → the transistor → Shockley comes home → Stanford Industrial Park →
Traitorous Eight / Fairchild → the integrated circuit → "that's where we get Silicon Valley from"). Read with
`project/LONGFORM.md`, `MANUAL.md` (**§10 overrides older sections; §10.9 = long-form rules**), `project/intro/BRIEF.md`
(still valid unless §10.9 relaxes it), `project/c2/analysis/BEATS.md` (beats, ASR fixes, cues), `ASSETS_NEEDED.md`
(asset IDs `E..` = exists, `N..` = needed), `SEGMENTS.md` (who builds what), `DECISIONS.md`.
Prepared 2026-10-31 by the c2 story analyst + edit planner.

## 0. How to read this file

- **Times** = LOCAL VO seconds of `vo_c2.mp3` (`transcript_c2.json`); scene boundaries on word starts.
  **128 scenes, C2S001–C2S128**, contiguous 0.00 → 597.86, no gaps. Average 4.7 s (the intro averaged 4.2 s).
- **Text cue `@t`** = start of the spoken word; first frame at `T(t) − 0.06`. Lines longer than one word are revealed
  **word by word** (each word its own literal `T()`), MANUAL §4.4.
- **Words** = exact narration under the shot; **Why** = why the picture matches those words (§10.1.3).
- **Ground**: `NIGHT` (dark/cinematic/archival full-frame), `PAPER` (Texturelabs `_hires` papers, two layers — top ≈ 90 %,
  §10.6.1), `GRID` (real scanned grid/ruled/ledger/blueprint/notebook paper: `assets/intro/papers/` K+E 1960 `_hires`,
  `assets/textures/paper_graph_01/lined_01/blueprint_01`). Rhythm: ≤ 3 in a row on one ground; PAPER+GRID ≤ 3 combined
  (§11.4). Never the same paper scan in consecutive scenes.
- **FX** = MANUAL §5 numbers + §10 craft: `W` whip (`FX.whip`, direction given), `FW` light-flash whip, `CA` cut on action,
  `HC` hard cut on action between two moving shots, `PT` push-through, `PS` paper slide / torn-paper wipe, `MC` match/curve cut,
  `cont.` same layout continues (camera move, no cut), `FH` focus hunt (once per scene max), `CS` `FX.chokeSettle`.
  **No iris.** Easing `FX.choppy(FX.ease.out|inOut|in, dur, 12)`; camera `FX.ease.cam` (not posterized).
- **Hold rule (§10.9)**: each scene's KEY animation (count, route, bars, stamp, reveal) finishes **≥ 0.5 s before** the scene's
  out-point; the cut-on-action uses the camera or a secondary motion. Scenes < 3 s list their "done by" time.
- **Glow**: `.halate` only on the scene's named **hero** (night only); everything else `.clean`; paper never glows.
- **Refs** = intro pack `D01–D15` (`references/style-images/intro/`), originals `R1–R12` (`references/style-images/1–12`,
  stills in `expected/layouts/`), plus **new reference ideas** named per scene (summarised in §11.2). Each reuse is a
  VARIATION: colour lead, orientation, density, entry animation are stated.
- **Palette for c2** (BEATS §7; = the lead's cross-chunk decision in LONGFORM.md for Silicon Valley content): **red** `#e03f2c` = West / Stanford / Terman / Palo Alto / the Industrial Park · **navy**
  `#1d5c9e` (sky `#9fc3e3` on night) = East / Bell Labs / New Jersey / Washington · **neutral** = Shockley, the eight,
  Fairchild, Noyce, other companies, military · **yellow** = highlighter + one key number per scene · no celadon (Taiwan
  doesn't appear). Max two accents per frame.
- **Spellings**: John Bardeen (ASR "Joan"), Walter Brattain ("Brayden"), Terman ("Termin", "Turman"), Traitorous Eight
  ("Traitress 8"), Fairchild Semiconductor, Robert Noyce, Leland Stanford, Stanford Industrial Park, Lockheed, Varian, HP,
  General Electric, Palo Alto. Everything else = his words; no text on slips (BEATS §2b).
- **Assets**: copyrighted archival allowed (§10.9 fair use, credited — 13 px micro-credit bottom-right while on screen,
  "© owner" in SOURCES.md). Prefer the TRUE image. Reuse allowed but prefer unique images (usage counts in ASSETS_NEEDED).
- **No face cam** in c2. **No upscaled paper scans** (full-frame grounds = `_hires` only). **Maps from `assets/maps/kit/`**
  (Natural Earth II / satellite / vintage atlas class — never flat grey/beige relief); old street/topo maps for close-ups.
- **SFX** lines = object events (LOCAL VO s) → `compositions/c2sNN.sfx.json` (vocabulary: intro SEGMENTS §3.4 + new
  `switch_click`, `tube_hum`, `solder_hiss`, `typewriter`, `card_flip`, `clock_tick`, `rewind`, `medal_ring`). Restraint pass
  (§10.8): mark the hero event per scene + each move; the sound pass thins them.

## 1. Act I — Steeples of excellence (0.00–56.37)
Music: continue c1's bed (same family); steady pulse; small lift on "steeples" 12.16; plant a soft motif on "silicon" 35.25.

### C2S001 · 0.00–2.08 · C2B001 · NIGHT
- **Words** "So it shouldn't even try."  **Why** c1 ended on "Stanford cannot be best at everything" → the long list of
  "everything" is struck out: Stanford shouldn't even try.
- **FX** #16 plate + #19 pen markup (`FX.markup.pen`, strike-through, bone) · **Ref** Pinterest idea "university course
  catalogue index, struck through" (dark, dense list — variation of D12's list but bright text on night).
- **Visual** Stanford Main Quad c.1900 plate (E40, dark-graded, fringe blur) behind a dense two-column list of ~30 field
  names (typeset in t-label bone at 40 %: Agriculture, Architecture, Chemistry, Electronics, Geology, Law, Medicine…).
  One fast pen stroke strikes the whole list diagonally @1.36 ("try") — done by 1.55.
- **Text** none spoken-word (the list is set dressing, typeset; no narrated words).
- **Hand-off** c1's last frame (lead to confirm with c1 planner): Stanford quad + "best at everything" list. If c1 ends
  differently, keep this scene and match its first frame to c1's last.
- **Out** `CA` — the list scrolls up fast while the camera pushes; cut mid-scroll @2.08 into C2S002's grid.
- **SFX** 1.34 marker_scratch · 2.00 whoosh_soft.

### C2S002 · 2.08–8.24 · C2B002 · GRID
- **Words** "His whole thing was that it's gonna pick a few fields, Paul pour all the resources that he's getting,"
  **Why** many field tiles → only a few kept → resources poured into them.
- **FX** #2 isotype + flow · **Ref D03** (isotype grid) **variation**: horizontal 10×3 grid of square field tiles (not
  people), ink-grey; lead colour red; entry = the tiles fly in from C2S001's scroll direction (up) at 12 fps.
- **Ground** K+E `ke1960_10x10_grid_black_norm_hires.jpg` multiply over paper_cream (E50).
- **Visual** 30 grey tiles @2.30; @4.24 ("few") all but 4 tiles fade to 20 % and slide away; the 4 survivors turn red
  (watercolour edge). @6.72 ("resources") a stream of small ink coins/dots (D11-like flow, on paper) pours from the top edge
  into the four tiles (12 fps).
- **Text** `a few fields` t-serif-i word-by-word `a` @4.16, `few` @4.24, `fields` @4.48 · `all the resources` t-label
  `all` @6.24, `the` @6.48, `resources` @6.72.
- **Camera** slow drift down (cam ease). **Out** `cont.` → C2S003 (the 4 tiles become bar bases).
- **SFX** 2.30 dot_ticks (0.5) · 4.30 paper_rustle · 6.70 dot_slide (1.0).

### C2S003 · 8.24–11.36 · C2B003 · GRID
- **Words** "and try to become the best in those few fields."  **Why** the four fields rise to "the best" line.
- **FX** #2 bars (12 fps, watercolour tops) · **Ref D01 variation**: 4 red bars rising from the tiles, dashed threshold
  labelled `the best` — no number box, no building (density low; vertical; entry = rise from the tiles).
- **Visual** bars rise @9.36 → cross the dashed line @9.52; all four clear it by 10.70 (hold ≥ 0.5 s).
- **Text** `the best` t-label on the dashed line: `the` @9.36, `best` @9.52 (label-box ink) · `few fields` small serif-i
  under the bars @10.32/10.64.
- **Out** the bar tops morph (12 fps) into four spire tips → `MC` into C2S004's painting spires @11.30.
- **SFX** 9.34 dot_ticks (bars, 0.8) · 11.28 whoosh_soft.

### C2S004 · 11.36–15.76 · C2B004 · PAPER (painting-to-print, §10.7)
- **Words** "He called steeples of excellence. That was his saying."  **Why** his phrase, treated as a quote: literal
  steeples (a colour painting of a church spire), then revealed as a printed pull-quote of "his saying".
- **FX** §10.7 painting-to-print + pen underline per word + #4 · **Ref** Lincoln reel (`references/reels/videos/
  lincoln_newspaper.mp4`) — variation: spire painting instead of a portrait; campus-newspaper column, not a broadsheet.
- **Assets** N01 Lyonel Feininger, *Gelmeroda IV* (1915) or *Gelmeroda VIII* (1921) — colour, tall Gothic spire (PD in the
  US; ≥ 2400 px). Page = typeset recreation in Crimson Pro/Haskoy (no real masthead), sepia newsprint, halftone.
- **Visual** open full-frame on the spire painting (slow push) → @14.70 eased 1.2 s pull-back + upward pan: it's a picture in
  a newspaper column with a small-caps caption `STEEPLES.` and the pull-quote below.
- **Text** pull-quote t-serif bold: `steeples` @12.16, `of` @12.80, `excellence` @13.60 — each word pen-underlined in red as
  spoken (`FX.markup.pen`). Caption line `— his saying` serif-i small: `his` @15.20, `saying` @15.36. (No name printed — he
  doesn't say it here; Terman is on screen two scenes later.)
- **Out** `W←` (whip left) @15.70.
- **SFX** 11.40 air_swell · 12.14 pencil_scribble (3 underlines) · 14.70 paper_slide (pull-back) · 15.68 whoosh.

### C2S005 · 15.76–20.88 · C2B005 · NIGHT (lamp pool)
- **Words** "In a simple words, what he was trying to say is that he doesn't want to be jack of all trade,"
  **Why** "jack of all trade(s)" → the Jack playing card ringed by many trades, pushed away.
- **FX** #16 + R9 lamp pool (desk under a lamp) + 12 fps card moves · **Ref R9** variation: green-baize card table instead of
  cork board, no string; Pinterest idea "vintage playing cards on felt, top-down".
- **Assets** N02 vintage Jack playing card scan (19th-c. PD deck, e.g. Commons "Playing cards 1880s"), N03 tiny trade icons
  (hammer, brush, scissors, wrench, quill — own SVGs, ink).
- **Visual** the Jack lands face-down @16.4, flips @19.44 ("jack"); ~10 trade icons orbit him; at 20.40 ("trade") the hand of
  icons scatters off the table (12 fps).
- **Text** none (the card carries it; slip "jack of all trade" not captioned — DECISIONS 4).
- **Out** `cont.` (same table) → C2S006.
- **SFX** 16.40 card_flip (soft) · 19.42 card_flip · 20.40 paper_rustle.

### C2S006 · 20.88–23.92 · C2B006 · NIGHT (lamp pool, same table)
- **Words** "he wants to be master of one or master of few."  **Why** one ace → a few aces.
- **FX** #13 word-by-word + card moves · **Ref** same as C2S005 (continuation).
- **Visual** the Jack slides out; a single Ace of spades slides to centre @22.40 ("one"); three more aces fan out beside it
  @22.96 (second "master") and finish by 23.42 so the fan holds 0.5 s before the cut; the text `few` @23.52 lands on the finished fan.
- **Text** `master of one` t-serif-i clean: `master` @21.68, `of` @22.16, `one` @22.40 · `master of few` below: `master`
  @22.96, `of` @23.28, `few` @23.52 (hero = none; clean).
- **Out** `PS` — a paper index card slides over the table from the right @23.86 (C2S007's first card).
- **SFX** 22.38 card_flip · 23.10 card_flip (fan) · 23.84 paper_slide.

### C2S007 · 23.92–30.88 · C2B007 · PAPER
- **Words** "And the few things he picks is electronics, radio science, materials research, and solid state physics,"
  **Why** the four chosen fields, each a card with a true image, landing as named.
- **FX** #12 collage (cards pinned stop-motion, torn edges) + #13 · **Ref D07** variation: a row of four typed index cards
  with photos + typographic boxes (density low, horizontal row, entry = pinned one per word; no stamps).
- **Assets** N04a electronics (1940s–50s Stanford/klystron or vacuum-tube lab photo), N04b radio science (1940s radio
  antenna/ionosphere sounder), N04c materials research (1950s crystal/metallurgy microscope photo), N04d solid-state
  physics (crystal lattice plate, e.g. a 1950s textbook diamond-lattice engraving). Cards = typewriter-label style
  (`paper_lined_01`).
- **Text** card titles t-label: `electronics` @25.44 · `radio science` @26.32/26.80 · `materials research` @27.44/28.24 ·
  `solid state physics` @29.04/29.60/30.00. Kicker `the few things he picks` NOT printed (rule: text minimal).
- **Camera** slow track left → right with the cards. **Out** `PT` into card 4's lattice image @30.82.
- **SFX** 25.42 pin_pop · 26.30 pin_pop · 27.42 pin_pop · 29.02 pin_pop (sound pass keeps 1–2) · 30.80 whoosh_soft.

### C2S008 · 30.88–36.13 · C2B008 · NIGHT
- **Words** "which is basically how electricity moves through solid material. Like silicon."  **Why** electricity (bright
  dots) moving through a solid's crystal lattice; then the real material: silicon.
- **FX** #8 subtle streaks + animated SVG lattice + #4 · **Ref** Pinterest idea "dark scientific diagram, glowing particles
  through a lattice" (Kurzgesagt-like but in our grain/texture).
- **Assets** N05 silicon lump photo (Commons "SiliconCroda.jpg" / polycrystalline silicon, CC) cut-out; lattice = own SVG.
- **Visual** diamond lattice drawn in bone hairlines (draw-on 12 fps), electron dots stream through @32.80 ("moves"); @35.25
  the lattice dissolves into the grey silicon chunk (rim light), which rotates slowly.
- **Text** `electricity` clean @32.00 · `moves` @32.80 · `solid material` @33.52/33.92 · `silicon` t-display 180 px
  **hero halate (bone)** @35.25.
- **Out** `FW` @36.08 (flash whip right).
- **SFX** 31.00 tone_blip · 32.78 dot_slide (1.0) · 35.23 chime_soft · 36.06 whoosh.

### C2S009 · 36.13–40.37 · C2B009 · PAPER
- **Words** "Remember the last part. Solid state physics relates directly to silicon."  **Why** callback: the 4-card row
  returns, all but "solid state physics" fade; a pen arrow joins it to a silicon card.
- **FX** §10.6.4 text contrast call-out + #18 highlighter + §10.6.2 pen arrow · **Ref** callout reel (Chris Moran).
- **Visual** C2S007's row (same layout, slight scale 0.85) — punch-in 10 % @36.13 while 3 cards fade to 20 %; highlighter
  swipes the `solid state physics` label @37.41; a fifth card (silicon chunk photo, N05) slides in right @38.6; red pen
  arrow draws card → card @39.40, lands @39.65.
- **Text** `silicon` t-label on the new card @39.65 (highlighted label above = existing card text).
- **Out** `cont.` → C2S010.
- **SFX** 36.15 paper_rustle · 37.40 highlighter_swipe · 39.40 marker_scratch.

### C2S010 · 40.37–44.53 · C2B010 · PAPER
- **Words** "And we'll come back to that part very quickly. So he has made that decision."  **Why** the silicon card is
  bookmarked (clipped) for later; Terman's photo card lands on the stack — decision made.
- **FX** #12 collage + rubber stamp (rough, settles — `CS`) · **Ref** D07 continuation (stamp variant).
- **Assets** N06 Frederick Terman portrait, 1950s, ≥ 1600 px (E41 `terman_frederick_1955.jpg` is only 960 px — card size
  only, ≤ native); red paper clip (own PNG).
- **Visual** a red paper clip snaps onto the silicon card @40.85 ("come back"); card slides into the margin. Terman card
  drops centre @42.93; ink stamp `DECISION` thuds @43.89 (settles by 44.0).
- **Text** stamp `decision` @43.89.
- **Out** `W↑` @44.47.
- **SFX** 40.84 pop_soft (clip) · 42.90 paper_slide · 43.87 stamp_thud · 44.45 whoosh.

### C2S011 · 44.53–48.85 · C2B011 · NIGHT
- **Words** "He's gonna try to make Stanford the best in these fields,"  **Why** Stanford campus; four red "steeples"
  rise out of it — the best in these fields.
- **FX** #16 plate + #20 callout pins + light #8 · **Ref** R12 variation (glow edge) on a photo instead of a map.
- **Assets** N07 Stanford campus aerial, 1940s–50s (Stanford Archives / Commons; copyright OK), ≥ 2400 px.
- **Visual** aerial plate, dark grade; 4 thin red light-pillars (steeple motif from C2S004) rise from campus @46.85 at
  12 fps, finish 47.9.
- **Text** `Stanford` t-label red @45.81 · `the best` clean @46.85/47.17 · `in these fields` @47.49/47.73/48.05.
- **Camera** slow push 1.0→1.08. **Out** `HC` — pillars still rising in camera push; hard cut @48.85.
- **SFX** 45.80 air_swell · 46.84 dot_ticks (pillars) · 48.80 whoosh_soft.

### C2S012 · 48.85–54.69 · C2B012 · PAPER
- **Words** "and he has the government helping him, but that doesn't necessarily guarantee success."  **Why** the government
  (Washington, East) sends money to Stanford (West) — but a "success" box stays unticked.
- **FX** #2 + #19 · **Ref D15** variation: two nodes only (US Capitol engraving in a navy ring → Terman/Stanford in a red
  ring), money arrow + label; orientation horizontal, entry = arrow draw-on; then a checkbox.
- **Assets** N08 US Capitol 19th-c. engraving (PD) for the navy circle; E41 Terman (circle crop, ≤ native size).
- **Visual** nodes pop @49.97; arrow draws @50.61 ("helping"); a ballot-style checkbox `success` appears @54.13, a pen
  hovers but doesn't tick (done by 54.2).
- **Text** `the government` t-label navy under the Capitol @49.73/49.97 · `guarantee` @53.41 · `success` @54.13 (box label).
- **Out** `CA` — the arrow keeps flowing as the frame rewinds (blur) into C2S013 @54.65.
- **SFX** 49.95 pop_soft · 50.60 marker_long (0.6) · 54.12 pencil_scribble (hover) .

### C2S013 · 54.69–59.73 · C2B013 · NIGHT
- **Words** "So he has to do more. Now this is where we will back up just a little bit."  **Why** "do more" then a literal
  rewind: years roll back.
- **FX** #13 odometer (year reels rolling backward) + #8 streaks (reverse direction) + tape-rewind smear · **Ref** Pinterest
  idea "VHS rewind / film counter rolling back" (variation of the intro's `1983` odometer: backward, smaller, off-centre).
- **Visual** `do more` lands; @57.65 ("back") the streaks reverse, a year odometer at frame right rolls 1951→1950→…→1947
  (reels slowing, cam ease), locking on `1947` at 59.97 in C2S014 (continues across the cut).
- **Text** `do more` clean serif-i: `do` @55.49, `more` @55.65 · `back up` t-label: `back` @57.65, `up` @58.05.
- **Out** `cont.` with the odometer → `PT` into the map @59.70.
- **SFX** 55.48 tick_soft · 57.62 rewind (1.6) · 59.68 whoosh.

## 2. Act II — Back up: 1947, the transistor (59.73–151.39)
Music: rewind whoosh; lighter, plucky texture under the explanation; hush during the word search; warm lift on "Nobel Prize".

### C2S014 · 59.73–63.25 · C2B014 · NIGHT (map)
- **Words** "In 1947, at Bell Labs in New Jersey,"  **Why** the year, the place on the map (East = navy), the lab pin.
- **FX** #3 map + #20 + #13 odometer lock · **Ref D14** variation: rich satellite US East Coast (map kit) with New Jersey filled
  navy/sky (overlay 0.8) instead of districts; no yellow route (pin + label only); entry = camera dives from the odometer.
- **Assets** K01 map-kit US East Coast satellite/relief (`assets/maps/kit/`), NJ outline from `us_overlay.json`.
- **Visual** `1947` odometer locks @59.97 (top-left, **hero halate**); NJ fills @62.29; pin at Murray Hill @61.17.
- **Text** `1947` @59.97 · `Bell Labs` pin label t-label @61.17/61.65 · `New Jersey` @62.29/62.53.
- **Camera** push to NJ, `FH` @62.7. **Out** `W→` @63.19.
- **SFX** 59.95 odometer_tick · 61.15 map_pin · 62.28 pop_soft · 63.17 whoosh.

### C2S015 · 63.25–67.57 · C2B015 · NIGHT
- **Words** "we have William Shockley, John Bardeen, and Walter Brattain"  **Why** the real 1948 Bell Labs photo of the
  three; the sharp spot moves to each man as he's named.
- **FX** #10 + §10.6.5 focal call-out (sharp circle travels) + #16 · **Ref** focal-blur call-out (Chris Moran).
- **Assets** N09 Bell Labs 1948 publicity photo "John Bardeen, William Shockley and Walter Brattain" (Shockley seated at the
  microscope; Commons / AT&T, © Nokia Bell Labs — fair use, credit), ≥ 2400 px.
- **Visual** photo sepia-duotone; focal circle on Shockley @63.73, slides to Bardeen @65.01, to Brattain @66.29 (long
  extreme ease); each gets a navy name tag.
- **Text** name tags t-label bone: `William Shockley` @63.73/64.13 · `John Bardeen` @65.01/65.33 · `Walter Brattain`
  @66.29/66.69.
- **Out** `CA` — push toward the bench/microscope @67.2 → C2S016.
- **SFX** 63.70 tone_blip (focus) · 65.00 tone_blip · 66.28 tone_blip (sound pass keeps one) · 67.20 whoosh_soft.

### C2S016 · 67.57–70.85 · C2B016 · PAPER
- **Words** "demonstrate how a transistor works. Transistor?"  **Why** the real Dec 1947 lab-notebook page/drawing of the
  first point-contact transistor; then the word with a question mark.
- **FX** #5 document (tilted page, halftone, push) + #13 · **Ref** intro dictionary page (IS015) variation: lab notebook
  (graph-ruled page, handwriting) instead of print.
- **Assets** N10 Brattain/Bardeen Bell Labs notebook page (Dec 1947) or the point-contact transistor replica photo (Commons,
  CC); fallback: patent drawing US 2,524,035 (PD).
- **Visual** page tilts in (rotateX 18°), push to the sketch.
- **Text** `transistor` t-serif @68.69 · `?` pops @69.97 (`Transistor?` replaces the label, word-level).
- **Out** `cont.` → C2S017 (same page).
- **SFX** 67.60 page_turn · 69.95 pop_soft.

### C2S017 · 70.85–73.57 · C2B017a · PAPER
- **Words** "Now, again, not an engineer in any way."  **Why** the narrator's honesty: the technical page gets his pen
  question marks; "not an engineer" in his hand.
- **FX** §10.6.2 pen markups (question marks, boil 4/s) · **Ref** markup reel.
- **Visual** 3 pen `?` scribbles draw around the circuit sketch (71.0–72.6).
- **Text** `not an engineer` pen-script look in t-serif-i: `not` @71.81, `an` @72.05, `engineer` @72.21.
- **Out** `PS` — a grid sheet slides over from below @73.51.
- **SFX** 71.00 pencil_scribble (1.4) · 73.49 paper_slide.

### C2S018 · 73.57–75.49 · C2B017b · GRID
- **Words** "Maybe one of the few Indians who's not."  **Why** the gag as an isotype: a grid of engineer icons, one
  empty spot — "one of the few who's not".
- **FX** #2 isotype (12 fps fill) · **Ref D03** variation #2: person pictograms (hard-hat/drafting icons) in ink, 8×4, the
  single hollow icon outlined in red; entry = fill in reading order. Done by 74.9.
- **Assets** N11 engineer pictogram SVG (own, adapt `assets/icons/graduate*.svg`).
- **Text** `one of the few` t-label @73.97/74.13/74.21/74.37 (no text on "Indians").
- **Out** `HC` @75.49 while the hollow icon pulses.
- **SFX** 73.60 dot_ticks (0.6).
- Hold: grid complete 74.9 → 0.59 s hold ✔.

### C2S019 · 75.49–79.97 · C2B018 · NIGHT
- **Words** "But transistor is basically like a switch. It tells electricity when it can come and go."  **Why** a real
  transistor next to a drawn switch symbol; current dots come and go through it.
- **FX** #16 cut-out + animated schematic (bone pen) · **Ref** Pinterest idea "museum object + hand-drawn schematic
  annotation on black".
- **Assets** N12 early transistor photo (Western Electric / Raytheon CK722 / TI 2N series, Commons CC), cut-out.
- **Visual** transistor rim-lit left; schematic switch draws right @77.17; dot current flows @79.41 ("come"), stops @79.73
  ("go") — switch arm opens.
- **Text** `a switch` clean @77.09/77.17 · `come` @79.41 · `go` @79.73.
- **Out** `W↓` @79.91.
- **SFX** 77.15 switch_click · 79.40 dot_slide (0.3) · 79.72 switch_click · 79.90 whoosh.

### C2S020 · 79.97–83.17 · C2B019 · PAPER
- **Words** "It's kind of like a switch you have in your bedroom,"  **Why** a 1950s magazine ad showing a bedroom wall light
  switch.
- **FX** #5 page treatment (halftone, tilt) + #19 circle · **Ref** Pinterest idea "mid-century print ad on newsprint".
- **Assets** N13 1950s home light-switch ad (GE / Leviton / Bryant toggle switch, LIFE or Saturday Evening Post via Google
  Books / archive.org — fair use) showing a bedroom; fallback: 1950s bedroom illustration + switch plate photo.
- **Visual** ad page, push to the switch; red pen circle round it @80.69.
- **Text** `your bedroom` t-label @81.81/82.21.
- **Out** `CA` — punch-in on the switch (1×→2×) @82.9.
- **SFX** 80.68 marker_scratch · 82.90 whoosh_soft.

### C2S021 · 83.17–87.01 · C2B020 · NIGHT
- **Words** "but it doesn't need like a physical movement to do anything, right?"  **Why** a finger flips a real switch
  (physical movement) — then crossed out.
- **FX** #1 footage + #14 weave + #19 cross · **Ref** markup reel.
- **Assets** N14 1950s–60s footage: hand flipping a wall light switch (Prelinger home-electrification films, archive.org).
- **Visual** clip at 0.8×; flip at ~85.0; bone pen X over the hand @86.37 ("anything") — done 86.5.
- **Text** `physical movement` clean @85.09/85.65.
- **Out** `FW` @86.95.
- **SFX** 85.00 switch_click · 86.36 marker_scratch · 86.93 whoosh.

### C2S022 · 87.01–95.26 · C2B021 · GRID (blueprint)
- **Words** "That's the whole thing that makes it so good. Where You can just turn it on and off with little electricity
  and it controls a lot of electricity."  **Why** a thin input current switches a thick output current — on, off.
- **FX** #2 flow diagram + 12 fps · **Ref D11** variation: Sankey on **blueprint paper** (light lines on blue, not dark ghost
  map), one thin band in → transistor symbol → one fat band out; entry = draw-on left to right.
- **Ground** `assets/textures/paper_blueprint_01` (hires) + K+E grid layer at 90 % top.
- **Visual** transistor symbol centre; thin line blinks on @91.34, off @91.74, on again @92.22; fat band floods out @93.98 and
  pulses with the thin one. Done by 94.6.
- **Text** `so good` serif-i @88.53/88.77 · `on` @91.34 · `off` @91.74 · `little electricity` t-label @92.22/92.54 ·
  `a lot of electricity` @93.98/94.06/94.22/94.38 (bigger).
- **Out** `PS` — blueprint rolls up from the bottom @95.20.
- **SFX** 91.33 switch_click · 91.73 switch_click · 93.96 air_swell · 95.18 paper_flip.

### C2S023 · 95.26–101.90 · C2B022 · NIGHT
- **Words** "That's basically what a transistor is. And when he invented this, we were already using other stuff that did
  this job."  **Why** the transistor as a hero object; then the camera pans to "other stuff" — a row of vacuum tubes in the
  dark.
- **FX** #16 + #4 + rack focus (`FX.focalBlur` sliding) · **Ref** Pinterest idea "dark museum vitrine line-up".
- **Assets** N12 (transistor, 2nd use) + N15 vacuum tubes row photo (Commons CC, e.g. "Vacuum tubes collection").
- **Visual** transistor centre, `transistor` @96.22; camera pans left (cam ease, 1.8 s) from 98.6 revealing tall tubes
  glowing faintly; focus pulls to them @100.14.
- **Text** `transistor` t-display **hero halate** @96.22 · `other stuff` clean @100.14/100.38.
- **Out** `CA` (pan continues) @101.86.
- **SFX** 96.20 chime_soft · 98.60 whoosh_soft · 100.10 tube_hum (dur 1.8).

### C2S024 · 101.90–106.62 · C2B023 · NIGHT
- **Words** "They used to be vacuum tubes, but they were massive, and they had a lot of other issues."  **Why** real vacuum
  tubes at their most massive: a huge 1920s–40s power tube / a wall of tubes.
- **FX** #1 footage + #14 weave + #16 · **Ref** —.
- **Assets** N16 = 10-min edit `ge_schenectady_1923_edison_langmuir_vacuum_tube.mp4` (re-download, example-docs/sources) —
  Edison & Langmuir holding a giant tube; or ENIAC tube racks photo (US Army PD).
- **Text** `vacuum tubes` clean @102.62/103.18 · `massive` t-display @104.38 · `issues` small @106.14.
- **Out** `W←` @106.56.
- **SFX** 101.92 projector_loop (dur 4.6) · 104.36 boom_low (soft) · 106.54 whoosh.

### C2S025 · 106.62–111.26 · C2B024 · PAPER
- **Words** "Like they wouldn't last that long, you know, hundreds of hours, and then you would have to replace it,"
  **Why** a real 1950s tube manual page; an hour-meter rolls through "hundreds of hours"; a technician replaces a tube.
- **FX** #5 manual page + #13 odometer (hour meter) + #12 photo card · **Ref** vintage manual rule (§10.5).
- **Assets** N17 RCA Receiving Tube Manual (1950s, archive.org) page with a tube diagram (sized ≤ native) on paper_stained;
  N18 photo "replacing a bad tube" ENIAC (US Army, PD).
- **Visual** manual page tilted; hour-meter odometer (bone on ink) spins 000→900 @108.78 (locks 109.6); photo card slides in
  @110.46 ("replace").
- **Text** `hundreds of hours` t-label @108.78/109.18/109.34 · `replace` @110.46.
- **Out** `PT` into the photo card's glowing tube @111.20.
- **SFX** 108.76 odometer_tick (0.8) · 110.44 paper_slide · 111.18 whoosh_soft.

### C2S026 · 111.26–114.30 · C2B025 · NIGHT
- **Words** "and they would get really, really hot, which was also an issue, right?"  **Why** a tube filament glowing hot.
- **FX** #1 macro footage + heat shimmer (displacement) + #4 · **Ref** —.
- **Assets** N19 macro footage of a glowing vacuum-tube filament (Pexels/Pixabay free, or Commons video), ≥ 1080p.
- **Text** `really` @112.14 · `really` @112.46 · `hot` t-display **hero halate** @112.62.
- **Out** `cont.` glow blooms to white → `FW` @114.24.
- **SFX** 111.30 tube_hum · 112.60 air_swell.

### C2S027 · 114.30–117.42 · C2B026 · NIGHT
- **Words** "So we had computers that used to run on vacuum tubes,"  **Why** a vacuum-tube computer: ENIAC.
- **FX** #16 plate + #10 light layering · **Ref** —.
- **Assets** N20 ENIAC photo (US Army, PD; Commons "Eniac.jpg" / "Classic shot of the ENIAC"), ≥ 2400 px.
- **Text** `computers` t-label @114.94 · `vacuum tubes` @116.46/116.86.
- **Camera** slow push into a tube rack → becomes the curve-cut start. **Out** `MC` (#15 curve cut) @117.9 — see C2S028.
- **SFX** 114.32 projector_click · 117.88 whoosh_big.

### C2S028 · 117.42–120.06 · C2B027 · NIGHT
- **Words** "but now that we had transistors, they could run on transistors."  **Why** curve cut: the ENIAC tube racks →
  a transistorised computer (TRADIC, Bell Labs 1954) sharing one zoom.
- **FX** #15 `FX.curveCut(tl, wrap, a, b, S(117.42), 1.1)` cut at peak velocity @117.90 + `FH` @118.6.
- **Assets** N21 TRADIC photo (US Air Force/Bell Labs, PD — Commons "TRADIC computer.jpg"), or IBM 7090 (IBM archives).
- **Text** `transistors` t-label @118.22 · `transistors` (second, larger) @119.50 — done 119.5, hold to 120.06.
- **Out** `W↑` @120.00.
- **SFX** 118.20 chime_soft · 119.98 whoosh.

### C2S029 · 120.06–125.50 · C2B028 · PAPER
- **Words** "And on top of that, one of the biggest benefits was the lifespan of transistors was possibly decades."
  **Why** a lifespan bar for transistors that runs for "decades".
- **FX** #2 horizontal bars + serif title, italic emphasis · **Ref D04** variation: two bars only, the transistor bar (ink)
  grows so long it runs off frame (camera tracks it); tube bar grey; title serif with italic red emphasis.
- **Ground** paper_cream hires + paper_stained top layer.
- **Text** title t-serif `the lifespan of transistors` @122.46/122.54/123.10/123.26 · emphasis `decades` italic red @124.94.
- **Visual** transistor bar grows from @123.26, crossing the frame edge by 124.9.
- **Out** `cont.` (camera tracks along the bar) → C2S030.
- **SFX** 123.25 marker_long (1.4) · 124.92 pop_soft.

### C2S030 · 125.50–129.50 · C2B029 · PAPER
- **Words** "So a very long lifespan compared to the alternative we had at the time."  **Why** camera rides back along the
  long bar to the tiny grey "alternative" (tube) bar.
- **FX** #2 continued · **Ref D04** continued.
- **Text** `very long lifespan` t-label on the bar @125.90/126.06/126.30 · `the alternative` grey label @127.58/127.74.
- **Out** `W→` @129.44.
- **SFX** 125.50 whoosh_soft (track) · 129.42 whoosh.

### C2S031 · 129.50–133.90 · C2B030 · NIGHT (museum vitrine)
- **Words** "On top of that, vacuum tube is like a bottle, or maybe it's smaller than a bottle, right?"  **Why** a vacuum
  tube standing next to a glass bottle — size comparison like a museum specimen.
- **FX** #16 cut-outs + R9 lamp pool · **Ref** new idea "natural-history specimen plate with scale ruler" (dark velvet
  variant), R9 lamp pool lighting.
- **Assets** N15 tube cut-out (large tube), N22 1950s glass soda bottle photo (Commons, CC) cut-out; ruler SVG.
- **Visual** tube placed @130.22; bottle slides in beside @131.26; tube shrinks a touch @132.22 ("smaller") — done 132.9.
- **Text** specimen labels t-label: `vacuum tube` @130.22 · `bottle` @131.26 · `smaller` serif-i @132.22.
- **Out** `cont.` (camera trucks right along the shelf) → C2S032.
- **SFX** 130.20 pop_soft · 131.24 pop_soft (glass) · 133.80 whoosh_soft.

### C2S032 · 133.90–139.66 · C2B031 · NIGHT (same vitrine)
- **Words** "But a transistor is like a coin. So it's already starting off very, very small, which is great."  **Why** a
  transistor next to a coin; zoom-out shows how tiny it is beside the tube.
- **FX** #16 + camera pull-back + `FH` @138.4 · **Ref** same specimen plate.
- **Assets** N12 transistor cut-out (3rd use — OK, §10.9) and N23 1950s US quarter/dime photo (US coins PD) cut-out.
- **Visual** transistor @134.30, coin beside @135.34; @137.50 camera pulls back 3× so tube+bottle loom over the tiny pair.
- **Text** `transistor` @134.30 · `coin` @135.34 · `very, very small` serif-i `very` @137.50 `very` @137.90 `small` @138.14.
- **Out** `PS` — torn paper wipe from below @139.60 (C2S033's paper).
- **SFX** 135.32 tick_soft (coin) · 137.50 whoosh_soft · 139.58 paper_tear.

### C2S033 · 139.66–143.34 · C2B032 · PAPER
- **Words** "This was groundbreaking, literally, and I think when I say groundmaking,"  **Why** "groundbreaking, literally"
  → the paper ground cracks open along the word.
- **FX** #18 rough edges + torn paper (`paper_torn_01`, Screen) split · **Ref** new idea "typographic crack / split paper".
- **Visual** `groundbreaking` t-display ink lands @140.14; @141.10 ("literally") the sheet splits along a jagged crack
  through the word, halves drift apart revealing night beneath (done 142.6).
- **Text** `groundbreaking` @140.14 · `literally` serif-i @141.10. (No text on "groundmaking".)
- **Out** `PT` through the crack into darkness @143.30.
- **SFX** 140.12 boom_low (soft) · 141.08 paper_tear · 143.28 whoosh_soft.

### C2S034 · 143.34–151.39 · C2B033–C2B034 · NIGHT
- **Words** "they they go on to people who found it this go on to when. What is it called? Nobel pre no not Nobel Priest
  Prize, I think Nobel Prize in Physics. Yeah."  **Why** while he searches for the word the medal turns out of focus; it
  snaps sharp when he finds "Nobel Prize in Physics".
- **FX** `FX.focusHunt` (long, deliberately unresolved until 149.6) + #4 + #16 · **Ref** DSLR focus-hunt reel.
- **Assets** N24 Nobel Prize medal (obverse, Alfred Nobel; Commons CC photo), ≥ 2000 px.
- **Visual** gold medal slowly rotating in a dark velvet case, heavy blur 143.4–149.4 (two hunting pulses); sharp @149.63.
- **Text** `Nobel Prize` t-display **hero halate** (bone) @149.63/149.95 · `in Physics` t-label @150.27/150.43.
- **Out** `CA` — medal rotation continues, push in → cut @151.39.
- **SFX** 143.40 air_swell (low) · 149.60 medal_ring (chime_soft) · 151.35 whoosh_soft.

## 3. Act III — Transistor everywhere (151.39–198.43)
Music: building layer; brighten on "radios" 181.15; widen to the world at 197.95.

### C2S035 · 151.39–155.95 · C2B035 · PAPER
- **Words** "Now, interesting point here, by the way, Bell Labs built this for telephones."  **Why** Bell System's own
  1950s ad about the transistor and telephones; Bell logo; a telephone.
- **FX** #12 collage poster + #5 halftone · **Ref D07** variation #2: poster with a big period photo of a 1950s telephone,
  typographic box, Bell System logo stamp (navy lead, vertical layout).
- **Assets** E42 `assets/logos/bell_system_1921.png` (navy tint) · N25 1950s Bell Telephone Laboratories transistor ad
  (LIFE/Scientific American 1950s — Google Books/archive.org, fair use) · N26 1950s black desk telephone (Western Electric
  500) photo cut-out (Commons CC).
- **Text** `Bell Labs` t-label navy @153.23/153.63 · `telephones` typographic box @155.23.
- **Out** `W→` @155.89.
- **SFX** 151.42 paper_slide · 153.21 stamp_thud · 155.87 whoosh.

### C2S036 · 155.95–162.83 · C2B036 · NIGHT (map)
- **Words** "You know, there was some use back in the day where there was a lot of issues sending your calls long distance."
  **Why** a coast-to-coast call line on a dark US map, noisy and breaking up.
- **FX** #3 + D13 dark line over ghost map + jitter · **Ref D13** variation: the line is a crackling signal path (not a
  chart), sky-blue (East origin) → bone; ghost US map from the map kit.
- **Assets** K02 map-kit US night/relief basemap; optional N27 1950s long-distance switchboard operators footage (AT&T
  Prelinger "Long Distance" films) in a picture-in-picture card.
- **Visual** line draws NY→SF @159.55, wobbles/drops out in segments (12 fps noise) @161.71.
- **Text** `calls` @161.15 · `long distance` @161.71/162.03.
- **Out** `cont.` → C2S037 (same map).
- **SFX** 159.50 tone_blip ×3 (static) · 161.70 marker_long.

### C2S037 · 162.83–169.95 · C2B037 · NIGHT (same map)
- **Words** "Transistors basically made that easier and cheaper, like more reliable, instead of doing other stuff."
  **Why** transistor repeater nodes pop along the line; it becomes steady; three benefits listed.
- **FX** #3 + **Ref D12** variation: dark list of three benefits on the right with a focus pull (blurred rows sharpen one by
  one) — text instead of money amounts.
- **Visual** 6 small transistor nodes pop along the line @162.83 (done 163.8); the line steadies.
- **Text** list rows clean: `easier` @164.91 · `cheaper` @165.63 · `more reliable` @166.83/167.07.
- **Out** `HC` @169.95 while the camera pulls out.
- **SFX** 162.85 dot_ticks (0.9) · 164.90 tick_soft · 165.62 tick_soft · 166.82 tick_soft.

### C2S038 · 169.95–176.75 · C2B038 · PAPER
- **Words** "I don't get it, but they built it for this, but slowly you realize how big of a deal this is, right?"
  **Why** "how big a deal" → a slow pull-back from a tiny transistor to the period magazine spread that hailed it.
- **FX** #5 magazine page + long pull-back · **Ref** §10.7 pull-back variation (no painting): Fortune, March 1953
  "The Year of the Transistor" (real article — fair use).
- **Assets** N28 Fortune 1953 "The Year of the Transistor" spread/cover, or LIFE 1950s transistor feature (archive.org /
  Google Books), ≥ 2400 px for the push.
- **Visual** start on a macro transistor printed in the column (171.3), slow 3 s pull-back reveals the whole spread @174.35.
- **Text** `how big` t-display ink @174.11/174.35 · `of a deal` @174.75/174.99/175.39.
- **Out** `CA` — pull-back continues into C2S039's grid @176.7.
- **SFX** 171.30 paper_rustle · 174.30 whoosh_soft.

### C2S039 · 176.75–180.35 · C2B039 · GRID
- **Words** "Like you could put these in any electronics, not just on telephones,"  **Why** an isotype of 1950s electronics
  fills in; the telephone is just one of them.
- **FX** #2 isotype · **Ref D03** variation #3: icons of objects (radio, TV, hearing aid, computer, car radio, phone) in a
  6×4 grid, ink with the telephone in navy; entry = row-by-row 12 fps.
- **Ground** `ke1960_mm_grid_green_norm_hires` (desaturated to ink-grey).
- **Assets** N29 own SVG icon set (1950s electronics).
- **Visual** grid fills @178.43 (done 179.3); telephone icon gets a red pen circle then the others highlight @179.79.
- **Text** `any electronics` t-label @178.11/178.43 · `not just telephones` serif-i @179.31/179.47/179.63/179.79.
- **Out** `PT` into the radio icon @180.30.
- **SFX** 178.40 dot_ticks · 179.78 marker_scratch · 180.28 whoosh_soft.

### C2S040 · 180.35–187.87 · C2B040 · NIGHT
- **Words** "you can put this in radios, which was which and which will end up becoming like the first portable device that
  people could have."  **Why** the real Regency TR-1 (first commercial transistor radio, 1954) + 1950s ads of people
  carrying a pocket radio.
- **FX** #10 Vox layered backgrounds (tinted ad panels drifting) + #16 · **Ref** s09 Vox cut-out (variation: object hero,
  three colour ad panels behind instead of newspapers).
- **Assets** N30 Regency TR-1 photo (Commons CC, any colour) cut-out · N31 2–3 1950s transistor-radio ads with people
  (Regency/Zenith/Sony TR-63, fair use).
- **Text** `radios` t-label @181.15 · `the first portable device` clean word-by-word @184.59/184.75/185.07/185.87.
- **Camera** drift + parallax. **Out** `W←` @187.81.
- **SFX** 181.13 pop_soft · 184.70 paper_slide (panels) · 187.79 whoosh.

### C2S041 · 187.87–194.03 · C2B041 · PAPER
- **Words** "And then yeah, you could put this in a bunch of the stuff that we'll talk about as innovations happen in our
  story."  **Why** a timeline of cards for the innovations still to come in this story (teaser).
- **FX** #12 collage/timeline (axis + travelling dot) · **Ref** s08 collage (variation: horizontal timeline, cards facing
  down = "to come", only silhouettes visible).
- **Assets** reuse photos already in c2/c3 (IC die N47, missile N35, computer N20) — shown small and dim (no new asset).
- **Visual** axis draws @188.6; 5 face-down cards drop along it; travelling red dot runs right @191.95.
- **Text** `innovations` serif-i @191.95 · `our story` @193.07/193.31.
- **Out** `FW` @193.97.
- **SFX** 188.60 marker_long · 189.20 paper_slide ×3 · 193.95 whoosh.

### C2S042 · 194.03–198.43 · C2B042 · NIGHT (map)
- **Words** "So after something like this happens, of course, everyone's innovating all around the world."  **Why** the
  world map lighting up with radio-wave rings from many places.
- **FX** #3 + §10.6.7 radio-wave rings · **Ref** Pinterest idea "dark world map with pulsing rings" (variation of intro IS055).
- **Assets** K03 map-kit world basemap (night-lights or Natural Earth II, dark grade).
- **Visual** rings pulse from ~10 cities @196.43 (done 197.7); camera tilts toward the US.
- **Text** `everyone's innovating` clean @196.43/196.91 · `all around the world` @197.47/197.63/197.87/197.95.
- **Hand-off** camera is gliding toward North America at 198.43 (c2s02 opens on the US map from that camera).
- **SFX** 194.10 air_swell · 196.40 tone_blip ×3.

## 4. Act IV — Terman's magnet & Shockley comes home (198.43–243.62)
Music: navy → red colour shift as the story moves West; tender, sparse 223.54–236.26; foreshadow sting on "big role" 241.70.

### C2S043 · 198.43–203.15 · C2B043 · NIGHT (map)
- **Words** "Terman, this is happening in the east, but Terman is using the money he's getting from the military"
  **Why** East (Bell Labs, navy) vs West (Stanford, red); the military money flows West to Terman.
- **FX** #3 + Sankey flow · **Ref D11** (dark Sankey over ghost US map) variation: one bone "military" band from Washington
  that widens as it crosses the map into a red Stanford node (horizontal, single source, entry = band grows E→W).
- **Assets** K02 map-kit US basemap (ghosted 35 %), E41 Terman circle (≤ native size), Washington pin.
- **Visual** NJ/Bell Labs glows sky-blue @199.95 ("east"); camera pans West (cam ease 1.4 s); Terman circle (red ring) pops at
  Stanford @200.43; band flows from DC @202.67, reaching Stanford by 203.6 (continues in C2S044).
- **Text** `the east` t-label sky @199.87/199.95 · `Terman` t-label red @200.43 · `military` bone label on the band @202.67.
- **Out** `cont.` (the band splits) → C2S044.
- **SFX** 199.93 pop_soft · 200.40 whoosh_soft (pan) · 202.65 marker_long (band).

### C2S044 · 203.15–210.02 · C2B044 · GRID
- **Words** "to start sending all these people who are doing leading, cutting edge research become. faculty at Stanford."
  **Why** researchers arrive one by one and fill Stanford's faculty seats.
- **FX** #2 parliament dots · **Ref D06** variation: Stanford faculty semicircle (red) filling seat-by-seat as figures arrive
  along the band from C2S043 (light ground instead of the D06 paper/italic title; seats are tiny person icons).
- **Ground** `ke1960_cross_section_green_norm_hires` desaturated.
- **Visual** person icons travel in from the left edge and drop into seats at 12 fps from 205.3; semicircle complete 209.3.
- **Text** `cutting edge research` serif-i @206.35/206.83/207.23 · `faculty` t-label @208.66 · `Stanford` red @209.46.
- **Out** `PS` — contract page slides over from the right @209.96.
- **SFX** 205.30 dot_ticks (2.0) · 208.64 pop_soft · 209.94 paper_slide.
- Hold: semicircle complete 209.3 → 0.66 s ✔.

### C2S045 · 210.02–213.86 · C2B045 · PAPER
- **Words** "So he's giving them bigger contracts, more money to come move to Stanford."  **Why** a real research contract
  (Office of Naval Research / Signal Corps — Stanford Electronics Research Lab) with "bigger contracts" highlighted.
- **FX** #5 document + #18 highlighter (body text, one stroke) · **Ref** §10.6.6 highlighter rules.
- **Assets** N32 1940s–50s federal research contract cover page with Stanford University (e.g. ONR contract N6onr-251, Stanford
  Archives / DTIC — fair use); fallback: typeset recreation "CONTRACT" form (no fake seals or signatures).
- **Text** `bigger contracts` typed-label + highlighter @210.90/211.22 · `more money` @211.78/211.94 · `Stanford` @213.22.
- **Out** `W↓` @213.80.
- **SFX** 210.88 highlighter_swipe · 211.76 typewriter (0.5) · 213.78 whoosh.

### C2S046 · 213.86–217.14 · C2B046 · NIGHT
- **Words** "Another interesting part, one of the Nobel Prize winner, William Shockley."  **Why** Shockley's portrait with the
  Nobel medal (callback) beside him.
- **FX** #16 plate + #4 · **Ref** —; motif: the C2S034 medal returns small.
- **Assets** N33 William Shockley portrait c.1956 (Nobel portrait — nobelprize.org / Commons, fair use), ≥ 1600 px.
- **Visual** portrait in duotone neutral (bone/ink); medal slides in bottom-left @215.14.
- **Text** `Nobel Prize` t-label @215.14/215.54 · `William Shockley` t-display **hero halate** @216.26/216.50.
- **Out** `CA` — portrait shrinks into a circle (D15 node) @216.9 → C2S047.
- **SFX** 215.12 chime_soft · 216.24 boom_low (soft).

### C2S047 · 217.14–220.42 · C2B047 · PAPER
- **Words** "So Terman is getting a lot of people who work with them, not the top guys,"  **Why** from Bell Labs' circle, many
  small grey people flow to Stanford — the three top men stay put.
- **FX** #2 relationship diagram · **Ref D15** variation #2: Bell Labs node (navy ring, logo E42) with three portrait circles
  (Shockley, Bardeen, Brattain — crops of N09) → arrow to Stanford node (red, Terman); grey dots stream along the arrow.
- **Visual** dots stream from 217.94 (done 219.4); the three portraits get a small pen bracket `not the top guys` @219.46.
- **Text** `a lot of people` t-label @217.94/218.02/218.18/218.26 · `not the top guys` serif-i @219.46/219.70/219.86/220.10.
- **Out** `cont.` → C2S048 (Shockley's circle detaches).
- **SFX** 217.90 dot_slide · 219.45 pencil_scribble.

### C2S048 · 220.42–223.54 · C2B048 · PAPER (vintage map)
- **Words** "but William Shockley himself comes to Palo Alto"  **Why** Shockley's circle travels coast to coast on a period
  road map and lands on Palo Alto.
- **FX** #3 + #20 · **Ref D10** variation: tilted 1950s colour road map of the US (rotateX 24°, rotateZ +6° — opposite tilt to
  the intro's Pacific map), dashed route East (navy) → West (red gradient); entry = route draws while camera tracks.
- **Assets** N34 1950s US road map (Esso / Rand McNally / Shell, colour scan — David Rumsey (licence check) / archive.org /
  fair use), ≥ 4000 px.
- **Visual** circle departs NJ @221.46 ("himself"); route draws; lands Palo Alto pin @222.50 — done 222.9.
- **Text** `himself` serif-i @221.46 · `Palo Alto` t-label red @222.50/223.06.
- **Out** `FW` @223.48.
- **SFX** 221.44 marker_long (1.0) · 222.48 map_pin · 223.46 whoosh.

### C2S049 · 223.54–227.14 · C2B049 · NIGHT (lamp pool)
- **Words** "because his mom, who's old and getting sick, is in Palo Alto,"  **Why** his mother's photo in a frame on a dark
  desk, a 1950s Palo Alto postcard beside it.
- **FX** #16 + R9 lamp pool + #12 photo card · **Ref** R9 variation (desk, no cork, no string).
- **Assets** N35m May Bradford Shockley photo (Shockley family / Stanford Special Collections — fair use; **don't print her
  name**); N36 1950s Palo Alto colour postcard (University Avenue).
- **Visual** framed photo under lamp @223.86; postcard slides in @226.02.
- **Text** `his mom` clean serif-i @223.70/223.86 · `Palo Alto` t-label @226.02/226.58.
- **Out** `CA` — slow push continues into the postcard @227.0.
- **SFX** 223.60 lamp_click · 226.00 paper_slide.

### C2S050 · 227.14–230.10 · C2B050 · NIGHT
- **Words** "and he wants to start a company selling transistors."  **Why** his company's real building/sign: Shockley
  Semiconductor Laboratory, 391 San Antonio Road.
- **FX** #16 plate + #19 underline · **Ref** —.
- **Assets** N37 Shockley Semiconductor Laboratory building photo (1950s, Computer History Museum / Stanford — fair use) or
  the 391 San Antonio Rd plaque/site photo (Commons CC).
- **Text** `a company` t-label @228.34/228.50 · `selling transistors` serif-i @228.98/229.38.
- **Out** `W→` @230.04.
- **SFX** 228.48 pop_soft · 230.02 whoosh.

### C2S051 · 230.10–236.26 · C2B051 · PAPER (old map)
- **Words** "And he's like, how about this? I'll just go do the company in Palo Alto, so I can be close to my mom."
  **Why** Palo Alto street map: a "company" pin and a "mom" pin, a short pen line between them = close.
- **FX** #3 old map + #19/#20 pins & pen · **Ref D09** (old city map) variation: USGS Palo Alto topo (E43) tinted warm sepia,
  vertical crop, two pins (red company, ink home), red pen bridge; entry = pins drop at 12 fps.
- **Assets** E43 `assets/maps/old/usgs_palo_alto_1899_topo.jpg` (+json) — ≥ native size; prefer N38 a 1950s Palo Alto city
  street map (archive.org / USGS 1953 Palo Alto quad, PD) for era.
- **Visual** company pin @232.10; home pin @235.38 ("my"); pen line joins them @234.82 ("close") — done 235.7.
- **Text** `the company` @232.02/232.10 · `Palo Alto` @232.82 · `close to my mom` serif-i @234.82/235.06/235.38/235.62.
- **Out** `cont.` → C2S052 (same map, zoom out).
- **SFX** 232.08 map_pin · 234.80 marker_scratch · 235.36 map_pin.

### C2S052 · 236.26–240.50 · C2B052 · PAPER (same map)
- **Words** "Nothing to do with like Stanford or anything. The decision was completely independent,"  **Why** zoom out to show
  Stanford's campus outlined in red; the line from Stanford to the company is drawn and crossed out — independent.
- **FX** #19 cross + #20 · **Ref D09** continued.
- **Visual** Stanford outline draws @237.62; dashed link draws and gets a pen ✗ @238.42; company pin rings once @239.86.
- **Text** `Stanford` t-label red @237.62 · `independent` serif-i @239.86.
- **Out** `PT` into the company pin @240.44.
- **SFX** 237.60 marker_long · 238.40 marker_scratch · 240.40 whoosh_soft.

### C2S053 · 240.50–243.62 · C2B053 · NIGHT (map)
- **Words** "but it's gonna end up paying a big role very quickly."  **Why** foreshadow: from the company's pin on a
  present-day satellite Bay Area, rings spread across the valley.
- **FX** #3 + §10.6.7 radio waves + §10.6.5 focal blur · **Ref D14** variation (satellite, no district fill, rings instead of
  a route; yellow none).
- **Assets** K04 map-kit Bay Area satellite (Esri World Imagery class, credit).
- **Visual** rings pulse @241.70 (3 rings, done 242.9).
- **Text** `a big role` clean @241.62/241.70/242.10.
- **Out** `W←` @243.56.
- **SFX** 241.68 boom_low (soft) · 243.54 whoosh.

## 5. Act V — The land trick: Stanford Industrial Park (243.62–371.18)
Music: pizzicato mischief for "finagling" 282.45; confident build from 289.81; roll-call rhythm 343.82–349.90; suspended chord
on "not Silicon Valley yet" 368.30 rising into 370.54.

### C2S054 · 243.62–248.50 · C2B054 · NIGHT
- **Words** "All the while this is happening, Terman does something else that's very interesting."  **Why** Terman back on
  screen (Vox cut-out) as the protagonist of this act.
- **FX** #10 Vox layered (tinted panels: Stanford quad, a land survey sheet, a 1950s calendar) + #16 · **Ref** s09.
- **Assets** N06 Terman 1950s portrait (hi-res, cut-out with `remove-background`), E40 quad, N39 survey sheet (PD USGS).
- **Text** `Terman` t-label red @245.22 · `something else` serif-i @246.34/246.66.
- **Out** `PS` — survey panel slides over @248.44.
- **SFX** 243.70 paper_slide ×2 · 248.42 paper_slide.

### C2S055 · 248.50–252.50 · C2B055 · PAPER
- **Words** "Place pays massive dividends down the road."  **Why** a dividend line that climbs far "down the road" — the line
  literally becomes a road receding into the distance.
- **FX** #2 line chart draw-on + perspective tilt · **Ref D05** variation: no axis values, no era band; the line chart plane
  tilts back (rotateX 55°) so the line turns into a road vanishing to the horizon (new idea: "chart becomes landscape").
- **Ground** paper_stained hires + paper_cream.
- **Text** `massive dividends` t-serif with italic red `dividends` @249.78/250.26 · `down the road` t-label @250.98/251.86/
  251.94.
- **Visual** line draws 249.0–250.6 (done) then plane tilts 250.98–251.9.
- **Out** `HC` @252.50 (tilt still moving).
- **SFX** 249.00 marker_long · 250.98 whoosh_soft.

### C2S056 · 252.50–255.54 · C2B056 · NIGHT
- **Words** "Stanford, when it was founded by Leland Stanford,"  **Why** the founder: Meissonier's colour oil portrait of
  Leland Stanford (paintings rule).
- **FX** #16 painting plate + #4 · **Ref** —.
- **Assets** N40 Jean-Louis-Ernest Meissonier, *Leland Stanford* (1881, Cantor Arts Center; PD-Art Commons) ≥ 2400 px; alt
  E44 Watkins 1874 portrait (re-download, example-docs/sources).
- **Text** `Stanford` t-label @252.50 · `Leland Stanford` t-display **hero halate** @254.10/254.82.
- **Out** `FW` @255.48.
- **SFX** 252.55 air_swell · 254.08 chime_soft · 255.46 whoosh.

### C2S057 · 255.54–260.50 · C2B057 · PAPER (map)
- **Words** "was granted eight thousand acres of land. A lot of land. That's insane amount."  **Why** the 8,000 acres filled
  red on a period map of the Palo Alto farm lands.
- **FX** #3 region fill (R12 halftone + glowing edge) + #13 count · **Ref R12** variation: vintage colour/USGS map instead of
  grey relief, fill red with halftone, edge glow; key number in a D01-style ink label box.
- **Assets** E43 USGS Palo Alto 1899 topo (+json) or N38 1950s quad; N41 Stanford lands outline (own SVG traced from the
  Stanford "Lands" map — Stanford Land Use & Environmental Planning, fair use).
- **Visual** outline draws @255.78 ("granted"); fill floods @256.42; count 0→8,000 @256.42 (done 257.1); camera pulls back
  a little @258.42 ("a lot of land").
- **Text** `8,000` label-box **yellow key number** @256.42 · `acres` @257.22 · `a lot of land` serif-i @258.42/258.58/258.74/
  258.90.
- **Out** `cont.` → C2S058.
- **SFX** 255.76 marker_long · 256.40 counter_ticks (0.7) · 258.40 whoosh_soft.

### C2S058 · 260.50–264.93 · C2B058 · PAPER (map)
- **Words** "I think that's like one fourth of San Francisco that's Stanford had."  **Why** San Francisco's outline split in
  four; one quarter slides onto Stanford's lands for comparison.
- **FX** #3 + leader labels · **Ref R11** variation: muted beige SF outline with a leader-line label, one quarter filled red;
  entry = SF slides in from the top of the frame (north), splits at 12 fps.
- **Assets** K05 map-kit Bay Area (vintage atlas style) with SF city outline (OSM/Natural Earth admin).
- **Visual** SF outline @262.34; quarter lines @261.70 timing → quarter slides south and overlays Stanford (done 264.3).
- **Text** `one fourth` t-label @261.30/261.70 · `San Francisco` leader label @262.34/262.58.
- **Out** `W↓` @264.87.
- **SFX** 261.68 marker_scratch · 262.32 pop_soft · 263.00 dot_slide · 264.85 whoosh.

### C2S059 · 264.93–267.49 · C2B059 · NIGHT (satellite)
- **Words** "Or has I'm not really sure how much they have now."  **Why** Stanford's land today from the satellite.
- **FX** #3 satellite + `FH` @265.6 · **Ref D14** variation #2 (satellite, red outline of today's campus, no route).
- **Assets** K06 map-kit Stanford satellite (Esri World Imagery / Google-style, credit) or E45 Stanford oval aerial 2007
  (re-download).
- **Text** `now?` serif-i @267.17.
- **Out** `cont.` → C2S060.
- **SFX** 264.95 tone_blip.

### C2S060 · 267.49–270.93 · C2B060 · NIGHT (satellite)
- **Words** "Well, technically speaking, they should have all of it, but let's not talk about that."  **Why** the original
  full 8,000-acre outline (dashed red) drawn over today's map — "all of it"; then the camera looks away.
- **FX** #20 map callout + quick camera whip-pan away · **Ref** D14 continuation.
- **Visual** dashed outline draws 268.0–269.0, glows @269.01; @269.81 ("let's not") camera whip-pans right (that whip is the
  transition).
- **Text** `all of it` clean @269.01/269.17/269.25.
- **Out** `W→` @270.87 (the whip-pan lands on the deed).
- **SFX** 268.00 marker_long · 270.85 whoosh.

### C2S061 · 270.93–276.69 · C2B061 · PAPER (document)
- **Words** "But there was one condition to Stanford having that, or I guess one rule in the deed that granted it to Stanford"
  **Why** the real 1885 Founding Grant of Leland Stanford Junior University.
- **FX** #5 document page (tilted 3D, halftone grows with the push, tinted blurred copy behind) · **Ref** s06 newspaper method
  on a legal document.
- **Assets** N42 Stanford Founding Grant 1885 pages (re-download `stanford_founding_grant_1885_heading_page.jpg` per
  example-docs/sources/assets_archival_documents.md) + a clause page.
- **Text** `one rule` t-label @273.97/274.13 · `deed` serif-i @274.69.
- **Camera** slow push to the clause area. **Out** `cont.` → C2S062.
- **SFX** 270.95 page_turn · 274.67 paper_rustle.

### C2S062 · 276.69–279.41 · C2B062 · PAPER (same document)
- **Words** "was they could not sell any of this land ever."  **Why** the clause highlighted; everything else dims.
- **FX** §10.6.4 text contrast call-out + #18 highlighter · **Ref** callout reel.
- **Visual** page fades to 20 % + punch-in 10 % @276.80; a typeset clause line (Crimson Pro, our recreation of the meaning in
  his words) returns full strength with the wipe; highlighter on `not sell` @277.33 (done 278.0).
- **Text** `could not sell` @277.09/277.33/277.65 · `ever` t-serif-i red @279.01 (a text cue, not the key animation — the
  key animation is the highlighter, done 278.0 → 1.4 s hold ✔).
- **Out** `CA` @279.41 (push continues into Terman).
- **SFX** 276.78 tone_blip (contrast "clunk") · 277.31 highlighter_swipe.

### C2S063 · 279.41–284.85 · C2B063 · NIGHT
- **Words** "And this is where Terman does that me and my friends like to call finagling. You know, you're finagling the
  rules."  **Why** Terman's cut-out with the deed behind him; pen loops wriggle around the rule.
- **FX** #10 Vox cut-out + §10.6.2 pen loops + `CS` reveal · **Ref** s09 variation (night, single tinted panel = the deed).
- **Assets** N06 Terman cut-out (2nd use), N42 deed panel.
- **Text** `Terman` t-label red @280.21 · `finagling` t-serif-i 140 px **hero halate** `CS` @282.45 · `the rules` @284.29/
  284.37.
- **Out** `PS` — ledger page slides up @284.79.
- **SFX** 282.43 pencil_scribble · 284.77 paper_slide.

### C2S064 · 284.85–289.81 · C2B064 · GRID (ledger)
- **Words** "I can't sell it. But how about I just rent it for very, very long time."  **Why** a ledger line: SELL crossed
  out, RENT written; a time ruler stretches "very, very long".
- **FX** §10.6.2 pen + #13 · **Ref** Pinterest idea "accountant's ledger with pen corrections".
- **Ground** E46 `assets/intro/papers/ledger_specimen_p318.jpg` (≤ native size, as a card on paper_lined_01 hires).
- **Visual** `sell` typed @285.25 → pen strike @285.49; `rent` handwritten @287.01; a dotted time ruler extends right from
  288.37 and runs off frame by 289.3.
- **Text** `sell` @285.25 · `rent` @287.01 · `very, very long time` serif-i @288.37/288.77/289.09/289.33.
- **Out** `FW` @289.75.
- **SFX** 285.47 marker_scratch · 287.00 pencil_scribble · 288.37 marker_long · 289.73 whoosh.

### C2S065 · 289.81–293.65 · C2B065 · NIGHT · 2.5D #1
- **Words** "So that's what he starts doing. He creates this thing called the Stanford Industrial Park,"  **Why** the real
  1950s aerial of the Stanford Industrial Park — one of the moments that deserves depth.
- **FX** #17 2.5D (s10 method: backdrop with buildings removed + blurred fill, mid layer = the low industrial buildings,
  foreground = trees/hill edge, title tucked behind the foreground) + `FH` after the dolly stops (@293.0) + haze.
- **Assets** N43 Stanford Industrial Park aerial photo, 1950s–early 60s (Stanford Archives / Palo Alto Historical Assoc. /
  Stanford Research Park history page — fair use, credit) ≥ 3000 px → 🛠 layer set + `layout.json`.
- **Text** title `Stanford Industrial Park` t-display **hero halate**, word-by-word `Stanford` @292.21, `Industrial` @292.85,
  `Park` @293.33 (behind the foreground trees).
- **Camera** dolly z −80 → 150, x drift. **Out** `CA` (dolly continues) @293.65.
- **SFX** 289.85 air_swell · 292.20 whoosh_big (dolly, low).

### C2S066 · 293.65–298.85 · C2B066 · PAPER (pictorial map)
- **Words** "meaning if you're a technology company who needs location, you can just come here."  **Why** a pictorial
  Peninsula map with the park parcel; a little company block arrives and settles "here".
- **FX** #3 + #19 arrow + 12 fps · **Ref D09** variation #2: colour pictorial map (not a street map) — red parcel outline,
  ink arrow, typographic "you are here"-style tag.
- **Assets** E47 `assets/intro/paintings/stanford_peninsula_map.jpg` (red pictorial Bay Peninsula map, 1920×2556; card-size
  crop ≤ native) — or N44 the "Palo Alto — birthplace of Silicon Valley" pictorial map Krish sent (if obtainable).
- **Visual** parcel outline draws @294.45; a factory-block icon slides from the frame edge @296.21; drops into the parcel
  @297.57 (done 298.2).
- **Text** `technology company` t-label @294.45/295.01 · `location` @296.21 · `come here` serif-i @297.57/297.89.
- **Out** `PS` — the lease form slides over @298.79.
- **SFX** 294.43 marker_long · 296.20 dot_slide · 297.88 map_pin · 298.77 paper_slide.

### C2S067 · 298.85–303.41 · C2B067 · PAPER (form)
- **Words** "And then yeah, you can get a ninety nine year lease on this land."  **Why** a lease form with the term typed in:
  99 years.
- **FX** #13 count + typewriter + #18 rough stamp · **Ref** new idea "typed government form with filled fields".
- **Assets** typeset recreation of a 1950s lease form (no seals/signatures) on paper_lined_01 hires; option N45 a real Stanford
  ground-lease page image if found (fair use).
- **Visual** form tilts in; `99` typed/counted @301.01 (done 301.6); `year lease` @301.73/301.97.
- **Text** `99` **yellow key number** @301.01 · `year lease` t-label @301.73/301.97 · `this land` @302.69/302.93.
- **Out** `W↑` @303.35.
- **SFX** 301.00 typewriter (0.6) · 303.33 whoosh.

### C2S068 · 303.41–306.61 · C2B068 · NIGHT
- **Words** "You can work here, and they're gonna be a lot of other benefits, right?"  **Why** engineers at work in a 1950s
  park lab (Varian/HP era footage).
- **FX** #1 footage + #14 weave + #16 · **Ref** —.
- **Assets** N46 1950s electronics-lab footage (engineers at benches, oscilloscopes — Prelinger / HP or Varian corporate films
  on archive.org / Computer History Museum YouTube via fetch relay).
- **Text** `work here` clean @303.73/303.97 · `benefits` t-label @305.65.
- **Out** `CA` (pan in footage) @306.61.
- **SFX** 303.45 projector_loop (dur 3.1).

### C2S069 · 306.61–311.89 · C2B069 · PAPER
- **Words** "One of the benefits is gonna be your people can come learn more in Stanford."  **Why** company employees in a
  Stanford classroom (1950s lecture photo) pinned as a card.
- **FX** #12 card + label box · **Ref D07** variation #3: single big photo card with a numbered tag `1` (benefit #1), stamp
  corner; entry = card swings in.
- **Assets** N47 1950s Stanford engineering classroom/lecture photo (Stanford Archives / Stanford Daily archive, fair use).
- **Text** tag `1` t-label · `your people` @308.37/308.85 · `learn` serif-i @310.13 · `Stanford` red @311.09.
- **Out** `cont.` — card slides left into the diagram @311.83.
- **SFX** 306.70 paper_slide · 310.12 pop_soft.

### C2S070 · 311.89–316.77 · C2B070 · GRID
- **Words** "So if there's graduate program any employees want to take, they can somehow get the salary,"  **Why** a
  three-node money diagram: employee ↔ company ↔ Stanford; first the salary arrow.
- **FX** #2 relationship diagram · **Ref D15** variation #3: triangle of three nodes (employee icon, company block, Stanford
  red ring), on graph paper; entry = arrows draw on as named.
- **Ground** `ke1960_10x10_grid_black_norm_hires` (different crop/colour from C2S002 — use `ke1960_cover_grid_blue_norm_hires`
  desaturated).
- **Text** `graduate program` t-label @312.69/313.17 · `employees` @313.73 · arrow label `salary` @316.13.
- **Out** `cont.` → C2S071.
- **SFX** 312.70 pop_soft · 316.10 marker_long.

### C2S071 · 316.77–321.58 · C2B071 · GRID (same)
- **Words** "still get their tuition paid by the company for this graduate program they're gonna study."  **Why** the
  company→Stanford arrow: tuition paid.
- **FX** #2 continued + small coin dots travelling · **Ref** D15 continued.
- **Text** arrow label `tuition` @317.49 · `paid` @318.05 · `by the company` @318.45/318.69/318.85.
- **Visual** arrow draws 317.49–318.3; coin dots run 318.85–320.4 (done).
- **Out** `W←` @321.52.
- **SFX** 317.48 marker_long · 318.84 dot_slide · 321.50 whoosh.

### C2S072 · 321.58–327.34 · C2B072 · NIGHT
- **Words** "And on top of that, all these professors that are gonna soon start coming in that are coming in already,"
  **Why** a real group photo of Stanford engineering professors of the 1950s; benefit #2.
- **FX** #10 + #16 + numbered tag `2` · **Ref** s09 variation (group photo, tag instead of panels).
- **Assets** N48 Stanford Electronics Research Lab / EE faculty group photo 1950s (Stanford Archives, fair use).
- **Text** tag `2` · `professors` t-label @323.50 · `coming in already` serif-i @326.22/326.46/326.78.
- **Out** `CA` (push) @327.30.
- **SFX** 321.60 paper_slide · 323.48 pop_soft.

### C2S073 · 327.34–330.38 · C2B073 · NIGHT
- **Words** "they're the leading edge in the stuff you guys are trying to do."  **Why** a Stanford invention at the leading
  edge: the klystron (Varian brothers, Stanford 1937) in the lab.
- **FX** #16 + #19 pen arrow · **Ref** markup reel.
- **Assets** N49 klystron photo (Stanford/Varian, Commons CC — e.g. "Klystron tube" or the 1937 Varian brothers with the
  klystron, Stanford, fair use).
- **Text** `leading edge` t-label + pen arrow @327.82/328.22 (arrow done 328.9).
- **Out** `PS` — split-week planner slides in @330.32.
- **SFX** 327.80 marker_scratch · 330.30 paper_slide.

### C2S074 · 330.38–336.14 · C2B074 · PAPER
- **Words** "Well, they can work for your company as paid consultant part-time while they're working for Stanford."
  **Why** a professor's week split: some days the company, some days Stanford.
- **FX** #2 Gantt-like bars + 12 fps · **Ref** new idea "1950s weekly desk planner with blocks" (Pinterest planner spreads),
  related to D04 bars (vertical orientation, two colours: ink company / red Stanford).
- **Assets** typeset planner on paper_graph_01 hires (Texturelabs).
- **Visual** professor circle (from N48 crop) top-left; ink blocks fill Mon–Tue @332.46; red blocks fill the rest @335.42
  (done 335.6).
- **Text** `paid consultant` t-label @332.46/332.86 · `part-time` @333.82 · `Stanford` red @335.42.
- **Out** `cont.` blocks fly to centre → `FW` @336.08.
- **SFX** 332.45 dot_ticks · 335.40 dot_ticks · 336.06 whoosh.

### C2S075 · 336.14–341.66 · C2B075 · NIGHT
- **Words** "So it's like a harmonious relationship happening between Stanford and all these companies,"  **Why** Stanford
  at the centre, companies orbiting in calm connection.
- **FX** #2 radial diagram + slow orbit + #8 faint streaks · **Ref D15** variation #4: dark ground, radial (hub & spokes)
  instead of triangle, entry = spokes draw one by one, gentle orbit.
- **Text** `harmonious relationship` serif-i @337.02/337.90 · `Stanford` red hub @339.50 · `companies` @341.10.
- **Out** `cont.` — the satellite nodes drop toward a parcel map (cut on that move) `CA` @341.66.
- **SFX** 337.00 chime_soft · 339.48 pop_soft.

### C2S076 · 341.66–346.46 · C2B076 · PAPER (park plan)
- **Words** "and companies started taking advantage of this. HP moves in, General Electric moves in,"  **Why** the park's
  parcel plan; HP and GE logo tiles drop onto their parcels as named.
- **FX** #3 plan + #12 logo cards 12 fps · **Ref R4/D02** idea re-cut as a map: logo circles landing on parcels; new
  reference "1950s land-subdivision plat map" (Pinterest).
- **Assets** N50 Stanford Industrial Park plan/plat (1950s–60s, Stanford Archives / Palo Alto, fair use) or typeset plat on
  blueprint-ish paper; N51 HP logo (vintage 1950s "hp" logo, `media-use resolve`), E48 GE logo
  (`assets/archival/brain_drain/ge_logo_bone.svg` / `ge_logo.svg` re-download).
- **Text** `HP` (logo is the text) @343.82 · `General Electric` logo + label @344.86/345.34.
- **Out** `HC` @346.46 while the GE tile is still settling (cut on action into the missile launch).
- **SFX** 343.80 stamp_thud · 344.84 stamp_thud (sound pass: keep the first, pitch-shift second).

### C2S077 · 346.46–349.90 · C2B077 · NIGHT
- **Words** "Lockheed's new missile division moves in, Varian moves in,"  **Why** Lockheed: a real missile from its missile
  division (Polaris launch, US Navy PD footage) with the Lockheed logo; then Varian's building/logo.
- **FX** #1 footage + #14 weave + logo cards · **Ref** —.
- **Assets** N52 Polaris missile launch footage (US Navy, PD, archive.org) — Lockheed Missiles & Space Division built it;
  N53 Lockheed logo (1950s), N54 Varian Associates logo + 1953 Varian building photo (first park tenant; fair use).
- **Visual** missile launch 346.46–348.6; `HC` inside the scene to Varian building @348.78 with logo.
- **Text** `Lockheed` logo/label @346.46 · `missile division` t-label @347.58/347.98 · `Varian` @348.78.
- **Out** `W↓` @349.84.
- **SFX** 346.50 boom_low (rocket, soft) · 348.76 pop_soft · 349.82 whoosh.

### C2S078 · 349.90–357.26 · C2B078 · PAPER (park plan, same)
- **Words** "a lot of companies that were founded in the area move their headquarters to this thing, or at least set up like
  something in there, right?"  **Why** the parcel plan fills up with many small company blocks.
- **FX** #2 isotype fill (buildings) on the plan · **Ref D03** variation #4: building pictograms filling parcels at 12 fps
  (density high), HP/GE/Lockheed/Varian tiles already in place.
- **Text** `a lot of companies` t-label @349.90/349.98/350.14/350.30 · `headquarters` @352.78.
- **Visual** parcels fill 350.3–355.3 (done); camera pulls back @355.4.
- **Out** `PT` — pull back continues and the plan shrinks into a photo circle @357.20.
- **SFX** 350.30 dot_ticks (2.5) · 355.40 whoosh_soft.

### C2S079 · 357.26–363.18 · C2B079 · NIGHT
- **Words** "So you have smart people, you have technological companies, and then you have bunch of land."  **Why** an
  equation: people + companies + land.
- **FX** #4 + 3 photo circles + plus signs · **Ref** new idea "Pinterest editorial equation layout (image circles with
  operators)".
- **Assets** N48 professors crop (people), E49 `assets/archival/hp/hewlett_and_packard_together_1960.jpg` crop (companies),
  N43 park aerial crop (land).
- **Visual** circle 1 @358.06, `+`, circle 2 @359.34, `+`, circle 3 @362.46.
- **Text** `smart people` @358.06/358.54 · `technological companies` @359.34/360.14 · `land` @362.46.
- **Out** `cont.` → C2S080.
- **SFX** 358.04 pop_soft · 359.32 pop_soft · 362.44 pop_soft.

### C2S080 · 363.18–371.18 · C2B080 · NIGHT
- **Words** "So there are a lot of equation happening uh already, but still, it's not Silicon Valley yet. That's about to
  happen."  **Why** the equation's "=" leads to an unlit SILICON VALLEY sign — not lit yet; it flickers "about to happen".
- **FX** #4 + #8 streaks (dim) · **Ref** new idea "unlit neon sign / marquee letters" (motif paid off at C2S127).
- **Visual** `=` @364.46; circles slide left; outline-only letters `SILICON VALLEY` (bone stroke, no fill) @368.30;
  `not … yet` in serif; one flicker @370.38 (done 370.6).
- **Text** `not` @368.06 · `Silicon Valley` (outline) @368.30/368.94 · `yet` @369.34 · `about to happen` @370.14/370.38/370.54.
- **Out** `FW` @371.12 (the flicker becomes the flash).
- **SFX** 368.28 tone_blip (neon buzz) · 370.36 tone_blip · 371.10 whoosh.

## 6. Act VI (part 1) — Tyranny of numbers (371.18–403.13)
Music: tense pulse / ticking under 382–403.

### C2S081 · 371.18–374.78 · C2B081 · PAPER
- **Words** "So there's another innovation that happens on top of transistors, right?"  **Why** a covered card is laid
  literally on top of the transistor card.
- **FX** #12 cards · **Ref** D07 card motif (variation: two cards stacked, top one blank with "?").
- **Assets** N12 transistor (cut-out on a card).
- **Text** `another innovation` serif-i @371.74/372.06 · `on top of` @373.10/373.26/373.50 · `transistors` @373.66.
- **Out** `PS` → blueprint @374.72.
- **SFX** 372.04 paper_slide · 373.26 paper_slide · 374.70 paper_flip.

### C2S082 · 374.78–378.73 · C2B082 · GRID (blueprint)
- **Words** "Transistors are a switch, but if you want to build a machine, any type of machine."  **Why** the switch symbol
  (C2S019 motif) multiplies into a machine's schematic.
- **FX** draw-on schematic + #13 · **Ref** C2S022 blueprint (different crop/rotation; ink lines bone on blue).
- **Assets** N55 1950s computer logic schematic (IBM/RCA manual, bitsavers — PD-ish/fair use) as faint underlay.
- **Text** `a switch` @375.66/375.74 · `a machine` t-display @376.94/377.02 · `any type of machine` serif-i
  @377.50/377.74/377.90/377.98.
- **Out** `CA` — schematic zooms out into C2S083's grid @378.70.
- **SFX** 375.72 switch_click · 377.00 marker_long.

### C2S083 · 378.73–382.41 · C2B083 · GRID
- **Words** "You need tens of thousands of transistors. Maybe more, right?"  **Why** transistor icons multiplying to tens
  of thousands; the camera keeps zooming out — maybe more.
- **FX** #2 isotype zoom-out (fractal) · **Ref D03** variation #5: tiny transistor pictograms, density extreme, camera zoom out
  ×20 (cam ease) — entry = multiply 1→10→100→… at 12 fps.
- **Ground** `ke1960_mm_grid_green_norm_hires` (≠ C2S039 crop/colour: use `ke1960_log_grid_green_norm_hires`).
- **Text** `tens of thousands` t-display ink @379.13/379.53/379.69 · `maybe more` serif-i @381.21/381.61.
- **Out** `W→` @382.35.
- **SFX** 379.10 dot_ticks (1.5) · 382.33 whoosh.

### C2S084 · 382.41–391.13 · C2B084 · NIGHT
- **Words** "And you're literally like soldering them, so like gluing them together with hand every time you're making a
  machine, which is a lot of headache."  **Why** real footage of hands soldering components one by one; then a tangle of
  wires = headache.
- **FX** #1 footage + #14 weave + §10.6.2 pen scribble (tangle) · **Ref** —.
- **Assets** N56 1950s–60s footage of hand soldering / wiring a computer or missile electronics (Prelinger, NARA, "Wiring a
  computer" IBM films) — contact sheet first; 2 shots (close soldering, wide assembly room).
- **Visual** close soldering (smoke) 382.4–386.3; `HC` inside to wide wiring room 386.33 ("gluing"); bone pen tangle scribbles
  over it @390.41 (done 390.6).
- **Text** `soldering` t-label @384.81 · `headache` serif-i @390.41.
- **Out** `CA` — the push into the tangle continues; cut on that move @391.13 into the TV's power-on.
- **SFX** 382.45 projector_loop (dur 8.6) · 384.80 solder_hiss · 390.40 pencil_scribble.

### C2S085 · 391.13–394.41 · C2B085 · NIGHT (TV)
- **Words** "And if you're talking about military stuff, let's say missiles,"  **Why** a 1950s newsreel of a missile launch,
  playing on a period TV set (how people saw missiles then).
- **FX** #11 TV (CRT power-on, scanlines, curvature, chromaticAberration 0.15) · **Ref** §10.1.7 better screens — **new set:
  1950s console/table TV** (RCA/Zenith/Admiral), NOT Tatung/Trinitron/IBM (used in the intro).
- **Assets** N57 1950s TV set photo with screen keyed (`*_screen.json`), N58 missile launch newsreel (Minuteman / Atlas / Thor
  test, USAF PD — archive.org Universal Newsreels).
- **Text** `military` t-label @392.57 · `missiles` @393.77.
- **Out** `PT` — camera pushes into the screen @394.0, the missile cutaway takes over @394.41.
- **SFX** 391.15 crt_click · 391.20 crt_hum (dur 3.2) · 393.75 boom_low (soft).

### C2S086 · 394.41–398.01 · C2B086 · PAPER (technical drawing)
- **Words** "10,000 pieces being soldered together every time,"  **Why** a missile cutaway drawing filling with 10,000
  component dots.
- **FX** #2 isotype dots inside a silhouette + #13 count · **Ref D03** variation #6: dot-fill inside an object outline
  (density extreme, ink dots, count in a D01 label box).
- **Assets** N59 1950s–60s missile cutaway/technical illustration (USAF / Convair Atlas manual, PD) — or own line drawing.
- **Text** `10,000` label-box **yellow key number** @394.41 (count done 395.1) · `pieces` @395.13 · `soldered together`
  @396.25/396.89.
- **Out** `cont.` → C2S087.
- **SFX** 394.40 counter_ticks (0.7) · 396.24 solder_hiss (soft).

### C2S087 · 398.01–403.13 · C2B087 · PAPER (same drawing)
- **Words** "means there's 10,000 things, 10,000 different options for things to go wrong."  **Why** the dots start failing
  one by one (tiny ✗ marks spread).
- **FX** #19 cross marks at 12 fps · **Ref** D03 continued.
- **Text** `10,000 things` @398.73/399.45 · `10,000` @400.01 · `different options` @400.81/401.13 · `go wrong` red serif-i
  @402.33/402.49.
- **Visual** ✗ marks spread from 399.5, ~200 by 402.6 (done).
- **Hand-off** at 403.13 the whole drawing slides up as a "problem" card (c2s03 starts with that card in frame).
- **SFX** 399.50 dot_ticks (2.5) · 402.48 boom_low (soft).

## 7. Act VI (part 2) — The Traitorous Eight (403.13–454.40)
Music: darker drone on "nightmare" 420.09; hits on "quit" 430.65 and "Traitorous Eight" 431.85; bright entrance on
"Fairchild" 435.69; hero lift on "Robert Noyce" 452.24.

### C2S088 · 403.13–407.69 · C2B088 · NIGHT
- **Words** "Someone needs to solve this problem. And guess what? Smart people are working on this."  **Why** the "problem"
  card (C2S087's drawing, shrunk) is pinned to the door of a lit lab at night — smart people at work inside.
- **FX** #16 plate + #12 card + lit-window flicker · **Ref** Pinterest idea "night exterior, warm windows, note on door".
- **Assets** N37 Shockley Semiconductor Laboratory building (2nd use, night grade) — or N46 lab footage still.
- **Text** `solve this problem` t-label @404.25/404.65/404.89 · `smart people` serif-i @406.25/406.65.
- **Out** `CA` — push toward the window @407.4.
- **SFX** 403.20 paper_slide · 404.90 pin_pop · 406.20 air_swell.

### C2S089 · 407.69–411.05 · C2B089 · NIGHT
- **Words** "William Shockley and his team are working on solving this problem."  **Why** the real photo of Shockley with
  his team (Nov 1956 lab celebration, glasses raised).
- **FX** #10 Vox layered + §10.6.5 focal blur (Shockley first, then the whole team) · **Ref** s09.
- **Assets** N60 photo "Shockley Semiconductor team toasting Shockley's Nobel, 1956" (Computer History Museum / Intel, fair use).
- **Text** `William Shockley` t-label @407.69/408.09 · `his team` serif-i @408.97/409.13.
- **Out** `PS` — ad page slides over @410.99.
- **SFX** 407.70 tone_blip (focus) · 410.97 paper_slide.

### C2S090 · 411.05–415.69 · C2B090 · PAPER (period ad)
- **Words** "Shockley is selling transistors, but he wanna see if he can come up with a better solution."  **Why** a real
  1958–60 Shockley Transistor Corp. trade ad (Electronics magazine) — the product he sold; "better solution" underlined.
- **FX** #5 page + §10.6.2 pen underline · **Ref** new idea "trade-magazine ad page, tilted, pen notes" (worldradiohistory.com
  Electronics scans).
- **Assets** N61 Shockley Transistor (4-layer diode) ad, *Electronics* 1958–60 (worldradiohistory.com, fair use).
- **Text** `selling transistors` t-label @411.85/412.17 · `better solution` serif-i + pen underline @414.81/415.05.
- **Out** `W↑` @415.63.
- **SFX** 411.10 page_turn · 414.80 pencil_scribble · 415.61 whoosh.

### C2S091 · 415.69–420.01 · C2B091 · NIGHT
- **Words** "Unfortunately, though, Shockley is a brilliant guy, but apparently not a good boss."  **Why** Shockley's portrait
  split in two halves: bright "brilliant" / shadowed "not a good boss".
- **FX** #16 + split light (two grades) + #4 · **Ref** new idea "split-tone portrait with two captions" (editorial posters).
- **Assets** N62 a second Shockley portrait (1950s–70s, e.g. Stanford News Service / Commons "William Shockley, Stanford
  University" CC) — different from N33.
- **Visual** left half lit @417.61; right half drops to shadow @419.05 (done 419.4).
- **Text** `brilliant` clean @417.61 · `not a good boss` t-label @419.05/419.21/419.37/419.53.
- **Out** `FW` @419.95 (shadow side flashes into the painting).
- **SFX** 417.60 chime_soft · 419.05 boom_low (soft) · 419.93 whoosh.

### C2S092 · 420.01–422.25 · C2B092a · NIGHT (painting)
- **Words** "A nightmare kind of boss to work with."  **Why** literally *The Nightmare* — Fuseli's oil painting (1781) as a
  short, ironic B-roll (paintings rule).
- **FX** #16 painting plate + #18 `CS` text · **Ref** —.
- **Assets** N63 Henry Fuseli, *The Nightmare* (1781, Detroit Institute of Arts, PD-Art), ≥ 2400 px.
- **Text** `nightmare` t-serif-i **hero halate** `CS` @420.09 (settled by 420.6) · `boss` small @420.97.
- **Camera** slow push. **Out** `PS` — org chart slides over @422.19 (done motion holds 1.6 s ✔).
- **SFX** 420.05 air_swell (dark) · 422.17 paper_slide.

### C2S093 · 422.25–428.49 · C2B092b · PAPER (org chart)
- **Words** "So he has some of the best scientists in the country working for him, but they couldn't really stand him."
  **Why** an org chart: Shockley on top, eight scientist circles under him; the circles turn away.
- **FX** #2 org chart + 12 fps · **Ref D15** variation #5: hierarchy (top-down tree), Shockley ink ring, eight grey circles;
  entry = lines draw down.
- **Assets** N64 portraits of the eight (crops from N65 photo) — small circles.
- **Visual** chart draws 423.0–424.3; at 427.13 the eight circles tilt/turn their backs (12 fps; done 428.0).
- **Text** `best scientists` t-label @423.77/424.09 · `the country` @425.13/425.29 · `couldn't stand him` serif-i
  @427.13/427.53/427.77/428.09.
- **Out** `cont.` → C2S094.
- **SFX** 423.00 marker_long · 427.10 paper_rustle.

### C2S094 · 428.49–431.05 · C2B093a · PAPER (same chart)
- **Words** "So one day eight of them get together and just quit."  **Why** the eight circles cut their lines and walk out
  together; a QUIT stamp.
- **FX** stop-motion 12 fps + stamp `CS` · **Ref** D15 continued.
- **Visual** lines snap @429.13; circles bunch together @429.85 and slide off right; stamp `quit` @430.65 (settles 430.75).
- **Text** `eight` t-display ink @429.13 · `quit` stamp @430.65.
- **Out** `W→` @430.99 (following the circles out).
- **SFX** 429.12 paper_tear (lines) · 430.63 stamp_thud · 430.97 whoosh.
- Hold: stamp settled 430.75 → 0.3 s before the whip starts — **start the stamp 0.2 s earlier (430.45, still a text-safe
  structural cue) so it settles by 430.55** ✔.

### C2S095 · 431.05–433.45 · C2B093b · NIGHT · 2.5D #2
- **Words** "They're called the Traitorous Eight."  **Why** the iconic 1960 group portrait of the eight — given depth.
- **FX** #17 2.5D (eight figures on 3 depth layers + backdrop) + #4 · **Ref** s10 2.5D method.
- **Assets** N65 Wayne Miller (Magnum) 1960 portrait of the Traitorous Eight (Moore, Roberts, Kleiner, Noyce, Grinich, Blank,
  Hoerni, Last) — © Magnum Photos, fair use, credit; ≥ 3000 px → 🛠 layer set.
- **Text** `Traitorous Eight` t-display **hero halate** @431.85/432.81 (done 432.9).
- **Camera** short dolly in (z 0→120). **Out** `CA` (dolly continues) @433.45.
- **SFX** 431.08 whoosh_big (low) · 431.83 boom_low.

### C2S096 · 433.45–437.68 · C2B094a · NIGHT
- **Words** "And then the very next day they start this company, Fairchild Semiconductor."  **Why** a calendar page flips one
  day; the real Fairchild Semiconductor logo + its first building (844 Charleston Rd).
- **FX** #13 + #16 · **Ref** new idea "tear-off calendar flip" + logo reveal.
- **Assets** N66 Fairchild Semiconductor logo (1950s–60s, `media-use resolve --type logo`), N67 Fairchild Charleston Road
  building photo 1958 (CHM / Fairchild, fair use); tear-off calendar = own typeset.
- **Visual** calendar flips @434.25 (done 434.7); building + logo @435.69 (logo settles 436.4).
- **Text** `the very next day` t-label @433.93/434.01/434.25/434.49 · `Fairchild Semiconductor` logo + label @435.69/436.49.
- **Out** `PS` — map slides up @437.62.
- **SFX** 434.24 paper_flip · 435.67 chime_soft · 437.60 paper_slide.

### C2S097 · 437.68–442.16 · C2B094b–C2B095 · PAPER (map)
- **Words** "Just right down the road. And yeah, this this company goes on for a very long time."  **Why** a short yellow
  marker route from Shockley's lab to Fairchild — "right down the road"; then the route keeps extending ("a very long time").
- **FX** #3 + #20 · **Ref R10/D14** variation: 1950s–60s Mountain View/Palo Alto street map (USGS 1961 quad, PD) — yellow
  rough marker route (R10's look) between two numbered pins; entry = pins pop, marker draws.
- **Assets** N68 USGS 1961 Mountain View / Palo Alto 7.5' quad (PD, ngmdb/topoView) ≥ 4000 px.
- **Visual** pins `1` (Shockley) and `2` (Fairchild) pop @437.70; marker route draws @438.24 (done 438.9); @441.52 the camera
  tilts so the road stretches to the horizon.
- **Text** `down the road` t-label @438.24/438.48/438.56 · `a very long time` serif-i @441.52/441.60/441.76/441.84.
- **Out** `cont.` → C2S098 (the road becomes a timeline).
- **SFX** 437.70 map_pin ×2 · 438.22 marker_long · 441.50 whoosh_soft.

### C2S098 · 442.16–448.00 · C2B096 · PAPER
- **Words** "In fact, just recently got acquired by some major company, but it was a major player for a very long time."
  **Why** a long timeline bar with the Fairchild logo travelling along it; a stamp "acquired" at its end (no acquirer named).
- **FX** #2 timeline + era band + stamp · **Ref D05** variation #2: horizontal era band = Fairchild's life, no years printed
  (none narrated), end stamp; orientation horizontal, ink lead.
- **Text** stamp `acquired` @443.44 (settles 443.6) · `major player` serif-i @446.64/446.88 · `a very long time` @447.36/
  447.44/447.60/447.76.
- **Out** `W←` @447.94.
- **SFX** 443.42 stamp_thud · 447.92 whoosh.

### C2S099 · 448.00–454.40 · C2B097 · NIGHT
- **Words** "And the reason being is because one of these eight people who finds finds this company is Robert Noyce, Bob
  Noyce."  **Why** the eight again — the focal circle travels along them and lands on Noyce; then Noyce's portrait.
- **FX** §10.6.5 focal blur + #16 + #4 · **Ref** focal call-out.
- **Assets** N65 eight photo (2nd use, flat), N69 Robert Noyce portrait c.1959–60 (Intel / CHM press photo, fair use)
  ≥ 1600 px.
- **Visual** focal circle sweeps from 449.28 along the eight, stops on Noyce @452.0; `HC` to Noyce portrait @452.24.
- **Text** `one of these eight` t-label @449.28/449.44/449.60/449.76 · `Robert Noyce` t-display **hero halate**
  @452.24/452.80 · `Bob Noyce` serif-i @453.44/453.68.
- **Out** `PS` @454.34.
- **SFX** 449.30 tone_blip · 452.22 chime_soft · 454.32 paper_slide.

## 8. Act VII — The integrated circuit (454.40–553.92)
Music: shimmering layer under the "print" idea 459–477; title swell on "integrated circuit" 478.40; thin bed under the aside
479–514; build on "rank" 518.35 → big lift on "100,000" 534.27; settle on "it just happened" 551.55.

### C2S100 · 454.40–459.04 · C2B098 · PAPER
- **Words** "And he solved the problem that we were talking about. Transistors, a lot of headaches."  **Why** Noyce's photo
  card clips onto the old "problem" card with the headache tangle (callbacks from C2S084/C2S088).
- **FX** #12 cards + pen tangle (callback) · **Ref** D07 card motif.
- **Text** `solved` t-label @454.88 · `the problem` @455.28/455.44 · `transistors` @457.04 · `headaches` serif-i @458.40.
- **Out** `PT` into the tangle, which straightens into a thin silver line @458.98.
- **SFX** 454.86 pop_soft · 458.38 pencil_scribble (short).

### C2S101 · 459.04–465.04 · C2B099 · NIGHT
- **Words** "But how about if you can just print it on like a silicon slice or something,"  **Why** a real silicon slice
  (wafer) from Fairchild's own 1960s film.
- **FX** #1 footage + #16 (chromaticAberration 0.12) · **Ref** —.
- **Assets** E50 `assets/intro/footage/wafer_closeup_purple.mp4` (Fairchild reel, Prelinger) or
  `silicon_crystal_melt_furnace.mp4` → wafer; usage in c2: 1.
- **Text** `print` t-label @461.68 · `silicon slice` serif-i @463.12/463.84.
- **Out** `MC` — the wafer's round edge matches the board's frame in C2S102 @464.98.
- **SFX** 459.06 air_swell · 461.66 tone_blip.

### C2S102 · 465.04–468.48 · C2B100 · NIGHT
- **Words** "you just print this whole setup that you're gonna do by hands."  **Why** split screen: left the hand-soldered
  board (C2S084 still), right a printed planar chip — the same setup, printed.
- **FX** split-frame divider wipe + #16 · **Ref** new idea "before/after split with a vertical divider".
- **Assets** N56 frame (soldering), N70 Fairchild Micrologic / planar IC die photo (Commons CC, e.g. "Fairchild uL914 die").
- **Visual** divider wipes left→right @465.52 (done 466.5).
- **Text** `whole setup` t-label @466.16/466.48 · `by hands` serif-i @467.68/467.84.
- **Out** `W↓` @468.42.
- **SFX** 465.50 whoosh_soft · 468.40 whoosh.

### C2S103 · 468.48–473.76 · C2B101 · PAPER (patent)
- **Words** "You can just print everything using light and photographic paper,"  **Why** Noyce's 1959 planar IC patent
  drawing; a beam of light passes through a mask onto the slice (photolithography).
- **FX** #5 document + #8 streaks as vertical light rays · **Ref** vintage-manual rule; new idea "patent drawing animated".
- **Assets** N71 US Patent 2,981,877 (Noyce, "Semiconductor device-and-lead structure", filed 1959) drawing sheet (PD,
  Google Patents) ≥ 3000 px.
- **Visual** patent sheet tilted; @470.56 light rays shine down through a stencil (mask) shape; @472.00 a photographic-paper
  sheet (Texturelabs paper, sepia) slides under and darkens in the mask's pattern (done 473.2).
- **Text** `light` t-label @470.56 · `photographic paper` serif-i @472.00/473.04.
- **Out** `cont.` → C2S104.
- **SFX** 470.55 air_swell · 472.00 paper_slide.

### C2S104 · 473.76–477.12 · C2B102 · PAPER (same patent)
- **Words** "and that way everything is just all together, right?"  **Why** the patent's separate parts slide together into
  one piece.
- **FX** 12 fps parts converge · **Ref** C2S103 continued.
- **Visual** parts converge 474.3–476.0 (done) and lock with a click.
- **Text** `all together` t-display ink @475.76/476.08.
- **Out** `PT` into the locked die @477.06.
- **SFX** 476.00 pop_soft (lock) · 477.04 whoosh_soft.

### C2S105 · 477.12–479.84 · C2B103 · NIGHT
- **Words** "This is something called the integrated circuit."  **Why** a real early IC die under a microscope (Fairchild film).
- **FX** #1 footage + #4 + `FH` @477.6 · **Ref** —.
- **Assets** E51 `assets/intro/footage/fab_microscope_closeup.mp4` (Fairchild reel) — usage 1.
- **Text** `integrated circuit` t-display **hero halate** @478.40/479.12 (done 479.2).
- **Out** `HC` @479.84.
- **SFX** 478.38 boom_low · 478.40 chime_soft.

### C2S106 · 479.84–485.28 · C2B104 · PAPER (manual)
- **Words** "Unfortunately, guys, I know that's not a good explanation, but I don't completely get how I can explain this
  properly."  **Why** a dense 1960s IC databook page — the narrator's pen question marks over it.
- **FX** #5 + §10.6.2 pen `?` marks · **Ref** vintage-manual rule; callback to C2S017.
- **Assets** N72 Fairchild Micrologic / "Integrated Circuits" 1960s databook page (bitsavers.org, fair use).
- **Text** `not a good explanation` serif-i @481.52/481.68/481.76/481.92.
- **Visual** pen `?` ×3 draw 482.7–484.4.
- **Out** `PS` — index card slides over @485.22.
- **SFX** 482.70 pencil_scribble · 485.20 paper_slide.

### C2S107 · 485.28–491.76 · C2B105 · GRID (index card)
- **Words** "Not an engineer. I try my best to understand it. So if you're an engineer, maybe you can drop some analogies down
  below."  **Why** a ruled index card "not an engineer" (callback); a pen arrow points down — "down below".
- **FX** §10.6.2 pen arrow (draw on, then out) · **Ref** markup reel.
- **Ground** `assets/textures/paper_lined_01` hires card on paper_cream.
- **Text** `not an engineer` @485.28/485.52/485.68 · `analogies` serif-i @490.16 · `down below` t-label @490.80/491.04 with a
  red pen arrow pointing down (done 491.2).
- **Out** `W↓` (follows the arrow) @491.70.
- **SFX** 485.30 paper_slide · 490.78 marker_scratch · 491.68 whoosh.

### C2S108 · 491.76–494.80 · C2B106 · NIGHT
- **Words** "But I think everyone knows what integrated circuits is."  **Why** ICs everybody knows — chips on everyday boards.
- **FX** #16 macro plate + slow slide · **Ref** —.
- **Assets** N73 modern chips on a phone/PC board macro (Commons CC).
- **Text** `everyone` clean @492.40 · `integrated circuits` @493.44/493.92.
- **Out** `CA` (slide continues) @494.80.
- **SFX** 491.80 whoosh_soft.

### C2S109 · 494.80–500.67 · C2B107 · PAPER
- **Words** "I just can't explain properly what was the Upgrade from transistors to integrated the circuit"  **Why** before →
  after: a transistor card → a big arrow → an IC card.
- **FX** #2 comparison + pen arrow · **Ref D01** variation: two "bars" become two object cards on paper with a dashed threshold
  labelled `upgrade` (density minimal, horizontal).
- **Assets** N12 transistor, N70 IC die.
- **Text** `upgrade` t-label @498.03 · `transistors` @498.75 · `integrated circuit` @499.63/500.27.
- **Visual** arrow draws 498.03–498.7.
- **Out** `FW` @500.61.
- **SFX** 498.02 marker_long · 500.59 whoosh.

### C2S110 · 500.67–506.59 · C2B108 · NIGHT
- **Words** "because it sounds so weird that hey you're literally printing the wirings and everything on this thing. That's
  just gonna work."  **Why** Fairchild-film macro: probe needles testing the printed wiring of a die — and it works (a
  square wave on the scope).
- **FX** #1 footage + #14 weave (light) · **Ref** —.
- **Assets** E52 `assets/intro/footage/wafer_probe_needles.mp4` + E53 `oscilloscope_fairchild_square_wave.mp4` (cut-in at
  505.8).
- **Text** `printing the wirings` t-label @502.99/503.39/503.47 · `work` serif-i @506.27.
- **Out** `cont.` → C2S111.
- **SFX** 501.00 projector_loop (dur 5.5) · 505.80 tone_blip.

### C2S111 · 506.59–509.79 · C2B109 · NIGHT
- **Words** "Because I have seen it. When you build computers, you have seen it."  **Why** a computer motherboard full of
  chips (what you see when you build computers).
- **FX** #16 plate + slow pan · **Ref** —.
- **Assets** E54 `assets/intro/photos/ibm5150_board_1984_cc0.jpg` (CC0, 6300 px original — use the full-size file).
- **Text** `build computers` t-label @507.95/508.27.
- **Out** `PT` into one chip @509.73.
- **SFX** 506.60 whoosh_soft.

### C2S112 · 509.79–514.03 · C2B110 · NIGHT
- **Words** "But yeah, I cannot publicly explain it, but this is like insane."  **Why** an extreme zoom into a chip's die —
  insane detail.
- **FX** deep zoom (cam ease) + `FH` @512.3 + #4 · **Ref** —.
- **Assets** N74 high-res die shot (Intel 4004 / any 1970s die, Commons CC; ≥ 4000 px).
- **Text** `insane` t-display **hero halate** @512.91.
- **Out** `W→` @513.97.
- **SFX** 510.00 whoosh_big (low) · 512.90 boom_low (soft) · 513.95 whoosh.

### C2S113 · 514.03–519.63 · C2B111 · PAPER
- **Words** "Like there are arguments online, debates online about the way does it rank in inventions."  **Why** a ranking of
  inventions, bars shuffling places = the debate.
- **FX** #2 ranked bars with circular images · **Ref D02** variation: bars topped with engraved invention circles (printing
  press, steam engine, light bulb, telephone, IC) — **no numbers, no names of ranks** (none narrated); bars swap positions at
  12 fps (debate); ink + one red bar (IC). Entry = bars rise left→right.
- **Assets** N75 PD engravings: Gutenberg press, Watt steam engine, Edison bulb, Bell telephone (Commons PD) + N70 IC.
- **Text** `debates` serif-i @515.87 · `rank` t-label @518.35 · `inventions` @519.07.
- **Visual** bars rise 514.5–515.9; two swaps 516.4 and 517.4 (done 517.9).
- **Out** `cont.` → C2S114.
- **SFX** 514.50 dot_ticks · 516.40 dot_slide · 517.40 dot_slide.

### C2S114 · 519.63–527.31 · C2B112 · PAPER (same chart)
- **Words** "Like if you were to rank impact each invention had on like aggregate humans as a whole, this is up there,"
  **Why** the IC bar climbs "up there" among the top.
- **FX** #2 continued + red pen circle · **Ref D02** continued.
- **Text** `impact` @520.83 · `up there` t-display @526.67/526.91.
- **Visual** IC bar rises 525.0–526.2; red pen circle round it @526.67 (done 526.8).
- **Out** `HC` @527.31 (camera tilt).
- **SFX** 525.00 marker_long · 526.65 marker_scratch.

### C2S115 · 527.31–531.31 · C2B113 · NIGHT
- **Words** "like how much impact this is gonna have altogether on all the humans."  **Why** Earth at night — all humans'
  lights (the chips' reach).
- **FX** #3 globe + slow rotation · **Ref** —.
- **Assets** N76 NASA Black Marble (Earth at night, PD) — map kit.
- **Text** `impact` @527.95 · `all the humans` clean @530.27/530.43/530.67.
- **Out** `PS` → graph sheet @531.25.
- **SFX** 527.35 air_swell.

### C2S116 · 531.31–538.19 · C2B114 · GRID
- **Words** "Like it took something that used to cost like 100,000 times more to like 100,000 times less."  **Why** a cost line
  plunging from a high marker "100,000× more" to a low marker "100,000× less".
- **FX** #2 line chart + #13 count · **Ref D05** variation #3: steep falling line, no years; two end labels; graph paper;
  the line draws with stopwatch ticks.
- **Ground** `ke1960_progress_chart_orange_norm_hires` desaturated (≠ earlier grids).
- **Text** `100,000` **yellow key number** label @534.27 · `times more` @535.31/535.71 · `100,000 times less` ink label
  @536.59/537.31/537.63.
- **Visual** line falls 535.8–537.4 (done).
- **Out** `cont.` → C2S117 (axis extends).
- **SFX** 534.25 counter_ticks · 535.80 clock_tick (1.6).

### C2S117 · 538.19–542.67 · C2B115 · GRID (same)
- **Words** "Like that's how big this thing was, or maybe millions of times more to millions of times less, right?"
  **Why** the axis stretches; the line keeps falling off the bottom — millions.
- **FX** #2 continued, camera tilt down · **Ref** D05 continued.
- **Text** `millions` t-display @540.11 · `millions of times less` @541.15/541.47/541.55/541.87.
- **Visual** axis stretches 539.0–540.3; line exits the bottom @541.87 (done 542.1).
- **Out** `W↓` @542.61.
- **SFX** 539.00 whoosh_soft · 542.59 whoosh.

### C2S118 · 542.67–550.75 · C2B116 · NIGHT
- **Words** "Like uh it is insane. It's like the cost dropped for something that's so important by a factor you can't even
  imagine."  **Why** an endless column of zeros scrolling down in a dark list — a factor you can't imagine.
- **FX** dark list + focus pull · **Ref D12** variation #2: one long number "1" followed by zeros scrolling vertically,
  blurred top/bottom, sharp centre (no amounts invented — zeros only, no value claimed).
- **Text** `cost dropped` t-label @544.91/545.47 · `can't even imagine` serif-i @549.15/549.63/549.95.
- **Visual** zeros scroll from 545.5, accelerate; freeze @550.2.
- **Out** `cont.` → C2S119 via a record-scratch whip.
- **SFX** 545.50 letter_ticks (4.0) · 550.20 tick_soft.

### C2S119 · 550.75–554.48 · C2B117 · PAPER
- **Words** "And it just happened. And by the way. Oh, we're getting off track."  **Why** "getting off track" → the camera
  slides off the list and lands back on the silicon card we bookmarked (C2S010) — back on track.
- **FX** whip-pan as the in-transition + #12 card · **Ref** callback.
- **Visual** `W←` lands @551.0 on the clipped silicon card; the red clip pops off @553.92.
- **Text** none.
- **Out** `cont.` → C2S120.
- **SFX** 550.75 whoosh · 553.90 pop_soft (clip).

## 9. Act VIII — Silicon → Silicon Valley (554.48–597.86)
Music: stop-go stabs 574.80–575.84; full lift on "Silicon Valley" 592.80; sustain into c3.

### C2S120 · 554.48–559.36 · C2B118 · PAPER
- **Words** "So he does all this on silicon, because silicon is a semi-conductor."  **Why** the silicon card flips to a
  vintage periodic-table cell: Si, 14 — labelled semiconductor.
- **FX** #5 chart page + highlighter · **Ref** new idea "vintage periodic table wall chart (1950s Welch / Sargent)".
- **Assets** N77 1950s periodic table chart scan (PD / fair use) or typeset cell on paper.
- **Text** `silicon` t-label @556.16 · `semiconductor` serif-i + highlighter @558.24.
- **Out** `FW` @559.30.
- **SFX** 556.14 card_flip · 558.22 highlighter_swipe · 559.28 whoosh.

### C2S121 · 559.36–566.64 · C2B119–C2B120 · NIGHT
- **Words** "And as the name suggests, which I didn't know until I started researching it, semi-conductor means like it can
  conduct electricity just like semi-ly."  **Why** the word itself splits: SEMI | CONDUCTOR.
- **FX** #13 kinetic type (split + slide) + #4 · **Ref** new idea "kinetic typography word split (Swiss poster)".
- **Text** `semiconductor` t-display @558.24 carried over → splits @562.40 into `semi-` (red) + `conductor` · `conduct
  electricity` clean @563.84/564.24 · `semi-ly` serif-i @565.60.
- **Out** `cont.` → C2S122 (the letters dissolve into the lattice).
- **SFX** 562.38 paper_tear (soft split) · 565.58 pop_soft.

### C2S122 · 566.64–572.64 · C2B121 · NIGHT
- **Words** "Meaning sometimes it can conduct it, sometimes it can't, depending on how you want to play with its properties,
  the elements."  **Why** the lattice motif (C2S008): current flows, then stops; dopant atoms (other elements) are added.
- **FX** animated SVG lattice + #8 · **Ref** C2S008 motif (variation: side view, two dopant colours bone/sky).
- **Visual** flow on @567.44; off @568.64; two different atoms drop into the lattice @571.84 (done 572.1).
- **Text** `sometimes it can` @566.96/567.28/567.44 · `sometimes it can't` @568.16/568.56/568.64 · `the elements` serif-i
  @571.68/571.84.
- **Out** `CA` — current resumes as we cut @572.64.
- **SFX** 567.42 dot_slide · 568.62 switch_click · 571.82 pop_soft.

### C2S123 · 572.64–576.16 · C2B122 · NIGHT (oscilloscope)
- **Words** "So that gives you a lot of freedom, right? You can stop, go, stop, go,"  **Why** a Tektronix oscilloscope showing a
  square wave — stop, go, stop, go — each word on a step.
- **FX** #11 screen (CRT grade) · **Ref** §10.1.7 — **Tektronix 475A scope frame** (E55, not used in the intro edit).
- **Assets** E55 `assets/intro/screens/tektronix_475a_scope_frame.png` + `_screen.json`; E53 square-wave clip (2nd use) or an
  own SVG trace synced to the words.
- **Text** `freedom` t-label @573.84 · `stop` @574.80 · `go` @575.20 · `stop` @575.52 · `go` @575.84 (each flashes on its wave
  edge).
- **Out** `PT` into the screen @576.10.
- **SFX** 572.66 crt_click · 574.78 tick_soft · 575.18 tick_soft · 575.50 tick_soft · 575.82 tick_soft (sound pass keeps 2).

### C2S124 · 576.16–582.56 · C2B123 · PAPER
- **Words** "because up after all computers, technically speaking, is just electricity, zeros and ones coming in and out, all
  this task."  **Why** an IBM punched card / binary tape: zeros and ones in and out.
- **FX** #5 card + 12 fps hole punching · **Ref** new idea "IBM 80-column card macro".
- **Assets** N78 IBM punched card scan (1960s, PD/CC) ≥ 3000 px; E56 `ibm_punch_cards_reader.mp4` as an inset (optional).
- **Text** `computers` t-label @577.04 · `electricity` @579.12 · `zeros and ones` serif-i @579.84/580.16/580.32 · `in and
  out` @580.80/580.96/581.12.
- **Visual** holes punch at 12 fps 579.8–581.4 (done).
- **Out** `W↑` @582.50.
- **SFX** 579.80 letter_ticks (1.5) · 582.48 whoosh.

### C2S125 · 582.56–588.00 · C2B124 · NIGHT
- **Words** "So semi- silicon is a very good material for that, and very abundant material for that."  **Why** silicon comes
  from sand/quartz — abundant: sand pouring, quartz crystal.
- **FX** #1 footage + #16 · **Ref** —.
- **Assets** N79 macro sand pouring footage (free/CC) + N80 quartz crystal photo (Commons CC).
- **Text** `silicon` t-label @583.36 · `very good material` @584.32/584.64/585.12 · `abundant` serif-i @586.64.
- **Out** `MC` — the sand pile's ellipse matches a wafer stack @587.94.
- **SFX** 582.60 sand pour (use wind, soft, dur 5.4).

### C2S126 · 588.00–591.44 · C2B125 · GRID
- **Words** "It's not something that's like hard to get, so you can scale with it."  **Why** wafers multiplying — scale.
- **FX** #2 isotype · **Ref D03** variation #7: wafer discs (own SVG from E50 still) multiply 1→4→16→64 at 12 fps.
- **Ground** `ke1960_10x10_grid_black_norm_hires` (not used since C2S002 — OK).
- **Text** `hard to get` @589.28/589.60/589.76 · `scale` t-display @590.64.
- **Visual** multiplication 589.8–590.9 (done).
- **Out** `FW` @591.38.
- **SFX** 589.80 dot_ticks · 591.36 whoosh.

### C2S127 · 591.44–594.24 · C2B126 · NIGHT
- **Words** "So that's where we get the Silicon Valley from,"  **Why** payoff: the unlit SILICON VALLEY sign from C2S080 now
  lights up over a real aerial of the valley.
- **FX** #4 + #8 streaks + light bloom · **Ref** C2S080 motif.
- **Assets** E57 `assets/intro/photos/silicon_valley_2014.jpg` (CC BY-SA, credit) or a 1960s–70s Santa Clara Valley aerial
  (N81, fair use) — prefer the period aerial.
- **Text** `Silicon Valley` t-display **hero halate** @592.80/593.52 (letters light 592.74–593.6).
- **Out** `cont.` → C2S128.
- **SFX** 592.78 boom_low · 592.80 tone_blip (neon on).

### C2S128 · 594.24–597.86 · C2B127 · NIGHT
- **Words** "because it's just such a big invention, and people don't realize how big."  **Why** pull-out: the valley turns out
  to be printed on a chip die — how big one small invention is.
- **FX** pull-back (cam ease) + die texture overlay · **Ref** §10.7-style pull-back variation (photo → die).
- **Assets** E57/N81 + N74 die shot.
- **Text** `big invention` clean @595.44/595.68 · `how big` serif-i @597.20/597.36.
- **Hand-off** c3 opens with "I don't think I'm completely explaining how big it was…" — end on the die, still pulling back
  (camera keeps moving through 597.86; c3 continues the move or cuts on it).
- **SFX** 594.30 whoosh_big (low) · 597.30 air_swell.

## 10. Music notes per segment (for the sound designer)
- c2s01 (0–198): continue c1's layered Epidemic bed; plucky/curious layer from 75; hush 143–149 (search for the word), warm
  lift 149.63; brighten 181; widen 197.
- c2s02 (198–403): colour shift East→West at 200; tender sparse 223–236; mischief at 282; confident build 290–357; suspended
  chord 368; tension pulse 382–403.
- c2s03 (403–598): drama 415–433; bright Fairchild 435.69; Noyce lift 452; shimmer 459–477; title swell 478.4; thin under the
  aside 479–514; build to 534.27; settle 551.55; stop/go stabs 574.8–575.8; full lift 592.80, sustain into c3.

## 11. Coverage tables

### 11.1 Effects (MANUAL §5 + §10)
| effect | scenes |
|---|---|
| #1 B-roll footage | S021, S024, S026, S068, S077, S084, S085 (in TV), S101, S105, S110, S125 |
| #2 charts (isotype, bars, lines, diagrams) | S002–003, S012, S018, S022, S029–030, S039, S044, S047, S055, S070–071, S074–075, S078, S083, S086–087, S093–094, S098, S109, S113–114, S116–117, S126 |
| #3 maps | S014, S036–037, S042, S043, S048, S051–053, S057–060, S066, S076, S078, S097, S115 |
| #4 film-title (hero halate) | S008, S014, S023, S026, S034, S046, S056, S063, S065, S092, S095, S099, S105, S112, S127 |
| #5 document/page treatment | S016, S020, S025, S038, S045, S061–062, S090, S103–104, S106, S120, S124 |
| #8 light streaks | S008, S013, S075, S080, S103 (light rays), S122, S127 |
| #10 Vox layered | S015, S040, S054, S063, S072, S089 |
| #11 screens (new sets) | S085 1950s TV, S123 Tektronix 475A scope |
| #12 collage / cards / timeline | S007, S009–010, S025, S035, S041, S069, S081, S100, S119 |
| #13 text animations | odometer S013–014 (backward), S025 (hour meter) · count S057, S067, S086, S116 · typewriter S045, S067 · word split S121 · word-by-word everywhere |
| #14 gate weave | S021, S024, S068, S077, S084, S110 |
| #15 curve/match cut | S027→S028 (curve cut), S003→S004, S101→S102, S125→S126 (match) |
| #16 hi-quality plate | S001, S011, S019, S023, S027, S031–032, S046, S049–050, S056, S088, S091–092, S108, S111 |
| #17 2.5D | S065 (Stanford Industrial Park aerial), S095 (Traitorous Eight) |
| #18 rough + highlighter | S009, S010, S033, S045, S062, S063, S092, S094, S120 |
| #19 markups (pen/arrows/crosses/circles) | S001, S009, S017, S020, S021, S039, S052, S064, S084, S090, S106, S107, S114 |
| #20 map callouts | S014, S048, S051–053, S057, S060, S066, S097 |
| §10.6 contrast/text call-out | S009, S062 · focal blur S015, S023, S053, S089, S099 · radio waves S042, S053 · highlighter S009, S045, S062, S120 |
| §10.7 painting-to-print | S004 (Feininger spire → campus-paper pull-quote) |
| paintings as B-roll (§10.5) | S004 Feininger, S056 Meissonier's Leland Stanford, S092 Fuseli's *The Nightmare*, S066 pictorial Peninsula map, S040 1950s radio ad illustrations |
| vintage manuals/datasheets (§10.5) | S016 lab notebook, S025 RCA tube manual, S090 Shockley ad, S103 Noyce patent, S106 IC databook, S120 periodic chart |
| focus hunt `FH` | S014, S028, S032, S034 (long hunt), S059, S065, S105, S112 |
| chokeSettle `CS` | S010, S063, S092, S094 |
| no iris | ✔ none |

### 11.2 Reference layouts — all intro refs used except D08 (carried over) + new ideas
| ref | scene(s) and the variation |
|---|---|
| D01 bars + threshold + label box | S003 (4 red bars, "the best" line, no building) · S086 (label-box count on a drawing) · S109 (two object cards + "upgrade" threshold) |
| D02 ranked bars topped with portraits | S113–S114 (engraved invention circles, bars swap = debate, IC in red) |
| D03 isotype grid | S002 (field tiles) · S018 (engineer icons, one hollow) · S039 (1950s electronics) · S078 (buildings on parcels) · S083 (transistors, zoom-out) · S086–087 (dots in a missile) · S126 (wafers) |
| D04 horizontal bars + serif title | S029–S030 (two bars, one runs off-frame) · S074 (vertical planner bars) |
| D05 line chart + era band | S055 (line becomes a road) · S098 (Fairchild era band + stamp) · S116–S117 (plunging cost line) |
| D06 parliament dots | S044 (Stanford faculty semicircle filling with arrivals) |
| D07 collage poster | S007 (four field cards) · S035 (Bell System ad poster) · S069 (benefit #1 card) |
| D08 telegram | **not used** in c2 (nothing in the words fits) → carries to c3 |
| D09 old city map | S051–S052 (Palo Alto topo, two pins) · S066 (pictorial Peninsula map) |
| D10 tilted topo map + route | S048 (1950s US road map, opposite tilt, East→West route) |
| D11 dark Sankey over ghost map | S022 (Sankey on blueprint: little current → a lot) · S043 (military money band → Stanford) |
| D12 dark list + focus pull | S037 (three benefits) · S118 (endless zeros) |
| D13 dark line over ghost map | S036 (crackling long-distance call line) |
| D14 satellite + district + yellow route | S014 (NJ fill + pin) · S053 (rings) · S059–S060 (today's Stanford + original outline) · S097 (yellow marker route, R10 look) |
| D15 relationship diagram | S012 (two nodes + money arrow) · S047 (Bell Labs → Stanford, top three stay) · S070–S071 (triangle: employee/company/Stanford) · S075 (dark radial hub) · S093–S094 (org chart) |
| R4 logos on bars | S076 (logos dropping onto parcels) |
| R9 lamp pool | S005–S006 (card table), S031–S032 (specimen vitrine), S049 (mother's photo desk) |
| R10 old map + yellow marker | S097 |
| R11 beige regions + leaders | S058 (SF quarter) |
| R12 region fill + halftone + glow | S057 (8,000 acres) |
| R5 isotype | as D03 |
**New reference ideas (named, to look up as Pinterest-style refs):** university catalogue index struck through (S001) ·
vintage playing cards on felt (S005–006) · dark scientific diagram with glowing particles (S008, S122) · VHS rewind / film
counter (S013) · museum object + hand-drawn schematic (S019) · mid-century print ad (S020) · natural-history specimen plate
with scale ruler (S031–032) · typographic crack / split paper (S033) · line chart that becomes a landscape/road (S055) ·
accountant's ledger with pen corrections (S064) · typed form with filled fields (S067) · 1950s weekly planner blocks (S074) ·
land-subdivision plat map (S076–078) · editorial equation with image circles (S079) · unlit neon/marquee sign (S080, S127) ·
night exterior with lit windows (S088) · trade-magazine ad page with pen notes (S090) · split-tone portrait with two captions
(S091) · tear-off calendar flip (S096) · before/after split divider (S102) · animated patent drawing (S103–104) · vintage
periodic-table chart (S120) · kinetic word split (S121) · IBM punched card macro (S124).

### 11.3 Ground rhythm (N night · P paper · G grid/ruled/blueprint)
```
c2s01  001N 002G 003G 004P 005N 006N 007P 008N 009P 010P 011N 012P 013N 014N 015N 016P 017P 018G 019N 020P 021N
       022G 023N 024N 025P 026N 027N 028N 029P 030P 031N 032N 033P 034N 035P 036N 037N 038P 039G 040N 041P 042N
c2s02  043N 044G 045P 046N 047P 048P 049N 050N 051P 052P 053N 054N 055P 056N 057P 058P 059N 060N 061P 062P 063N
       064G 065N 066P 067P 068N 069P 070G 071G 072N 073N 074P 075N 076P 077N 078P 079N 080N 081P 082G 083G 084N
       085N 086P 087P
c2s03  088N 089N 090P 091N 092N 093P 094P 095N 096N 097P 098P 099N 100P 101N 102N 103P 104P 105N 106P 107G 108N
       109P 110N 111N 112N 113P 114P 115N 116G 117G 118N 119P 120P 121N 122N 123N 124P 125N 126G 127N 128N
```
Longest runs: NIGHT 3 (013–015, 026–028, 110–112, 121–123); light (P+G) 3 (002–004, 016–018, 069–071, 081–083). ✔ ≤ 3.
Night ≈ 53 %, paper/grid ≈ 47 % — close to the intro's balance.

### 11.4 Transitions in order (never the same twice in a row)
c2s01: CA, cont, MC, W←, cont, PS, PT, FW, cont, W↑, HC, CA, PT(odometer), W→, CA, cont, PS, HC, W↓, CA, FW, PS, CA, W←, PT,
FW, MC(curve), W↑, cont, W→, cont, PS, PT, CA, W→, cont, HC, CA, PT, W←, FW, CA(boundary glide) ·
c2s02: cont, PS, W↓, CA, cont, FW, CA, W→, cont, PT, W←, PS, HC, FW, cont, W↓, cont, W→(whip-pan), cont, CA, PS, FW, CA, PS,
W↑, CA, cont, cont, W←, CA, PS, FW, CA, HC, W↓, PT, cont, FW, PS, CA, W→, CA, PT(into screen), cont, (slide-up boundary) ·
c2s03: CA, PS, W↑, FW, PS, cont, W→, CA, PS, cont, W←, PS, PT, MC, W↓, cont, PT, HC, PS, W↓, CA, FW, cont, PT, W→, cont, HC,
PS, cont, W↓, cont(scratch whip), cont, FW, cont, CA, PT, W↑, MC, FW, cont, (moving end into c3). ✔ no type twice in a row
(`cont.` = same layout, not a transition). Whip directions vary ← → ↑ ↓.

### 11.5 Palette check
Red (West/Stanford/Terman/Palo Alto/Industrial Park): S002–004, S011–012, S043–045, S047–048, S051–052, S057, S060, S063,
S066, S069–071, S074–076, S109 (IC bar), S113–114, S121 ("semi-"). Navy/sky (East/Bell Labs/NJ/Washington): S012, S014–015,
S035–037, S043, S047–048. Neutral: Shockley/eight/Fairchild/Noyce throughout. Yellow key numbers: `8,000` (S057), `99`
(S067), `10,000` (S086), `100,000` (S116); other yellow = highlighter (S009, S045, S062, S097 marker route, S120). No celadon.
Max two accents per frame: S043/S047/S048 carry red + navy only.

### 11.6 Checks against Krish's rules
- No face cam ✔ · every scene lists the words it covers + why ✔ · animations finish + hold ≥ 0.5 s (short scenes list "done
  by"; editors confirm in snapshots of each scene's last second) ✔ · ≤ 3 same ground ✔ · no same transition twice ✔ · no
  iris ✔ · halation only on one hero per scene ✔ · paper grounds = `_hires` only; small scans as cards at ≤ native size ✔ ·
  maps from the map kit (K01–K06) or real period maps ✔ · cohesive with the intro: same type system, textures, D-layouts as
  variations, Vox call-outs, painting-to-print, paintings as B-roll, better screens (new sets) ✔.

## 12. Open questions (defaults in DECISIONS.md)
1. Palette mapping — **settled** by the lead's cross-chunk colour decision (LONGFORM.md): vermilion = West/Stanford, navy = East.
2. "jack of all trade" — no caption (card only)? → yes.
3. Copyrighted key photos (Traitorous Eight by Wayne Miller/Magnum, Bell Labs trio, Shockley/Noyce portraits, Fortune 1953) —
   use with credit (fair use)? → yes per §10.9.
4. Fuseli's *The Nightmare* for "a nightmare kind of boss" — playful literal painting; OK? → yes (2.2 s, paintings rule).
5. Shockley's mother — show a real photo if found, never print her name → yes.
6. D08 telegram unused → carry to c3.
7. "Stanford Industrial Park" (his words) vs today's name "Stanford Research Park" → show his words only.
8. Acquirer of Fairchild unnamed in VO → never name/show it.
9. c1→c2 first frame: C2S001 assumes c1 ends on Stanford + a "best at everything" list → lead to align with c1's planner.
