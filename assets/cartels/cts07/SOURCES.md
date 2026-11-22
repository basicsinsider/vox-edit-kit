# assets/cartels/cts07 — sources (cts07 segment editor, 2026-11-22)
All files looked at before use. Commons files fetched as 1920/960 px thumbnails (`tools/commons_thumb.sh` / upload.wikimedia.org thumb URLs).

| file | subject | URL | licence | author | date | size |
|---|---|---|---|---|---|---|
| photos/reaper_flight_2.jpg | MQ-9 Reaper ("Predator B" on the fuselage) in flight over desert, **unarmed** (sensor ball under the nose, no weapons) | https://commons.wikimedia.org/wiki/File:MQ-9_Reaper_in_flight_2.jpg | public domain (US Air Force work; Commons lists CC0/PD) | U.S. Air Force | 2000s | 1920×1060 |
| photos/sheinbaum_2025_eneas.jpg | Claudia Sheinbaum, President of Mexico (portrait) | https://commons.wikimedia.org/wiki/File:Claudia_Sheinbaum_(2025)_(cropped).jpg | CC BY 4.0 — on-screen credit "Photo: Eneas / CC BY 4.0" | Eneas | 2025-08-14 | 1920×2563 |
| logos/cia_seal.png | Seal of the Central Intelligence Agency | https://commons.wikimedia.org/wiki/File:Seal_of_the_Central_Intelligence_Agency.svg | public domain (US Gov) | CIA | — | 960×960 |
| logos/dod_seal.png | Seal of the U.S. Department of Defense | https://commons.wikimedia.org/wiki/File:Seal_of_the_United_States_Department_of_Defense.svg | public domain (US Gov) | DoD | — | 960×960 |
| logos/fbi_seal.png | Seal of the Federal Bureau of Investigation | https://commons.wikimedia.org/wiki/File:Seal_of_the_Federal_Bureau_of_Investigation.svg | public domain (US Gov) | FBI | — | 960×989 |
| logos/dea_seal.png | Seal of the Drug Enforcement Administration | https://commons.wikimedia.org/wiki/File:Seal_of_the_United_States_Drug_Enforcement_Administration.svg | public domain (US Gov) | DEA | — | 960×961 |

Derived (made by `project/cartels/gen/cts07_assets.py` from the map kit, `assets/maps/kit/README.md` "Cartels project"):
| file | from | what |
|---|---|---|
| derived/a_border_night.jpg | mexico_night.jpg, kit px x 0–4200, y 0–2362 → 2880×1620 | US + northern Mexico, night relief (AWS Terrain Tiles / Natural Earth, PD) |
| derived/a_fill_us.png, a_fill_mx.png | mexico_overlay.svg `#c-united_states_of_america` / `#c-mexico` ∩ mexico_landmask | steel / olive fills in the same pixels |
| derived/b_arizona_satdesat.jpg | mexico_satdesat.jpg, kit px x 500–2900, y 150–1500 (native) | southern Arizona + Sonora (Esri, Maxar, Earthstar — credited on screen) |
| derived/b_fill_az.png | `#us-arizona` ∩ landmask | steel fill |
| derived/c_sierra_sat.jpg | sinaloa_sat.jpg, px x 2160–4027, y 260–1310 | Sierra Madre foothills (Esri imagery) for the drone-camera view (no place claimed on screen) |
| derived/d_davis_monthan.jpg | aerial_tucson_davis_monthan_z16.jpg, px x 0–4800, y 300–3000 → 3200×1800 | Davis-Monthan AFB (JIATF-CC HQ), Esri imagery |
| derived/paths.json | mexico_overlay.svg + mexico.json + the aerial json | border / Arizona paths (RDP-simplified), place pixels; inlined into compositions/cts07.html as `P7` |

Shared assets used (logged in their own folders): `assets/cartels/news/n03_twz_reapers.jpg` + `_k1.jpg` (TWZ, 18 Feb 2025),
`assets/cartels/news/n04b_arabnews_jiatf_calabrese.jpg` + `_k1.jpg` (Arab News / Reuters, Feb 2026),
`assets/cartels/people/calabrese_1.jpg` (Brig. Gen. Maurizio D. Calabrese official USAF portrait — af.mil biography photo, PD; the people
folder had NO SOURCES.md when this segment was built, so the credit "Photo: U.S. Air Force" rests on RESEARCH.md §1 Ch 4's af.mil bio link).
