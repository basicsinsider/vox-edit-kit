# Intro fixes after Krish's review (2026-10-31)

Krish loved the intro except: (1) one area of grid paper looked poor, (2) a few cuts land before the animation finishes
(e.g. the phones shipped to the US), (3) the flat grey/beige maps. All three are fixed below. Rules: MANUAL §10.9.
Checks: `tools/sync_audit.py` 0 flagged on intro01/02/03 (transcript_intro.json) · `hyperframes lint` 0 errors ·
snapshots of every changed scene's last 0.6 s and 1:1 crops looked at (sandbox `work/introfix/.snap/`).
**Sound:** SFX markers in `compositions/intro0{1,2,3}.sfx.json` were moved with the events below → re-run
`tools/audio/place_sound.py` before the next render. **Not rendered, not committed.**

## A. Paper quality (no upscaled K+E scans)
The K+E working copies (`assets/intro/papers/ke1960_*.jpg`) are 1920-wide UPSCALES of 780–1616 px scans, shown full frame
and scaled ×1.25 (2.2–2.9× upscale → soft grid lines, seen at 1:1). Replaced by Texturelabs `paper_graph_01_hires.jpg`
(4240 px), always displayed ≤ native; two paper layers kept (cream 60 % + grid 90 %).

| scene | before | after |
|---|---|---|
| IS024 D15 diagram | ke1960_cover_grid_blue (820 px) full frame | graph_01_hires, new `.p2.gr` class (scale 1.5, desat/contrast tuned to the old washed look) |
| IS026 25,000 isotype | ke1960_10x10_grid_black (780 px) | graph_01_hires scale 1.9, darker lines |
| IS036 idea card dropped | ke1960_cross_section_green (1616×600) | graph_01_hires scale 1.65, −0.8°, other crop |
| IS040 bar for bar | ke1960_cross_section_green | graph_01_hires scale 1.4, other crop |
| IS042 callback table | ke1960_cover_grid_blue | graph_01_hires scale 1.55, a little more colour (old blue-grey) |
| IS052 two bars (intro03) | ke1960_mm_grid_green_norm (1376 px) full frame | graph_01_hires 2880 px wide |
| IS007/IS008 export chart (intro01) | paper_graph_01.jpg (1920) — IS008 at 2900 px = 1.5× upscale | paper_graph_01_hires.jpg |
| IS063 progress bar sheet | paper_graph_01.jpg | paper_graph_01_hires.jpg |
| IS014 idea card / IS036+IS040 card backs | K+E cross-section as small card ground (0.7–0.8× native) — allowed prop | switched to the native `_hires` file (no double resample) |

## B. Animation timing — every scene audited (66)
Method: each composition's GSAP timeline was dumped in a headless page (every tween's start/end + target) and compared with
its scene's cut / whip start; flagged scenes were snapshotted in their last 0.6 s. Rule applied: key animation complete
≥ 0.5 s before the whip starts / the hard cut (camera or secondary motion may carry a cut-on-action meanwhile).
Text cues never moved off their words (0–120 ms before); where a scene start moved, its first cue still lands after it.

| scene | problem | fix |
|---|---|---|
| **IS006 phones → US** (Krish's example) | route drew 19.70–20.90 but the whip started 20.32: never arrived | the **telephone now rides the route** (19.15–20.05) and the camera follows it (driven by the route tween); lands on San Francisco 20.05, holds to 20.56 with "United States", push, whip 20.48 → **20.72** (IS007 "4" lands 20.88 on its word) |
| IS001 1983 | odometer locked 0.80, whip 0.96 | odometer T(0.20) 0.26 s stagger 0.02 → locked 0.52; whip 0.28 s → 0.46 s hold (bounded by "Robert" @1.12) |
| IS002 Tsao/UMC | UMC card slid until 5.44, past the cut 5.28 | card 0.7 s (lands 5.04); push 5.28; cut 5.28 → 5.54 (IS003 footage, no text) |
| IS004 insight | settled 9.82, whip 10.00 | choke 0.5 s; whip 10.16 → 10.40 |
| IS005 "the world" | rise ended after the push-through began; faded mid-rise | rise 0.6 s (15.34); fade 15.66; push 15.50; cut 15.52 → 15.86 |
| IS007 bar 4→24 | bar topped out 24.46, push 24.60 | bar 0.9 s (23.96) |
| IS008 12 months | 12 ticks until 27.98, whip 27.92 | 2 ticks per 12 fps step (done 27.48); whip 28.08 → 28.16 |
| IS009 phones | "phones" rising into the paper slide | rise 0.45 s; slide 31.80 → 32.17; IS010 line starts 32.20, peak dot 32.80 |
| IS011 sales died | pen arrow ended 40.21, cut 40.40 — and it was **drawn off-frame** (FX.markupDefs resets the viewBox to 1920×1080 on a 3000×1400 svg) | viewBox restored → the arrow is now visible; arrow 39.46–40.06; fall 40.11; cut 40.40 → 40.56 |
| IS012 one product | cross drawn 46.70–47.06, whip 47.12 | icon 0.6 s; cross 46.42 (on "product"); whip 47.28 → 47.44 |
| IS013 anything in demand | 5 bars grew until 53.85, past the hard cut 53.12 | bars from 51.36, 0.9 s (done 52.60) |
| IS014 novel concept | highlight 57.52, slide 57.88 | highlight 0.3 s; slide 57.95 |
| IS018 permission | rise into the cut | T(72.10), 0.35 s (cut 72.93) |
| IS019 a year ago | bracket 77.30, whip 77.49 | bracket 0.5 s from 76.62 (77.12); whip 77.65 → 77.80 |
| IS023 one condition | highlighter ended after the whip started | highlight 93.94, 0.28 s; whip 94.55 → 94.71 (narration-bound: next sentence @94.61) |
| IS024 D15 | US circle popped until 99.63, past the cut | pop 0.5 s, ink 0.45 s; push 99.63; cut 99.57 → 99.95 (IS025 spot/flicker moved with it) |
| IS025 | last words rising into the whip | rises 0.6 s |
| IS027 reorient | compass/building turned until 120.22 (cut 120.26) | turn 0.9 s (119.72) |
| **IS028 flight to New York** | plane landed 123.26 = the whip | route + plane 121.70–122.60, NY dot 122.55, camera pull-out 121.60; text rises 0.4 s |
| IS029 executive | silhouette slid in until 125.44 (whip 125.08) | in at 123.98, 0.6 s |
| IS031 on top of the world | words rose past the cut 134.98 | rises 0.4 s; cut → 135.42 |
| IS032 anymore | rise past the whip | 0.5 s; whip 140.68 → 141.12 |
| IS033 stonewalled | last stone bounced to 144.72, cut 144.82 | cut → 145.25 (telegram camera re-timed) |
| IS034 telegram | typed 148.89, slide 149.20 | slide 149.36, 0.36 s |
| IS035 board ring | 12 dots until 154.64, whip 154.20 | dots from "your" 153.46, ½-step stagger, 0.35 s (154.02); whip 154.36 → 154.60 |
| IS036 dropping the idea | card fell until 157.25 (cut 157.22) | fall 0.74 s from 156.22 (gone 156.96); cut → 157.46 |
| IS037 breaks ground | rises 0.9 s on the last words | 0.6/0.4/0.3 s (narration-bound: IS038 text @160.68) |
| IS039 never a product | cross until 168.02, whip 167.96 | cross 167.40; rises 0.5 s; whip 168.12 → 168.50 |
| IS040 bar for bar | highlighter bars until 170.92, cut 170.98 | bars 0.25 s at 170.44/170.50 (170.75); cut → 171.25 |
| IS041 CEO | rises into the whip | 0.5 s (face-cam clip end fixed, so the whip stays) |
| IS042 In New York | rises into the push | 0.5 s; push 179.84; cut 180.05 → 180.18 |
| IS044 to this very day | words faded 0.07 s after completing | words 0.3 s; halves part 190.30; fade 190.60; cut 190.61 → 190.80 |
| IS045 rival lines | end dots popped into the whip | lines 4.5 s (195.67), dots 195.66 0.4 s; whip 196.55 → 196.75 |
| IS046 | lines drew to 198.60 | 1.6 s from 196.78 |
| IS047 greatest business stories | "ever" completing as the whip started | words 0.3 s; whip 201.84 → 202.30 |
| IS048 the West | West fill ended 206.95, after the cut 206.77 | fill 0.5 s (206.65); shrink 206.85; cut → 207.25 |
| IS050 rivalry | rise into the hard cut | 0.4 s |
| IS053 Hsinchu | road + TSMC/UMC plots drawn 228.13–228.73, cut 228.61 | road 227.80 0.5 s, plots 227.90 (done 228.30); cut → 228.86 (IS054 camera re-timed) |
| IS054 replica quote | last underline 233.05, whip 233.28 | whip 233.44 → 233.80 |
| IS058 Searching Lessons | title settled 253.10, cut 253.30 | 1.0 s; cut → 253.40 |
| IS059 built for radio | radio/needle until 255.30, whip 255.16 | radio 253.80 0.9 s, needle 254.62 0.4 s (255.02); whip 255.32 → 255.68 |
| IS062 long story | words rising into the sheet | 0.3 s; sheet 265.56 → 265.80 |
| IS063 progress bar | crawled (linear) until 270.04 = the cut | 268.60, 0.9 s FX.ease.inOut (269.50) |
| IS064 historic images | stamp 271.35–271.60, whip 271.56 | stamp 270.70 |
| IS066 here's the story | rise into the end flash | 0.3 s |

Left as designed (not violations): IS016 pin + push-through (the push IS the transition), IS020 card rotation (continuous
cut-on-action), IS022→IS023 hover handoff, IS038/IS060 push/line transitions, IS055/IS056 camera push, IS058 film strip
pass-through. Narration-bound holds < 0.5 s (next scene's text lands right after): IS001 0.46, IS023 0.35, IS037, IS041.

**Gotcha found (now in MANUAL §4.2):** face-cam `<video class="clip">` elements become visible at their own `data-start` even
inside a scene that is still hidden — so moving a cut later also needs the clip's `data-start` (+ same delta on
`data-media-start`, lip sync unchanged) moved: IS041, IS046, IS049, IS059 (IS059 duration +0.30, clip is long enough).
Clips that ended at the old cut were lengthened: IS002 chip (4.42), IS012 footage (7.04).

## C. Maps (map kit, `assets/maps/kit/`)
`project/intro/gen/intro_maps_kit.py` re-projects the kit rasters into the **exact pixel spaces the scenes already used**
(`assets/intro/derived/maps/`, SOURCES.md there), so routes, fills, pins and OSM overlays still line up; checked by overlaying
the old masks/paths.

| scene | before | after |
|---|---|---|
| IS006 phones → US | pacific_beige (30 px/deg) | world_atlas re-projected, 45 px/deg + East-Asia-atlas inset (128 px/deg) for the Taiwan close-up; Formosa 1943 map now multiplies (no white halo) |
| IS016 didn't exist | world_desat_3840 | world_night 7680 + native Taiwan inset for the 7× push; credit "Relief: AWS Terrain Tiles (PD) · Natural Earth" |
| IS028 flight to NY | pacific_relief_grey_2850 (sepia-washed) | same atlas file as IS006 (3× density), lighter filter |
| IS035 Taiwan 1984 | taiwan_relief_grey | taiwan_night (celadon burn unchanged) |
| IS045 ghost Taiwan | taiwan_relief_grey | taiwan_night (brightened under the grey ghost filter) |
| IS048/IS049 world | world_beige (NASA desat colourised) | world_atlas 6480 (1.5×); credit updated |
| IS050 2.5D Taiwan | taiwan_relief_grey | taiwan_atlas, land-only (alpha land mask) on the night sea |
| IS053 Taiwan → Hsinchu | grey relief + soft Sentinel-2 | taiwan_sat (ground = its sea colour) → Esri z17 aerial composited over Sentinel-2 at 1.25× (park, roads, TSMC/UMC plots line up); credit "Imagery: Esri, Maxar, Earthstar Geographics · …", now shown from the scene start |
| IS055/IS056 world | world_dark | world_night 4320 + native Taiwan inset for the 3.2× push; credit updated |
Not changed: IS002 Taiwan panel, IS025/IS039 dim background world maps, IS038/IS042 1945 town plan (period prop).
