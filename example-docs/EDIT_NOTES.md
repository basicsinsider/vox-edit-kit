# EDIT NOTES — "Silicon Valley wasn't inevitable" (VO 0.00–600.00)

Shot-by-shot plan for the full 10-minute edit. Read with `MANUAL.md` (style, effect catalog §5, reference
layouts §6), `analysis/BEATS.md` (beats, ASR name fixes, key-word cues — its §5 fact check is NOT applied on screen, see §0), `ASSETS_NEEDED.md` (sourcing) and
`SEGMENTS.md` (who builds what, shared conventions).

## 0. How to read this file

- **Times** are voiceover seconds (`vo10.mp3`). Scene boundaries sit on word starts from `transcript.json`.
  94 scenes, SC001–SC094, contiguous, no gaps, 0.00 → 600.00.
- **Text cue `@t`** = the start time of the spoken word. Put the text's first visible frame at `T(t) − 0.06`
  (MANUAL §4.4: 0–120 ms before the word). Structural moves (camera, exits) are free.
- **Ground**: `PAPER` (`--paper` + paper-tex + folds) or `NIGHT` (`--night`, cinematic). Never more than 3 in a row.
- **FX** numbers = MANUAL §5 catalog. The first number listed is the scene's **primary** effect; no primary
  repeats back-to-back (checked in §9). `#6 Sound` and `#7 Textures` run on every scene (default grain + dust +
  vignette, MANUAL §3.3) and are only listed when they are the point of the shot.
- **Ref** = reference layout from `references/style-images/` (R1, R4–R12; R2 optional/not used, R3 skipped),
  always rebuilt in our three fonts and palette, always animated (12 fps pops, draw-ons, counters, drift).
- **Copy** = the approved sample (`compositions/sNN-*.html`) whose code to start from.
- **Asset IDs** (`A01`…) point to `ASSETS_NEEDED.md`. Paths in `assets/…` already exist.
- **SFX** lines are object events with absolute VO times; editors copy them into `compositions/segNN.sfx.json`
  (format in SEGMENTS.md). Keep every SFX quiet (far under the VO).
- **Text style shorthand**: `display` = `t-display` (Haskoy), `label` = `t-label` (Cooper Hewitt caps),
  `serif`/`serif-i` = Crimson Pro, `+halate` on night, `.label-box` / `.hl` on paper.
- **Colour code (fixed)**: West = vermilion, East = navy, yellow = highlighter or the one key number of a scene.

### Text policy (user decision, 2026-10-29 — overrides BEATS.md §5)

- On-screen text follows **exactly what the voiceover says**. No fact-checking, no "neutral wording": show
  "90% of US GDP" as a plain stat, "invented the IQ test", "PhD", "finishes at 24, in 1924", "founded in 1891",
  "president in the 20s", etc. as narrated. Do not add dates/names the VO doesn't say unless purely as a visual label of
  an object already on screen (and keep those to a minimum).
- **Only** correct ASR spellings of names: Herbert Hoover (ASR "Harvard"), Frederick Terman ("Federick Turner",
  "Fredric", "Federic", "Termin"), Lewis Terman ("Louis"), Vannevar Bush ("Vanuar"), Packard ("Packett"), AT&T ("ATT"),
  plus "Board of Trustees" (ASR "trustee") and "changes" ("chang").
- Narrator slips/repeats (BEATS §2b) still get **no** on-screen emphasis: no second logo on the repeated "Bell Labs, General
  Electric", no text on "one of those people, or one of these people", "goes to, goes to, goes to", "finds when I say finds",
  etc. Where the narrator self-corrects (B073 "out west. Or … out east"), show the word he lands on (**East**).

---

## 1. Act 0 + Act I — The trillion-dollar West (0.00–54.48)
Music: soft pad under SC001; `curious_neutral_Dmaj_96bpm` (marimba + pizz) enters on "Silicon" @4.32 and
drives Act I with a light, confident groove. Small `stinger_reveal_Dmaj` on the West burn reveal @35.36.

### SC001 · 0.00–4.32 · B001 · NIGHT
- **FX** #8 light streaks (+#7) · **Ref** — · **Copy** s01 (streak canvas only)
- **Text** none ("After him?" is unclear in the ASR — do not caption).
- **Visual** black ground, fractal-noise streaks fading up from 0 to ~0.35 opacity, warm tint; very slow upward drift.
  Light leak `assets/textures/lightleak_03.jpg` (screen, 0.15) breathes once at ~2.5 s.
- **Motion → next** streaks keep running under SC002 (same canvas, seed continues): soft continuity, no cut.
- **SFX** 0.10 `air_swell` (very low, sets the room).
- **Music** pad only (held chord), no marimba yet.

### SC002 · 4.32–8.16 · B002 · NIGHT
- **FX** #4 film-title typography (+#13 random letters, #8 streaks behind) · **Copy** s01 / s10 title
- **Text** `SILICON VALLEY` — display + halate, 200 px, letters appear in random order (`FX.text.random`)
  @4.32 ("Silicon"), second word completes @5.12 ("Valley").
- **Visual** behind the title: modern dusk aerial of the Santa Clara Valley (A01), blurred 8 px, tinted to sepia-dark,
  0.35 opacity, slow push 1.00→1.06.
- **Motion → next** title rises out of frame (blur-in reversed) while the background panel slides right and becomes
  panel 1 of SC003's layered stack (match on the photo).
- **SFX** 4.30 `whoosh_soft` (title), 4.35–5.2 `letter_ticks` (random-letter pops, very quiet).
- **Music** marimba enters on the downbeat at 4.32.

### SC003 · 8.16–13.20 · B002 · NIGHT
- **FX** #10 Vox layered backgrounds (+#13 fill pop) · **Copy** s09
- **Text** `most powerful` serif-i @8.16 → swaps to `most successful` serif-i @10.48 (yellow fill pop that settles to bone,
  `FX.text.fill`). Kicker label `COMPANIES IN THE WORLD` @11.12 (small).
- **Visual** 3 tinted panels drifting at different speeds: Apple Park aerial (A02), NVIDIA HQ (A03), Googleplex/Meta
  sign (A04); `FX.tintDefs` blacks→#1a1917, whites→bone; newsprint overlay; offset/rotated with shadows.
- **Motion → next** camera drifts right; **hard cut** to paper on "Let" @13.20.
- **SFX** 8.14 `paper_slide` (panel 2), 9.6 `paper_slide` (panel 3), 10.46 `pop_soft` (fill pop).

### SC004 · 13.20–17.52 · B003 · PAPER
- **FX** #13 odometer text · **Copy** s01 (odometer helper)
- **Text** `STATS` display ink @14.80 (slot-machine letters), `NUMBERS` @15.92 below it. A thin ink rule draws under both.
- **Visual** clean paper ground with folds; faint grid of tiny ledger lines (multiply 0.15). A pencil-tick column of
  digits blurs past (odometer reels) behind the words, ink at 15 % — they lock on the final glyphs.
- **Motion → next** whole sheet slides up and out (12 fps choppy) revealing the night of SC005.
- **SFX** 14.78 `odometer_tick` burst (0.5 s), 15.90 `odometer_tick` burst, 17.45 `paper_slide`.

### SC005 · 17.52–21.76 · B004 · NIGHT
- **FX** #4 film title (+#8 streaks, #13 count) · **Copy** s01 (approved; re-time)
- **Text** `October 2026` label + halate @19.12 (random letters); `12` display yellow, 430 px, counts 0→12 @21.20
  (`FX.text.count`, 12 fps). `Companies · in the United States` right column @21.76 / @22.48 (rise) — these land
  inside SC006 if needed: keep them in SC005 only if the cut moves; otherwise leave for SC006.
- **Visual** s01 layout: streak canvas + warm radial glow + rule.
- **Motion → next** the yellow "12" scales down and flies to the top-left of SC006 where it becomes the chart kicker
  (cross-ground transition: a 6-frame white-paper wipe from the bottom).
- **SFX** 19.10 `tick_soft`, 21.18–21.8 `counter_ticks` (12 ticks), 21.74 `whoosh` (fly-out).

### SC006 · 21.76–32.88 · B004–B005 · PAPER
- **FX** #2 animated chart · **Ref** R4 ranked bars with circular portraits (+ R1's dashed threshold line) · **Copy** s03 (bars)
- **Text**
  - kicker `12 U.S. COMPANIES` label (inherits the yellow 12) — on screen at scene start.
  - `$1 TRILLION` `.label-box` on a dashed ink line across the chart @24.32 ("trillion").
  - `changes daily` serif-i small @27.28 ("changes").
  - `12` yellow on the kicker re-pops @29.60 ("12").
  - source line (label, 14 px): `Market value as of 29 Oct 2026 · companiesmarketcap.com` from 22.0.
- **Visual** 12 vertical bars (heights = market cap, §6 of BEATS), ranked left→right, bars rise one by one
  (choppy 12 fps, 0.08 s stagger) from 22.0; each topped by a circular badge (logo or HQ photo, see Q1):
  NVIDIA, Apple, Microsoft, Alphabet, Amazon, SpaceX, Broadcom, Meta, Tesla, Eli Lilly, Berkshire, Micron.
  Bars vermilion, **Eli Lilly bar navy** (East) — no label yet (the reveal belongs to SC007). Ghosted halftone
  skyline of a modern campus at the bottom (R4's ghosted building; A02 cutout, 12 % opacity).
  @27.28 bars "breathe" (±3 % height wobble, 12 fps) = market moving; @31.68 ("less") Micron's bar dips to touch
  the dashed line; @32.24 ("more") a dashed ghost 13th bar flickers in and out.
- **Motion → next** camera tilts down onto the bottom ink line which becomes the Mississippi river of SC007
  (match line; cut on "But" @32.88).
- **SFX** 22.0–23.0 `pop_soft` ×12 (bars, very quiet), 24.30 `marker_scratch` (dashed line + box), 27.3 `paper_rustle`,
  31.66 `tick_soft`, 32.22 `pop_soft`.

### SC007 · 32.88–41.52 · B006–B007 · NIGHT
- **FX** #3 map (burn reveal, river draw, pins, clouds) · **Copy** s02 (approved; already timed 32.9–42.9)
- **Text** `12` count @33.76; `11` @35.36; `WEST` label + `11 OF 12 COMPANIES` @36.88; `Mississippi River` @37.52
  (rotated along the river while it draws); `1` + `EAST` @40.56 (navy-lit label).
- **Visual** s02 as approved: desat Blue Marble, West region burns in vermilion (overlay), river stroke draws,
  HQ pins pop with ×N clusters, satellite clouds + shadows, foreground puffy cloud fly-through.
- **Motion → next** camera continues pushing to Indianapolis (4184, 1223) — no cut, SC008 takes over the same camera.
- **SFX** 33.74 `counter_ticks`, 35.36 `burn_crackle` (1.5 s), 36.0–36.8 `map_pin` ×9 (staggered), 37.5 `marker_scratch`
  (river draw, long soft), 38.9 `wind` (cloud fly-through), 40.56 `map_pin` (Lilly, slightly brighter).
- **Music** `stinger_reveal_Dmaj` (low) @35.36.

### SC008 · 41.52–46.48 · B007 · NIGHT
- **FX** #20 map callout (+#16 card photo, #19 circle) · **Ref** R12 (relief map, one state filled + halftone + glowing edge) · **Copy** s02 (Lilly card) + s11 (markup)
- **Text** `Eli Lilly` display, fill pop @41.52; `pharmaceuticals` serif-i @43.44; `Indianapolis, Indiana` label @45.04.
- **Visual** push into Indiana: grey hillshade relief (A43) cross-dissolves over the Blue Marble so Indiana reads
  **navy** with halftone dots + a thin bone glowing edge (R12 adapted: East = navy, no red). Rough hand-drawn circle
  (vermilion, `FX.markup.circle`) around the Indianapolis pin @45.04. Card: Eli Lilly HQ photo
  (`assets/maps/eli_lilly_hq_tower_2011.jpg`, CC BY 2.0 — credit line) with fringe blur + dust, yellow leader line.
- **Motion → next** camera pulls back fast (12 fps) and the map flattens to paper (cross-ground: paper wipes in from right).
- **SFX** 41.50 `pop_soft` (card), 45.02 `marker_scratch` (circle), 46.40 `whoosh`.

### SC009 · 46.48–51.20 · B008 · PAPER
- **FX** #2 chart · **Ref** R8 dot-matrix semicircle with highlighted headline · **Copy** s03 (isotype grid logic)
- **Text** serif headline: `The trillion-dollar club, by value` with `.hl` highlighter on *by value* swiping @49.76
  ("admit"); leader labels `West of the Mississippi` (vermilion) and `East` (navy) pop @50.24 / @50.56 (no extra numbers on screen).
  Small source line: `Market value, Oct 2026`.
- **Visual** semicircle of 305 dots (1 dot = $100 B), filling clockwise from 46.6 (12 fps); 293 vermilion, 12 navy (Lilly).
  A visual recap that sets up the "comparison" — dots fill while he talks (labels only).
- **Motion → next** dots scatter downward like confetti and settle into the paper; two halftone fruit cutouts drop in (SC010).
- **SFX** 46.6–48.6 `dot_ticks` (fine, rising), 49.74 `highlighter_swipe`, 50.22 / 50.54 `pop_soft`.

### SC010 · 51.20–54.48 · B008 · PAPER
- **FX** #12 collage (+#13 rise) · **Copy** s08
- **Text** `not a fair comparison` serif-i @51.44 ("fair"); `apples` label under left cutout @53.12; `oranges` label under
  right cutout @53.68.
- **Visual** two halftone cutouts on torn paper cards: an apple (tinted ink→paper, vermilion halftone) and an orange
  (navy halftone) (A41), pinned with 12 fps stop-motion wobble; a hand-drawn `≠` between them (`FX.markup`) @53.5.
- **Motion → next** camera rushes into the orange's halftone dots (expo zoom) — those dots become the city lights
  of SC011 (curve-cut feel into the next scene's push).
- **SFX** 51.4 `paper_slide`, 53.10 `pin_pop`, 53.66 `pin_pop`, 54.40 `whoosh`.

---

## 2. Act II — The flip, a century ago (54.48–110.17)
Music: at "completely flipped" (62.49–63.21) the marimba drops out; `historic_nostalgic_Gmaj_84bpm_3-4` enters @63.21
(sepia, nostalgic); `tension_braindrain_Bmin_92bpm` crossfades in from @93.53 (people leaving) through Act III's
"brain drain" (ends ~122.98).

### SC011 · 54.48–58.49 · B009 · NIGHT
- **FX** #15 cutting-the-curve match cut · **Copy** s07 (`FX.curveCut`)
- **Text** none (keep it visual; "how big of a feat" is carried by the cut).
- **Visual** A: modern Silicon Valley aerial (A01, colour, slightly graded) with expo.inOut push (12 fps) centred on the
  valley floor; B: a 1920s Santa Clara Valley orchard / "Valley of Heart's Delight" photo (A05, sepia) parented to
  the same zoom; cut at peak velocity ≈57.6 with a 2-frame blur. B settles with gate weave starting.
- **Motion → next** B's slow zoom continues as the paper of SC012 slides over it (12 fps).
- **SFX** 57.5 `whoosh_big` (peaks at the cut), 57.62 `projector_click` (enters old film), 57.7 `projector_loop` (fades out by 58.5).

### SC012 · 58.49–64.17 · B009 · PAPER
- **FX** #13 number count (+#4 ink title, #2 equation) · **Copy** s03 (opening + equation, approved)
- **Text** label `THE U.S. ECONOMY` @58.49; year `2026 → 1926` counts down @59.69 ("100"); serif-i `100 years ago` @60.25;
  equation `WEST > EAST` (vermilion / navy) @61.29 ("equation"); the `>` sign rotates 180° to `<` @62.49 and
  locks with a stamp @63.21 ("flipped").
- **Visual** s03 opening as approved: paper, folds, big ink year, equation row.
- **Motion → next** the equation's EAST word scales up and becomes the title of SC013.
- **SFX** 59.67–60.4 `counter_ticks`, 62.49 `paper_flip`, 63.19 `stamp_thud`.
- **Music** marimba out at 62.49; `historic_nostalgic` in at 63.21.

### SC013 · 64.17–69.77 · B010 · PAPER
- **FX** #2 chart · **Ref** R1 (vermilion bars with watercolour tops, dashed line, halftone building cutout, ink label box) · **Copy** s03 (bars + count) + `tools/halftone.py`
- **Text** `.label-box` `90%` (Haskoy, paper on ink box, R1's "4%" box) counting 0→90 @64.17 ("90%"); label `of US GDP` @65.53 ("GDP");
  `in the East` display navy @67.45 ("east"); `.hl` highlighter on *far East* serif-i @68.65 ("far").
- **Visual** R1 restyled to the narrated stat: two fat bars on paper — **East** (navy, rises to 90 % height with a watercolour
  top fade + grain) and **West** (vermilion, a stub at ~10 %); a dashed ink line at the 90 % mark carrying the label box;
  halftone NYC 1921 skyline cutout along the bottom (`assets/archival/cutouts/nyc_skyline_1921_halftone.png`) overlapping the East bar,
  exactly like R1's building. (The approved s03 isotype — 90 navy cells of 100 — can be used as a 1.5 s intro inside the scene if wanted.)
- **Motion → next** the bars collapse (12 fps) into the dashed line, which becomes the horizon of the SC014 photo.
- **SFX** 64.15–65.0 `counter_ticks`, 64.2 `pop_soft` ×2 (bars), 65.51 `marker_scratch` (label box), 68.63 `highlighter_swipe`.

### SC014 · 69.77–73.77 · B011 · NIGHT
- **FX** #16 hi-quality photo treatment (fringe blur, dust, vignette, slow zoom) · **Copy** s05 plate / s07
- **Text** `West` display vermilion halate @70.65; serif-i `basically nothing` @72.57.
- **Visual** an empty 1920s Western scene: Palo Alto/Santa Clara Valley dirt road with orchards (A06; fallback the
  A05 orchard plate), sepia duotone, fringe blur, dust, slow zoom 1.0→1.05, slight gate weave.
- **Motion → next** CRT power-on of SC015 replaces the frame (the photo collapses to a horizontal line = CRT off/on).
- **SFX** 70.63 `whoosh_soft`, 72.55 `wind` (very thin), 73.70 `crt_click`.

### SC015 · 73.77–84.49 · B012–B013 · NIGHT
- **FX** #11 vintage TV (TV #1: Philco Predicta, existing) (+#18 choke) · **Copy** s04 (approved; timed 73.7–83.9)
- **Text** `Stanford` @76.01; `or` serif-i; `UC Berkeley` @77.29; `1920s` label + yellow number @78.57;
  `opportunities in the West` @81.61; `scarce` display with Simple-Choker reveal @83.45.
- **Visual** s04 as approved: `assets/textures/tv_frame_01.png`, Berkeley 1932 commencement footage
  (`assets/archival/footage/berkeley_1932_grad_cut.mp4`) with CRT effects; tinted Stanford Inner Quad behind
  (`assets/archival/hoover/stanford_inner_quad_west_entrance_c1900.jpg`).
- **Motion → next** TV powers off (scaleY → 0.012, white line) and the line becomes the rail of a ticket in SC016.
- **SFX** 73.8 `crt_click` + `crt_hum` (bed, low, to 84.3), 76.0 / 77.27 `pop_soft`, 78.55 `tick_soft`,
  83.43 `marker_scratch` (choke), 84.35 `crt_off`.

### SC016 · 84.49–93.53 · B014 · PAPER
- **FX** #18 rough edges (choker reveal + roughen + 12 fps) (+#19 arrow) · **Copy** s04 (choke) / s06 (rough)
- **Text** `go East` display navy @86.57 ("east"); two ticket stubs appear, each roughen/choke-revealed:
  `POSTGRADUATE` @90.01, `A JOB` @93.05.
- **Visual** two 1920s railroad ticket stubs / Overland Limited timetable cards (A07, or own-made tickets in our fonts
  with halftone texture) on paper, torn rough edges (boiling 12 fps); a vermilion→navy hand-drawn arrow (`FX.markup.arrow`)
  pointing right (East) draws @86.57.
- **Motion → next** tickets slide right off frame; the arrow continues and becomes the West→East route of SC017's map.
- **SFX** 86.55 `marker_scratch`, 89.99 `paper_tear`, 93.03 `paper_tear`, 93.45 `whoosh`.
- **Music** `tension_braindrain` starts creeping in (−6 dB) @93.53.

### SC017 · 93.53–100.25 · B015 · PAPER
- **FX** #3 map (+#20 leader-line labels) · **Ref** R11 (muted map, beige land, coloured regions, leader-line labels) · **Copy** s02 (geometry) — paper restyle
- **Text** leader-line labels (label 26 px, ink): `California` @97.21 (vermilion fill); `New York` @98.25,
  `New Jersey` @98.73, `Massachusetts` @99.37 (navy fills, pop in sequence). Do **not** caption "Western United States"
  (slip at 94.01–96.09).
- **Visual** R11 restyle: muted grey-blue water, beige land (paper texture inside states, A44 built from
  `assets/maps/us_states.geojson` / `us_overlay.json`), thin ink state borders. California fills vermilion (overlay
  + watercolour edge), the three Eastern states navy. A dotted route line (12 fps dashes) runs CA → NY/NJ/MA.
  Camera drifts east following the line.
- **Motion → next** camera arrives at New York; a shutter closes (SC018's first iris) on the NY state fill.
- **SFX** 97.19 `map_pin`, 98.23 / 98.71 / 99.35 `pin_pop`, 97.4–100.0 `pencil_scribble` (route dashes), 100.10 `shutter`.

### SC018 · 100.25–110.17 · B016 · NIGHT
- **FX** #9 shutter transitions (+#14 gate weave, #16 plates) · **Copy** s05 (approved, timed 96.5–104.5)
- **Text** `Bell Labs` display halate @102.65 (first mention only); `General Electric` + GE logo
  (`assets/archival/brain_drain/ge_logo_bone.svg`) @103.69; serif-i `and many more` @107.45. No text on the repeat (104.81–106.33).
- **Visual** shutter chain: NYC skyline 1921 (`assets/archival/brain_drain/nyc_skyline_1921.jpg`) → iris @102.5 →
  Bell Labs West St (`assets/archival/companies/bell_labs_west_street_building_historic.jpg`) → iris @103.55 →
  GE Schenectady works 1920s (A08) → (hold through repeat, slow push) → iris @107.3 → Edison West Orange lab
  (`assets/archival/brain_drain/nj_edison_labs_west_orange.jpg`) → iris @109.9 opens on paper (SC019).
- **SFX** `shutter` 0.15 s before each iris: 102.35, 103.40, 107.15, 109.75; `projector_loop` bed 100.3–110.0 (very low).

---

## 3. Act III — The trustee who noticed: Hoover (110.17–287.56)
Music: `tension_braindrain_Bmin` continues to ~122.98, crossfades into `curious_neutral_Dmaj` (storytelling,
mid-tempo) for Hoover's origin; playful pluck on "fails" @143.94; `stinger_soft_rise_Dmaj` on "Hoover gets in"
@157.22; `historic_nostalgic` under the Founding Grant / money section (214.67–249.00); gentle build through the
GSB; settle/resolve on "a good start" @286.84.

### SC019 · 110.17–118.49 · B017 · PAPER
- **FX** #12 collage (+#19 arrow) · **Copy** s08
- **Text** tag `STANFORD` (ink tag, paper text) @113.85; serif-i `did not like what they were seeing` small @116.89 ("like").
- **Visual** paper collage: Stanford Inner Quad photochrom card (`assets/archival/hoover/stanford_inner_quad_west_entrance_c1900.jpg`,
  tinted ink→paper, halftone multiply, torn edges) pinned centre-left @112.25 ("West"); a small stack of student cutout
  cards (from A20) peel off the card and drift right while a vermilion rough arrow points East @116.0.
- **Motion → next** the drifting cards wipe the frame (12 fps) into SC020.
- **SFX** 112.23 `pin_pop`, 113.83 `paper_slide` (tag), 116.0 `marker_scratch`, 117.8 `paper_rustle`.

### SC020 · 118.49–122.98 · B018 · PAPER
- **FX** #18 rough-edge title (choker reveal) · **Copy** s04/s10 (choke) · motif: **BRAIN DRAIN** (recurs in SC032)
- **Text** `BRAIN` @119.85, `DRAIN` @120.33 — display ink, 220 px, Simple-Choker reveal, roughened (12 fps boil);
  serif-i `inside the country` @121.53 ("inside").
- **Visual** halftone US silhouette (from `assets/maps/us_states.geojson`, `tools/halftone.py`), small ink dots flow
  out of California and run East along a river-like path (12 fps), collecting as navy on the East coast.
- **Motion → next** hard cut on "And" @122.98 to the newspaper (night).
- **SFX** 119.83 `marker_scratch` (choke), 120.31 `marker_scratch`, 120.5–122.8 `dot_ticks` (dots trickling).

### SC021 · 122.98–131.46 · B019 · NIGHT
- **FX** #5 newspaper (NEWSPAPER #1: NYT 7 Nov 1928) (+#18 highlighter) · **Copy** s06 (approved, timed 122.9–131.3)
- **Text** `future president` serif-i @126.90 ("president"); `Herbert Hoover` display choke @128.58 (ASR "Harvard");
  no extra role line. No text on "one of those people, or one of these people".
- **Visual** s06 as approved: `assets/archival/newspapers/nyt_1928-11-07_hoover_wins_frontpage.jpg` on a tilted 3D page,
  sepia, halftone that grows with zoom; yellow rough highlighter on "HOOVER WINS" @126.90; portrait clip
  (`assets/archival/hoover/hoover_presidential_portrait_photo_NARA.jpg`) slides in @128.5.
- **Motion → next** camera pushes into the portrait's face; the portrait becomes SC022's photo (match).
- **SFX** 123.0 `paper_rustle` (page settles), 126.88 `highlighter_swipe`, 128.56 `paper_slide` (clip), 131.3 `whoosh_soft`.

### SC022 · 131.46–136.98 · B020 · NIGHT
- **FX** #16 hi-quality photo treatment (+#15 curve cut out) · **Copy** s07 (part A, approved)
- **Text** `Hoover` label @131.86; `the first class` display @134.18 ("first"); serif-i `that ever existed in Stanford` @135.62 ("existed").
- **Visual** young Hoover (`assets/archival/hoover/hoover_young_1898.jpg`), framed off-centre with blurred tinted copy behind,
  fringe blur, dust, vignette, slow zoom.
- **Motion → next** `FX.curveCut` — expo zoom into the photo, cut at peak velocity ≈136.7 into the Main Quad 2.5D world of SC023.
- **SFX** 131.84 `pop_soft`, 134.16 `tick_soft`, 136.5 `whoosh_big` (peaks at cut).

### SC023 · 136.98–141.70 · B021 · NIGHT — 2.5D #1 (the founding)
- **FX** #17 2.5D parallax · **Copy** s10 (stage, layer math) + s07 (pano)
- **Text** kicker `founded in` label @138.50 ("founded"); `1891` display yellow, title tucked **behind** the
  Memorial Arch layer, rises @139.30; serif-i `the first class` @141.06 ("first").
- **Visual** Main Quad c.1896 (`assets/archival/hoover/stanford_main_quad_panorama_c1896.jpg` / `_b.jpg`) cut into layers
  (A20 layer job): sky + far hills (blurred), Memorial Arch / church façade (mid), arcade columns (near), foreground
  palm/ground blur. Camera dolly: z −80→150, x drift +120, rotateY 3°, haze between layers, warm light rays from the top-right.
- **Motion → next** dolly continues as an ink X-mark flash cuts to paper (SC024) on "And" @141.70.
- **SFX** 137.0 `air_swell` (dolly), 139.28 `boom_low` (soft, 1891), 141.6 `whoosh`.

### SC024 · 141.70–146.74 · B022 · PAPER
- **FX** #19 Vox markup (cross / X) · **Copy** s11
- **Text** `entrance exams` serif title @144.90; `fails all` display vermilion @143.94 ("fails") with a big hand-drawn vermilion `✗` (cross markup) over the sheet; the X's second stroke lands @145.46 ("exams").
- **Visual** an 1890s exam sheet / blue-book page (A52: archival or own-made in our fonts with halftone, "STANFORD
  UNIVERSITY · ENTRANCE EXAMINATION · 1891"), lying slightly rotated on paper. Several subject lines on the sheet each get a quick vermilion tick-cross @144.5–145.4 (all failed).
- **Motion → next** the sheet is pulled down (12 fps) and the night collage of SC025 rises.
- **SFX** 143.92 `marker_scratch` (X, two strokes), 144.5–145.4 `pencil_scribble` (small crosses), 146.6 `paper_slide`.
- **Music** light comic pizz pluck on 143.94.

### SC025 · 146.74–154.58 · B023 · NIGHT
- **FX** #10 Vox layered backgrounds (+#16) · **Copy** s09
- **Text** `Quaker` display halate @147.78; serif-i `reviewing admissions` @152.58 ("admissions"); `a Quaker too` display halate @154.90 (lands in SC026's first frames — keep the card on screen across the cut).
- **Visual** layered tinted background: 19th-c. Friends meetinghouse engraving (A10), Stanford 1890s campus
  (`stanford_early_campus_main_entrance_c1900.jpg`), newsprint overlay; foreground cards: young Hoover (left),
  the admissions reviewer (Joseph Swain portrait, A09 — no name on screen, VO doesn't name him) slides in @151.3 ("guessing"). Both cards with rough paper borders.
- **Motion → next** Swain card stays; Hoover card flips over (12 fps) revealing the admission card of SC026.
- **SFX** 147.76 `pop_soft`, 151.3 `paper_slide`, 154.5 `paper_flip`.

### SC026 · 154.58–158.66 · B024 · PAPER
- **FX** #12 collage (+#13) · **Copy** s08
- **Text** serif-i `because of that` @155.94 ("because"); `HOOVER GETS IN` vermilion rubber stamp, rough (12 fps) thud @157.22 ("gets").
- **Visual** an own-made 1891 admission card in our fonts ("Leland Stanford Junior University — Herbert C. Hoover")
  with halftone + paper tex; tiny Quaker-hat ink doodles on both names (Hoover and the reviewer) @154.90 (playful: two Quakers).
- **Motion → next** the stamp impact shakes the frame (2 frames) — cut to night film on "For" @158.66.
- **SFX** 154.88 `pencil_scribble`, 155.92 `tick_soft`, 157.20 `stamp_thud`.
- **Music** `stinger_soft_rise_Dmaj` @157.22.

### SC027 · 158.66–166.34 · B025 · NIGHT
- **FX** #14 old-footage gate weave + flicker (+#1) · **Copy** s05/s07 weave
- **Text** serif-i `a life-changing moment` @160.98 ("life"); serif-i `very successful` @163.70 ("successful"); label `Stanford played a big role` @164.90 ("Stanford").
- **Visual** archival film of Hoover (1910s–20s newsreel, A11) full-frame with weave + flicker + scratches;
  fallback: Ken-Burns on `hoover_secretary_of_commerce_1924_with_hughes.jpg` with weave.
- **Motion → next** film burns out at a frame edge (lightleak_03 screen flash, 4 frames) into paper.
- **SFX** 158.7–166.3 `projector_loop` (low), 160.96 `tick_soft`, 166.25 `film_burn`.

### SC028 · 166.34–169.86 · B026 · PAPER
- **FX** #12 collage · **Copy** s08
- **Text** tag `his wife` @168.18 ("wife") with the small name label `Lou Henry` under her card; serif-i `at the university` @168.98 ("university").
- **Visual** two collage cards slide together: young Hoover (reuse) and Lou Henry (A12, c.1890s), tinted, halftone,
  torn edges; a small vermilion hand-drawn loop connects them @168.5.
- **Motion → next** cards slide up and become two dots on SC029's timeline (match on position).
- **SFX** 166.4 `paper_slide`, 168.16 `pin_pop`, 168.5 `pencil_scribble`.

### SC029 · 169.86–177.30 · B027 · PAPER
- **FX** #2 chart · **Ref** R7 (line chart with shaded era band, end labels, annotations — adapted as a decade timeline) · **Copy** s03 + s08 timeline
- **Text** serif title `before he becomes president` @170.42 ("before"); axis labels pop exactly as narrated:
  `the 20s` @173.46, `late 1910s` @174.74 (band shades 1916–1919), `early 1920s` @176.18 (band shades 1920–1923);
  vermilion end label `President of the United States` at the right end of the line @171.54 ("president").
- **Visual** R7 restyle: horizontal year axis 1910–1930, an ink line draws left→right (dashoffset, 12 fps) toward the vermilion end dot;
  paper-2 era bands fade in on each narrated period; thin ink annotation leader lines.
- **Motion → next** camera pushes into the early-1920s band; the band colour floods the screen into the TV glow of SC030.
- **SFX** 170.4–172.5 `pencil_scribble` (line draw), 171.52 `pop_soft`, 173.44 / 174.72 / 176.16 `tick_soft`, 177.2 `whoosh`.

### SC030 · 177.30–182.03 · B028 · NIGHT
- **FX** #11 vintage TV (TV #2: 1930s wooden radio-cabinet TV, e.g. RCA TRK-12, A48a) · **Copy** s04
- **Text** `part of the administration` serif-i @178.74 ("administration"); `Secretary of Commerce` display halate @179.86. Single card only (repeat at 182.03 not emphasised).
- **Visual** wood console set at 3/4 angle in a dim parlour (tinted background: Commerce building/Washington 1920s or
  `hoover_secretary_of_commerce_1928_informal.jpg` blurred); on screen: Hoover newsreel (A11) or the 1923 halftone
  portrait (`hoover_secretary_of_commerce_1923.jpg`) with scanlines, chromatic aberration, crtCurvature. CRT power-on.
- **Motion → next** CRT power-off line → paper slides in.
- **SFX** 177.30 `crt_click`, 177.4–181.9 `crt_hum`, 179.84 `pop_soft`, 181.95 `crt_off`.

### SC031 · 182.03–186.43 · B029 · PAPER
- **FX** #5 newspaper (NEWSPAPER #2: Stanford Daily / Daily Palo Alto clipping) (+#18 highlighter) · **Copy** s06 (paper restyle)
- **Text** `Stanford's` label @184.43; `Board of Trustees` display ink @185.31 ("board"; ASR "board of trustee").
- **Visual** a 1910s–20s Stanford Daily clipping mentioning Trustee Hoover (A13), cut out with rough edges, lying on paper,
  slight 3D tilt; yellow rough highlighter swipes the words "Board of Trustees" @185.31.
- **Motion → next** clipping slides down; the paper turns to night map (cross-ground fade 8 frames).
- **SFX** 182.1 `paper_slide`, 185.29 `highlighter_swipe`.

### SC032 · 186.43–191.39 · B030 · NIGHT
- **FX** #3 map (flow particles) · **Copy** s02 (camera/basemap) · motif: BRAIN DRAIN (callback of SC020)
- **Text** small rough `brain drain` label (same lettering as SC020) @188.51; `Western United States` label @190.27 over the West.
- **Visual** desat Blue Marble US, West region faintly vermilion (overlay), hundreds of bone dots stream from the West
  (Stanford/Berkeley/Palo Alto at `palo_alto` place) to the East coast (NYC/Boston) along curved paths (12 fps), turning navy.
- **Motion → next** camera pulls up; the dots resolve into the isotype grid of SC033 (match on dots).
- **SFX** 186.5 `wind` (low), 188.49 `marker_scratch`, 189–191 `dot_ticks`.

### SC033 · 191.39–199.07 · B031 · PAPER
- **FX** #2 chart · **Ref** R5 isotype pictogram grid (variant 1) · **Copy** s03 (grid) · motif: graduate icons (recurs SC078)
- **Text** `smart people` serif-i @191.63; column headers pop right: `Eastern companies` @196.27, `Eastern universities` @198.11 (navy labels).
- **Visual** a 10×6 grid of graduate pictograms (cap-and-gown, A39) on paper. Cells fill vermilion row by row @191.63;
  @194.91 ("leaving") rows start sliding right in 12 fps steps; each icon turns navy as it crosses a vertical dashed line
  (the Mississippi tick from SC006/SC007); they file into two navy columns under the headers.
- **Motion → next** grid empties; the last vermilion icon remains, zoom into it → cut to Hoover photo (SC034).
- **SFX** 191.6–193.0 `pop_soft` ×6 (rows), 194.9–198.5 `tick_soft` rhythm (12 fps steps, very quiet), 196.25 / 198.09 `pin_pop`.

### SC034 · 199.07–206.27 · B032 · NIGHT
- **FX** #16 hi-quality photo treatment (+#15 curve cut) · **Copy** s07
- **Text** `to fix this` serif-i @199.31 ("fix"); `changes` display halate @200.91; label `Stanford today` @204.19 after the cut.
- **Visual** A: Hoover 1928 informal portrait (`assets/archival/hoover/hoover_secretary_of_commerce_1928_informal.jpg`),
  fringe blur, dust, slow zoom; curve-cut (expo, 12 fps) at ≈204.0 into B: modern Stanford Main Quad / Hoover Tower
  aerial (A31), graded slightly warm but desaturated.
- **Motion → next** B keeps zooming as a paper chart card slides over from the right (SC035).
- **SFX** 200.89 `pop_soft`, 203.9 `whoosh_big` (cut), 206.2 `paper_slide`.

### SC035 · 206.27–214.67 · B033 · PAPER
- **FX** #2 chart · **Ref** R6 (horizontal bars, serif title with italic emphasis) · **Copy** s03
- **Text** serif title `A *revenue* generation model` (italic on *revenue*) @209.23 ("revenue"); two bar labels (label caps):
  `BEFORE` and `AFTER`; serif-i `charging for classes` @212.51 ("charging"); the AFTER bar's end label `classes` pops @214.03.
- **Visual** R6: two horizontal bars on paper — BEFORE is an empty outline (no charge), AFTER fills vermilion left→right
  (12 fps choppy) @212.51; thin ink axis without values (narration gives none). A small halftone ledger/coin cutout
  at the bar end.
- **Motion → next** chart paper folds away (12 fps) revealing the dark desk of SC036.
- **SFX** 209.21 `paper_slide` (title), 212.49 `pop_soft` + bar `tick_soft`s, 214.01 `pop_soft`, 214.6 `paper_flip`.

### SC036 · 214.67–225.63 · B034 · NIGHT
- **FX** #5 document (DOCUMENT #3: the Founding Grant, 1885) (+#19 circle) · **Copy** s06
- **Text** serif-i `against the rule` @216.43 ("against"); title `the trust document` display halate @220.19 ("trust");
  lower-third serif-i `its founder` @224.19 then `Leland Stanford` display @224.59.
- **Visual** Founding Grant scan (A14) on a tilted 3D page with sepia + halftone; camera push across its heading;
  vermilion rough circle around the date/heading @220.59; at 223.5 Leland Stanford's cabinet portrait
  (`assets/archival/hoover/leland_stanford_portrait_watkins_1874.jpg`) slides in as a clipped photo on top.
  Tinted, blurred copy of the page as background (s06 trick).
- **Motion → next** cut to paper on "I" @225.63.
- **SFX** 214.7 `paper_rustle`, 220.57 `marker_scratch`, 223.5 `paper_slide`, 224.57 `pop_soft`.
- **Music** `historic_nostalgic` (strings forward) under 214.67–249.00.

### SC037 · 225.63–229.79 · B035 · PAPER
- **FX** #19 markup (strike-through) · **Copy** s11
- **Text** `no charge` display ink @226.67 ("no"), `for students` serif-i @227.47; a vermilion rough strike-through
  scratches across "no charge" @228.43 ("cannot").
- **Visual** paper, a small engraved 1890s Stanford seal / campus vignette (halftone) in the corner.
- **Motion → next** shutter iris closes on the struck-out words (SC038).
- **SFX** 226.65 `pop_soft`, 228.41 `marker_scratch`, 229.65 `shutter`.

### SC038 · 229.79–237.32 · B035 · NIGHT
- **FX** #9 shutter transitions (+#16) · **Copy** s05
- **Text** `competitive` display halate @232.19 ("competitive"); serif-i `in the long term` @233.31.
- **Visual** iris chain of rival campuses c.1920s (A15): MIT new Cambridge campus (`assets/archival/collage/mit_main_group_from_boston.png`)
  → Harvard Yard (A26) → Caltech/Throop or Chicago (A15) → back to Stanford Main Quad (pano). Each plate with fringe blur, slow push.
- **SFX** `shutter` @229.65 (in), 231.05, 233.15, 235.4; 237.2 `whoosh`.

### SC039 · 237.32–244.28 · B036 · PAPER
- **FX** #18 rough edges (choke reveal) · **Copy** s04/s10 (choke)
- **Text** serif-i `even a` @240.52 ("Even"); `massive amount of money` display ink, choke reveal @241.08 ("massive"),
  `money` gets the yellow highlighter @241.88; serif-i `very hard to continue` @243.00 ("very"). No text on "Without taking account" (slip).
- **Visual** halftone cutouts of 1880s–90s engraved gold certificates/banknotes (A16) fanned on paper, slowly sliding
  apart (12 fps) as if money draining off the right edge @243.24.
- **Motion → next** the last banknote slides off to reveal a sepia film frame (SC040).
- **SFX** 241.06 `marker_scratch` (choke), 241.86 `highlighter_swipe`, 243.2–244.2 `paper_slide` ×3.

### SC040 · 244.28–249.00 · B037 · NIGHT
- **FX** #14 gate weave + flicker (+#16) · **Copy** s05/s07
- **Text** serif-i `issues` @245.08 ("issues"); label `late 1910s` yellow @248.12.
- **Visual** a 1910s Stanford campus photo (A17, e.g. the library/Quad c.1915) with weave, flicker, dust, dimming vignette
  closing slightly (mood: strain).
- **Motion → next** flicker to white (3 frames) into paper SC041.
- **SFX** 244.3–249.0 `projector_loop` (low), 248.10 `tick_soft`.

### SC041 · 249.00–256.20 · B038 · PAPER
- **FX** #12 collage + timeline · **Copy** s08 (timeline axis + travelling dot) · motif: Stanford timeline axis (recurs SC044, SC052)
- **Text** kicker `change no. 2` label @249.88 ("second"); card tag `Stanford Business Graduate Program` @253.88–254.92 ("Stanford"→"Graduate", words pop one by one);
  serif-i `right before he becomes president` @250.76 ("right") on the axis.
- **Visual** timeline axis along the bottom 1915–1930 with the travelling vermilion dot: stops at `1920 tuition` (small grey
  tag, callback), moves right (just before the vermilion "president" mark carried over from SC029) where a pinned card appears: early GSB building / first class photo (A18; fallback:
  Stanford 1920s Quad), tinted + halftone + torn edges.
- **Motion → next** camera slides along the axis to the right edge and turns to night map (SC042).
- **SFX** 249.86 `tick_soft`, 250.5–251.5 `dot_slide`, 254.50 `pin_pop`, 250.74 `tick_soft`, 256.1 `whoosh`.

### SC042 · 256.20–266.12 · B039 · NIGHT
- **FX** #3 map (arcs) · **Copy** s02 (camera, basemap)
- **Text** `MIT` label pin @262.20; `Harvard` label pin @263.32; serif-i `smart people` @260.84 near the Stanford pin.
- **Visual** desat Blue Marble (na_basemap or us_basemap), Stanford pin (Palo Alto 586,1456) glowing vermilion; at 260.84
  three bone dots leave Stanford along great-circle arcs (draw-on, 12 fps) towards Boston (5694, 964) — MIT pin @262.20,
  Harvard pin @263.32 (both navy). Clouds drift. Camera follows the arcs east.
- **Motion → next** camera whips back west (12 fps) to the Stanford pin (SC043 begins mid-whip).
- **SFX** 260.8 `whoosh_soft` (arcs), 262.18 / 263.30 `map_pin`, 265.8 `whoosh_big` (whip back).

### SC043 · 266.12–268.52 · B039 · NIGHT
- **FX** #20 map callout (+#13 fill pop) · **Copy** s11 (markup) + s02 (map)
- **Text** `HERE` display yellow halate @267.96 ("here"), fill pop; small label `Stanford, Calif.`.
- **Visual** arcs reverse — dots return to Stanford; a rough hand-drawn vermilion circle + arrow around the Stanford pin @267.4.
- **Motion → next** pin flash; paper slides in from below.
- **SFX** 267.40 `marker_scratch`, 267.94 `pop_soft`, 268.45 `paper_slide`.

### SC044 · 268.52–275.48 · B040 · PAPER
- **FX** #12 collage (then vs now) · **Copy** s08
- **Text** serif-i `a big deal` @271.08 ("deal"); tag `Stanford Business graduate program` @272.76–274.12 under the modern card.
- **Visual** the early card from SC041 (left, sepia, halftone) and a modern Stanford GSB / Knight Management Center
  photo card (A19, right, colour muted toward palette) pinned beside; timeline axis extends from the early card to `now` @275.00 ("now")
  (dashed) with the dot running to the end @272.76.
- **Motion → next** cards fade to the right; the dashed axis stretches into the night of SC045.
- **SFX** 268.6 `paper_slide`, 271.06 `pop_soft`, 272.7 `dot_slide`, 273.30 `pin_pop`.

### SC045 · 275.48–285.16 · B041 · NIGHT
- **FX** #14 gate weave + flicker (+#13 random letters) · **Copy** s07 (pano) + s05 weave
- **Text** `overnight` display halate @277.40 — then a vermilion rough strike @280.92 ("Stanford") turning it into
  "not overnight". No text on "churn turning".
- **Visual** Stanford Main Quad panorama (`stanford_main_quad_panorama_c1896_b.jpg`) panning very slowly; a light leak
  (`lightleak_01.jpg`) crosses the frame slowly like passing days; weave + flicker.
- **Motion → next** light leak blooms and the streaks of SC046 rise out of it.
- **SFX** 275.5–285.1 `projector_loop` (very low), 277.38 `tick_soft`, 280.90 `marker_scratch`.

### SC046 · 285.16–287.56 · B041 · NIGHT
- **FX** #4 film-title typography (+#8 streaks) · **Copy** s01
- **Text** `a good start` display halate, yellow on *good start* @286.84.
- **Visual** streak canvas warm, glow behind; short and clean (act button).
- **Motion → next** streaks dim; dolly into the 2.5D campus of SC047.
- **SFX** 286.82 `chime_soft`.
- **Music** Act III resolves on 286.84 (cadence), short breath before Act IV.

---

## 4. Act IV — Enter Terman (287.56–337.19)
Music: a fresh, lighter Terman motif — `curious_neutral_Dmaj` marimba stem only (pizz light), brighter register.

### SC047 · 287.56–296.23 · B042 · NIGHT — 2.5D #2 (a 1920s campus scene)
- **FX** #17 2.5D parallax · **Copy** s10
- **Text** serif-i `another student` @289.56 ("another"); title `FREDERICK TERMAN` display halate, tucked behind the
  student layer, rises @294.60 ("Frederick", ASR "Federick Turner"); small label `Stanford, 1910s–20s` @295.32.
- **Visual** 1920s Stanford students on the Quad / Palm Drive (A20) cut into layers: arcades backdrop (subject removed,
  blurred), mid students group, foreground column/palm blur; haze; camera dolly z −60→140 with a slow pan. At 295.3 a
  small portrait card of young Terman (A21) pops beside the title (fallback `assets/archival/collage/terman_frederick_1955.jpg`, small).
- **Motion → next** dolly ends with a cut on "He" @296.23 to paper.
- **SFX** 287.6 `air_swell`, 294.58 `boom_low` (soft), 295.30 `pop_soft`.

### SC048 · 296.23–304.23 · B043 · PAPER
- **FX** #13 number animation · **Copy** s01/s03 (count)
- **Text** `born` label + `1900` display ink, count @297.03 (VO "the 1900s" = the year 1900, "a very lucky year"); serif-i `a lucky year` @298.55; `2000` appears on the
  right in navy @300.87 (VO "the 2000s") with `=` hand-drawn between; at 302.07 ("calculate") a small counter `age = year − 1900` ticks
  1900→1924 above (ties to SC052).
- **Visual** paper, big ink numerals, rough-edge underline; tiny halftone baby-photo frame? no — keep typographic.
- **Motion → next** numbers slide off left; night layered collage rises.
- **SFX** 297.01 `counter_ticks`, 300.85 `pop_soft`, 302.05–303.0 `odometer_tick`, 304.1 `paper_slide`.

### SC049 · 304.23–308.87 · B044 · NIGHT
- **FX** #10 Vox layered backgrounds (+#13 fill) · **Copy** s09
- **Text** `accomplished` display, yellow fill pop → bone @307.83 (no text on "successful").
- **Visual** layered tinted panels: Stanford c.1910s campus, the 1916 book title page (`assets/archival/terman/terman_1916_title_page_HIRES_color.jpg`)
  at a tilt, a 1910s Palo Alto street; drifting at separate speeds; newsprint overlay.
- **Motion → next** the book panel slides to centre and becomes SC050's page (match).
- **SFX** 304.3 `paper_slide`, 307.81 `pop_soft`.

### SC050 · 308.87–314.55 · B045 · PAPER
- **FX** #5 document (DOCUMENT #4: "The Measurement of Intelligence", 1916) (+#18 highlighter) · **Copy** s06 (paper restyle)
- **Text** lower-third `Lewis Terman` display ink @309.59 (ASR "Louis"); serif-i `Stanford psychologist` @311.75;
  `invented the IQ test` display ink @312.71 ("invented"), `IQ` in yellow @313.35.
- **Visual** the book on a paper desk, 3D tilt: title page (`terman_1916_title_page_HIRES_color.jpg`), page turn @312.6 to the
  IQ distribution chart (`terman_1916_IQ_distribution_chart_HIRES_color.jpg`); highlighter swipe on "Measurement of
  Intelligence" @311.2. Small circular halftone portrait of Lewis Terman (`lewis_terman_1923_LOWRES.jpg` → halftone to hide
  the low res, ≤ 240 px on screen; better copy A22 if found).
- **Motion → next** camera pushes into the bell curve; it becomes the scan-line glow of the TV in SC051.
- **SFX** 309.0 `paper_rustle`, 309.57 `pop_soft`, 311.2 `highlighter_swipe`, 312.6 `page_turn`.

### SC051 · 314.55–321.27 · B046 · NIGHT
- **FX** #11 vintage TV (TV #3: 1950s portable, A48b) · **Copy** s04
- **Text** none on "I have taken it"; `Frederick Terman's dad` serif-i halate @317.91 ("Frederick") → `invented it` display @319.59 ("invented").
- **Visual** portable TV on a table, slight low angle; on screen: classroom intelligence-test footage (A23, Prelinger PD)
  with scanlines, RGB split, CRT curvature; dim room, lamp glow.
- **Motion → next** CRT off → paper collage (SC052).
- **SFX** 314.6 `crt_click`, 314.7–321.0 `crt_hum`, 317.89 `pop_soft`, 321.2 `crt_off`.

### SC052 · 321.27–330.63 · B047–B048 · PAPER
- **FX** #12 collage + timeline · **Copy** s08 (approved — re-time)
- **Text** tag `Stanford` @324.55 (no text on "goes to, goes to"); `undergrad` serif-i @325.27; `24` display vermilion @327.43 (age, "24 years old");
  `1924` display @329.51 ("1924") lands on the timeline tick where the dot stops (finishes undergrad).
- **Visual** s08: Terman card (A21 young / fallback `terman_frederick_1955.jpg`) + Stanford card (Main Quad) on paper; timeline axis
  (same axis styling as SC041/SC044) 1918–1926 with travelling dot.
- **Motion → next** the Stanford card swaps (12 fps) to a railroad map card that fills the frame (SC053).
- **SFX** 321.3 `paper_slide`, 324.53 `pin_pop`, 325.25 `tick_soft`, 327.41 `pop_soft`, 329.49 `pin_pop`.

### SC053 · 330.63–337.19 · B049 · PAPER (light archival map)
- **FX** #3 map (+#20 marker route) · **Ref** R10 (old map, yellow marker line, circle, numbered pin) — variant A: 1920s US railroad map · **Copy** s11 (markup) on a map plate
- **Text** `goes East` serif-i @331.83 ("east"); `doctorate degree` label @332.87 ("doctorate"); `engineering` serif-i @334.39;
  `MIT` display ink in the marker circle @336.31; number pin `1`.
- **Visual** 1920s Rand McNally railroad map (A24), desaturated toward paper, halftone; a fat yellow marker line (multiply,
  rough edge, 12 fps draw) from Palo Alto → across the continent → Boston, camera tracking it with slight 3D tilt (like R10);
  yellow circle + vermilion numbered pin at Cambridge @336.31. 
- **Motion → next** camera pushes into the pin; the map dissolves into the 1925 MIT aerial (SC054).
- **SFX** 331.8–335.5 `marker_long` (yellow line), 336.29 `pin_pop`.

---

## 5. Act V — The Eastern blueprint (337.19–479.31)
Music: build energy from "already had a Silicon Valley" (343–347): `momentum_building_Dmaj_108bpm` enters @346.07,
full by 355; drop to pad at "mind palace" @474.95.

### SC054 · 337.19–342.95 · B050 · NIGHT
- **FX** #16 hi-quality photo treatment · **Copy** s07 plate
- **Text** serif-i `something very interesting` @340.39 (small, lower third).
- **Visual** MIT campus aerial 1925 (`assets/archival/terman/mit_campus_aerial_1925_great_dome.jpg`), fringe blur, dust,
  vignette, slow zoom toward the Great Dome; slight cool tint (East = navy family).
- **Motion → next** zoom into the dome; streaks rise over the dark sky (SC055).
- **SFX** 337.2 `air_swell` (low), 341.5 `whoosh_soft`.

### SC055 · 342.95–348.31 · B051 · NIGHT
- **FX** #4 film-title typography (+#8 streaks, #18 choke-out) · **Copy** s01 · motif: SILICON VALLEY title (callback of SC002)
- **Text** label `the United States already had a` @344.31 (small); `SILICON VALLEY` (identical lettering to SC002) @346.07;
  @347.35 ("not") the title roughens and chokes away to leave a ghost outline with `?` serif-i.
- **Visual** streaks cooler (navy tint), MIT dome photo faint behind at 0.15.
- **Motion → next** ghost outline shrinks into a dot that becomes the numbered pin on the Boston map (SC056).
- **SFX** 346.05 `boom_low` (soft), 347.33 `marker_scratch` (choke), 348.2 `whoosh`.
- **Music** `momentum_building` enters @346.07.

### SC056 · 348.31–355.59 · B052 · PAPER (light archival map)
- **FX** #20 map callout (+#3) · **Ref** R10 — variant B: 1920s Boston/Cambridge street map · **Copy** s11
- **Text** `the ingredients` serif-i @348.71; `Boston` display ink, big, @355.03; small pins `MIT`, `Harvard` (pre-lit for SC057).
- **Visual** Bromley/Sanborn-style 1920s street atlas of Boston–Cambridge (A25), tilted 3D, camera sliding across;
  yellow marker loop circling Cambridge (MIT on the Charles, Harvard Square) drawn @352.6; numbered pins 1 (MIT) and 2 (Harvard).
- **Motion → next** shutter iris closes on pin 1 (SC057).
- **SFX** 352.6–354.4 `marker_long`, 355.01 `pop_soft`, 355.45 `shutter`.

### SC057 · 355.59–359.98 · B053 · NIGHT
- **FX** #9 shutter transitions (+#16) · **Copy** s05
- **Text** `MIT` display halate @358.46; `Harvard` display halate @359.34. (No text on "very successful universities".)
- **Visual** iris chain: MIT main group from Boston (`assets/archival/collage/mit_main_group_from_boston.png`) → iris @359.2 →
  Harvard Yard 1920s (A26). Plates with fringe blur.
- **SFX** `shutter` 355.45, 359.05.

### SC058 · 359.98–366.22 · B054 · PAPER
- **FX** #2 animated diagram (triangle) · **Copy** s03 (paper chart) + s11 (rough strokes)
- **Text** three node labels pop in sequence: `universities` @361.34, `professors` @362.14, `companies` @363.10 (label caps, ink);
  serif-i `leading tech companies` @364.46.
- **Visual** paper; a triangle diagram with three halftone circular icons (Great Dome, a professor portrait — Bush crop,
  a 1920s factory) at its corners; rough ink edges drawn on (12 fps) between them as each node appears.
- **Motion → next** camera pushes into the triangle centre; tiny people dots start circling (handover to SC059 night footage via iris-free crossfade 6 frames).
- **SFX** 361.32 / 362.12 / 363.08 `pin_pop`, 361.4–364.0 `pencil_scribble`.

### SC059 · 366.22–371.82 · B055 · NIGHT
- **FX** #14 old-footage gate weave (+ particle overlay) · **Copy** s05 weave
- **Text** `free flow of people` serif-i halate @367.74 ("free").
- **Visual** archival film of 1920s–30s engineers/students walking a campus or entering a lab (A27), weave + flicker;
  overlaid faint bone dots looping in a triangle path (callback of SC058) at 0.4 opacity.
- **Motion → next** film flickers out; paper collage of logos (SC060).
- **SFX** 366.3–371.7 `projector_loop` (low), 367.72 `whoosh_soft`.

### SC060 · 371.82–378.62 · B056 · PAPER
- **FX** #12 collage (logos + arrows) · **Copy** s08
- **Text** logos/wordmarks stamp in once each: `General Electric` @373.74, `AT&T` @374.94 (ASR "ATT"), `Bell Labs` @375.66;
  serif-i `visit campus` @377.58.
- **Visual** paper collage: a central MIT card (Great Dome halftone); three 1920s logo/wordmark cards (A28 — GE monogram
  exists, AT&T bell, Bell Labs) slide in from the edges at 12 fps; ink arrows draw from each into MIT @377.58.
- **Motion → next** the MIT card tilts and becomes one panel of SC061's layered background.
- **SFX** 373.72 / 374.92 / 375.64 `stamp_thud` (light), 377.56 `marker_scratch` ×3.

### SC061 · 378.62–388.70 · B057 · NIGHT
- **FX** #10 Vox layered backgrounds (+#13 odometer) · **Copy** s09
- **Text** `fund labs` display halate @378.94; `professors invent` serif-i @381.98 ("professors"); `commercialize` display,
  odometer letters @385.34.
- **Visual** layered tinted panels: Bush's differential analyzer (`assets/archival/terman/bush_differential_analyzer_integrator_mit_museum.jpg`),
  a 1920s MIT lab (A27), a 1920s radio/vacuum-tube product ad (A49); foreground cutout: vacuum tube (A49, halftone) that
  rotates slightly. At 385.34 the tube cutout gets a price-tag card (rough) = commercialized.
- **Motion → next** panels slide left; a bulletin page slides up (paper).
- **SFX** 378.92 `pop_soft`, 381.96 `paper_slide`, 385.32 `odometer_tick`, 387.9 `paper_slide`.

### SC062 · 388.70–398.46 · B058 · PAPER
- **FX** #5 document (DOCUMENT #5: MIT Bulletin page on Course VI-A, the co-op programme with GE, 1917–) (+#18 highlighter) · **Copy** s06 (paper restyle)
- **Text** serif-i `students` @389.74; `real-life experience` display ink @393.50 ("real"); label `part of the curriculum` @397.66.
- **Visual** MIT Bulletin / catalogue page describing the cooperative course with General Electric (A29) on paper, 3D tilt,
  halftone; yellow highlighter on "Co-operative Course" @393.5. Small cut-in photo: students in a GE plant (A30).
- **Motion → next** camera pushes into the cut-in photo → curve cut (SC063).
- **SFX** 388.8 `paper_rustle`, 393.48 `highlighter_swipe`, 397.64 `pop_soft`.

### SC063 · 398.46–405.90 · B059 · NIGHT
- **FX** #15 cutting-the-curve (twice: there and back) · **Copy** s07
- **Text** `hired` display halate @399.26; serif-i `back and forth` @405.10 ("back").
- **Visual** A: student at a lab bench (A27/A30) → expo zoom → cut at peak ≈399.2 to B: GE Schenectady factory interior 1920s
  (A30) → second curve cut back toward a campus photo at ≈404.9 ("back and forth" = there and back).
- **Motion → next** last zoom settles; paper with two printed photos slides in.
- **SFX** 399.0 `whoosh_big`, 404.7 `whoosh_big`, 405.8 `paper_slide`.

### SC064 · 405.90–410.94 · B060 · PAPER
- **FX** #19 Vox markup (arrow + circle) · **Copy** s11
- **Text** `Stanford` label @407.26; `today` serif-i small; `the connection` serif-i @409.82 ("connection").
- **Visual** two printed photos on paper: MIT 1920s (left, sepia) and modern Stanford (A31, right, muted colour);
  a hand-drawn vermilion double arrow draws between them @409.82; circle around the Stanford photo @407.26.
- **Motion → next** camera slides onto the MIT photo, which becomes SC065's plate.
- **SFX** 407.24 `marker_scratch`, 409.80 `marker_scratch`.

### SC065 · 410.94–416.86 · B061 · NIGHT
- **FX** #16 hi-quality photo treatment · **Copy** s07
- **Text** lower third `Frederick Terman` display halate @411.26; serif-i `graduate student, MIT` @413.74 ("graduate").
- **Visual** young Terman portrait (A21; fallback `terman_frederick_1955.jpg`) over a blurred tinted MIT 1925 aerial, fringe blur,
  dust, slow zoom.
- **Motion → next** the portrait is pinned onto cork (SC066) — the plate shrinks and a pin hits it.
- **SFX** 411.24 `pop_soft`, 416.7 `cork_pin`.

### SC066 · 416.86–423.31 · B062 · PAPER (cork) · motif: CORK BOARD (recurs SC074)
- **FX** #12 collage on cork (+#19 string draw-on) · **Ref** R9 (cork board, pinned photos, red string) · **Copy** s08 (cards) + s11 (stroke draw-on)
- **Text** tag `advisor` @418.14; tag `Vannevar Bush` @421.26 (ASR "Vanuar").
- **Visual** cork texture (A47) full frame; Terman card pinned left (from SC065); Bush card (`assets/archival/terman/vannevar_bush_1938.jpg`,
  tinted, halftone) pinned right @421.26 with 12 fps stop-motion; red string (vermilion, slight sag) draws from Terman's pin to
  Bush's pin @421.5. Board layout must be identical when SC074 returns.
- **Motion → next** camera tilts down off the board into darkness → TV in SC067.
- **SFX** 418.12 `cork_pin`, 421.24 `cork_pin`, 421.5 `string_pull` (soft).

### SC067 · 423.31–427.39 · B063 · NIGHT
- **FX** #11 vintage TV (TV #4: late-1940s console with doors, A48c) · **Copy** s04
- **Text** none (narrator's aside).
- **Visual** console TV in a dark room, newsreel of Vannevar Bush (1940s OSRD/newsreel, A32) with scanlines, RGB split; slow push to the screen.
- **Motion → next** push through the screen glass; scanlines fade into the 1932 MIT photo (SC068).
- **SFX** 423.32 `crt_click`, 423.4–427.2 `crt_hum`.

### SC068 · 427.39–437.23 · B064 · NIGHT
- **FX** #19 Vox markups · **Copy** s11 (approved; timed 427.3–435.2)
- **Text** `MIT` boxed label @428.51; serif-i `one of the founders of` @430.67; `Raytheon` display halate @432.03; serif-i `defense electronics` @433.23;
  label `still exists today` @435.63 ("exists").
- **Visual** s11 as approved: Bush & Compton MIT 1932 photo, rough circle + arrow markups that track the camera.
- **Motion → next** cut to paper on "And" @437.23.
- **SFX** 428.49 `marker_scratch`, 431.9 `marker_scratch`, 432.01 `pop_soft`, 435.61 `tick_soft`.

### SC069 · 437.23–443.63 · B065 · PAPER
- **FX** #18 rough edges (choke reveal, stamp) · **Copy** s04/s10 choke
- **Text** serif-i `at other universities` @439.71; `TABOO` display ink, rough stamp, choke reveal @441.87.
- **Visual** paper with two halftone icons: a gothic university tower (A33) and a 1920s factory (A30 crop) separated by a hand-drawn
  barrier/gap; the TABOO stamp lands across the gap.
- **Motion → next** stamp slides left with the tower card into SC070's layered night.
- **SFX** 441.85 `stamp_thud`, 443.5 `paper_slide`.

### SC070 · 443.63–449.07 · B065 · NIGHT
- **FX** #10 Vox layered (+#19 cross) · **Copy** s09 + s11
- **Text** `commercializing their research` serif-i halate @445.79; vermilion rough cross-out on it @447.95 ("research").
- **Visual** tinted layered backgrounds of gothic "ivory tower" campus architecture (A33) with a closed iron gate cutout in front.
- **Motion → next** gate swings open (12 fps) — reveal Boston on paper (SC071).
- **SFX** 445.77 `pop_soft`, 447.93 `marker_scratch`, 448.9 `gate_creak` (very soft).

### SC071 · 449.07–454.83 · B066 · PAPER
- **FX** #13 odometer text · **Copy** s01/s04 odometer
- **Text** `In Boston` label @449.39; the word `TABOO` (same stamp style) rolls odometer-style into `OPPOSITE` @450.51
  ("complete"); serif-i `professors consult for companies` @453.15 ("consultants").
- **Visual** paper with the Boston Custom House 1920 photo (`assets/archival/companies/massachusetts_boston_custom_house_1920.jpg`)
  as a tinted halftone strip along the right edge.
- **Motion → next** strip slides off; film frame of SC072.
- **SFX** 449.37 `pop_soft`, 450.49 `odometer_tick`, 453.13 `pop_soft`.

### SC072 · 454.83–460.99 · B067 · NIGHT
- **FX** #14 gate weave (+#16) · **Copy** s05
- **Text** serif-i `come teach our students` @457.95 ("teach"); `fund our research labs` display halate @459.47 ("fund").
- **Visual** 1920s–30s lab footage or stills (A27, e.g. MIT/GE research lab, students around a bench) with weave/flicker/scratches.
- **Motion → next** flicker; the layered night of SC073 slides in.
- **SFX** 454.9–460.9 `projector_loop` (low), 459.45 `tick_soft`.

### SC073 · 460.99–470.95 · B068 · NIGHT
- **FX** #10 Vox layered (+#13 fill) · **Copy** s09
- **Text** `professors` label @462.11; `start companies` display halate @463.55 ("starting"); small card `Raytheon — Vannevar Bush`
  @464.27 ("companies"); serif-i `very big` with yellow fill pop @468.43 ("big").
- **Visual** layered: 1920s Raytheon BH rectifier tube photo/ad (A34), MIT building, Bush portrait cutout (from `vannevar_bush_1938.jpg`);
  at 465.63 ("become") the Raytheon card scales up step-wise (12 fps) as if growing.
- **Motion → next** the cards fly to the cork board (SC074) — each card lands with a pin.
- **SFX** 462.09 `pop_soft`, 463.53 `paper_slide`, 465.6–466.9 `tick_soft` ×3 (growth steps), 468.41 `pop_soft`, 470.8 `whoosh`.

### SC074 · 470.95–479.31 · B069 · PAPER (cork) — R9 callback
- **FX** #12 collage on cork (+#19 strings) · **Ref** R9 (full board) · **Copy** s08 + s11
- **Text** `mind palace` serif-i halate-ink @474.95 ("mind"); no text on "maybe it comes back useful".
- **Visual** the SC066 board pulls back wide: Terman, Bush, MIT dome, Harvard, GE, AT&T, Bell Labs, Raytheon, the TABOO→OPPOSITE note,
  the VI-A bulletin clip; red strings draw from Terman to every card (12 fps, staggered) 471.4–474.5; @474.95 a warm desk-lamp pool
  narrows (vignette closes) and the board slowly recedes = filed away; @478.19 ("maybe") lamp dims further.
- **Motion → next** lamp goes out (fade to night 10 frames) → relief map glow (SC075).
- **SFX** 470.9–472.0 `cork_pin` ×5 (landing cards), 471.4–474.5 `string_pull` ×6 (soft), 476.0 `lamp_click`, 479.2 `lamp_click`.
- **Music** pull back to pad at 474.95 (momentum drops), reflective.

---

## 6. Act VI — Back West: heartbreak and the plan (479.31–600.00)
Music: minor-key dip (`tension_braindrain_Bmin`, pad + sparse marimba) 491.48–504.92; **turn** on "1938" @505.96 with
`stinger_reveal_Dmaj` → `momentum_building_Dmaj_108bpm` builds through the plan; cliffhanger: VO cuts mid-sentence at
599.67 — ride the music out, do not resolve (fade over 598.87–600.00 and beyond if the edit continues).

### SC075 · 479.31–486.92 · B070 · NIGHT
- **FX** #3 map (+#20 glow, route) · **Ref** R12 — variant 2: California vermilion on grey relief, halftone, glowing edge · **Copy** s02
- **Text** serif-i `after MIT` @480.75; `Stanford` label pin @485.24; `West` display vermilion halate @486.52.
- **Visual** grey hillshade relief of the US (A43), a navy dotted line from Boston runs west (reverse of SC053's route) @481.6–485.2;
  California fills vermilion with halftone dots and a warm glowing edge (R12) @485.24; Palo Alto pin.
- **Motion → next** push into the Palo Alto pin → paper.
- **SFX** 481.6–485.0 `marker_long` (route), 485.22 `map_pin`, 486.50 `burn_crackle` (light, the fill).

### SC076 · 486.92–491.48 · B071 · PAPER
- **FX** #13 random-letter text · **Copy** s10 (`FX.text.random`)
- **Text** label `teaching career` @487.96 ("teaching"); `RADIO ENGINEERING` display ink, random letters @489.72 ("radio").
- **Visual** paper with a halftone 1920s vacuum tube / radio-set cutout (A49) and faint 1920s radio circuit diagram lines (multiply 0.2).
- **Motion → next** the words fade to grey; film frame of graduation (SC077).
- **SFX** 487.94 `tick_soft`, 489.7–490.4 `letter_ticks`.

### SC077 · 491.48–496.92 · B072 · NIGHT
- **FX** #14 gate weave + flicker (+#16, slowed footage) · **Copy** s05
- **Text** none (let the music carry "breaking his heart"); optional serif-i `every year` @493.64 small.
- **Visual** Stanford commencement 1920s–30s footage/still (A38; fallback a different section of `berkeley_1932_grad_cut.mp4`
  — but **not** framed in the TV, and not labelled "Stanford" if it is the Berkeley clip), slowed to ~70 %, weave + flicker, desaturated, vignette heavier.
- **Motion → next** a graduate silhouette freezes and becomes one pictogram of SC078 (match).
- **SFX** 491.5–496.8 `projector_loop` (low, slowing), 495.96 `air_swell` (soft).
- **Music** minor dip begins 491.48.

### SC078 · 496.92–504.92 · B073 · PAPER
- **FX** #2 chart · **Ref** R5 isotype — variant 2 (same graduate icons as SC033) · **Copy** s03 grid
- **Text** `his smartest students` serif-i @497.32 ("smartest"); `→ East` display navy @503.64 ("east"). The narrator self-corrects at 501.48 → 503.64; show only where he lands (East).
- **Visual** a row of 12 graduate icons in ink; the best (4 icons) turn vermilion @497.32, then walk off frame to the right (12 fps steps),
  turning navy, along a dashed arrow labelled East; remaining icons stay grey. Paper background with a faint Stanford seal watermark.
- **Motion → next** empty frame; a slow push into darkness → streaks.
- **SFX** 497.30 `pop_soft` ×4, 499.5–503.6 `tick_soft` steps, 503.62 `pin_pop`.

### SC079 · 504.92–513.08 · B074 · NIGHT
- **FX** #8 light streaks (+#4 halate, #13 count) · **Copy** s01
- **Text** `1938` display yellow halate, counts 1925→1938 @505.96; serif-i `he decides to change this` @507.64 ("decides");
  `two favorite students` label @511.08 ("two").
- **Visual** streak canvas (warmer, faster evolution than SC001 — momentum), glow; two small bone silhouettes rise at the bottom @511.08.
- **Motion → next** silhouettes become the two cards of SC080 (match).
- **SFX** 505.94 `boom_low` + `counter_ticks`, 507.62 `whoosh_soft`, 511.06 `pop_soft` ×2.
- **Music** **turn** @505.96: `stinger_reveal_Dmaj` → `momentum_building_Dmaj_108bpm`.

### SC080 · 513.08–519.24 · B075 · NIGHT
- **FX** #10 Vox layered + cutouts · **Copy** s09 (approved; timed 513.0–519.2)
- **Text** `Bill` / `Hewlett` @515.72; `David` / `Packard` @516.84 / @517.24 (s09 layout).
- **Visual** s09 as approved: Stanford pano backgrounds tinted, two cards with silhouettes that reveal Hewlett
  (`assets/archival/hp/hewlett_william_c1962.jpg` / cutout) and Packard (`assets/archival/hp/packard_david_1933.jpg` / cutout).
- **Motion → next** Packard card slides to paper (SC081).
- **SFX** 515.70 `pop_soft`, 517.22 `pop_soft`, 519.1 `paper_slide`.

### SC081 · 519.24–527.32 · B076 · PAPER
- **FX** #19 Vox markup (arrow + circle) · **Copy** s11
- **Text** serif-i `stay in California` @523.40 ("stay"); `already gone` display ink @526.92 ("gone").
- **Visual** paper; a small muted outline of California (from us_states) with a vermilion circle drawn around Palo Alto @524.12;
  Packard's card (1933, halftone) sits inside the circle then slides out East along a hand-drawn navy arrow @525.96 ("Packard"),
  leaving an empty pin hole.
- **Motion → next** the arrow continues off-frame → cut to Schenectady (SC082).
- **SFX** 524.10 `marker_scratch`, 525.94 `paper_slide` + `marker_scratch`, 526.90 `pop_soft`.

### SC082 · 527.32–531.00 · B077 · NIGHT
- **FX** #13 number count (+#16 plate) · **Copy** s01 count + s07 plate
- **Text** label `General Electric` @528.12; serif-i `around` + `$100` display yellow, count 0→100 @529.88; serif-i `a month` @530.60.
- **Visual** GE Schenectady works aerial 1930s (A40), sepia, fringe blur, slow push; GE monogram (`ge_logo_bone.svg`) small top-left.
- **Motion → next** quick slide to paper (SC083).
- **SFX** 528.10 `pop_soft`, 529.86 `counter_ticks`, 530.9 `paper_slide`.

### SC083 · 531.00–536.92 · B078 · PAPER
- **FX** #12 collage (fork in the road) (+#19 arrows) · **Copy** s08
- **Text** card tag `Bill Hewlett` @531.40; fork label `more study?` @536.04 ("studies").
- **Visual** Hewlett card (cutout `assets/archival/cutouts/hewlett_william_c1962.png`, halftone) at the left; a hand-drawn fork
  (two vermilion/navy arrows) grows to the right: upper branch → a university card (Harvard/MIT halftone), lower branch blank until SC084.
- **Motion → next** camera follows the lower branch → shutter (SC084).
- **SFX** 531.38 `pin_pop`, 533.5 `pencil_scribble`, 536.02 `pop_soft`, 536.8 `shutter`.

### SC084 · 536.92–542.47 · B078 · NIGHT
- **FX** #9 shutter transitions (callback of SC018) · **Copy** s05
- **Text** `a job` serif-i halate @537.40 ("job"); no text on the repeat (539.48–541.56).
- **Visual** same Eastern company plates as SC018 (Bell Labs West St, GE Schenectady, + RCA/Westinghouse 1930s (A08b)), iris chain,
  slightly faster.
- **SFX** `shutter` 536.80, 538.6, 540.3, 542.2.

### SC085 · 542.47–549.03 · B079 · PAPER (light archival map)
- **FX** #20 map callout (+#3) · **Ref** R10 — variant C: old Palo Alto topographic/street map · **Copy** s11
- **Text** kicker `THE PLAN` label @544.39 ("plan"); `a company` serif-i @548.15 ("company"); `California` small label @549.03.
- **Visual** USGS historical topo or 1930s street map of Palo Alto (A35), tilted (R10 look); yellow marker line from the Stanford campus
  along University Ave/Waverley to 367 Addison Ave, yellow circle + numbered pin `1` @548.15; camera tracks the line in 3D.
- **Motion → next** camera dives into the pin (expo push) — the map gives way to the garage 2.5D world (SC086).
- **SFX** 544.37 `pop_soft`, 545.5–548.0 `marker_long`, 548.13 `pin_pop`, 548.9 `whoosh_big`.

### SC086 · 549.03–556.31 · B079–B080 · NIGHT — 2.5D #3 (the garage)
- **FX** #17 2.5D parallax · **Copy** s10 (approved; timed 544.5–551.5 — re-time)
- **Text** label `CALIFORNIA` @549.03; `PALO ALTO` display, choke reveal, tucked behind the roof @549.91 ("Palo"); no further text ("He does a lot to convince them" is carried by the dolly). No text on "He he says".
- **Visual** s10 as approved: HP garage layers (`assets/archival/hp/layers/backdrop.jpg`, `garage.png`, `hedge.png`, `house.png`), dolly,
  haze, rays, foreground blur. Continue the dolly slowly through 556.3 (Terman "does a lot to convince them").
  CC BY-SA credit line (garage photo).
- **Motion → next** cut to paper document on "his" @556.31 (garage doors close-match → thesis page).
- **SFX** 549.0 `air_swell`, 549.89 `marker_scratch` (choke), 551.49 `pop_soft`.

### SC087 · 556.31–561.59 · B080 · PAPER
- **FX** #5 document (DOCUMENT #6: Hewlett's thesis title page) (+#18 highlighter) · **Copy** s06 (paper restyle)
- **Text** label `his thesis` @560.47 ("thesis").
- **Visual** title page "A New Type Resistance-Capacity Oscillator" (A36: Stanford scan if obtainable; else a typeset recreation in
  Crimson Pro) on paper, 3D tilt, halftone; yellow highlighter on "Oscillator" @561.0.
- **Motion → next** push into "Oscillator" → cut to the instrument (SC088).
- **SFX** 556.4 `paper_rustle`, 560.45 `pop_soft`, 561.0 `highlighter_swipe`.

### SC088 · 561.59–567.03 · B081 · NIGHT
- **FX** #16 hi-quality photo treatment (+#19 callouts) · **Copy** s07 + s11
- **Text** `audio oscillator` display halate @563.43 ("audio"); no other label.
- **Visual** `assets/archival/hp/hp_200A_audio_oscillator_front_panel.jpg` (CC BY-SA 2.0 — credit), fringe blur, dust, vignette, slow zoom
  to the big dial; rough vermilion circle around the dial @565.3.
- **Motion → next** dial needle swing → sine wave line continues into the diagram (SC089).
- **SFX** 563.41 `pop_soft`, 565.28 `marker_scratch`, 566.9 `tone_blip` (very soft 440 Hz, 0.2 s — the instrument's voice).

### SC089 · 567.03–573.91 · B082 · PAPER
- **FX** #2 animated diagram · **Copy** s03 (paper chart)
- **Text** label `audio equipment makers` @567.99 ("making"); serif-i `for consumers` @571.67.
- **Visual** paper diagram: oscillator icon (halftone 200A crop) → ink signal line → amplifier/speaker icon (1930s radio cabinet halftone);
  a clean sine wave draws along the line (dashoffset, 12 fps) @572.3.
- **Motion → next** sine wave continues into SC090's footage as an overlay.
- **SFX** 567.97 `pop_soft`, 571.65 `pop_soft`, 572.3–573.8 `pencil_scribble`.

### SC090 · 573.91–578.79 · B082 · NIGHT
- **FX** #14 gate weave (+ sine overlay) · **Copy** s05
- **Text** `test` display halate @573.91 ("test"); serif-i `good enough — or not?` @577.75 ("good").
- **Visual** 1930s radio factory / sound-testing footage (A37, Prelinger PD) with weave + flicker; thin bone sine wave overlaid,
  wobbling @575.3 then snapping clean @577.75 (pass).
- **SFX** 573.9–578.7 `projector_loop` (low), 573.89 `tick_soft`, 577.73 `chime_soft`.

### SC091 · 578.79–588.15 · B083 · PAPER
- **FX** #12 collage (thesis → product) (+#13 fill) · **Copy** s08
- **Text** card tag `PhD` @580.39 ("PhD") — the card's title line reads `thesis` @581.27 as he self-corrects (both as narrated); `commercialize` display ink, yellow fill pop → ink @585.03;
  serif-i `all the research` @587.27 ("research").
- **Visual** three cards in a row linked by ink arrows: thesis page (from SC087) → HP 200A photo → a price-tag card
  (own-made, blank tag with a "$" sign) drawn on @585.03.
- **Motion → next** the $ tag flips into a banknote (SC092).
- **SFX** 581.25 `pin_pop`, 583.0 `marker_scratch`, 585.01 `pop_soft`, 587.9 `paper_flip`.

### SC092 · 588.15–594.15 · B084 · NIGHT
- **FX** #18 rough edges (choke) · **Copy** s04/s10 choke
- **Text** `money` display yellow halate, choke reveal @591.59 ("money"); serif-i `to get it off the ground` @593.43 ("off"). No text on "finds when I say finds".
- **Visual** 1930s banknote / gold certificate engraving (A16) halftone cutouts floating up slowly (12 fps), tinted, on night; faint streaks underneath.
- **Motion → next** a banknote turns into a fellowship letter (paper flip).
- **SFX** 591.57 `marker_scratch` (choke), 592.5 `paper_rustle`, 593.9 `paper_flip`.

### SC093 · 594.15–598.87 · B085 · PAPER
- **FX** #13 random-letter text (+#19 underline) · **Copy** s10 (random) + s11 (underline)
- **Text** `fellowship` display ink, random letters @594.71 ("fellowship"); serif-i `he makes sure they get it` @597.27 ("makes");
  vermilion rough underline under "fellowship" @598.23 ("fellowship"). No text on the repeat at 595.19.
- **Visual** own-made fellowship letter card (1930s look) (our fonts, halftone, paper tex) pinned at an angle; small Hewlett and Packard
  halftone portraits clipped to it.
- **Motion → next** slow push continues; ground darkens (SC094).
- **SFX** 594.69 `letter_ticks`, 597.25 `pop_soft`, 598.21 `marker_scratch`.

### SC094 · 598.87–600.00 · B085 · NIGHT (hold / fade)
- **FX** #7 textures (+#14 flicker) · **Copy** s10 (garage backdrop) / any
- **Text** none ("On top of that, he puts his…" is cut off — never caption it).
- **Visual** cross-dissolve to the 2.5D garage backdrop (SC086 world) at 0.6 brightness, grain + dust + a slow light-leak, flicker
  rising slightly; fade to black begins 599.5 (or hold if the edit continues past 600).
- **SFX** 598.9 `air_swell` (soft), 599.8 `projector_click` (end).
- **Music** ride out the `momentum_building` phrase, no cadence (cliffhanger).

---

## 7. Variations ledger (what makes each repeat different)

| effect | variants used |
|---|---|
| #11 TV | SC015 Philco Predicta 1960 (existing) · SC030 1930s wooden radio-cabinet TV (RCA TRK-12 type) · SC051 1950s portable · SC067 late-1940s console with doors |
| #5 newspaper/document | SC021 NYT 7 Nov 1928 front page (night, 3D page) · SC031 Stanford Daily clipping (paper, torn) · SC036 Founding Grant 1885 (night, document) · SC050 1916 book with page turn (paper) · SC062 MIT Bulletin VI-A page (paper) · SC087 Hewlett thesis title page (paper) |
| #3 / R10–R12 maps | SC007 Blue Marble US burn + river (s02) · SC008 R12 Indiana navy relief · SC017 R11 beige US with leader labels · SC032 brain-drain particle flow · SC042 great-circle arcs Stanford→Boston · SC053 R10-A 1920s railroad map · SC056 R10-B Boston/Cambridge street atlas · SC075 R12 California vermilion relief · SC085 R10-C Palo Alto topo/street map |
| #17 2.5D | SC023 Stanford Main Quad 1891/96 (founding) · SC047 1920s students on the Quad (Terman intro) · SC086 HP garage, 367 Addison (s10) |
| #9 shutter | SC018 Eastern companies · SC038 rival campuses · SC057 MIT→Harvard · SC084 Eastern companies callback (faster) |
| #15 curve cut | SC011 modern valley→1920s orchards · SC022→SC023 Hoover→Main Quad · SC034 Hoover 1928→Stanford today · SC063 lab→factory→campus (double) |
| #8 streaks | SC001 slow warm (prelude) · SC002/SC005 under titles · SC046 short act button · SC055 cool/navy tint · SC079 faster, warmer (momentum) |
| #4 film titles | SC002 SILICON VALLEY · SC005 12 · SC046 a good start · SC055 SILICON VALLEY (crossed out) |
| #13 text | odometer SC004, SC071, SC061 · count SC005, SC012, SC048, SC079, SC082 · random SC002, SC076, SC093 · fill SC003, SC043, SC049, SC073, SC091 |
| #18 rough/highlighter | choke titles SC016 (tickets), SC020 (BRAIN DRAIN), SC039 (money), SC069 (TABOO stamp), SC092 · highlighter SC009, SC013, SC021, SC031, SC039, SC050, SC062, SC087 |
| #19 markups | X SC024 · strike SC037, SC045, SC070 · circle/arrow SC008, SC043, SC064, SC068 (s11), SC081 · underline SC093 · strings SC066/SC074 |
| #12 collage | apples/oranges SC010 · Stanford card SC019 · ADMITTED stamp SC026 · Lou Henry SC028 · timelines SC041/SC044/SC052 · logos SC060 · cork SC066/SC074 · fork SC083 · thesis→product SC091 |
| #10 Vox layered | SC003 modern SV · SC025 Quaker · SC049 Terman family · SC061 labs · SC070 ivory tower · SC073 Raytheon · SC080 Hewlett & Packard (s09) |
| #14 weave | SC027 Hoover newsreel · SC040 1910s Stanford · SC045 Quad + light leak · SC059 free flow · SC072 labs · SC077 graduation · SC090 audio testing |
| #16 HQ photo | SC014 empty West · SC022 young Hoover · SC034 Hoover 1928 · SC054 MIT aerial · SC065 Terman · SC088 HP 200A |
| #2 charts (refs) | SC006 R4 · SC009 R8 · SC013 R1 · SC029 R7 · SC033 R5 · SC035 R6 · SC058 triangle diagram · SC078 R5-b · SC089 signal diagram |

## 8. Coverage table — effects and reference layouts → scenes

| item | scenes (primary in **bold**) | count |
|---|---|---|
| #1 B-roll matched to words | every photo/footage scene: SC003, SC011, SC014, SC015, SC018, SC021–SC023, SC025, SC027, SC034, SC036, SC038, SC040, SC045, SC047, SC054, SC057, SC059, SC063, SC065, SC067, SC068, SC072, SC077, SC080, SC082, SC084, SC086, SC088, SC090 | 30+ |
| #2 Animated charts/stats | **SC006, SC009, SC013, SC029, SC033, SC035, SC058, SC078, SC089** | 9 |
| #3 Maps | **SC007, SC017, SC032, SC042, SC053, SC075**; SC008, SC056, SC085 | 9 |
| #4 Film-title typography | **SC002, SC005, SC046, SC055**; halate on every night text | 4+ |
| #5 Newspapers/documents | **SC021, SC031, SC036, SC050, SC062, SC087** | 6 |
| #6 Sound | every scene (SFX lists) + music turns at 4.32, 35.36, 62.49/63.21, 93.53, 143.94, 157.22, 214.67, 286.84, 346.07, 474.95, 491.48, 505.96, 598.87 | all |
| #7 Textures | every scene; **SC094** | all |
| #8 Light streaks | **SC001, SC079**; SC002, SC005, SC046, SC055, SC092 | 7 |
| #9 Shutter transition | **SC018, SC038, SC057, SC084**; iris also closes SC017, SC037, SC056, SC083 | 4 (+4 in) |
| #10 Vox layered backgrounds | **SC003, SC025, SC049, SC061, SC070, SC073, SC080** | 7 |
| #11 Vintage TV | **SC015, SC030, SC051, SC067** (4 different sets) | 4 |
| #12 Collage / timelines | **SC010, SC019, SC026, SC028, SC041, SC044, SC052, SC060, SC066, SC074, SC083, SC091** | 12 |
| #13 Text animations | **SC004, SC012, SC048, SC071, SC076, SC082, SC093**; SC002, SC003, SC005, SC043, SC049, SC061, SC073, SC079, SC091 | 16 |
| #14 Gate weave + flicker | **SC027, SC040, SC045, SC059, SC072, SC077, SC090**; SC011, SC014, SC018, SC094 | 11 |
| #15 Cutting the curve | **SC011, SC063**; SC022→SC023, SC034 | 4 |
| #16 Hi-quality photo | **SC014, SC022, SC034, SC054, SC065, SC088**; SC008, SC018, SC038, SC057, SC082 | 11 |
| #17 2.5D | **SC023, SC047, SC086** | 3 |
| #18 Rough edges + highlighter | **SC016, SC020, SC039, SC069, SC092**; highlighter SC009, SC013, SC021, SC031, SC050, SC062, SC087 | 12 |
| #19 Vox markups | **SC024, SC037, SC064, SC068, SC081**; SC008, SC016, SC019, SC043, SC045, SC066, SC070, SC074, SC083, SC088, SC093 | 16 |
| #20 Map/document callouts | **SC008, SC043, SC056, SC085**; SC017, SC053, SC075 | 7 |
| R1 bars + halftone building + label box | SC013 ("90%" label box) | 1 |
| R2 dollar's-worth line chart | not used (optional — see Q2) | 0 |
| R3 coin in pieces | skipped (user instruction) | 0 |
| R4 ranked bars + circle portraits | SC006 | 1 |
| R5 isotype grid | SC033, SC078 | 2 |
| R6 horizontal bars, serif italic title | SC035 | 1 |
| R7 line + shaded era band + annotations | SC029 | 1 |
| R8 dot-matrix semicircle + highlighted phrase | SC009 | 1 |
| R9 cork board + red string | SC066, SC074 | 2 |
| R10 old map + yellow marker + numbered pin | SC053, SC056, SC085 | 3 |
| R11 muted beige map, leader labels | SC017 | 1 |
| R12 grey relief + filled region + halftone + glow | SC008 (Indiana, navy), SC075 (California, vermilion) | 2 |

## 9. Sequence check (primary effect + ground, in order)

No primary effect repeats back-to-back; never more than 3 scenes in a row on the same ground (cork/light-map = PAPER).

| SC | t | ground | primary | | SC | t | ground | primary |
|---|---|---|---|---|---|---|---|---|
| 001 | 0.00 | N | #8 | | 048 | 296.23 | P | #13 |
| 002 | 4.32 | N | #4 | | 049 | 304.23 | N | #10 |
| 003 | 8.16 | N | #10 | | 050 | 308.87 | P | #5 |
| 004 | 13.20 | P | #13 | | 051 | 314.55 | N | #11 |
| 005 | 17.52 | N | #4 | | 052 | 321.27 | P | #12 |
| 006 | 21.76 | P | #2 R4 | | 053 | 330.63 | P | #3 R10 |
| 007 | 32.88 | N | #3 | | 054 | 337.19 | N | #16 |
| 008 | 41.52 | N | #20 R12 | | 055 | 342.95 | N | #4 |
| 009 | 46.48 | P | #2 R8 | | 056 | 348.31 | P | #20 R10 |
| 010 | 51.20 | P | #12 | | 057 | 355.59 | N | #9 |
| 011 | 54.48 | N | #15 | | 058 | 359.98 | P | #2 |
| 012 | 58.49 | P | #13 | | 059 | 366.22 | N | #14 |
| 013 | 64.17 | P | #2 R1 | | 060 | 371.82 | P | #12 |
| 014 | 69.77 | N | #16 | | 061 | 378.62 | N | #10 |
| 015 | 73.77 | N | #11 | | 062 | 388.70 | P | #5 |
| 016 | 84.49 | P | #18 | | 063 | 398.46 | N | #15 |
| 017 | 93.53 | P | #3 R11 | | 064 | 405.90 | P | #19 |
| 018 | 100.25 | N | #9 | | 065 | 410.94 | N | #16 |
| 019 | 110.17 | P | #12 | | 066 | 416.86 | P | #12 R9 |
| 020 | 118.49 | P | #18 | | 067 | 423.31 | N | #11 |
| 021 | 122.98 | N | #5 | | 068 | 427.39 | N | #19 |
| 022 | 131.46 | N | #16 | | 069 | 437.23 | P | #18 |
| 023 | 136.98 | N | #17 | | 070 | 443.63 | N | #10 |
| 024 | 141.70 | P | #19 | | 071 | 449.07 | P | #13 |
| 025 | 146.74 | N | #10 | | 072 | 454.83 | N | #14 |
| 026 | 154.58 | P | #12 | | 073 | 460.99 | N | #10 |
| 027 | 158.66 | N | #14 | | 074 | 470.95 | P | #12 R9 |
| 028 | 166.34 | P | #12 | | 075 | 479.31 | N | #3 R12 |
| 029 | 169.86 | P | #2 R7 | | 076 | 486.92 | P | #13 |
| 030 | 177.30 | N | #11 | | 077 | 491.48 | N | #14 |
| 031 | 182.03 | P | #5 | | 078 | 496.92 | P | #2 R5 |
| 032 | 186.43 | N | #3 | | 079 | 504.92 | N | #8 |
| 033 | 191.39 | P | #2 R5 | | 080 | 513.08 | N | #10 |
| 034 | 199.07 | N | #16 | | 081 | 519.24 | P | #19 |
| 035 | 206.27 | P | #2 R6 | | 082 | 527.32 | N | #13 |
| 036 | 214.67 | N | #5 | | 083 | 531.00 | P | #12 |
| 037 | 225.63 | P | #19 | | 084 | 536.92 | N | #9 |
| 038 | 229.79 | N | #9 | | 085 | 542.47 | P | #20 R10 |
| 039 | 237.32 | P | #18 | | 086 | 549.03 | N | #17 |
| 040 | 244.28 | N | #14 | | 087 | 556.31 | P | #5 |
| 041 | 249.00 | P | #12 | | 088 | 561.59 | N | #16 |
| 042 | 256.20 | N | #3 | | 089 | 567.03 | P | #2 |
| 043 | 266.12 | N | #20 | | 090 | 573.91 | N | #14 |
| 044 | 268.52 | P | #12 | | 091 | 578.79 | P | #12 |
| 045 | 275.48 | N | #14 | | 092 | 588.15 | N | #18 |
| 046 | 285.16 | N | #4 | | 093 | 594.15 | P | #13 |
| 047 | 287.56 | N | #17 | | 094 | 598.87 | N | #7 |

(Scene lengths: shortest SC094 1.13 s (fade/hold), SC043 2.4 s and SC046 2.4 s (single-word buttons); longest SC006 11.1 s
and SC036 11.0 s (continuous chart / document moves with internal beats). Median ≈ 5.9 s.)

## 10. Open questions for the user

(Fact-related questions dropped per the user's decision: text follows the narration.)

1. **Company logos (SC006 R4, SC009 R8).** Use the 12 real logos in the circles (trademarks; Commons SVGs), HQ-building photos in
   circles, or plain wordmarks set in Cooper Hewitt?
2. **R2 "A Dollar's Worth".** Not used. Want it anyway (e.g. an engraved-banknote duotone line chart behind "$100 a month" in SC082)?
   It would need a money-over-time series, i.e. text beyond the narration.
3. **Hewlett's thesis page (SC087).** If no scan is reachable, is a typeset recreation in Crimson Pro acceptable?
4. **Young Terman photo.** If no 1910s–20s portrait is found (Stanford Quad yearbooks), use the 1955 portrait small and halftoned?
5. **Cold open (SC001).** "After him? Well, I don't think I need to tell you much." gets no caption — streaks only. OK?
6. **SC077 footage.** If no Stanford commencement film is found, may we reuse the Berkeley 1932 clip (unlabelled) as generic graduation footage?
7. **Ending (SC094).** Fade to black at 600.00, or hold on the garage because the full episode continues?
8. **Lou Henry name (SC028).** VO only says "his wife" — keep the small name label under her card, or show "his wife" only?
9. **Missing audio docs.** MANUAL §7 references `assets/audio/LIBRARY.md` and `MIX_RULES.md`, which don't exist yet; the sound agent should write them.
