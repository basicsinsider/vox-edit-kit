# assets/intro/derived/maps — map-kit rasters re-projected into the intro's existing pixel spaces (2026-10-31)

Built by `project/intro/gen/intro_maps_kit.py` from `assets/maps/kit/` (see its SOURCES.md for upstream sources/licences).
Each file is a pure resample of a kit raster into the pixel space the intro compositions already used, so every route, fill,
pin and OSM overlay path stays valid; only the `<img src>` changed.

| file | made from | pixel space (old asset it replaces) | used in | on-screen credit |
|---|---|---|---|---|
| pacific_atlas_8550.jpg | kit world_atlas.jpg, 110E→60W, 56→8N, 45 px/deg | 1.5× of x=(lon-110)*30, y=(56-lat)*30 (pacific_beige / pacific_relief_grey_2850) | IS006, IS028 | Relief: AWS Terrain Tiles (PD) · Natural Earth |
| pacific_inset_taiwan_116_127E_19_29N.jpg | kit east_asia_atlas.jpg native crop (128×150 px/deg) | inset at left 180, top 810 (330×300) of the IS006 space | IS006 close-up | same |
| world_night_7680.jpg | kit world_night.jpg resized | 2× of x=(lon+180)*10.667 (world_desat_3840) | IS016 | same |
| world_night_4320.jpg | kit world_night.jpg resized | x=(lon+180)*12 (derived/intro03/world_dark) | IS055/056 | same |
| world_night_inset_110_134E_10_34N.jpg | kit world_night.jpg native crop | insets in the IS016 / IS055 cameras around Taiwan | IS016, IS055 | same |
| world_atlas_6480.jpg | kit world_atlas.jpg resized | 1.5× of x=(lon+180)*12 (derived/intro03/world_beige) | IS048, IS049 | same |
| taiwan_{atlas,night,sat}_2480.jpg | kit taiwan_*.jpg, affine resample (sea colour beyond the kit's 0.1° tighter bounds) | x=(lon-119.2)*800, y=(25.5-lat)*800 (taiwan_relief_grey) | IS050 atlas · IS035/IS045 night · IS053 sat | sat: Imagery: Esri, Maxar, Earthstar Geographics |
| hsinchu_s2_esri_z17_4660.jpg | kit aerial_hsinchu_park_z17.jpg (Esri z17, 1.08 m/px) feathered over EOX Sentinel-2 cloudless 2016 (graded to match) | 1.25× of the z15 Web-Mercator space of maps/hsinchu_s2cloudless2016 | IS053 | Imagery: Esri, Maxar, Earthstar Geographics · Sentinel-2 cloudless 2016 by EOX, CC BY 4.0 · © OpenStreetMap contributors |

Esri imagery: © Esri and its data providers — fair use per MANUAL §10.9, credited on screen.
