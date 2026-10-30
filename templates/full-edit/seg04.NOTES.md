# seg04 — VO 296.23–398.46 (102.23 s), SC048–SC062

Built all 15 scenes in `compositions/seg04.html` (one timeline, cues as `T(vo)`), SFX in `seg04.sfx.json` (81 markers).
Lint 0 errors (only the framework's generic "file too large"/nested-media-start warnings); `sync_audit` 0 flagged.

| SC | ground | build |
|---|---|---|
| 048 | paper | `born` + 1900 count (1850→1900, 12 fps), vermilion rough underline; 1900 slides left, `2000` navy, hand-drawn `=`; `AGE = 1924 − 1900 = 24` double counter; slides off left |
| 049 | night | Vox layers: Stanford aerial c1920 (bg), arcade panel, 1916 title-page panel; young Terman halftone cutout; `accomplished` fill. Book panel slides to centre = SC050's opening page (match) |
| 050 | paper | 1916 book in 3D on paper, Lewis Terman halftone circle + name/role, rough yellow highlighter on the title, 3D page turn to the IQ distribution chart, `IQ` highlighter, push into the bell curve |
| 051 | night | TV #3 Bush TV22 (keyed copy `tv_frame_03_cut.png`) on a table, lamp glow; Prelinger classroom test footage with CRT grading; power-on + CRT-off |
| 052 | paper | s08 collage re-timed: Terman 1920 card (Theta Xi crop), Stanford aerial card, timeline 1918–1926 (axis top 935, 24 px vermilion dot, s08 ticks), `24` stamp, `1924` on the tick; railroad-map card swaps in and the board pushes into it |
| 053 | paper/map | **R10-A** Rand McNally 1920 map on a tilted plane, yellow marker (Catmull-Rom of the JSON route, 12 fps draw) with a camera that follows the marker head, yellow circle + numbered pin `1` + `MIT` label at Boston; text slip lower-left |
| 054 | night | MIT 1925 aerial plate, fringe/weave/dust, navy soft-light (East), slow zoom into the Great Dome |
| 055 | night | cool (navy-tinted) streaks over a faint dome; `SILICON VALLEY` (t-display halate 200 px, 0.02em) rises, chokes away on "not" to a ghost outline + `?`; ghost shrinks into the navy pin |
| 056 | paper/map | **R10-B** USGS 1903 Boston topo, same tilt/marker/pin style; pins 1 MIT, 2 Harvard; yellow loop around Cambridge; `Boston`; iris closes on pin 1 |
| 057 | night | iris opens on MIT main group from Boston (pan) → iris → Harvard Widener 1915 |
| 058 | paper | triangle diagram: halftone circle nodes (Great Dome / Bush 1938 / GE Schenectady), rough ink edges drawn per node, ink "people" dots circling, push in; 6-frame crossfade to SC059 |
| 059 | night | radio-school 1940 lab footage, gate weave + flicker, bone dots looping a triangle (0.4, screen) |
| 060 | paper | MIT card + stamped GE (monogram mask), AT&T (Bell System 1921), Bell Labs (typeset) cards; three rough ink arrows into MIT |
| 061 | night | Vox layers: differential analyzer bg, MIT card panel (continuity from SC060), Edison/Langmuir tube footage panel; vacuum-tube cutout; `fund labs` fill, `professors invent` rise, `commercialize` odometer + `$` price tag |
| 062 | paper | MIT Bulletin page Course VI-A, rough yellow highlighter on "The Co-operative Course", GE 1925 lab photo drops in, texts, push into the photo |

## Deviations / substitutions
- **A29 MIT Bulletin ❌** → typeset recreation in Crimson Pro on paper (no seal, no fake catalogue number). Body copy is a neutral description of the GE co-operative course; it is a prop, not a quotation.
- **A49 vacuum tube ❌** → cutout from the Raytheon BH photo (CC BY-SA 2.0, Joe Haupt; micro-credit shown in SC061), brand lettering darkened. SC073 (seg05) may still use the original Raytheon photo — different framing.
- SC049 "Terman family": young Frederick halftone cutout + the 1916 book (no family photo available).
- SC051 uses a keyed copy of TV #3 (the PNG shipped with the museum wall); file `assets/textures/tv_frame_03_cut.png`.
- SC058 serif line reads `leading technological companies` (VO wording) instead of EDIT_NOTES' "tech".
- SC060 Bell Labs wordmark set in type (no clean logo), AT&T uses `assets/logos/bell_system_1921.png`.
- **Pins:** R10 pin *style* is fixed (Haskoy number, disc, 6 px bone ring, shadow); colour follows the West/East code — MIT/Harvard pins are **navy** (palette moments for seg04). SC085 (Palo Alto) should use the same `.seg04-pin` markup with vermilion.
- SC052 shows a small `Frederick Terman` tag on his card (cued on the spoken name at 321.59).

## R10 map snippet (for SC085, seg06)
Stage `perspective: 2200px` → plane 1920×1080 with `rotateX(18deg) rotateZ(-6deg)` (origin 960 540) → camera div in map pixels:
`translate(960-cx*z, 540-cy*z) scale(z)`. Map img filter `sepia(0.35–0.4) saturate(0.5) contrast(1.05–1.08)`, paper_cream multiply 0.45, halftone_01_norm overlay 0.32.
Marker: `stroke:#f2d33b`, width 34–40 map px, round caps, `mix-blend-mode:multiply`, opacity .92, filter `FX.roughDefs(…,{freq:0.012, scale:14})`, dashoffset posterized to 12 fps, hide the path until progress > 0 (round caps otherwise leave a dot).
Pin: 64 px disc, `border: 6px solid var(--bone)`, Haskoy 34 px number, `box-shadow 0 6px 14px rgba(0,0,0,.35)`; labels `.label-box`.

## Boundary hand-offs
- In (296.23): clean hard cut to paper (blank paper ~6 frames, `born` lands at 296.49).
- Out (398.46): final frame = `assets/archival/companies/ge_research_lab_kellogg_rice_speaker_1925.jpg` **full-frame**, upright, sepia(0.3); image ≈ 2130 px wide × 1370 px tall, horizontally centred, top edge ≈ −100 px (≈ seg05's 1.06× cover at object-position 46% 30%). Small residual scale difference (~4–5 %) at the cut.

## For the lead
- Script-local helper `gate(a,b,reg)` wraps `FX.onFrame` so weave/streaks/map cameras only run inside their scene window — candidate for fx.js.
