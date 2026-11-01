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

## Eastern Europe / Russia (Ivan project, 2026-11-01)
Built with the same tools/styles as above (`map_kit.py eastern_europe|russia`, `map_kit.py aerial <name>`). Palette for fills:
Russia = oxblood, Ukraine = azure (`--sky` on night), nothing else coloured (SEGMENTS §2).
**Crimea:** Natural Earth (de-facto) puts Crimea inside Russia; our overlays move it into `#c-ukraine` (recognised border) and also
give it its own `#c-crimea` path, so a scene can hatch/label it as occupied. `#c-russia` therefore does NOT include Crimea.

| file | what | size | formula (lon/lat → px) | credit line |
|---|---|---|---|---|
| `eastern_europe_{atlas,night,sat,satdesat}.jpg` + `eastern_europe.json` + `_overlay.svg` + `_landmask.png` | 20–62°E × 42–62°N: Poland/Warsaw, Baltics, Belarus, Ukraine + Crimea, western Russia (Moscow, Ryazan, Ivanovo, Nizhny, Kazan, Yelabuga, Samara, Saratov/Engels, Volgograd), Urals edge, NW Kazakhstan, Black Sea, Caspian N half | 6206×4800 | `x = (lon - 20) * 147.768 ; y = (62 - lat) * 240` (k = cos 52°) | atlas/night: Natural Earth / AWS Terrain Tiles (PD) · sat: Esri, Maxar, Earthstar Geographics |

`eastern_europe.json → places` has pixels for moscow, kyiv, warsaw, minsk, st_petersburg, kazan, yelabuga, alabuga_drone_factory,
ryazan, ivanovo, engels, saratov, kharkiv, odesa, lviv, belgorod, kursk, voronezh, rostov_on_don, volgograd, nizhny_novgorod, samara,
sevastopol, vilnius, riga, tallinn, helsinki, uralsk_oral, aktobe, ufa, perm, yekaterinburg, dyagilevo_airbase, ivanovo_severny_airbase,
engels_airbase, kirillov_blast_site, sarvarov_blast_site, kazan_aircraft_plant (same ids as `#p-…` circles in the overlay).
Overlay country ids: `#c-russia #c-ukraine #c-crimea #c-poland #c-belarus #c-kazakhstan #c-lithuania #c-latvia #c-estonia #c-finland
#c-moldova #c-romania #c-georgia …`; rivers `#river-volga #river-dnipro #river-don #river-kama #river-vistula …` (river ids can repeat —
select with `querySelectorAll`).

| file | what | size | formula / note | credit line |
|---|---|---|---|---|
| `russia_{atlas,night}.jpg` + `russia.json` + `_overlay.svg` + `_landmask.png` | whole Russia 20°E → 170°W (Chukotka; lon < 20 → lon + 360), 40–78°N: Europe edge, Murmansk/Olenya, Urals, Siberia, Irkutsk/Belaya, Far East, Kazakhstan, Mongolia, N China | 6566×2850 | `x = (lon - 20) * 38.625 ; y = (78 - lat) * 75` (k = cos 59°; shapes true around 59°N, far north stretched) | Natural Earth / AWS Terrain Tiles (PD) |
| `aerial_moscow_kirillov_blast_z17.jpg` | Ryazansky Prospekt, SE Moscow (Kirillov bomb, Dec 2024); pin `kirillov_blast_site` at 1706,1574 (on the avenue's south side — from the lead's coordinates) | 3328×3072, 0.67 m/px | Web Mercator, formula in json | Esri, Maxar, Earthstar Geographics |
| `aerial_moscow_sarvarov_blast_z17.jpg` | Yasenevaya Street, S Moscow (Sarvarov car bomb, Dec 2025); pin `sarvarov_blast_site` 1589,1558 (lead's coordinates) | 3328×3072, 0.68 m/px | same | same |
| `aerial_olenya_airbase_z16.jpg` | Olenya air base, Murmansk oblast — runway, bomber stands on the N loop; pin 2287,2831 (runway centre). Esri has two clouds over the NE apron/S end | 4352×5376, 0.89 m/px | same | same |
| `aerial_belaya_airbase_z16.jpg` | Belaya air base, Irkutsk oblast — runway + two star-shaped dispersal fields (bomber stands); pin 2113,2089 | 4096×4096, 1.44 m/px | same | same |
| `aerial_dyagilevo_airbase_z16.jpg` | Dyagilevo air base, Ryazan — E–W runway, aircraft on the N apron; light clouds on the W edge; pin 1664,1541 | 3072×2304, 1.38 m/px | same | same |
| `aerial_ivanovo_severny_airbase_z16.jpg` | Ivanovo Severny air base — runway + parked heavy aircraft along the S apron; pin 1629,909 | 3072×2304, 1.30 m/px | same | same |
| `aerial_alabuga_sez_z16.jpg` | Alabuga special economic zone N of Yelabuga, Tatarstan (the Shahed/Geran drone plant is inside it). Pins: `alabuga_drone_factory` 2804,2067 = SEZ centre (generic); `alabuga_nw_new_halls` 693,789 = the new twin-hall complex with fresh earthworks in the NW corner. **The exact drone-plant building is not verified** — frame the SEZ, don't claim a specific building. Esri imagery here is older (pre-"defensive towers") | 5376×4096, 1.34 m/px | same | same |
| `aerial_kazan_aircraft_plant_z16.jpg` | Kazan Aviation Plant (Gorbunov) + its runway, Kazan N; aircraft on the apron; pin 1752,1784 | 3584×2816, 1.34 m/px | same | same |

Palette note: `*_sat.jpg` and the aerials are real colour (green fields). Per SEGMENTS §2 prefer `*_satdesat.jpg` / `*_night.jpg`
/ `*_atlas.jpg`, or grade the aerials toward ash (saturate 0.2–0.4) and put oxblood/azure only in the overlay.
Known limits: `eastern_europe_sat` is Esri z8 (≈ 1.4 px per source px) — soft beyond a 2× push, fine for region shots; overlay
`#c-russia` has a vertical seam at 180° in `russia_overlay.svg` (Chukotka split by Natural Earth) — fill only, or hide the stroke there.
The Caspian is drawn as flat water in both reliefs (its bathymetry tiles had seams).

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
