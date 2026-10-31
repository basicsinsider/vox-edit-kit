# ASSETS NEEDED — CHUNK c3 (local 0.00–602.02)

Deduplicated list for `EDIT_NOTES.md` (IDs `E..` = exists in the repo, `N..` = still needed / to make). Snapshot 2026-10-31,
before gatherers start (c3 gatherer pass 2026-10-31: see `assets/c3/ASSETS.md`) — **gatherers: flip ❌ → ✅/🔁 with the path when you land a file**, store c3 media under
`assets/c3/<type>/` and log every file in that folder's `SOURCES.md` (subject, URL, licence or "© owner, fair use", author, date,
size; bboxes for documents/headlines).

Rules (§10.9): **true images first** — copyrighted press photos, newspapers, posters, book pages and logos are allowed as fair
use (documentary commentary, transformed, credited: 13 px on-screen credit where customary + SOURCES.md). Never log in, never pay,
never strip watermarks. Reject wrong subject/era, < 1600 px long side for full-frame (≥ 3000 px for 2.5D). Re-use allowed when the
story needs it (usage column). Maps from the map kit (never flat grey/beige relief), papers from Texturelabs `_hires`.
Search: `python3 tools/find_media.py commons-html|archive|archive-texts|files "<query>"`; Commons downloads via
`tools/commons_thumb.sh`; LOC via tile.loc.gov (MANUAL §8.1); blocked sites → `requests/fetch.json` (§8.2).

Legend: ✅ exists · 🔁 substitute · ❌ to find · 🛠 to make.

## 1. Existing assets reused (✅)
| ID | status | path | what | scenes | uses |
|---|---|---|---|---|---|
| E01 | ✅ | `assets/intro/footage/wafer_die_pattern_macro.mp4` | IC die-pattern macro (archival) | C3S001 | 1 |
| E03 | ✅ | `assets/intro/screens/ibm_5154_monitor_frame.png (+ _screen.json)` | IBM 5154 monitor, screen keyed | C3S003 | 1 |
| E04 | ✅ | `assets/intro/screens/sony_trinitron_kv1320_frame.png (+ _screen.json)` | Sony Trinitron KV-1320 | C3S018 | 1 |
| E05 | ✅ | `assets/intro/screens/tatung_tv20cge_frame.png (+ _screen.json)` | Tatung TV20 (Taiwanese maker) | C3S092 | 1 |
| E07 | ✅ | `assets/intro/paintings/stanford_peninsula_map.jpg` | pictorial Stanford/peninsula map (colour) | C3S004 | 1 |
| E08 | ✅ | `assets/intro/photos/silicon_valley_aerial.jpg` | Silicon Valley aerial | C3S006, C3S019 | 2 |
| E09 | ✅ | `assets/intro/photos/silicon_valley_2014.jpg` | modern Silicon Valley (for halftone cut-out) | C3S029 | 1 |
| E10 | ✅ | `assets/archival/collage/terman_frederick_1955.jpg` | Frederick Terman portrait | C3S019, C3S026, C3S036, C3S038, C3S040 | 5 |
| E11 | ✅ | `assets/archival/hoover/hoover_presidential_portrait_photo_NARA.jpg` | Hoover photo (fallback for N18) | C3S030 | 1 |
| E13 | ✅ | `assets/archival/hoover/stanford_inner_quad_west_entrance_c1900.jpg (+ main quad panoramas)` | Stanford quad | C3S019, C3S027, C3S031, C3S035 | 4 |
| E14 | ✅ | `assets/archival/hp/hewlett_and_packard_together_1960.jpg` | Hewlett & Packard 1960 | C3S019, C3S035 | 2 |
| E15 | ✅ | `assets/archival/hp/hewlett_william_c1962.jpg` | Bill Hewlett c1962 | C3S027, C3S042 | 2 |
| E16 | ✅ | `assets/archival/hp/layers/garage.png (+ backdrop/house/hedge)` | HP garage | C3S019, C3S027 | 2 |
| E17 | ✅ | `assets/maps/old/rand_mcnally_railroad_map_us_1920.jpg (+ .json)` | vintage US railroad map (D10 tilt) | C3S015 | 1 |
| E18 | ✅ | `assets/maps/us_basemap.jpg + us_overlay.json (s02)` | US satellite basemap — fallback for the kit | C3S008, C3S011 | 2 |
| E19 | ✅ | `assets/intro/maps/taiwan_relief_grey.jpg + taiwan_mask.png / intro/derived/intro03/taiwan_mask_alpha.png` | Taiwan relief + mask (fallback; prefer kit hi-res) | C3S037, C3S044 | 2 |
| E20 | ✅ | `assets/intro/maps/formosa_1943_japanese_aviation_map.jpg (+ .json)` | 1943 Japanese map of Formosa | C3S045 | 1 |
| E21 | ✅ | `assets/intro/maps/pacific_basemap.jpg / pacific_relief_grey_2850.jpg (+ .json)` | Pacific basemap (fallback; prefer kit) | C3S037, C3S046 | 2 |
| E22 | ✅ | `assets/intro/maps/world_basemap_desat.jpg + world_countries.svg` | world ghost map / country paths | C3S067, C3S094 | 2 |
| E23 | ✅ | `assets/intro/footage/taiwan_1960_*.mp4 (presidential_office_taipei, taipei_north_gate_traffic, taipei_boulevard_high_angle)` | Taiwan 1960 footage | C3S050, C3S058, C3S076, C3S092 | 4 |
| E24 | ✅ | `assets/intro/paintings/taiwan_birdseye_1935.jpg` | Taiwan bird's-eye painting 1935 | C3S075 | 1 |
| E26 | ✅ | `assets/intro/footage/rotary_phone_1970_dialing.mp4` | rotary phone dialing | C3S102 | 1 |
| E27 | ✅ | `assets/textures/paper_{lined,graph,blueprint,stained}_01_hires.jpg + assets/intro/papers/ke1960_* + ledger_*` | papers (hires grounds; K+E/ledger only as cards) | C3S007, C3S021, C3S036, C3S051, C3S103 | 5 |
| E28 | ✅ | `assets/textures/cork_01.jpg` | cork board (CC BY — credit) | C3S019 | 1 |
| E34 | ✅ | `assets/icons/graduate*.svg, pin_*.svg` | pictograms + pins | C3S024 | 1 |
| E37 | ✅ | `assets/maps/us_states.geojson / us_beige.svg (shapes only)` | US state shapes for fills | C3S009 | 1 |
| E38 | ✅ | `assets/maps/clouds/` | s02 cloud layers | C3S048 | 1 |

## 2. People & portraits
| ID | status | need (subject, size) | era | search terms | best sources (licence) | scenes | uses |
|---|---|---|---|---|---|---|---|
| N07 | ✅ `assets/c3/photos/field_david_dudley_brady_handy.jpg` | David Dudley Field portrait (Brady-Handy studio) | 1860s–70s | "David Dudley Field" Brady | Commons / LOC (PD) via tile.loc.gov | C3S013 | 1 |
| N12 | ❌ | "Traitorous eight" / Fairchild founders group photo (Wayne F. Miller, 1960) ≥ 2400 px + 2.5D layer set (backdrop, rows, fg, layout.json) | 1960 | "Fairchild founders 1960 Wayne Miller" | Magnum / CHM press (© fair use, credit) | C3S020 | 1 |
| N16 | ❌ | Terman c.1960–65 photo (provost era) | 1960s | "Frederick Terman provost 1965" | Stanford News Service / Stanford Archives (© fair use); fallback E10 | C3S026 | 1 |
| N18 | ✅ `assets/c3/paintings/hoover_herbert_tarbell_npg_painting.jpg` | Herbert Hoover portrait **painting** (colour) | 1931/1956 | "Herbert Hoover portrait Douglas Chandor", "Elmer Wesley Greene Hoover" | National Portrait Gallery open access (CC0) / White House Historical (PD/fair use); fallback E11 | C3S030 | 1 |
| N24 | ❌ | Terman teaching / Stanford radio (communications) lab, 1930s | 1930s | "Terman Stanford radio laboratory 1930s", "Terman lecture" | Stanford Archives (© fair use), Commons; fallback E10 | C3S038 | 1 |
| N25 | ❌ | Pan Wen-Yuan 潘文淵 portrait — young (1930s–40s) if any, else the best available | 1930s–70s | "潘文淵", "Pan Wen-Yuan", "Wen-Yuan Pan RCA" | zh.wikipedia / ITRI history pages / RCA Engineer (© fair use) | C3S039, C3S040 | 2 |
| N25b | ❌ | Pan Wen-Yuan later photo (1970s Taiwan / ITRI era) | 1970s | "潘文淵 工研院", "潘文淵 1974" | ITRI (工研院) history, Taiwanese press archives (© fair use) | C3S044, C3S046 | 2 |
| N37 | ✅ `assets/c3/photos/cairo_1943_*.jpg + footage/cairo_1943_*.mp4 (no 2.5D layers yet)` | Cairo Conference 1943 photo (Chiang, Madame Chiang, FDR, Churchill) ≥ 3000 px + 2.5D layers | 1943 | "Cairo Conference 1943 Chiang Roosevelt Churchill" | Commons (PD US Army) | C3S064 | 1 |
| N39 | ✅ `assets/c3/photos/fdr_portrait_perskie_1944.png` | Franklin D. Roosevelt portrait (colour painting or photo) | 1940s | "Franklin Roosevelt portrait Salisbury", "FDR official portrait" | Commons / FDR Library (PD) | C3S066 | 1 |
| N45 | ✅ `assets/c3/photos/chiang_kai_shek_portrait.jpg, mao_*.jpg (Mao small)` | Chiang Kai-shek portrait + Mao Zedong portrait, ≥ 1600 px | 1940s | "Chiang Kai-shek portrait 1940s", "Mao Zedong 1940s portrait" | Commons (PD) | C3S072 | 1 |
| N47 | 🔁 `assets/c3/footage/newsreel_1959_chiang_and_madame_chiang_walk.mp4` | Chiang in Taipei 1950 (resuming presidency / Presidential Office) | 1950 | "蔣中正 復行視事 1950", "Chiang Kai-shek Taipei 1950" | Commons (PD-ROC) | C3S076 | 1 |
| N50 | ✅ `assets/c3/photos/eisenhower_*_1960*.jpg (small)` | Eisenhower & Chiang Kai-shek, Taipei, June 1960 | 1960 | "Eisenhower Chiang Kai-shek Taipei 1960" | Commons (PD US gov) | C3S079 | 1 |
| N53 | ✅ `assets/c3/photos/mao_stalin_moscow_1949_dec21.jpg` | Stalin & Mao, Moscow, Dec 1949 | 1949 | "Mao Stalin 1949 Moscow" | Commons (PD-Russia / fair use) | C3S086 | 1 |

## 3. Logos, flags, UI
| ID | status | need (subject, size) | era | search terms | best sources (licence) | scenes | uses |
|---|---|---|---|---|---|---|---|
| N11 | ❌ | HBO *Silicon Valley* title card / still (16:9) | 2014–19 | "Silicon Valley HBO title card" | press kit / Commons logo (© HBO — fair use, credited) | C3S018 | 1 |
| N13 | 🔁 `assets/c3/logos/fairchild_semiconductor_logo.png (later logo)` | Fairchild Semiconductor logo (1957 "F" mark) | 1957 | "Fairchild Semiconductor logo" | Commons SVG | C3S020, C3S021 | 2 |
| N14 | ✅ `assets/c3/logos/intel_logo_1968_2006.png` | Intel 1968 "dropped-e" logo | 1968 | "Intel logo 1968" | Commons SVG (PD-textlogo) | C3S021 | 1 |
| N40 | 🔁 `assets/c3/flags/ (US 48/50, France, USSR, ROC, PRC; UK/Russia/Japan missing)` | Flags (SVG): US 48-star & 50-star, UK, France, USSR, Russia, ROC (1928–), + generic flags for dominoes/isotype | — | Commons flag SVGs | Commons (PD) | C3S063, C3S065, C3S079, C3S090, C3S095, C3S100, C3S110, C3S111 | 8 |
| N03 | 🛠 | 🛠 Searching Lessons player UI (waveform, progress bar 4:26:14 = intro IS062 motif) + video-card style | — | — | make (typeset); reuse intro03 progress-bar code | C3S003, C3S004 | 2 |
| N63 | 🛠 | 🛠 CSS/3D domino tiles with flag faces | — | — | make (uses N40) | C3S100 | 1 |

## 4. Documents, newspapers, books, papers
| ID | status | need (subject, size) | era | search terms | best sources (licence) | scenes | uses |
|---|---|---|---|---|---|---|---|
| N04 | ❌ | Periodic table plate from a 1940s–50s chemistry textbook (Si visible), ≥ 2400 px | 1940s–50s | "periodic table 1950 textbook", "periodic chart of the elements 1940" | archive.org texts (PD), Commons, Science History Institute (CC) | C3S005 | 1 |
| N06 | 🛠 | 🛠 typeset employment agreement with a non-compete clause (generic, no logos/signatures) — 2 variants (C3S010 clean, C3S017 typed form) | — | — | make on paper_lined/cream | C3S010, C3S017 | 2 |
| N08 | ✅ `assets/c3/documents/field_ny_civil_code_1865_*.jpg` | Field's *Draft of a Civil Code for the State of New York* (1865) — cover + title page scans | 1865 | "Draft of a civil code for the state of New York 1865" | archive.org texts, HathiTrust full view (PD) | C3S012, C3S013, C3S014, C3S015 | 4 |
| N10 | 🔁 `assets/c3/documents/cal_civil_code_s1673_page246_hart1892.jpg (1892 ed., same text)` | California Civil Code 1872 — title page + the page with §1673 ("…restrained from exercising a lawful profession…") | 1872 | "Civil Code of the State of California 1872 section 1673" | archive.org, HathiTrust, Google Books scans (PD) | C3S016 | 1 |
| N15 | ❌ | Reference only: 1969 SEMI "Silicon Valley Genealogy" (Fairchildren) chart | 1969 | "Silicon Valley genealogy chart 1969 Fairchildren" | CHM / SEMI (© — reference, rebuilt in our style, not shown) | C3S021 | 1 |
| N23 | ❌ | Vintage recipe index card scan (ruled, blank or typed) | 1940s–60s | "vintage recipe card blank", "index card 1950s" | Commons / archive.org (PD); else 🛠 typed on paper_lined_01 | C3S035, C3S047 | 2 |
| N26 | ❌ | First pages of Proc. IRE papers by F. E. Terman & W. Y. Pan (late 1930s) | 1937–41 | "Terman Pan Proceedings of the IRE", "W. Y. Pan Terman 1939" | IEEE Xplore first-page previews (© fair use), archive.org Proceedings of the IRE scans | C3S041 | 1 |
| N27 | ❌ | (optional) a Hewlett–Pan paper page; else typeset bibliography card | 1930s | "Hewlett Pan Stanford 1939" | IEEE Xplore / Stanford theses; fallback 🛠 | optional | 0 |
| N28 | ❌ | Pan's Stanford PhD dissertation (1940) title page | 1940 | "Pan Wen-Yuan Stanford dissertation 1940" | Stanford SearchWorks / ProQuest preview (© fair use); fallback 🛠 typeset (no fake seal) | C3S044 | 1 |
| N29 | 🔁 `assets/c3/newspapers/university_daily_kansan_1971-10-26_frontpage.jpg` | NYT front page 26 Oct 1971 "U.N. Seats Peking and Expels Taipei" ≥ 3000 px | 1971 | "New York Times October 26 1971 front page UN seats Peking" | archive scans / newspapers on archive.org / Commons (© NYT, fair use) — never log in to TimesMachine; alt: another US paper of 26 Oct 1971 | C3S052, C3S057 | 2 |
| N31 | ❌ | Central Daily News 中央日報 26 Oct 1971 front page | 1971 | "中央日報 1971年10月26日", "中華民國退出聯合國 報紙" | Taiwanese archives / Commons (© fair use) | C3S055 | 1 |
| N38 | ✅ `assets/c3/newspapers/japan_surrender_1945_slnsw.jpg, shen_bao_1945-08-16_*.jpg` | A newspaper front page of Aug 1945 "war ends / Japan surrenders" | 1945 | "Japan surrenders front page August 1945" | archive.org / Commons (PD or © fair use) | C3S065 | 1 |
| N42 | 🔁 `assets/c3/footage/newsreel_1945_un_charter_book.mp4` | UN Charter 1945 — signature page and Art. 23 text page | 1945 | "Charter of the United Nations 1945 original"  | archive.org / UN Treaty Collection scans (PD) | C3S069 | 1 |
| N61 | 🔁 `assets/c3/posters/nara_515905_united_nations_security_council.jpg` | 1950s UN explainer booklet (cover + organs chart page) | 1950s | "The United Nations how it works booklet 1950" | archive.org texts (PD/fair use) | C3S109 | 1 |

## 5. Photos: places, objects, events
| ID | status | need (subject, size) | era | search terms | best sources (licence) | scenes | uses |
|---|---|---|---|---|---|---|---|
| N01 | ✅ `assets/c3/photos/fairchild_micrologic_series_01.jpg` | Integrated-circuit photo: early Fairchild planar IC / Micrologic (1960–61), die + package, ≥ 2000 px | 1960s | "Fairchild Micrologic", "first planar integrated circuit", "Fairchild IC 1961" | Commons (CHM/Intel/Fairchild uploads); Computer History Museum press (© fair use) | C3S002, C3S006 | 2 |
| N17 | ❌ | Stanford Industrial Park / Santa Clara Valley aerial, 1960s, ≥ 2400 px | 1955–68 | "Stanford Industrial Park aerial 1960", "Santa Clara Valley aerial 1965 orchards" | Stanford Research Park / Stanford Archives (© fair use), Commons, Calisphere | C3S027, C3S028, C3S035 | 3 |
| N19 | ✅ `assets/c3/photos/hoover_tower_01.jpg (source only, layers not cut)` | Hoover Tower photo ≥ 3000 px for 2.5D (tower vs sky, trees fg) + layer set | modern | "Hoover Tower Stanford" | Commons (CC BY-SA — credit) | C3S032 | 1 |
| N20 | ❌ | Hoover Institution Library & Archives reading room / stacks photo | modern | "Hoover Institution Library and Archives reading room" | Hoover Institution press (© fair use) / Commons | C3S033 | 1 |
| N30 | ❌ | UN 1971: PRC delegation takes China's seat (Nov 1971, "CHINA" placard) / GA vote-board photo for Res. 2758 | 1971 | "PRC delegation UN November 1971 Qiao Guanhua", "Resolution 2758 vote board" | UN Photo (© UN, fair use), Commons | C3S053 | 1 |
| N32 | ✅ `assets/c3/newspapers/scmp_1971-10-27_roc_walkout_photo.png` | ROC delegation (Chow Shu-kai 周書楷) walking out of the GA, 25 Oct 1971 — photo or footage | 1971 | "周書楷 退出聯合國", "ROC delegation walks out UN 1971" | UN Photo / AP (© fair use), archive.org newsreels | C3S056 | 1 |
| N36 | ✅ `assets/c3/photos/ww2_sc*.jpg (2 of 3)` | US Army Signal Corps photos: Chinese & American soldiers together (×3) | 1943–45 | "Chinese soldiers American advisers 1944 Signal Corps", "Ledo Road Chinese troops" | Commons / NARA (PD) | C3S062 | 1 |
| N41 | 🔁 `assets/c3/footage/newsreel_1945_un_charter_signing_san_francisco.mp4 (not Koo)` | China (Wellington Koo) signing the UN Charter, San Francisco, June 1945 | 1945 | "Wellington Koo signs UN Charter 1945" | UN Photo (© fair use) / Commons | C3S069 | 1 |
| N43 | 🔁 `assets/c3/posters/nara_515905_united_nations_security_council.jpg; c4 photo un_security_council_1962` | Security Council session 1946–50s with the "CHINA" placard | 1946–50s | "Security Council 1946 China delegate", "UN Security Council 1950 Tsiang" | UN Photo (© fair use), Commons | C3S070 | 1 |
| N46 | ❌ | 1949 ROC retreat: ships/troops arriving at Keelung/Kaohsiung | 1949 | "1949 retreat to Taiwan Keelung", "國軍撤退來台 1949" | Commons / Taiwan archives (PD-Taiwan / fair use); fallback keelung_port_cc0.jpg | C3S075 | 1 |
| N51 | ❌ | Treaty of Taipei (Japan–ROC) signing, 28 Apr 1952 | 1952 | "Treaty of Taipei signing 1952", "中日和約 簽字" | Commons (PD-ROC) | C3S083 | 1 |
| N52 | ❌ | UN Headquarters 1950s with the flag row (ROC flag visible) | 1950s | "United Nations headquarters 1952 flags" | Commons / UN Photo (fair use) | C3S084 | 1 |
| N58 | ❌ | US–ROC Mutual Defense Treaty signing, Dec 1954 (Dulles & George Yeh) | 1954 | "Sino-American Mutual Defense Treaty signing 1954" | Commons (PD) | C3S101 | 1 |
| N60 | ✅ `assets/c3/footage/newsreel_1960_un_general_assembly_*.mp4` | UN General Assembly hall 1960s photo (new members / flag raising 1960) | 1960s | "UN General Assembly 1960 new members" | UN Photo (© fair use) / Commons | C3S108 | 1 |
| N62 | 🔁 `assets/c4/photos/un_security_council_1962_stevenson_chamber.jpg` | UN Security Council chamber photo (horseshoe table) | any | "UN Security Council chamber" | Commons (CC BY-SA — credit) / UN Photo | C3S110 | 1 |
| N22 | ❌ | Pull-down projection screen + projector photo, screen keyed transparent + `_screen.json` | 1950s–60s | "projection screen 1960s classroom", "16mm projector screen" | Commons / archive.org (PD/CC); key with tools as for intro screens | C3S034 | 1 |

## 6. Paintings & posters (§10.5)
| ID | status | need (subject, size) | era | search terms | best sources (licence) | scenes | uses |
|---|---|---|---|---|---|---|---|
| N34 | ❌ | 1940s anti-Japanese war woodcut/poster (CCP-era art) | 1938–45 | "Yan'an woodcut anti-Japanese", "抗战木刻" | Commons / museums (© fair use) | C3S060 | 1 |
| N35 | ✅ `assets/c3/posters/owi_this_man_is_your_friend_chinese_1942.jpg` | OWI poster "This man is your FRIEND — Chinese — He fights for freedom" (1942) | 1942 | "This man is your friend Chinese he fights for freedom poster" | NARA / Commons (PD) | C3S061 | 1 |
| N48 | 🔁 `assets/c3/posters/roc_1960s_slogan_recover_mainland.jpg (small)` | 1950s ROC "反攻大陸" (recover the mainland) poster | 1950s | "反攻大陸 海報 1950" | Commons / Taiwanese museums (© fair use) | C3S077 | 1 |
| N54 | 🔁 `assets/c3/posters/nara_5730089_supporting_stalin.jpg (verify)` | 1950s Sino-Soviet friendship poster (handshake) | 1950s | "Sino-Soviet friendship poster 1950" | Commons / poster archives (© fair use) | C3S087 | 1 |

## 7. Footage
| ID | status | need (subject, size) | era | search terms | best sources (licence) | scenes | uses |
|---|---|---|---|---|---|---|---|
| N33 | ✅ `assets/c3/footage/newsreel_1945_pacific_*.mp4` | WWII Pacific newsreel (2 shots: general title + carrier/air combat) | 1942–45 | "Universal Newsreel Pacific 1944", "Pacific war newsreel" | archive.org (PD US gov / Universal Newsreels) | C3S059, C3S082 | 2 |
| N44 | ✅ `assets/c3/footage/newsreel_1949_*.mp4` | Chinese Civil War newsreel 1946–49 (troops, refugees, 1949) | 1946–49 | "Chinese civil war newsreel 1949", "Reds take Shanghai Universal Newsreel" | archive.org (PD) | C3S071 | 1 |
| N55 | ✅ `assets/c3/footage/newsreel_1961_*.mp4` | Soviet May Day / Red Square parade footage, 1950s | 1950s | "Red Square parade 1950s newsreel" | archive.org (PD) | C3S096 | 1 |
| N56 | ✅ `assets/c3/footage/newsreel_1956_us_navy_*.mp4` | 1950s US Navy fleet steaming footage | 1950s | "US Navy fleet 1950s newsreel" | archive.org / NARA (PD) | C3S096 | 1 |
| N57 | 🔁 `assets/c3/footage/prelinger_1953_raytheon_*.mp4` | 1950s US factory / assembly line footage | 1950s | "Detroit assembly line 1950s Prelinger" | archive.org Prelinger (PD) | C3S097 | 1 |
| N59 | ✅ `assets/c3/footage/newsreel_1957_ghana_*.mp4` | Ghana independence, 6 Mar 1957 (Nkrumah) footage or photo | 1957 | "Ghana independence 1957 Nkrumah newsreel" | archive.org newsreels / Commons (PD/fair use) | C3S106 | 1 |
| N21 | ❌ | Hoover Institution video still (e.g. Uncommon Knowledge / Battlegrounds set) | modern | "Uncommon Knowledge Hoover Institution" | Hoover press stills (© fair use) — YouTube blocked from cloud: fetch relay if needed | C3S034 | 1 |

## 8. Maps & data
| ID | status | need (subject, size) | era | search terms | best sources (licence) | scenes | uses |
|---|---|---|---|---|---|---|---|
| N05 | ❌ | **Map kit** `assets/maps/kit/`: US night satellite (s02 grade), vintage colour atlas plates (US, world, Europe–Asia, Africa), East Asia + China shaded relief (Natural Earth II class), Taiwan + strait sharp satellite, Pacific relief, Africa relief; each with lon/lat→px json | — | Natural Earth II 21600 px; NASA Blue Marble NG; Esri World Imagery (© credit); 1940s–50s atlas plates | Natural Earth (PD), NASA (PD), Esri (credit), Commons/LOC atlas scans — gatherer C builds once for c1–c6 | C3S008, C3S009, C3S011, C3S023, C3S037, C3S046, C3S048, C3S049, C3S054, C3S067, C3S068, C3S073, C3S074, C3S078, C3S080, C3S088, C3S098, C3S104 | 18 |
| N09 | ❌ | 1860s New York map (city or state), colour or engraved, ≥ 3000 px | 1860s | "map of New York 1865", "Colton New York 1860s" | LOC maps via Commons (PD) | C3S013, C3S014 | 2 |
| N68 | ❌ | Vintage colour world/atlas plates (1940s–50s) ≥ 4000 px — part of the map kit | 1940s–50s | "world political map 1950 atlas plate" | Commons / LOC / archive.org (PD); David Rumsey only if CC BY | C3S049, C3S097, C3S105 | 3 |
| N02 | ✅ `assets/c3/maps/black_marble_2012_*_globe.jpg` | NASA Black Marble — Earth at night (globe or flat), ≥ 3840 px | 2012/2016 | "Black Marble 2016" | NASA Earth Observatory / Visible Earth (PD) | C3S002 | 1 |
| N49 | ✅ `assets/c3/data/recognition.json` | Data: countries recognising ROC vs PRC by year (≈1950/1960/1969) → `assets/c3/data/recognition.json` | — | — | Wikipedia lists (BEATS §5) | C3S078, C3S081, C3S093 | 3 |
| N64 | ✅ `assets/c3/data/africa_independence.json` | Data: African independence / UN admission order → `assets/c3/data/africa_independence.json` | — | — | Wikipedia (BEATS §5) | C3S104, C3S107 | 2 |

## 9. Priorities for the gatherers (biggest needs first)
1. **Map kit N05/N68** (gatherer C) — 18 scenes depend on it (US night satellite, East Asia/China relief, Taiwan strait satellite,
   world night, Europe–Asia, Africa, vintage colour atlas plates). Fallbacks exist (E18, E21, E22, E19) but Krish rejected flat
   relief — build the kit first; it serves c1–c6.
2. **1971 UN expulsion set** N29 (NYT front page), N30 (PRC seated), N31 (Central Daily News), N32 (ROC walk-out) — the chunk's
   emotional turn (C3S052–C3S057).
3. **California law documents** N08 (Field 1865 draft), N10 (Cal. Civil Code 1872 §1673), N07 (Field portrait), N09 (1860s NY map)
   — all PD on archive.org/HathiTrust/LOC (C3S012–C3S016).
4. **Pan Wen-Yuan** N25/N25b/N26/N28 — few photos exist; accept the best available, duotone; typeset fallbacks for documents.
5. **2.5D sources ≥ 3000 px** N12 (Fairchild founders), N19 (Hoover Tower), N37 (Cairo 1943) + layer sets with `layout.json`.
6. **WWII / civil war / Cold War archive** N33, N35, N36, N44, N45, N50, N53–N58 (archive.org newsreels + Commons PD).
7. Posters/paintings N18, N34, N35, N48, N54 (colour beats B/W, §10.5).
8. Data JSONs N49 + N64 (Wikipedia lists, dated) for the map fills.

## 10. Make (🛠) list
N03 player UI + video cards · N06 contracts ×2 · N23 recipe card (if no scan) · N63 dominoes · seat horseshoe / GA semicircle (D06
code) · isotype country grid (D03) · Sankey (D11) · dark list (D12) · timelines (C3S043, C3S057–058) · blueprint plan (C3S036) ·
typed memo (C3S103) · history-book page (C3S060) — all in our fonts/palette on real paper textures; no fake seals, signatures or
real mastheads.

