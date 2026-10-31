# ASSETS_B — chunk c4, gatherer B (footage + c4-specific maps), 2026-10-31

Full per-file log (source URL, in-point, licence, content): `assets/c4/footage/SOURCES.md`, `assets/c4/maps/SOURCES.md`.
All clips: h264, 24 fps, no audio, native resolution (no upscaling), 2.5–15 s, every clip checked on a contact sheet.
Total footage 75 clips / ~145 MB (largest file < 6 MB). Raw downloads stayed in /tmp (not in the repo).

## Footage — `assets/c4/footage/`
| id | files | subject | scenes | size / dur | licence |
|---|---|---|---|---|---|
| B-UN50 | `un_1950_security_council_{delegates_table,horseshoe,president_china_delegate,session,wide,chamber_high_wide}.mp4` | UN Security Council in session 1950 (horseshoe table; ROC delegate at the table) | C4S001–003, C4S006, C4S009 | 640×480, 3.6–12.5 s | Universal Newsreel (PD, NARA) |
| B-UN60 | `un_1960_general_assembly_{hall_wide,hall_wide_b,rostrum_wide,podium_wide,delegates,delegates_b,african_delegates}.mp4` | UN General Assembly hall, Sept 1960 (incl. newly admitted African delegations) | C4S004–005, C4S011–013, C4S020 | 640×480, 2.6–13 s | Universal Newsreel (PD) |
| B-FFC | `taiwan_1960_*.mp4` (29 clips) | *Taiwan: The Face of Free China* 1960 colour: rice transplanting (a/b), water buffalo (road / paddy wide), farmer buckets, farmhouse + haystacks, threshing, sugarcane, sugar mill, refinery towers/tanks, factory sheds, brickworks women, market stalls, school, campus cyclists, red-brick hall, Chiang Kai-shek portrait billboard, officials' ribbon ceremony, students writing, steam train, highway builders, street + movie posters, ROC flag, **painted map with Japanese flags popping onto Taiwan** | C4S028–029, 033–037, 046, 050–059, 063, 070–074, 086, 088–091, 094, 103 | 640×480, 4.5–18 s | CC0 (NARA) |
| B-FC59 | `formosa_1959_{harbour_bridge,city_street,department_store,ship_loading_export,aluminium_factory,chiang_kaishek_and_madame_chiang}.mp4` | Universal "Free China — 10 years on Formosa" 1959 | C4S056, C4S058, C4S085, C4S088, C4S094, C4S100 | 640×480, 2.6–9.4 s | Universal Newsreel (PD) |
| B-F61 | `formosa_1961_{chiang_kaishek_officials_steps,chiang_kaishek_uniform_podium,troops_march,plaza_formation,double_ten_formation,presidential_office_crowd}.mp4` | Double Ten 1961: Chiang Kai-shek in uniform, generals & officials, troops | C4S085–088 | 640×480, 2.6–11.3 s | Universal Newsreel (PD) |
| B-USN45 | `usn_1945_formosa_strike_{smoke_coast,plane_over_smoke,target_area,planes_over_smoke}.mp4`, `usn_1945_tbf_formation_to_formosa.mp4`, `usn_1945_formosa_{mountains_through_clouds,coast_aerial}.mp4` | USS Essex air strike on Formosa (Eiko airstrip), 4 Jan 1945 — smoke along the coast, planes over smoke (timecode cropped) | C4S042 | 1280×618, 5–14 s | PD (US Navy, NARA) |
| B-CN49 | `china_1949_{crowded_boat_harbour,crowds_fleeing_city,crowds_trucks_street,wharf_crowd_ships,refugees_boarding_ship,liner_harbour,mao_tiananmen_waving,tiananmen_crowd}.mp4` | 1949: Nationalist collapse / evacuation crowds and ships; Mao at Tiananmen, 1 Oct 1949 | C4S007, C4S010, C4S043, C4S045, C4S047 | 480×360, 3.5–8.5 s | © Wolper/Films Inc. 1972 — fair use, credit |
| B-TAC55 | `tachen_1955_{nationalist_troops_beach,sampan_causeway_troops,troops_boats_shore,crowded_ship_deck}.mp4` | Tachen Islands evacuation to Taiwan, Feb 1955 (real Nationalist evacuation; soft image) | C4S045 (substitute) | 1280×720 (soft), 10–12 s | PD (NARA) |
| B-SSA50 | `formosa_1950_songshan_airport_{plane_arrival,officers_greet}.mp4` | Songshan (Sung-shan) Airport, Taipei, Aug 1950; US + ROC officers | C4S069, C4S077, C4S087 | 720×480, 8.5–11 s | PD (US Army, NARA) |

Cautions: `china_1949_refugees_boarding_ship` second half shows Western evacuees (a nun) — use the first 2.5 s only or
skip; `un_1950_..._president_china_delegate` — the Chinese delegate is probably T. F. Tsiang but unconfirmed: don't name
him. `taiwan_1960_campus_students_bicycles` / `palm_boulevard_building` are not verified as NTU — don't label them "NTU".
Tachen (1955) and the 1972-documentary 1949 clips are true events but not "arriving in Taiwan 1949" — editors note it.

## Maps — `assets/c4/maps/`
| id | files | subject | scenes | size | licence |
|---|---|---|---|---|---|
| B-EPZ17 | `aerial_kaohsiung_epz_z17.jpg` + json | Esri z17 satellite, Zhongdao peninsula = Kaohsiung EPZ site, harbour around (Web-Mercator formula + EPZ pin in json) | C4S102, C4S099 | 4352×4864, 1.1 m/px | © Esri — fair use, on-screen credit "Esri, Maxar, Earthstar Geographics" |
| B-KH16 | `aerial_kaohsiung_harbour_z16.jpg` + json | whole Kaohsiung harbour (both entrances) | C4S102 wide, C4S100 | 4608×4608 | same |
| B-AFR | `africa_{night,atlas}.jpg`, `africa_landmask.png`, `africa_overlay.svg`, `africa.json` | Africa crop of the kit world relief + 92 Natural Earth country paths (`c-*`) + independence-year order (`independence_year_by_svg_id`; 1960 wave = 17 ids) | C4S013, 014, 016, 017 | 3413×3413 | PD |
| B-EUR | `eurasia_{night,atlas}.jpg`, `eurasia_landmask.png`, `eurasia_overlay.svg`, `eurasia.json` | Eurasia crop + modern paths + **1960 borders** (`h-ussr`, `h-east_germany`, `h-czechoslovakia`… `data-warsaw-pact="true"`; `warsaw_pact_1960_ids` in json) | C4S008, 066, 095 | 7145×3004 | PD + historical-basemaps (GPL-3.0 data) |
| (other gatherer) | `takao_1945_ams_city_plan.jpg`, `kaohsiung_harbour_epz_esri_z16.jpg` | AMS Takao city plan 1945; z16 harbour | C4S098, C4S102 | — | already logged |

Map notes: the Africa/Eurasia bases are straight crops of `assets/maps/kit/world_*` (45.5 px/°): sharp for a continent
frame at 1080p, soft past ~1.5× push — for East Asia close-ups switch to `kit/east_asia_*`. For "China red" use the
modern `c-china` path (the 1960 `h-china` excludes Tibet). 1960s Africa: merge Sudan+S. Sudan, Ethiopia+Eritrea,
Somalia+Somaliland (hint in africa.json).

## Still missing (my scope)
- **N32c** Kaohsiung EPZ assembly-line footage (women assembling electronics, 1966–70s): nothing on archive.org; YouTube
  blocked. Fallback: intro `fab_women_cleanroom_line.mp4` / `fab_hk_workers_microscope_rows_*.mp4` (Hong Kong, 1960s–70s)
  or `taiwan_1960_brickworks_workers.mp4`. Owner could fetch a Taiwan Film Institute / CNA clip via the relay (MANUAL §8.2).
- UN **vote** footage specifically on the China seat (1950s–1971): not found as a separate newsreel; the 1950 SC and 1960
  GA clips stand in. The 1971 vote (2758) exists only in UN Audiovisual Library (not reachable here).
- Combat Bulletin No. 41 (gov.dod.dimoc.20304, "Carrier force strikes Formosa", CC0) has a 640×480 MPEG2 of 1.6 GB —
  skipped for disk space (8 GB free); the NPC-7040 strike footage covers C4S042.
- 1949 arrival **in Keelung/Kaohsiung** footage (ships unloading in Taiwan): not found; substitutes above.
