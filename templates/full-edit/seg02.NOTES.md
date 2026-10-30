# seg02 — notes (VO 100.25–206.27, SC018–SC034)

Built: `compositions/seg02.html` (one timeline, 17 scenes), `compositions/seg02.sfx.json` (77 markers).
Checks: lint 0 errors (sandbox `work/seg02`), `sync_audit` 0 flagged (all text cues −0.06 s before their word).
Cue convention: `T()` = word-synced text (audited); `S()` = the same function for structural moves (cuts, camera,
pins, markups), so sync_audit only lists text cues.

## Deviations / choices
- **SC018** shots: NYC = `nyc_skyline_battery_park_1929.jpg` (the 1921 file has a colour-bar scan border); GE = pan across
  `ge_schenectady_works_panorama_1907_lc.jpg` (the "General Electric Company" building is in frame) during the repeat;
  last shot = `new_jersey_edison_west_orange_lab_hoover_1928.jpg` (historic, Edison + Hoover) instead of the modern West Orange photo.
  Iris starts closed at local 0 and opens in 0.15 s (local iris helper exposing state; same geometry as FX.iris).
  Bell Labs carries the CC BY-SA micro-credit.
- **SC019** C5 student cutouts don't exist → three torn-edge halftone cards cropped (zoomed) from the 1920 student group photo.
- **SC020** made `assets/cutouts/us_halftone.png` (C6, from us_overlay conus outline). Dots start vermilion (West) and
  turn navy past the Mississippi (ink vs navy was unreadable) — same colour logic as SC032/SC033.
- **SC021** s06 kept; the "31st President" role line removed (not narrated); added `future president` (serif-i) top right.
  Highlighter kept at the approved 127.3 (camera only reaches the headline then). Ends pushing into the portrait to black.
- **SC022/SC023** one container: s07 part A → `FX.curveCut` (mid 136.70) into the 2.5D quad (s10 math, P=1200, layers
  sky −900 / title −420 / haze −200 / quad 0 / palms_left 150 / palms_right+bush 320, ×1.1 overscan so edges never show).
  Made `layers_quad/quad_seg02.png`: alpha eroded 2 px (removes the sky fringe on the roofline) and the inpainted areas
  behind the near palms darkened to foliage tone so parallax reveals look like shadow, not grey smudges. Sky graded to dusk
  so the yellow 1891 reads; 1891 rises from behind the arcade roof (bottom ~10 % tucked). Vermilion X flash at 141.48 cuts to paper.
- **SC024–SC026** run as planned; Quaker-hat doodles land at 154.95–155.4 (end of SC025, VO "Quaker too"), then the
  Hoover card flips (155.32) into the admission card; SC026 starts at 155.52 (not 154.58) so "a Quaker too" stays on the cards.
- **SC027** footage: `hoover_1928_south_america_sequence_full.mp4` (0–2.3 s, Hoover at the train) then `…_crowd_b.mp4`.
- **SC028** no "Lou Henry" label (DECISIONS #8); Lou Henry = `cutouts/cards/lou_henry_1905_cut.png` on a paper card.
- **SC030** TV #2 = `tv_frame_02.png` (RCA TRK-12) with a radial mask (its museum background fades to dark); screen shows
  `sequence_full` 8.7–13.4 s (different shots than SC027).
- **SC031** A13 missing → own-made typographic clipping ("Daily Palo Alto" masthead, headline BOARD OF TRUSTEES, body as
  grey line blocks — no invented copy). Window extends to 186.55 under SC032's 8-frame cross-fade.
- **SC032** made `assets/maps/seg02_west_fill.png` (west_of_mississippi raster, 3200×1600) instead of inlining the 200 KB path;
  Mississippi path inlined (decimated). Same basemap + grade as s02. Dots bone → navy (sky stroke) east of the river.
- **SC033** uses `assets/icons/graduate_{grey,vermilion,navy}.svg` at 56 px (R5 motif for SC078): 59 icons file into two
  columns of 5×6, one vermilion icon stays and the camera zooms into it.
- **SC034** last 6 frames: full-frame paper card slides from x=1960 to x=+180 (SC035 continues from +180); overlays switch
  to paper levels for those frames. Stanford aerial carries the CC BY-SA 2.0 Jill Clardy credit.

## For the lead
- Local helpers in the segment script (candidates for fx.js): `ink(parent, d, t, dur, o)` = draw-on stroke for any path
  (used for hats, loops, big X, career line) and the iris with `openFromClosed()`.
- `hyperframes lint` warns `nested_media_start_basis_ambiguous` on the three videos — their data-start values are composition-local (correct).
