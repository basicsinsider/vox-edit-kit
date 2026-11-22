# assets/cartels/cts03 — sources (cts03 editor, 2026-11-22)
All files looked at before use. News photos = © owner, fair use (MANUAL §10.9). Derived files are made by
`project/cartels/gen/cts03_assets.py` (maps, Treasury crop) or a PIL crop noted below.

| file | subject | URL | licence | author / owner | date | size |
|---|---|---|---|---|---|---|
| photos/src_eluniversal_alfredo_2008.jpg | Alfredo Beltrán Leyva "El Mochomo" presented under escort after his arrest (Jan 2008); escorts in balaclavas | og:image of https://www.eluniversal.com.mx/tendencias/el-era-alfredo-beltran-leyva-el-papa-de-el-mochomito-presunto-autor-del-ataque-a-federales-en-sinaloa/ (resizer SBB53E6BYFGRDBYWSULDKPDX54, width=1920) | © El Universal (agency photo), fair use | El Universal | 2008 photo | 1920×1276 |
| photos/src_expansion_arturo.jpg | composite: LEFT = Arturo Beltrán Leyva (the widely published file photo); right half (Genaro García Luna) NOT used | og:image of https://politica.expansion.mx/mexico/2023/01/26/quien-fue-arturo-beltran-leyva-como-murio | © Expansión, fair use | Expansión Política | 2023 article | 1800×1200 |
| photos/src_vanguardia_hector_chapo.gif | composite: LEFT = Héctor Beltrán Leyva (PGR photo after his Oct 2014 arrest), RIGHT = Joaquín "El Chapo" Guzmán (PGR photo, Feb 2014 arrest) | og:image of https://vanguardia.com.mx/articulo/hector-beltran-leyva-el-hombre-que-metio-el-chapo-en-el-negocio-de-las-drogas-y-se | © Vanguardia / PGR, fair use | Vanguardia (MX) | 2018 article | 730×500 |
| photos/fentanyl_2mg_pencil_dea.jpg | 2 mg of fentanyl on a pencil tip (DEA illustration of a lethal dose) | https://commons.wikimedia.org/wiki/File:2_milligrams_of_fentanyl_on_pencil_tip._A_lethal_dose_for_most_people._US_Drug_Enforcement_Administration.jpg (1920 px thumb) | Public domain (US Gov, DEA) | Drug Enforcement Administration | — | 1920×1167 |
| derived/id_arturo.jpg | crop (60,0,960,1200) of src_expansion_arturo → 600×800 | — | as source | — | — | 600×800 |
| derived/id_alfredo.jpg | crop (730,0,1180,600) of src_eluniversal_alfredo_2008 → 600×800 | — | as source | — | — | 600×800 |
| derived/id_hector.jpg | crop (0,8,366,496) of src_vanguardia_hector_chapo (Héctor) → 600×800 (upscaled ×1.6, used ≤ 230 px wide, duotone) | — | as source | — | — | 600×800 |
| derived/id_chapo.jpg | crop (366,8,730,494) of src_vanguardia_hector_chapo (El Chapo) → 600×800 (used ≤ 254 px wide) | — | as source | — | — | 600×800 |
| derived/id_isidro.jpg | crop of assets/cartels/people/meza_fbi_photo_1.jpg (FBI wanted-poster photo of Fausto Isidro Meza Flores) | see people/ | US Gov (FBI) | FBI | — | 600×800 |
| derived/mx_relief_dark.jpg | kit `mexico_relief.jpg` crop (0,0,3400,3000), dark-slate grade | assets/maps/kit (AWS Terrain Tiles, Natural Earth) | public domain | map kit | 2026-11-22 | 3400×3000 |
| derived/son_sat_warm.jpg | kit `mexico_sat.jpg` crop (500,300,2300,1700), saturation 0.55 | assets/maps/kit (Esri, Maxar, Earthstar Geographics) | © Esri et al., credited on screen | map kit | 2026-11-22 | 1800×1400 |
| derived/treasury_page.jpg | crop (400,0,3440,2700) of assets/cartels/docs/d10_treasury_ofac_2013_full.jpg — Treasury press release tg1824 "Treasury Designates Additional Sinaloa-Based Drug Trafficking Organization", 17 Jan 2013. Key bboxes (crop px): date 640–835 × 1012–1042; "announced the designation" 1799,1198,402×44; "of the Meza Flores Drug Trafficking Organization" 639,1255,698×44; "OFAC is designating … the leader of the Meza Flores" 639,2327,1573×44 | https://home.treasury.gov/news/press-releases/tg1824 | US Gov work (public domain) | U.S. Department of the Treasury | 2013-01-17 | 3040×2700 |
Map vectors for the scenes (Sonora/Sinaloa/Arizona/border/Mex 15 north from the kit overlays, northern Sinaloa region transformed from
`sinaloa_overlay.svg`, boat waypoints checked against `mexico_landmask.png`) → `project/cartels/gen/cts03_mapdata.json` (inlined by build_cts03.py).

FIX ROUND 1 (#11, whole-head circle portraits, made by `project/cartels/gen/cts03_circles.py`, 480×480; margins where the photo is tighter
than the square = edge-extended + blurred copy of the same photo, background only):
| derived/circ_arturo.jpg | square crop (12,0,136,124) of people/arturo_beltranleyva_1.jpg (PGR wanted photo, en.wikipedia, fair use) | — | as source | — | — | 480×480 |
| derived/circ_alfredo.jpg | crop (670,0,1210,560) of photos/src_eluniversal_alfredo_2008.jpg in a 600-px square | — | as source | — | — | 480×480 |
| derived/circ_hector.jpg | crop (16,0,300,400) of people/hector_beltranleyva_mugshot_3.jpg (PGR booking photo) in a 430-px square | — | as source | — | — | 480×480 |
| derived/circ_isidro.jpg | crop (0,0,1515,1900) of people/meza_fbi_photo_hires_2.jpg (FBI) in a 1960-px square | — | US Gov (FBI) | FBI | — | 480×480 |
