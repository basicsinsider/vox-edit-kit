# EDIT NOTES — CHUNK c3 "Taiwan: the chip rivalry" (Searching Lessons), VO local 0.00–602.02 (full audio 1475.72–2077.72)

Shot-by-shot plan for chunk c3. Read with `project/LONGFORM.md` (the brief), `MANUAL.md` (**§10.1–10.9 override older
sections**; §5 effects; §6/§6.1 reference layouts), `project/c3/analysis/BEATS.md` (beats, ASR fixes, cues), `ASSETS_NEEDED.md`
(asset IDs `E..` = exists, `N..` = needed), `SEGMENTS.md` (who builds what) and `DECISIONS.md`. Prepared 2026-10-31 by the c3
director / edit planner. Quality bar = the approved intro (`review/intro_720p.mp4`, `project/intro/EDIT_NOTES.md`).

## 0. How to read this file

- **Times** = LOCAL VO seconds (`vo_c3.mp3`; full-audio = local + 1475.72), scene boundaries on word starts from
  `transcript_c3.json`. **111 scenes, C3S001–C3S111**, contiguous, 0.00 → 602.02, no gaps. Every text cue time below was
  machine-checked against the transcript's word starts; every scene's key-animation end was checked against its cut (≥ 0.5 s hold).
- **Text cue `@t`** = start of the spoken word; the text's first frame sits at `T(t) − 0.06`. Lines longer than one word are
  revealed **word by word** (each word its own literal `T()`), MANUAL §4.4.
- **Words** = the exact narration under the shot (ASR names corrected). **Why** = why the picture matches those words (§10.1.3).
- **Ground**: `NIGHT` (dark/cinematic/archival, satellite maps), `PAPER` (paper_cream + folds, or a vintage map/document/poster
  on paper; blueprint counts as PAPER), `GRID` (real graph sheet — K+E 1960 scans or Texturelabs `paper_graph_01_hires`).
  Rhythm: ≤ 3 in a row on the same ground; PAPER+GRID combined ≤ 3 in a row (checked in §11.4). **No FACE ground: no face cam
  in c3** (LONGFORM).
- **FX** = MANUAL §5 numbers + §10 craft: `W` whip (`FX.whip`, direction given), `FW` light-flash whip, `CA` cut on action,
  `HC` hard cut on action (two moving shots, §10.1.6 a), `MC` match cut, `PT` push-through, `PS` paper slide / torn wipe,
  `cont.` = same layout continues (no cut), `FH` focus hunt (`FX.focusHunt`, once per scene max), `CS` `FX.chokeSettle`.
  **No iris anywhere.** Easing `FX.ease.out/inOut/in` wrapped in `FX.choppy(…,12)`; camera `FX.ease.cam` (never posterized).
- **Hold rule (§10.9)**: each scene lists `Done` = when its key animation (route, bars, count, stamp, text) completes; the cut
  starts ≥ 0.5 s later. Cut-on-action uses the camera or a secondary motion — never an unfinished key animation.
- **Glow**: `.halate` only on the scene's **hero** (named "hero"). Everything else `.clean`. Paper never glows.
- **Ref** = intro pack `D01–D15` (`references/style-images/intro/`), original refs `R1–R12` (`references/style-images/1–12`,
  worked examples in `expected/layouts/`) — always as **variations**; or a named **Pinterest-style idea** (new layout) when
  none fits — each new idea is described in the scene and listed in §11.2.
- **Palette for c3** (lead's cross-chunk decision, LONGFORM end; `lib/palette.css` tokens only; max two accents per frame):
  - **Acts I–IV (0.00–235.94, Silicon Valley + Pan)** — c1 convention: **vermilion** = the West / Stanford / Silicon Valley /
    California; **navy** = the US East coast (New York, Field's code); **celadon** = Taiwan / Pan Wen-Yuan (from C3S037).
  - **Acts V–X (235.94–602.02, political)** — **red** (`--vermilion`) = PRC / CCP / the Soviet & Communist bloc; **celadon** =
    Taiwan / the ROC; **navy** = the United States and its allies *when a contrast is needed* (C3S051, 063, 090, 094, 095, 098,
    099); everyone else neutral (UK, UN, Japan, France: ink/bone/grey). Silicon Valley in Act V is part of the US → navy, never
    vermilion, so red means only the CCP side from 235.94 on.
  - TSMC/Morris Chang do not appear in c3 (no red-TSMC/red-PRC clash). Celadon is a fill/ring, never a text colour.
  - **yellow** = highlighter or the scene's one key number. Real flags/posters/newspapers keep their own colours and words; our
    overlay text = the narrator's words (small original Chinese of a slogan may appear as decoration under his English).
- **Spellings on screen**: IC (ASR "I see"), Silicon Valley (ASR "silicon value"), Terman (ASR "tournament"), Bill Hewlett (ASR
  "Hewitt"), Pan Wen-Yuan, Hoover Institution (he says "Institute"), David Dudley Field, Fairchild, Intel, Republic of China / ROC,
  CCP, Warsaw Pact, UN General Assembly, "your side" (ASR "site"). Everything else = his words; no text on slips (BEATS §2b).
- **Assets**: real/true images first (§10.9: copyrighted press photos, front pages, posters allowed as fair use, credited with a
  13 px on-screen credit + SOURCES.md "© owner, fair use"). Re-use allowed when the story needs it; counts in ASSETS_NEEDED.
- **Maps**: from `assets/maps/kit/` (to be built — N05; Natural Earth II-class relief, sharp satellite close-ups, vintage colour atlas
  plates); s02 satellite US is the quality bar. **Never** the flat grey/beige relief of the intro. Fallbacks named per scene.
- **Papers**: Texturelabs `_hires` papers for full-frame grounds; K+E/ledger scans only as cards at ≤ native size; two paper
  layers (top ~90 %) on document scenes (§10.6.1); never the same paper in consecutive paper scenes.
- **SFX** lines are object events (local VO s) → `compositions/c3sNN.sfx.json` (vocabulary SEGMENTS §3.4). The sound pass
  applies the §10.8 restraint (hero per scene + moves).

## 1. Act I — How big it was (0.00–26.47)
Music: continue c2's bed (marimba/pulse family of the intro); lift on "the world" 5.44 and "Silicon Valley" 25.51.

### C3S001 · 0.00–2.32 · C3B001 · NIGHT
- **Words** "I don't think I'm completely explaining how big it was."  **Why** 'how big it was' — the IC (last chunk's subject) seen at macro, then pulled back to show its scale.
- **FX** #1 footage + #16 plate (fringe, CA 0.12) + #13 rise · **Ref** — (c2 hand-off; continues c2's chip look)
- **Visual** E01 die-pattern macro, camera pulls back 1.6→1.0 so the die repeats into a full wafer ('how big'). Short scene: the text uses a quick 0.3 s rise (exception to the long-ease rule, noted).
- **Assets** E01
- **Text** `how big` t-serif-i clean: `how`@1.52 `big`@1.68 (sizes up 1.0→1.15 as it lands).
- **Camera** pull-back (FX.ease.cam) ending 2.0. **Out** `MC` @2.32 — the wafer's round edge becomes the Earth's limb in C3S002
- **Done** key animation complete @1.80 (cut @2.32; hold 0.52 s).
- **SFX** 0.00 air_swell (J-cut from c2) · 1.50 whoosh_soft

### C3S002 · 2.32–7.04 · C3B001 · NIGHT
- **Words** "Like the world wouldn't exist without **IC,** the world we are in right now."  **Why** 'the world wouldn't exist without IC, the world we are in right now' → the modern, lit-up world (city lights = electronics).
- **FX** #15 cutting-the-curve (die → night Earth) + FH after landing · **Ref** variation of intro IS005 (wafer→Blue Marble) — here IC → Black Marble night lights
- **Visual** IC die close-up (N01 Fairchild planar IC photo) zooms (expo.inOut, the one allowed use) and cuts at peak velocity 4.90 into NASA Black Marble Earth at night (N02); FH 5.6.
- **Assets** N01, N02
- **Text** `IC` label-box @4.56 (ASR 'I see') · `the world` hero halate: `the`@5.28 `world`@5.44.
- **Camera** zoom in 2.32→4.9, settle 4.9→6.0, drift east. **Out** `CA` @7.04 — the globe keeps rotating while C3S003's screen slides in
- **Done** key animation complete @6.00 (cut @7.04; hold 1.04 s).
- **SFX** 4.88 whoosh_big (curve) · 5.42 boom_low (very soft)

### C3S003 · 7.04–10.08 · C3B002 · NIGHT
- **Words** "This podcast that's like changing your guys' lives."  **Why** 'This podcast…' → the podcast itself playing on a period screen (a chip-powered device).
- **FX** #11 screen (IBM 5154 monitor) + #13 count (progress timer) · **Ref** variation of intro IS062 progress-bar motif; screen per §10.1.7
- **Visual** E03 IBM 5154 monitor (keyed screen); inside, a typeset Searching Lessons player (N03 🛠): waveform + progress bar 4:26:14 (intro motif). CRT power-on @7.10.
- **Assets** E03, N03
- **Text** `this podcast` t-label inside the player: `this`@7.04 `podcast`@7.36 · `lives` serif-i @9.44.
- **Camera** slow push 1.0→1.08. **Out** `PT` @9.6 — camera pushes into the screen, its glow fills frame
- **Done** key animation complete @9.40 (cut @10.08; hold 0.68 s).
- **SFX** 7.06 crt_click · 7.1 crt_hum (dur 2.9) · 9.6 whoosh

### C3S004 · 10.08–15.68 · C3B003 · PAPER
- **Words** "All the videos I have made for people who have seen my other videos wouldn't exist without Silicon Valley."  **Why** 'All the videos I have made… wouldn't exist without Silicon Valley' → his video cards vanish, Silicon Valley is the reason.
- **FX** #12 collage cards (12 fps pinning) + #13 + PS reveal · **Ref** Pinterest idea 'video-thumbnail contact sheet on paper' + D07 variation
- **Visual** Grid of 9 ink video cards (play triangle, progress bar) pins in at 12 fps @10.64; on 'wouldn't exist' 13.68 cards fade to dashed empty outlines; @14.72 they slide apart revealing the pictorial Stanford-peninsula map E07 (colour).
- **Assets** E07 (painting/pictorial map), N03 card style
- **Text** `videos`@10.64 serif-i · `wouldn't exist`@13.68 `exist`@14.08 (crossed by pen) · `SILICON VALLEY` label-box vermilion: `Silicon`@14.72 `Valley`@15.28.
- **Camera** static → push 1.0→1.06 on the map. **Out** `CA` @15.68 — map keeps pushing as C3S005's page slides over it
- **Done** key animation complete @15.10 (cut @15.68; hold 0.58 s).
- **SFX** 10.62 paper_slide · 13.66 paper_rustle · 14.70 paper_slide

### C3S005 · 15.68–21.43 · C3B004 · PAPER
- **Words** "So I think. Yeah, if you enjoyed my videos, you have silicon to thank,"  **Why** 'you have silicon to thank' → the element silicon on a period periodic table, circled.
- **FX** #5 document (tilted page) + #19 pen circle + FX.textCallout · **Ref** Pinterest idea 'vintage textbook periodic table, pencil circle'
- **Visual** N04 1950s periodic-table page tilts in (rotateX 12°); one video card from S004 shrinks into the corner on 'enjoyed my videos' (18.07); pen circle on the Si cell @20.23; text callout dims the rest.
- **Assets** N04
- **Text** `enjoyed`@18.07 t-label small · `silicon`@20.23 serif-i · `to thank`: `to`@20.95 `thank`@21.11.
- **Camera** push to Si cell 1.0→1.6 (cam ease), FH @20.8. **Out** `W` ↓ @21.37
- **Done** key animation complete @20.90 (cut @21.43; hold 0.53 s).
- **SFX** 15.70 paper_slide · 20.21 pencil_scribble · 21.35 whoosh

### C3S006 · 21.43–26.47 · C3B005 · NIGHT
- **Words** "or **IC** uh integrated circuit to thank for it. So that's how we get Silicon **Valley.**"  **Why** 'or IC, integrated circuit… that's how we get Silicon Valley' → a real IC, its silicon die becomes the valley.
- **FX** #1 + #16 + PT (die grid → aerial street grid) · **Ref** Pinterest idea 'macro chip die dissolving into city grid' (match on pattern)
- **Visual** N01 IC photo under lamp (2nd use, different crop: package + die); camera pushes into the die grid @24.6 which match-dissolves into E08 Silicon Valley aerial (orchard/street grid).
- **Assets** N01, E08
- **Text** `IC` label-box @21.59 · `integrated circuit`: `integrated`@22.47 `circuit`@23.03 · `SILICON VALLEY` hero halate, one line landing on its first word: `Silicon`@25.51 (Valley@26.07 already visible).
- **Camera** push 1.0→2.4 then settle on aerial. **Out** `PS` @26.47 — lined paper slides up over the aerial
- **Done** key animation complete @25.95 (cut @26.47; hold 0.52 s).
- **SFX** 21.45 whoosh_soft · 24.6 whoosh_big · 25.49 boom_low

## 2. Act II — The California law (26.47–120.58)
Music: investigative pizzicato/pulse ostinato; tick texture under the documents; small sting on ILLEGAL 76.47; ease off at 105.54.

### C3S007 · 26.47–32.63 · C3B006 · PAPER
- **Words** "There's another argument here that's kind of debated, but I'll say it because I agree with it."  **Why** 'another argument… debated… I agree with it' → a legal pad with the argument and his tick.
- **FX** #18 rough reveal (CS) + #19 pen tick + two paper layers (§10.6.1) · **Ref** Pinterest idea 'yellow legal-pad notes with pencil ticks'
- **Visual** Lined paper (paper_lined_01_hires) over paper_cream at 90 %; handwritten-style serif heading slots in; pencil double underline under 'debated'; tick ✓ @31.75.
- **Assets** E27 papers
- **Text** `another argument`: `another`@26.79 `argument`@27.27 (CS) · `debated`@29.35 (pencil underline) · `I agree`: `I`@31.59 `agree`@31.75 + ✓.
- **Camera** drift down 30 px. **Out** `CA` @32.6 — camera tilt continues into C3S007's map push
- **Done** key animation complete @32.10 (cut @32.63; hold 0.53 s).
- **SFX** 26.49 paper_slide · 29.33 pencil_scribble · 31.73 marker_scratch

### C3S008 · 32.63–37.19 · C3B007 · NIGHT
- **Words** "And that argument is how much of a role did California law play in it?"  **Why** 'how much of a role did California law play' → California isolated on the US, with the question.
- **FX** #3 satellite map (s02 look) + #20 contrast call-out (§10.6.3) + FH · **Ref** R12 variation (region lit) on the s02 satellite basemap
- **Visual** Map kit US night satellite (N05/E18); ease-in push west; contrast call-out cuts on the push's peak @35.11: CA stays sharp + vermilion overlay 0.6, rest veiled.
- **Assets** N05 (map kit US), E18 fallback
- **Text** `CALIFORNIA LAW` hero halate: `California`@35.11 `law`@35.83 (no extra '?' glyph — the push itself asks).
- **Camera** push to CA 1.0→2.2, FH @35.5. **Out** `W` → @37.13 (whip continues the westward push into the atlas)
- **Done** key animation complete @36.40 (cut @37.19; hold 0.79 s).
- **SFX** 35.09 circuit_clunk (contrast) · 37.11 whoosh

### C3S009 · 37.19–42.55 · C3B008 · PAPER
- **Words** "Because California is an exception in terms of how the law across the United States works,"  **Why** 'California is an exception… how the law across the United States works' → every state the same, CA different.
- **FX** #3 vintage colour atlas + watercolour state fills (R11 variation) · **Ref** R11 variation — on a vintage colour-atlas plate (not flat beige; §10.9)
- **Visual** Vintage atlas US plate (N05 kit 'atlas' style); 47 states fill ink-hatch at 12 fps west→east 'across' @40.95; California stays vermilion watercolour.
- **Assets** N05, E37 state shapes
- **Text** `exception` serif-i @38.79 next to CA · `UNITED STATES` t-label @41.43.
- **Camera** slow pull 1.15→1.0. **Out** `PS` @42.49 (the contract page slides over the atlas)
- **Done** key animation complete @41.90 (cut @42.55; hold 0.65 s).
- **SFX** 37.21 whoosh_soft · 40.9 dot_ticks (fill, dur 0.8) · 42.47 paper_slide

### C3S010 · 42.55–46.71 · C3B009 · PAPER
- **Words** "where you can you cannot actually enforce a non-compete inside of California."  **Why** 'you cannot actually enforce a non-compete inside of California' → a non-compete clause highlighted and struck through.
- **FX** #18 highlighter (body text) + #19 pen cross + §10.6.4 text call-out · **Ref** Pinterest idea 'redlined contract'
- **Visual** Typeset employment agreement (N06 🛠, generic, no logos) on two paper layers; highlighter swipe on the clause line 'NON-COMPETE' @44.87; pen X over the clause @45.67; small CA outline stamp-free label.
- **Assets** N06
- **Text** `cannot`@43.43 `enforce`@44.23 t-label · highlight `non-compete` @44.87 · `California` t-label vermilion @46.07.
- **Camera** punch-in 10 % on the clause (textCallout). **Out** `CA` @46.71 — the page slides left while C3S010's map slides in
- **Done** key animation complete @46.20 (cut @46.71; hold 0.51 s).
- **SFX** 44.85 highlighter_swipe · 45.65 marker_scratch

### C3S011 · 46.71–50.55 · C3B010 · NIGHT
- **Words** "That's not the case outside of it, at least in most important states."  **Why** 'not the case outside of it… most important states' → other big states light up as enforcing.
- **FX** #3 satellite map + #20 callouts (pins + leader labels) · **Ref** R11 leader-label idea on the night satellite map (continuity with C3S008)
- **Visual** Same US night map, wider; CA dims; NY, MA, TX, IL, NJ glow bone outlines + pins at 12 fps from @48.87.
- **Assets** N05/E18
- **Text** `outside`@47.51 t-label · `most important states`: `most`@48.87 `important`@49.35 `states`@49.91.
- **Camera** pull-back 1.4→1.0. **Out** `W` ← @50.49
- **Done** key animation complete @50.00 (cut @50.55; hold 0.55 s).
- **SFX** 47.49 whoosh_soft · 48.85 map_pin ×5 (soft)

### C3S012 · 50.55–54.23 · C3B011 · NIGHT
- **Words** "But uh basically, and how it came about is also an interesting story where"  **Why** 'how it came about is also an interesting story' → the story's object: an old law book on a desk, about to open.
- **FX** #5 document on dark desk + R9 lamp pool · **Ref** R9 lamp-pool lighting variation (no cork)
- **Visual** N08 'Draft of a Civil Code for the State of New York' (1865) — cloth cover/title page, lamp clicks on @50.6, cover opens to the title page @53.5.
- **Assets** N08
- **Text** `interesting story` serif-i clean: `interesting`@53.11 `story`@53.51.
- **Camera** slow push 1.0→1.1. **Out** `CA` @54.23 — the page turning carries into C3S012
- **Done** key animation complete @53.70 (cut @54.23; hold 0.53 s).
- **SFX** 50.57 lamp_click · 53.4 page_turn

### C3S013 · 54.23–59.35 · C3B012 · PAPER
- **Words** "some guy named David Dudley Field wrote a legal code for New York, right?"  **Why** 'some guy named David Dudley Field wrote a legal code for New York' → his portrait, his code, New York.
- **FX** #10 Vox layered panels + #12 torn edges · **Ref** s09/intro IS002 'cut-out over tinted panels' variation (navy = East/New York)
- **Visual** N07 Field (Brady-Handy) cut-out, halftone, ink duotone; panels slide behind at 12 fps: code title page N08 @57.35, 1860s New York engraving panel tinted navy @58.15.
- **Assets** N07, N08, N09
- **Text** `DAVID DUDLEY FIELD` label-box ink: `David`@55.19 `Dudley`@55.67 `Field`@56.39 · `legal code`@57.35 `code`@57.75 · `New York` t-label navy @58.15.
- **Camera** drift right 40 px. **Out** `PS` @59.29 — the code page slides down onto C3S013's map
- **Done** key animation complete @58.80 (cut @59.35; hold 0.55 s).
- **SFX** 55.17 paper_slide · 57.33 paper_slide · 58.13 pop_soft

### C3S014 · 59.35–63.03 · C3B013 · PAPER
- **Words** "But New York never actually adopted that code, they went with something else,"  **Why** 'New York never actually adopted that code' → the code laid on New York and crossed out.
- **FX** #3 old map (D09) + #19 pen cross + #20 map call-out · **Ref** D09 old city map — 1860s New York map (navy tint)
- **Visual** N09 1860s New York map (D09 look, tilted 8°); the code title card drops onto it; pen X across the card @60.71; card slides off-frame left 'went with something else' @62.23.
- **Assets** N09, N08
- **Text** `never`@60.15 `adopted`@60.71 t-label.
- **Camera** static, slight tilt. **Out** `W` ← @62.97 (follows the card)
- **Done** key animation complete @62.40 (cut @63.03; hold 0.63 s).
- **SFX** 59.37 paper_slide · 60.69 marker_scratch · 62.95 whoosh

### C3S015 · 63.03–68.63 · C3B014 · PAPER
- **Words** "but California ended up adopting for some reason, just copy pasted the whole thing, right?"  **Why** 'California ended up adopting… copy pasted the whole thing' → the code travels NY→California and is copied whole.
- **FX** #3 D10 tilted vintage map + yellow marker route + photocopy light-bar · **Ref** D10 tilted close-up map with route (R10 yellow marker)
- **Visual** E17 Rand McNally US map tilted (rotateX 28°, rotateZ −6°), lens blur far edge; yellow marker route draws NY→CA @63.27 (done 64.9); on 'copy' a scanner light-bar sweeps the card and an identical copy slides out @66.39.
- **Assets** E17, N08
- **Text** `California` t-label vermilion @63.27 · `copy`@66.39 `pasted`@66.87.
- **Camera** track west along the route (cam ease). **Out** `FW` @68.57
- **Done** key animation complete @67.80 (cut @68.63; hold 0.83 s).
- **SFX** 63.25 marker_long (dur 1.5) · 66.37 scanner_sweep→tone_blip · 68.55 whoosh

### C3S016 · 68.63–75.27 · C3B015 · NIGHT
- **Words** "And in this code, one of the laws said that you cannot contract someone out of a lawful profession."  **Why** 'one of the laws said you cannot contract someone out of a lawful profession' → the actual 1872 California Civil Code section.
- **FX** #5 tilted 3D page + §10.6.4 text call-out + #18 highlighter (body text) + FH · **Ref** s06 newspaper treatment on a document; Pinterest idea 'law-book macro, one line lit'
- **Visual** N10 California Civil Code 1872, §1673 page ('Every contract by which any one is restrained from exercising a lawful profession… is to that extent void'), sepia on dark desk; text call-out isolates that sentence; highlighter on 'lawful profession' @73.83.
- **Assets** N10
- **Text** `one of the laws` t-label: `one`@69.91 `laws`@70.39 · highlight on page @73.83.
- **Camera** ease-in push to the paragraph, FH @71.0. **Out** `HC` @75.27 — hard cut on the continuing push
- **Done** key animation complete @74.60 (cut @75.27; hold 0.67 s).
- **SFX** 68.65 page_turn · 73.81 highlighter_swipe

### C3S017 · 75.27–82.10 · C3B016 · PAPER
- **Words** "Like a contract is illegal. If it says, hey, you cannot work in this field afterwards."  **Why** 'a contract is illegal if it says you cannot work in this field afterwards' → that contract, stamped ILLEGAL, the clause typed.
- **FX** #13 typewriter + stamp + D08 telegram-style typed card · **Ref** D08 telegram variation (typed form, rubber stamp)
- **Visual** Typed contract form (N06 🛠 variant, ruled) slides in @75.75; red-ink-free ink stamp ILLEGAL lands @76.47 (done 77.1); camera pans down to the clause which types word by word.
- **Assets** N06
- **Text** `contract`@75.75 · stamp `ILLEGAL` @76.47 · typed: `you`@78.74 `cannot`@78.98 `work`@79.78 `in`@80.26 `this`@80.42 `field`@80.66 `afterwards`@81.06.
- **Camera** pan down 1.0 s @77.4. **Out** `CA` @82.10 — pan continues as the TV slides in
- **Done** key animation complete @81.50 (cut @82.10; hold 0.60 s).
- **SFX** 75.73 paper_slide · 76.45 stamp_thud · 78.7 letter_ticks (dur 2.8)

### C3S018 · 82.10–86.90 · C3B017 · NIGHT
- **Words** "And yeah, that's an interesting one. I think a Silicon Valley TV show has an episode on this too."  **Why** 'a Silicon Valley TV show has an episode on this' → the HBO show on a TV.
- **FX** #11 TV (Sony Trinitron) + CRT power-on · **Ref** §10.1.7 screens — Trinitron KV-1320
- **Visual** E04 Trinitron, CRT on @83.94; screen plays N11 HBO 'Silicon Valley' title card/still (© HBO, fair use, credit).
- **Assets** E04, N11
- **Text** `TV show` t-label: `TV`@84.74 `show`@85.06 · `episode`@85.46 serif-i.
- **Camera** slow push. **Out** `CRT-off` line @86.90 (the image collapses to a line, the next board fades up)
- **Done** key animation complete @86.30 (cut @86.90; hold 0.60 s).
- **SFX** 83.92 crt_click · 83.95 crt_hum (dur 2.9) · 86.85 crt_off

### C3S019 · 86.90–90.74 · C3B018 · NIGHT
- **Words** "But that makes a lot of things possible that we have already talked about, right?"  **Why** 'that makes a lot of things possible that we have already talked about' → a board of the things we already covered.
- **FX** R9 cork board + #12 pinned cards + red string · **Ref** R9 cork board (c1 'mind palace' variation — new pins)
- **Visual** E28 cork + lamp pool; pinned (12 fps): E10 Terman, E14 Hewlett & Packard, E16 HP garage, E13 Stanford quad, E08 aerial; red string draws between them @88.90.
- **Assets** E28, E10, E14, E16, E13, E08
- **Text** `possible`@88.90 serif-i · `already talked about`: `already`@89.70 `talked`@90.02 `about`@90.18.
- **Camera** push in 1.0→1.15. **Out** `W` ↑ @90.68
- **Done** key animation complete @90.10 (cut @90.74; hold 0.64 s).
- **SFX** 86.92 pin_pop ×5 (12 fps) · 88.88 string_draw→marker_long · 90.66 whoosh

### C3S020 · 90.74–94.66 · C3B019 · NIGHT
- **Words** "Fairchild doesn't get born if it wasn't for this law, maybe."  **Why** 'Fairchild doesn't get born if it wasn't for this law' → the Fairchild founders (the eight), Fairchild logo.
- **FX** #17 2.5D (eight men) + #4 + #8 streaks behind · **Ref** 2.5D variation (s10 / 2.5D-campus) — portrait group
- **Visual** N12 'traitorous eight' photo cut into layers (backdrop, back row, front row, foreground) — dolly in; N13 Fairchild logo tucked behind the men @90.74.
- **Assets** N12 (+layers), N13
- **Text** `FAIRCHILD` hero halate @90.74 · `this law` t-label: `this`@93.38 `law`@93.78.
- **Camera** dolly z −80→150, x drift. **Out** `CA` @94.66 (dolly continues as the tree draws down)
- **Done** key animation complete @94.10 (cut @94.66; hold 0.56 s).
- **SFX** 90.72 air_swell · 92.0 whoosh_soft (dolly)

### C3S021 · 94.66–101.94 · C3B020 · GRID
- **Words** "People say that we're gonna have many things down the line that I created like Intel if wasn't for this."  **Why** 'many things down the line… like Intel' → a family tree from Fairchild running down the page to Intel.
- **FX** #2 diagram (lines drawn on, nodes pop 12 fps) + logo · **Ref** D15 relationship diagram variation + Pinterest idea: 1969 SEMI 'Silicon Valley Genealogy' chart (N15, reference only)
- **Visual** K+E graph sheet (hires) + paper_cream; Fairchild node top; ink branch lines draw downward @96.98 'down the line'; Intel node (N14 1968 logo) pops @98.90; other nodes are unnamed dots (narrator names only Intel).
- **Assets** N13, N14, N15 (ref), E27
- **Text** `down the line`: `down`@96.98 `the`@97.22 `line`@97.30 · `INTEL` (logo) @98.90.
- **Camera** tilt down following the branch. **Out** `cont.` @101.94 (same sheet, camera pulls back)
- **Done** key animation complete @99.60 (cut @101.94; hold 2.34 s, continues — no cut).
- **SFX** 96.96 pencil_scribble (dur 1.0) · 98.88 pop_soft

### C3S022 · 101.94–105.54 · C3B021 · GRID
- **Words** "So yeah, a lot of things are born because of this."  **Why** 'a lot of things are born because of this' → the tree keeps sprouting nodes.
- **FX** #2 + 12 fps sprouting (dot_ticks) · **Ref** D15 / genealogy (continued)
- **Visual** Same sheet pulled back 1.0→0.6: dozens of branch nodes sprout at 12 fps from every node @104.02.
- **Assets** as C3S021
- **Text** `born` serif-i @104.02.
- **Camera** pull back (cam ease). **Out** `W` ↓ @105.48
- **Done** key animation complete @104.90 (cut @105.54; hold 0.64 s).
- **SFX** 104.0 dot_ticks (dur 0.8) · 105.46 whoosh

### C3S023 · 105.54–109.06 · C3B022 · NIGHT
- **Words** "But some people do argue maybe this wasn't that big a deal, especially at the beginning."  **Why** 'some argue it wasn't that big a deal, especially at the beginning' → a chart of the law's role, flat at the start.
- **FX** #2 dark line chart over ghost map + SVG draw-on · **Ref** D13 dark line chart over a ghost California map
- **Visual** Ghost California outline (bone 8 %), axis draws; a vermilion line runs flat along the bottom; 'beginning' bracket @108.66. No values (DECISIONS #2).
- **Assets** N05 CA outline
- **Text** `argue`@106.42 t-label · `wasn't that big a deal`: `wasn't`@107.22 `that`@107.46 `big`@107.62 `a`@107.86 `deal`@107.94 · `beginning`@108.66.
- **Camera** slow push. **Out** `cont.` @109.06 (line keeps drawing)
- **Done** key animation complete @108.90 (cut @109.06; hold 0.16 s, continues — no cut).
- **SFX** 105.56 tone_blip · 106.0 tick_soft (line, dur 2.6)

### C3S024 · 109.06–114.66 · C3B023 · NIGHT
- **Words** "Down the line is gonna play a bigger role when companies are bigger and people want to leave these big companies to go to other companies."  **Why** 'down the line a bigger role… people want to leave big companies for other companies' → line rises; people icons hop from a big block to others.
- **FX** #2 line + isotype people (12 fps hops) · **Ref** D13 continued + R5 pictogram hop (c1 graduates motif)
- **Visual** Line curves up steeply @109.94; under it a big ink block 'big companies' and small blocks; graduate/person icons hop from the big block to small ones @112.34.
- **Assets** E34 icons
- **Text** `bigger role`: `bigger`@110.18 `role`@110.42 · `leave`@112.34 t-label.
- **Camera** track right with the line. **Out** `PS` @114.60
- **Done** key animation complete @113.90 (cut @114.66; hold 0.76 s).
- **SFX** 109.9 tick_soft (dur 1.0) · 112.32 dot_slide ×4 · 114.58 paper_slide

### C3S025 · 114.66–120.58 · C3B024 · PAPER
- **Words** "But at the start, maybe it didn't play a role. That's what people say or argue online, but I think it did. I think it did."  **Why** 'people say or argue online… but I think it did. I think it did.' → online comment cards vs his own ticked answer.
- **FX** #12 cards + #19 pen underline/tick · **Ref** Pinterest idea 'forum comments printed as paper slips'
- **Visual** Three typeset comment slips (anonymous avatars, no real usernames) pin in; then his line is pen-written large and underlined.
- **Assets** 🛠 typeset
- **Text** `didn't play a role`: `didn't`@115.86 `play`@116.02 `a`@116.18 `role`@116.26 · `online`@117.94 · `I think it did`: `I`@118.82 `think`@118.98 `it`@119.14 `did`@119.30 (pen underline).
- **Camera** drift. **Out** `FW` @120.52
- **Done** key animation complete @119.90 (cut @120.58; hold 0.68 s).
- **SFX** 115.84 paper_slide · 118.8 pencil_scribble · 120.5 whoosh

## 3. Act III — Terman steps down, Hoover, the recipe (120.58–179.37)
Music: sustained pad, reflective; humour lift 159–168; resolve on "recipe" 169.13.

### C3S026 · 120.58–124.98 · C3B025 · NIGHT
- **Words** "But nonetheless, 1965 **Terman** steps down."  **Why** '1965 Terman steps down' → the year, then Terman's portrait literally stepping down out of frame.
- **FX** #13 odometer + #4 hero + #8 streaks · **Ref** variation of intro IS001 year card (here digits roll down)
- **Visual** Streaks on night; `1965` odometer; E10 Terman portrait card (sepia) below it slides DOWN and dims @124.02 (0.43 s move, done 124.45).
- **Assets** E10 (or N16 1960s Terman)
- **Text** `1965` hero halate odometer lock @122.34 · `TERMAN` label @123.46 · `steps down`: `steps`@124.02 `down`@124.42.
- **Camera** push 1.0→1.04. **Out** `CA` @124.98 (portrait still sliding)
- **Done** key animation complete @124.45 (cut @124.98; hold 0.53 s).
- **SFX** 122.3 odometer_tick · 124.0 whoosh_soft

### C3S027 · 124.98–129.62 · C3B026 · PAPER
- **Words** "He has done everything that he doesn't even realize at that time how big it's gonna be,"  **Why** 'He has done everything… doesn't realize how big it's gonna be' → a collage of what Terman built, ticked off.
- **FX** #12 collage (D07 poster) + #19 ticks · **Ref** D07 collage poster variation (photos + typographic box + stamps)
- **Visual** D07 layout: photos E13 Stanford quad, E16 HP garage, N17 Stanford Industrial Park, E15 Hewlett; pen ticks pop on each @125.78; typographic box asks 'how big'.
- **Assets** E13, E16, N17, E15
- **Text** `everything`@125.78 · `how big`: `how`@128.66 `big`@128.82 (typographic box).
- **Camera** slow pan. **Out** `W` → @129.56
- **Done** key animation complete @129.00 (cut @129.62; hold 0.62 s).
- **SFX** 125.0 paper_slide ×3 · 125.76 marker_scratch ×4 · 129.54 whoosh

### C3S028 · 129.62–136.90 · C3B027 · NIGHT
- **Words** "because in 65, of course, Silicon Valley is important, of course, it's growing, there has a lot of cool stuff, a lot of important companies,"  **Why** 'in '65 Silicon Valley is important, growing… a lot of important companies' → a 1960s aerial with companies circled.
- **FX** #16 plate + #19 markups (circles) + markup-map · **Ref** markup-map (SC064) + D14 district highlight variation on a 1960s aerial
- **Visual** N17 1960s Stanford Industrial Park / Santa Clara Valley aerial, sepia; vermilion rough circles on 3 company sites at 12 fps @135.78; slow push.
- **Assets** N17
- **Text** `'65` t-label @129.94 · `growing`@133.30 serif-i · `important companies`: `important`@135.78 `companies`@136.18.
- **Camera** push 1.0→1.12. **Out** `CA` @136.90
- **Done** key animation complete @136.30 (cut @136.90; hold 0.60 s).
- **SFX** 129.64 projector_click · 135.76 marker_scratch ×3

### C3S029 · 136.90–142.17 · C3B028 · PAPER
- **Words** "but it's like. Nowhere close to what it's gonna become. It's gonna become like a behemoth in the cell."  **Why** 'nowhere close to what it's gonna become… a behemoth' → a small 1965 bar vs a giant bar running off the page.
- **FX** #2 bars (D01) + halftone cut-out + label-box · **Ref** D01 (R1) bars + dashed threshold + halftone object — variation: 2 bars, the 2nd breaks the frame
- **Visual** Paper; bar '’65' short (dashed threshold at its top); bar 2 rises past the top of frame @138.09; halftone cut-out of modern Silicon Valley (E09) at the base; label-box BEHEMOTH @140.73. Shapes only.
- **Assets** E09 (halftone cut-out)
- **Text** `’65` t-label under bar 1 · `nowhere close`: `Nowhere`@138.09 `close`@138.49 · `BEHEMOTH` label-box @140.73.
- **Camera** tilt up following bar 2. **Out** `FW` @142.11
- **Done** key animation complete @141.50 (cut @142.17; hold 0.67 s).
- **SFX** 138.07 dot_ticks (bar, dur 1.2) · 140.71 pop_soft · 142.09 whoosh

### C3S030 · 142.17–146.65 · C3B029 · NIGHT
- **Words** "I think Hoover also gets some credit because he set up a lot of things that we didn't really talk about."  **Why** 'Hoover also gets some credit' → a colour painting of Herbert Hoover (§10.5).
- **FX** #16 painting plate + #4 hero · **Ref** §10.5 painting as B-roll
- **Visual** N18 Hoover portrait painting (colour), fringe blur + slow push.
- **Assets** N18 (fallback E11)
- **Text** `HOOVER` hero halate @142.41 · `credit` t-label @143.69.
- **Camera** push 1.0→1.06. **Out** `PS` @146.59
- **Done** key animation complete @144.30 (cut @146.65; hold 2.35 s).
- **SFX** 142.19 air_swell · 146.57 paper_slide

### C3S031 · 146.65–154.81 · C3B030 · PAPER
- **Words** "One of the important one being Stanford could not legally, I think, charge tuition, which would have made it like impossible to continue other stuff he did."  **Why** 'Stanford could not legally charge tuition… impossible to continue' → Stanford + an empty TUITION bar that cannot move + 'impossible'.
- **FX** #2 R6 bars + #18 highlighter + #19 pen · **Ref** R6 variation (c1 'revenue model' tuition bars) — here one bar locked at zero
- **Visual** Paper; Stanford quad card E13 (2nd use) top-left; serif title; one empty bar 'TUITION' with a padlock-free pen X when it fails to fill @149.93; pen scribble 'impossible' @152.49.
- **Assets** E13
- **Text** `could not legally`: `could`@148.65 `not`@148.81 `legally`@149.05 · `charge tuition`: `charge`@149.93 `tuition`@150.41 (highlighter) · `impossible`@152.49.
- **Camera** drift. **Out** `W` ↑ @154.75
- **Done** key animation complete @153.20 (cut @154.81; hold 1.61 s).
- **SFX** 149.91 highlighter_swipe · 152.47 pencil_scribble · 154.73 whoosh

### C3S032 · 154.81–159.13 · C3B031 · NIGHT
- **Words** "And if you're into history, if you're into geopolitics, you know the Hoover Institute,"  **Why** 'history… geopolitics… the Hoover Institution' → Hoover Tower, the institution's home.
- **FX** #17 2.5D (tower vs sky) + #8 haze · **Ref** 2.5D-quad variation (tower)
- **Visual** N19 Hoover Tower ≥3000 px cut into sky / tower / trees foreground; dolly; title tucked behind the tower.
- **Assets** N19 (+layers)
- **Text** `history`@155.93 t-label · `geopolitics`@157.05 · `HOOVER INSTITUTION` hero halate @158.17 (accurate name; narrator says 'Institute').
- **Camera** dolly up. **Out** `CA` @159.13
- **Done** key animation complete @158.60 (cut @159.13; hold 0.53 s).
- **SFX** 155.0 air_swell · 158.15 boom_low (soft)

### C3S033 · 159.13–165.45 · C3B032 · PAPER
- **Words** "which is still going to this day, probably the best institute in the world. Very good, very good, at least."  **Why** 'still going to this day… the best institute in the world. Very good, very good at least' → pen writes 'the best', strikes it, writes 'very good' (his self-correction).
- **FX** #19 pen write/strike + photo card · **Ref** Pinterest idea 'editor's pen correction on a photo caption'
- **Visual** N20 Hoover Institution Library & Archives photo card on paper; caption line under it; pen writes `best` @161.77, strikes it @163.53, writes `very good`.
- **Assets** N20
- **Text** `to this day`: `to`@159.93 `this`@160.09 `day`@160.25 · `best`@161.77 (pen) · `very good`: `Very`@163.53 `good`@163.85.
- **Camera** push 1.0→1.05. **Out** `FW` @165.39
- **Done** key animation complete @164.60 (cut @165.45; hold 0.85 s).
- **SFX** 161.75 pencil_scribble · 163.51 marker_scratch · 165.37 whoosh

### C3S034 · 165.45–168.57 · C3B033 · NIGHT
- **Words** "I like their videos. If you like to get good historians,"  **Why** 'I like their videos… historians' → a Hoover Institution video playing on a projector screen.
- **FX** #11 screen (projector + pull-down screen, new set) + #14 flicker · **Ref** §10.1.7 'projector screen' (new screen type)
- **Visual** N22 pull-down screen; projector beam with dust motes; N21 Hoover Institution video still projected (© fair use, credit).
- **Assets** N22, N21
- **Text** `their videos`: `their`@165.77 `videos`@166.01 · `historians`@167.61 serif-i.
- **Camera** static, slight zoom. **Out** `PS` @168.51
- **Done** key animation complete @168.00 (cut @168.57; hold 0.57 s).
- **SFX** 165.47 projector_loop (dur 3.1) · 168.49 paper_slide

### C3S035 · 168.57–174.17 · C3B034 · PAPER
- **Words** "this is the recipe, right? A great university, company, industrial park, people coming in and out,"  **Why** 'this is the recipe: a great university, company, industrial park, people coming in and out' → a typed recipe card, each ingredient as named.
- **FX** #12 photo chips + #13 typewriter + #19 ticks · **Ref** Pinterest idea 'vintage typed recipe index card' (new layout)
- **Visual** N23 recipe card (ruled index card, typed header RECIPE); each line types + a small photo chip pins: E13 Stanford, E14 HP, N17 park, arrows in/out for people.
- **Assets** N23, E13, E14, N17
- **Text** `recipe` header @169.13 · `university`@170.49 · `company`@171.21 · `industrial park`: `industrial`@171.85 `park`@172.41 · `people`@172.97 · `in and out`: `in`@173.53 `and`@173.69 `out`@173.85.
- **Camera** tilt down the card. **Out** `cont.` @174.17 (card flips over)
- **Done** key animation complete @173.60 (cut @174.17; hold 0.57 s, continues — no cut).
- **SFX** 169.11 letter_ticks (dur 0.5) · 170.47/171.19/171.83/172.95 pin_pop

### C3S036 · 174.17–179.37 · C3B035 · PAPER
- **Words** "and yeah, where we think uh Silicon Valley was built by someone, which is interesting."  **Why** 'Silicon Valley was built by someone' → a blueprint of Silicon Valley with the builder's name box.
- **FX** blueprint ground + line draw-on + #18 CS · **Ref** variation of intro IS037 blueprint
- **Visual** paper_blueprint_01_hires; 'SILICON VALLEY' drawn as a plan (title block, dimension lines) @175.61; title-block field 'BUILT BY' with an empty box that fills with a small Terman circle (E10) @177.77.
- **Assets** E27 blueprint, E10
- **Text** `Silicon Valley`: `Silicon`@175.61 `Valley`@176.17 · `built`@176.89 · `by someone`: `by`@177.53 `someone`@177.77.
- **Camera** slow push. **Out** `FW` @179.31
- **Done** key animation complete @178.60 (cut @179.37; hold 0.77 s).
- **SFX** 175.59 pencil_scribble (dur 1.2) · 177.75 pop_soft · 179.29 whoosh

## 4. Act IV — The Taiwan connection: Pan Wen-Yuan (179.37–235.94)
Music: new melodic layer (Melting Glass family) from 179.37; swell on "Pan Wen-Yuan" 188.09; darken from 228.34.

### C3S037 · 179.37–182.01 · C3B036 · NIGHT
- **Words** "Now we already have a Taiwan connection here because"  **Why** 'we already have a Taiwan connection' → Stanford (vermilion) and Taiwan (celadon) joined by a line across the Pacific.
- **FX** #3 map + line draw + pins · **Ref** D13 ghost map variation (Pacific)
- **Visual** Map kit Pacific relief night (E21/N05); Stanford pin vermilion; Taiwan celadon fill @180.49; line draws Stanford→Taiwan @181.13.
- **Assets** E21/N05, E19
- **Text** `TAIWAN` t-label @180.49 · `connection` serif-i @181.13.
- **Camera** pull out. **Out** `CA` @182.01 (camera keeps moving east→ into the photo card)
- **Done** key animation complete @181.50 (cut @182.01; hold 0.51 s).
- **SFX** 180.47 pin_pop · 181.11 marker_long (dur 0.7)

### C3S038 · 182.01–185.61 · C3B037 · PAPER
- **Words** "while Terman was teaching in the 30s before the war,"  **Why** 'while Terman was teaching in the 30s before the war' → a 1930s photo of Terman teaching.
- **FX** #16 photo card + #12 year tag · **Ref** c1 continuity (Terman cards)
- **Visual** N24 1930s Terman teaching / Stanford radio lab photo card on paper; typed year tag.
- **Assets** N24 (fallback E10)
- **Text** `TERMAN` label-box vermilion @182.25 · `30s`@184.01 tag · `before the war`: `before`@184.57 `the`@184.89 `war`@185.05.
- **Camera** push. **Out** `W` → @185.55
- **Done** key animation complete @185.10 (cut @185.61; hold 0.51 s).
- **SFX** 182.23 paper_slide · 184.0 stamp_thud (soft) · 185.53 whoosh

### C3S039 · 185.61–189.85 · C3B038 · NIGHT
- **Words** "he had a Taiwanese or Chinese student, **Pan Wen-Yuan.**"  **Why** 'he had a Taiwanese or Chinese student, Pan Wen-Yuan' → Pan's portrait revealed.
- **FX** #3 burn reveal (on a portrait) + #4 hero · **Ref** intro IS043 portrait burn variation (celadon edge glow)
- **Visual** N25 young Pan Wen-Yuan photo, celadon/sepia duotone; burn reveal from centre @188.09.
- **Assets** N25
- **Text** `student` t-label @187.69 · `PAN WEN-YUAN` hero halate: `Pan`@188.09 `Wen-`@188.57 `Yuan`@188.89.
- **Camera** push 1.0→1.05, FH @188.9. **Out** `CA` @189.85
- **Done** key animation complete @189.30 (cut @189.85; hold 0.55 s).
- **SFX** 188.07 burn_crackle (dur 1.2)

### C3S040 · 189.85–193.37 · C3B039 · PAPER
- **Words** "He was a bright student, he worked very closely with Terman."  **Why** 'a bright student, worked very closely with Terman' → Pan and Terman circles tied tight.
- **FX** #2 diagram (D15) + markup arrows · **Ref** D15 relationship diagram
- **Visual** Pan circle (celadon ring) + Terman circle (vermilion ring, E10) on paper; a short double line draws between them @191.93.
- **Assets** N25, E10
- **Text** `bright student`: `bright`@190.49 `student`@190.97 · `very closely`: `very`@191.93 `closely`@192.09.
- **Camera** static. **Out** `PT` @193.2 — camera pushes into the drawn line; the papers fill the frame
- **Done** key animation complete @192.80 (cut @193.37; hold 0.57 s).
- **SFX** 189.87 pop_soft ×2 · 191.91 marker_long

### C3S041 · 193.37–197.13 · C3B040 · NIGHT
- **Words** "He actually co wrote a lot of papers that Terman published at the time."  **Why** 'co-wrote a lot of papers that Terman published' → real paper first pages with both names.
- **FX** #5 tilted pages under lamp + #18 highlighter on byline · **Ref** R9 lamp-pool desk variation
- **Visual** N26 Proc. IRE first pages (Terman & Pan) fan in at 12 fps; highlighter on the 'W. Y. Pan' byline (body size).
- **Assets** N26
- **Text** `co-wrote`: `co`@193.77 `wrote`@194.09 · `papers`@194.73.
- **Camera** push to byline. **Out** `PS` @197.07
- **Done** key animation complete @196.40 (cut @197.13; hold 0.73 s).
- **SFX** 193.39 paper_flip ×3 · 194.7 highlighter_swipe · 197.05 paper_slide

### C3S042 · 197.13–200.34 · C3B041 · PAPER
- **Words** "He also published some papers with Bill **Hewlett.**"  **Why** 'He also published some papers with Bill Hewlett' → Hewlett joins the diagram.
- **FX** #2 diagram (D15) continued · **Ref** D15
- **Visual** Same diagram as C3S040; Hewlett circle (E15, ink ring) pops @198.97; line to Pan draws.
- **Assets** E15
- **Text** `BILL HEWLETT` t-label: `Bill`@198.97 `Hewlett`@199.37.
- **Camera** pull out to fit 3 circles. **Out** `FW` @200.28 — segment hand-off c3s01→c3s02
- **Done** key animation complete @199.80 (cut @200.34; hold 0.54 s).
- **SFX** 198.95 pop_soft · 199.4 marker_long · 200.26 whoosh

### C3S043 · 200.34–205.94 · C3B042 · NIGHT
- **Words** "And a little bit later, when I say a little bit later, I mean a few decades later, after Silicon Valley,"  **Why** 'a little bit later… I mean a few decades later, after Silicon Valley' → a timeline racing through decades.
- **FX** #12 dark timeline + travelling dot + #8 streaks · **Ref** Pinterest idea 'dark horizontal timeline, travelling dot, decade ticks'
- **Visual** Night; axis with decade ticks scrolls fast right→left (streaks smear) while a celadon dot (Pan) holds centre; ticks stop @204.10.
- **Assets** 🛠
- **Text** `a few decades later`: `few`@203.46 `decades`@203.70 `later`@204.10 (no text on the repeated 'a little bit later').
- **Camera** static (axis moves). **Out** `CA` @205.94 (axis still decelerating)
- **Done** key animation complete @205.00 (cut @205.94; hold 0.94 s).
- **SFX** 200.36 whoosh_soft · 201.0 tick_soft (dur 3.0) · 204.08 tone_blip

### C3S044 · 205.94–213.14 · C3B043 · NIGHT
- **Words** "after graduating and everything, he's gonna become one of the most important people in Taiwan."  **Why** 'after graduating… one of the most important people in Taiwan' → his Stanford PhD title page, then Pan placed on Taiwan.
- **FX** #5 doc card + #3 Taiwan relief + celadon fill · **Ref** R12 relief + region fill (intro IS035 Taiwan motif)
- **Visual** N28 Pan's 1940 Stanford dissertation title page slides in @206.26 then off; E19 Taiwan relief (map kit hires) fills celadon @212.34; older Pan photo (N25b) pinned on Taiwan @210.50.
- **Assets** N28, E19, N25b
- **Text** `graduating`@206.26 · `most important people`: `most`@210.50 `important`@210.82 `people`@211.46 · `TAIWAN` t-label @212.34.
- **Camera** push to Taiwan. **Out** `PS` @213.08
- **Done** key animation complete @212.60 (cut @213.14; hold 0.54 s).
- **SFX** 206.24 paper_slide · 210.48 pin_pop · 212.32 pop_soft · 213.06 paper_slide

### C3S045 · 213.14–216.90 · C3B044 · PAPER
- **Words** "Which is not a country at this point, by the way, but it will become a country."  **Why** 'which is not a country at this point, but it will become a country' → a 1930s–40s map/poster where Taiwan is labelled as a Japanese possession.
- **FX** #3 old map + #19 pen markups + #20 map call-out · **Ref** D10 tilted vintage map (intro E30 formosa map, wider crop)
- **Visual** E20 1943 Japanese aviation map of Formosa tilted; pen circle around the island label @213.86; pen arrow → 'will become' @215.86.
- **Assets** E20
- **Text** `not a country`: `not`@213.54 `a`@213.70 `country`@213.86 · `will become`: `will`@215.86 `become`@216.10.
- **Camera** slow drift. **Out** `W` ← @216.84
- **Done** key animation complete @216.30 (cut @216.90; hold 0.60 s).
- **SFX** 213.84 pencil_scribble · 215.84 marker_scratch · 216.82 whoosh

### C3S046 · 216.90–223.46 · C3B045 · NIGHT
- **Words** "He becomes an important person in Taiwan, and he's not paying attention to everything that's happening in Silicon Valley right now."  **Why** 'an important person in Taiwan… everything happening in Silicon Valley' → Taiwan watching Silicon Valley across the Pacific (radio-wave rings).
- **FX** #3 map + §10.6.7 radio-wave rings + focal blur + #20 map call-out · **Ref** D13 ghost Pacific map + radio waves
- **Visual** Night Pacific (as C3S037, motif); rings emanate from Silicon Valley (vermilion) @221.94 and reach Taiwan (celadon) where Pan's small circle sits.
- **Assets** E21/N05, N25b
- **Text** `Taiwan` t-label @218.50 · `Silicon Valley` t-label: `Silicon`@221.94 `Valley`@222.50. (No text on 'not paying attention' — slip.)
- **Camera** pan Taiwan→SV. **Out** `CA` @223.46
- **Done** key animation complete @222.90 (cut @223.46; hold 0.56 s).
- **SFX** 218.48 pop_soft · 221.92 radio_pulse→tone_blip (dur 1.0)

### C3S047 · 223.46–228.34 · C3B046 · PAPER
- **Words** "But he's gonna go back and look and see what made it so."  **Why** 'he's gonna go back and look and see what made it so' → the recipe card examined under a focal call-out.
- **FX** §10.6.5 focal blur + FH · **Ref** callback of C3S035 recipe card
- **Visual** The recipe card from C3S035 on paper; a sharp focal circle slides from ingredient to ingredient @225.70 'see'.
- **Assets** N23 (motif)
- **Text** `go back`: `go`@224.34 `back`@224.50 · `what made it so`: `what`@226.34 `made`@226.82 `it`@227.30 `so`@227.62.
- **Camera** push 1.0→1.15, FH @224.9. **Out** `W` ↓ @228.28
- **Done** key animation complete @227.80 (cut @228.34; hold 0.54 s).
- **SFX** 223.48 paper_slide · 225.7 whoosh_soft · 228.26 whoosh

### C3S048 · 228.34–235.94 · C3B047 · NIGHT
- **Words** "And that's an interesting story, so but before we get into that story, let's look at exactly the situation Taiwan is in."  **Why** 'before we get into that story, let's look at exactly the situation Taiwan is in' → Taiwan from orbit, clouds gathering (the situation).
- **FX** #3 satellite + clouds drifting + shadows · **Ref** s02 satellite + clouds (quality bar) on Taiwan
- **Visual** Map kit Taiwan sharp satellite (N05 kit); s02 cloud layers drift in from the north-west and darken @233.70.
- **Assets** N05, E38 clouds
- **Text** `before`@230.90 t-label · `the situation`: `the`@233.70 `situation`@234.02 · `TAIWAN` hero halate @234.66.
- **Camera** push down to Taiwan. **Out** `CA` @235.94
- **Done** key animation complete @235.30 (cut @235.94; hold 0.64 s).
- **SFX** 228.36 wind (dur 7.6) · 234.64 boom_low (soft)

## 5. Act V — The existential crisis (235.94–291.29)
Music: drop to drone/low pulse at "desperate" 241.62; hit on "kicked out" 257.22; near-silence under "nothing… not a country".

### C3S049 · 235.94–240.50 · C3B048 · PAPER
- **Words** "Now, of course, everyone wants Silicon Valley, but why did Taiwan want it?"  **Why** 'everyone wants Silicon Valley, but why did Taiwan want it?' → pins all over a world atlas; Taiwan circled with a question.
- **FX** #3 vintage atlas + pins + #19 circle + #20 map call-out · **Ref** R10 old map + circle + numbered pin variation (world scale)
- **Visual** Vintage colour world atlas plate (N05 kit/N68); ink pins pop in many countries at 12 fps @236.74 (neutral — no West accent in the political acts); rough circle around Taiwan @239.54 + '?'.
- **Assets** N68
- **Text** `everyone`@236.74 · `Silicon Valley`: `Silicon`@237.46 `Valley`@238.18 · `why`@239.06 · `Taiwan`@239.54.
- **Camera** push to Taiwan. **Out** `FW` @240.44
- **Done** key animation complete @239.90 (cut @240.50; hold 0.60 s).
- **SFX** 236.72 map_pin ×8 · 239.52 marker_scratch · 240.42 whoosh

### C3S050 · 240.50–244.74 · C3B049 · NIGHT
- **Words** "And why were they so desperate? This is when we come back to Taiwan,"  **Why** 'why were they so desperate? This is when we come back to Taiwan' → Taiwan period footage, 'desperate' as hero word.
- **FX** #1 footage + #14 weave + #4 hero · **Ref** intro Taiwan 1960 clips (new clip)
- **Visual** E23 taiwan_1960_taipei_north_gate_traffic.mp4, graded, weave 0.6.
- **Assets** E23
- **Text** `desperate` hero halate @241.62 · `back to Taiwan`: `back`@243.78 `to`@243.94 `Taiwan`@244.18.
- **Camera** slow push. **Out** `PS` @244.68
- **Done** key animation complete @244.20 (cut @244.74; hold 0.54 s).
- **SFX** 240.52 projector_loop (dur 4.2) · 244.66 paper_slide

### C3S051 · 244.74–253.94 · C3B050 · GRID
- **Words** "because while the Silicon Valley is on the up and up, Taiwan is actually facing one of the most existential crises it has ever faced."  **Why** 'while Silicon Valley is on the up and up, Taiwan is facing… existential crises' → two lines: one up, one plunging into a crisis band.
- **FX** #2 line chart + era band (D05) · **Ref** D05 line chart + era band
- **Visual** Graph sheet; navy 'Silicon Valley' line (US) climbs @246.82; ink 'Taiwan' line with a celadon end dot dives @248.90; shaded crisis band fades in @250.18. Shapes only.
- **Assets** E27 graph
- **Text** `Silicon Valley` end label @245.38 · `up and up`: `up`@246.82 `and`@247.14 `up`@247.30 · `Taiwan` end label @247.86 · `existential crises`: `existential`@250.18 `crises`@251.06.
- **Camera** track right. **Out** `W` → @253.88
- **Done** key animation complete @252.00 (cut @253.94; hold 1.94 s).
- **SFX** 246.8 tick_soft (dur 0.8) · 248.88 whoosh_soft (dive) · 253.86 whoosh

### C3S052 · 253.94–261.05 · C3B051 · NIGHT
- **Words** "This crisis has to do with the fact that the UN had just kicked out Taiwan, the Republic of China, as a country."  **Why** 'the UN had just kicked out Taiwan, the Republic of China' → the real 1971 front page: U.N. seats Peking, expels Taipei.
- **FX** #5 newspaper (tilted page, halftone, push to headline) + #19 box markup · **Ref** s06 newspaper look
- **Visual** N29 NYT 26 Oct 1971 front page (© NYT, fair use, credit), sepia, halftone grows with zoom; rough box around the headline line about Taipei @257.22.
- **Assets** N29
- **Text** `kicked out` t-label: `kicked`@257.22 `out`@257.62 · `Republic of China` small caption @258.50 (`of`@258.98 `China`@259.14).
- **Camera** push to headline. **Out** `CA` @261.05
- **Done** key animation complete @259.90 (cut @261.05; hold 1.15 s).
- **SFX** 253.96 paper_rustle · 257.2 marker_scratch

### C3S053 · 261.05–265.93 · C3B052 · NIGHT
- **Words** "It basically said that there's no such thing. China belongs to the CCP."  **Why** 'there's no such thing. China belongs to the CCP' → the 1971 UN photo of the PRC delegation taking China's seat.
- **FX** #16 plate + label · **Ref** —
- **Visual** N30 UN 1971 photo (PRC delegation seated, 'CHINA' placard) slow push; red (vermilion) label CCP.
- **Assets** N30
- **Text** `no such thing`: `no`@262.81 `such`@263.05 `thing`@263.37 · `China`@263.93 · `CCP` label-box red @265.21.
- **Camera** push to the placard. **Out** `W` ↓ @265.87
- **Done** key animation complete @265.40 (cut @265.93; hold 0.53 s).
- **SFX** 261.07 projector_click · 265.19 pop_soft · 265.85 whoosh

### C3S054 · 265.93–272.73 · C3B053 · NIGHT
- **Words** "The CCP is the governing government of China, and because of that, Taiwan is just nothing. Not a country."  **Why** 'CCP is the governing government of China… Taiwan is just nothing. Not a country' → map: China in CCP ink; Taiwan's fill drains away.
- **FX** #3 relief map + region fill (R12) + glow edge + #20 map call-out · **Ref** R12 relief + filled region (here a fill that empties)
- **Visual** Map kit East Asia shaded relief; mainland China fills red (vermilion 0.6, halftone) @266.09; Taiwan celadon fill drains to an empty outline @270.65.
- **Assets** N05 kit
- **Text** `CCP` t-label @266.09 · `China`@267.85 · `nothing` serif-i @270.65 · `not a country`: `Not`@271.53 `a`@271.85 `country`@272.01.
- **Camera** push to the strait. **Out** `PS` @272.67
- **Done** key animation complete @272.10 (cut @272.73; hold 0.63 s).
- **SFX** 266.07 pop_soft · 270.63 air_swell (reverse/drain) · 272.65 paper_slide

### C3S055 · 272.73–277.21 · C3B054 · PAPER
- **Words** "And from a Taiwanese point of view, this was something they did not expect."  **Why** 'from a Taiwanese point of view, this was something they did not expect' → a Taiwanese front page of that day.
- **FX** #5 newspaper + text call-out · **Ref** §10.6.1 two paper layers
- **Visual** N31 Central Daily News 26 Oct 1971 front page (© fair use), sepia; text call-out on the lead column.
- **Assets** N31
- **Text** `Taiwanese` t-label @273.29 · `did not expect`: `did`@276.25 `not`@276.49 `expect`@276.65.
- **Camera** slow push. **Out** `CA` @277.21
- **Done** key animation complete @276.70 (cut @277.21; hold 0.51 s).
- **SFX** 272.75 paper_rustle

### C3S056 · 277.21–280.17 · C3B055 · NIGHT
- **Words** "This was something they didn't know what was gonna happen next."  **Why** 'they didn't know what was gonna happen next' → the ROC delegation walking out of the UN.
- **FX** #1 footage/photo + #14 weave · **Ref** —
- **Visual** N32 ROC delegation leaving the GA hall (25 Oct 1971), slow push, weave.
- **Assets** N32
- **Text** `next` serif-i @279.61.
- **Camera** slow push. **Out** `PS` @280.11
- **Done** key animation complete @279.60 (cut @280.17; hold 0.57 s).
- **SFX** 277.23 projector_loop (dur 2.9) · 280.09 paper_slide

### C3S057 · 280.17–284.49 · C3B056 · PAPER
- **Words** "And to truly understand why this was such an existential crisis,"  **Why** 'to truly understand why this was such an existential crisis' → the 1971 page pinned at the end of a timeline.
- **FX** #12 timeline (paper) + pinned card · **Ref** c1 timeline/collage motif (R7 axis without values)
- **Visual** Paper timeline axis; the 1971 front-page card (N29 crop) pins at the right end @282.89.
- **Assets** N29 crop
- **Text** `existential crisis`: `existential`@282.89 `crisis`@283.69.
- **Camera** static. **Out** `cont.` @284.49 (dot rewinds left)
- **Done** key animation complete @283.90 (cut @284.49; hold 0.59 s, continues — no cut).
- **SFX** 280.19 paper_slide · 282.87 pin_pop

### C3S058 · 284.49–291.29 · C3B057 · PAPER
- **Words** "we have to understand just a little bit of background about Taiwan and how the government there came to be."  **Why** 'background about Taiwan and how the government there came to be' → the timeline rewinds to the government's origin.
- **FX** #12 timeline rewind (travelling dot, cards flip back) · **Ref** R7 / timeline
- **Visual** Dot runs left fast @286.49; year ticks blur; stops at the WWII end; card of the ROC Presidential Office in Taipei (E23 still) pops @289.13.
- **Assets** E23 (still frame)
- **Text** `background`@286.49 · `Taiwan`@287.45 · `government`@289.13.
- **Camera** track left. **Out** `FW` @291.23
- **Done** key animation complete @290.30 (cut @291.29; hold 0.99 s).
- **SFX** 286.47 dot_slide (dur 1.2) · 289.11 pin_pop · 291.21 whoosh

## 6. Act VI — WWII and the post-war order (291.29–359.00)
Music: archival strings + low pulse, projector texture; build to "Security Council" 356.76.

### C3S059 · 291.29–294.01 · C3B058 · NIGHT
- **Words** "Our story starts in World War II."  **Why** 'Our story starts in World War II' → WWII newsreel with the title.
- **FX** #1 newsreel + #14 weave + #4 hero · **Ref** intro film-title over footage
- **Visual** N33 WWII Pacific newsreel (PD), weave + flicker.
- **Assets** N33
- **Text** `WORLD WAR II` hero halate: `World`@292.81 `War`@293.21 `II`@293.53.
- **Camera** —. **Out** `PS` @293.95
- **Done** key animation complete @293.50 (cut @294.01; hold 0.51 s).
- **SFX** 291.31 projector_loop (dur 2.7) · 292.79 boom_low

### C3S060 · 294.01–298.97 · C3B058 · PAPER
- **Words** "And this is where current China, the CCP, has tried to change the story a bit,"  **Why** 'the CCP has tried to change the story a bit' → a history page being re-written with a pen.
- **FX** #19 pen strike + rewrite on a page + CS · **Ref** Pinterest idea 'redacted/rewritten history book page'
- **Visual** Typeset history-book page (our recreation, no real book title) on two paper layers; CCP-era anti-Japanese war woodcut (N34) as its illustration; pen strikes a line and writes over it @297.37.
- **Assets** N34
- **Text** `CCP` t-label red @295.93 · `change the story`: `change`@297.37 `the`@297.69 `story`@297.85.
- **Camera** push. **Out** `W` → @298.91
- **Done** key animation complete @298.40 (cut @298.97; hold 0.57 s).
- **SFX** 294.03 page_turn · 297.35 pencil_scribble · 298.89 whoosh

### C3S061 · 298.97–303.53 · C3B059 · NIGHT
- **Words** "where they claim that China fought with the United States. Which is true, by the way."  **Why** 'they claim that China fought with the United States. Which is true' → the 1942 US poster of a Chinese soldier as America's ally.
- **FX** #16 poster plate (§10.5) + #19 tick · **Ref** §10.5 vintage poster as B-roll
- **Visual** N35 OWI poster 'This man is your FRIEND — Chinese — He fights for freedom' (PD), colour, fringe; pen tick @302.57.
- **Assets** N35
- **Text** `China`@300.17 t-label · `fought with`: `fought`@300.57 `with`@301.05 · `United States`@301.29 · `true`@302.57 ✓.
- **Camera** push. **Out** `CA` @303.53
- **Done** key animation complete @303.00 (cut @303.53; hold 0.53 s).
- **SFX** 298.99 air_swell · 302.55 marker_scratch

### C3S062 · 303.53–310.65 · C3B060 · NIGHT
- **Words** "I'm sure a lot of Chinese people who are in China right now actually fought with the United States in World War II against Japan."  **Why** 'a lot of Chinese people… fought with the United States in World War II against Japan' → real photos of Chinese and US soldiers together.
- **FX** #10 Vox layered panels · **Ref** s09 layered backgrounds
- **Visual** N36 US Army Signal Corps photos (Chinese & American troops, Burma/Yunnan 1944) as offset tinted panels drifting; hero photo on top.
- **Assets** N36 (×3)
- **Text** `Chinese people`: `Chinese`@304.33 `people`@304.73 · `against Japan`: `against`@309.45 `Japan`@309.77.
- **Camera** parallax drift. **Out** `PS` @310.59
- **Done** key animation complete @310.00 (cut @310.65; hold 0.65 s).
- **SFX** 303.55 paper_slide ×3 · 310.57 paper_slide

### C3S063 · 310.65–317.45 · C3B061 · PAPER
- **Words** "But it wasn't the CCP that was fighting with the United States. In fact, CCP stay out of World War II."  **Why** 'it wasn't the CCP that was fighting with the United States' → US ↔ CCP link drawn, then crossed out.
- **FX** #2 diagram (D15) + #19 cross · **Ref** D15 relationship diagram
- **Visual** US circle (48-star flag, navy ring) and CCP circle (red ring); link draws @311.93; pen X on it @312.89. No text on the 'stay out' claim (DECISIONS).
- **Assets** N40 flags
- **Text** `CCP` label @311.93.
- **Camera** static. **Out** `CA` @317.45 (CCP circle slides off as Cairo plate slides in)
- **Done** key animation complete @313.60 (cut @317.45; hold 3.85 s).
- **SFX** 311.91 pop_soft · 312.87 marker_scratch

### C3S064 · 317.45–324.28 · C3B062 · NIGHT
- **Words** "It was the ROC, the nationalists who were ruling China at the time, who fought with the United States against Japan."  **Why** 'It was the ROC, the nationalists ruling China, who fought with the US against Japan' → Chiang Kai-shek with Roosevelt and Churchill at Cairo, 1943.
- **FX** #17 2.5D (Cairo photo) + #4 · **Ref** 2.5D variation (seated group)
- **Visual** N37 Cairo Conference photo cut into backdrop / Chiang & Madame Chiang / FDR & Churchill / foreground; dolly; celadon rim on Chiang.
- **Assets** N37 (+layers)
- **Text** `the ROC` label-box celadon fill, ink text @318.01 · `nationalists` serif-i @318.97.
- **Camera** dolly. **Out** `W` ↑ @324.22
- **Done** key animation complete @322.00 (cut @324.28; hold 2.28 s).
- **SFX** 317.47 air_swell · 324.20 whoosh

### C3S065 · 324.28–330.52 · C3B063 · PAPER
- **Words** "And then as soon as the war ended, ROC was one of the big four countries,"  **Why** 'as soon as the war ended, ROC was one of the big four countries' → a 1945 'war ends' front page, then four flag-topped pillars.
- **FX** #5 newspaper card + #2 pillars (D02) · **Ref** D02 bars topped with circles (flags instead of faces), equal heights
- **Visual** N38 Aug 1945 front page card @325.56 slides off; four bars rise at 12 fps, each topped by a 1945 flag circle (N40); ROC bar celadon @329.08.
- **Assets** N38, N40
- **Text** `war ended`: `war`@325.56 `ended`@325.96 · `BIG FOUR`: `big`@329.08 `four`@329.48.
- **Camera** pull back. **Out** `cont.` @330.52
- **Done** key animation complete @330.00 (cut @330.52; hold 0.52 s, continues — no cut).
- **SFX** 325.54 paper_slide · 329.06 dot_ticks (bars) · 329.5 pop_soft ×4

### C3S066 · 330.52–335.08 · C3B064 · PAPER
- **Words** "according to the United States, that would, you know, maintain a post-war order."  **Why** 'according to the United States, would maintain a post-war order' → FDR (whose plan it was) over the four pillars.
- **FX** #2 continued + portrait circle · **Ref** D02
- **Visual** FDR circle (N39) lowers over the US pillar @331.24; serif line 'post-war order' with highlighter.
- **Assets** N39
- **Text** `United States`@331.24 · `post-war order`: `post-war`@333.96 `order`@334.60 (highlighter).
- **Camera** push 1.0→1.08. **Out** `FW` @335.02
- **Done** key animation complete @334.50 (cut @335.08; hold 0.58 s).
- **SFX** 331.22 pop_soft · 333.94 highlighter_swipe · 335.00 whoosh

### C3S067 · 335.08–339.88 · C3B065 · NIGHT
- **Words** "Basically the four policemen of the world. And those four were the United States,"  **Why** 'the four policemen of the world… the United States' → a dark world map; a ring around the globe; the first pin on the US.
- **FX** #3 world map + pins + ring · **Ref** intro IS056 world map variation
- **Visual** Map kit world night (E22/N05); a thin bone ring orbits; pin US @338.92.
- **Assets** N05/E22
- **Text** `FOUR POLICEMEN` hero halate: `four`@335.80 `policemen`@336.12 · `United States` t-label @338.92.
- **Camera** slow rotate. **Out** `cont.` @339.88
- **Done** key animation complete @339.30 (cut @339.88; hold 0.58 s, continues — no cut).
- **SFX** 335.78 boom_low (soft) · 338.9 map_pin

### C3S068 · 339.88–346.20 · C3B066 · NIGHT
- **Words** "the great the UK, the Soviet Union, and the Republic of China, ROC."  **Why** 'the UK, the Soviet Union, and the Republic of China' → pins on each.
- **FX** #3 pins + labels · **Ref** as C3S067
- **Visual** Pins UK @340.84, USSR @342.04, China (ROC, celadon) @343.88; arcs link the four.
- **Assets** N05
- **Text** `UK`@340.84 · `Soviet Union`: `Soviet`@342.04 `Union`@342.60 · `Republic of China`: `Republic`@343.88 `of`@344.36 `China`@344.52 · `ROC`@345.08.
- **Camera** pan east. **Out** `PS` @346.14
- **Done** key animation complete @345.50 (cut @346.20; hold 0.70 s).
- **SFX** 340.82 map_pin · 342.02 map_pin · 343.86 map_pin · 346.12 paper_slide

### C3S069 · 346.20–352.84 · C3B067 · PAPER
- **Words** "On top of that, the ROC, China was also one of the founding members that had signed the UN Charter."  **Why** 'one of the founding members that had signed the UN Charter' → photo of China signing the Charter, 1945.
- **FX** #16 photo card + #5 document (Charter signature page) · **Ref** Pinterest idea 'signature page with photo clipped on'
- **Visual** N41 photo of the Chinese delegate signing (San Francisco, June 1945) clipped to the Charter signature page (N42).
- **Assets** N41, N42
- **Text** `founding members`: `founding`@349.88 `members`@350.36 · `UN CHARTER` label-box @351.72 (`Charter`@352.20).
- **Camera** push. **Out** `CA` @352.84
- **Done** key animation complete @352.30 (cut @352.84; hold 0.54 s).
- **SFX** 346.22 paper_slide · 351.70 stamp_thud (soft)

### C3S070 · 352.84–359.00 · C3B068 · NIGHT
- **Words** "It had a veto, it had a permanent seat on the UN Security Council."  **Why** 'It had a veto, a permanent seat on the UN Security Council' → the Council table with the CHINA nameplate circled.
- **FX** #16 plate + #19 circle + FH · **Ref** markup-map style circle on a photo
- **Visual** N43 Security Council photo (1946–50s, CHINA placard); rough circle on the placard @355.08.
- **Assets** N43
- **Text** `veto` t-label @353.32 · `permanent seat`: `permanent`@354.44 `seat`@355.08 · `SECURITY COUNCIL` hero halate: `Security`@356.76 `Council`@357.48.
- **Camera** push to placard, FH @355.6. **Out** `W` ← @358.94
- **Done** key animation complete @358.00 (cut @359.00; hold 1.00 s).
- **SFX** 355.06 marker_scratch · 357.46 boom_low (soft) · 358.92 whoosh

## 7. Act VII — Civil war and flight to Taiwan (359.00–404.17)
Music: percussive pulse to 383; thin at "flee" 381.00; wistful line 383–404.

### C3S071 · 359.00–365.40 · C3B069 · NIGHT
- **Words** "Now, as soon as World War II ends, the civil war kicks off in China, or I guess to be more accurate,"  **Why** 'as soon as World War II ends, the civil war kicks off in China' → civil-war newsreel.
- **FX** #1 newsreel + #14 weave + #4 hero · **Ref** —
- **Visual** N44 Chinese Civil War newsreel (1946–49, PD), weave 0.8, flicker.
- **Assets** N44
- **Text** `CIVIL WAR` hero halate: `civil`@361.72 `war`@362.12.
- **Camera** —. **Out** `PS` @365.34
- **Done** key animation complete @362.80 (cut @365.40; hold 2.60 s).
- **SFX** 359.02 projector_loop (dur 6.3) · 361.70 boom_low

### C3S072 · 365.40–372.76 · C3B070 · PAPER
- **Words** "it restarts in China, where the ROC, who are the nationalists, are fighting against the communists, which is the CCP."  **Why** 'it restarts… the ROC nationalists fighting the communists, the CCP' → face-off of the two leaders.
- **FX** #12 torn poster + portrait circles · **Ref** intro IS044 torn fight-poster variation (celadon vs red)
- **Visual** Torn-paper poster: Chiang Kai-shek (N45, celadon duotone) left @367.40, Mao Zedong (N45, red duotone) right @370.44; torn seam down the middle.
- **Assets** N45 ×2
- **Text** `restarts`@365.64 · `ROC`@367.40 · `nationalists`@368.44 · `communists`@370.44 · `CCP`@371.72.
- **Camera** push. **Out** `W` ↓ @372.70
- **Done** key animation complete @372.00 (cut @372.76; hold 0.76 s).
- **SFX** 365.42 paper_tear · 367.38 pop_soft · 370.42 pop_soft · 372.68 whoosh

### C3S073 · 372.76–378.68 · C3B071 · NIGHT
- **Words** "Over the next four years, they fight on the CCP comes out ahead, the communists win the civil war,"  **Why** 'over the next four years… the communists win the civil war' → CCP ink spreading over the map of China.
- **FX** #3 burn reveal (ink spreads N→S) + #13 count · **Ref** R12 relief + s02 burn reveal variation
- **Visual** Map kit China relief night; red (CCP) burns south over four steps at 12 fps; counter 1→4 small.
- **Assets** N05
- **Text** `four years`: `four`@373.56 (count 1→4) `years`@373.80 · `win`@377.56.
- **Camera** pull back to fit China. **Out** `cont.` @378.68
- **Done** key animation complete @378.00 (cut @378.68; hold 0.68 s, continues — no cut).
- **SFX** 373.54 counter_ticks · 374.0 burn_crackle (dur 3.5)

### C3S074 · 378.68–383.45 · C3B072 · NIGHT
- **Words** "and the ROC, the nationalists actually flee to the island of Taiwan."  **Why** 'the ROC… flee to the island of Taiwan' → route from the mainland across the strait to Taiwan on satellite imagery.
- **FX** #3 satellite + yellow marker route + celadon district fill + #20 map call-out · **Ref** D14 satellite + highlighted district + yellow route
- **Visual** Map kit strait satellite; yellow marker route draws mainland→Taiwan @381.00; Taiwan fills celadon @382.36.
- **Assets** N05
- **Text** `flee`@381.00 t-label · `TAIWAN` hero halate @382.36.
- **Camera** track along route. **Out** `PS` @383.39
- **Done** key animation complete @382.90 (cut @383.45; hold 0.55 s).
- **SFX** 380.98 marker_long (dur 1.3) · 382.34 boom_low (soft) · 383.37 paper_slide

### C3S075 · 383.45–388.49 · C3B073 · PAPER
- **Words** "Now, they have arrived at this island, which is Taiwan. It's called Taiwan at that point too."  **Why** 'they have arrived at this island… It's called Taiwan at that point too' → 1949 arrival photo, then a pre-war painting labelled Taiwan.
- **FX** #16 photo card + painting (§10.5) + #19 underline · **Ref** §10.5 pictorial painting
- **Visual** N46 1949 arrival at Keelung photo card @384.25 → E24 Taiwan bird's-eye 1935 painting; pen underline under its 'Taiwan' title @386.89.
- **Assets** N46, E24
- **Text** `arrived`@384.25 · `Taiwan`@386.89 (pen underline).
- **Camera** pan across. **Out** `CA` @388.49
- **Done** key animation complete @387.90 (cut @388.49; hold 0.59 s).
- **SFX** 383.47 paper_slide · 386.87 pencil_scribble

### C3S076 · 388.49–396.89 · C3B074 · NIGHT
- **Words** "But they are not Taiwanese at this point. In fact, all these people, the government that's coming to the island, they say that they are the government of Taiwan."  **Why** 'they are not Taiwanese… the government coming to the island… say they are the government' → the ROC government installed in Taipei.
- **FX** #1 footage + #14 weave · **Ref** —
- **Visual** N47 Chiang in Taipei 1950 photo → E23 Presidential Office clip (1st use).
- **Assets** N47, E23
- **Text** `not Taiwanese`: `not`@389.21 `Taiwanese`@389.37 · `government`@392.65.
- **Camera** slow push. **Out** `FW` @396.83
- **Done** key animation complete @394.00 (cut @396.89; hold 2.89 s).
- **SFX** 388.51 projector_loop (dur 8.3) · 396.81 whoosh

### C3S077 · 396.89–404.17 · C3B075 · PAPER
- **Words** "They're just going through, you know, temporary problems, temporary inconvenience, but they're still the government of Taiwan."  **Why** 'temporary problems, temporary inconvenience… still the government' → a 1950s 'recover the mainland' poster: they planned to go back.
- **FX** #16 poster + #19 pen strike/replace · **Ref** §10.5 poster B-roll
- **Visual** N48 1950s ROC poster (fair use), colour; typed caption line: `temporary problems` then 'problems' struck and `inconvenience` written @401.21.
- **Assets** N48
- **Text** `temporary`@398.57 · `problems`@399.53 · `inconvenience`@401.21 · `still`@402.65.
- **Camera** push. **Out** `W` → @404.11 — segment hand-off c3s02→c3s03
- **Done** key animation complete @403.40 (cut @404.17; hold 0.77 s).
- **SFX** 396.91 paper_slide · 401.19 marker_scratch · 404.09 whoosh

## 8. Act VIII — Recognition: the world says ROC (404.17–479.00)
Music: steady mid-tempo; darker colour on "problem" 444.60; settle 462–479.

### C3S078 · 404.17–409.21 · C3B076 · NIGHT
- **Words** "And guess what? The world says the same thing. Majority of the world says the same thing."  **Why** 'the world says the same thing. Majority of the world' → countries on a dark world map flip to the ROC colour.
- **FX** #3 map fills 12 fps · **Ref** intro IS056 world map variation
- **Visual** Map kit world night; ~1950 ROC-recognising countries (N49 data) fill celadon 0.8 at 12 fps @405.29, more @407.21.
- **Assets** N05, N49
- **Text** `the world`: `The`@405.13 `world`@405.29 · `majority`@407.21.
- **Camera** slow pan. **Out** `PS` @409.15
- **Done** key animation complete @408.60 (cut @409.21; hold 0.61 s).
- **SFX** 405.27 dot_ticks (dur 1.6) · 409.13 paper_slide

### C3S079 · 409.21–412.33 · C3B077 · PAPER
- **Words** "The United States is with the ROC, it's with the nationalists."  **Why** 'The United States is with the ROC' → Eisenhower and Chiang in Taipei.
- **FX** #10 layered panels · **Ref** s09 layered
- **Visual** N50 Eisenhower & Chiang, Taipei 1960 (PD) hero; panels: US flag, ROC flag (N40).
- **Assets** N50, N40
- **Text** `United States`: `United`@409.37 `States`@409.69 · `ROC` label-box celadon @410.57.
- **Camera** drift. **Out** `CA` @412.33
- **Done** key animation complete @411.80 (cut @412.33; hold 0.53 s).
- **SFX** 409.23 paper_slide · 410.55 pop_soft

### C3S080 · 412.33–417.85 · C3B078 · NIGHT
- **Words** "That means it recognizes the ROC as the government of China, as all of China."  **Why** 'recognizes the ROC as the government of China, as all of China' → the whole of China outlined in the ROC's claim.
- **FX** #3 R12 region fill + glow edge · **Ref** R12 relief + filled region
- **Visual** Map kit East Asia relief; mainland + Taiwan filled celadon + halftone + glowing edge @416.73.
- **Assets** N05
- **Text** `recognizes`@413.21 · `ALL OF CHINA` hero halate: `all`@416.73 `of`@416.97 `China`@417.21.
- **Camera** pull back. **Out** `FW` @417.79
- **Done** key animation complete @417.30 (cut @417.85; hold 0.55 s).
- **SFX** 413.19 tone_blip · 416.71 boom_low (soft)

### C3S081 · 417.85–423.45 · C3B079 · NIGHT
- **Words** "Same thing with all the US allies. Most of the US allies, including Japan after the war,"  **Why** 'the US allies, including Japan after the war' → a dark list of allies with a focus pull onto Japan.
- **FX** #13 list + rack focus (D12) · **Ref** D12 dark list with blurred bars + focus pull
- **Visual** Dark list of US-allied countries (N49) with thin celadon bars, blurred; focus pulls to JAPAN @422.01.
- **Assets** N49
- **Text** `US allies`: `US`@419.05 `allies`@419.45 · `Japan`@422.01.
- **Camera** list scrolls slowly. **Out** `CA` @423.45
- **Done** key animation complete @422.80 (cut @423.45; hold 0.65 s).
- **SFX** 418.0 tick_soft (dur 1.0) · 421.99 tone_blip

### C3S082 · 423.45–428.33 · C3B080 · NIGHT
- **Words** "even though Japan just fought the United States and Taiwan before."  **Why** 'even though Japan just fought the United States' → WWII Pacific footage.
- **FX** #1 newsreel + #14 weave · **Ref** —
- **Visual** N33 WWII Pacific newsreel (2nd use, different shot: carrier/air combat).
- **Assets** N33
- **Text** `Japan`@424.09 · `fought`@424.81. (No text on 'and Taiwan' — slip.)
- **Camera** —. **Out** `PS` @428.27
- **Done** key animation complete @425.40 (cut @428.33; hold 2.93 s).
- **SFX** 423.47 projector_loop (dur 4.8) · 428.25 paper_slide

### C3S083 · 428.33–433.05 · C3B081 · PAPER
- **Words** "It recognizes Taiwan as the true government of China."  **Why** 'It recognizes Taiwan as the true government of China' → the 1952 Japan–ROC treaty signing.
- **FX** #16 photo card + #18 highlighter · **Ref** —
- **Visual** N51 Treaty of Taipei signing photo on two paper layers; caption with highlighter on 'true government'.
- **Assets** N51
- **Text** `true government`: `true`@430.97 `government`@431.45 (highlighter).
- **Camera** push. **Out** `W` ↑ @432.99
- **Done** key animation complete @432.20 (cut @433.05; hold 0.85 s).
- **SFX** 428.35 paper_slide · 430.95 highlighter_swipe · 432.97 whoosh

### C3S084 · 433.05–438.44 · C3B082 · NIGHT
- **Words** "The United Nations also recognizes the ROC as the true government of China."  **Why** 'The United Nations also recognizes the ROC' → UN HQ in the 1950s, the ROC flag in the row of flags.
- **FX** #16 plate + #19 circle · **Ref** —
- **Visual** N52 UN HQ 1950s photo with flag row; rough circle around the ROC flag @435.69.
- **Assets** N52
- **Text** `UNITED NATIONS` hero halate: `United`@433.29 `Nations`@433.77 · `ROC`@435.69.
- **Camera** push. **Out** `CA` @438.44
- **Done** key animation complete @436.80 (cut @438.44; hold 1.64 s).
- **SFX** 433.27 air_swell · 435.67 marker_scratch

### C3S085 · 438.44–443.24 · C3B083 · PAPER
- **Words** "They have the permanent seat, they have a seat as China and the UN."  **Why** 'They have the permanent seat… a seat as China in the UN' → the Council horseshoe; the CHINA seat fills.
- **FX** #2 seat dots (D06 semicircle as the horseshoe table) · **Ref** D06 parliament dots variation (Security Council horseshoe)
- **Visual** Paper; 11 seat dots on a horseshoe, 5 permanent ringed; the 'China' seat fills celadon @439.56.
- **Assets** 🛠
- **Text** `permanent seat`: `permanent`@439.00 `seat`@439.56 · `as China`: `as`@441.16 `China`@441.48.
- **Camera** slow push. **Out** `FW` @443.18
- **Done** key animation complete @442.00 (cut @443.24; hold 1.24 s).
- **SFX** 439.54 pop_soft · 443.16 whoosh

### C3S086 · 443.24–451.96 · C3B084 · NIGHT
- **Words** "But there is a problem. We have the Soviet Union recognizing the CCP as the true government of China because communist communists."  **Why** 'there is a problem: the Soviet Union recognizing the CCP' → Stalin and Mao, Moscow 1949.
- **FX** #16 plate + contrast call-out · **Ref** §10.6.3
- **Visual** N53 Stalin & Mao, Dec 1949; contrast call-out on the two @445.88; red label CCP.
- **Assets** N53
- **Text** `problem`@444.60 · `Soviet Union`: `Soviet`@445.88 `Union`@446.36 · `CCP`@447.64.
- **Camera** ease-in push. **Out** `CA` @451.96
- **Done** key animation complete @448.20 (cut @451.96; hold 3.76 s).
- **SFX** 445.86 circuit_clunk

### C3S087 · 451.96–455.40 · C3B085 · PAPER
- **Words** "They are just brothers. You know, they're gonna recognize each other. On top of that,"  **Why** 'They are just brothers… recognize each other' → a Sino-Soviet friendship poster (handshake).
- **FX** #16 poster (§10.5) · **Ref** §10.5
- **Visual** N54 1950s Sino-Soviet friendship poster, colour, slow push.
- **Assets** N54
- **Text** `brothers` serif-i @452.36.
- **Camera** push. **Out** `W` → @455.34
- **Done** key animation complete @453.20 (cut @455.40; hold 2.20 s).
- **SFX** 451.98 paper_slide · 455.32 whoosh

### C3S088 · 455.40–462.20 · C3B086 · NIGHT
- **Words** "slowly the whole Soviet bloc, the Warsaw Pact, starts recognizing CCP as China."  **Why** 'slowly the whole Soviet bloc, the Warsaw Pact, starts recognizing CCP' → Warsaw Pact countries turn to the CCP side one by one.
- **FX** #3 map fills (slow 12 fps) + contrast call-out + #20 map call-out · **Ref** R12/kit Europe map variation
- **Visual** Map kit Europe–Asia night; Warsaw Pact states fill red (vermilion 0.6 + halftone), slowly west→east @455.40; contrast call-out on the bloc @457.48.
- **Assets** N05
- **Text** `Soviet bloc`: `Soviet`@456.44 `bloc`@456.92 · `WARSAW PACT` label: `Warsaw`@457.48 `Pact`@458.28 · `CCP`@460.68.
- **Camera** pan east. **Out** `PS` @462.14
- **Done** key animation complete @461.30 (cut @462.20; hold 0.90 s).
- **SFX** 455.42 dot_ticks (dur 3) · 457.46 circuit_clunk · 462.12 paper_slide

### C3S089 · 462.20–468.28 · C3B087 · PAPER
- **Words** "But that's not a big issue, especially at the beginning, because Taiwan has the seat of China in the UN."  **Why** 'not a big issue… Taiwan has the seat of China in the UN' → the horseshoe again, China seat still celadon.
- **FX** #2 seat dots (motif) + highlighter · **Ref** D06 horseshoe (callback of C3S085)
- **Visual** Same horseshoe as C3S085; the China seat pulses; caption highlighter.
- **Assets** 🛠
- **Text** `not a big issue`: `not`@462.60 `a`@462.68 `big`@462.76 `issue`@463.00 · `seat of China`: `seat`@466.20 `of`@466.68 `China`@466.92.
- **Camera** push to seat. **Out** `CA` @468.28
- **Done** key animation complete @467.40 (cut @468.28; hold 0.88 s).
- **SFX** 466.18 pop_soft

### C3S090 · 468.28–473.08 · C3B088 · NIGHT
- **Words** "So it doesn't matter if the Soviet Union is recognizing because Taiwan has the United States,"  **Why** 'doesn't matter if the Soviet Union… Taiwan has the United States' → Taiwan tied to the US; the USSR node greys out.
- **FX** #2 diagram on night (D15) · **Ref** D15 on night ground
- **Visual** Nodes: Taiwan (celadon), US (navy ring), USSR (red ring); USSR greys @469.00; thick line Taiwan↔US draws @472.36.
- **Assets** N40 flags
- **Text** `doesn't matter`: `doesn't`@468.68 `matter`@469.00 · `United States`: `United`@472.36 `States`@472.68.
- **Camera** static. **Out** `W` ↓ @473.02
- **Done** key animation complete @472.50 (cut @473.08; hold 0.58 s).
- **SFX** 469.0 tone_blip · 472.34 marker_long · 473.00 whoosh

### C3S091 · 473.08–479.00 · C3B089 · PAPER
- **Words** "and because of the United States, it has more than enough support in the UN that it's not gonna get kicked out at all."  **Why** 'more than enough support in the UN… not gonna get kicked out' → a support bar running far past the dashed 'kicked out' line.
- **FX** #2 horizontal bars (D04) + dashed threshold · **Ref** D04 horizontal bars + serif title
- **Visual** Paper; serif title 'support in the UN'; one celadon bar grows at 12 fps past a dashed threshold labelled 'kicked out'.
- **Assets** 🛠
- **Text** `more than enough support`: `more`@474.68 `than`@474.84 `enough`@475.00 `support`@475.32 · `kicked out` at the threshold: `kicked`@477.64 `out`@478.04.
- **Camera** track right. **Out** `FW` @478.94
- **Done** key animation complete @478.30 (cut @479.00; hold 0.70 s).
- **SFX** 474.66 dot_ticks (dur 1.2) · 478.92 whoosh

## 9. Act IX — The hidden fragility (479.00–550.59)
Music: clock-like pulse from 521.07; domino sting 534.03; hollow sustain on "very, very long time".

### C3S092 · 479.00–484.28 · C3B090 · NIGHT
- **Words** "Now this is where I want to explain the situation that the Taiwanese government is in,"  **Why** 'the situation that the Taiwanese government is in' → ROC government footage on a Taiwanese Tatung TV.
- **FX** #11 TV (Tatung) + CRT on · **Ref** §10.1.7 Tatung (Taiwanese maker)
- **Visual** E05 Tatung TV20; E23 Presidential Office / Taipei boulevard clip (2nd use of the office clip, different section).
- **Assets** E05, E23
- **Text** `situation`@481.16 · `Taiwanese government`: `Taiwanese`@482.20 `government`@483.08.
- **Camera** push. **Out** `PT` @484.0 (into the screen)
- **Done** key animation complete @483.60 (cut @484.28; hold 0.68 s).
- **SFX** 479.02 crt_click · 479.05 crt_hum (dur 5)

### C3S093 · 484.28–490.84 · C3B091 · PAPER
- **Words** "because even though it has majority recognition, in reality it's not majority recognition."  **Why** 'even though it has majority recognition, in reality it's not' → an isotype grid of countries: most look celadon, then reveal hollow.
- **FX** #2 isotype grid (D03) · **Ref** D03 isotype grid with labels
- **Visual** Grid of country squares; majority fill celadon @486.12; 'in reality' most turn to hollow outlines @489.00.
- **Assets** 🛠, N49
- **Text** `majority recognition`: `majority`@486.12 `recognition`@486.92 · `in reality`: `in`@487.88 `reality`@488.04 · `not`@489.00.
- **Camera** static. **Out** `CA` @490.84
- **Done** key animation complete @490.00 (cut @490.84; hold 0.84 s).
- **SFX** 486.10 dot_ticks · 489.0 dot_ticks (reverse)

### C3S094 · 490.84–497.63 · C3B092 · NIGHT
- **Words** "Let me explain A lot of countries say hey Taiwan is the government of China because the United States is saying that."  **Why** 'a lot of countries say Taiwan is the government of China because the United States is saying that' → flows from the US to many countries.
- **FX** #2 dark Sankey over ghost world map (D11) · **Ref** D11 dark Sankey money-flow variation
- **Visual** Ghost world map; thin celadon flows fan from a navy US node to many country nodes @495.32.
- **Assets** E22
- **Text** `a lot of countries`: `lot`@492.12 `countries`@492.36 · `because the United States`: `because`@495.32 `United`@495.80 `States`@496.20.
- **Camera** pull back. **Out** `PS` @497.57
- **Done** key animation complete @497.00 (cut @497.63; hold 0.63 s).
- **SFX** 495.30 whoosh_soft (flows) · 497.55 paper_slide

### C3S095 · 497.63–504.67 · C3B093 · PAPER
- **Words** "And this is something Taiwan realizes from the beginning, too. US was truly the foremost power after World War II."  **Why** 'Taiwan realizes… the US was truly the foremost power after World War II' → bars topped with flags; the US bar towers.
- **FX** #2 ranked bars topped with circles (D02) · **Ref** D02 / R4 ranked bars with portraits — flags instead
- **Visual** Paper; bars rise at 12 fps topped with flag circles (US, USSR, UK, France); US bar navy and tallest, USSR bar red, others neutral; label-box `foremost power`. Shapes only.
- **Assets** N40
- **Text** `Taiwan realizes`: `Taiwan`@498.51 `realizes`@499.07 · `foremost power`: `foremost`@502.11 `power`@502.75.
- **Camera** tilt up the US bar. **Out** `W` ↑ @504.61
- **Done** key animation complete @503.90 (cut @504.67; hold 0.77 s).
- **SFX** 500.6 dot_ticks (bars) · 502.09 pop_soft · 504.59 whoosh

### C3S096 · 504.67–508.83 · C3B094 · NIGHT
- **Words** "Doesn't matter what the USSR says. We had a bigger military,"  **Why** 'Doesn't matter what the USSR says. We had a bigger military' → Soviet parade dims; US fleet footage.
- **FX** #1 footage + #14 weave + HC on action · **Ref** —
- **Visual** N55 Soviet May Day parade (dims to 30 % @506.0) → hard cut on action to N56 1950s US fleet steaming @507.71.
- **Assets** N55, N56
- **Text** `USSR` t-label @505.47 · `bigger military`: `bigger`@507.71 `military`@508.11.
- **Camera** —. **Out** `CA` @508.83
- **Done** key animation complete @508.30 (cut @508.83; hold 0.53 s).
- **SFX** 504.69 projector_loop (dur 4.1) · 507.69 whoosh_soft

### C3S097 · 508.83–513.23 · C3B095 · PAPER
- **Words** "bigger economy, especially if you, you know, factor in the whole Western bloc."  **Why** 'bigger economy… factor in the whole Western bloc' → 1950s US factory film, then the Western bloc map.
- **FX** #1 footage card + #3 map (vintage atlas) · **Ref** R11 regions on vintage atlas
- **Visual** N57 1950s assembly-line clip in a paper-framed card; slides off to a vintage atlas where Western-bloc countries fill bone/ink outline @512.11.
- **Assets** N57, N68
- **Text** `bigger economy`: `bigger`@508.83 `economy`@509.23 · `Western bloc`: `Western`@512.11 `bloc`@512.51.
- **Camera** pull back. **Out** `FW` @513.17
- **Done** key animation complete @512.70 (cut @513.23; hold 0.53 s).
- **SFX** 508.85 paper_slide · 512.09 dot_ticks · 513.15 whoosh

### C3S098 · 513.23–521.07 · C3B096 · NIGHT
- **Words** "So it was the power. And because of that, when the US said something, there were vast majority of the countries who said the same thing."  **Why** 'it was the power… when the US said something, most countries said the same' → a pulse from the US and countries lighting up in its wake.
- **FX** #3 world map + §10.6.7 radio-wave rings + #20 map call-out · **Ref** radio-wave variation on the world map
- **Visual** Map kit world night; navy rings expand from the US @516.51; countries light navy-tinted in the ring's wake @518.27.
- **Assets** N05
- **Text** `the power` hero halate: `the`@514.43 `power`@514.75 · `same thing`: `same`@520.35 `thing`@520.59.
- **Camera** slow push. **Out** `PS` @521.01
- **Done** key animation complete @520.40 (cut @521.07; hold 0.67 s).
- **SFX** 516.49 radio_pulse (dur 1.5) · 521.0 paper_slide

### C3S099 · 521.07–527.23 · C3B097 · PAPER
- **Words** "But that creates an issue. And that issue is if the US pulls your recognition,"  **Why** 'that creates an issue… if the US pulls your recognition' → the isotype grid again; the US string is pulled.
- **FX** #2 isotype grid (D03 motif) + string · **Ref** D03 motif (C3S093)
- **Visual** Same grid; strings from each square to a navy US square; the US square is yanked aside @524.51, strings go taut.
- **Assets** 🛠
- **Text** `issue`@522.19 · `pulls`@524.51 · `recognition`@525.79.
- **Camera** push. **Out** `CA` @527.23
- **Done** key animation complete @526.30 (cut @527.23; hold 0.93 s).
- **SFX** 522.17 tone_blip · 524.49 whoosh_soft (pull)

### C3S100 · 527.23–535.23 · C3B098 · NIGHT
- **Words** "you cannot really say that's just one country saying, hey, we don't recognize you. That's gonna mean a lot of countries that will start following suit."  **Why** 'not just one country… a lot of countries will start following suit' → dominoes labelled with flags falling after the first.
- **FX** 2.5D CSS dominoes (12 fps fall) · **Ref** Pinterest idea 'Cold-War domino-theory row' (new)
- **Visual** Row of 3D dominoes on a dark table, each with a flag face (N40/N63); first (US) tips @528.91; the rest fall in sequence @534.03.
- **Assets** N63, N40
- **Text** `one country`: `one`@528.91 `country`@529.15 · `following suit`: `following`@534.03 `suit`@534.59.
- **Camera** track along the row. **Out** `W` → @535.17
- **Done** key animation complete @534.70 (cut @535.23; hold 0.53 s).
- **SFX** 528.89 domino_tick (wood) · 534.0 domino_run (dur 0.9) · 535.15 whoosh

### C3S101 · 535.23–541.47 · C3B099 · PAPER
- **Words** "But as of right now, that's not a big issue at all, because remember one thing, it's the United States of America."  **Why** 'not a big issue… it's the United States of America' → the 1954 US–ROC Mutual Defense Treaty signing.
- **FX** #16 photo card + typographic · **Ref** —
- **Visual** N58 1954 treaty signing photo (PD) on paper; typographic box 'United States of America' word by word (last word settles in 0.12 s, done 540.95).
- **Assets** N58
- **Text** `remember one thing`: `remember`@538.19 `one`@538.59 `thing`@538.83 · `United States of America`: `United`@539.79 `States`@540.27 `of`@540.67 `America`@540.83.
- **Camera** push. **Out** `CA` @541.47
- **Done** key animation complete @540.95 (cut @541.47; hold 0.52 s).
- **SFX** 535.25 paper_slide · 539.77 stamp_thud (soft)

### C3S102 · 541.47–544.35 · C3B100 · NIGHT
- **Words** "They're not gonna talk to the communist ever."  **Why** 'They're not gonna talk to the communists ever' → a telephone that never gets dialled through.
- **FX** #1 footage + #14 · **Ref** —
- **Visual** E26 rotary-phone clip (1st use) — the dial stops; image freezes and darkens @543.55.
- **Assets** E26
- **Text** `not gonna talk`: `not`@541.79 `gonna`@541.95 `talk`@542.19 · `ever`@543.55.
- **Camera** slow push. **Out** `PS` @544.29
- **Done** key animation complete @543.80 (cut @544.35; hold 0.55 s).
- **SFX** 541.49 dial_click→tick_soft · 543.53 projector_click (freeze)

### C3S103 · 544.35–550.59 · C3B101 · PAPER
- **Words** "That's the belief assumption that Taiwan is gonna operate under for a very, very long time."  **Why** 'the belief… assumption Taiwan is gonna operate under for a very, very long time' → a typed memo: 'belief' struck to 'assumption', long arrow of time.
- **FX** D08 typed memo + #19 pen + timeline arrow · **Ref** D08 telegram/memo variation
- **Visual** Typed memo card (ledger paper ≤ native size) with Taiwan celadon tab; 'belief' struck → 'assumption'; a long dashed arrow runs off frame right @548.75.
- **Assets** E27 ledger
- **Text** `belief`@544.99 · `assumption`@545.63 · `very, very long time`: `very`@548.75 `very`@549.07 `long`@549.39 `time`@549.95.
- **Camera** track right with the arrow. **Out** `FW` @550.53
- **Done** key animation complete @550.00 (cut @550.59; hold 0.59 s).
- **SFX** 544.97 letter_ticks · 545.61 marker_scratch · 548.73 marker_long · 550.51 whoosh

## 10. Act X — Decolonization and the UN vote (550.59–602.02)
Music: new rhythmic layer at 550.59; keep under the UN explanation; carry across the c4 boundary.

### C3S104 · 550.59–556.59 · C3B102 · NIGHT
- **Words** "Now, as years pass, there's decolonization that's happening inside of Africa."  **Why** 'as years pass, there's decolonization in Africa' → Africa's colonial blocks dissolving into new countries.
- **FX** #3 map + 12 fps border reveal + #4 hero · **Ref** R12 relief variation (Africa)
- **Visual** Map kit Africa shaded relief night; grey colonial blocks crack into country borders at 12 fps @553.15 (N64 data order).
- **Assets** N05, N64
- **Text** `DECOLONIZATION` hero halate @553.15 · `Africa` t-label @555.79.
- **Camera** push. **Out** `CA` @556.59
- **Done** key animation complete @555.90 (cut @556.59; hold 0.69 s).
- **SFX** 553.13 dot_ticks (dur 2) · 555.77 pop_soft

### C3S105 · 556.59–560.64 · C3B103 · PAPER
- **Words** "Very far away from China, but unfortunately."  **Why** 'very far away from China, but…' → a dashed distance line from Africa to China on a tilted atlas.
- **FX** #3 D10 tilted vintage atlas + dashed line · **Ref** D10
- **Visual** Vintage atlas plate tilted; dashed ink line Africa→China draws @556.91.
- **Assets** N68
- **Text** `far away`: `far`@556.91 `away`@557.23 · `China`@557.79.
- **Camera** track east. **Out** `W` ← @560.58
- **Done** key animation complete @558.80 (cut @560.64; hold 1.84 s).
- **SFX** 556.89 marker_long · 560.56 whoosh

### C3S106 · 560.64–568.56 · C3B104 · NIGHT
- **Words** "That decolonization is gonna have a drastic impact on this fight that's happening between the CCP and the ROC."  **Why** 'a drastic impact on this fight between the CCP and the ROC' → Ghana's independence 1957, then the two sides' labels.
- **FX** #1 footage + #14 + split labels · **Ref** —
- **Visual** N59 Ghana independence footage (Nkrumah) graded; at @566.48 a split: red CCP label left, celadon ROC label right.
- **Assets** N59
- **Text** `drastic impact`: `drastic`@562.72 `impact`@563.36 · `CCP`@566.48 · `ROC`@567.76.
- **Camera** slow push. **Out** `PS` @568.50
- **Done** key animation complete @568.00 (cut @568.56; hold 0.56 s).
- **SFX** 560.66 projector_loop (dur 5.8) · 568.48 paper_slide

### C3S107 · 568.56–576.80 · C3B105 · PAPER
- **Words** "That's because you see every new country that is being born in Africa after decolonization is a new country that has now a new vote"  **Why** 'every new country born in Africa… has a new vote' → assembly dots popping in one by one, then a ballot.
- **FX** #2 parliament dots (D06) 12 fps · **Ref** D06 parliament dots + highlighted title
- **Visual** Paper; GA semicircle of dots; new dots pop at 12 fps (one per new African member) @571.20; ballot icon @576.24.
- **Assets** N64
- **Text** `new country`: `new`@569.92 `country`@570.16 · `born`@571.20 · `new vote`: `new`@575.92 `vote`@576.24 (highlighter title).
- **Camera** slow push. **Out** `CA` @576.80
- **Done** key animation complete @576.30 (cut @576.80; hold 0.50 s).
- **SFX** 571.18 dot_ticks (dur 2.5) · 576.22 pop_soft

### C3S108 · 576.80–584.48 · C3B106 · NIGHT
- **Words** "inside of the UN General Assembly, and that vote is gonna come in very very useful if you can somehow get that vote on your **side.**"  **Why** 'inside the UN General Assembly… useful if you get that vote on your side' → the GA hall; ballots slide to one side.
- **FX** #16 plate + ballot cards · **Ref** —
- **Visual** N60 UN General Assembly hall photo (1960s); two ballot stacks (red CCP / celadon ROC); a ballot slides to one side @583.2 (done 583.95).
- **Assets** N60
- **Text** `UN GENERAL ASSEMBLY` hero halate: `UN`@577.60 `General`@578.00 `Assembly`@578.40 · `useful`@581.04 · `your side`: `your`@583.76 `side`@584.00.
- **Camera** push. **Out** `PS` @584.42
- **Done** key animation complete @583.95 (cut @584.48; hold 0.53 s).
- **SFX** 577.58 air_swell · 583.2 paper_slide

### C3S109 · 584.48–591.92 · C3B107 · PAPER
- **Words** "And this is where I want to explain just quickly how the UN works because everyone knows, I feel like, especially if you're watching this podcast,"  **Why** 'how the UN works… especially if you're watching this podcast' → a vintage UN explainer booklet opens to its org chart.
- **FX** #5 manual (§10.5) + page turn · **Ref** §10.5 vintage manual
- **Visual** N61 1950s UN booklet: cover → page turn @586.88 to the organs chart (GA, SC).
- **Assets** N61
- **Text** `how the UN works`: `how`@586.88 `the`@587.04 `UN`@587.20 `works`@587.68.
- **Camera** push to the chart. **Out** `W` ↑ @591.86
- **Done** key animation complete @588.60 (cut @591.92; hold 3.32 s).
- **SFX** 584.50 paper_slide · 586.86 page_turn · 591.84 whoosh

### C3S110 · 591.92–597.44 · C3B108 · NIGHT
- **Words** "that there's a veto in UN permanent members. So the United States, the UK,"  **Why** 'a veto in UN permanent members. So the United States, the UK' → the Council chamber; flag circles appear as named.
- **FX** #16 plate + flag circles (D02 heads) · **Ref** D02 circles on night
- **Visual** N62 Security Council chamber photo, dimmed; `VETO`; flag circles pop US @595.44, UK @596.64.
- **Assets** N62, N40
- **Text** `VETO` hero halate @592.56 · `permanent members`: `permanent`@593.84 `members`@594.24 · `United States`@595.44 · `UK`@596.64.
- **Camera** slow push. **Out** `PS` @597.38
- **Done** key animation complete @596.90 (cut @597.44; hold 0.54 s).
- **SFX** 592.54 boom_low (soft) · 595.42 pop_soft · 596.62 pop_soft · 597.36 paper_slide

### C3S111 · 597.44–602.02 · C3B109 · PAPER
- **Words** "France, China, and now Russia, but back then it was the Soviet Union."  **Why** 'France, China, and now Russia, but back then it was the Soviet Union' → the five flag circles; Russia flips to the USSR flag.
- **FX** #2 flag-circle row + card flip · **Ref** D02 heads row
- **Visual** Paper; row of 5 circles: France @597.44, China @598.32 (ROC flag — the seat's holder then, celadon ring), Russia @599.92 flips to USSR @601.20. Hold to 602.02 — c4 continues 'All of them have a veto'.
- **Assets** N40
- **Text** `France`@597.44 · `China`@598.32 · `Russia`@599.92 · `Soviet Union`: `Soviet`@601.20 `Union`@601.52.
- **Camera** pull back slowly (continues into c4). **Out** `CA` → c4 (row slides left on c4's first word)
- **Done** key animation complete @601.50 (cut @602.02; hold 0.52 s).
- **SFX** 597.42 pop_soft · 598.30 pop_soft · 599.90 pop_soft · 601.18 paper_flip

## 11. Coverage tables

### 11.1 Effects (MANUAL §5 + §10)
| effect | scenes |
|---|---|
| #1 B-roll footage/photos | C3S001, C3S006, C3S050, C3S056, C3S059, C3S071, C3S076, C3S082, C3S096, C3S097, C3S102, C3S106 |
| #2 charts / diagrams | C3S021, C3S022, C3S023, C3S024, C3S029, C3S031, C3S040, C3S042, C3S051, C3S063, C3S065, C3S066, C3S085, C3S089, C3S090, C3S091, C3S093, C3S094, C3S095, C3S099, C3S107, C3S111 |
| #3 maps (incl. burn reveal) | C3S008, C3S009, C3S011, C3S014, C3S015, C3S037, C3S039, C3S044, C3S045, C3S046, C3S048, C3S049, C3S054, C3S067, C3S068, C3S073, C3S074, C3S078, C3S080, C3S088, C3S097, C3S098, C3S104, C3S105 |
| #4 film-title hero halate | C3S020, C3S026, C3S030, C3S039, C3S050, C3S059, C3S064, C3S071, C3S104 |
| #5 document / newspaper page | C3S005, C3S012, C3S016, C3S041, C3S044, C3S052, C3S055, C3S065, C3S069, C3S109 |
| #8 light streaks | C3S020, C3S026, C3S032, C3S043 |
| #10 Vox layered | C3S013, C3S062, C3S079 |
| #11 screens (varied) | C3S003, C3S018, C3S034, C3S092 |
| #12 collage / timeline / torn | C3S004, C3S013, C3S019, C3S025, C3S027, C3S035, C3S038, C3S043, C3S057, C3S058, C3S072 |
| #13 text animations (word-by-word in every scene; listed = odometer, count, typewriter, rise, list specials) | C3S001, C3S003, C3S004, C3S017, C3S026, C3S035, C3S073, C3S081 |
| #14 gate weave | C3S034, C3S050, C3S056, C3S059, C3S071, C3S076, C3S082, C3S096, C3S102, C3S106 |
| #15 curve cut | C3S002 |
| #16 hi-quality plate | C3S001, C3S006, C3S028, C3S030, C3S038, C3S053, C3S061, C3S069, C3S070, C3S075, C3S077, C3S083, C3S084, C3S086, C3S087, C3S101, C3S108, C3S110 |
| #17 2.5D | C3S020, C3S032, C3S064 |
| #18 rough + highlighter | C3S007, C3S010, C3S016, C3S031, C3S036, C3S041, C3S083 |
| #19 markups | C3S005, C3S007, C3S010, C3S014, C3S025, C3S027, C3S028, C3S031, C3S033, C3S035, C3S045, C3S049, C3S052, C3S060, C3S061, C3S063, C3S070, C3S075, C3S077, C3S084, C3S103 |
| #20 map callouts | C3S008, C3S011, C3S014, C3S045, C3S046, C3S049, C3S054, C3S074, C3S088, C3S098 |
| §10.6 call-outs (contrast / text / focal / radio waves / pen) | C3S005, C3S008, C3S010, C3S011, C3S014, C3S016, C3S045, C3S046, C3S049, C3S054, C3S055, C3S074, C3S086, C3S088, C3S098 |
| §10.5 paintings & posters as B-roll | C3S030, C3S061, C3S072, C3S075, C3S077, C3S087, C3S109 |
| focus hunt FH | C3S002, C3S005, C3S008, C3S016, C3S039, C3S047, C3S070 |
| chokeSettle CS | C3S007, C3S036, C3S060, C3S100 |
| whip W | C3S005, C3S008, C3S011, C3S014, C3S019, C3S022, C3S027, C3S031, C3S038, C3S045, C3S047, C3S051, C3S053, C3S060, C3S064, C3S070, C3S072, C3S077, C3S083, C3S087, C3S090, C3S095, C3S100, C3S105, C3S109 |
| light-flash whip FW | C3S015, C3S025, C3S029, C3S033, C3S036, C3S042, C3S049, C3S058, C3S066, C3S076, C3S080, C3S085, C3S091, C3S097, C3S103 |
| cut on action CA | C3S002, C3S004, C3S007, C3S010, C3S012, C3S017, C3S020, C3S026, C3S028, C3S032, C3S037, C3S039, C3S043, C3S046, C3S048, C3S052, C3S055, C3S061, C3S063, C3S069, C3S075, C3S079, C3S081, C3S084, C3S086, C3S089, C3S093, C3S096, C3S099, C3S101, C3S104, C3S107, C3S111 |
| hard cut on action HC | C3S016 |
| match cut MC | C3S001 |
| push-through PT | C3S003, C3S040, C3S092 |
| paper slide PS | C3S006, C3S009, C3S013, C3S024, C3S030, C3S034, C3S041, C3S044, C3S050, C3S054, C3S056, C3S059, C3S062, C3S068, C3S071, C3S074, C3S078, C3S082, C3S088, C3S094, C3S098, C3S102, C3S106, C3S108, C3S110 |
| #9 shutter/iris | ✔ none (retired, §10.1.6) |
| #6 sound | sound designer (SFX lines per scene + act music notes) |
| #7 textures | every scene (default stack; papers per §10.9) |

### 11.2 Reference layouts (intro pack D01–D15, originals R1–R12) — all reused as variations
| ref | scenes | variation in c3 |
|---|---|---|
| D01 | C3S029 | 2 bars, the second breaks the frame; halftone modern-SV cut-out (BEHEMOTH) |
| D02 | C3S065, C3S066, C3S095, C3S110, C3S111 | flag circles instead of portraits; equal pillars (Big Four), ranked (foremost power), flag row (P5) |
| D03 | C3S093, C3S099 | grid of country squares that turn hollow; strings to the US |
| D04 | C3S091 | single support bar past a dashed "kicked out" threshold |
| D05 | C3S051 | two lines (SV up / Taiwan down) + crisis band on graph paper |
| D06 | C3S085, C3S089, C3S107 | UN horseshoe seats; GA semicircle with new dots |
| D07 | C3S004, C3S027 | Terman legacy poster; video-card grid |
| D08 | C3S017, C3S103 | typed contract clause + ILLEGAL stamp; typed memo belief→assumption |
| D09 | C3S014 | 1860s New York map with the rejected code |
| D10 | C3S015, C3S045, C3S105 | tilted Rand McNally route NY→CA; tilted atlas Africa→China; Formosa 1943 map |
| D11 | C3S094 | Sankey flows US → countries (recognition) |
| D12 | C3S081 | dark list of US allies, focus pull to Japan |
| D13 | C3S023, C3S024, C3S037, C3S046 | dark line chart over ghost CA; Pacific ghost map with radio rings |
| D14 | C3S028, C3S074 | satellite strait + celadon Taiwan + yellow marker route |
| D15 | C3S021, C3S022, C3S040, C3S042, C3S063, C3S090 | Pan–Terman–Hewlett network; US↔CCP crossed; Taiwan↔US vs USSR |
| R1 | C3S029 | = D01 |
| R4 | C3S095 | = D02 |
| R5 | C3S024 | = D03 |
| R6 | C3S031 | tuition bar locked at zero |
| R7 | C3S057, C3S058 | timeline axis without values |
| R9 | C3S012, C3S019, C3S041 | callback cork board |
| R10 | C3S015, C3S049 | world atlas pins + circle on Taiwan |
| R11 | C3S009, C3S011, C3S097 | vintage colour-atlas US, CA watercolour; Western bloc |
| R12 | C3S008, C3S044, C3S054, C3S073, C3S080, C3S088, C3S104 | relief + fills (China/Taiwan drain, all of China, civil war spread, Africa, Warsaw Pact) |
| R2 | — | optional (owner) — not needed |
| R3 | — | skipped (owner) |
| R8 | (= D06) | parliament dots — C3S085, C3S089, C3S107 |

**New layout ideas (Pinterest/Vox-style, described for the editors):**
| idea | scene | description |
|---|---|---|
| video-card contact sheet | C3S004 | 3×3 ink cards (play triangle + progress bar) pinned at 12 fps on paper; fade to dashed outlines on "wouldn't exist" |
| vintage periodic-table page + pencil circle | C3S005 | real 1950s textbook plate, tilted; pen circle on Si; text call-out dims the rest |
| macro die → city grid match | C3S006 | push into an IC die's grid that dissolves into an aerial street/orchard grid |
| legal-pad argument notes | C3S007 | lined paper over cream, pencil underline + tick |
| redlined contract | C3S010, C3S017 | body-size highlighter + pen X; typed clause + ink stamp (his word "illegal") |
| photocopy light-bar | C3S015 | scanner bar sweeps the code card; an identical copy slides out ("copy pasted") |
| forum comments as paper slips | C3S025 | anonymous typed slips (no real usernames) vs his pen line "I think it did" |
| editor's pen correction | C3S033 | pen writes "best", strikes it, writes "very good" — his own self-correction |
| projector + pull-down screen | C3S034 | new screen type (§10.1.7): beam with dust motes, image on a screen with keystone |
| typed recipe index card | C3S035, C3S047 | ruled index card, typed ingredients each with a photo chip; later examined with a focal call-out |
| blueprint of Silicon Valley | C3S036 | title block "BUILT BY" — variation of intro IS037's blueprint |
| dark decade timeline | C3S043 | axis scrolls past decade ticks with streak smear, celadon dot holds centre |
| rewritten history page | C3S060 | typeset book page (our recreation) with a period woodcut; pen strike + rewrite |
| Cold-War domino row | C3S100 | CSS 3D dominoes with flag faces, 12 fps fall on "following suit" |
| UN horseshoe seats | C3S085, C3S089 | D06 dots arranged as the Security Council horseshoe, five permanent seats ringed |

### 11.3 Screens, 2.5D, maps, documents, paintings (variety check)
| kind | scenes |
|---|---|
| screens | C3S003 IBM 5154 · C3S018 Sony Trinitron · C3S034 projector + pull-down screen (new) · C3S092 Tatung (Taiwanese maker, for the Taiwan government) — four different sets, none repeated |
| 2.5D (the 3 moments that most deserve depth) | C3S020 Fairchild founders · C3S032 Hoover Tower · C3S064 Cairo 1943 (Chiang with FDR & Churchill) |
| maps | US satellite C3S008/C3S011 · vintage atlas US C3S009 · 1860s NY C3S014 · Rand McNally tilted C3S015 · ghost CA C3S023 · Pacific C3S037/C3S046 · Taiwan relief C3S044 · Formosa 1943 C3S045 · Taiwan satellite + clouds C3S048 · world atlas C3S049 · East Asia relief C3S054/C3S080 · world night C3S067–068/C3S078/C3S098 · China civil war C3S073 · strait satellite C3S074 · Europe/Warsaw Pact C3S088 · ghost world Sankey C3S094 · Western bloc atlas C3S097 · Africa C3S104 · tilted atlas C3S105 |
| documents / newspapers | Field code C3S012–015 · CA Civil Code 1872 C3S016 · contracts C3S010/C3S017 · Proc. IRE papers C3S041 · dissertation C3S044 · NYT 1971 C3S052 · Central Daily News C3S055 · 1945 front page C3S065 · UN Charter C3S069 · UN booklet C3S109 |
| paintings / posters (§10.5) | stanford-peninsula pictorial map C3S004 · Hoover painting C3S030 · OWI 'This man is your friend' C3S061 · Taiwan bird's-eye 1935 C3S075 · ROC 'recover the mainland' poster C3S077 · Sino-Soviet friendship poster C3S087 |
| footage | E01 die C3S001 · Taiwan 1960 clips C3S050/C3S076/C3S092 · WWII newsreel C3S059/C3S082 · civil war C3S071 · Soviet parade + US fleet C3S096 · factory C3S097 · rotary phone C3S102 · Ghana 1957 C3S106 · ROC walk-out C3S056 |

### 11.4 Ground rhythm (N night · P paper · G grid) — max run 3, PAPER+GRID combined max 3 ✔ (script-checked)
```
001N 002N 003N 004P 005P 006N 007P 008N 009P 010P 011N 012N 013P 014P 015P 016N 017P 018N 019N 020N
021G 022G 023N 024N 025P 026N 027P 028N 029P 030N 031P 032N 033P 034N 035P 036P 037N 038P 039N 040P
041N 042P 043N 044N 045P 046N 047P 048N 049P 050N 051G 052N 053N 054N 055P 056N 057P 058P 059N 060P
061N 062N 063P 064N 065P 066P 067N 068N 069P 070N 071N 072P 073N 074N 075P 076N 077P 078N 079P 080N
081N 082N 083P 084N 085P 086N 087P 088N 089P 090N 091P 092N 093P 094N 095P 096N 097P 098N 099P 100N
101P 102N 103P 104N 105P 106N 107P 108N 109P 110N 111P
```

Totals: NIGHT 59 · PAPER 49 · GRID 3. No face cam.

### 11.5 Transitions in order (never the same type twice in a row ✔; `cont.` = no cut)

MC, CA, PT, CA, W↓, PS, CA, W→, PS, CA, W←, CA, PS, W←, FW, HC, CA, CRT-off, W↑, CA, cont., W↓, cont., PS, FW, CA, W→, CA, FW, PS, W↑, CA, FW, PS, cont., FW, CA, W→, CA, PT, PS, FW, CA, PS, W←, CA, W↓, CA, FW, PS, W→, CA, W↓, PS, CA, PS, cont., FW, PS, W→, CA, PS, CA, W↑, cont., FW, cont., PS, CA, W←, PS, W↓, cont., PS, CA, FW, W→, PS, CA, FW, CA, PS, W↑, CA, FW, CA, W→, PS, CA, W↓, FW, PT, CA, PS, W↑, CA, FW, PS, CA, W→, CA, PS, FW, CA, W←, PS, CA, PS, W↑, PS, CA → c4.

### 11.6 Hold check (§10.9) ✔
Every scene's key animation completes ≥ 0.5 s before its cut (script-checked; tightest: C3S001 0.52, C3S006 0.52, C3S026 0.53, C3S042 0.54, C3S101 0.52, C3S108 0.53, C3S110 0.54, C3S111 0.52 → c4). Short scenes (C3S001, C3S037, C3S059, C3S102) use quicker 0.3–0.5 s text rises — the one allowed exception to the 1.0–1.6 s entrance rule; editors keep them ≥ 0.3 s.

### 11.7 Palette check (lead's cross-chunk decision)
- Acts I–IV: vermilion West/Stanford/SV/California — C3S004, 006, 008–011, 015, 023–024, 028–029, 036–038, 040, 042, 046 (the
  Fairchild tree C3S021–022 is ink); navy East/New York — C3S013–014; celadon Taiwan/Pan — C3S037–046, 048. Vermilion + celadon
  share a frame only in C3S037, C3S040, C3S042, C3S046 (exactly two accents).
- Acts V–X: red = CCP / PRC / USSR / Warsaw Pact — C3S053, 054, 060, 063, 072, 073, 086, 088, 090, 095, 096, 106, 108;
  celadon = Taiwan/ROC — C3S048–111 wherever meant; navy = US (+ allies) only when contrasted — C3S051, 063, 090, 094, 095, 098, 099.
  No vermilion-as-West after 235.94 (C3S049 pins are ink, C3S051's Silicon Valley line is navy).
- Yellow: highlighters (C3S010, 016, 031, 041, 066, 083, 089, 107) + yellow marker routes (C3S015, C3S074). No yellow key number in
  c3 ("1965" is a bone halate).

### 11.8 Words ↔ visual (§10.1.3) — risky lines and how they're handled
| words | handling |
|---|---|
| "This podcast that's like changing your guys' lives" | the podcast itself (player on an IBM 5154) — not a face, not a mood shot |
| "I think a Silicon Valley TV show has an episode on this too" | the real show on a Trinitron (© HBO, fair use) |
| "If you like to get good historians" (garbled) | Hoover Institution video on a projector screen — the sentence's subject |
| "where we think Silicon Valley was built by someone" | blueprint with a "BUILT BY" title block |
| "he's not paying attention…" (slip for "now") | the meaning: radio rings from SV reaching Taiwan; no text on the slip |
| "CCP stay out of World War II" (claim; no fact-check) | no typographic restatement; the diagram crosses the US↔CCP link on "wasn't"; next shot shows who fought (ROC, Cairo) |
| "they're still the government of Taiwan" (likely "of China") | the poster of their intent to return; text only `temporary`/`inconvenience`/`still` |
| "Very far away from China, but unfortunately." | a dashed distance line Africa → China only |

## 12. Open questions (defaults in DECISIONS.md)
1. Colour mapping → **resolved by the lead** (LONGFORM end): Acts I–IV vermilion West / navy East; Acts V–X red = CCP/Communist bloc, celadon = ROC, navy = US when contrasted.
2. Switch point 235.94 ("everyone wants Silicon Valley, but why did Taiwan…") — from there Silicon Valley is navy (US). → **yes**.
3. "Hoover Institute" → on screen "Hoover Institution"? → **yes** (accurate name).
4. Show his self-correction best → very good as a pen correction? → **yes** (it is exactly what he says).
5. Political claims (CCP & WWII) — minimal text, visuals of who fought? → **yes**.
6. Fair-use press items (NYT 1971, Central Daily News, UN Photo, HBO still, Traitorous Eight, Hoover video) — credited, transformed → **yes**.
7. Pan Wen-Yuan Chinese characters 潘文淵 as a sub-label? → **no** by default.
8. 1971 date of the UN vote isn't spoken — print it? → **no label**; the real dated front page is enough.

