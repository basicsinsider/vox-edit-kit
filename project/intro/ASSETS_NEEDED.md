# ASSETS NEEDED — INTRO (0.00–275.06)

Deduplicated list for `EDIT_NOTES.md` (IDs `E..` = exists, `N..` = still needed / to make). Snapshot of the folders taken
2026-10-31 while gatherers A/B/C were still working — **gatherers: flip ❌ → ✅/🔁 with the path when you land a file**,
and log every file in its folder's `SOURCES.md` (subject, URL, licence, author, date, size; bboxes for documents).

Rules: free / PD / CC0 / CC BY(-SA) only (BY → 13 px on-screen credit); never log in; look at every file; reject wrong
subject/era, watermarks, < 1600 px long side for full-frame (≥ 3000 px for 2.5D). **Usage ≤ 2 per photo/clip in this
chunk** — the "uses" column is the budget; editors must not exceed it. Maps, papers, textures, icons and our own graphics
are motifs (no limit) but keep the grade identical.

Legend: ✅ exists · 🔁 substitute · ❌ to find · 🛠 to make (from existing material).

## 1. People (photos → circles, cut-outs, duotones)
| ID | status | path / need | scenes | uses | notes |
|---|---|---|---|---|---|
| E01 | ✅ | `assets/intro/photos/tsao_portrait_cc0.jpg` (1280×1921, museum, vase foreground) | IS002 cut-out, IS017 2.5D | 2 | 2.5D wants ≥ 3000 px — fetch the larger original if Commons has it |
| E02 | ✅ | `assets/intro/photos/tsao_advisor_cc0.jpg` (black polo, grey bg — clean cut-out) | IS027 D15 circle, IS044 poster | 2 | |
| E03 | ✅ | `assets/intro/photos/tsao_rally_2023.jpg` (full figure on stage) | IS033 stonewall cut-out | 1 | crop above the mic hand |
| E24 | ✅ | `assets/intro/photos/chang_2018.jpg` (1920×1280, speaking) | IS043 reveal (+ silhouette matte N38 cut from it), IS044 poster | 2 | **hidden until 180.69**; red duotone |
| E25 | ✅ | `assets/intro/photos/chang_award.jpg` (with Chen Chien-jen — crop to Chang only) | IS052 D02 circle, IS056 circle | 2 | |
| E04 | ✅ | `assets/intro/photos/chang_1951_mit.jpg` (MIT yearbook, 1951) | IS064 D07 collage (historic image) | 1 | after the reveal only |
| E05 | ✅ | `assets/intro/photos/chang_and_sophia_cc0.jpg` | reserve | 0 | |
| E06 | ❌ | `assets/intro/photos/chang_portrait_cc0.jpg` is a 2 KB broken file | — | 0 | re-download or delete (gatherer A) |
| N02a | ❌ | Robert Tsao photo #3, head & shoulders, ≥ 1200 px | IS030 dinner-collage chip (+ its IS042 callback) | 2 | Commons "Robert Tsao" / "曹興誠"; Office of the President ROC Flickr (CC BY 2.0); zh/en Wikipedia images |
| N02b | ❌ | Robert Tsao photo #4, frontal, plain bg | IS052 D02 circle, IS056 circle | 2 | same sources; a 1980s photo would be ideal but is unlikely to be free |
| N38 | 🛠 | grey executive silhouette (head & shoulders), matte cut from the E24 crop, filled neutral — **not recognisable** | IS024, IS025, IS027, IS029, IS030, IS041 (behind FC1), IS042, start of IS043 | graphic | intro02 makes `assets/intro/cutouts/silhouette_exec.png` |
| N38b | 🛠 | person pictogram SVG (D03 isotype) in ink/grey + the silhouette as leader icon | IS026 | graphic | adapt `assets/icons/graduate*.svg` style |

## 2. Logos
| ID | status | need | scenes | uses |
|---|---|---|---|---|
| N03 | ❌ | UMC logo (SVG/PNG, recolour to blue `#1d5c9e`) | IS002, IS019 (+ IS027 small) | logo |
| N04 | ❌ | TSMC logo (SVG/PNG, red `#e03f2c`) | IS043, IS051 | logo |
Source: `npx --yes hyperframes@0.8.217 media-use resolve --type logo --entity "UMC" / "TSMC" --project .` → `assets/intro/logos/`; fallback Commons "UMC logo.svg", "TSMC logo.svg". (E26 `umc_fab8ab.jpg` and `umc_hsinchu.jpg` show the real UMC sign as a cross-check.)

## 3. Buildings, places, objects (photos)
| ID | status | path / need | scenes | uses |
|---|---|---|---|---|
| E26 | ✅ | `assets/intro/photos/umc_fab8ab.jpg` (UMC building with logo disc) | IS020 cut-out (rotating on the compass) | 1 |
| E27 | ✅ | `assets/intro/photos/tsmc_fab5.jpg` | IS051 panel | 1 |
| E28 | ✅ | `assets/intro/photos/tsmc_fabs_hsinchu_01.jpg` | IS051 panel | 1 |
| E29 | ✅ | `assets/intro/photos/tsmc_rd_night.jpg` | IS051 panel | 1 |
| E35 | ✅ | `assets/intro/photos/hsp_40th.jpg` (Hsinchu Science Park 40th sign) | IS054 card | 1 |
| E22 | ✅ | `assets/intro/photos/wafer_12in.jpg` | IS005 alt for the wafer | 0–1 |
| — | ✅ | `umc_hsinchu.jpg`, `umc_ut_tower.jpg`, `intel8088_chip.jpg`, `cleanroom_cc0.jpg`, `wafer_researcher_cc0.jpg` | reserve (chunk 1) | 0 |
| — | ❌ | `cleanroom2_cc0.jpg` is broken | — | — |
| N05 | ❌ (optional) | 1980s fab/cleanroom photo, PD (Sandia/DOE, NIST, NASA JPL) ≥ 2400 px | IS012 alt only | 0–1 |
| N07 | ❌ | NASA Blue Marble globe (round, PD), ≥ 2400 px | IS005 curve-cut target | 1 | NASA Visible Earth "Blue Marble" |
| N09 | ❌ | 1980s push-button telephone, clean cut-out (ideally "Made in Taiwan"), ≥ 1600 px | IS006 pin, IS007 halftone base (D01) | 2 | Smithsonian Open Access (CC0), Commons "push-button telephone" |
| N16 | ❌ | stone/brick wall photo, frontal, ≥ 2400 px, CC0/PD | IS033 | 1 | Commons, Openverse CC0 |
| N18 | ❌ | groundbreaking ceremony — ceremonial shovels in dirt, PD photo or footage, no readable signage | IS037 | 1 | NARA, NASA, DOE, USDA Flickr (PD) |
| N25 | ❌ | modern Taipei skyline (Taipei 101), dusk, **≥ 3000 px** + 2.5D layer set 🛠 (sky / skyline / foreground) | IS050 | 1 | Commons "Taipei skyline" CC BY-SA |
| N34 | ❌ | old cloth-bound hardcover book on a dark desk, title area clear, PD/CC0 | IS047 | 1 | Commons / Openverse CC0 |

## 4. Paintings, posters, illustrations (Krish's rule 4)
| ID | status | need | scenes | uses | sources |
|---|---|---|---|---|---|
| N13 | ❌ | Titian, *Sisyphus* (1548–49, Prado), colour, ≥ 2400 px | IS021 | 1 | Commons (PD-Art) |
| N22 | ❌ | New York vintage travel/WPA or 1939 World's Fair poster, colour | IS029 | 1 | LOC WPA posters via Commons (PD) |
| N27a | ❌ | pictorial Silicon Valley / Palo Alto / Santa Clara County illustrated map (Krish's example), PD/CC | IS054 (+ stamp icon in IS055) | 1 + icon | Commons, archive.org, Calisphere PD items; fallback ✅ `assets/maps/old/usgs_palo_alto_1899_topo.jpg` |
| N28 | ❌ | vintage radio illustration / ad (1930s–50s), colour, PD | IS059 (behind FC5) | 1 | Commons "radio advertisement 1930s" |
| N29 | ❌ | vintage colour illustration of a man mopping sweat from his brow (Puck / Judge lithograph, PD) | IS063 | 1 | LOC Puck via Commons |
| N14 | ❌ | engraved compass rose (PD) | IS020 | 1 | Commons old-map compass roses |
| N31 | ❌ | 3–4 historic Taiwan photos for chunk 1 (1950s–80s; e.g. USAID / US Army PD, Taiwan gov open data) | IS064 collage (teaser) | 1 each | Commons |

## 5. Documents, manuals, papers
| ID | status | path / need | scenes | uses |
|---|---|---|---|---|
| N10a | ✅ | `assets/intro/papers/ke1960_10x10_grid_black*.jpg`, `ke1960_mm_grid_green*.jpg` (K+E 1960 catalogue) — D01 chart ground | IS007–008, IS026 | motif |
| N10b | ✅ | `assets/intro/papers/ke1960_cross_section_green*.jpg` — idea-card / notebook ground | IS014, IS036, IS040 | motif |
| N10c | ✅ | `assets/intro/papers/ke1960_business_ruled_orange*.jpg` — ledger timeline | IS019 | motif |
| N10d | ✅ | `assets/intro/papers/ke1960_progress_chart_orange*.jpg` — D02 "decades" ground | IS052 | motif |
| — | ✅ | `ke1960_page_00xx`, `polar_orange`, `log_grid_green`, `cover/back_cover_grid_blue` | reserve | — |
Grade note: the K+E sheets are green/orange — use the `_norm` copies in multiply/overlay and desaturate the rule colour
toward ink-grey (≤ 30 % saturation) so the palette stays ours; never redraw a grid as vector.
| ID | status | need | scenes | uses | sources |
|---|---|---|---|---|---|
| N11a | ❌ | telephone service-manual page with an exploded view / circuit board (1970s–80s push-button set) | IS009 | 1 | archive.org "Bell System Practices telephone set", "2500 set" |
| N11b | ❌ | UMC telephone tone/pulse dialer IC datasheet page (UM91xx / UM95xx) or UMC data book page | IS009 | 1 | archive.org / bitsavers "UMC data book", "UM91210", "UM9151"; rights = archival (DECISIONS #6); fallback 🛠 typeset datasheet card |
| N12 | ❌ | dictionary page with the "foundry" entry (Webster's 1913 or older, PD), ≥ 2400 px | IS015 | 1 | archive.org |
| N17 | 🛠 | telegram blank, typeset in our fonts on paper_cream (D08 layout), ink/blue header, no seals/signatures | IS034 | 1 | reference D08 only |
| N23 | ❌ | New York restaurant menu (NYPL "What's on the Menu?", no known restrictions) + two place settings (PD photo or our flat illustration) | IS030 (+ IS042 callback) | 2 | NYPL Digital Collections |
| N41 | 🛠 | chapter list + progress readout `0:04:22 / 4:26:14` (D12 layout) | IS062, IS063 bar | graphic | — |

## 6. Footage
| ID | status | path | scenes | uses |
|---|---|---|---|---|
| E07 | ✅ | `assets/intro/footage/fab_floor_manager_walks_rows.mp4` (15 s) | IS003 (+ freeze/cut-out in IS004, same shot) | 1 |
| E08 | ✅ | `assets/intro/footage/fab_hk_workers_microscope_rows_a.mp4` | IS012 | 1 |
| E36 | ✅ | `assets/intro/footage/fab_hk_workers_microscope_rows_b.mp4` | IS065 on the Trinitron | 1 |
| E20 | ✅ | `assets/intro/footage/wafer_closeup_purple.mp4` | IS005 curve cut | 1 |
| E21 | ✅ | `assets/intro/footage/wafer_die_pattern_macro.mp4` | IS002 chip panel | 1 |
| E23 | ✅ | `assets/intro/footage/jet_707_takeoff_hongkong.mp4` | IS031 | 1 |
| E37 | ✅ | `assets/intro/footage/boardroom_blackboard_meeting_a.mp4` | IS018 | 1 |
| — | ✅ | `boardroom_blackboard_meeting_b.mp4`, `fab_corridor_wide_cleanroom.mp4`, `fab_engineers_furnaces.mp4`, `fab_women_cleanroom_line.mp4` | reserve / IS032 cut-in / IS065 alt | 0 |
| — | ⚠ | `fab_hk_semiconductor_ltd_sign.mp4` — shows a *Hong Kong* plant sign: **do not use** for UMC/TSMC | — | 0 |
| — | ❌ | `wafer_probe_needles.mp4` unreadable (incomplete download) | — | — |
(Gatherer B: log the archive.org source of these clips — 1960s colour film — in `assets/intro/footage/SOURCES.md`.)

## 7. Maps
| ID | status | path | scenes |
|---|---|---|---|
| E09/E10 | ✅ | `assets/intro/maps/taiwan_relief_grey.jpg` (+json) + `taiwan_mask.png`, `taiwan_land_mask_all.png` | IS002 panel, IS035, IS049 (behind FC3), IS053 |
| E30 | ✅ | `assets/intro/maps/formosa_1943_japanese_aviation_map.jpg` (+json) | IS006 close-up (D10) |
| E31 | ✅ | `assets/intro/maps/pacific_relief_grey.jpg` (+json), `pacific_basemap(_desat).jpg`, `pacific_land_mask.png` | IS006 pull-out, IS028 |
| E32 | ✅ | `assets/intro/maps/hsinchu_shinchiku_1945_us_army_city_plan.jpg` | IS038 (D09) — needs UMC/new-site pixel positions (gatherer C) |
| E33 | ✅ | `assets/intro/maps/hsinchu_s2cloudless2016.jpg` (+json, EOX CC BY 4.0 → credit) | IS053 (D14) |
| E34 | ✅ | `assets/intro/maps/hsinchu_park_osm_z16.jpg` (+json, ODbL → credit) | IS053 park outline / plot tracing |
| E11 | ✅ | `assets/intro/maps/world_basemap_desat.jpg` (+json) + `world_countries.svg` | IS016, IS025 ghost, IS039 ghost, IS048 (beige grade), IS055–056 |
| E12 | ✅ | `assets/maps/us_beige.svg` | IS024 US circle |
| E13 | ✅ | `assets/maps/clouds/` | IS031 |

## 8. Screens (TVs) — §10.1.7
| ID | status | need | scenes |
|---|---|---|---|
| N24a | ❌ | **Tatung** colour TV (1970s–80s) photo, screen keyed transparent + `_screen.json` | IS060 |
| N24b | ❌ | **Sony Trinitron** (1970s–80s) photo, screen keyed + `_screen.json` | IS065 |
Sources: Commons "Tatung television", "Sony Trinitron KV-"; never the four museum TVs of the 10-min edit.

## 9. Face cam (gitignored, regenerable)
| ID | status | file | scene | insert |
|---|---|---|---|---|
| N32a | ✅ | `assets/facecam/fc_170.5.mp4` + `_fg.webm` + `_bg.webm` | IS041 | 1 (cut-out) |
| N32b | ✅ | `assets/facecam/fc_195.8.mp4` + `_fg.webm` + `_bg.webm` | IS046 | 2 (cut-out) |
| N32c | ❌ | **new pre-cut `fc_206.5.mp4` (206.5–210.0) + fg/bg** (`remove-background … -o fg.webm -b bg.webm`) | IS049 | 3 (cut-out) |
| N32d | ✅ | `assets/facecam/fc_245.8.mp4` (cut-out in progress — not needed: clean insert) | IS057 | 4 (clean) |
| N32e | ❌ | `fc_251.0.mp4` ✅ → needs `_fg.webm` + `_bg.webm` | IS059 | 5 (cut-out) |
| N32f | ✅ | `fc_256.0.mp4` + `fc_261.5.mp4` (or `input/Face Cam.mp4` @ media 259.194) | IS061 | 6 (clean) |

## 10. Graphics to make (🛠, no sourcing)
N37 product icons SVG (telephone, TV, calculator, computer, watch, game console) — IS012, IS013, IS039 · plane icon SVG —
IS028 · N39 film strip of intro stills (from our own snapshots after build) — IS058 · N43 colour-bar card — IS060 ·
FOUNDER & CEO frosted-glass nameplate — IS041 · YES / RECORD / BETRAYAL stamps (rough type in our fonts) — IS010, IS022,
IS044 · Silicon-Valley stamp icon (from N27a) — IS055.

## 11. Biggest gaps (priority order)
1. **UMC + TSMC logos** (N03, N04) — on screen 6×. 2. **Two more Robert Tsao photos** (N02a/b). 3. **Tatung + Trinitron
TVs** (N24a/b). 4. **fc_206.5 pre-cut + fc_251.0 cut-out** (N32c/e). 5. **Telephone cut-out** (N09) and the **manual /
datasheet / dictionary** pages (N11a/b, N12). 6. **Paintings/posters**: Sisyphus, NY poster, pictorial Silicon Valley map,
radio ad, sweat cartoon (N13, N22, N27a, N28, N29). 7. Taipei skyline ≥ 3000 px for 2.5D (N25). 8. Blue Marble globe,
groundbreaking, stone wall, old book, menu (N07, N18, N16, N34, N23).
