# SEGMENTS — podcast "TSMC vs UMC" (Searching Lessons), master 0.00–5752.03 s (95:52) — the shared plan for every editor

Lead: the lead session. Owner: Krish (asleep — never wait for answers; decide sensibly and write it in your NOTES).
Read first, in this order: `project/podcast/BRIEF.md` (Krish's binding rules), `CLAUDE.md`, `MANUAL.md` (ALL of it: §0, §3–§6.1, §4.2
gotchas, §10 incl. §10.6 call-outs and **§10.10 design notes**, which override older sections), `EDITOR_BRIEF.md`, THIS file,
`project/podcast/sections.json` (your compositions: exact start/end), the analyst notes for your range
(`project/podcast/analysis/part*_notes.md` — names, spellings, slips, verbatim quotes). Quality bar and code to copy: the Paraguay
and Ivan edits (`compositions/pys0*.html`, `compositions/ivs0*.html`, `project/paraguay/SEGMENTS.md`, `project/ivan/FIXES_ROUND1.md`)
and — because this podcast tells the SAME story — the Taiwan long-form edit: `compositions/intro01–03.html` (Tsao 1983 → Chang
reveal), `c1s01–c6s03.html` (Silicon Valley, Terman, HP, Shockley, Fairchild, Kilby, Moore, the UN in 1971, Chiang, Sun Yun-suan,
K.T. Li, Pan Wen-yuan, RCA …) with their plans `project/intro/EDIT_NOTES.md`, `project/c*/…` and asset libraries
`assets/intro/`, `assets/c1…c6/` (each with ASSETS/SOURCES files). **Port those scenes and assets wherever the words match** —
re-timed to THIS take's words, in THIS video's palette, upgraded to the rules below. Never reuse the old timings.

## 0. What this video is
A two-person video podcast: **Sam** (host, tells the story) and **Sunkit** (co-host, asks questions). The source picture is an
already-switched programme (split screen / Sam single / Sunkit single). Krish's rules:
1. **First 5 minutes = business as usual**: a full documentary edit exactly like Paraguay / Ivan / Taiwan (B-roll, maps, charts,
   call-outs, sound design, cut on action, whips) — compositions **pd01–pd03** (0.00–346.00 s).
   Face-cam rules: **no speaker on camera for the first 10 s**; after that **short 1–2 s on-camera pop-ins** (never longer than ~2.5 s),
   on lines where a speaker addresses the viewer or the other host, and for Sunkit's questions in the aside (raw 184–230 s).
2. **After that the speakers carry the video.** Edited sections exist ONLY where a visual is truly needed to explain the story or
   clearly improves the viewing experience — compositions **pd04–pd44**, each listed in `sections.json` with its reason.
   A section is a full-frame graphic piece that hard-cuts in from the speakers and hard-cuts back. No face cam inside sections.
3. **References come only from inspo-frames ASSETS** — saved in `references/inspo-assets/` (`INDEX.md`, `assets.json`,
   `sheet_1–3.jpg`, `img/<id>.webp`). Use only what fits; rebuild in our style per MANUAL §6/§6.1 (structure from the reference,
   OUR fonts/palette/textures/motion, the narration's real words and numbers). **Your NOTES must name the asset id that inspired
   each scene** (or "none — ported from <old scene>"). §5 below maps references to scene types.
4. Accuracy: every visual matches the exact words under it; facts, names and spellings correct (§4).
5. Palette: `lib/palette_podcast.css` (auto-loaded for `pd*`), swatch `references/palette_podcast.png` (§2).
6. **No narration captions** (MANUAL §0, Krish's Paraguay review): never put the spoken sentence on screen. Allowed text: map and
   place labels, name tags, chart/diagram text (titles, values, axis, explanatory labels), dates as titles, document/newspaper text,
   credits, and a line the speaker explicitly quotes (e.g. Chiang's "stay dignified and strengthen ourselves", the NTU slogan,
   "father of Silicon Valley" as a name-tag subtitle). When in doubt, no text.

## 1. Technical frame
- **Master**: `vo_pd.mp3` (preview of the cut voice track; never process it), word timings **`transcript_pd.json`** (master seconds;
  each word also has `raw_id`). Raw-take times in the analyst notes are NOT master times: use `sections.json` (`start`, `end`, `dur`,
  `first_word`) and look words up in `transcript_pd.json`. Quick dump: `python3 project/podcast/gen/pd_words.py <t0> <t1>`.
- **Frame rate: the final video is 30 fps** (the A-roll's rate) and compositions are rendered at 30 fps. Author in seconds as always;
  `FX.choppy(…, 12)` stays. Every section `start`/`end` is on the 30 fps grid.
- **Composition**: `compositions/pdNN.html`, composition id `pdNN`, root
  `<div id="root" data-composition-id="pdNN" data-vo-start="START" data-duration="DUR" data-width="1920" data-height="1080">` with START and DUR
  exactly as in `sections.json`. `const T = s => s - START` (text cues), `S` (same function; structural cues). Temp audio for your
  previews: `<audio id="pdNN-vo" class="temp-vo" src="vo_pd.mp3" data-start="0" data-duration="DUR" data-media-start="START" data-volume="1">`.
  Element ids prefixed `pdNN-`. No `font-family` in composition CSS. Scenes hidden outside their window; per-frame FX gated.
- **Sections (pd04+) start and end on a hard cut from/to the speakers**: frame 0 must already show the scene's ground and the
  first element in motion (set initial states with `gsap.set`, MANUAL §4.2) — no black, no fade from black, no empty paper for
  more than ~6 frames. Let the key animation finish and hold ≥ 0.5 s (MANUAL §10.9); the last frame is a complete, clean picture
  (a slow camera drift may continue through the cut). Timing is tight on purpose: a section's first/last words are in `sections.json`
  — if you believe a boundary should move (max ±1.5 s, to a sentence start), say so in NOTES with the exact new master times; do not
  change START/DUR yourself.
- **Intro (pd01–pd03) is continuous**: pd01 starts at 0.00 with a designed opening (no speaker for the first 10 s); pd01→pd02 and
  pd02→pd03 cut on action / whip (write your first and last scene in NOTES; the next editor continues with a fresh shot);
  pd03 ends at 346.00 on a hard cut to Sam on camera ("So this is the rivalry, and this is the story that I want to share today").
- **Face cam (intro only)**: `assets/facecam/pd_facecam_intro.mp4` — 1920×1080, 30 fps, **aligned to master time** (frame at master
  t = media time t; covers 0–397 s). `<video id="pdNN-fcK" class="clip" muted playsinline src="assets/facecam/pd_facecam_intro.mp4"
  data-start="LOCAL" data-duration="D" data-media-start="MASTER_T" …>`. It is the switched programme: LOOK at the frames of the
  moment you want (`ffmpeg -ss T -i assets/facecam/pd_facecam_intro.mp4 -frames:v 1 x.jpg`) — it may be the split screen, Sam alone
  or Sunkit alone, and it changes layout by itself. Keep it clean (no grade, no texture on the speakers); never start or end a pop-in
  within 0.2 s of a layout change in the source; punch-in origin above the faces. A 30 fps clip in a 30 fps render needs no offset.
- **Sound**: you add no music. Write per-object SFX markers to `compositions/pdNN.sfx.json` as `[{ "t": LOCAL_SECONDS, "type": "...",
  "scene": "...", "dur": …, "level": "normal|quiet", "note": "…" }]` (types as in `compositions/pys0*.sfx.json`; restraint: the hero
  move of each scene, whips, big reveals — MANUAL §10.8). Music and SFX will sit far under the voices (new limits), so do not rely on
  sound to explain anything.
- **Work in a sandbox** (`tools/make_sandbox.sh pdNN`, then `cd work/pdNN && python3 tools/build_index.py pdNN --root . &&
  npx --yes hyperframes@0.8.217 lint && npx --yes hyperframes@0.8.217 snapshot --at … --no-end -o .snap/x`). `export PATH=~/.local/bin:$PATH`
  first. **This machine is shared by ~10 agents and a long ffmpeg job**: snapshot at most 6 frames per call, never render, never run
  two heavy commands at once, no background jobs left behind, scratch files only in your own `work/pdNN/` folder.
  LOOK at every snapshot (Read the PNG) before you call a scene done; check the first frame, the last frame and the text frames at 100 %.
- `python3 tools/sync_audit.py compositions/pdNN.html --transcript transcript_pd.json` — every text cue 0–120 ms before its word.
- Deliver per composition: `compositions/pdNN.html`, `compositions/pdNN.sfx.json`, `compositions/pdNN.NOTES.md` (scenes with master
  times and the words each covers, the inspo asset id per scene, assets used/new, deviations, open issues). New assets go to
  `assets/podcast/pdNN/` with a `SOURCES.md` (subject, URL, licence/"© owner, fair use", author, date). Do NOT commit or push; do not
  edit files that are not yours (`lib/`, other compositions, MANUAL). If you need a new FX helper, put it inside your composition.

## 2. Palette — `lib/palette_podcast.css` ("the colours of a chip fab"); three story colours + lemon; shades only
| colour | tokens | means |
|---|---|---|
| **Magenta** (photoresist) | `--magenta` #d1307a (= `--vermilion`), `--magenta-dark` #7a1746, `--magenta-light` #f3a6c8 | **TSMC & Morris Chang**; the primary emphasis colour (markup circles, pins, the betrayal). Before Chang is revealed (master ≈ 314 s) the unnamed executive is NEUTRAL silicon — never magenta, never a recognisable face. |
| **Copper** (amber) | `--copper` #e0882a (= `--navy`), `--copper-dark` #8a4f0f, `--copper-light` #f6c98a (= `--sky`) | **UMC & Robert Tsao** |
| **Board green** | `--board` #2f9e5b (= `--celadon`), `--board-dark` #17603a, `--board-light` #9bd8b0 | **Taiwan** itself: the island on maps, Hsinchu, the ROC government, Taiwanese officials |
| **Silicon** (cool neutrals) | `--paper` `--paper-2` `--ink` `--night` `--bone` `--ash` `--ash-light` `--ash-dark` | grounds, ink, photo tints; **everyone else**: the US, Silicon Valley, Stanford, Terman, HP, Bell Labs, TI, Japan, the PRC, the UN |
| **Lemon** | `--yellow` #f2e24a | ONLY the highlighter and the ONE key number of a scene |
Rules: max two accents per frame; photos desaturated / silicon duotone so accents pop; every fill under a texture; thin lines and text
on night use the LIGHT shade; paper scenes never glow, `.halate` only on the one hero title/number of a night scene. In the long
US-history part (pd04–pd19) there is no Taiwanese actor: use magenta as the single emphasis accent (markups, the highlighted bar,
the key pin) and keep everything else silicon; copper may serve as the "second series" of a chart. From pd20 on: Taiwan/ROC = green,
PRC/CCP = neutral dark ash with magenta ONLY as markup emphasis (do not paint China magenta — magenta is TSMC's), the US = ash-light.
Old Taiwan-edit code uses red = TSMC, blue = UMC, celadon = Taiwan: the tokens map over automatically (`--vermilion`, `--navy`,
`--celadon`), but replace any hard-coded hex colours.

## 3. Compositions — see `project/podcast/sections.json` for exact times (`python3 project/podcast/gen/sections.py` prints the table)
| editor | compositions | story |
|---|---|---|
| ED01 | pd01 (0–113.77) | "Our story starts in 1983 with Robert Tsao", CEO of UMC, walking the factory floor: an insight. A year earlier Taiwan's telephone exports to the US: 4 million → 24 million units in 12 months (6×). UMC made the chips inside → record profits in its first full year; the US phone boom dies, UMC's sales die. A chip factory should not bet on one product → make chips for any product in demand: a pure-play foundry, a novel concept in 1983. He must ask his board: UMC is one year old, he is a hired CEO, not a founder. |
| ED02 | pd02 (113.77–227.37) | The board is excited and says yes — with one condition: share the plan with their adviser, a high-level chip executive in the US, "the most respected Chinese American in the chip business", managing 25,000 people. Tsao flies to New York; the meeting goes well; dinner; he flies home on top of the world. Then the aside: Sunkit asks why a competitor advises them; Sam: he is in the US doing cutting-edge work, advising Taiwan on the old stuff, not on the board. |
| ED03 | pd03 (227.37–346.00) | Back in Taiwan the board has gone cold; he is stonewalled and drops the idea. Two years later, across the street from UMC, a new company that only manufactures chips for anyone. Its founder: the same executive from New York — **Morris Chang**; the company: **TSMC**. Betrayal → a two-decade war → a rivalry that has not died down. |
| ED04 | pd04 pd05 pd06 | Terman name card; the trillion-dollar map (12 companies, 11 west of the Mississippi, 1 east — **no state or company names on it: Sam runs a quiz**; port the approved `s02-map`/`s01`), 1926: 90 % of GDP in the East / 10 % West, students leaving Stanford and Berkeley for New York, New Jersey, Massachusetts (Bell Labs, General Electric); Hoover name card. |
| ED05 | pd07 pd08 pd09 pd10 | Terman's background and Boston (MIT, Harvard); Vannevar Bush / Raytheon; 1938 Hewlett & Packard; the audio oscillator and what Terman gave them. |
| ED06 | pd11 pd12 pd13 | Steeples of excellence → transistor inventors → how a transistor works; Shockley to Palo Alto; Stanford's 8,000 acres and the 99-year lease. |
| ED07 | pd14 pd15 | The hand-wiring problem; the Traitorous Eight and Fairchild. |
| ED08 | pd16 | Kilby's integrated circuit (Texas Instruments) → germanium vs silicon, Noyce → semiconductor → "Silicon Valley". |
| ED09 | pd17 pd18 pd19 pd20 | Moore's Law; California's non-compete accident and the Field Code; 1971 chapter opener. |
| ED10 | pd21 pd22 pd23 pd24 | ROC/CCP, the four policemen; the ROC flees to Taiwan; recognition blocs; Japanese rule. |
| ED11 | pd25 pd26 pd27 pd28 | US aid; Chiang Kai-shek; the NTU slogan; special economic zones. |
| ED12 | pd29 pd30 pd31 pd32 | Kissinger's secret trip; Africa's new votes; July → October and George H.W. Bush; the "important question" (66 %). |
| ED13 | pd33 pd34 pd35 | The walkout and its aftermath, Chiang's quote; Chiang Ching-kuo; Deng Xiaoping reveal. |
| ED14 | pd36 pd37 pd38 pd39 | Sun Yun-suan and K.T. Li; the Ten Major Projects; Pan Wen-yuan (RCA); the value chain and "four years, ten million dollars". |
| ED15 | pd40 pd41 pd42 pd43 pd44 | The "Taiwanese shield"; the research-institute model; the Silicon copycats; Route 128 and DEC; Christensen's Innovator's Dilemma. |

Inside a section, build scenes of 4–12 s that follow the words; where a section contains banter or a question from Sunkit, hold the
current image with a slow move (never an unrelated scene). Name cards land on the NAME as it is spoken, not before (do not spoil
reveals: "HP founders" is Sunkit's answer; Deng Xiaoping is revealed on the name; the executive is unnamed until "Morris Chang").

## 4. Spellings and facts on screen (ASR → correct). The speakers' words otherwise; numbers as spoken; never show a slip
Robert **Tsao** (ASR Cao/Sao/Chao) · **UMC** (United Microelectronics Corporation) · Morris **Chang** (Shang) · **TSMC** (also ASR "PSMC",
"TSM C") · **Hsinchu** Science Park (Sin Shu) · Frederick / Fred **Terman** (Turner, Termin, Kerman) · Leland Stanford · Herbert Hoover ·
**Vannevar Bush** (Vanaver Busch) · Raytheon · Bill **Hewlett** & David **Packard** · William **Shockley**, John **Bardeen**, Walter
**Brattain** · Bell Labs · the **Traitorous Eight** · **Fairchild** Semiconductor · Jack **Kilby** (Jake Kelby) · Texas Instruments ·
Robert **Noyce** · **germanium** (Germania) · **Moore's Law** (Morse) · David Dudley **Field** / the Field Code (David Fields) ·
**Chiang Kai-shek** (Chien Ka Shek) · **Mao Zedong** · Henry **Kissinger** · George H.W. **Bush** · **Chiang Ching-kuo** · **Deng Xiaoping** ·
**Sun Yun-suan** (Sun Yu Swan) · **K.T. Li** (Keiki Li) · **Pan Wen-yuan** (Pen Wen Juan, Panwan) · RCA · **Route 128** (ASR "Roueight" —
he says Route 128) · **Digital Equipment Corporation / DEC** (ASR "DC") · AnnaLee **Saxenian** · Clayton **Christensen**, *The Innovator's
Dilemma* · Silicon Alley / Silicon Fen / Silicon Wadi / Silicon Saxony / Silicon Plateau / Silicon Glen · ROC = Republic of China
(the Nationalists, Taiwan) · CCP = Chinese Communist Party · PRC.
Slips — do NOT put on screen: "two thousand tens and twenties" (he means the 1910s–20s); "going out west" for east; "Wilson's
administration" (he is unsure); "in four years in 1945" for the civil war's end (show no year there — or only "CCP wins the civil war");
"against China in World War II" (means Japan); "1946" for New York's codification (show no year); "Stanford founded in 1890" may be
shown as spoken only if needed (prefer no year). When a spoken fact is doubtful, show the image without the number.
Krish's rule (MANUAL §0.9): on-screen text follows the narration — no fact-checking — but names are always spelled correctly.

## 5. The inspo-frames reference menu (rebuild in our style; ids are the last 8 characters; full list in INDEX.md)
| scene type | references | idea to take |
|---|---|---|
| country / region maps | `7c824c47` (3-D relief, one country filled), `8a634241` (two countries in one accent with pins + city labels), `e2d14822` (two blocs in two colours on a dark sea), `9b4c4611` (flat textured country, city dots + small-caps labels), `813e40ef` (empire fill over dark relief), `64e14029` (inset focus box on a dark satellite map), `8689427d`, `16774fce` (pale hand-drawn atlas) | our map kit (`assets/maps/kit/`: world, us, bay_area, northeast, east_asia, taiwan, pacific … atlas / night / sat / satdesat + overlay SVG + json), fills in the palette under halftone/texture, labels per Ivan FIXES §1 |
| routes / journeys | `73184e83` (route line with dots and labels over relief) | Kissinger's trip, the brain drain, the Field Code moving west, Tsao's flight to New York |
| a person on a map | `b57b4e0e` (vintage map, marker outline round the country, pinned photo with name label) | Shockley → Palo Alto, Pan Wen-yuan, the executive in New York |
| many places at once | `5fc04bfb` (isometric map with pins and small portraits/buildings) | the Silicon copycats, Stanford Industrial Park, Ten Major Projects |
| person introduced | `ccc84f71` (B/W cut-out over colour blocks + small related photos), `566a46e7` (cut-out + quote + grid paper + props), `f3ea432e` (portrait + circle photo + year tag + map panel), `6af0421b` (outlined cut-out + big year + building + short line), `e7774dbc`, `50ad486a` | the standard name card of this video: desaturated cut-out, one accent block, Haskoy name, `t-label` role line, 1–2 related photos; vary layout every time |
| groups of people | `455f4813` (heads collage over a building), `8e364ca5` (ID photos with name strips), `10434ee1`, `b2d84747`, `8be645e2` (photo boards / desks) | the board of directors, the Traitorous Eight, the cabinet of engineers, Bell Labs three |
| two rivals | `0a134429` (two cut-outs back to back with flags + objects), `ab8146d1` (two men at a table under a headline), `549d4839` (red halftone face) | Tsao vs Chang; the New York dinner (executive as silhouette); the betrayal |
| headlines / documents | `b5214313`, `b3974b01`, `a7bd471a` (headline with highlighter on paper), `96a54925` (newspaper as an object), `f76a4410` (typed letter), `990c442a` | real headlines/documents when they exist (fair use, credited), highlighter per §10.6; typeset recreations never fake a real masthead |
| big-number / date titles | `62b64549`, `10fe493f` (huge numerals with a painting inside), `6af0421b`, `fbd84a66` (torn-paper title) | 1983, 1971, 1947, 1938 chapter beats |
| charts | `2ebb47ad` (two-area line chart on a grid with tags), `255d4d29` (dark curve with dated milestones), `c01248c5` (thin lemon bars, serif title), `a06c4bb3` / `d0fc4b3f` (grid of tiles with a share call-out) | phone exports 4 M → 24 M, boom and bust, Moore's Law, 11 of 12, 90/10, 66 %, the innovator's dilemma |
| explainers / diagrams | `b76c4b43`, `3dbd4abf` (grid-paper desk, isometric diagram cards, hand labels, tape) | foundry idea, transistor switch, wiring problem, integrated circuit, economic zone, institute model, value chain |
| footage on a screen | `abbb4a75` (TV + hand-drawn arrow note), `b42f48f8` (three rounded screens) | archival footage (factory floor, phones, cleanrooms); MANUAL §10.1.7 screens |
| photo sequence | `4abe44bc` (centre photo sharp, neighbours blurred) | walkout photographs, archive runs |
Do not use: `3937428e` (HUD), `4e6642fa`, `94ec4f14`, `76064062`, `9bcc4687`, `ad12498d` unless a scale/weighing metaphor is really said.

## 6. Checks before you report (each composition)
lint 0 errors · sync audit clean · snapshots looked at (first frame, every scene mid + last 0.5 s, every text frame at 100 %) ·
grid 96/72 px, one focal point, nothing touching edges or faces · contrast · one text idea at a time · no narration captions ·
names spelled per §4 · palette tokens only (no stray hex from old projects) · map labels on every map · no repeat of the same
treatment back to back · timeline `tl.duration()` ≤ DUR · sfx.json + NOTES.md written (with the inspo asset id per scene).
Report: compositions built, scene count, references used, new assets, anything unfinished or doubtful, boundary change requests.
