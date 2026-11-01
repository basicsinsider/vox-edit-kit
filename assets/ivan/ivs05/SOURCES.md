# assets/ivan/ivs05 — sources (segment ivs05, master 594.35–675.59)

All files looked at before use (contact sheets / stills). Footage trimmed with ffmpeg: h264, 24 fps, no audio.

## footage/
| file | subject | source | licence / credit | size |
|---|---|---|---|---|
| bbc_mamon_walk.mp4 | Polish journalist Marcin Mamoń walking in a street (close, sunglasses) | BBC World Service "Shadowmen" (`assets/ivan/footage/raw/bbc_shadowmen.mp4`) 00:01:15.4–00:01:20.6 | © BBC, fair use (Krish approved) — on screen "Video: BBC World Service" | 1920×1080, 5.2 s |
| bbc_ivan_airfield_dusk.mp4 | Ivan's own footage: anonymous silhouette watching lights of a military airfield at dusk ("launching 'birds' to destroy strategic aircraft") | BBC "Shadowmen" 00:00:44.4–00:00:49.2, cropped 1538×865+160+95 (removes BBC logo + burned subtitle), scaled 1600×900 | © BBC, fair use — "Video: BBC World Service" | 1600×900, 4.8 s |
| sbu_bomber_strike.mp4 | Operation Spiderweb FPV drone hits a bomber on an apron, fireball | `assets/ivan/footage/raw/src_fast.mp4` (SBU compilation) 00:00:30.8–00:00:34.6 | © Security Service of Ukraine, fair use — "Video: Security Service of Ukraine (SBU)" | 1920×1080, 3.8 s |
| bbc_yelabuga_strike.mp4 | Drone hits the Yelabuga (Tatarstan) plant, fireball (BBC split-screen, right panel only; keeps BBC's "Yelabuga, Tatarstan" label) | BBC "Shadowmen" 01:02:43.8–01:02:49.0, crop 1080×704+692+262, scaled 1290×840 | © Ostorozhno Novosti (location verified by Reuters) via BBC, fair use — "Video: Ostorozhno Novosti via BBC World Service" | 1290×840, 5.2 s |

## photos/
| file | subject | source | licence / credit | size |
|---|---|---|---|---|
| tu95_voronezh_2014.jpg | Two Tu-95 strategic bombers in flight, Voronezh air show, 2014-09-20 | https://commons.wikimedia.org/wiki/File:Tu-95_at_an_Air_show_in_Voronezh_2014.jpg (1920 thumb) | CC BY-SA 4.0, Роман Дергунов (Roman Dergunov) — on screen "Photo: Roman Dergunov, CC BY-SA 4.0" | 1920×1424 |
| shahed136_rendering.png | Shahed-136 one-way attack drone, 3D rendering (transparent) | https://commons.wikimedia.org/wiki/File:Shahed_136_rendering.png (1280 thumb) | CC BY 4.0, Idmental (Sketchfab) — on screen "Render: Idmental, CC BY 4.0" | 1280×654 |

## derived/ (made by `project/ivan/gen/ivs05_assets.py`)
| file | what | from | credit |
|---|---|---|---|
| russia_wide_night.jpg | lon 15–120°E, lat 28–82°N at 32 px/deg (x=(lon−15)·32, y=(82−lat)·32) | `assets/maps/kit/world_night.jpg` | Relief: AWS Terrain Tiles (PD); Natural Earth (PD) |
| ee_night_crop.jpg | lon 28–56°E, lat 46–60°N, half res (x=(lon−28)·73.884, y=(60−lat)·120) | `assets/maps/kit/eastern_europe_night.jpg` | same |
| ivs05_map_paths.json | Russia / Ukraine (+Crimea in the EE crop) outlines in both crops' pixel spaces | kit `world_overlay.svg`, `eastern_europe_overlay.svg` (Natural Earth, PD) | — |
| alabuga_sez_esri_z16.jpg | Alabuga special economic zone (Yelabuga, Tatarstan) incl. the drone-plant area; Esri World Imagery z16 mosaic (51.985–52.095°E, 55.812–55.862°N), cropped + scaled to 1920×1080 | Esri World Imagery tiles (`tools/map_tiles.py`) | "Imagery: Esri, Maxar, Earthstar Geographics" |

Also used (shared, not copied): `assets/facecam/ivan_facecam_master.mp4` (Krish), `assets/ivan/motifs/grey_man.svg`, `assets/textures/*`
(cork_01: "Cork texture: Trougnouf (Benoit Brummer), CC BY 4.0").
