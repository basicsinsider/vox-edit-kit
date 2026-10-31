# assets/c6/derived/c6s03 — derived files for compositions/c6s03.html

All are crops, stills or layers made from assets already in the repo or fetched by the c6s03 editor. Raw downloads
are in `_tmp/c6s03/raw/` (not committed). Generator: `project/c6/gen_c6s03_assets.py` (Pacific card, Fei Hua circle);
`_tmp/c6s03/aldrin_layers.py` (2.5D layers).

| file | made from | licence / credit on screen | used in |
|---|---|---|---|
| aldrin_25d_back.jpg, aldrin_25d_subject.png, aldrin_25d_front.png, aldrin_25d_layout.json | `assets/c6/photos/apollo11_aldrin_as11-40-5903.jpg` (NASA), subject cut with `hyperframes remove-background`, ground/foreground split by hand | PD NASA, "NASA AS11-40-5903 (PD)" | C6S095 |
| melies_trip_to_the_moon_1902_rocket_eye.jpg | frame of Georges Méliès, *Le Voyage dans la Lune* (1902), archive.org copy; raw frames `_tmp/c6s03/raw/melies_4*.jpg` (the previous editor did not record the exact archive.org item) | PD (1902), credited | C6S095 |
| destination_moon_1950_lunar_surface.jpg | frame of *Destination Moon* (Pichel, 1950), archive.org (likely item `destination-moon-1950_202509`; the exact item was not recorded); raw frames `_tmp/c6s03/raw/dm_4*.jpg` | treated as © fair use, credited "Destination Moon, 1950 (fair use)" | C6S095, C6S096 (blurred backing panel) |
| still_formosa_1959_*.jpg, still_newsreel_1959_formosa_taipei_street.jpg, still_taiwan_1960_*.jpg | frames from `assets/c4/footage/formosa_1959_*.mp4`, `assets/c3/footage/newsreel_1959_formosa_taipei_street.mp4`, `assets/c4/footage/taiwan_1960_*.mp4` and `assets/intro/footage/taiwan_1960_steel_mill_molten.mp4` (see those folders' SOURCES.md) | as their source clips; credited "Film: Taiwan, c. 1959–60 — archival" | C6S078, C6S083, C6S093 |
| freeway1_hsinchu_esri_z17_crop.jpg | crop of `assets/intro/derived/maps/hsinchu_s2_esri_z17_4660.jpg` (Esri World Imagery z17; National Freeway 1 through Hsinchu) | "Imagery: Esri, Maxar, Earthstar Geographics" | C6S086 |
| pacific_atlas_card.jpg | crop of `assets/maps/kit/pacific_atlas.jpg` (map kit, lon 112°E–115°W, lat 52–12°N) | kit credits: "Relief: AWS Terrain Tiles · Natural Earth (PD)" | C6S102 |
| fei_hua_circle.jpg | **fallback**: his name 費驊 set in WenQuanYi Zen Hei (rendered to an image — our fonts have no CJK) on `paper_cream_02`. The real portrait (Commons `File:19710809費驊.jpg`, 204×255, CC0) could not be downloaded: upload.wikimedia.org answered 429 / an error page from this IP (2026-10-31). It is requested in `requests/fetch.json`. Drop it at `assets/c6/photos/fei_hua_1971.jpg` (log it in that folder's SOURCES.md) and re-run `.venv/bin/python project/c6/gen_c6s03_assets.py`; the composition picks it up unchanged | own typographic image | C6S106 (burn reveal), C6S107 (card) |
