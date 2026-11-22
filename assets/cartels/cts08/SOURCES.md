# assets/cartels/cts08 — sources (cts08 editor, 2026-11-22)

## photos/
| file | subject | source URL | licence | author | date | size |
|---|---|---|---|---|---|---|
| maduro_portrait.png | Nicolás Maduro, official portrait (sash, Venezuelan flag) | https://commons.wikimedia.org/wiki/File:Nicol%C3%A1s_Maduro_official_portrait.png | CC0 / Venezuelan public-sector work (per Commons) | Presidency of the Bolivarian Republic of Venezuela | 2013 | 1280×1658 (Commons 1280 px thumb) |
| mdc_brooklyn_a.jpg | Metropolitan Detention Center Brooklyn, exterior | https://commons.wikimedia.org/wiki/File:Metropolitan_Detention_Center_Brooklyn_November_2024.jpg | CC BY 4.0 (credit on screen) | Kidfly182 | 15 Nov 2024 | 3840×1727 |
| ven_su30_a.jpg | Venezuelan Air Force Sukhoi Su-30MK2 on the apron | https://commons.wikimedia.org/wiki/File:Sukhoi_Su-30MK2_de_Venezuela.jpg | CC BY-SA 4.0 (credit on screen) | Carlos E. Perez S.L | 30 Jul 2016 | 1920×1283 |
| ven_parade_b.jpg | Venezuelan army multiple rocket launchers on parade, Caracas | https://commons.wikimedia.org/wiki/File:Caracas,_Canciller_Ricardo_Pati%C3%B1o_particip%C3%B3_en_los_actos_de_conmemoraci%C3%B3n_de_la_muerte_de_Hugo_Ch%C3%A1vez_(12960876943).jpg | CC BY-SA 2.0 (credit on screen) | Cancillería del Ecuador | 5 Mar 2014 | 1920×1280 |

## derived/ (made by `project/cartels/gen/cts08_assets.py`)
| file | what | from |
|---|---|---|
| carib_night.jpg | night relief crop lon −125…−55 × lat 50…0 (3186×2276, 45.5111 px/deg; x=(lon+125)·45.5111, y=(50−lat)·45.5111) | kit `americas_night.jpg` (AWS Terrain Tiles PD + Natural Earth PD) |
| carib_borders.png, carib_venezuela.png, carib_usa.png, carib_mexico.png | country hairlines + fills in the same pixel space | kit `world_overlay.svg` (Natural Earth, PD) |
| sil_mexico.png, sil_usa.png | white+alpha silhouettes (balance-scale medallions) | kit `world_overlay.svg` |
| caracas_esri_z12.jpg | Caracas valley satellite inset (1340×771; pin at 715,338) | Esri World Imagery z12 tiles via `tools/map_tiles.py` (© Esri, Maxar — fair use, credited) |
| maduro_stairs_still.jpg | frame at 3.0 s of `assets/cartels/footage/x_maduro_stairs_stewart.mp4` | RPP pool aerial (see footage/SOURCES.md) |

## Shared files used that had NO SOURCES line yet (people/, news/ gatherers) — provenance checked here
- `assets/cartels/people/trump_sotu2026_arrive_1.png` = Commons "Donald Trump and Melania Trump heading to the U.S. Capitol for the 2026 State of the Union Address.png" (CC0, The White House, 2160×2700) — https://commons.wikimedia.org/wiki/File:Donald_Trump_and_Melania_Trump_heading_to_the_U.S._Capitol_for_the_2026_State_of_the_Union_Address.png (matched by title search + look; gatherer should log it).
- `assets/cartels/people/mencho_mugshot_2.jpg`, `meza_fbi_photo_1.jpg` — no SOURCES line found; used as known agency photos (SFPD mugshot / FBI poster). Lead: confirm provenance.
- `assets/cartels/news/front_pages/fp_2026-02-23_{reforma,jornada,milenio}.jpg` — no SOURCES.md in news/ yet; © the newspapers, fair use.
- Trump quote "We've also taken down one of the most sinister cartel kingpins of all." — ABC News live blog, SOTU 24 Feb 2026: https://abc7news.com/live-updates/state-union-2026-live-updates-president-donald-trump-address/18639619/entry/18647112 (checked 2026-11-22).
