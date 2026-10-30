# ASSETS NEEDED — full 10-minute edit

Deduplicated sourcing list for `EDIT_NOTES.md` (IDs `A01…` are referenced there). Each folder gets a `SOURCES.md`
entry per file: subject, source URL, direct file URL, licence/author, date, saved dimensions (same format as
`assets/archival/SOURCES.md`).

**Rules for every asset agent**
- Licence: **public domain / CC0** preferred; **CC BY / CC BY-SA** allowed with attribution (add a credit line to
  SOURCES.md and an on-screen micro-credit in the scene, like s02). No "editorial use only", no stock watermarks, no NC/ND.
- US works published before 1931 are PD in the US (as of 2026). US federal works (NARA, NASA, USGS, War Dept.) are PD.
- Wikimedia: download thumbnails with `tools/commons_thumb.sh "File name.jpg" out.jpg 1920` (or 3840) — originals return 429.
  archive.org works (use `/download/<id>/…` or the jp2 zip leaf); LOC/Chronicling America were blocked (403/503) — try once,
  then fall back to the Commons copy of the same LOC item.
- Resolution: full-frame plates ≥ 1920 px wide (≥ 2400 px if the scene zooms > 1.2×; ≥ 3000 px for 2.5D layer sources);
  cards/cutouts ≥ 1200 px on the long side; footage ≥ 480p is acceptable for TV screens / weave scenes (it gets degraded anyway),
  ≥ 720p for full-frame.
- Save to the listed folder with descriptive snake_case names; never overwrite approved sample assets.
- Every scene also uses the default texture stack (exists) — nothing to source for that.

Legend: ✅ exists (path) · 🔎 must be found · 🛠 must be made (from existing or found material).

---

## 1. Archival photos

| ID | status | scenes | subject / era | preferred free sources | licence | min res | save to |
|---|---|---|---|---|---|---|---|
| A01 | ✅ | SC002, SC011 | Modern aerial of Silicon Valley / Santa Clara Valley (San Jose–Mountain View), ideally dusk, wide | Commons "Silicon Valley aerial", "Santa Clara Valley aerial"; NASA ISS photo of SF Bay Area at night (PD) as alternate | CC BY(-SA) / PD | 2400 w | assets/archival/modern/ → `modern/silicon_valley_south_to_san_jose_2014.jpg` (3840w, daytime haze, not dusk) + `silicon_valley_aerial_2013.jpg` (1920w) — CC BY-SA credit |
| A02 | ✅ | SC003, SC006 (ghost cutout) | Apple Park aerial (2017+) | Commons "Apple Park" aerial | CC BY-SA | 1920 w | assets/archival/modern/ → `modern/apple_park_aerial_2018.jpg` (3840w) |
| A03 | ✅ | SC003 | NVIDIA HQ (Endeavor/Voyager, Santa Clara) | Commons "NVIDIA headquarters" | CC BY-SA | 1920 w | assets/archival/modern/ → `modern/nvidia_hq_santa_clara_2018.jpg` (1920w) |
| A04 | ✅ | SC003 | Googleplex (Mountain View) and/or Meta "Like" sign, Menlo Park | Commons | CC BY-SA | 1920 w | assets/archival/modern/ → `modern/googleplex_2015.jpg` (1920w) + `meta_hq_like_sign_menlo_park_2022.jpg` (🔁 current Meta sign, 1280w) |
| A05 | ✅ | SC011, SC014 (fallback) | Santa Clara Valley orchards 1900s–1920s ("Valley of Heart's Delight"), blossom rows | Commons (Calisphere/LOC copies), archive.org, San José Public Library on Calisphere if PD | PD | 2400 w | assets/archival/west1920/ → `west1920/santa_clara_prune_orchard.jpg` (hand-coloured slide, blossom, 1920w — below 2400, no larger copy) |
| A06 | 🔁 | SC014 | Empty 1910s–20s Western scene: Palo Alto University Ave or a dirt road with orchards | Commons, Calisphere (PD items), LOC Detroit Publishing photochroms via Commons | PD | 1920 w | assets/archival/west1920/ → no Palo Alto street found; `west1920/santa_clara_prune_orchard_rows_blossom_1904.jpg` (orchard lane, 1460w) or `hoover/stanford_main_entrance_driveway_c1900_lc.jpg` (3840w photochrom) |
| A08 | ✅ | SC018, SC063, SC084 | General Electric Schenectady Works, 1910s–20s (exterior/street view of the works) | Commons "Schenectady General Electric" (LOC Detroit Publishing), archive.org GE Review | PD | 1920 w | assets/archival/companies/ → `companies/ge_schenectady_works_aerial_1896.jpg` (1920w) + `ge_schenectady_works_panorama_1907_lc.jpg` (3840×863 panorama) |
| A08b | ✅ | SC084 | One more Eastern tech employer, 1920s–30s (RCA Camden or Westinghouse East Pittsburgh) | Commons / LOC via Commons | PD | 1920 w | assets/archival/companies/ → `companies/rca_victor_camden_coil_winder_hine_1937.jpg`, `rca_victor_camden_cabinet_assembler_hine_1937.jpg` (1937 interiors), `westinghouse_east_pittsburgh_postcard_c1930.jpg` |
| A09 | ✅ | SC025 | Joseph Swain portrait (c.1890s; Stanford math professor, later Indiana/Swarthmore president) | Commons "Joseph Swain", Indiana Univ. archives (PD scans) | PD | 1200 long side | assets/archival/hoover/ → `hoover/joseph_swain_portrait.jpg` (1280×1938, pre-1913) |
| A10 | ✅ | SC025 | 19th-century Quaker (Friends) meetinghouse engraving or photo | Commons "Friends meeting house" engravings, NYPL Digital Collections PD | PD | 1920 w | assets/archival/hoover/ → `hoover/friends_meeting_house_jordans_engraving_1853.jpg` (1920w) + `friends_meeting_house_haddonfield_1868.jpg` |
| A12 | 🔁 | SC028 | Lou Henry (Hoover) c.1890s–1899, Stanford era | Commons "Lou Henry Hoover" (Hoover Library PD copies) | PD | 1200 long side | assets/archival/hoover/ → no 1890s photo found; `hoover/lou_henry_hoover_1905_harris_ewing.jpg` (c.1905) + `lou_henry_hoover_1922.jpg` |
| A15 | ✅ | SC038 | Rival campuses c.1910s–20s: Caltech (Throop) or Univ. of Chicago; Princeton/Yale fine too | Commons (LOC Detroit Publishing) | PD | 1920 w | assets/archival/campuses/ → `campuses/throop_polytechnic_pasadena_c1900.jpg` (3840w photochrom; pre-1910s) |
| A17 | ✅ | SC040 | Stanford campus 1910s (library, Quad, Memorial Church) | Commons "Stanford University 1910s", LOC photochroms | PD | 1920 w | assets/archival/hoover/ → `hoover/stanford_campus_aerial_c1920_quad1921.jpg`, `stanford_memorial_church_c1920_quad1921.jpg`, `stanford_arcade_c1920_quad1921.jpg`, `stanford_arcade_stairs_c1920_quad1921.jpg` (1921 Quad duotone plates, ~1600–2200px) |
| A18 | ❌ | SC041, SC044 | Early Stanford business school (1925–30s: building, first class, or Stanford Quad yearbook page about it) | archive.org Stanford Quad yearbooks 1926–1929 (PD pre-1931), Commons | PD | 1200 long side | assets/archival/stanford_gsb/ → no 1925–30s GSB image found (Stanford Quad 1926–29 not on archive.org); use typographic card |
| A19 | ✅ | SC044 | Stanford GSB Knight Management Center (modern) | Commons "Knight Management Center" | CC BY-SA | 1920 w | assets/archival/stanford_gsb/ → `stanford_gsb/knight_management_center_2011.jpg` (1920w, CC BY 3.0) |
| A20 | 🔁 | SC019 (cards), SC047 (2.5D) | 1910s–20s Stanford students on the Quad / Palm Drive / arcades — clear foreground figures + architecture, for layer separation | archive.org Stanford Quad yearbooks 1915–1928; Commons; LOC via Commons | PD | **3000 w** | assets/archival/stanford_1920s/ → no 3000w students-on-Quad plate; `stanford_1920s/stanford_medical_students_group_1920_quad1921.jpg` (outdoor student group, 2322w) + campus plates from A17 |
| A21 | ✅ | SC047, SC052, SC065, SC066, SC074 | Young Frederick Terman (1918–1925) | archive.org Stanford Quad 1920/1921/1922 (senior portraits), MIT Technique 1924, IEEE ETHW (check licence) | PD | 900 long side | assets/archival/terman/ — fallback ✅ `assets/archival/collage/terman_frederick_1955.jpg` → `terman/terman_frederick_1920_theta_xi_crop.jpg` (+`_2x`) from labelled Theta Xi group `theta_xi_stanford_1920_group_quad1921.jpg` — small (280×600 native), halftone it |
| A22 | ❌ | SC050 | Lewis M. Terman, better copy (1910s–20s) | archive.org Stanford Quad faculty pages; Commons | PD | 900 long side | assets/archival/terman/ — fallback ✅ `assets/archival/terman/lewis_terman_1923_LOWRES.jpg` (halftone to hide res) → no better copy found — keep fallback lowres (now `cutouts/lewis_terman_ht.png`) |
| A26 | ✅ | SC038, SC057, SC083 | Harvard Yard / Widener Library 1910s–20s | Commons (LOC Detroit Publishing "Harvard") | PD | 1920 w | assets/archival/campuses/ → `campuses/harvard_widener_library_dedication_1915.jpg` (3840w) + `harvard_gate_detroit_c1899.jpg` |
| A30 | ✅ | SC062 (cut-in), SC063, SC069 | GE Schenectady factory/lab interior 1920s; students/apprentices in a plant | Commons, archive.org "General Electric Review" scans, Schenectady Museum (PD items) | PD | 1920 w | assets/archival/companies/ → `companies/ge_research_lab_kellogg_rice_speaker_1925.jpg` (GE Research Lab 1925, 1280w); RCA 1937 interiors (A08b) as factory alt |
| A31 | ✅ | SC034, SC064 | Modern Stanford Main Quad / Hoover Tower aerial | Commons | CC BY-SA | 2400 w | assets/archival/modern/ → `modern/stanford_oval_main_quad_aerial_2007.jpg` (1920w — under 2400) + `stanford_aerial_panorama_2024.jpg` (3840×960) |
| A33 | ✅ | SC069, SC070 | Gothic "ivory tower" campus architecture 1910s–20s (Princeton Holder/Cleveland Tower, Yale Harkness) + an iron gate | Commons (LOC Detroit Publishing) | PD | 1920 w | assets/archival/campuses/ → `campuses/yale_harkness_tower_branford_court_postcard_c1930.jpg` (1920w) + gate `harvard_north_gate_1879_detroit_1910s.jpg` (3840w) |
| A34 | ✅ | SC073 | Raytheon 1920s: BH rectifier tube photo or 1920s Raytheon advert | Commons "Raytheon BH", archive.org radio magazines 1925–28 (Radio News ads) | PD | 1200 long side | assets/archival/terman/ → `terman/raytheon_bh_tube_c1925.jpg` (1280×1791, CC BY-SA 2.0) |
| A38 | ✅ | SC077 | Stanford commencement 1920s–30s (photo or film) | archive.org; Commons; fallback ✅ `assets/archival/footage/berkeley_1932_grad_cut.mp4` (unlabelled, see Q6) | PD | 1920 w / 720p | assets/archival/footage/ — per DECISIONS Q6 reuse berkeley_1932_grad_cut.mp4 (other segment) |
| A40 | ✅ | SC082 | GE Schenectady works aerial or exterior, 1930s | Commons / NARA | PD | 1920 w | assets/archival/companies/ → `companies/ge_schenectady_postcard.jpg` (1930s aerial postcard, 1280w) |
| A41 | ✅ | SC010 | An apple and an orange, isolated (for halftone cutouts) | Commons CC0 / Pexels-on-Commons / Unsplash-equivalent CC0 only | CC0/PD | 1500 long side | assets/cutouts/src/ → `cutouts/src/apple_wet_isolated.jpg` (CC BY 2.0), `orange_closeup.jpg` (CC BY-SA 3.0) — no CC0 found |
| — | ✅ | SC021, SC022, SC025, SC028 | Hoover: young 1898, NARA portrait, Commerce 1923/1924/1928 | `assets/archival/hoover/hoover_young_1898.jpg`, `…presidential_portrait_photo_NARA.jpg`, `…secretary_of_commerce_1923.jpg`, `…_1924_with_hughes.jpg`, `…_1928_informal.jpg` | PD | — | — |
| — | ✅ | SC015, SC019, SC023, SC025, SC045 | Stanford photochroms + Main Quad panoramas c.1896–1905 | `assets/archival/hoover/stanford_*` | PD | — | — |
| — | ✅ | SC036 | Leland Stanford cabinet portrait 1874 | `assets/archival/hoover/leland_stanford_portrait_watkins_1874.jpg` | PD | — | — |
| — | ✅ | SC017→SC018, SC084 | NYC 1921/1929 skylines, Bell Labs West St, Edison West Orange, Jersey City | `assets/archival/brain_drain/*`, `assets/archival/companies/*` | PD / CC BY-SA (Bell Labs bldg) | — | — |
| — | ✅ | SC054, SC056, SC057, SC060 | MIT aerial 1925, MIT main group from Boston, Boston Custom House 1920 | `assets/archival/terman/mit_campus_aerial_1925_great_dome.jpg`, `assets/archival/collage/*`, `assets/archival/companies/massachusetts_boston_custom_house_1920.jpg` | PD | — | — |
| — | ✅ | SC061, SC066, SC068, SC073 | Vannevar Bush 1938, Bush & Compton 1932, differential analyzer | `assets/archival/terman/vannevar_bush_*`, `bush_differential_analyzer_integrator_mit_museum.jpg` | PD / CC0 | — | — |
| — | ✅ | SC080, SC081, SC083, SC086, SC088 | Hewlett c.1962, Packard 1933, H&P 1960, HP garage, HP 200A | `assets/archival/hp/*` | PD / CC BY-SA (garage, 200A) | — | — |
| — | ✅ | SC008 | Eli Lilly HQ photos + 1919 postcard + logo | `assets/maps/eli_lilly_*` | CC BY(-SA) / PD | — | — |

## 2. Newspapers & documents

| ID | status | scenes | subject | preferred sources | licence | min res | save to |
|---|---|---|---|---|---|---|---|
| — | ✅ | SC021 | NYT 7 Nov 1928 front page (headline bbox in SOURCES.md) | `assets/archival/newspapers/nyt_1928-11-07_hoover_wins_frontpage.jpg` | PD | — | — |
| A07 | ✅ | SC016 | 1920s railroad ticket stubs or Southern Pacific "Overland Limited" timetable/ticket | archive.org railroad timetables (PD), Commons ephemera; fallback 🛠 own-made tickets in our fonts + halftone | PD | 1500 w | assets/archival/documents/ — own-made: assets/archival/documents/railroad_ticket_1_made.png (Palo Alto→New York), railroad_ticket_2_made.png (→Boston) |
| A13 | ❌ | SC031 | Stanford Daily (or Daily Palo Alto) clipping 1912–1928 mentioning Hoover as trustee / Board of Trustees | stanforddailyarchives.com (Stanford Daily Archives; pre-1931 issues PD in US), archive.org | PD | 2000 w (page) | assets/archival/newspapers/ — not found: no pre-1931 Stanford Daily/Daily Palo Alto scans on archive.org/Commons in time (stanforddailyarchives.com not tried) — fallback: own-made clipping |
| A14 | ✅ | SC036 | Stanford Founding Grant (1885) — printed/engraved document page with heading | Commons "Founding Grant Stanford", archive.org ("The Founding Grant with amendments", 1887/1916 printings), Stanford facts site scans (check licence) | PD | 2400 h | assets/archival/documents/ — assets/archival/documents/stanford_founding_grant_1885_heading_page.jpg (2008x3433, bbox in SOURCES) + _title_page.jpg |
| A16 | ✅ | SC039, SC092 | Engraved US gold certificates / banknotes 1880s–1930s (front), for halftone cutouts | Commons "United States gold certificate", Smithsonian NNC via Commons | PD (US currency images; use one side, not actual size) | 2000 w | assets/archival/documents/ — assets/archival/documents/gold_certificate_{20,50,100,1000}_1882_*_{front,back}.jpg (~3720 w) |
| — | ✅ | SC049, SC050 | Terman 1916 "The Measurement of Intelligence": title page + IQ distribution chart + classification table (hi-res colour) | `assets/archival/terman/terman_1916_*_HIRES_color.jpg` | PD | — | — |
| A29 | ❌ | SC062 | MIT Bulletin / catalogue page describing Course VI-A (EE co-operative course with General Electric, 1917–) | archive.org "MIT Bulletin" / "Catalogue of the Massachusetts Institute of Technology" 1918–1928; MIT Technology Review 1920s | PD | 2000 h | assets/archival/documents/ — not found: MIT catalogue 1918–28 not located on archive.org search in time |
| A36 | ✅ | SC087, SC091 | Hewlett's thesis title page "A New Type Resistance-Capacity Oscillator" (Stanford, 1939) | Stanford SearchWorks / Stanford Digital Repository (check access + licence); fallback 🛠 typeset recreation in Crimson Pro (Q3) | PD? / own | 2000 h | assets/archival/documents/ — recreation (no scan sought): assets/archival/documents/hewlett_thesis_titlepage_1939_recreation.png |
| A52 | ✅ | SC024 | 1891 Stanford entrance-exam sheet (or 1890s exam blue book) | look on archive.org for 1890s university entrance exam papers; else 🛠 own-made sheet in our fonts + paper/halftone tex | PD / own | 2000 h | assets/archival/documents/ — own-made: assets/archival/documents/entrance_exam_1891_made.png (row bboxes in SOURCES) |
| A53 | ✅ | SC026 | 1891 admission card "Leland Stanford Junior University — Herbert C. Hoover" + rubber stamp "HOOVER GETS IN" | own-made (Cooper Hewitt/Crimson Pro, paper_cream_01 + halftone_03) | own | 2000 w | assets/cutouts/made/ — own-made: assets/cutouts/made/admission_card_hoover_1891.png + stamp_hoover_gets_in.png |
| A54 | ✅ | SC093 | Fellowship letter card, 1930s look (Stanford letterhead feel, no fake signature) | own-made | own | 2000 h | assets/cutouts/made/ — own-made: assets/cutouts/made/fellowship_letter_1938.png |

## 3. Footage clips

All footage: download the **smallest file ≥ 480p** from archive.org (`/download/<id>/<file>.mp4`), cut with ffmpeg
(`-ss … -t … -an` — VO is never touched; footage audio is discarded), save a contact sheet in `_sheet/`, log segments in
`assets/archival/footage/SOURCES.md`.

| ID | status | scenes | subject | preferred sources | licence | len needed |
|---|---|---|---|---|---|---|
| — | ✅ | SC015 | Berkeley 1932 commencement | `assets/archival/footage/berkeley_1932_grad_cut.mp4` | PD Mark | — |
| A11 | ✅ | SC027, SC030 | Herbert Hoover newsreel 1920s (Commerce Secretary; radio speech; walking with officials) | archive.org (Universal Newsreels are PD; Prelinger; "Hoover 1928 campaign"), NARA via archive.org | PD | 2 × 6 s — assets/archival/footage/hoover_1928_south_america_{with_officials_a,crowd_b,sequence_full}.mp4 (1928 South America tour, not Commerce/radio) |
| A23 | ✅ | SC051 | Children taking an intelligence test / classroom testing (1930s–50s) | archive.org Prelinger Archives (search "intelligence test", "testing children", "aptitude") | PD | 7 s — assets/archival/footage/classroom_test_1956_wide.mp4 |
| A27 | ✅ | SC059, SC061, SC063, SC072 | 1920s–30s engineering students / university or corporate research lab (benches, vacuum tubes, oscilloscopes) | archive.org Prelinger ("electrical engineering", "research laboratory", GE/Westinghouse industrials), MIT if PD | PD | 3 × 6 s — assets/archival/footage/ge_schenectady_1923_edison_langmuir_vacuum_tube.mp4, ge_schenectady_research_lab_1923_interior.mp4, radio_engineers_1940_lab_benches.mp4, radio_school_1940_students_lab_bench_{a,b}.mp4 |
| A32 | ✅ | SC067 | Vannevar Bush newsreel (1940s, OSRD) | archive.org Universal Newsreel / NARA | PD | 4 s — assets/archival/footage/vannevar_bush_1945_united_news_osrd.mp4 (close-up last ~3 s) |
| A37 | ✅ | SC090 | 1930s radio factory: testing loudspeakers/radios, sound engineers with meters | archive.org Prelinger (RCA/Philco industrial films) | PD | 5 s — assets/archival/footage/radio_factory_1940_assembly_line.mp4, radio_factory_1940_headphone_testing.mp4 |
| A38 | ✅ | SC077 | Stanford commencement 1920s–30s (fallback ✅ Berkeley clip, other segment) | archive.org, California Revealed | PD | 6 s — per DECISIONS Q6 reuse berkeley_1932_grad_cut.mp4 (no Stanford film searched) |

## 4. Maps & geodata

| ID | status | scenes | subject | source | licence | res / notes | save to |
|---|---|---|---|---|---|---|---|
| — | ✅ | SC007, SC032, SC042 | US Blue Marble basemap (desat) + overlay paths (states, Mississippi, West/East regions, places), clouds, burn maps | `assets/maps/us_basemap_desat.jpg`, `us_overlay.json`, `clouds/*`, `burn_a/b.png`, `na_basemap.jpg` | PD / CC0 | projection x=(lon+128)*100, y=(52−lat)*100 | — |
| A43 | ✅ | SC008, SC075 | **Grey shaded-relief** basemap of the CONUS on the **same projection/bounds** as `us_basemap.jpg` (R12 look) | Natural Earth "Shaded Relief" (SR_HR) or "Gray Earth" 1:10m raster; or NASA SRTM/GMTED hillshade | PD | 6400×3200, lon −128…−64, lat 20…52 (reproject/crop with PIL) | assets/maps/us_relief_grey.jpg → `assets/maps/us_relief_grey.jpg` (+ .json, state masks); also `california_relief_grey.jpg` (SC075) and `indiana_relief_grey.jpg` (SC008), see maps/SOURCES.md |
| A44 | ✅ | SC017, SC081 | **Beige muted US** map (R11): beige land, grey-blue water, thin ink state borders, paper texture inside states | build from ✅ `assets/maps/us_states.geojson` + `us_overlay.json` (SVG); paper_cream_01 multiply | own | SVG + 3840 px PNG preview | assets/maps/us_beige.svg → `us_beige.svg` + `us_beige_3840.png` |
| A24 | 🔁 | SC053 | 1920s US railroad map (Rand McNally / Poole Bros. / USRA), continental, showing Palo Alto/SF → Chicago → Boston | Commons (LOC map division copies), David Rumsey (CC BY-NC — **not allowed**), archive.org, NYPL Map Division (PD items) | PD | ≥ 5000 w | assets/maps/old/ → `assets/maps/old/rand_mcnally_railroad_map_us_1920.jpg` (PD, LOC) — only 3840 w could be fetched (< 5000); usable at ≤1.4x push; control points + route in .json |
| A25 | ✅ | SC056 | 1900s–1920s Boston/Cambridge street map or atlas plate showing MIT (Mass. Ave, Charles) and Harvard Square | Commons (Bromley atlases via LOC/State Library of Mass.), USGS Boston 1903 topo (PD), NYPL | PD | ≥ 4000 w | assets/maps/old/ → `assets/maps/old/usgs_boston_1903_topo.jpg` (4738 w, USGS PD; topo, not a Bromley atlas) + .json places |
| A35 | ✅ | SC085 | Old Palo Alto map: USGS historical topo (Palo Alto quad 1899/1940s) or 1920s–30s street map showing Stanford campus, University Ave, Addison Ave | USGS TopoView historical topos (PD), Commons, Calisphere PD maps | PD | ≥ 4000 w | assets/maps/old/ → `assets/maps/old/usgs_palo_alto_1899_topo.jpg` (4983 w, USGS PD) + .json places (Stanford, University Ave, 367 Addison) |
| A47 | ✅ | SC066, SC074 | Cork-board texture (+ push-pin cutouts) | Texturelabs (cork/board), Commons CC0 | Texturelabs licence / CC0 | ≥ 3840 w | assets/textures/cork_01.jpg → `assets/textures/cork_01.jpg` (3840x2160, CC BY 4.0 Trougnouf — credit) + pins `assets/icons/pin_*.svg` |

## 5. Cutouts, halftones & 2.5D layers to make (🛠)

Tools: `npx hyperframes remove-background in.jpg -o out.png` (people; blur halftone prints first, then apply the matte to the
original), `tools/halftone.py` (45° dot screen, `--sky-key` for plain skies), hand polygons for buildings (see s10 notes).

| ID | scenes | what to make | from | output |
|---|---|---|---|---|
| L1 | ✅ SC023 | **2.5D Main Quad (founding)**: layers = sky/far hills (blurred, extended), Memorial Arch / church façade (mid), arcade columns (near), foreground ground/palm blur; title slot behind the arch | ✅ `stanford_main_quad_panorama_c1896.jpg` / `_b.jpg` (+ A17 if better) | assets/archival/hoover/layers_quad/*.png + backdrop.jpg → ✅ `assets/archival/hoover/layers_quad/` (sky, quad, palms_left/right, bush_left_edge, backdrop, layout.json) |
| L2 | ✅ SC047 | **2.5D 1920s campus**: backdrop (subject removed, blurred), student group (cutout), foreground column/palm (blur) | A20 | assets/archival/stanford_1920s/layers/* → ✅ `assets/archival/stanford_1920s/layers/` (backdrop, students_back, students_front, layout.json; source only 2322 w) |
| L3 | SC086 | 2.5D HP garage | ✅ `assets/archival/hp/layers/{backdrop.jpg,garage.png,hedge.png,house.png}` | — |
| C1 | SC006 | 12 circular badges (logo or HQ crop — Q1), 400 px, ink ring | A46 | assets/cutouts/badges/*.png |
| C2 | SC006 | ghost halftone campus cutout (R4 background building) | A02 | assets/cutouts/applepark_halftone.png — ✅ `assets/cutouts/applepark_halftone.png` |
| C3 | SC010 | apple + orange halftone cutouts | A41 | assets/cutouts/apple_ht.png, orange_ht.png — ✅ apple_ht.png, orange_ht.png |
| C4 | SC013 | NYC skyline halftone (R1 building) | ✅ `assets/archival/cutouts/nyc_skyline_1921_halftone.png` | — |
| C5 | SC019, SC033, SC078 | student cutouts / graduate silhouettes | A20 | assets/cutouts/students_*.png — ❌ matte failed on crowded group — see cutouts/SOURCES.md |
| C6 | SC020, SC032 | halftone US silhouette | ✅ us_states.geojson → `tools/halftone.py` | assets/cutouts/us_halftone.png |
| C7 | SC025, SC028 | Hoover young, Swain, Lou Henry cards (tinted, torn edges) | ✅ hoover_young_1898, A09, A12 | assets/cutouts/cards/*.png — ✅ `cutouts/cards/joseph_swain_cut.png`, `lou_henry_1905_cut.png` (+ circles in `cutouts/portraits/`); tint/torn edges in-scene |
| C8 | SC039, SC092 | banknote / gold-certificate halftone cutouts (3–5) | A16 | assets/cutouts/money_*.png |
| C9 | SC047, SC052, SC065, SC066 | young Terman cutout + card | A21 (fallback ✅ terman_frederick_1955) | assets/cutouts/terman_young.png — ✅ `cutouts/terman_young.png` + `_ht.png` + `portraits/terman_young_circle.png` |
| C10 | SC050 | Lewis Terman circular halftone portrait | A22 / ✅ lowres | assets/cutouts/lewis_terman_ht.png — ✅ `cutouts/lewis_terman_ht.png` |
| C11 | SC058 | three halftone circular icons: Great Dome, professor (Bush crop), 1920s factory | ✅ MIT aerial, ✅ Bush 1938, A30 | assets/cutouts/triangle_*.png |
| C12 | SC061, SC076 | vacuum tube / 1920s radio set cutout, halftone | A49 | assets/cutouts/tube_ht.png, radio_ht.png |
| C13 | SC069, SC070 | gothic tower + iron gate cutouts | A33 | assets/cutouts/tower.png, gate.png |
| C14 | SC073 | Raytheon tube/ad card; Bush cutout | A34, ✅ vannevar_bush_1938 | assets/cutouts/raytheon_card.png, bush_cut.png |
| C15 | SC081, SC083 | Packard and Hewlett halftone cards | ✅ `assets/archival/cutouts/packard_david_1933.png`, `hewlett_william_c1962.png` | — |
| C16 | SC089 | HP 200A crop icon + 1930s speaker/radio cabinet icon (halftone) | ✅ hp_200A photo, A49 | assets/cutouts/osc_icon.png, speaker_icon.png |
| C17 | SC030, SC051, SC067 | transparent-screen TV PNGs + `*_screen.json` bbox (like tv_frame_01) | A48a/b/c | assets/textures/tv_frame_02…04.png |

## 6. Logos

| ID | status | scenes | subject | source | licence |
|---|---|---|---|---|---|
| — | ✅ | SC018, SC060, SC082 | GE monogram | `assets/archival/brain_drain/ge_logo.svg`, `ge_logo_bone.svg` | PD (trademark) |
| — | ✅ | SC008 | Eli Lilly logo | `assets/maps/eli_lilly_logo.svg` | PD (trademark) |
| A28 | ✅ | SC060 | AT&T 1920s Bell System bell logo; Bell Telephone Laboratories wordmark (1925+) | Commons "Bell System logo 1921", "Bell Labs logo" | PD-textlogo (trademark) → `assets/logos/bell_system_1921.png`, `att_bell_1921_1939.png`; Bell Labs wordmark ❌ (set in type) |
| A46 | ✅ | SC006, SC009 | 11 more logos for the trillion-dollar companies: NVIDIA, Apple, Microsoft, Alphabet/Google, Amazon, SpaceX, Broadcom, Meta, Tesla, Berkshire Hathaway, Micron (only if Q1 = logos) | Commons SVGs | PD-textlogo / trademark — confirm with user (Q1) → `assets/logos/*.svg` — all 11 (Berkshire & Broadcom from Commons) |

## 7. Textures

All default textures ✅ in `assets/textures/` (grain, dust, scratches, halftone, newsprint, paper, light leaks — see its SOURCES.md).
New:

| ID | status | scenes | subject | source |
|---|---|---|---|---|
| A47 | ✅ | SC066, SC074 | cork board (see §4) | Texturelabs / CC0 → `assets/textures/cork_01.jpg` |
| T1 | ❌ | SC024, SC087, SC093 | typewritten/old-document paper with slight foxing (if paper_cream_01 isn't enough) | Texturelabs Paper not made — paper_cream_01/02 suffice |
| T2 | ✅ | SC017 | watercolour edge mask for R11 / R1 bar tops | make from Texturelabs paper + threshold (`tools/halftone.py` style) → `assets/textures/watercolour_edge_mask_01.png` |

## 8. TV sets & props

| ID | status | scenes | subject | source | licence | notes |
|---|---|---|---|---|---|---|
| — | ✅ | SC015 | TV #1 Philco Predicta 1960 | `assets/textures/tv_frame_01.png` + `_screen.json` | CC0 | approved |
| A48a | ✅ | SC030 | TV #2: 1930s wooden radio-cabinet television (RCA TRK-12 1939, or similar mirror-lid/console set) — front/3⁄4 view | Commons (museum photos by Daderot are often CC0), Early Television Museum images (check licence) | CC0 / CC BY-SA | cut out screen → alpha; record screen bbox json — assets/textures/tv_frame_02.png (RCA TRK-12 1939, mirror-lid; bg kept) |
| A48b | ✅ | SC051 | TV #3: 1950s portable TV | Commons | CC0 / CC BY(-SA) | as above — assets/textures/tv_frame_03.png (Bush TV22 1950; bg kept) |
| A48c | ✅ | SC067 | TV #4: late-1940s console with doors (e.g. RCA 630-TS cabinet, DuMont) | Commons | CC0 / CC BY(-SA) | as above — assets/textures/tv_frame_04.png (Westinghouse 196 c.1949, no doors; bg kept) |
| A49 | ❌ | SC061, SC076, SC089 | 1920s vacuum tube (e.g. UV-201A) and a 1920s–30s radio set / loudspeaker | Commons museum photos | CC0 / CC BY-SA | plain background preferred for keying — not done (out of time); footage ge_schenectady_1923_edison_langmuir_vacuum_tube.mp4 shows a tube |
| P1 | ✅ | SC066, SC074 | push pins (vermilion, navy, bone) + red string stroke style | own SVG | own | → `assets/icons/pin_{vermilion,navy,bone}[_top].svg`, `red_string_style.css` |

## 9. Icons for isotype / diagrams (🛠, SVG, own work)

| ID | scenes | icon set | style |
|---|---|---|---|
| A39 | ✅ SC033, SC078 | graduate pictogram (cap & gown), 1 shape, used in a grid; must be identical in both scenes | flat, 64×64 grid, ink fill; vermilion / navy / grey states (R5) → ✅ `assets/icons/graduate*.svg` |
| I2 | ✅ SC009 | dot for the semicircle (R8) — plain circles, 305 positions computed in code | — (code only) |
| I3 | ✅ SC032, SC042, SC059 | flow dots / arc heads | bone dot + 2 px halo → ✅ `assets/icons/flow_dot.svg` |
| I4 | ✅ SC058, SC089 | diagram arrows and node rings (rough via `FX.roughDefs`) | ink stroke 3 px → ✅ `assets/icons/arrow.svg`, `node_ring.svg` |
| I5 | ✅ SC006 | dashed $1 T threshold line style shared with SC013's dashed line (R1) | ink, 10/8 dash → ✅ `assets/icons/dashed_threshold.svg` |

## 10. Sound (for the sound agent; free sources only)

| status | item | source |
|---|---|---|
| ✅ | music beds + stingers (marimba/pad/pizz stems): curious_neutral_Dmaj_96bpm, historic_nostalgic_Gmaj_84bpm_3-4, momentum_building_Dmaj_108bpm, tension_braindrain_Bmin_92bpm, stinger_reveal/soft_rise/tension | `assets/audio/music/*` (synthesized, own) |
| ✅ | shutter | `assets/sfx/shutter.wav` |
| ✅ | Kenney impact / interface / RPG packs (CC0) — pops, ticks, paper, thuds | `assets/audio/_raw/kenney_*` |
| 🔎 | whooshes, paper slide/rustle/tear/flip, page turn, marker scratch, highlighter swipe, pencil scribble, pin pop / cork pin, string pull, stamp thud, odometer/counter ticks, projector loop + click, CRT click/hum/off, low boom, burn crackle, wind, lamp click, gate creak, film burn, chime, 440 Hz tone blip | freesound.org **CC0 only**, Kenney, Sonniss GDC bundles (royalty-free), or synthesize (`tools/audio/`) |
| 🛠 | `assets/audio/LIBRARY.md` and `assets/audio/MIX_RULES.md` (referenced by MANUAL §7, missing) | sound agent writes them |

---

## Summary counts

| group | ✅ exists | 🔎 to find | 🛠 to make |
|---|---|---|---|
| archival photos | 9 groups | 26 | — |
| newspapers/documents | 2 | 6 | 3 (+2 fallbacks) |
| footage | 1 | 6 | — |
| maps/geodata | 1 set | 5 (incl. cork) | 1 |
| cutouts / 2.5D layers | 3 | — | 17 |
| logos | 2 | 2 (A28, A46) | — |
| textures | full set | 1 (+cork) | 1 |
| TV sets & props | 1 | 4 | 1 |
| icons | — | — | 5 |
| SFX | packs + shutter | ~22 types | 2 docs |

**New items to source: 49** (🔎, deduplicated; A38 and A47 counted once) · **to make: 28** (🛠, cutouts/layers/icons/own-made documents/maps).
