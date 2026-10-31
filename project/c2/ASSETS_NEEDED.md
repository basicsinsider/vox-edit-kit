# ASSETS NEEDED — CHUNK c2 (local 0.00–597.86)

Deduplicated list for `EDIT_NOTES.md` (IDs `E..` = exists, `K..` = map kit, `N..` = still needed / to make). Snapshot of the
folders taken 2026-10-31 — **gatherers: flip ❌ → ✅/🔁 with the path when you land a file**, log every file in its folder's
`SOURCES.md` (subject, URL, licence or "© owner, fair use", author, date, size; bboxes for documents). New files go to
`assets/c2/<type>/` (photos, footage, documents, paintings, logos, maps, cutouts, layers, derived).

Rules (§10.9 long-form): **copyrighted material allowed** (fair use: documentary commentary, transformed with our treatments,
credited) — prefer the TRUE image (the real people, buildings, documents, period ads, press photos). Never log in, never
pay, never strip watermarks (find a clean copy elsewhere instead). Look at every file; reject wrong subject/era, < 1600 px
long side for full-frame (≥ 3000 px for 2.5D). Reuse is allowed but prefer unique images ("uses" column = plan).
Full-frame paper grounds only from `_hires` files. Maps: map kit (`assets/maps/kit/`) for modern/satellite/world views;
real period maps for close-ups.

**Gatherer c2 pass 2026-10-31:** statuses below updated; full list + what's missing in `assets/c2/ASSETS.md`.

Legend: ✅ exists · 🔁 re-download (listed in `example-docs/sources/`) or substitute · ❌ to find · 🛠 to make.

**Best sources for this chunk (in order):** Computer History Museum (computerhistory.org — "Revolution" exhibit pages and
catalog images: Shockley lab, Traitorous Eight, Fairchild, Noyce, Micrologic) · Stanford Libraries (Stanford Historical Photograph
Collection, SearchWorks/purl.stanford.edu, Stanford Daily archive, Stanford Research Park history page) · Palo Alto Historical
Association · Wikimedia Commons (`find_media.py commons-html`) · archive.org (Prelinger, Universal Newsreels, "Electronics"
magazine runs, RCA tube manuals) · worldradiohistory.com (Electronics, Bell Laboratories Record, Radio-Electronics — period ads &
articles) · bitsavers.org (databooks, schematics) · Google Patents (PD patent drawings) · Google Books (LIFE magazine full run;
Fortune via archive.org) · nobelprize.org (laureate photos) · Intel newsroom/museum (Noyce) · NARA / US Navy / USAF (missiles,
PD) · USGS topoView / ngmdb (historical quads, PD) · NASA (Black Marble, PD) · LOC image servers (tile.loc.gov).
YouTube/Vimeo footage (AT&T Archives, HP/Varian corporate films, CHM lectures) → `requests/fetch.json` (fetch relay, §8.2).

## 1. People
| ID | status | path / need | scenes | uses | sources / notes |
|---|---|---|---|---|---|
| E41 | ✅ | `assets/archival/collage/terman_frederick_1955.jpg` (960×936, PD) | S010 card, S012 circle, S043 circle | 3 | card/circle size only (≤ native) |
| N06 | 🔁 `assets/c2/cutouts/terman_1955_cut.png` (cut from E41, 960 px — no larger copy reachable) | Frederick Terman portrait 1950s, ≥ 1600 px, clean bg → cut-out 🛠 | S054 Vox cut-out, S063 | 2 | Stanford News Service / Stanford Historical Photograph Collection; Commons "Frederick Terman"; IEEE History Center (ETHW, CC) |
| N09 | ✅ `assets/c2/photos/bardeen_shockley_brattain_1948.jpg` (1920) | Bell Labs 1948 publicity photo: Bardeen, Shockley (seated at microscope), Brattain, ≥ 2400 px | S015, crops S047 | 2 | Commons "Bardeen Shockley Brattain 1948.JPG"; AT&T/Nokia Bell Labs © fair use |
| N33 | ✅ `assets/c2/photos/shockley_portrait.jpg` (2317) + `cutouts/shockley_portrait_cut.png` | William Shockley portrait c.1956 (Nobel) ≥ 1600 px | S046 | 1 | nobelprize.org; Commons |
| N62 | ✅ `assets/c2/photos/shockley_stanford_painter.jpg` (+ `shockley_1959_lecture.jpg`, `shockley_blackboard_transistor.jpg`) | second Shockley portrait (different photo; 1950s–70s) | S091 | 1 | Commons "William Shockley, Stanford University" (Chuck Painter / Stanford News Service, CC); CHM |
| N35m | ❌ | Shockley's mother (May Bradford Shockley) photo — **name never printed** | S049 | 1 | Stanford Special Collections (Shockley papers), Joel Shurkin's *Broken Genius* plates, findagrave; fallback: an empty frame + Palo Alto postcard only |
| N60 | 🔁 `assets/c2/photos/chm_shockley_nobel_toast_1956.jpg` (800 px only) | Shockley Semiconductor team toasting Shockley's Nobel, Nov 1956 | S089 | 1 | CHM catalog; Intel; widely reproduced press photo (fair use) |
| N65 | 🔁 `assets/c2/photos/fairchild_eight_lobby_1960_wmiller_millersville.jpg` + `chm_fairchild_eight_lobby_1960_wmiller.jpg` (800 px max — no free hi-res) | **Traitorous Eight** group portrait, 1960, Wayne Miller (Magnum) ≥ 3000 px → 🛠 2.5D layer set (backdrop, 3 depth layers, `layout.json`) + 8 circle crops (N64) | S093–094 circles, S095 2.5D, S099 focal | 3 | © Magnum Photos — fair use with credit; CHM / Intel press reprints; never a watermarked copy |
| N69 | 🔁 `assets/c2/photos/noyce_1959_motherboard.png` (640) + `chm_noyce_fairchild_gm_1962.jpg` (800) + `cutouts/noyce_1959_cut.png` | Robert Noyce portrait c.1959–60 (Fairchild era) ≥ 1600 px | S099, S100 card | 2 | Intel Museum / CHM / Commons "Robert Noyce" |
| N40 | 🔁 `assets/c2/paintings/leland_stanford_p1070023.jpg` (595x800 only) | Meissonier, *Leland Stanford* (1881, oil, Cantor Arts Center) ≥ 2400 px | S056 | 1 | Commons (PD-Art) |
| E44 | ✅ `assets/c2/photos/leland_stanford_watkins_1874.jpg` | Leland Stanford Watkins portrait 1874 (alt for S056) | S056 alt | 0–1 | example-docs/sources/assets_archival.md (Commons 3840 px) |
| N47 | ❌ | 1950s Stanford engineering classroom / lecture photo | S069 | 1 | Stanford Historical Photograph Collection; Stanford Daily archive |
| N48 | ❌ | Stanford EE / Electronics Research Lab faculty group photo, 1950s | S072, S074 crop, S079 crop | 3 | Stanford Archives; ETHW |
| N11 | 🛠 | engineer pictogram SVG (ink, hard-hat/drafting) | S018 | graphic | adapt `assets/icons/graduate*.svg` |
| N64 | 🛠 | 8 portrait circles from N65 | S093–094 | graphic | |

## 2. Logos
| ID | status | need | scenes | notes |
|---|---|---|---|---|
| E42 | ✅ | `assets/logos/bell_system_1921.png` (+ `att_bell_1921_1939.png`) | S035, S047 | navy tint |
| E48 | ✅ | `assets/archival/brain_drain/ge_logo_bone.svg` (bone); `ge_logo.svg` 🔁 | S076 | |
| N51 | 🔁 period 'hp' logo only on `assets/c2/documents/hp_annual_report_1958_cover_hp_logo.jpg` / `_1959_cover.jpg` (redraw) | HP logo, 1950s style ("hp" in circle) | S076 | `npx --yes hyperframes@0.8.217 media-use resolve --type logo --entity "Hewlett-Packard" --project .`; Commons |
| N53 | ❌ | Lockheed logo (1950s–60s) | S077 | same tool; Commons |
| N54 | 🔁 modern `assets/c2/logos/varian_logo.png` only | Varian Associates logo + 1953 Varian building photo (first Industrial Park tenant) | S077 | Varian/Stanford Research Park history; CHM |
| N66 | 🔁 modern `assets/c2/logos/fairchild_semiconductor_logo.png` only (period Flying-F visible in lobby photo) | Fairchild Semiconductor logo (1957–70s) | S096, S098 | `media-use resolve`; Commons "Fairchild Semiconductor logo" |
| — | — | **no logo of Fairchild's acquirer** (unnamed in VO) | — | |

## 3. Places, buildings, aerials
| ID | status | path / need | scenes | uses | notes |
|---|---|---|---|---|---|
| E40 | ✅ | `assets/archival/hoover/stanford_main_quad_panorama_c1896.jpg` (+ `_b`) | S001, S054 panel | 2 | c1→c2 hand-off image (align with c1) |
| N07 | ❌ | Stanford campus aerial 1940s–50s ≥ 2400 px | S011 | 1 | Stanford Archives; Fairchild Aerial Surveys via UCSB FrameFinder (view only) — Commons "Stanford University aerial 19xx" |
| E45 | 🔁 | Stanford oval/main quad aerial 2007 (`assets/archival/modern/…`, re-download) | S059 alt | 0–1 | prefer K06 satellite |
| N43 | 🔁 partial: `assets/c2/photos/hp_stanford_industrial_park_plant_rendering_1959.jpg` (aerial rendering) + `hp_stanford_industrial_park_plant_exterior_1958.jpg` — no 1950s aerial photo reachable | **Stanford Industrial Park aerial, 1950s–early 60s** ≥ 3000 px → 🛠 2.5D layers | S065 2.5D, S079 crop | 2 | Stanford Research Park "History" page, Stanford Archives, Palo Alto Historical Assoc., HP archives (HP 1960 Page Mill site aerial) — the chunk's 2.5D hero; if only ≤ 2000 px exists, use a 2-layer (sky + land) version |
| N50 | ❌ | Stanford Industrial Park plan / plat map (1950s–60s parcels) | S076, S078 | 2 | Stanford Archives / Palo Alto city records; fallback 🛠 typeset plat on paper_blueprint traced from the park's parcel outline (OSM) — no fake seals |
| N37 | ✅ `assets/c2/photos/chm_shockley_lab_mountain_view_c1960.jpg` (800) + `shockley_bldg.jpg`, `shockley_semiconductor_lab_1956.jpg` | Shockley Semiconductor Laboratory building, 391 San Antonio Rd (1950s photo) or the site/plaque (Commons CC) | S050, S088 | 2 | CHM; Commons "Shockley Semiconductor Laboratory" |
| N67 | ✅ `assets/c2/photos/fairchild_bldg_844_charleston.jpg` (907) + `chm_plaque_844_charleston_ic.jpg` | Fairchild Semiconductor's first building, 844 Charleston Rd (1958) | S096 | 1 | CHM; Fairchild history; Commons (historic marker photo) |
| N36 | ❌ | 1950s Palo Alto colour postcard (University Avenue) | S049 | 1 | archive.org / eBay-free scans / Palo Alto Hist. Assoc. (fair use) |
| N81 | ❌ | Santa Clara Valley aerial 1960s–70s (orchards + fabs) | S127–128 | 1 | CHM; San José Public Library California Room; else E57 |
| E57 | ✅ | `assets/intro/photos/silicon_valley_2014.jpg` (CC BY-SA 3.0, credit) | S127–128 alt | 0–1 | |
| E49 | ✅ | `assets/archival/hp/hewlett_and_packard_together_1960.jpg` (2584×2090) | S079 circle | 1 | |
| N08 | ✅ `assets/c2/paintings/us_capitol_engraving_sartain.jpg` (1280; LOC original 9875) | US Capitol 19th-c. engraving (PD) | S012 | 1 | LOC / Commons |

## 4. Objects, technology (photos)
| ID | status | need | scenes | uses | sources / notes |
|---|---|---|---|---|---|
| N05 | ✅ `assets/c2/objects/polysilicon_rod.jpg` + `cutouts/polysilicon_rod_cut.png` | lump of polycrystalline silicon, clean bg → cut-out 🛠 | S008, S009 card, S119–120 card | 3 | Commons "SiliconCroda.jpg" (CC), "Polycrystalline silicon rod" |
| N10 | ✅ `assets/c2/photos/chm_point_contact_transistor_1947.jpg`, `replica_first_transistor_b.jpg`, `documents/us2524035_*`, `chm_shockley_notebook_1948_junction.jpg` | Dec 1947 Bell Labs lab-notebook page (Brattain) or point-contact transistor replica photo | S016–017 | 1 | Commons "Replica-of-first-transistor.jpg" (PD), CHM; fallback US Patent 2,524,035 drawing (PD) |
| N12 | 🔁 `assets/c2/objects/ck722.jpg` (needs polygon cut-out) · `transistors_white.jpg` is modern | early transistor (Western Electric / Raytheon CK722 / TI 2N) clean cut-out 🛠 | S019, S023, S032, S081, S109 | 5 (motif) | Commons "Transistors-white.jpg", CK722 photos (CC) |
| N15 | ✅ `assets/c2/objects/eniac_tubes_row.jpg`, `early_triode_vacuum_tubes.jpg` | row of vacuum tubes on dark bg (+ one large tube cut-out) | S023, S031 | 2 | Commons "Vacuum tubes" (CC) |
| N20 | ❌ | ENIAC photo (US Army, PD) ≥ 2400 px | S027 | 1 | Commons "Eniac.jpg", "Classic shot of the ENIAC" |
| N18 | ✅ `assets/c2/photos/eniac_changing_a_tube.jpg` (1239) | "replacing a bad tube" ENIAC photo (US Army, PD) | S025 card | 1 | Commons |
| N21 | ✅ `assets/c2/photos/chm_bell_labs_tradic_felker_harris.jpg` (800) | TRADIC (Bell Labs 1954, first transistorised computer) or IBM 7090 | S028 | 1 | Commons "TRADIC computer.jpg" (USAF PD); IBM archives |
| N22 | ❌ | 1950s glass soda bottle, clean cut-out | S031 | 1 | Commons (CC) |
| N23 | ❌ | 1950s US coin (quarter/dime) | S032 | 1 | US coins PD (Commons / US Mint) |
| N24 | ✅ `assets/c2/objects/nobel_medal_fleming_1945.jpg` + `derived/c2s02/nobel_medal_cut.png` (c2s02) | Nobel Prize medal (obverse) ≥ 2000 px | S034, S046 | 2 | Commons "Nobel Prize medal" (CC) |
| N26 | 🔁 `assets/c2/objects/we_model_500_telephone.jpg` (needs polygon cut-out) | Western Electric 500 desk telephone (1950s) cut-out | S035 | 1 | Commons (CC) |
| N30 | ✅ `assets/c2/objects/regency_tr1_b.jpg` + `photos/chm_regency_tr1_red.jpg` | Regency TR-1 transistor radio photo cut-out | S040 | 1 | Commons "Regency TR-1" (CC) |
| N49 | ✅ `assets/c2/objects/klystron_prototype_cutaway.jpg`, `klystron_oscillator_1944.jpg` (small) | klystron (Varian brothers / Stanford) photo | S073 | 1 | Commons "Klystron", Stanford/SLAC history (fair use) |
| N70 | ✅ `assets/c2/photos/chm_micrologic_dime_life_1961.jpg`, `chm_micrologic_presentation_block.jpg`, `chm_2n1613_planar_transistor_micrograph.jpg` | Fairchild Micrologic / planar IC die photo | S102, S109, S113 circle | 3 | Commons "Fairchild µL914", CHM "first planar IC" |
| N73 | ❌ | modern chips on a board, macro (CC) | S108 | 1 | Commons |
| N74 | 🔁 `assets/c2/objects/intel_4004_layout.jpg` (layout plot, 2782) | high-res die shot (Intel 4004 or similar) ≥ 4000 px | S112, S128 | 2 | Commons (CC BY) — credit |
| E54 | ✅ | `assets/intro/photos/ibm5150_board_1984_cc0.jpg` (CC0) | S111 | 1 | use the full 6300 px original if re-downloaded |
| N80 | ✅ `assets/c2/objects/quartz_tibet.jpg` | quartz crystal photo (CC) | S125 | 1 | Commons |
| N04a–d | ❌ | four field photos: electronics (1940s–50s vacuum-tube/klystron lab), radio science (radio antenna/ionosphere sounder), materials research (crystal growth / metallurgy microscope), solid-state physics (lattice engraving/plate) | S007 cards | 1 each | Stanford Archives, NIST/NBS (PD), Commons; lattice: 1950s textbook plate or 🛠 own SVG |
| N02 | 🔁 Jack only: `assets/c2/objects/playing_card_jack_spades_19c.jpg` (CC0) | 19th-c. Jack + Ace playing cards (PD deck scan) | S005–006 | 1 | Commons "Playing cards 1880s", Rijksmuseum (CC0) |
| N75 | 🔁 Watt only: `assets/c2/paintings/watt_steam_engine_1782_engraving.jpg` | PD engravings: Gutenberg press, Watt steam engine, Edison bulb, Bell telephone | S113–114 circles | 1 each | Commons / LOC (PD) |

## 5. Documents, ads, manuals, patents, magazines
| ID | status | need | scenes | uses | sources / notes |
|---|---|---|---|---|---|
| N01 | 🔁 `assets/c2/paintings/feininger_gelmeroda_iv_1915.jpg` (1024) / `_viii_1921.jpg` (672) | Lyonel Feininger, *Gelmeroda IV* (1915) or *VIII* (1921) colour painting ≥ 2400 px | S004 painting-to-print | 1 | Commons (PD in US — pre-1929); Guggenheim/Whitney collection pages (fair use) |
| 🛠 | 🛠 | campus-newspaper column recreation (Crimson Pro/Haskoy, sepia, halftone; **no real masthead**) | S004 | — | typeset |
| N13 | ❌ | 1950s home light-switch ad showing a bedroom (GE / Leviton / Bryant / Pass & Seymour) | S020 | 1 | LIFE / Saturday Evening Post via Google Books & archive.org (fair use) |
| N17 | ❌ | RCA Receiving Tube Manual (1950s) page with a tube diagram | S025 | 1 | archive.org "RCA receiving tube manual RC-16/RC-19" (≤ native size as card) |
| N25 | ❌ | 1950s Bell System / Bell Labs ad about the transistor & telephones | S035 | 1 | LIFE / Scientific American via Google Books; worldradiohistory.com Bell Laboratories Record (fair use) |
| N28 | ❌ | Fortune, March 1953 "The Year of the Transistor" spread/cover (or LIFE transistor feature) ≥ 2400 px | S038 | 1 | archive.org Fortune runs; Google Books LIFE (fair use) |
| N31 | ❌ | 2–3 1950s transistor-radio ads with people (Regency, Zenith Royal, Sony TR-63) | S040 panels | 1 | worldradiohistory.com, Google Books LIFE (fair use) |
| N32 | ❌ | 1940s–50s federal research contract with Stanford (ONR N6onr-251 / Signal Corps) cover page | S045 | 1 | Stanford Archives, DTIC; fallback 🛠 typeset "CONTRACT" form (no fake seals/signatures) |
| N42 | ✅ `assets/c2/documents/stanford_founding_grant_1885_{p10_heading,p11_land_clause,title}.jpg` (bboxes in SOURCES) | Stanford **Founding Grant 1885** pages (heading + a clause page) | S061–062, S063 panel | 3 | `example-docs/sources/assets_archival_documents.md` (stanford_founding_grant_1885_heading_page.jpg / title page) — re-download; archive.org |
| N45 | ❌ (optional) | a real Stanford ground-lease page (1950s) | S067 | 0–1 | Stanford Archives; else 🛠 typeset lease form |
| N55 | ✅ `assets/c2/documents/edn_jul1961_micrologic_logic_schematics_p2.jpg` | 1950s computer logic schematic (IBM/RCA manual) | S082 underlay | 1 | bitsavers.org |
| N59 | 🔁 `assets/c2/photos/chm_minuteman_guidance_computer_detail.jpg` (not a cutaway) | 1950s–60s missile cutaway / technical illustration (Atlas, Minuteman) | S086–087 | 1 | USAF / NASM (PD), archive.org manuals; else 🛠 own line drawing |
| N61 | ✅ `assets/c2/documents/shockley_4layer_diode_brochure_p1.jpg`, `_b_p2.jpg` (brochure, not an Electronics ad) + `logos/shockley_transistor_logo.png` | Shockley Transistor Corp. 4-layer-diode ad, *Electronics* 1958–60 | S090 | 1 | worldradiohistory.com (fair use) |
| N71 | ✅ `assets/c2/documents/us2981877_noyce_sheet{1,2,3}.png` (2320x3408 USPTO) + text p1 | Noyce's planar IC patent US 2,981,877 drawing sheet ≥ 3000 px | S103–104 | 1 | Google Patents (PD) |
| N72 | ✅ `assets/c2/documents/fairchild_epitaxial_micrologic_1963_{cover,p9_dies}.jpg`, `edn_jul1961_micrologic_elements_p1.jpg` | 1960s Fairchild Micrologic / IC databook page | S106 | 1 | bitsavers.org/components/fairchild (fair use) |
| N77 | ❌ | 1950s periodic table wall chart (Welch/Sargent) | S120 | 1 | archive.org / Commons; else 🛠 typeset Si cell |
| N78 | ✅ `assets/c2/documents/punch_card_80col.jpg` (3080) | IBM 80-column punched card scan ≥ 3000 px | S124 | 1 | Commons "Punched card" (PD/CC) |
| E46 | ✅ | `assets/intro/papers/ledger_specimen_p318.jpg` | S064 card | 1 | ≤ native size |

## 6. Paintings / illustrations (§10.5)
| ID | status | need | scenes | notes |
|---|---|---|---|---|
| N01 | ❌ | Feininger *Gelmeroda* (see §5) | S004 | |
| N40 | ❌ | Meissonier *Leland Stanford* | S056 | |
| N63 | ✅ `assets/c2/paintings/fuseli_the_nightmare_1781.jpg` (1920) | Henry Fuseli, *The Nightmare* (1781, Detroit Institute of Arts) ≥ 2400 px | S092 | Commons PD-Art |
| E47 | ✅ | `assets/intro/paintings/stanford_peninsula_map.jpg` (red pictorial Peninsula map, 1920×2556) | S066 | card crop ≤ native |
| N44 | ❌ (optional) | "Palo Alto — birthplace of Silicon Valley" pictorial map (Krish's example) | S066 alt | ask Krish for the file/link |

## 7. Footage
| ID | status | need | scenes | uses | sources / notes |
|---|---|---|---|---|---|
| E50 | ✅ | `assets/intro/footage/wafer_closeup_purple.mp4` (Fairchild reel, Prelinger) | S101, S126 still (wafer SVG source) | 2 | |
| E51 | ✅ | `assets/intro/footage/fab_microscope_closeup.mp4` | S105 | 1 | |
| E52 | ✅ | `assets/intro/footage/wafer_probe_needles.mp4` | S110 | 1 | |
| E53 | ✅ | `assets/intro/footage/oscilloscope_fairchild_square_wave.mp4` | S110 cut-in, S123 | 2 | |
| E56 | ✅ | `assets/intro/footage/ibm_punch_cards_reader.mp4` | S124 inset (optional) | 0–1 | |
| N14 | ❌ | hand flipping a wall light switch, 1950s–60s | S021 | 1 | Prelinger (home electrification / "Leave It to Roll-Oh"-type films) |
| N16 | ✅ `assets/c2/footage/ge_schenectady_1923_edison_langmuir_vacuum_tube.mp4` | `ge_schenectady_1923_edison_langmuir_vacuum_tube.mp4` (giant tube) | S024 | 1 | example-docs/sources/assets_archival_footage.md — re-download; alt ENIAC racks still |
| N19 | ✅ `assets/c2/footage/erpi1943_vacuum_tube_filament_glow.mp4` + `bell_transistor1953_tube_filament_anim.mp4` (SD) | macro of a glowing vacuum-tube filament ≥ 1080p | S026 | 1 | Pexels/Pixabay (free licence), Commons video |
| N27 | ✅ `assets/c2/footage/bell_transistor1953_switching_office_technicians.mp4` (SD) | 1950s long-distance switchboard / AT&T Long Lines footage | S036 inset | 0–1 | Prelinger AT&T films; AT&T Archives (YouTube → fetch relay) |
| N46 | ✅ `assets/c2/footage/bell_transistor1953_engineers_at_benches.mp4` (SD) | 1950s electronics lab, engineers at benches (HP/Varian/GE corporate or generic) | S068 (+ S088 still) | 2 | Prelinger; HP/Varian films on YouTube → fetch relay |
| N52 | ❌ | Polaris missile launch (Lockheed Missiles & Space Division), US Navy | S077 | 1 | archive.org / NARA (PD) |
| N56 | 🔁 `assets/c2/footage/bell_transistor1953_hands_assembling.mp4` (transistor assembly, not soldering) + `photos/hp_1958_subassembly_line_wiring.jpg` | 1950s–60s hand soldering / point-to-point wiring of computers or missile electronics — 2 shots | S084, S102 still | 2 | Prelinger, NARA, IBM films; contact sheet first |
| N58 | ✅ `assets/c2/footage/un1958_atlas_{on_pad_cape_canaveral,night_launch,blockhouse_engineers}.mp4` (PD newsreel) | missile launch newsreel (Atlas / Thor / Minuteman, USAF) | S085 (inside TV) | 1 | archive.org Universal Newsreels (PD) |
| N79 | ❌ | macro sand pouring | S125 | 1 | Pexels/Pixabay/Commons |

## 8. Screens
| ID | status | need | scenes | notes |
|---|---|---|---|---|
| E55 | ✅ | `assets/intro/screens/tektronix_475a_scope_frame.png` + `_screen.json` | S123 | not used in the intro |
| N57 | ✅ `assets/c2/derived/c2s02/tv_rca_1950s_keyed.png` + `_screen.json` (c2s02) | 1950s TV set (RCA / Zenith / Admiral table or console) photo, screen keyed transparent + `*_screen.json` | S085 | Commons (CC), museum photos; **not** the intro's Tatung/Trinitron or the 10-min edit's museum TVs |

## 9. Maps
| ID | status | need | scenes | notes |
|---|---|---|---|---|
| K01 | ❌ (map kit) | US East Coast satellite/relief (NJ close-up), lon/lat→px json | S014 | `assets/maps/kit/` — map-kit agent; Esri World Imagery class (credit) |
| K02 | ❌ (map kit) | US basemap night/relief (ghost-able), json | S036–037, S043 | Natural Earth II 21600 px class |
| K03 | ❌ (map kit) | world basemap, dark (night-lights or NE II) | S042 | |
| K04 | ❌ (map kit) | Bay Area / Peninsula satellite | S053 | Esri/Google-style imagery, credit |
| K05 | ❌ (map kit) | Bay Area vintage-atlas style with SF city outline | S058 | |
| K06 | ❌ (map kit) | Stanford lands satellite close-up | S059–060 | |
| N76 | ❌ | NASA Black Marble globe (PD) | S115 | NASA Visible Earth |
| E43 | ✅ | `assets/maps/old/usgs_palo_alto_1899_topo.jpg` (+json, + `_grey`) | S051–052, S057 | era older than the story — prefer N38 for S051–052 |
| N38 | ✅ `assets/c2/maps/usgs_palo_alto_1953_24k.jpg` + json (also `usgs_palo_alto_1948_62k`) | USGS Palo Alto 1953 (or 1940s) 7.5'/15' quad (PD) + json | S051–052, S057 | USGS topoView / ngmdb |
| N68 | ✅ `assets/c2/maps/usgs_palo_alto_1961_24k.jpg`, `usgs_mountain_view_1961_24k.jpg` + json | USGS 1961 Mountain View / Palo Alto 7.5' quad (PD) ≥ 4000 px + json | S097 | topoView |
| N34 | ❌ | 1950s colour US road map (Esso / Rand McNally / Shell) ≥ 4000 px | S048 | archive.org, David Rumsey (licence check — CC BY-NC is NOT ok unless fair-use path chosen; prefer archive.org/LOC) |
| N39 | ✅ `assets/c2/maps/usgs_palo_alto_1948_62k.jpg` + json | USGS/land survey sheet (PD) | S054 panel | |
| N41 | 🛠 | Stanford lands (8,000-acre) outline SVG, traced onto N38/E43 pixel space | S057, S060 | trace from Stanford's published land map (fair use reference) |

## 10. Graphics to make (🛠, editors or gatherer C)
Crystal lattice SVG + dopant atoms (S008, S122) · switch schematic (S019, S082) · 1950s electronics icon set N29 (S039) ·
trade icons N03 (S005) · engineer pictogram N11 · building pictograms (S078) · wafer disc SVG (S126) · transistor pictogram
(S083) · red paper clip PNG (S010) · tear-off calendar (S096) · lease form, contract fallback, planner (S067, S045, S074) ·
unlit/lit SILICON VALLEY outline letters (S080/S127) · "problem" card PNG export (S087→S088) · hour-meter odometer (S025).

## 11. Papers / textures (all ✅)
`assets/textures/paper_{graph,lined,stained,torn,blueprint}_01*_hires.jpg`, `paper_cream_01`, K+E `_norm_hires` grids in
`assets/intro/papers/` (10×10 black, cover grid blue, cross-section green, mm grid green, log grid green, progress chart
orange). Assignment per scene in EDIT_NOTES; never the same file in consecutive scenes.

## 12. Biggest gaps (gatherers: do these first)
1. **N43 Stanford Industrial Park aerial (1950s)** — 2.5D hero of the chunk.
2. **N65 Traitorous Eight photo** (clean, high-res) + N60 Shockley team toast + N69 Noyce — the act VI/VII faces.
3. **N09 Bell Labs trio 1948** + N33/N62 Shockley portraits.
4. **Footage**: N56 hand soldering, N46 1950s lab, N52/N58 missiles, N14 switch, N19 glowing tube.
5. **Documents**: N71 Noyce patent, N42 Founding Grant (re-download), N28 Fortune 1953, N61 Shockley ad, N17 tube manual.
6. **Maps**: map-kit K01–K06 (depends on the map-kit agent) + USGS quads N38/N68 + 1950s road map N34.
7. **N57** 1950s TV with keyed screen.
