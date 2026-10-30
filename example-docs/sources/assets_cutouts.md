# Cutout sources

### cutouts/src/apple_wet_isolated.jpg
- Subject: Apple isolated on white (A41)
- Source: https://commons.wikimedia.org/wiki/File:Wet_apple_isolated_on_white.jpg
- License / author: CC BY 2.0 / robin_24 — credit required (no CC0 found)
- Date: 2010-10-30
- Dimensions: 1920x1275
- Added by: asset agent A (2026-10-29), verified visually

### cutouts/src/orange_closeup.jpg
- Subject: Orange isolated on white (A41)
- Source: https://commons.wikimedia.org/wiki/File:Orange_Fruit_Close-up.jpg
- License / author: CC BY-SA 3.0 / freestock.ca — credit required (no CC0 found)
- Date: 2007-11-04
- Dimensions: 1280x853
- Added by: asset agent A (2026-10-29), verified visually

## Derived cutouts / halftones (agent A, 2026-10-29) — all made locally from the sources above or in archival/SOURCES.md
- `cutouts/terman_young.png` (+ `terman_young_ht.png`, 45° halftone cell 7) — C9. From Stanford Quad 1921 Theta Xi group (leaf n453), 3× upscale, `hyperframes remove-background` matte limited by a hand polygon; edges are partly polygonal (paper-cut look) and a thin red-ish sliver at the left collar — hide with card/torn-edge treatment. 719×1812.
- `cutouts/portraits/terman_young_circle.png` (600), `lewis_terman_circle.png` (600, from lowres 240×300 — soft, use small), `joseph_swain_circle.png` (900), `lou_henry_1905_circle.png` (900) — circle-masked portraits for R4.
- `cutouts/lewis_terman_ht.png` — C10 circular halftone, from `archival/terman/lewis_terman_1923_LOWRES.jpg` 4× upscale + halftone (hides low res). 920×920.
- `cutouts/cards/joseph_swain_cut.png`, `cutouts/cards/lou_henry_1905_cut.png` — C7 people cutouts (remove-background), ready for tint/torn-edge cards.
- `cutouts/apple_ht.png`, `cutouts/orange_ht.png` — C3 halftone fruit (colour/white key mask + tools/halftone.py). Credit CC BY 2.0 robin_24 / CC BY-SA 3.0 freestock.ca.
- `cutouts/applepark_halftone.png` — C2 ghost halftone of Apple Park ring (transparent paper, feathered ellipse). Credit CC BY-SA 4.0 Daniel L. Lu. 3180×1570.
- C5 student cutouts: NOT made — remove-background returned an empty matte on the crowded 1920 group photo; use `archival/stanford_1920s/stanford_medical_students_group_1920_quad1921.jpg` as a halftone card, or polygon-cut individuals.

## seg04 editor additions (2026-10-29)
- `cutouts/vacuum_tube_bh_cut.png` — C12 vacuum tube cutout (SC061). From `archival/terman/raytheon_bh_tube_c1925.jpg` via `hyperframes remove-background`, desaturated, brand lettering on the base darkened out. **CC BY-SA 2.0 / Joe Haupt — credit on screen** (SC061 shows the micro-credit). 1280×1791.
