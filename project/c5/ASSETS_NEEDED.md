# ASSETS NEEDED — CHUNK c5 (local 0.00–598.03)

Deduplicated list for `EDIT_NOTES.md`. IDs: `E..` exists in the repo · `N..` to find · `M..` map kit (`assets/maps/kit/`, being built by the map-kit agent) · `G..` to make (typeset/graphic, from our own material). **Gatherers: flip ❌ → ✅/🔁 with the path when a file lands, and log every file in its folder's `SOURCES.md`** (subject, URL, licence or "© owner, fair use", author, date, size; bboxes for documents). Put new c5 files under `assets/c5/{photos,footage,documents,paintings,screens,logos,made}/`.

Rules (MANUAL §8.1 + **§10.9**): copyrighted material allowed under fair use (documentary commentary, transformed with our treatments, credited
on screen where customary) — news/press photos, UN Photo, presidential-library images, newspaper pages, magazine covers, period ads. Prefer PD/US-gov
(NARA, presidential libraries, LOC, State Dept, US Navy) and Commons when equal in quality. Never log in, never pay, never strip watermarks (skip
watermarked Getty/AP/Pathé previews). Look at every file; reject wrong subject/era, < 1600 px long side for full-frame (≥ 3000 px for 2.5D).
Re-use allowed when the story needs it (§10.9) — the "scenes" column shows planned uses. Search: `python3 tools/find_media.py commons-html|archive|archive-texts|files "<q>"`.

Legend: ✅ exists · 🔁 substitute · ❌ to find · 🛠 to make.

## 1. People (photos → plates, circles, cut-outs)
| ID | status | subject / path | era | scenes (segment) | search terms | best sources | notes |
|---|---|---|---|---|---|---|---|
| N01 | ✅ | Henry Kissinger portrait as National Security Advisor (1969–73), ≥2000 px → `assets/c5/photos/kissinger_portrait_1973_official.jpg (+ nixon_kissinger_*.jpg)` | 1970–72 | 046, 047, 049, 078, 119 (02/03) | "Henry Kissinger 1973" "Kissinger national security advisor portrait" | Commons (White House photo, PD), Nixon Library, NARA | 2 uses (C5S046, crops for C5S049/078/119) |
| N02 | ✅ | Kissinger arriving in Pakistan, July 1971 (with Yahya Khan / at Chaklala or Islamabad) → `assets/c5/photos/kissinger_rawalpindi_hilaly_1971-07-08.jpg (CC BY-SA, credit)` | Jul 1971 | 054 (02) | "Kissinger Pakistan July 1971" "Kissinger Yahya Khan" | Dawn archive, Pakistan Information Dept, Nixon Library; news archives (fair use, credit) | fallback: Kissinger 1971 photo + Pakistan map card |
| N03 | ✅ | Kissinger at his desk / in the White House, 1971 → `assets/c5/photos/nixon_kissinger_eob_poodle.jpg / nixon_kissinger_oval_window.jpg` | 1971 | 080 (02) | "Kissinger White House 1971 desk" | Nixon Library (PD), NARA, Commons | dark grade for the title |
| N04 | ❌ | Kissinger with Zhou Enlai, Beijing, July 1971 (Polo I) | Jul 1971 | 083 (02) | "Kissinger Zhou Enlai 1971" "secret trip Beijing 1971" | Nixon Library, NARA, National Security Archive (GWU), Xinhua (fair use) |  |
| N05 | ❌ | Kissinger in Beijing, October 1971 (Polo II, Great Hall) | Oct 1971 | 110, 121 (03) | "Kissinger October 1971 Beijing Zhou Enlai Great Hall" | Nixon Library, NARA, Commons, news archives | 2 uses (C5S110, C5S121 crop) |
| N06 | ❌ | Kissinger boarding / aboard a plane, 1971 | 1971 | 120 (03) | "Kissinger aboard plane 1971" "Kissinger Air Force One" | Nixon Library, NARA |  |
| N07 | ✅ | Richard Nixon official portrait (1971) → `assets/c5/photos/nixon_official_portrait_nara530679.jpg` | 1971 | 045, 049, 078, 119 (02/03) | "Richard Nixon presidential portrait 1971" | Commons (PD, White House) | cut-out; crops for D11/D02 circles |
| N08 | 🔁 | Nixon–Zhou Enlai handshake at Beijing airport, Feb 1972 → `assets/c5/photos/nixons_exit_af1_peking_1972.jpg, nixon_zhou_toast_1972.jpg` | 1972 | 094 (03) | "Nixon Zhou Enlai handshake 1972" | Commons / NARA (PD White House, Oliver Atkins / Byron Schumaker) |  |
| N09 | ✅ | Nixon & Khrushchev "Kitchen Debate", Moscow 1959 → `assets/c5/photos/kitchen_debate_1959.jpg` | 1959 | 077 (02) | "Kitchen Debate 1959 Nixon Khrushchev" | LOC U.S. News & World Report collection (PD) via Commons; Erwitt photo = fair use |  |
| N10 | ✅ | William P. Rogers, Secretary of State, portrait → `assets/c5/photos/rogers_secretary_of_state_portrait.jpg` | 1969–73 | 048 (02) | "William P. Rogers Secretary of State portrait" | Commons (PD State Dept) | no name text on screen |
| N11 | 🔁 | Tiananmen Gate with Mao portrait, 1960s–70s, ≥3000 px (for 2.5D) → `assets/c5/photos/tiananmen_mao_portrait_gatetower_modern.jpg (modern) + footage/china_1967_tiananmen_gate_mao_portrait.mp4` | 1960s–70s | 037 (01) | "Tiananmen 1970s Mao portrait" "Tiananmen gate 1967" | Commons, archive.org, news archives (fair use) | 2.5D layers 🛠 (sky / roof / portrait / crowd) |
| N12 | 🔁 | Mao Zedong colour portrait (official painting or 1960s poster) → `reuse assets/c3/photos/mao_tse_tung_portrait.jpg, assets/c6/photos/mao_portrait_tiananmen_gate.jpg` | 1960s | 061, 102, 103 (02/03) | "Mao Zedong official portrait painting" "Mao portrait 1967 poster" | Commons, chineseposters.net (IISH/Landsberger, credit) | lightly muted; crops for the split screen |
| N13 | 🔁 | Chiang Kai-shek colour official portrait → `assets/c5/photos/chiang_kaishek_official_portrait.jpg (B&W)` | 1950s–60s | 035, 102, 103 (01/03) | "Chiang Kai-shek official portrait colour" | Commons (ROC gov work, PD in Taiwan), Academia Historica | also used in split screen |
| N14 | ❌ | Chiang Kai-shek, late 1960s / early 1970s photo | 1969–72 | 072 (02) | "Chiang Kai-shek 1971" "蔣中正 1971" | Commons, Academia Historica, CNA (fair use) |  |
| N15 | ✅ | Eisenhower and Chiang Kai-shek in Taipei, June 1960 → `assets/c5/photos/eisenhower_chiang_taipei_1960-06-18.jpg; colour alt assets/c3/photos/eisenhower_chiang_soong_taipei_1960_colour.jpg` | 1960 | 074 (02) | "Eisenhower Chiang Kai-shek Taipei 1960" | Commons (PD US gov), Eisenhower Library, NARA |  |
| N16 | ✅ | George H.W. Bush as US Ambassador to the UN (1971), portrait → `assets/c6/photos/bush_george_un_us_desk_1971_nara186386.jpg; N16b colour assets/c5/photos/bush_un_swearing_in_1971_nara194352.jpg` | 1971 | 112, 117, 118, 119, 121 (03) | "George H. W. Bush UN ambassador 1971" | Bush Library, UN Photo (fair use), Commons | N16b = a COLOUR photo for the §10.7 reveal (1971–72; colour preferred) |
| N17 | ❌ | Bush with delegates at the UN, Oct 1971 | Oct 1971 | 116 (03) | "George Bush United Nations 1971 delegates" "UN General Assembly October 1971 Bush" | UN Photo (fair use, credit), Bush Library, AP-free news archives |  |
| N18 | ❌ | Jeff Bezos colour photo | 2010s | 106 (03) | "Jeff Bezos" (Commons CC BY/BY-SA) | Commons (e.g. Steve Jurvetson CC BY 2.0) | CC credit on screen |
| N19 | ✅ | Zhou Enlai portrait → `assets/c5/photos/zhou_enlai_1972.jpg (699 px), zhou_enlai_signing_rijks.jpg` | 1970s | 059 (02) | "Zhou Enlai 1971 portrait" | Commons (PD), NARA |  |
| N20 | ❌ | Fred Terman lecturing / at a lectern (1950s–60s) | 1950s–60s | 030 (01) | "Frederick Terman lecture" "Terman Stanford 1960s" | Stanford University Archives (fair use), Commons, example-docs/sources | fallback E05 with a lectern cut-out |
| N21 | ✅ | Red Guards rally stills (backup for N63) → `assets/c5/photos/red_guards_tiananmen_1966.jpg (890 px card)` | 1966–67 | 039 (01) | "Red Guards 1966 rally Tiananmen" | Commons, news archives (fair use) |  |
| N22 | ❌ | Intellectual persecuted in a struggle session, placard on chest | 1966–68 | 040 (01) | "struggle session 1966 placard" "Cultural Revolution intellectual paraded" | Li Zhensheng (Red-Color News Soldier — fair use, credit), Commons | respectful crop; no gore |
| N23 | ✅ | Cultural Revolution propaganda poster (colour) → `assets/c5/posters/cr_poster_raise_great_red_flag.jpg, cr_poster_mao_featuring.jpg` | 1966–70 | 038 (01) | "Cultural Revolution poster 1967" | chineseposters.net (IISH / Landsberger, credit), Commons | keeps its red (red = PRC), lightly muted |
| N24 | ❌ | 1960s Chinese school textbook page | 1960s | 041 (01) | "1960s Chinese textbook" "语文课本 1964" | archive.org texts, Commons | native size as a card |
| N25 | ❌ | US military in Taiwan, 1960s (USTDC / joint exercise) | 1955–70 | 084 (03) | "United States Taiwan Defense Command" "US Navy Taiwan 1960s" | Commons / NARA / US Navy (PD) |  |

## 2. Products, industry, places, objects (photos / footage / props)
| ID | status | subject / path | era | scenes (segment) | search terms | best sources | notes |
|---|---|---|---|---|---|---|---|
| N30 | ❌ | Macro of a vintage "MADE IN TAIWAN" label/stamp (toy, radio, umbrella) | 1960s–80s | 003 (01) | "made in Taiwan label vintage" "Made in Taiwan Republic of China stamp" | Commons, Flickr CC, eBay/press photos (fair use, no watermarks) | ≥2400 px, shallow DoF ideal |
| N31 | ❌ | a–e: period photos/ads of Taiwan-made Christmas lights, transistor radio, washing machine, umbrella, textiles | 1960s–70s | 004 (01) | "Taiwan Christmas lights 1970s" "Made in Taiwan transistor radio" "Tatung washing machine ad" "Taiwan umbrella factory 1970s" "Taiwan textile mill 1960s" | archive.org (Free China Review, Taiwan Trade), Commons, Taiwan national archives (fair use) | five cards for the D07 collage |
| N32 | ❌ | US-aid "clasped hands" emblem in Taiwan (on flour sacks / signs), 1950s | 1950s | 006 (01) | "US aid Taiwan 1950s flour sack" "美援 麵粉袋" | Commons, Taiwan archives, news (fair use) | halftone card |
| N33 | ✅ | a–c: 1960s electronics magazine covers / US tech ads (GI, TI, RCA era) → `assets/c5/documents/electronics_magazine_1965-04-19_cover.jpg + electronics_1965-04-19_rca_*_ad.jpg` | 1964–70 | 007 (01) | "Electronics magazine 1966 cover" "Texas Instruments ad 1967" "RCA ad 1968" | worldradiohistory.com (scans), archive.org | tinted panels |
| N34 | 🔁 | a–c: logos — General Instrument, Texas Instruments, RCA (period versions) → `assets/c5/logos/rca_wordmark_1968.svg, general_instrument_wordmark_1990s.png (TI missing)` | 1960s–70s | 008, 009, 010 (01) | media-use resolve --type logo | `npx --yes hyperframes@0.8.217 media-use resolve --type logo --entity "Texas Instruments"` etc.; Commons SVG | bone/ink, no brand colours (palette rule) |
| N35 | ❌ | a–c: GI, TI, RCA annual-report covers (late 1960s) | 1966–70 | 008 (01) | "Texas Instruments annual report 1968" "RCA annual report 1969" "General Instrument annual report" | archive.org, worldradiohistory.com, company archives | fallback: magazine ads with logos |
| N36 | ❌ | RCA colour TV set (c. 1970–71), front view, screen keyed transparent + `_screen.json` | 1970–71 | 067 (02) | "RCA color TV 1971" "RCA XL-100" | Commons, museum photos, eBay/auction photos (fair use) | new set (never the intro's) |
| N37 | ❌ | 1960s transistor / IC catalogue or datasheet page (TI or Fairchild) | 1960s | 012 (01) | "Texas Instruments transistor catalog 1965" "Fairchild integrated circuit catalog 1967" | bitsavers.org, worldradiohistory.com, archive.org | body text must contain "transistors" / "integrated circuits" |
| N38 | ✅ | Taiwan electronics assembly-line footage (women assembling radios/TVs/parts) → `assets/c5/footage/taiwan_1974_*.mp4 (⚠ Periscope watermark caption — lead decides)` | 1965–78 | 011, 014, 018 (01) | "Taiwan electronics factory 1970s film" "Kaohsiung export processing zone 1970" | archive.org (USIS/NARA films), Taiwan Film & Audiovisual Institute (fair use), news reels without watermarks | 2 clips (C5S011, C5S014); no readable non-Taiwan signage |
| N39 | ❌ | Kaohsiung / Nanzih EPZ aerial (1970s) — also halftone base for D01 | 1970s | 005, 020 (01) | "Kaohsiung Export Processing Zone aerial 1970s" "加工出口區 空照" | Taiwan national archives, Commons, MOEA EPZ history pages (fair use) |  |
| N40 | ✅ | Close-up of a Taiwanese worker's hands assembling electronics → `assets/c5/footage/taiwan_1974_pcb_hands_soldering_worker.mp4 (⚠ watermark)` | 1970s | 017, 018 (01) | "Taiwan electronics worker 1970s hands assembly" | Commons, Taiwan archives, news (fair use) |  |
| N41 | ❌ | US semiconductor fab footage, 1960s (Fairchild / TI Dallas / Motorola) | 1960s | 013 (01) | "Fairchild Semiconductor film 1960s" "Texas Instruments 1960s plant film" | archive.org (Prelinger, company films), Computer History Museum (fair use) | fallback E10 🔁 |
| N42 | ❌ | Grand Hotel Taipei postcard / photo (1960s–70s) | 1960s–70s | 022 (01) | "Grand Hotel Taipei 1970s postcard" "圓山大飯店 1970" | Commons, postcard archives (fair use) | a conference venue (not named on screen) |
| N43 | ❌ | Technical-conference audience / lecture hall (1960s–70s) | 1960s–70s | 024, 030 (01) | "engineering conference 1970 audience" "IEEE conference 1968 audience" | Commons (NASA/NIST PD), archives | 2 uses (C5S024, C5S030 crop) |
| N44 | 🔁 | Pakistan International Airlines Boeing 707 (1960s–70s), ≥3000 px for 2.5D → `assets/c5/photos/pia_boeing_707_*.jpg (≤1280 px, not 2.5D size)` | 1965–75 | 058, 064 (02) | "PIA Boeing 707 1970" "Pakistan International Boeing 707" | Commons (CC BY-SA, credit), airliners.net (fair use) | 2 uses (2.5D + board card) |
| N45 | 🔁 | US aircraft carrier of the Seventh Fleet, 1950s (top-down/aerial) → `assets/c5/footage/navy_1950s_carrier_*.mp4 (film, ⚠ watermark)` | 1954–58 | 092 (03) | "USS Essex 1958 Taiwan Strait" "Seventh Fleet carrier 1955 aerial" | Commons / NHHC / NARA (US Navy, PD) | for the curve cut: round-ish deck shape → dot |
| N46 | 🔁 | UN General Assembly hall, ≥3000 px (for 2.5D) → `assets/c5/photos/un_general_assembly_hall_modern_3.jpg (modern, CC BY-SA)` | 1960s–70s (or modern if needed) | 109 (03) | "United Nations General Assembly hall 1971" | UN Photo (fair use, credit), Commons (CC) | 2.5D layers 🛠 |
| N47 | ✅ | UN General Assembly in session (1960s) → `assets/c3/footage/newsreel_1960_un_general_assembly_*.mp4 (reuse)` | 1960s | 098 (03) | "UN General Assembly 1965 session" | UN Photo (fair use), Commons |  |
| N48 | ❌ | UN "CHINA" delegation nameplate (1960s–71) | ≤1971 | 099 (03) | "China nameplate United Nations 1971" | UN Photo (fair use), news archives | cut-out |
| N49 | ❌ | UN delegates listening (Oct 1971) | 1971 | 118 (03) | "UN General Assembly October 1971 delegates" | UN Photo (fair use) |  |
| N50 | ✅ | UN General Assembly electronic voting board (1970s) → `assets/c6/footage/un1971_vote_board_closeup.mp4 (reuse)` | 1970s | 124 (03) | "UN General Assembly voting board 1971" | UN Photo (fair use), Commons | kept blurred — no tally readable (result is in c6) |
| N51 | ✅ | Henry Fuseli, The Nightmare (1781) → `assets/c5/paintings/fuseli_the_nightmare_1781_dia.jpg` | 1781 | 096 (03) | "Fuseli The Nightmare" | Commons (PD, Detroit Institute of Arts) |  |
| N52 | ❌ | Circus tightrope-walker poster (lithograph) | 1890s–1930s | 105 (03) | "tightrope walker circus poster lithograph" | LOC Strobridge circus posters via Commons (PD) |  |
| N53 | ❌ | Balance-scale engraving | 19th c. | 108 (03) | "balance scale engraving" | Commons / Old Book Illustrations (PD) | cut-out |
| N54 | ❌ | Vintage wall clock (cut-out) | 1960s–70s | 069 (02) | "vintage wall clock 1960s" | Commons CC0/Pexels-like CC0 | hands as separate layers 🛠 |

## 3. Documents, newspapers, archival film, old maps
| ID | status | subject / path | era | scenes (segment) | search terms | best sources | notes |
|---|---|---|---|---|---|---|---|
| N55 | ✅ | Kissinger–Zhou memorandum of conversation, 9–11 July 1971 (declassified) → `assets/c5/documents/kissinger_zhou_memcon_1971-07-09_title.jpg, _p2, _p5_taiwan (bboxes in SOURCES)` | 1971 | 060 (02) | "Kissinger Zhou Enlai memcon July 1971" | National Security Archive EBB 66 (nsarchive2.gwu.edu, PD US gov), FRUS 1969–76 vol. XVII | 2 pages |
| N56 | ❌ | 1971 news clipping: Kissinger ill / resting in Pakistan (stomach) | Jul 1971 | 051, 055, 057, 065 (02) | "Kissinger ill Pakistan July 1971 newspaper" | archive.org newspapers, Google News Archive (free), Chronicling America (no), fair use | fallback: G06 typeset clipping (no real masthead). N56b = a busy 1971 front page for the focal call-out |
| N57 | ❌ | Department of State Bulletin, Aug 1971 — US statement on Chinese representation in the UN | 1971 | 113 (03) | "Department of State Bulletin August 1971 Chinese representation" | HathiTrust / archive.org (PD US gov) | highlight the representation lines |
| N58 | ❌ | Mutual Defense Treaty US–Republic of China (1954), text page | 1954 | 075 (02) | "Sino-American Mutual Defense Treaty text 1954" | NARA / UST treaty series on archive.org (PD) |  |
| N59 | ❌ | 1958 newspaper front page on the Quemoy (Kinmen) shelling | 1958 | 088 (03) | "Quemoy shelled 1958 front page" | archive.org newspapers, Google News Archive (fair use) | body highlight on Formosa/Taiwan |
| N60 | 🔁 | 1950s newspaper explainer map of the Formosa Strait (Quemoy / Matsu) → `assets/c5/footage/navy_1950s_seventh_fleet_formosa_strait_map.mp4 (⚠ watermark)` | 1954–58 | 091 (03) | "Quemoy Matsu map 1955 newspaper" | archive.org, Life magazine (Google Books, fair use), Commons | card, native size |
| N61 | ❌ | Nixon TV address, 15 July 1971 (announcement of the China trip) footage | Jul 1971 | 067, 068 (02) | "Nixon July 15 1971 announcement China trip" | Nixon Library (PD), archive.org, NARA | 6–10 s, no burned-in captions/logos |
| N62 | ❌ | Nixon arrives in Beijing, Feb 1972 (steps off the plane / handshake) footage | 1972 | 071 (02) | "Nixon arrives Beijing 1972 film" "USIA Nixon China visit" | archive.org (USIA/NARA, PD), Nixon Library |  |
| N63 | ✅ | Red Guards rally footage, 1966–67 → `assets/c5/footage/china_1967_*.mp4 (⚠ watermark)` | 1966–67 | 039 (01) | "Red Guards 1966 newsreel" "Cultural Revolution newsreel" | archive.org (Universal Newsreel PD, others fair use), British Pathé only if no watermark | 6–10 s |
| N64 | ❌ | (optional) 1958 Quemoy shelling newsreel | 1958 | — | "Universal Newsreel Quemoy 1958" | archive.org (Universal Newsreel, PD) | B-roll option for C5S089–090 |
| N65 | ❌ | Old city map of Peking / Beijing (pre-1950) | 1900–1940s | 070 (02) | "Peking city map 1914" "Map of Peking 1936" | Commons (PD), LOC maps via Commons, Perry–Castañeda | D09 look |
| N66 | ❌ | Vintage colour atlas sheet(s): Asia (Pakistan → China) + Pacific, 1950s–60s | 1950s–60s | 025, 059, 066 (01/02) | "atlas Asia 1955 map colour" "National Geographic Asia map 1959" | map kit (`assets/maps/kit/`), Commons, archive.org atlases, David Rumsey (fair use now allowed) | tilted D10 plane |
| N67 | ❌ | (optional) Sino-Soviet border clash 1969 (Zhenbao/Damansky) photo | 1969 | 079 (02) | "Zhenbao Island 1969" "Damansky incident" | Commons (fair use) | small card |

## 4. Maps (map kit — `assets/maps/kit/`)
| ID | status | subject / path | era | scenes (segment) | search terms | best sources | notes |
|---|---|---|---|---|---|---|---|
| M01 | ❌ | East Asia hi-res shaded relief / atlas (China, Taiwan, Korea, Japan, USSR edge) — map kit | — | 025, 036, 053, 085 (01/02/03) | Natural Earth II 21600 px class | `assets/maps/kit/` (map-kit agent) | ≥ 8k px across the region; JSON lon/lat→px |
| M02 | ❌ | Satellite globe render path Washington → Pakistan (s02 quality) | — | 050 (02) | Blue Marble / Esri World Imagery | map kit | credit Esri/NASA |
| M03 | ❌ | South Asia satellite (Pakistan, India, Himalaya, west China) | — | 052, 053 (02) | Esri World Imagery / Sentinel-2 cloudless | map kit | credit |
| M04 | ❌ | Taiwan Strait satellite (Fujian coast, Kinmen, Matsu, Taiwan) ≥ 8k px | — | 089, 090, 092, 093 (03) | Esri / Sentinel-2 cloudless (s2cloudless) | map kit | credit; labels Kinmen / Matsu small |
| M05 | ❌ | World at night (NASA Black Marble) | 2016 | 063 (02) | "Black Marble 2016" | NASA Earth Observatory (PD) |  |
| M06 | ❌ | Muted beige world map (R11 look) with USSR / China shapes as SVG paths | — | 078, 079 (02) | Natural Earth admin-0 + beige grade | map kit (vector + texture) | antimeridian fix (MANUAL §4.2) |
| M07 | ❌ | Taiwan hi-res relief + celadon mask (kit version) | — | 010, 021, 034 (01) | Natural Earth II / SRTM hillshade | map kit | until delivered: intro `taiwan_relief_grey.jpg` + E14 (Krish dislikes the flat grey — upgrade) |

## 5. To make (🛠 typeset / graphics / layers)
| ID | status | subject / path | era | scenes (segment) | search terms | best sources | notes |
|---|---|---|---|---|---|---|---|
| G01 | 🛠 | Smile-curve value-chain SVG (ink line, shaded ends, celadon dot) | — | 016, 019 (01) |  | own | NEW ref |
| G02 | 🛠 | Manufacturing ladder (4 rungs, labels only from the narration) | — | 015 (01) |  | own | D04 variation |
| G03 | 🛠 | Conference programme (typeset, narrated topics legible, rest blurred) + badge card | — | 023, 030 (01) |  | own | no real event name |
| G04 | 🛠 | Public-schedule list (typeset rows "public event", blurred details) | — | 056, 065 (02) |  | own | D12 variation |
| G05 | 🛠 | Diplomatic cable / teletype on yellow flimsy (typeset, narrated words only) | — | 070 (02) |  | own | no seals, no real letterhead |
| G06 | 🛠 | Typeset newspaper column/page (Crimson Pro / Haskoy), generic masthead-free — for §10.7 (Bezos, Bush) + fallback clippings | — | 051, 055, 057, 065, 066, 106, 117, 122 (02/03) |  | own | never a real masthead/date |
| G07 | 🛠 | Meeting agenda list (typeset; only "Taiwan" legible) | — | 086 (03) |  | own |  |
| G08 | 🛠 | Two-seat UN diagram (seat icons, Taiwan celadon, China red) | — | 100, 101, 114 (03) |  | own | shared motif c5s03 |
| G09 | 🛠 | D15 relationship circles (Terman/government; US–USSR–China triangle; Taiwan–US–CCP row) | — | 081, 082, 107 (02/03) |  | own | same circle size/ring style as intro D15 |
| G10 | 🛠 | D11 Sankey flows (Kissinger → president/policy; US ↔ China) | — | — |  | own |  |
| G11 | 🛠 | D06 UN semicircle of member dots | — | 097, 111, 123 (03) |  | own | match c3/c4 UN vote motif (lead to confirm) |
| G12 | 🛠 | D02 two portrait-topped columns | — | 119 (03) |  | own |  |
| G13 | 🛠 | Halftone flags: US (navy), PRC (red), ROC (ink — its own red/blue fields would break the code) | — | 044, 062, 076, 081, 104 (02/03) |  | own (flag SVGs from Commons → halftone) | single-colour halftone prints in the code colour |
| G14 | 🛠 | Engineer pictogram (isotype) + population dots | — | 026 (01) |  | own from E16 |  |
| G15 | 🛠 | Tear-off calendar (blank pages) + October 1971 desk calendar page | — | 022, 115 (01/03) |  | own | real dates for Oct 1971 only |
| G16 | 🛠 | Org chart (President / National Security Advisor / Secretary of State) | — | 047 (02) |  | own |  |
| G17 | 🛠 | VHS-rewind look (tracking lines, reversed clips) | — | 087 (03) |  | own (ffmpeg reverse of earlier shots) |  |
| G18 | 🛠 | Patient chart card (typeset, only "sick") | — | 054 (02) |  | own |  |

## 6. Existing in the repo
| ID | status | subject / path | era | scenes (segment) | search terms | best sources | notes |
|---|---|---|---|---|---|---|---|
| E01 | ✅ | `assets/intro/photos/nanzih_epz_ose_factory.jpg` — Nanzih EPZ factory | 1970s–80s | 001 (01) |  | (intro) | c4 may use it too — same grade |
| E02 | ✅ | `assets/intro/screens/tatung_tv20cge_frame.png` + `_screen.json` (Tatung TV, screen keyed) | 1970s | 014 (01) |  | (intro) | intro IS060 used it — use a different angle/crop + shelf plate |
| E03 | ✅ | `assets/intro/screens/sony_trinitron_kv1320_frame.png` + `_screen.json` | 1970s | 087 (03) |  | (intro) | rewind gag |
| E04 | ✅ | `assets/intro/footage/jet_707_takeoff_hongkong.mp4` (Pan Am 707) | 1960s | 027 (01) |  | (intro) | use the landing/pass section |
| E05 | ✅ | `assets/archival/collage/terman_frederick_1955.jpg` (+ c1 Terman assets in templates/full-edit, example-docs/sources) | 1955 | 028, 029, 031, 032, 033 (01) |  | (10-min edit) | check c1 usage; c5 = callback |
| E06 | ✅ | `assets/intro/photos/silicon_valley_aerial.jpg` | modern | 033 (01) |  | (intro) | sepia grade |
| E07 | ✅ | `assets/intro/footage/taiwan_1960_taipei_boulevard_high_angle.mp4` | 1960 | 042 (01) |  | (intro) |  |
| E08 | ✅ | `assets/intro/footage/taiwan_1960_taipei_north_gate_traffic.mp4` | 1960 | 095 (03) |  | (intro) | + fog from `assets/maps/clouds` |
| E09 | ✅ | `assets/intro/footage/taiwan_1960_presidential_office_taipei.mp4` (still frame) | 1960 | 031, 032 (01) |  | (intro) | Taiwanese government circle |
| E10 | 🔁 | `assets/intro/footage/fab_engineers_furnaces.mp4` / `diffusion_furnace_glow.mp4` | 1960s | 013 (01) |  | (intro) | only as substitute for N41 — confirm in intro SOURCES that the plant is in the US |
| E11 | ✅ | `assets/intro/photos/stone_wall_texture_cc0.jpg` | — | 076 (02) |  | (intro) | wall blocks |
| E12 | ✅ | `assets/textures/cork_01.jpg` (CC BY — credit) | — | 064, 065 (02) |  | Texturelabs/… | R9 board |
| E13 | ✅ | papers: `assets/textures/paper_*_hires.jpg` (graph, lined, stained, torn, cream, fiber), `assets/intro/papers/ke1960_*_hires.jpg`, `ledger_specimen_p38.jpg` (card only) | — | 002, 004, 005, 006, 012, 015, 016, 018, 044 (01/02) |  | (kit) | never upscale small scans; two layers top ~90 % |
| E14 | ✅ | `assets/intro/maps/taiwan_celadon_fill.png`, `assets/intro/made/taiwan_celadon_wash.png` | — | 010, 024, 069, 084 (01/02/03) |  | (intro) | celadon Taiwan motif (until the map kit has its own) |
| E15 | 🔁 | `assets/intro/footage/taiwan_1960_factory_yard_workers.mp4` | 1960 | 011 (01) |  | (intro) | substitute only if N38 fails (it shows steel bars, not electronics) |
| E16 | ✅ | `assets/icons/graduate*.svg` | — | 026 (01) |  | (kit) | base for the engineer pictogram G14 |

## 7. Priorities (biggest needs first)
1. **Kissinger / Nixon / Bush / Mao / Chiang photo set** (N01–N17) — 30+ scenes depend on them; presidential libraries + NARA + Commons are PD.
2. **Archival footage**: Nixon's 15 July 1971 address (N61), Nixon arriving in Beijing 1972 (N62), Red Guards (N63), Taiwan electronics
   assembly 1965–78 (N38), US 1960s fab (N41).
3. **True documents**: Kissinger–Zhou memcon (N55, PD), State Dept Bulletin Aug 1971 (N57, PD), Mutual Defense Treaty (N58, PD), 1971
   "Kissinger ill" clipping (N56), 1958 Quemoy front page (N59), 1950s Strait explainer map (N60).
4. **Map kit** M01–M07 (Taiwan Strait satellite, South Asia satellite, East Asia relief, beige world map, night globe).
5. **2.5D sources ≥ 3000 px**: Tiananmen + Mao portrait (N11), PIA 707 (N44), UN GA hall (N46).
6. **UN Photo set** (N46–N50): hall, session, CHINA nameplate, delegates, voting board.
7. **Screens**: RCA 1970–71 colour TV keyed (N36).
8. **Made-in-Taiwan products** (N30, N31a–e, N32) and the GI/TI/RCA logos + reports (N34, N35).

Counts: 104 IDs — 14 ✅, 2 🔁, 70 ❌, 18 🛠.

