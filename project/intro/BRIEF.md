# Intro edit brief — "Taiwan: the chip rivalry" (Searching Lessons), INTRO 0.00–275.06 s

Read first: `USER_BRIEF.md`, `MANUAL.md` (all — **§10 is Krish's round-2 rules and overrides older sections**), `EDITOR_BRIEF.md`,
`AGENT_BRIEFS.md`, `SOURCES_INDEX.md`, this file.

## Inputs
- VO: `vo_intro.mp3` (= `input/Final Full Audio.mp3` 0–275.06, stream copy — never process it).
- Word timings: `transcript_intro.json` (Parakeet; 838 words). Full-video transcript: `project/transcript_full.json`.
- Face cam: `input/Face Cam.mp4` (1920×1080, 29.97 fps, 4:35). Face-cam time = VO time − 0.026 s.
- Palette: `lib/palette.css` (approved): red = TSMC / Morris Chang, blue = UMC / Robert Tsao, celadon = Taiwan, yellow =
  highlighter + one key number, everyone else neutral. Swatch `references/palette_taiwan.png`.

## Krish's rules for this intro (all binding)
1. **No narrator on camera in the first 10 s.** After that the face cam appears **5–6 times, 1–3 s each**, only on lines where
   he talks to the viewer (≈171 "Guess who was the founder…", ≈196 "That's the story I want to share…", ≈246 "I'm your host,
   Sam…", 251–270 the "face built for radio / camera lights / sweat" joke — allowed, in 1–3 s pieces). Face cam stays **clean
   and modern** (no film grade on him). Allowed: our text treatments; **graphics behind him** (remove-background → room plate →
   our chart/map/news graphic → narrator cut-out → text).
2. **Every visual matches the exact words under it** (MANUAL §10.1.3). No mood shots over a line that says something else.
3. **Accurate spellings on screen** even when mispronounced/mis-transcribed: Robert Tsao (ASR "Robot Cao", "Sao", "Xiao"),
   Morris Chang, UMC (United Microelectronics Corporation), TSMC (Taiwan Semiconductor Manufacturing Company), Hsinchu Science
   Park ("Shin Shu Park"), host Sam, show "Searching Lessons". On-screen text = what he says; no fact-checking otherwise.
4. **B-roll includes paintings, oil paintings, illustrations and vintage posters** (Krish's examples: illustrated California
   maps, Wild West poster art, a pictorial Palo Alto map) — a colour painting of a famous figure often beats a B/W photo. Same
   rule as all B-roll: it must match what's being said. PD/CC/free only, logged in SOURCES.md.
5. **Vintage grid and ruled paper** grounds (look of Creative Market "Vintage Ruled Grid Paper Textures" — reference only,
   not bought, never vector-recreated): real scanned paper (archive.org `kecatalog` = K+E Graph Sheets Catalog 1960, old
   ledgers/notebooks, Texturelabs paper). **Vintage instruction manuals** of the era (chip/telephone/computer manuals,
   datasheets — archive.org, bitsavers) are great visuals.
6. **Reference layouts to rebuild** (MANUAL §6.1): `references/style-images/intro/D01–D15.jpg` — use as many as the narration
   allows; leftovers carry to chunk 1. D01 4 % bars+building, D02 ranked bars with portraits, D03 isotype grid with labels,
   D04 horizontal bars on paper, D05 line chart with era band, D06 parliament dots + highlighted title, D07 moonshine-ad
   collage poster (photos + typographic boxes + stamps), D08 telegram, D09 old city map, D10 tilted close-up topo map with
   route lines, D11 dark Sankey money flow over a ghost US map, D12 dark list of amounts with blurred bars (focus pull),
   D13 dark line chart over a ghost map, D14 satellite view with highlighted districts + yellow route, D15 relationship
   diagram (portrait circles + arrows + money labels) on paper. Also: look for similar Pinterest-style references for
   scenes not covered by these (describe the source in the notes).
7. **Round-2 craft** (MANUAL §10): halation only on a scene's hero element; rough reveals settle; long smooth eases
   (`FX.ease.*`, 12 fps); cuts on action; **whip transitions** (`FX.whip`) instead of the iris; DSLR focus hunt after fast
   zooms; better screens (Tatung TVs, Trinitron, IBM PC, terminals) when footage is framed; ≤ 2 uses of any photo/clip.
8. **Sound**: layered Epidemic Sound bed (reference playlist `references/audio/epidemic_playlist_documentaries.json`, anchor
   "Melting Glass"), stems via `tools/epidemic_fetch.py`; SFX on objects, quiet; never one single music track.

## Story (intro) in one paragraph
1983: Robert Tsao, CEO of Taiwanese chip company UMC, walks his factory floor and has an insight. A year earlier Taiwan's
telephone exports to the US went from 4 million to 24 million units (6× in 12 months); UMC made the chips inside those
phones → record profits in its first full year; then the phone boom died and UMC's sales with it. Insight: a chip factory
should make chips for anything in demand — a pure-play **foundry**, which didn't exist anywhere in 1983. He asks his board;
UMC was ~1 year old; the board is excited but sets one condition: get approval from their advisor, the most respected
Chinese-American chip executive, running a 25,000-person global chip division at one of the biggest companies in the world
(Morris Chang, unnamed until the reveal). Tsao flies to New York, great meeting + dinner, flies home on top of the world —
but the board has gone cold, stonewalls him; in Taiwan in 1984 you did nothing without your board, so he drops it. Two
years later a new chip company breaks ground across the street from UMC, making chips for anyone and never its own product
— Tsao's plan "bar for bar" (narrator's words). Founder & CEO: the same executive — Morris Chang; the company: TSMC. The
betrayal starts a rivalry that built Taiwan into a chip superpower; TSMC wouldn't be world-renowned without these two men
one-upping each other for decades; Hsinchu Science Park, a replica of Silicon Valley (per a Taiwanese leader); countless
countries tried to recreate Silicon Valley and failed. Host intro ("I'm your host, Sam, and this is Searching Lessons"),
the "face built for radio / camera lights / sweat" joke, "enjoy the historic images and B-rolls… here's the story."

## Folders
- Planning: `project/intro/` (analysis/BEATS.md, EDIT_NOTES.md, ASSETS_NEEDED.md, SEGMENTS.md, DECISIONS.md).
- Assets: `assets/intro/<type>/` + `SOURCES.md` per folder. Face-cam cut-outs: `assets/facecam/` (gitignored, regenerable).
- Compositions: `compositions/introNN.html` (+ `introNN.sfx.json`, `introNN.NOTES.md`).
