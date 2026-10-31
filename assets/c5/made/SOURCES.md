# assets/c5/made — derived files (made from logged sources)

## c5s03 editor (2026-10-31) — generator: project/c5/gen/c5s03_assets.py + ffmpeg lines below
| file | what | made from | credit |
|---|---|---|---|
| strait_esri_z10.jpg / .json | Taiwan Strait satellite mosaic, Esri World Imagery z10 tiles stitched unmodified (Web Mercator, 3840x4096, 117.3–122.3°E, 21.9–26.6°N; place pixels in json: Kinmen, Matsu, Xiamen, Fuzhou, Taipei…) | `MK_CACHE=/tmp/c5s03/tiles python3 tools/map_tiles.py fetch esri 10 117.3 21.9 122.3 26.6` → `c5s03_assets.py strait` | "Imagery: Esri, Maxar, Earthstar Geographics" (on screen) |
| strait_taiwan_mask.png | Taiwan main-island mask (white+alpha) in the same pixel space, from the imagery | `c5s03_assets.py twmask` | — |
| carrier_at_sea_1945_slow.mp4 | carrier in heavy sea, slowed ×1.45 (5.8 s) | assets/c3/footage/newsreel_1945_pacific_carrier_at_sea.mp4 (PD newsreel) | US Navy newsreel, PD |
| un1971_us_desk_slow.mp4 | US desk at the UN, slowed ×1.12 (4.2 s) | assets/c6/footage/un1971_us_desk.mp4 (UN film, fair use) | UN film 1971, fair use |
| un1971_vote_board_still.jpg | still of the vote board close-up (t = 0.7 s), always shown blurred | assets/c6/footage/un1971_vote_board_closeup.mp4 | UN film 1971, fair use |
| rewind_montage_reversed.mp4 | VHS-rewind montage: 4 × 1.15 s reversed ×3.5 (Formosa street 1959, Mao rostrum 1959, Taipei boulevard 1960, fleet review 1956) | c3/intro PD newsreels | PD |
