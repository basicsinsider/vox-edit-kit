# Map assets: sources, licenses, projection

## Projection / bounds (shared by us_basemap*.jpg, us_overlay.json, us_overlay.svg)

- Projection: equirectangular (plate carree), WGS84 lon/lat mapped linearly.
- `us_basemap.jpg` / `us_basemap_desat.jpg`: 6400 x 3200 px, lon -128 .. -64, lat 20 .. 52, 100 px per degree.
- `x = (lon + 128) * 100`, `y = (52 - lat) * 100`. Pixel (0,0) is the top-left corner at lon -128, lat 52.
- In CSS, scale the basemap and the SVG overlay (viewBox `0 0 6400 3200`) with the same transform and they stay aligned.
  CONUS fills roughly x 300-6100, y 300-2600. A 16:9 crop of the CONUS is about x 250..6150, y 0..3200 at a 0.33 scale.
- `na_basemap.jpg`: 6000 x 3250, lon -170 .. -50, lat 10 .. 75, 50 px/deg, so `x = (lon+170)*50`, `y = (75-lat)*50`.
- `world_basemap.jpg`: 5400 x 2700, lon -180 .. 180, lat -90 .. 90, 15 px/deg.
- `clouds/clouds_us_aligned.png`: 1456 x 728 with the same bounds as us_basemap (lon -128..-64, lat 20..52), about 22.76 px/deg.
  Stretch it to 6400 x 3200 to lay it over the basemap. It is accurate to about 1 basemap px.

## Files

| File | Dimensions | Source | License |
|---|---|---|---|
| us_basemap.jpg | 6400x3200 | NASA Visible Earth, Blue Marble Next Generation w/ Topography & Bathymetry, July 2004, 500 m tiles A1 + B1 (`world.topo.bathy.200407.3x21600x21600.{A1,B1}.jpg`), https://visibleearth.nasa.gov/images/73751 (files: https://eoimages.gsfc.nasa.gov/images/imagerecords/73000/73751/). Mosaicked, cropped, Lanczos-resampled to 100 px/deg | Public domain (NASA). Credit: "NASA Earth Observatory / Reto Stockli, Blue Marble Next Generation" |
| us_basemap_desat.jpg | 6400x3200 | Same image at 35% saturation (documentary look) | Public domain (NASA) |
| na_basemap.jpg | 6000x3250 | Same NASA tiles, North America crop | Public domain (NASA) |
| world_basemap.jpg | 5400x2700 | NASA BMNG `world.topo.bathy.200407.3x5400x2700.jpg`, same record | Public domain (NASA) |
| us_states.geojson | 316 KB, 56 features | us-atlas v3 `states-10m.json` (US Census Bureau cartographic boundaries 1:10M), https://cdn.jsdelivr.net/npm/us-atlas@3/states-10m.json, converted from TopoJSON. Properties: `name`, `fips`, `abbr`, `conus` | ISC (us-atlas); the Census data is public domain |
| mississippi.geojson | 27 KB, 1184 pts | Natural Earth 10m `rivers_lake_centerlines` (name = Mississippi), https://github.com/nvkelso/natural-earth-vector/blob/master/geojson/ne_10m_rivers_lake_centerlines.geojson. Segments chained into one LineString from Lake Itasca (a point at the Itasca outlet is prepended) to the end of Southwest Pass. Small delta side channels are dropped | Public domain (Natural Earth) |
| project_to_svg.py | n/a | Builds us_overlay.json and us_overlay.svg (and us_overlay_preview.jpg with `--preview`). Needs shapely and Pillow | n/a |
| us_overlay.json | 359 KB | Output of the script (contents listed below) | n/a |
| us_overlay.svg | viewBox 6400x3200 | The same paths in one SVG, for inspection or direct use | n/a |
| us_overlay_preview.jpg | 1600x800 | Alignment check: west region orange, east region blue, river cyan, places as red dots | n/a |
| clouds/cloud_01..04_satellite.png | 2200x1400 RGBA | Top-down satellite-style cloud patches cut from "Transparent Fair Weather Clouds Map.png" by GabrielGGD, https://commons.wikimedia.org/wiki/File:Transparent_Fair_Weather_Clouds_Map.png. Elliptical feathered alpha, upscaled 2x | CC0 |
| clouds/clouds_us_aligned.png | 1456x728 RGBA | Same CC0 cloud map, cropped to the US bounds | CC0 |
| clouds/cloud_05..07_puffy.png | 4000x2300, 4000x1500, 2300x4000 RGBA | Cumulus clouds keyed off a blue-sky photo with Python (alpha from blue-minus-red, luminance as color, feathered edges). Source: "Bright blue sky with scenic white cloud patterns.jpg" by Trixia Lao (via Pexels), https://commons.wikimedia.org/wiki/File:Bright_blue_sky_with_scenic_white_cloud_patterns.jpg | CC0 |
| eli_lilly_hq_corporate_center.jpg | 4032x3024 | "Eli Lilly Corporate Center, Indianapolis, Indiana, USA.jpg" by Momoneymoproblemz, https://commons.wikimedia.org/wiki/File:Eli_Lilly_Corporate_Center,_Indianapolis,_Indiana,_USA.jpg | CC BY-SA 4.0 (attribution required) |
| eli_lilly_hq_tower_2011.jpg | 4320x3240 | "Eli Lilly and Company Corporate Center - Feb 2011.jpg" by Paul Sableman, https://commons.wikimedia.org/wiki/File:Eli_Lilly_and_Company_Corporate_Center_-_Feb_2011.jpg | CC BY 2.0 (attribution required) |
| eli_lilly_hq_1919_postcard.jpg | 3200x2053 | "Eli Lilly and Company Headquarters ca1919" (postcard illustration), https://commons.wikimedia.org/wiki/File:Eli_Lilly_and_Company_Headquarters_ca1919_b1007511_003_tif_zs25x9459.png. Downscaled and flattened to JPG | Public domain |
| eli_lilly_logo.svg / eli_lilly_logo.png | 631x344 SVG / 1920x1047 RGBA PNG | "Eli Lilly and Company.svg", https://commons.wikimedia.org/wiki/File:Eli_Lilly_and_Company.svg (PNG is the Wikimedia render) | Public domain on Commons (below the threshold of originality). It is still a trademark |

## us_overlay.json contents

- `width`, `height`, `bounds`, `px_per_degree`, `projection`, `formula`
- `states[ABBR]` for the 48 contiguous states plus DC: `name`, `d` (SVG path), `bbox` [x0,y0,x1,y1], `label` (an interior point)
- `mississippi`: `d` (open polyline, use `fill="none"`), `length_px` (for stroke-dasharray draw-on), `bbox`
- `regions`:
  - `west_of_mississippi` and `east_of_mississippi`: the CONUS cut exactly along the river. North of Lake Itasca the cut runs straight north along lon -95.21 to the Canadian border; south of the mouth it runs straight south.
  - `west_by_state` and `east_by_state`: whole-state groups. MN, IA, MO, AR, LA count as west; WI, IL, KY, TN, MS count as east. Other states go to whichever side holds most of their area.
  - `conus_outline`
- `places` (lon, lat, x, y): indianapolis, eli_lilly_hq_indianapolis, palo_alto, new_york_city, boston, mississippi_mouth_southwest_pass, mississippi_head_of_passes, mississippi_source_lake_itasca, new_orleans, st_louis

Key pixel coordinates in us_basemap space: Indianapolis (4184, 1223), Palo Alto (586, 1456), NYC (5399, 1129), Boston (5694, 964), Mississippi mouth / Southwest Pass (3859, 2307), Head of Passes (3875, 2285), Lake Itasca (3279, 476).

## Caveats

- Blue Marble shows a July 2004 cloud-free composite. Water is deep navy and the Great Lakes are nearly black. Grade it in CSS if needed.
- The CC0 cloud map has a visible horizontal seam over the Pacific off Washington, near lat 45 (about y 700 in clouds_us_aligned). Avoid that strip, or use the separate cloud patches.
- us-atlas 10m boundaries are generalized (1:10M), which is fine at 1080p. They do not match the Blue Marble coastline exactly in places such as the Chesapeake Bay and Louisiana marsh.

---

## Added by asset agent C (2026-10-29): relief maps, beige US, old maps

### Generated relief basemaps (ref R12 look) — `tools/gen_relief.py`, geodata via `tools/gen_geodata.py`
Elevation: **AWS Terrain Tiles** (terrarium PNG), https://registry.opendata.aws/terrain-tiles/ (tiles `https://s3.amazonaws.com/elevation-tiles-prod/terrarium/{z}/{x}/{y}.png`). Built from public-domain / open sources (SRTM, GMTED2010, ETOPO1, USGS NED…). Suggested credit: "Terrain: Mapzen Terrain Tiles (SRTM/GMTED/ETOPO1, USGS)". Lakes masked with Natural Earth `ne_10m_lakes` (PD). Own hillshade (az 315°, alt 42°, + soft north light), light grey land, navy-grey water (#2e3e4a).

| File | Size | Bounds / projection | Notes |
|---|---|---|---|
| us_relief_grey.jpg (+ .json) | 6400x3200 | **same pixel space as us_basemap.jpg / us_overlay.json**: x=(lon+128)*100, y=(52-lat)*100 | A43. z7 tiles, exaggeration 5. Cross-dissolves 1:1 with the Blue Marble. `us_relief_mask_CA.png`, `us_relief_mask_IN.png` = state alpha masks in that space (for halftone/vermilion fills, CSS mask-image) |
| california_relief_grey.jpg (+ .json, california_mask.png) | 4000x3680 | lon −125.5…−113, lat 31.5…43, 320 px/deg: x=(lon+125.5)*320, y=(43−lat)*320 | SC075 (R12 California). z9 tiles. JSON has state paths (CA + neighbours) and places (palo_alto, stanford_main_quad, hp_garage, SF, LA, …) |
| indiana_relief_grey.jpg (+ .json, indiana_mask.png) | 2200x2200 | lon −89.5…−84, lat 37…42.5, 400 px/deg: x=(lon+89.5)*400, y=(42.5−lat)*400 | SC008 (R12 Indiana, navy). z9, exaggeration 14 (Indiana is flat). Places: indianapolis, eli_lilly_hq_indianapolis, bloomington_in, chicago |

### Beige muted US map (ref R11) — `tools/gen_us_beige.py`
| File | Size | Notes |
|---|---|---|
| us_beige.svg | viewBox 6400x3200 (same space as us_overlay.json) | A44. Vector: `#water` rect, `#neighbours` (Canada/Mexico/…, grey-blue), `#states` with `<path id="st-XX">` beige #e6d6b2 + ink 3 px borders @0.55, `#lakes`. Fill a state vermilion by restyling `#st-CA`. |
| us_beige_3840.png | 3840x1920 (scale 0.6 of the overlay space: x=(lon+128)*60, y=(52−lat)*60) | Raster plate: paper_cream_01 texture multiplied inside states + soft watercolour edge darkening, ink borders. |
Boundaries: us-atlas states-10m (US Census, PD) + Natural Earth 1:50m admin-0 countries and lakes (PD, https://github.com/nvkelso/natural-earth-vector). Paper texture: Texturelabs (see assets/textures/SOURCES.md).

### Old map scans — `assets/maps/old/`
| File | Size | Source | Licence |
|---|---|---|---|
| usgs_palo_alto_1899_topo.jpg (+ _grey.jpg, .json) | 4983x5958 | A35. USGS 1:62,500 Palo Alto, CA quadrangle, edition Mar. 1899 (reprint June 1906). USGS National Map historical topo item 298455, GeoTIFF https://prd-tnm.s3.amazonaws.com/StagedProducts/Maps/HistoricalTopo/GeoTIFF/CA/CA_Palo%20Alto_298455_1899_62500_geo.tif (found via https://tnmaccess.nationalmap.gov/api/v1/products?datasets=Historical%20Topographic%20Maps) | Public domain (US federal work, USGS). Credit: "USGS Historical Topographic Map Collection" |
| usgs_boston_1903_topo.jpg (+ _grey.jpg, .json) | 4738x5963 | A25. USGS 1:62,500 Boston, MA quadrangle, edition July 1903, item 352504, https://prd-tnm.s3.amazonaws.com/StagedProducts/Maps/HistoricalTopo/GeoTIFF/MA/MA_Boston_352504_1903_62500_geo.tif. Shows Cambridge/Harvard, Back Bay, Charles River (MIT's Cambridge campus opened 1916, so its site is still empty fill here — MIT 1903 was at Copley Sq.; both points in the JSON) | Public domain (USGS) |
| rand_mcnally_railroad_map_us_1920.jpg (+ _grey.jpg, .json) | 3840x2827 | A24. "Rand McNally new official railroad map of the United States and southern Canada" (1920), Library of Congress Geography & Map Division 2006627698 via Commons: https://commons.wikimedia.org/wiki/File:Rand_McNally_new_official_railroad_map_of_the_United_States_and_southern_Canada._LOC_2006627698.jpg (original 11841x8718; only the 3840 thumbnail could be fetched — 5120/6000/7680 thumbs failed) | Public domain (published 1920, LOC: no known restrictions) |

Geodata in the old-map JSONs: topo quads have the 4 neat-line corner pixels + lon/lat (15′ quads) and a bilinear lon/lat→px formula (polyconic; ~10–40 px error at 5000 px — check visually before pinning a tiny point); pre-computed places (stanford_main_quad, university_ave, hp_garage_367_addison, mit_great_dome_1916, mit_boston_tech_copley_1903, harvard_yard, harvard_square, state house, kendall_square…). The railroad map has hand-picked control points (SF, Palo Alto≈, Sacramento, Reno, LA, Chicago, Indianapolis, NYC, Boston) and a Palo Alto→Boston route guide polyline. `_grey` variants = paper/ink duotone (R10 look). Raw GeoTIFFs not kept (re-download from the URLs).

## russia/ — Russia → Saint Petersburg relief maps (sample x01, ref R12)

All three use `x = (lon − lon0) · ppd · 0.5`, `y = (lat1 − lat) · ppd` (equirectangular with a 60°N standard parallel,
`gen_relief.py --xscale 0.5`). Geodata (Russia outline, St Petersburg urban area, Neva, placements of the finer maps inside
the wide one) is in `russia/russia_spb.json` (`tools/gen_russia_spb_geo.py`).

| file | size | source | licence |
|---|---|---|---|
| russia/russia_relief_grey.jpg | 5250x3360 | lon 10..185, lat 28..84, ppd 60. AWS Terrain Tiles z6 (terrarium, https://registry.opendata.aws/terrain-tiles/), `tools/gen_relief.py 6 10 28 185 84 60 … --xscale 0.5 --lakes ne_10m_lakes --exag 4` | Terrain data: public-domain sources (SRTM, GMTED2010, ETOPO1). Credit "AWS Terrain Tiles" |
| russia/gulf_finland_relief_grey.jpg | 3300x2400 | lon 20..42, lat 56..64, ppd 300, z8, `--exag 1.6` | same |
| russia/spb_relief_grey.jpg | 3600x1800 | lon 28.6..32.2, lat 59.45..60.35, ppd 2000, z11, `--exag 2.5 --smooth 2.5 --landpoly ne_10m_admin_0_countries` (DEM coast is boxy at city zoom) | same + Natural Earth (public domain) |
| russia/russia_spb.json | — | Natural Earth 1:50m admin-0 countries (Russia), 1:10m urban areas, 1:10m rivers (Neva), from https://github.com/nvkelso/natural-earth-vector/tree/master/geojson | Public domain (Natural Earth) |
