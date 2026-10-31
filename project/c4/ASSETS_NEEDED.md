# ASSETS NEEDED — CHUNK c4 (local 0.00–601.44)

Deduplicated list for `EDIT_NOTES.md` (IDs `E..` = exists in the repo, `N..` = still needed / to make). Snapshot taken
2026-10-31 by the planner. **Gatherers: flip ❌ → ✅/🔁 with the path when you land a file**, log every file in its folder's
`SOURCES.md` (subject, URL, licence or "© owner — fair use (documentary commentary, transformed, credited)", author, date,
size; bboxes for documents). New files go to `assets/c4/<type>/` (photos, footage, documents, posters, maps, cutouts, layers).

Rules (§10.9 long-form): **copyrighted material allowed** (news/press photos, UN Photo, magazine covers, period posters,
newspaper pages) — never log in, never pay, never strip watermarks, credit on screen where customary; prefer the TRUE image
in the best quality; reuse is allowed when needed but prefer unique images. Reject wrong subject/era, < 1600 px long side for
full-frame (≥ 3000 px for 2.5D). Look at every file. Sensitive subjects (Japanese army in China, White Terror, war damage,
1949 refugees): **non-graphic only** — no bodies, no executions.

Legend: ✅ exists · 🔁 substitute · ❌ to find · 🛠 to make (from existing material).

**Best sources for this chunk** (in order): UN Photo / UN Digital Library / UN Audiovisual Library (digitallibrary.un.org,
media.un.org — UN photos are © UN; fair use + credit "UN Photo") · Wikimedia Commons (`tools/find_media.py commons-html`) —
pre-1945 Taiwan photos and pre-1970s ROC government photos are public domain in Taiwan · archive.org (Universal Newsreels,
NARA films, `gov.archives.arc.653126` "Taiwan: The Face of Free China" 1960 — already our source) · NARA catalog (USAAF
1944–45 Formosa strike photos/films, PD) · LOC image servers (§8.1) · Taiwan open archives: National Archives Administration
(archives.gov.tw), Academia Historica (國史館), Taiwan Memory / National Central Library, Kaohsiung Museum of History, NTU
Library digital archive (Taihoku Imperial University photos) — fair use + credit · chineseposters.net / IISH Stefan
Landsberger collection (PRC posters; credit) · press archives for clippings (NYT TimesMachine front-page images via
Commons/archive.org mirrors; Google News Archive scans; TIME covers at content.time.com — fair use).

## 1. Existing (reuse — paths verified 2026-10-31)
| ID | status | path | scenes | notes |
|---|---|---|---|---|
| E01 | ✅ | `assets/intro/footage/taiwan_1960_presidential_office_taipei.mp4` (8 s, 640×480, CC0, 1960) | C4S039 (first half), C4S085 (second half) | Japanese-built Governor-General's Office = Presidential Office; upscale ≤ 1.5× inside a plate with fringe blur |
| E02 | ✅ | `assets/intro/footage/taiwan_1960_taipei_north_gate_traffic.mp4` | C4S094 | |
| E03 | ✅ | `assets/intro/footage/taiwan_1960_taipei_boulevard_high_angle.mp4` | C4S024 | |
| E04 | ✅ | `assets/intro/footage/taiwan_1960_sun_moon_lake.mp4` (Sun Moon Lake = Japanese-era hydropower reservoir) | C4S034 (still card "hydropower" — only if N16c not found) | |
| E05 | ✅ | `assets/intro/footage/taiwan_1960_factory_yard_workers.mp4`, `taiwan_1960_steel_mill_molten.mp4` | reserve (C4S056 / C4S091 fallback) | |
| E08 | ✅ | `assets/intro/photos/keelung_port_cc0.jpg` | C4S034 "ports" (fallback if N16b not found) | modern? check era — prefer N16b |
| E09 | ✅ | `assets/intro/photos/nanzih_epz_ose_factory.jpg` | C4S099 fallback | a real export-processing-zone factory |
| E10 | ✅ | `assets/intro/maps/taiwan_relief_grey.jpg` (+json), `taiwan_mask.png`, `taiwan_celadon_fill.png`, `made/taiwan_celadon_wash.png` | C4S010, 014, 017, 037, 046, 060, 082 | celadon motif (intro grade); alpha mask rule §4.2 |
| E11 | ✅ | `assets/intro/maps/world_basemap_desat.jpg` / `_2560.jpg` (+json), `world_countries.svg` | C4S053, C4S072 | until the map kit lands |
| E12 | ✅ | `assets/intro/maps/pacific_relief_grey.jpg` (+json, 2850 px version) | C4S049, C4S078–079 | |
| E13 | ✅ | `assets/intro/maps/formosa_1943_japanese_aviation_map.jpg` (+json) | C4S043 | vintage colour map of the strait area |
| E14 | ✅ | `assets/intro/paintings/taiwan_expo_1935_poster.jpg`, `taiwan_birdseye_1935.jpg` | C4S027 (poster), C4S036 (bird's-eye) | Japanese-era originals — perfect matches |
| E15 | ✅ | `assets/intro/screens/tektronix_475a_scope_frame.png`, `tatung_tv20cge_frame.png` (+`_screen.json`) | C4S023, C4S103 | |
| E16 | ✅ | `assets/intro/papers/ke1960_*_hires.jpg`, `assets/textures/paper_{graph,lined,stained,blueprint,torn,cream,fiber}_01*_hires.jpg` | all PAPER/GRID scenes | `_hires` only at full frame |
| E18 | ✅ | `assets/intro/documents/telegram_western_union_1959.jpg` | C4S015 (form reference for the typeset cable) | |
| E20 | ✅ | `assets/intro/photos/jfk_1981_panam747.jpg` | C4S077 (small, newspaper column) | era 1981 — fine as a small airliner; better: N29d 1960s airliner |
| E22 | ✅ | `assets/textures/cork_01.jpg` (CC BY — credit) | C4S083 | |
| E24 | ✅ | `assets/icons/graduate*.svg` | C4S071, 082, 084 | |

## 2. People
| ID | status | need | scenes | era | search terms | best sources |
|---|---|---|---|---|---|---|
| N08 | ✅ `c4/photos/mao_proclaims_prc_1949_tiananmen.jpg` (771 px) + footage `c4/footage/china_1949_mao_tiananmen_waving.mp4`, `china_1949_tiananmen_crowd.mp4` + `prc_founding_1949_tiananmen_crowd.jpg` | Mao proclaiming the PRC, Tiananmen, 1 Oct 1949 (+ crowd/gate crops) | C4S007, C4S010 | 1949 | "Mao proclaims People's Republic 1949", "开国大典 照片" | Commons (PD-China), Xinhua via press archives (fair use) |
| N13 | ✅ `c4/photos/eisenhower_chiang_motorcade_taipei_1960.jpg` (1102 px) + colour alt | Eisenhower with Chiang Kai-shek in Taipei, June 1960 (motorcade / joint appearance) | C4S021 | 1960 | "Eisenhower Taipei 1960", "Eisenhower Chiang Kai-shek motorcade" | Eisenhower Library / NARA (PD), Commons, Universal Newsreel on archive.org |
| N15b | ✅ `c4/paintings/emperor_meiji_portrait_painting.jpg` | Meiji Emperor portrait (colour print or photo) | C4S028 | 1870s–1900s | "Emperor Meiji portrait" | Commons (PD) |
| N23c / N23d | ❌ | 1950s Taiwanese landowner (gentry) portrait; tenant farmer portrait | C4S051–052 | 1950s | "Taiwan landlord 1950s", "Taiwan farmer 1950s photo", "耕者有其田 農民" | Taiwan National Archives, Face of Free China stills (N40), Commons |
| N27 | 🔁 `c4/photos/tiananmen_gate_mao_portrait_modern.jpg` (crop) | Mao Zedong official painted portrait (Tiananmen style) | C4S066 | 1950s–60s | "Mao Zedong official portrait painting" | Commons (PD) |
| N30 | ✅ `c4/photos/chiang_kaishek_uniform_cape_map_nara.jpg` (+cutout, 2 more portraits) | Chiang Kai-shek in uniform, ≥ 3000 px (2.5D) | C4S088 | 1940s–50s | "Chiang Kai-shek uniform portrait", "蔣中正 戎裝" | Commons (PD-ROC-exempt / PD-old), LOC (`hec`/`cph` items), Academia Historica |
| N30b | ❌ | 1950s ROC cabinet / KMT leadership group photo (mainland-born leaders) | C4S086 | 1950s | "Executive Yuan 1950s cabinet photo", "KMT Central Standing Committee 1950s" | Academia Historica, Commons |
| N30c | ❌ | ROC generals line-up / staff, 1950s | C4S087 | 1950s | "ROC Army generals 1950s Taiwan", "國軍 將領 1950" | Commons, NARA (US advisers with ROC generals — PD) |
| N30d | 🔁 `c4/documents/time_cover_1927_chiang_kaishek.jpg` (400 px, not uniform) | Period magazine cover of Chiang Kai-shek in uniform | C4S089 | 1937–55 | "TIME cover Chiang Kai-shek" | TIME vault (content.time.com) — © TIME, fair use, credit |
| N30e | ❌ | ROC government / officials arriving in Taiwan 1949–50 | C4S085 | 1949–50 | "Chiang Kai-shek arrives Taiwan 1949", "ROC government relocation Taipei 1949" | Commons, Universal Newsreel, Academia Historica |
| N30f | 🔁 `c4/photos/lin_family_taiwanese_gentry_london.jpg` (Wufeng Lin family, 1927) | 1950s Taiwanese elite / gentry group photo | C4S086 | 1950s | "Taiwanese gentry 1950s", "Taiwan provincial assembly 1950s" | Commons, Taiwan Memory |
| N31 | ❌ | 1960s Taiwanese engineers at drafting tables / at Shihmen Dam (unnamed) | C4S091 | 1960s | "Shihmen Dam construction 1960s engineers", "Taiwan engineers 1960s drafting" | Commons, Taiwan Water Resources Agency archive, Face of Free China |

## 3. Places, events, objects (photos / footage)
| ID | status | need | scenes | era | search terms | best sources |
|---|---|---|---|---|---|---|
| N01 | ✅ `c4/photos/un_security_council_1962_stevenson_chamber.jpg` + footage `c4/footage/un_1950_security_council_*.mp4` / GA `un_1960_general_assembly_*.mp4` | UN Security Council chamber (horseshoe table, Krohg mural), wide, ≥ 2400 px | C4S001 | 1950s–60s | "Security Council chamber 1950s UN Photo", "Security Council meeting 1960" | UN Photo (© UN, fair use, credit "UN Photo"), Commons (UN Photo uploads), LOC |
| N02 | 🔁 `c4/photos/un_general_assembly_hall_wide_emblem.jpg` (2006, 3840 px) | UN General Assembly hall, wide with the emblem above the rostrum, ≥ 3000 px (2.5D layers) | C4S004–005 | 1950s–60s | "General Assembly hall 1955", "UN General Assembly 1961 wide" | UN Photo, Commons |
| N03 | ✅ `c4/cutouts/un_emblem.svg` | UN emblem (vector) | C4S004 | — | "Emblem of the United Nations.svg" | Commons |
| N04 | ❌ | ROC delegation desk with the 'CHINA' nameplate in the GA / SC | C4S006 | 1950s–60s | "China nameplate United Nations 1960s", "Republic of China delegation UN" | UN Photo, AP/press (fair use) |
| N06 | ❌ | 3–4 real newspaper clippings/front pages on the yearly UN China-seat vote ("U.N. again bars Red China"–type headlines) | C4S011 | 1950s–1970 | "UN rejects seating Red China headline", "U.N. bars Peiping" | NYT TimesMachine images (Commons/archive.org mirrors), Google News Archive (fair use) |
| N07 | ✅ `c4/documents/un_draft_A-L630_1971_expel.jpg` | Real UN draft-resolution page on the representation of China (expel the representatives in Taiwan) | C4S009 | 1960s | "A/L draft resolution representation of China", "restoration of the lawful rights People's Republic of China draft resolution" | UN Digital Library (ODS PDFs, public) |
| N11 | ❌ | ROC agricultural / diplomatic mission in Africa ("Operation Vanguard") | C4S015 | 1960s | "Republic of China agricultural mission Africa 1960s", "先鋒案 農耕隊 非洲" | Taiwan ICDF / MOFA archives, Academia Historica (fair use) |
| N15 | ✅ `c4/paintings/taiwan_1895_sankakuyu_battle_woodblock.jpg` (single sheet) | Colour ukiyo-e triptych of the 1895 Japanese invasion of Taiwan | C4S028 | 1895 | "Japanese invasion of Taiwan 1895 woodblock", "台湾 錦絵 1895" | Commons (PD), LOC Japanese prints (`jpd` items — tile.loc.gov), MFA Boston |
| N16a | ✅ `c4/photos/japanese_era_taihoku_station.jpg` | Japanese-era Taiwan railway (steam train / Taihoku station) | C4S034 | 1910s–30s | "Taihoku station 1930s", "Taiwan railway Japanese era" | Commons (PD), NTU/Taiwan Memory |
| N16b | ❌ | Japanese-era harbour (Keelung / Takao 1930s) | C4S034 | 1930s | "Keelung harbor 1930s", "Takao port Japanese era" | Commons |
| N16c | ✅ `c4/photos/japanese_era_jitsugetsutan_power_plant_workers.jpg` | Japanese-era hydropower plant (Sun Moon Lake / Daguan) | C4S034 | 1934 | "Sun Moon Lake hydroelectric 1934", "日月潭 発電所" | Commons |
| N16d | ❌ | Japanese-era power lines / electric company; period light bulb | C4S034, C4S044 | 1930s | "Taiwan Electric Power Company Japanese era" | Commons |
| N16e | ✅ `c4/photos/japanese_era_fenglin_kogakko_school.jpg` + `japanese_era_hsinchu_school_pupils_sports_meet.jpg` | Japanese-era primary school pupils (kōgakkō) | C4S035 | 1920s–30s | "公學校 台湾 1930", "Taiwan public school Japanese rule" | Commons, NTU archive |
| N16f | ✅ `c4/photos/taihoku_1930s_street_joss_paper_store.jpg` | 1930s Taihoku (Taipei) street | C4S033 | 1930s | "Taihoku street 1930s", "Sakaemachi Taihoku" | Commons |
| N17 | ✅ `c4/photos/japanese_naval_troops_shanghai_1937.jpg`, `japanese_army_parade_nanking_1937_colour.jpg` | Japanese army in China 1937–38, marching columns (non-graphic) | C4S030–031 | 1937–38 | "Japanese troops China 1937 march" | Commons, NARA, Universal Newsreel (archive.org) |
| N17b | ✅ `c4/photos/japanese_era_police_officer_sedan_chair_1918.jpg` (+c1900 alt) | Japanese colonial police in Taiwan | C4S032 | 1900s–30s | "Japanese police Taiwan colonial" | Commons |
| N19 | ✅ `c4/photos/formosa_1945_*_usaf.jpg` (4 NARA prints) + footage `c4/footage/usn_1945_formosa_strike_*.mp4` (USS Essex strike 4 Jan 1945, PD) | USAAF strike footage/photos over Formosa (bomb run, smoke, harbour) | C4S042 | 1944–45 | "bombing of Formosa 1945", "Takao air raid 1945", "Taihoku air raid" | NARA (PD), archive.org (USAF films), Commons |
| N20 | 🔁 footage `c4/footage/china_1949_crowded_boat_harbour.mp4`, `china_1949_wharf_crowd_ships.mp4` (1949 evacuation, © 1972 doc, fair use) + `tachen_1955_*.mp4` (real Nationalist evacuation to Taiwan, 1955, PD) | 1949 ship crowded with soldiers/refugees arriving in Taiwan | C4S045 | 1949 | "1949 retreat to Taiwan ship Keelung", "Nationalist troops arrive Taiwan 1949" | Commons, LIFE (Jack Birns — fair use), Universal Newsreel |
| N21 | ✅ `c4/documents/bank_of_taiwan_1949_one_million_yuan_cheque.jpg`, `old_taiwan_dollar_500_1946_back.jpg` | 1949 banknotes (old Taiwan dollar, very high denominations) — cut-outs | C4S044 | 1946–49 | "Old Taiwan dollar 1949 banknote", "舊臺幣 百萬" | Commons |
| N22 | ❌ | US-aid handshake emblem on a flour sack (中美合作) | C4S048 | 1950s | "US aid flour sack Taiwan", "中美合作 麵粉袋" | Commons, Taiwan museums (fair use) |
| N23 | ✅ `c4/documents/land_to_the_tiller_poster_1960s.jpg` (+booklet, 1963 stamp) | 1950s land-reform poster ("land to the tiller") in colour | C4S050 | 1953 | "耕者有其田 海報", "land to the tiller poster Taiwan" | Taiwan National Archives, Commons |
| N23b | ❌ | Land deed / ownership certificate of the 1953 reform (or typeset recreation, no seals) | C4S052 | 1953 | "耕者有其田 所有權狀" | Taiwan National Archives |
| N24 | ✅ `c4/documents/taiwan_cement_share_certificate_1950s.jpg` | Real 1950s share certificate of a state company given to landowners | C4S054 | 1953–54 | "台灣水泥 股票 1954", "land reform shares certificate Taiwan" | Taiwan museums / auction archives (fair use) |
| N24b | ❌ | 1950s Taiwanese state-owned factory interior, ≥ 3000 px (2.5D) | C4S056 | 1950s | "Taiwan Cement plant 1950s", "Taiwan factory 1950s" | Commons, Face of Free China (E05 fallback) |
| N25 | ❌ | 1950s–60s Taiwan market (rice / produce for sale) | C4S058 | 1950s–60s | "Taiwan market 1960s photo" | Commons, Face of Free China |
| N25b | ❌ | ration queue / empty bowls; a street crowd; a wall of posters (non-specific period) | C4S047 | 1940s | "rice ration line 1940s China", "crowd Taipei 1947" (avoid 228 specifics) | Commons, NARA |
| N26 | ✅ `c4/photos/green_island_human_rights_park.jpg`, `jingmei_human_rights_park_entrance.jpg` | White Terror memorial: Green Island prison / Jing-Mei detention centre corridor | C4S063–065 | (site) | "Green Island White Terror memorial", "Jing-Mei detention center corridor" | Commons (CC BY — credit) |
| N26b | ❌ | 1950s KMT rally (portraits, banners) | C4S063 | 1950s | "Kuomintang rally 1950s Taipei" | Commons, Academia Historica |
| N26c | 🔁 `c4/photos/wooden_ballot_box_smithsonian.jpg` (+`derived/c4s02/ballot_box_cutout.png`; generic US box — c4s02) | period wooden ballot box | C4S061 | 1950s | "ballot box 1950s" | Commons |
| N27b | ✅ `c4/posters/four_pests_campaign_poster_1958.jpg`, `brave_the_wind_and_waves_poster_glf.jpg` (small, cards — c4s02) | 2 colour Great Leap Forward posters | C4S067 | 1958–60 | "Great Leap Forward poster 1958" | chineseposters.net (credit), Commons |
| N28 | 🔁 `c4/photos/taihoku_imperial_university_staff_1937.jpg` (staff group, small) | Taihoku Imperial University / NTU main building, 1960s NTU Royal Palm Boulevard | C4S070, C4S074 | 1930s / 1960s | "Taihoku Imperial University", "National Taiwan University 1960s" | NTU Library archive, Commons |
| N28c | ❌ | 1950s Taiwan classroom | C4S070 | 1950s | "Taiwan classroom 1950s" | Face of Free China, Commons |
| N28d | ❌ | Colour 1960s NTU campus postcard (§10.7 painting-to-print) | C4S076 | 1960s | "台大 明信片 1960" | Commons, postcard archives (fair use) |
| N29 | 🔁 footage `c4/footage/formosa_1950_songshan_airport_plane_arrival.mp4` (Songshan apron 1950, PD; no 1960s terminal interior) | Taipei Songshan Airport terminal 1960s (doors / departure hall) | C4S069 | 1960s | "Songshan Airport 1960s terminal", "松山機場 1960" | Commons, Taiwan Memory |
| N29b / N29c / N29d | ❌ | 1960s diploma (or typeset); suitcase + airline ticket; 1960s airliner | C4S073, C4S077 | 1960s | "1960s airline ticket", "Pan Am 707 1960s" | Commons, SFO Museum (credit) |
| N32 | ❌ | Kaohsiung Export Processing Zone 1966–70: factory floor ≥ 3000 px (2.5D), gate | C4S099 | 1966–70 | "Kaohsiung Export Processing Zone 1966", "加工出口區 1966" | MOEA EPZ Administration history page (fair use), Taiwan Panorama, Commons (E09 fallback) |
| N32c | ❌ no EPZ assembly footage found on archive.org (YouTube blocked); fallback `c4/footage/taiwan_1960_brickworks_workers.mp4` / intro `fab_women_cleanroom_line.mp4`, `fab_hk_workers_microscope_rows_*.mp4` | EPZ assembly-line footage (women assembling electronics) | C4S103 | 1960s–70s | "Kaohsiung export processing zone film", "Taiwan electronics assembly 1970 newsreel" | archive.org newsreels, Taiwan Film Institute clips (fair use, short) |
| N33 / N33b | 🔁 N33b `c4/photos/shenzhen_skyline_from_shenzhen_bay.jpg` (modern, halftone strip); N33 ❌ → typographic timeline | early Shenzhen SEZ (billboard / construction) photo; Shenzhen skyline for halftone | C4S096, C4S097 | 1980s | "Shenzhen special economic zone 1980 billboard" | Commons, press (fair use) |
| N35 | ❌ | 1960s cargo ship cut-out | C4S100 | 1960s | "cargo ship 1960s photo Kaohsiung" | Commons |
| N40a | ✅ 29 clips `c4/footage/taiwan_1960_*.mp4` (rice transplanting, water buffalo, farmhouse, sugar, refinery, school, Chiang billboard, painted map w/ Japanese flags…) | more clips from *Taiwan: The Face of Free China* (1960): rice paddies, farmer + water buffalo ploughing | C4S037, C4S057 | 1960 | `gov.archives.arc.653126` contact sheet (`ffmpeg fps=1/4 tile`) | archive.org (CC0) — already our source, easy win |
| N41 | ❌ | brass balance scale (cut-out) | C4S019 | — | "balance scale antique" | Commons (CC) |

## 4. Maps (`assets/maps/kit/` — **currently EMPTY**; maps must look rich at 1080p after the push, §10.9)
| ID | status | need | scenes | notes |
|---|---|---|---|---|
| N36 | 🔁 kit has East Asia/Taiwan/world/Pacific (`assets/maps/kit/`); c4 adds `c4/maps/africa_*` (+ `c-*` country paths, independence order) and `c4/maps/eurasia_*` (+ 1960 Warsaw-Pact paths `h-*`) — crops of the kit world relief (45 px/°) | Map kit: high-res shaded relief (Natural Earth II class) for **Eurasia** (Warsaw Pact masks), **Africa** (admin-0 masks for the 1950s–60s independence sequence), **East Asia** (China / Taiwan / Japan / Korea masks), **Asia**; lon/lat→px json each | C4S008, 013–014, 016–017, 040, 043, 053, 066, 095 | dark (night) and beige (paper) grades from the same kit; Taiwan celadon / China red overlays |
| N36b | ❌ | Vintage colour atlas plates (1930s–50s): world (war-room map), East Asia | C4S022, 025, 041, 092 | David Rumsey (CC BY-NC → check; else Commons / LOC atlas plates PD) |
| N34 | ✅ `c4/maps/aerial_kaohsiung_epz_z17.jpg` (4352×4864, Zhongdao EPZ) + `aerial_kaohsiung_harbour_z16.jpg` (+json) — credit Esri, Maxar, Earthstar Geographics | Satellite imagery of Kaohsiung harbour / Qianzhen EPZ (sharp at 1080p) | C4S102 | Esri World Imagery (credit) or Sentinel-2 cloudless (CC BY 4.0) |
| N34b | ✅ `c4/maps/takao_1945_ams_city_plan.jpg` (logged by another gatherer) | US Army Map Service city plan of Takao (Kaohsiung), 1944–45 | C4S098 | PD — UT Austin PCL map collection / Commons (same series as the intro's Hsinchu plan) |

## 5. Made by us (🛠, graphics — motifs, no limit)
Seat horseshoe + chair icon (C4S002–003, 010, 020); GA dot hemicycle (C4S020); stamps DEFEATED / VETO / NEW OWNER / TARIFF
(ink rubber-stamp texture); typeset diplomatic cable (C4S015 — no fake seals/logos); filmstrip rewind (C4S026); calendar pad
(C4S007); pictogram family N38 (people, graduates, generals, engineers, factory, chip) → `assets/c4/icons/`; flow diagram parts
(crates, gate, ship, zone border) C4S100–101; typeset newspaper column for §10.7 (C4S076–077 — no real masthead); pennant.

## 6. Biggest needs (priority for gatherers)
1. **Map kit** (N36, N34, N34b) — 13 scenes depend on it.
2. **UN set** (N01, N02 ≥ 3000 px, N04, N06, N07) — Act A/B (C4S001–011) is built on them.
3. **Japanese-era Taiwan set** (N15, N16a–f, N17b) + **1949 set** (N19, N20, N21) — Acts D–E.
4. **Land reform set** (N22, N23, N23b, N24, N24b) and **EPZ set** (N32, N32c).
5. **Chiang Kai-shek ≥ 3000 px** (N30) + NTU set (N28, N28d, N29).
6. Easy win: more 1960 *Face of Free China* clips (N40a) — CC0, already on archive.org.
