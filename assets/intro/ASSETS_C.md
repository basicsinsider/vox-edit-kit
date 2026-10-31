# Asset gatherer C — maps, vintage grid/ruled papers, face-cam cut-outs (2026-10-31)

Licences/sources in detail: `maps/SOURCES.md`, `papers/SOURCES.md`, `../facecam/README.md`. Every file below was looked at.

| id | file | what | size | licence | fits story moment |
|---|---|---|---|---|---|
| C01 | maps/taiwan_relief_grey.jpg (+json) | grey shaded relief of Taiwan, navy sea | 2480×3040 | own render of AWS Terrain Tiles (PD sources) | "Taiwan's telephone exports…", "built Taiwan into a chip superpower", locator for Hsinchu (places in JSON) |
| C02 | maps/taiwan_mask.png / taiwan_land_mask_all.png | main-island alpha mask / all land | 2480×3040 | derived | celadon Taiwan fill, halftone fill, CSS mask-image |
| C03 | maps/pacific_relief_grey.jpg (+json) | Pacific-centred grey relief Taiwan → US West Coast → New York, country paths + great-circle routes | 5700×1440 | AWS Terrain Tiles (own render) | "Taiwan exports to the US" arrows; "Tsao flies to New York" flight route; "flies home on top of the world" |
| C04 | maps/pacific_basemap_desat.jpg / pacific_basemap.jpg | same space, NASA Blue Marble (35 % sat / full colour) | 5700×1440 | PD (NASA) | same moments, satellite look; cross-dissolves 1:1 with C03 |
| C05 | maps/pacific_land_mask.png | land mask | 5700×1440 | derived | US/Taiwan fills |
| C06 | maps/world_basemap_desat.jpg (+json, 241 country paths, 40 places) | whole-world Blue Marble, desat | 10800×5400 | PD (NASA) + Natural Earth (PD) | "countless countries tried to recreate Silicon Valley and failed" (light up countries / copy-site pins: Bangalore, Shenzhen, Tel Aviv, Sophia Antipolis, Skolkovo, Tsukuba…) |
| C07 | maps/world_countries.svg | Natural Earth 50m country outlines, `<path id>` per country | viewBox 10800×5400 | PD | same; per-country colour/stroke animation |
| C08 | maps/formosa_1943_japanese_aviation_map.jpg (+json) | colour Japanese military aviation map of Taiwan (printed 1935), routes + compass roses | 3840×3500 | PD (Commons/Geographicus) | D10 tilted close-up topo map with route lines; "Taiwan in 1984…" period texture; Hsinchu 新竹 visible |
| C09 | maps/hsinchu_shinchiku_1945_us_army_city_plan.jpg (+json) | US Army 1:10,000 city plan of Hsinchu (Shinchiku), 1945 | 3840×3243 | PD (US Gov) | D09 old city map for "Hsinchu"; **park/UMC/TSMC are off-sheet** (arrow off the SE edge) |
| C10 | maps/hsinchu_s2cloudless2016.jpg (+json with OSM paths) | satellite view of Hsinchu + science park | 3728×2823 | CC BY 4.0 (EOX Sentinel-2 cloudless 2016) — on-screen credit | D14 satellite + highlighted districts + yellow route: "breaks ground across the street from UMC", "Hsinchu Science Park, a replica of Silicon Valley" |
| C11 | maps/hsinchu_park_osm_z16.jpg (+json) | OSM street map of the park (TSMC HQ, Fab 12, UMC labelled) | 1398×1180 | ODbL (© OSM contributors) | tracing base / close-up for "across the street"; redraw in our style from JSON paths |
| C12 | (coordinates) | **TSMC HQ/Fab 12A 24.77292 N 121.01275 E; UMC (Li-Hsin 6th Rd) 24.77222 N 121.01503 E** — across Li-Hsin 6th Rd, ~230 m; UMC main campus 24.77035 N 121.02047 E | — | OSM/Nominatim | across-the-street beat |
| C20 | papers/ke1960_mm_grid_green* | mm graph paper | 1376×1180 native | rulings = blank form (not copyrightable); see licence note | D01/D04 chart grounds |
| C21 | papers/ke1960_10x10_grid_black* | 10×10 statistical grid | 780×990 | same | chart grounds, "4 million → 24 million" bars |
| C22 | papers/ke1960_log_grid_green* | log-log sheet | 792×816 | same | growth curve ("6× in 12 months") |
| C23 | papers/ke1960_cross_section_green* | engraved cross-section strip | 1616×600 | same | idea card / foundry concept notes |
| C24 | papers/ke1960_business_ruled_orange* | business statistical ledger ruling | 1352×888 | same | sales up / down (phone boom dies) |
| C25 | papers/ke1960_progress_chart_orange* | month/day progress chart | 1416×904 | same | timeline 1983 → 1984 → "two years later" |
| C26 | papers/ke1960_polar_orange* | polar sheet | 770×1036 | same | reserve (rivalry circle diagram ground) |
| C27 | papers/ke1960_cover_grid_blue* | blue-grey grid (front cover) | 820×1380 | same | D15 relationship-diagram ground |
| C28 | papers/ke1960_back_cover_grid_blue* | blue-grey fine grid with crease | 1188×3052 | same | tall paper ground, vertical pans |
| C29 | papers/ke1960_page_0023/0045/0059* | full aged catalogue pages | 2448×3168 | text possibly © K+E 1960 → props only, blurred | paper-stack collage, D07 collage |
| C30 | papers/ledger_specimen_p318.jpg | bound ledger spread, red ruling, handwriting | 1920×1952 | CC0 | "record profits", board-room books (blurred) |
| C31 | papers/ledger_specimen_p38.jpg | ledger spread, sparser | 1920×1966 | CC0 | same |
| C32 | papers/ledger_fragment_1880_folded.jpg | blank ledger fragment with folds | 1920×1576 | CC0 | fold/stain overlay |
| C40–C45 | ../facecam/fc_<start>.mp4 (+_fg.webm, _bg.webm) | narrator windows 170.5, 195.8, 245.8, 251.0, 256.0, 261.5 | 1920×1080, 24 fps | own footage | face-cam beats (see facecam/README.md) |

## Missing / notes
- **Sharp close-up aerial of the park**: only 10 m Sentinel-2 (soft below ~1.5 km frame width). Taiwan NLSC orthophotos are sharp
  and open-licensed but watermarked ("NLSC 2025") → rejected. For the across-the-street shot, use C11/C10 + our own drawn blocks from
  the OSM paths in the JSON, or a PD/CC photo of the park (gatherer A).
- Historical (1980s) map of the science park: none found free. 1945 AMS sheet stops ~1.5 km west of the park.
- Taipei→New York great-circle leaves the top of C03 (polar route); draw a stylised arc or a 2-leg route (Taipei→Anchorage/SF→NY).
- Texturelabs graph/lined/stained paper (5 URLs in papers/SOURCES.md) need a manual download (site button).
- K+E: catalogue copyright renewal not verified — use rulings only as grounds; full pages as blurred props.
- Old ledgers carry unrelated handwriting → blur or crop to rulings.
- No quadrille engineering-notebook scan found in the time box (archive.org/Commons searches empty).
