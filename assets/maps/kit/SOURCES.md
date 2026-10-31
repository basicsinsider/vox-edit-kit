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
