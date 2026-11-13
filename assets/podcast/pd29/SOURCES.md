# assets/podcast/pd29 — derived map plates (ED12)
Made by `.venv/bin/python project/podcast/gen/ed12/ed12_assets.py pd29` from the map kit.
| file | what | source | licence |
|---|---|---|---|
| world_night_base.jpg | world night relief, 135°W–150°E × 86°N–40°S, equirectangular with standard parallel ≈ 40°N (x=(lon+135)·12.32, y=(86−lat)·16), 3511×2016 | `assets/maps/kit/world_night.jpg` | relief: AWS Terrain Tiles (SRTM/GMTED/ETOPO1); vectors: Natural Earth — public domain |
| asia_night_detail.jpg | same style and projection, 24–135°E × 58–2°N at 2.5× (3419×2240), overlaid in the same camera space for the close-ups | same | same |
| pd29_map.json | country outlines (US, Pakistan, China, India, Taiwan) + city pixels in that space; inlined into the composition by `gen/ed12/build.py` | `assets/maps/kit/world_overlay.svg` (Natural Earth) | public domain |
Photos used by pd29 are existing library files (no copies): `assets/c5/photos/kissinger_portrait_1973_official.jpg` (US State Dept, PD),
`assets/c5/photos/pia_boeing_707_340c_an0633118.jpg` (airliners.net via Wikimedia Commons, GFDL/CC BY-SA — credited on screen),
`assets/c5/photos/nixon_official_portrait_nara530679.jpg` (NARA, PD), `assets/c3/photos/mao_zedong_with_cap.jpg` (PD) — see their SOURCES.md.
