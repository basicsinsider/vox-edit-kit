# Texture sources — taiwan-edit

Downloaded 2026-10-29. Each texture comes in three versions:
- `name.jpg` / `name.png`: a 1920 px wide working copy.
- `name_hires.jpg`: the full-resolution re-encode (q95).
- `_raw/`: the original download, untouched. Texturelabs serves single JPGs, so there were no zips to extract.

## Licenses
- **Texturelabs** (https://texturelabs.org/terms): Free for commercial use, and attribution is optional. You **may not** resell or redistribute the textures in their original form, for example in packs or templates. You also may not use them to train AI models. Using them inside a finished video is fine.
- **Wikimedia Commons CC0**: Public-domain dedication. No attribution required.
- **Synthetic grain**: Generated locally with Python/numpy. No third-party rights.

## Blend-mode key
- **Black background** → Screen, Lighten, or Add.
- **White/light background** → Multiply or Darken.
- **`_norm`**: Desaturated, with the histogram median shifted to 128 (50% gray) and contrast left unchanged. Use Overlay, Soft Light, or Linear Light. The 50% gray is neutral, so the texture shows without shifting color or exposure.

## Files

| File | Source | License | Dims (hi-res) | Recommended blend |
|---|---|---|---|---|
| dust_01.jpg | Texturelabs Grunge 353 "Film print dust", https://texturelabs.org/textures/grunge_353/ | Texturelabs | 4240x3014 | Screen (black bg, white specks) |
| dust_02.jpg | Texturelabs Grunge 355 "Film scan dust" (slight red tint; desaturate if needed), https://texturelabs.org/textures/grunge_355/ | Texturelabs | 4240x3381 | Screen |
| dust_03.jpg | Texturelabs Grunge 316 "Fine details specks", https://texturelabs.org/textures/grunge_316/ | Texturelabs | 4240x2828 | Screen |
| grain_01.jpg / grain_01_norm.jpg | Texturelabs Grunge 318 "Fine grunge and scratches" (black, dense fine grain), https://texturelabs.org/textures/grunge_318/ | Texturelabs | 4240x2828 | Original: Screen. _norm: Overlay/Soft Light |
| grain_02.jpg / grain_02_norm.jpg | Texturelabs Paper 236 "Medium tooth overlay" (gray, fine even grain), https://texturelabs.org/textures/paper_236/ | Texturelabs | 4240x2828 | _norm: Overlay/Soft Light |
| grain_03_synthetic_tile2048_norm.png | Generated (Gaussian grain plus a coarser clump layer, FFT-filtered so it **tiles seamlessly**) | Own work | 2048x2048 | Overlay/Soft Light, 10–30% opacity |
| grain_04_synthetic_seq_1920x1080/grain_seq_0000–0023.jpg | Generated: a 24-frame animated grain loop (import as an image sequence at 24 fps) | Own work | 1920x1080 | Overlay/Soft Light |
| halftone_01.png / _norm.jpg | Texturelabs Grunge 354 "Newspaper halftone pattern", https://texturelabs.org/textures/grunge_354/ | Texturelabs | 4240x2926 | Original: Multiply. _norm: Overlay/Linear Light |
| halftone_02.png / _norm.jpg | Texturelabs Grunge 351 "Tiny halftone overlay" (very fine screen; use `_hires` / `_norm_hires` scaled in the comp to avoid moiré) | Texturelabs | 4240x3156 | _norm: Overlay/Linear Light |
| halftone_03.png / _norm.jpg | Texturelabs Grunge 356 "Newspaper photo halftone", https://texturelabs.org/textures/grunge_356/ | Texturelabs | 4240x2931 | Original: Multiply. _norm: Overlay/Linear Light |
| newsprint_01.jpg / _norm.jpg | Texturelabs Paper 290 "Vintage newspaper plain" (blank aged newsprint), https://texturelabs.org/textures/paper_290/ | Texturelabs | 4240x2828 | Original: Multiply (or a background plate). _norm: Overlay/Soft Light |
| newsprint_02.jpg / _norm.jpg | Texturelabs Paper 377 "Antique newspaper" (faint print layout visible), https://texturelabs.org/textures/paper_377/ | Texturelabs | 4240x3034 | Multiply / _norm Overlay |
| paper_cream_01.jpg / _norm.jpg | Texturelabs Paper 331 "Light antique old paper" (cream parchment, soft stains), https://texturelabs.org/textures/paper_331/ | Texturelabs | 4240x3100 | Multiply / _norm Soft Light |
| paper_cream_02.jpg / _norm.jpg | Texturelabs Paper 237 "Bright clean cold press" (near-white, very subtle), https://texturelabs.org/textures/paper_237/ | Texturelabs | 4240x2828 | Multiply / _norm Soft Light |
| paper_fiber_01.jpg / _norm.jpg | Texturelabs Paper 240 "Natural fiber paper", https://texturelabs.org/textures/paper_240/ | Texturelabs | 4240x2828 | _norm: Overlay/Soft Light |
| scratches_01.jpg | Texturelabs Grunge 320 "Specks and scratches", https://texturelabs.org/textures/grunge_320/ | Texturelabs | 4240x2828 | Screen |
| scratches_02.jpg | Texturelabs Grunge 319 "Scratches light grunge" (lighter), https://texturelabs.org/textures/grunge_319/ | Texturelabs | 4240x2828 | Screen |
| lightleak_01.jpg | Texturelabs LensFX 169 "Orange light leaks", https://texturelabs.org/textures/lensfx_169/ | Texturelabs | 3000x2000 | Screen/Add |
| lightleak_02.jpg | Texturelabs LensFX 147 "Warm light leaks" (orange bokeh blob), https://texturelabs.org/textures/lensfx_147/ | Texturelabs | 4240x2828 | Screen |
| lightleak_03.jpg | Texturelabs LensFX 131 "Burned light leaks" (film-edge burn), https://texturelabs.org/textures/lensfx_131/ | Texturelabs | 4000x2668 | Screen |
| tv_frame_01.png | Philco "Predicta" TV (1960), Museum für Angewandte Kunst Köln, photo by Daderot. https://commons.wikimedia.org/wiki/File:Predicta_television,_Philco,_Philadelphia_PA,_1960,_plastic,_sheet_steel,_glass,_wood_-_Museum_f%C3%BCr_Angewandte_Kunst_K%C3%B6ln_-_Cologne,_Germany_-_DSC09668.jpg | CC0 | 3109x2963 RGBA | Normal; place footage on the layer **below** |
| tv_frame_01_withbg.png | Same photo, uncropped, with the museum wall kept and only the screen transparent | CC0 | 3745x3541 RGBA | Normal |

### tv_frame_01 screen geometry
- The background is removed and the CRT face is transparent, with a 2 px feathered edge.
- **Screen bbox in tv_frame_01.png:** x0=317, y0=303, x1=2354, y1=1788. As x,y,w,h that is (317, 303, 2037, 1485). Center (1335, 1045), roughly 1.37:1.
- **Screen bbox in tv_frame_01_withbg.png:** x0=722, y0=536, x1=2759, y1=2021.
- **Shape:** The screen is a rounded "pillow" superellipse, not a rectangle: |dx/1018|^4 + |dy/742|^4 <= 1. Scale 4:3 footage to cover the bbox. The PNG's alpha does the masking.
- Full details are in `tv_frame_01_screen.json`.

## Not available / notes
- **Film grain**: Texturelabs has no dedicated 35mm grain still or video. grain_01 and grain_02 are its closest fine-grain textures. grain_03 (tileable) and grain_04 (animated) are generated locally to fill the gap.
- **Vintage TV / CRT screen texture**: Texturelabs has none. Its Lens Effects > Viewfinder set is camera viewfinders only, so it was skipped. The TV frame comes from Wikimedia Commons instead.
- **Login**: None of the downloads needed a login or account.

## Added by asset agent C (2026-10-29)
| File | Source | Licence | Size | Blend |
|---|---|---|---|---|
| cork_01.jpg | A47. Patch-quilted (random flips, 50 px feathered seams, lighting flattened, slightly warmed) from "NIND corkboard ISO200.png" by Trougnouf (Benoit Brummer), https://commons.wikimedia.org/wiki/File:NIND_corkboard_ISO200.png (3840 thumb kept in `_raw/nind_corkboard_iso200_3840.png`) | **CC BY 4.0** — credit "Cork texture: Trougnouf (Benoit Brummer), CC BY 4.0" in the scene micro-credit/end credits | 3840x2160 | Normal (full-frame ground for SC066/SC074) |
| watercolour_edge_mask_01.png | T2. Own work (CC0): ragged watercolour top edge (random walk + paper_cream_01 noise displacement), white = paint, slightly denser pigment at the edge. Use as CSS mask-image on R11 fills / R1 bar tops (stretch horizontally) | own / CC0 | 2048x512 L | mask |

No Texturelabs cork exists that could be fetched without login; Texturelabs licence not needed. T1 (foxed document paper) not made — paper_cream_01/02 cover it.

## TV frames #2–#4 (asset gatherer B) — screen transparent (alpha 0, ~1 px feather); museum background KEPT (not keyed) — mask/crop in comp or blur bg
| file | subject | source | licence | dims | screen bbox xywh (in file) |
|---|---|---|---|---|---|
| tv_frame_02.png (+_withbg = full photo) | RCA Victor TRK-12 (1939) mirror-lid television, front, lid open; the "screen" is the CRT seen in the lid mirror (small: footage reads as a reflected image) | https://commons.wikimedia.org/wiki/File:Television,_RCA_Victor_TRK_12,_1939,_Wolfsonian-FIU_Museum.JPG (Wolfsonian-FIU, photo Wmpearl) | CC0 | 1686x2744 | 711,424,414,281 (rounded top corners) |
| tv_frame_03.png (+_withbg) | Bush TV22 portable television (UK, 1950), Bakelite, front | https://commons.wikimedia.org/wiki/File:TV22a_portable_television_receiver,_designed_and_manufactured_by_Bush,_1950_-_Design_Museum,_Kensington_-_London_-_DSC01605.jpg (Daderot) | CC0 | 2741x2601 | 724,638,1380,1080 (superellipse n=3) |
| tv_frame_04.png (+_withbg) | Westinghouse Television Model 196, c.1949, console on legs (no doors) | https://commons.wikimedia.org/wiki/File:Westinghouse_Television_Model_196,_c._1949_-_National_Electronics_Museum_-_DSC00058.JPG (Daderot) | CC0 | 2640x4464 | 711,574,1110,960 (superellipse n=4) |
Full geometry in `tv_frame_0N_screen.json`. Raw downloads in `_raw/tv/` (also scott.jpg: Scott 6T-11 mirror TV, CC0 Daderot, https://commons.wikimedia.org/wiki/File:Scott_Model_6t-11_Television,_vertical_tube_with_mirror_-_National_Electronics_Museum_-_DSC00190.JPG — unused alternate).

- `tv_frame_03_cut.png` (seg04 editor) — tv_frame_03.png with the white/beige museum background keyed out (border flood-fill on luminance + hand polygon trims at the shoulders, bottom label strip removed). Same CC0 source (Daderot). Screen geometry unchanged: `tv_frame_03_screen.json`.

### Added 2026-10-31 (Krish's picks). The full-resolution original of each is in `_raw/Texturelabs_Paper_NNNL.jpg`.
| File | Source | License | Dims (hi-res) | Recommended blend |
|---|---|---|---|---|
| paper_graph_01.jpg / _norm.jpg | Texturelabs Paper 300 "Blue lines graph paper", https://texturelabs.org/textures/paper_300/ | Texturelabs | 4240x3194 | Background plate for charts, or Multiply |
| paper_lined_01.jpg / _norm.jpg | Texturelabs Paper 152 "Antique lined paper" (portrait, punched holes), https://texturelabs.org/textures/paper_152/ | Texturelabs | 3258x4240 | Background plate (notes, lists), or _norm Overlay/Soft Light |
| paper_stained_01.jpg / _norm.jpg | Texturelabs Paper 353 "Stained vintage paper" (coffee rings), https://texturelabs.org/textures/paper_353/ | Texturelabs | 4240x3161 | Multiply |
| paper_torn_01.jpg / _norm.jpg | Texturelabs Paper 351 "Torn and folded" (black, white fold lines and tears), https://texturelabs.org/textures/paper_351/ | Texturelabs | 4240x3016 | Screen (dark background) — folded-paper overlay |
| paper_blueprint_01.jpg / _norm.jpg | Texturelabs Paper 380 "Antique blueprint" (blue), https://texturelabs.org/textures/paper_380/ | Texturelabs | 4240x3317 | Background plate (plans, diagrams), or _norm Overlay/Soft Light |
