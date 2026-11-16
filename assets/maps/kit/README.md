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

## South America / Paraguay (Paraguay project, 2026-11-08)
Built with the same tools/styles (`map_kit.py south_america|paraguay`, `map_kit.py aerial <name>`, `map_kit.py crop americas`).
Preview: `_preview_paraguay.jpg`. Palette (`lib/palette_paraguay.css`): fill `#c-paraguay` tierra `#cf5a33`, neighbours neutral.
Overlay ids: `#c-paraguay #c-brazil #c-argentina #c-bolivia #c-chile #c-peru #c-uruguay #c-colombia #c-venezuela #c-ecuador #c-guyana
#c-suriname #c-french_guiana #c-falkland_is #c-panama …` (French Guiana split out of `#c-france` by `guiana_fix()`); rivers `#river-paraguay
#river-parana #river-pilcomayo #river-amazonas …`; cities `#p-asuncion #p-brasilia #p-buenos_aires #p-la_paz #p-ciudad_del_este #p-encarnacion
#p-concepcion #p-san_lorenzo #p-luque …` (ids use `_`, same keys as `json → places`). **Natural Earth calls the Paraguay river "Paraná"** —
`river_fix()` renames that line to `#river-paraguay`; `slug()` now strips accents (`Paraná` → `parana`, it used to give `paran`).

| file | what | size | formula (lon/lat → px) | credit line |
|---|---|---|---|---|
| `south_america_{atlas,night,sat,satdesat}.jpg` + `south_america.json` + `_overlay.svg` + `_landmask.png` | 95–25°W × 15°N–58°S: whole continent + Panama/Costa Rica edge, Falklands, S. Georgia; 37 places (capitals, São Paulo/Rio, Paraguay cities, Asunción landmarks) | 5490×6132 | `x = (lon + 95) * 78.4224 ; y = (15 - lat) * 84` (k = cos 21°; shapes true around Paraguay, Patagonia slightly wide) | atlas/night: AWS Terrain Tiles (PD) + Natural Earth (PD) · sat: Esri, Maxar, Earthstar Geographics |
| `paraguay_{atlas,night,sat,satdesat}.jpg` + `paraguay.json` + `_overlay.svg` + `_landmask.png` | 63.5–53.5°W × 19–28°S: all Paraguay + edges of Bolivia, Brazil (Foz do Iguaçu, Itaipu), Argentina (Clorinda, Formosa, Posadas); Itaipu + Yacyretá + Yguazú reservoirs and the Paraguay/Paraná rivers are water in the reliefs | 5136×5040 | `x = (lon + 63.5) * 513.576 ; y = (-19 - lat) * 560` (k = cos 23.5°) | same + rivers/borders/reservoirs © OpenStreetMap contributors (ODbL) |
| `americas_night.jpg` / `americas_satdesat.jpg` + `americas.json` | crops of `world_night` / `world_satdesat_21600`, 130–20°W × 55°N–58°S (US East Coast/Washington → Asunción → Buenos Aires) | 5006×5143 / 6600×6780 | night: `x = (lon + 180) * 45.5111 - 2276 ; y = (90 - lat) * 45.5111 - 1593`; satdesat: `x = (lon + 180) * 60 - 3000 ; y = (90 - lat) * 60 - 2100` (exact values + place px in json). Borders: `world_overlay.svg` with `viewBox="2276 1593 5006 5143"` over the night crop | night: AWS Terrain/NE (PD) · satdesat: NASA Blue Marble NG |
| `aerial_asuncion_city_z15.jpg` | all of Asunción (river, bay, downtown → Villa Morra), all landmark pins below | 3840×2816, 4.3 m/px | Web Mercator, formula in json | Esri, Maxar, Earthstar Geographics |
| `aerial_asuncion_congress_z18.jpg` | downtown by the bay: `palacio_de_lopez` 1509,1097 (U-shaped palace facing the bay garden), `palacio_legislativo` 1844,1486, `plaza_de_armas` 1990,1622, `plaza_de_los_heroes` 1910,2146, `plaza_de_la_democracia` 1960,2342 | 3584×3072, 0.54 m/px | same | same |
| `aerial_asuncion_banco_central_z18.jpg` | Banco Central del Paraguay campus (Av. Federación Rusa y Augusto Roa Bastos, Las Lomas): pin 1487,1220 = campus centre; long office block just right of the pin, round-roofed hall up-left | 3072×2560, 0.54 m/px | same | same |
| `aerial_asuncion_ueno_hq_z18.jpg` | ueno HQ, Av. Santa Teresa 3088 c/ Concejal Vargas (address from ueno's own 2026 shareholder notice): pin `ueno_hq_santa_teresa_3088` 2832,2117 on the modern office block with car park at the Santa Teresa / Concejal Vargas corner; also `torres_del_paseo_la_galeria` 1181,1004 (older address, Santa Teresa 1827 — Paseo La Galería towers) | 4096×3328, 0.54 m/px | same | same |
| `aerial_asuncion_mburuvicha_roga_z18.jpg` | Mburuvicha Róga presidential residence on Av. Mariscal López: pin 1472,1260 (house + pool; helipad lawn to the south) | 2816×2560, 0.54 m/px | same | same |

Positions: Asunción landmarks from OpenStreetMap (Nominatim), each checked by eye on the aerial (buildings/plazas where expected).
Known limits: Esri imagery over downtown has a colour seam on the bay water (x ≈ 1920 in `congress_z18`) and a cloud shadow SE of
the plazas; `asuncion_city_z15` has one small cloud + shadows (S-centre). The Ueno HQ pin is OSM's — the Esri photo may predate a
façade/rename, so frame the block, don't claim signage. `paraguay_atlas` is mostly flat Chaco (pale by nature; relief only in the east).
NE 1:10M borders/rivers were 2–13 km off the imagery at Paraguay scale, so `paraguay_overlay.svg` uses OSM geometry for
`#c-paraguay/brazil/argentina/bolivia` and `#river-paraguay/parana/pilcomayo` (REGIONS `osm=`; JSONs from Nominatim `lookup?osm_ids=R287077,R59470,R286393,R252645,R302330,R421678,R1085755,R49550,R102679&polygon_geojson=1&polygon_threshold=0.0002–0.0003`, cached in `/tmp/mk/osm`); other rivers there (Uruguay, Bermejo…) are still NE and can sit ~1–3 km off. On `south_america_*` NE is accurate to ~1–2 px.

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
`.venv/bin/python tools/map_tiles.py fetch terr|esri <z> lon0 lat0 lon1 lat1` (vectors: world-atlas@2 + NE geojson into `/tmp/mk/vec`; Paraguay also needs the OSM JSONs in `/tmp/mk/osm`) then `.venv/bin/python tools/map_kit.py <region>`
(regions in `REGIONS`, aerials in `AERIALS`; add a dict entry for a new place). One region at a time (peak ≈ 3 GB for the world).

## NVIDIA project (2026-11-16)
Built with the same tools/styles (`map_kit.py` functions, unchanged) through the wrapper `work/nv-maps/nv_maps.py`, which adds the
REGIONS / PLACES / AERIALS entries below at runtime plus a grey-base land mask for the PRD (merge into `tools/map_kit.py` to make it
permanent). Preview: `_preview_nvidia.jpg`. Overlay ids as usual: `#c-china` (one clean fillable path incl. Hainan; de-facto NE borders,
Aksai Chin inside China), `#c-taiwan`, `#c-hong_kong`, `#c-macao` are separate paths; cities `#p-<place>` = json `places` keys.

| file | what | size | formula (lon/lat → px) | credit line |
|---|---|---|---|---|
| `southeast_asia_{atlas,night,sat,satdesat}.jpg` + `.json` + `_overlay.svg` + `_landmask.png` | 95–125°E × 6.5°S–31.5°N: S China coast (Guangzhou/Shenzhen/HK, Shanghai at the top edge), Taiwan, Vietnam, Thailand, Malaysia, Singapore, Sumatra/Borneo, Java N coast (Jakarta), Philippines. 68 places incl. singapore, kuala_lumpur, johor_bahru, kulai, cyberjaya, batam, penang, bangkok, hanoi, ho_chi_minh_city, manila, jakarta, taipei, hsinchu, hong_kong, shenzhen, guangzhou, shanghai, hangzhou | 5428×7030 | `x = (lon - 95) * 180.9485 ; y = (31.5 - lat) * 185` (k = cos 12°) | atlas/night: AWS Terrain Tiles + Natural Earth (PD) · sat: Esri, Maxar, Earthstar Geographics |
| `china_{atlas,night,sat,satdesat}.jpg` + `.json` + `_overlay.svg` + `_landmask.png` | 72–142°E × 16–55°N: all China + Mongolia, Koreas, Japan to Tokyo, Taiwan, N India/Nepal/Bangladesh, Kazakh/Kyrgyz edge, Russian Far East edge. 76 places (beijing, shanghai, shenzhen, hangzhou, hong_kong, taipei, seoul, tokyo, chengdu, wuhan, xian, hefei…) | 6383×4368 | `x = (lon - 72) * 91.1792 ; y = (55 - lat) * 112` (k = cos 35.5°) | same |
| `pearl_river_delta_{atlas,night,sat,satdesat}.jpg` + `.json` + `_overlay.svg` + `_landmask.png` | 113.4–114.6°E × 22.0–22.9°N: Hong Kong (Island, Kowloon, NT, Lantau + airport), Victoria Harbour, Shenzhen (Futian, Nanshan/Shekou, Shenzhen Bay), the HK–Shenzhen border, Macau/Zhuhai edge, Pearl River mouths. Places: hong_kong_central, victoria_harbour, mong_kok, sham_shui_po, golden_computer_arcade, shenzhen_futian, huaqiangbei, seg_plaza, huaqiang_electronics_world, shekou_port, hk_macau_ferry_terminal, lo_wu_control_point, futian_checkpoint, shenzhen_bay_port, hk_airport, macau, zhuhai, hong_kong, shenzhen | 6211×5040 (≈ 19 m/px; Esri/terrain z13) | `x = (lon - 113.4) * 5175.52 ; y = (22.9 - lat) * 5600` (k = cos 22.45°) | same + overlay HK/Macau borders © OpenStreetMap contributors (ODbL) |
| `aerial_shenzhen_huaqiangbei_z17.jpg` | Huaqiangbei, Futian: pins `seg_plaza` 1561,1435 (base of the SEG tower; its roof with the round helipad is displaced up-left by lean), `huaqiang_electronics_world` 1440,1415, `huaqiangbei` 1487,1354 (the N–S pedestrian street); Shenzhen River + HK fish ponds at the bottom | 3328×2816, 1.10 m/px | Web Mercator, formula in json | Esri, Maxar, Earthstar Geographics |
| `aerial_memphis_xai_colossus_z16.jpg` | xAI Colossus (former Electrolux plant), Paul R Lowry Rd, S Memphis, beside TVA Allen plant + Mississippi: pin `xai_colossus_1` 1406,1358 (building centre, by eye; generator rows around it); `colossus_1_address_3231_paul_r_lowry_rd` 1611,1358 (Nominatim address point, on the road). Esri colour seam on the river (W edge) | 3072×2560, 1.96 m/px | same | same |
| `aerial_memphis_xai_colossus2_z16.jpg` | Colossus 2, Tulane Rd, Whitehaven: pin `xai_colossus_2_macrohard` 1441,1303 — roof painted "MACROHARD" (legible in the imagery) | 3072×2560, 1.96 m/px | same | same |
| `aerial_johor_data_centers_z16.jpg` | **Sedenak Tech Park, Kulai** (chosen: data halls clearly visible): pin `sedenak_tech_park_data_halls` 1680,1533 = twin white-roof data halls; `sedenak_tech_park` 1429,1309 = park road grid. Esri imagery dated Feb 2021 (early phase; the park is far bigger now); a few small clouds | 2816×2560, 2.39 m/px | same | same |
| `aerial_johor_nusajaya_tech_park_z16.jpg` | backup: Nusajaya Tech Park, Iskandar Puteri (2025 imagery, many new halls but haze + one cloud over the centre); pin `nusajaya_tech_park` 1002,641 (OSM area centre). Operators of individual buildings NOT verified — frame the park | 1792×1536, 2.39 m/px | same | same |

`pacific.json` already had santa_clara, san_jose, taipei, hsinchu_city/hsinchu_science_park, shenzhen, hong_kong; added
`nvidia_hq_santa_clara` (6073.4, 995.7). Singapore / Kuala Lumpur (lat < 5°) and Memphis (lon < 115°W) are outside the Pacific base.

**PRD land mask:** the DEM coast (> 0.5 m) missed the reclaimed land (HK airport, Shenzhen Bay, Macau) and flooded the fish ponds;
NE 10m is far too coarse and Overpass (OSM coastline) was unreachable. So land/water comes from Esri's `Canvas/World_Light_Gray_Base`
tiles z13 (water = flat grey-violet ≈ 208,206,212; bridges opened away, ponds < 400 px filled). In `pearl_river_delta_overlay.svg`,
`#land`, `#c-china`, `#c-hong_kong`, `#c-macao` are traced from that mask (fill-rule evenodd; HK/Macau cut by the OSM boundaries
R913110 / R1867188), plus `<g id="borders"> #b-hk_mainland_border` (dashed: Shenzhen Bay → Shenzhen River → Sha Tau Kok → Mirs Bay).
Rivers/lakes there are still NE (coarse). Known limits: Esri clouds over E Shenzhen/Sha Tau Kok (on the border line, upper right) and a
few over Sai Kung; sea in `pearl_river_delta_sat*` is one calm tone (as the other close-ups). `southeast_asia`/`china` sat are Esri
z8/z7 (≈ native) — soft beyond a 2× push; use `pearl_river_delta_*` for HK/Shenzhen.
