# Map kit — sources (all fetched 2026-10-31, no login, no payment)

| asset(s) | source | licence / credit |
|---|---|---|
| `*_atlas.jpg`, `*_night.jpg`, `*_landmask.png` (relief) | AWS Terrain Tiles, terrarium PNG, https://s3.amazonaws.com/elevation-tiles-prod/terrarium/{z}/{x}/{y}.png (z6 world/Pacific, z8 East Asia/US, z11 Taiwan/Northeast, z13 Bay Area) — SRTM, GMTED2010, ETOPO1, USGS NED | public domain sources; credit "Relief: AWS Terrain Tiles (SRTM/ETOPO1)" optional |
| coastline / lakes in relief + `*_overlay.svg` | Natural Earth 10m via jsDelivr: `world-atlas@2/countries-10m.json`, `world-atlas@2/land-10m.json`, `us-atlas@3/states-10m.json`, `gh/nvkelso/natural-earth-vector@master/geojson/ne_10m_lakes.geojson`, `ne_10m_rivers_lake_centerlines.geojson` | public domain (Natural Earth) |
| `world_satdesat_21600.jpg` | NASA Blue Marble Next Generation, topography + bathymetry, Aug 2004, `world.topo.bathy.200408.3x21600x10800.jpg`, https://eoimages.gsfc.nasa.gov/images/imagerecords/73000/73776/ | public domain; credit "NASA Blue Marble" |
| `*_sat.jpg`, `*_satdesat.jpg` (regional) and `aerial_*.jpg` | Esri World Imagery tiles, https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x} | © Esri and its data providers — fair use per MANUAL §10.9; **on-screen credit "Esri, Maxar, Earthstar Geographics"** |
| `scans/far_east_1943.jpg` | "The Far East and adjoining areas", Milrose Publishing Co., New York 1943 — Library of Congress G&M Division, https://www.loc.gov/item/2006636620/ (IIIF, 50 % of master) | no known restrictions; credit "Library of Congress" |
| `scans/cia_formosa_1949.jpg` | "China, Taiwan Province (Formosa)", CIA 1949 — https://www.loc.gov/item/2013591166/ (IIIF, 60 %) | US government work, public domain |
| `scans/cia_nationalist_china_1958.jpg` | "Nationalist China, Hong Kong, and Macao", CIA 1958 — https://www.loc.gov/item/2013591164/ (full) | US government work, public domain |

Not reachable from the cloud session: Natural Earth rasters (NE2_HR_SR_W_DR / NE1 / GRAY_HR, naciscdn.org answers 403;
the naturalearthdata.com link redirects to a 404). The relief here is built from the same class of data (SRTM/ETOPO) with our own
hypsometric tint + multi-directional hillshade, so it does not need them. To add NE2 anyway, fetch it on a Mac via the relay (MANUAL §8.2).
Wikimedia Commons API was rate-limiting (no airline route maps fetched); David Rumsey's API did not connect.
Build tools: `tools/map_tiles.py` (fetch), `tools/map_kit.py` (build; `map_kit.py <region>` / `map_kit.py aerial`).

## Ivan project additions (fetched 2026-11-01, no login, no payment)
| asset(s) | source | licence / credit |
|---|---|---|
| `eastern_europe_{atlas,night,landmask}`, `russia_{atlas,night,landmask}` | AWS Terrain Tiles terrarium (z8 Eastern Europe, z6 Russia) — SRTM / GMTED2010 / ETOPO1 | public domain |
| `eastern_europe_{sat,satdesat}.jpg` | Esri World Imagery tiles z8 | © Esri and its data providers, fair use per MANUAL §10.9; on-screen credit "Esri, Maxar, Earthstar Geographics" |
| `eastern_europe_overlay.svg`, `russia_overlay.svg` | Natural Earth 10m via jsDelivr (world-atlas@2 countries/land, NE lakes + rivers geojson). Crimea moved from Russia to Ukraine (+ separate `#c-crimea`) by `crimea_fix()` in `tools/map_kit.py` | public domain |
| `aerial_moscow_kirillov_blast_z17`, `aerial_moscow_sarvarov_blast_z17`, `aerial_olenya_airbase_z16`, `aerial_belaya_airbase_z16`, `aerial_dyagilevo_airbase_z16`, `aerial_ivanovo_severny_airbase_z16`, `aerial_alabuga_sez_z16`, `aerial_kazan_aircraft_plant_z16` (.jpg + .json) | Esri World Imagery tiles z16/z17, stitched unmodified (https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}) | © Esri and its data providers, fair use per MANUAL §10.9; **on-screen credit "Esri, Maxar, Earthstar Geographics"** |
Place coordinates: blast sites and airfields from the lead's brief (checked against the imagery: airfields/runways and the avenue/street
are where expected); Alabuga SEZ located by eye on Esri z12/z14 (the brief's 55.79N 52.05E is the M7 highway S of the SEZ).


## Paraguay project additions (fetched 2026-11-08, no login, no payment)
| asset(s) | source | licence / credit |
|---|---|---|
| `south_america_{atlas,night,landmask}`, `paraguay_{atlas,night,landmask}` | AWS Terrain Tiles terrarium (z7 / z10) — SRTM / GMTED2010 / ETOPO1 | public domain |
| `south_america_{sat,satdesat}`, `paraguay_{sat,satdesat}` | Esri World Imagery tiles z8 / z10 | © Esri and its data providers, fair use per MANUAL §10.9; on-screen credit "Esri, Maxar, Earthstar Geographics" |
| `south_america_overlay.svg`, `paraguay_overlay.svg` (other countries/rivers), lakes | Natural Earth 10m via jsDelivr (world-atlas@2, NE lakes + rivers geojson) | public domain |
| `paraguay_overlay.svg` Paraguay/Brazil/Argentina/Bolivia borders, Paraguay/Paraná/Pilcomayo rivers; Itaipu + Yacyretá water in `paraguay_*` reliefs/landmask | OpenStreetMap via nominatim.openstreetmap.org `lookup` (relations 287077, 59470, 286393, 252645, 302330, 421678, 1085755, 49550, 102679), polygon_geojson simplified 0.0002–0.0003° | © OpenStreetMap contributors, ODbL — credit "© OpenStreetMap contributors" when the overlay is on screen |
| `americas_night.jpg`, `americas_satdesat.jpg` | crops of `world_night.jpg` / `world_satdesat_21600.jpg` | as the world bases (PD / NASA Blue Marble) |
| `aerial_asuncion_{city_z15,congress_z18,banco_central_z18,ueno_hq_z18,mburuvicha_roga_z18}` (.jpg + .json) | Esri World Imagery tiles, stitched unmodified | © Esri and its data providers, fair use; credit "Esri, Maxar, Earthstar Geographics" |
Place coordinates: Asunción landmarks from OpenStreetMap/Nominatim, checked by eye on the aerials. Ueno address: ueno's 2026 shareholder
notice (https://www.ueno.com.py/wp-content/uploads/2026/06/Convocatoria-de-Asambleas-31d50a9a-d9aa-4a4d-9a06-5adcb678a3ea.pdf) — Av. Santa
Teresa 3088 c/ Concejal Vargas; older sources give Santa Teresa 1827 (Torres del Paseo). BCP address: bcp.gov.py (Av. Federación Rusa y Augusto Roa Bastos).

## NVIDIA project additions (fetched 2026-11-16, no login, no payment)
| asset(s) | source | licence / credit |
|---|---|---|
| `southeast_asia_{atlas,night,landmask}`, `china_{atlas,night,landmask}`, `pearl_river_delta_{atlas,night}` | AWS Terrain Tiles terrarium (z8 / z7 / z13) — SRTM / GMTED2010 / ETOPO1 | public domain |
| `southeast_asia_{sat,satdesat}`, `china_{sat,satdesat}`, `pearl_river_delta_{sat,satdesat}` | Esri World Imagery tiles z8 / z7 / z13 | © Esri and its data providers (Maxar/Vantor, Earthstar), fair use per MANUAL §10.9; on-screen credit "Esri, Maxar, Earthstar Geographics" |
| `pearl_river_delta_landmask.png` (+ coast in its reliefs/sat and `#land #c-china #c-hong_kong #c-macao` in its overlay) | Esri Canvas World_Light_Gray_Base tiles z13, https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer/tile/{z}/{y}/{x} (water colour thresholded) | © Esri, HERE, Garmin, © OpenStreetMap contributors — derived mask only; credit "Esri" with the map |
| `pearl_river_delta_overlay.svg` HK / Macau boundaries, `#b-hk_mainland_border` | OpenStreetMap via nominatim.openstreetmap.org `lookup?osm_ids=R913110,R1867188&polygon_geojson=1&polygon_threshold=0.0001` | © OpenStreetMap contributors, ODbL |
| `southeast_asia_overlay.svg`, `china_overlay.svg` (and NE rivers/lakes in the PRD overlay) | Natural Earth 10m via jsDelivr (world-atlas@2, NE lakes + rivers geojson) | public domain |
| `aerial_shenzhen_huaqiangbei_z17`, `aerial_memphis_xai_colossus_z16`, `aerial_memphis_xai_colossus2_z16`, `aerial_johor_data_centers_z16` (Sedenak Tech Park, imagery 2021-02-15), `aerial_johor_nusajaya_tech_park_z16` (imagery 2025) (.jpg + .json) | Esri World Imagery tiles, stitched unmodified | © Esri and its data providers, fair use; credit "Esri, Maxar, Earthstar Geographics" |
Place coordinates: PRD/Huaqiangbei places from OpenStreetMap/Nominatim (SEG Plaza, Huaqiang Electronics World, Golden Computer Arcade,
Shun Tak / HK-Macau Ferry Terminal, Shekou Cruise Center, Lo Wu, Futian checkpoint), checked by eye on the imagery; Colossus 1/2 and the
Sedenak halls located by eye on Esri z14–z16 (Colossus 1 = 3231 Paul R Lowry Rd per Nominatim; Colossus 2 roof reads "MACROHARD");
Sedenak Tech Park position cross-checked with Baxtel/DataCenterMap campus points (~1.70 N, 103.41 E: https://baxtel.com/campus/k2-kulai-johor-campus,
https://baxtel.com/campus/vantage-johor-jhb1-sedenak-campus); imagery dates from Esri's World_Imagery identify service.
NVIDIA HQ (pacific.json `nvidia_hq_santa_clara`): Nominatim "NVIDIA Endeavor, 2788 San Tomas Expressway, Santa Clara".
