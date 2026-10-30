# seg01 — notes (VO 0.00–100.25, SC001–SC017)

**Source of truth:** `compositions/seg01.html` is GENERATED. Edit `tools/seg01/seg01_template.html`, then run
`python3 tools/seg01/gen_seg01.py` (inlines US/Indiana map paths, HQ pins, the CA→NY route — same approach as `tools/gen_s02.py`).
Segment-only assets (resized copies / derived masks) live in `assets/seg01/`.

## What's built (scene → effect)
| scene | effect(s) | notes |
|---|---|---|
| SC001 | #8 streaks (one canvas shared with SC002 + SC005), lightleak_03 breath @1.9–4.5 | no caption (DECISIONS 5) |
| SC002 | #4 halate title + #13 random letters per word (4.26 / 5.06) | aerial (A01) blurred + sepia tint at 0.35; it **becomes panel 1 of SC003** (shrinks, unblurs, rotates) |
| SC003 | #10 Vox layers: Googleplex base, aerial / Apple Park / NVIDIA panels, newsprint overlay, each drifting | "most powerful" (rise) → "most successful" (#13 fill pop) → kicker |
| SC004 | #13 odometer STATS / NUMBERS on ledger paper, digit reels behind (7.5 % ink) | sheet slides up (12 fps) revealing SC005 |
| SC005 | s01 layout re-timed: October 2026 (random), rule, yellow 12 count | the 12 **flies** to the SC006 kicker during a 6-frame paper wipe from the bottom |
| SC006 | #2 R4 ranked bars + logo badges + R1 dashed $1T line (watercolour tops) | bars rise 12 fps from 22.0; breathe from 27.28; Micron dips to the line on "less"; dashed ghost 13th bar on "more"; tilt-down exit |
| SC007 | #3 s02 map (approved) re-timed: fg cloud fly-through, pins, West burn @35.36, river draw, East burn @40.50 | head counter 12 → 11 ("of 12 companies / located west") |
| SC008 | #20 R12: relief cross-dissolve, Indiana navy (multiply) + halftone + glowing bone edge, #19 rough circle, card with fringe plate | same camera continues from SC007 |
| SC009 | #2 R8 semicircle, 305 dots (293 vermilion / 12 navy) fill clockwise 12 fps, `.hl` on *by value*, leader labels | dots fall like confetti to reveal SC010 |
| SC010 | #12 collage: torn rough cards, tinted halftone apple (vermilion) / orange (navy), 12 fps wobble, markup ≠ | expo rush into the orange |
| SC011 | #15 curve cut (FX.curveCut) aerial → 1900s orchard slide, cut at 57.60, then #14 weave | |
| SC012 | s03 opening + equation (approved), stamp "FLIPPED" on "flipped" | EAST grows into SC013 |
| SC013 | #2 R1: navy East bar 90 %, vermilion West stub, dashed line + `.label-box` 90 % count, halftone NYC 1921 skyline, `.hl` far East | bars collapse into the dashed line |
| SC014 | #16 plate (orchard rows 1904, sepia tint, fringe, slow zoom) + #14 weave | collapses to a CRT line |
| SC015 | #11 s04 Predicta TV (approved) re-timed + power-off at 84.0 | |
| SC016 | #18 roughened tickets + Simple-Choker stamps (POSTGRADUATE / A JOB), #19 red→navy arrow, rail track | |
| SC017 | #3 R11 beige map (us_beige_3840.png), watercolour state fills (CA vermilion; NY/NJ/MA navy), dotted 12 fps route, screen-space leader labels | iris closes on New York at 100.08–100.23 (hand-off to SC018, which opens it) |

## Deviations / decisions
- **s05 (shutter montage)**: per EDIT_NOTES it belongs to SC018 (seg02); SC017 is the R11 map, so seg01 only provides the closing iris.
- **SC005 "Companies · in the United States"** moved to SC006 (kicker: [12] COMPANIES / *in the United States*), as EDIT_NOTES allowed.
- **SC007 text**: one head counter (12 → 11) plus WEST (no sub) and EAST "1 of 12", so "11 of 12" doesn't appear twice.
- **Map overlay colours** follow SEGMENTS §2 (West vermilion, East navy, overlay) instead of s02's original orange/blue.
- **SC008 leader line** is bone, not yellow (the Indianapolis pin is already the scene's yellow element).
- **SC006 logos**: monochrome ink (`filter: brightness(0)`); Amazon uses `assets/seg01/logos/amazon_mark.svg` (the original has an orange disc that became a black blob). Wordmark logos (Micron, Broadcom, Berkshire, Lilly) render wide inside the badge.
- **Watercolour bar tops** use `assets/seg01/wc_top.png` (the original mask normalised so its body is fully opaque; the original produced a visible grey band).
- **SC017 camera** holds the full US until 98.3 so California and New York are both on screen when named, then pushes east.
- **Cue helpers**: `T()` = text cues only (audited); `S()` = structural cues (same VO seconds, not audited). Local helpers worth promoting to fx.js:
  `gated(a, b, build)` (wraps FX.onFrame so FX.streaks/roughDefs/markupDefs/weave only run inside a window) and a **ceil-stepped choppy ease**
  (`FX.choppy` floors, so a 0.2 s choppy fade stays invisible for its first 1/12 s → text appeared late; the ceil version lands on the cue frame).

## Credits on screen (13 px)
SC002–003 (Coolcaesar, Daniel L. Lu, Grendelkhan), SC006 (Apple Park ghost, Daniel L. Lu), SC008 (Paul Sableman CC BY 2.0, NASA Blue Marble, Mapzen terrain),
SC010 (robin_24 CC BY 2.0, freestock.ca CC BY-SA 3.0), SC011 (Coolcaesar).

## Map continuity snippet (for SC032, SC042/43, SC075)
- Camera: `<div id="…-cam" style="position:absolute;left:0;top:0;width:6400px;height:3200px;transform-origin:0 0">`, `cam(cx,cy,z) = {x: 960-cx*z, y: 540-cy*z, scale: z}`.
- Base: `assets/maps/us_basemap_desat.jpg` 6400×3200, `filter: brightness(0.82) contrast(1.08) saturate(0.7)`.
- Fills: svg `mix-blend-mode: overlay`; West `fill="#e5482a" opacity="0.9"`, East `fill="#23415e" opacity="0.85"`, burn reveal = s02 feImage/colour-matrix filters.
- Lines: states `stroke #f4eee2 @0.22, 3px`; region edges West `#f6b49a`, East `#9cc6e8` 6px @0.7; river `#e6f4ff` 11px + `#8fd0ff` 34px glow.
- Pins: bone dot r44 + `#141312` 10px ring + halo r90; Lilly/Stanford = yellow `#f2d33b`. Clouds: `cloud_01/03_satellite.png` (opacity 0.6) with blurred black shadows (0.28).
- R12: `assets/maps/us_relief_grey.jpg` cross-dissolves 1:1; state tile `indiana_relief_grey.jpg` placed at (3850, 950) 550×550 in camera space,
  fill = `indiana_mask.png` luminance mask, navy `mix-blend-mode: multiply` + `halftone_01_norm` overlay (140 px), bone edge 6 px + 22 px blurred glow.

## Open issues
- Snapshots checked for every scene (start+0.3 and mid); no full render made from the sandbox.
- SC004 odometer glyphs show partial letters while spinning (same as the approved helper).
