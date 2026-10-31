# Map kit (built 2026-10-31 for Krish's round-3 map-quality note, MANUAL §10.9)

Replaces the flat grey relief and grey-beige Pacific maps in `assets/intro/maps`. Preview: `_preview.jpg`.
Every base has a `<region>.json` with the lon/lat → pixel formula, bounds and key place pixels, plus
`<region>_overlay.svg` in the same pixel space (groups `land`, `countries` (`#c-taiwan`, `#c-china`, `#c-japan`…),
`us_states` (`#st-california`…), `lakes`, `rivers`, `cities` (`#p-taipei`…)) and `<region>_landmask.png`.
Use them in a camera div exactly like s02: `<img>` + `<svg viewBox="0 0 W H">` + GSAP push.

**Variants:** `atlas` = warm vintage colour relief (muted teal-grey sea, warm hypsometric land, multi-direction
hillshade) for paper scenes; `night` = graphite land on near-night sea for D11/D13-style data maps, with lines/fills in
palette colours; `sat` = Esri imagery, natural colour; `satdesat` = the s02 look (desaturated, cool shadows) for
night/cinematic scenes, with red/blue/celadon overlays.

| file | what | size | best for | credit line |
|---|---|---|---|---|
| `world_atlas.jpg` / `world_night.jpg` | world relief, plate carrée, x=(lon+180)*45.511, y=(90-lat)*45.511 | 16384×8192 | globe/world establishing shots, Cold War world (UN, Soviet Union, US, China) | Natural Earth / AWS Terrain Tiles (PD) |
| `world_satdesat_21600.jpg` | NASA Blue Marble NG topo-bathy, desaturated | 21600×10800 | night-ground world, s02 look (multiply world.json pixels by 1.318359) | NASA Blue Marble |
| `pacific_{atlas,night,sat,satdesat}.jpg` | Pacific, 100°E → 115°W across the antimeridian (lon<100 → +360) | 6380×2420 | Taiwan ↔ US West Coast routes, Japan–Korea–Taiwan–California arc, shipping/flight lines | atlas/night: PD · sat: Esri, Maxar, Earthstar Geographics |
| `east_asia_{…}.jpg` | 100–150°E, 15–48°N (China coast, Taiwan Strait, Korea, Japan) | 6398×4950 | Beijing–Taipei–Tokyo–Seoul, Taiwan Strait, Cold War East Asia | same |
| `us_{…}.jpg` | continental US, 126–66°W, 23.5–50°N | 6392×3524 | US East vs West (New York/Boston vs California), state fills via `#st-*` | same |
| `bay_area_{…}.jpg` | SF Bay, 123.0–121.55°W, 36.95–38.25°N (SF, Oakland, Stanford, Palo Alto, Mountain View, San Jose) | 5972×6760 | Silicon Valley origin, Stanford → Palo Alto → Santa Clara push | same |
| `northeast_{…}.jpg` | NY–Boston, 75.2–69.8°W, 40.4–43.0°N | 6397×4129 | New York, MIT/Boston, Route 128, Bell Labs | same |
| `taiwan_{atlas,night,sat,satdesat}.jpg` | Taiwan close-up incl. Penghu, 119.3–122.2°E, 21.8–25.4°N | 3246×4399 | Taiwan island fills (celadon), Hsinchu pin, Taipei; atlas is the premium relief | same |
| `aerial_hsinchu_park_z18.jpg` | Hsinchu Science Park core, Esri z18 (0.54 m/px), TSMC HQ/Fab 12A + UMC pins in json | 4608×3584 | D14-style aerial: fill TSMC red / UMC blue blocks, road highlight | Esri, Maxar, Earthstar Geographics |
| `aerial_hsinchu_park_z17.jpg` | whole park + Hsinchu edge, z17 (1.08 m/px) | 4864×3840 | wider aerial push into the park | same |
| `aerial_stanford_z17.jpg` | Stanford campus + Palo Alto + Stanford Research Park | 4352×3840 | Stanford / Terman / Research Park | same |
| `aerial_palo_alto_hp_garage_z18.jpg` | HP garage (367 Addison Ave) neighbourhood, z18 | 3584×3072 | HP garage pin, "birthplace of Silicon Valley" | same |
| `aerial_mit_z17.jpg` | MIT + Charles River + Back Bay | 4352×3840 | MIT / Boston scenes | same |
| `scans/far_east_1943.jpg` | colour atlas map, Milrose 1943 (Japanese "Taiwan (Formosa)", rail/air lines) | 7462×5371 | D10 tilted vintage map, WWII/Cold-War East Asia; approx affine for 110–140°E (±25 px) | Library of Congress |
| `scans/cia_formosa_1949.jpg` | CIA 1949 Taiwan Province map with graticule (linear fit ±40 px) | 4858×6416 | Cold War document, Taiwan Strait, offshore islands | CIA 1949 / Library of Congress |
| `scans/cia_nationalist_china_1958.jpg` | CIA 1958 "Nationalist China, Hong Kong and Macao" ("Communist China" label, FOUO) | 5854×5406 | archival prop; not georeferenced | CIA 1958 / Library of Congress |

## Sharpness (checked by 640 px crops at full res)
- Regional crops are ≥ 5970 px wide (Taiwan ≥ 4399 tall), so a 1920 frame showing ⅓ of the map is a 1:1 crop — a 2–3× camera
  push stays sharp. The aerials are native tile pixels (no resampling).
- The world relief is 16384 px (≈ 45 px/deg): sharp for whole-continent framing; for a push past one country switch to the
  regional crop (same style, same colours) under a cross-dissolve.
- `pacific_*` is 44 px/deg — fine for the ocean-wide routes, too soft for a Taiwan close-up (use `taiwan_*` / `east_asia_*`).

## Known limits
- Natural Earth rasters (NE2/NE1/GRAY_HR) were blocked (naciscdn 403), so the relief is built from AWS terrain tiles with our own
  styling (`tools/map_kit.py`). The two caps beyond ±84° on the world maps are filled with smoothed copies (no data there).
- `bay_area_sat`: Esri's Bay Area mosaic mixes sources (visible colour patches in the south hills); water is replaced with
  one calm tone using the landmask. For a clean frame prefer `bay_area_atlas` or `bay_area_satdesat` with an overlay.
- Close-up relief (Taiwan, Bay, Northeast) uses the elevation coastline (> 0.5 m) and a flat sea; the overlay SVG uses Natural
  Earth 10m coastlines, which are coarser than the relief at that zoom — use the landmask PNG for exact coast fills there.
- Vintage scans: the 1943 map is conic (curved graticule) — the affine only holds locally around East Asia; re-check pins by eye.

## Rebuild / extend
`.venv/bin/python tools/map_tiles.py fetch terr|esri <z> lon0 lat0 lon1 lat1` then `.venv/bin/python tools/map_kit.py <region>`
(regions in `REGIONS`, aerials in `AERIALS`; add a dict entry for a new place). One region at a time (peak ≈ 3 GB for the world).
