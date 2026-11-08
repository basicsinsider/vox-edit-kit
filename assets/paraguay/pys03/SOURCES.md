# pys03 assets (segment editor pys03, 2026-11-08)

## photos/
| file | subject | source URL | licence / credit | size |
|---|---|---|---|---|
| moneylender_matsys_1514.jpg | Quentin Matsys, *The Moneylender and His Wife*, 1514 (Louvre) | https://commons.wikimedia.org/wiki/File:Massysm_Quentin_%E2%80%94_The_Moneylender_and_his_Wife_%E2%80%94_1514.jpg | public domain (CC0 on Commons) | 1280×1205 (Commons thumb) |
| asuncion_govt_bldgs_loc.jpg | "Paraguay, Asuncion. Govt. bldgs." — old glass-plate photo of the Palacio de López from the port (Library of Congress, LCCN 2016821420) | https://commons.wikimedia.org/wiki/File:Paraguay,_Ascuncion._Govt._bldgs._LCCN2016821420.jpg | public domain (no known restrictions, LOC) | 1920×1383 |
| soy_silos_paraguay.jpg | "SOJA Y SILOS EN PARAGUAY" — grain silos | https://commons.wikimedia.org/wiki/File:SOJA_Y_SILOS_EN_PARAGUAY.jpg | CC0 | 1920×1280 |
| rotary_press.jpg | "Euzkadi egunkariaren errotatiba 02" — newspaper rotary press (museum) | https://commons.wikimedia.org/wiki/File:Euzkadi_egunkariaren_errotatiba_02.jpg | CC BY-SA 4.0 (author per Commons page) | 1920×1080 |
| data_center.jpg | "BalticServers data center" | https://commons.wikimedia.org/wiki/File:BalticServers_data_center.jpg | CC BY-SA 3.0, BalticServers.com | 1920×1275 |

## derived/ (made by `project/paraguay/gen/pys03_assets.py` — re-run from the repo root)
| file | what |
|---|---|
| world_night_crop.jpg | `assets/maps/kit/world_night.jpg` cropped lon −125…145, lat 78…−74 (16:9), 3840×2160 (AWS Terrain / Natural Earth, PD) |
| world_borders.svg, world_{asia,southam,mideast,us,paraguay}.svg | country outlines / region fills from `world_overlay.svg` in the crop's pixel space (sub-paths decimated to ≥ 6 world-px steps) |
| paraguay_night_half.jpg | `paraguay_night.jpg` at 50 % (2568×2520) |
| paraguay_overlay_pys03.svg | Paraguay fill (tierra) + Brazil/Argentina/Bolivia borders + Paraguay/Paraná/Pilcomayo rivers (OSM ODbL via the map kit) |
| miguel_cut.png | `npx hyperframes remove-background` of `shared/photos/miguel_vazquez.jpg` (press photo, © owner, fair use) |
| miguel_plate.jpg | clean plate for the 2.5D: the subject filled from its surroundings (normalised-convolution growth, numpy/scipy) |
