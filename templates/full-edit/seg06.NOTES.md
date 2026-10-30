# seg06 — VO 496.92–600.00 (SC078–SC094) · editor notes

Root `seg06`, data-vo-start 496.92, duration 103.08. SFX markers: `compositions/seg06.sfx.json` (86 events).
Lint 0 errors · `sync_audit` 0 flagged · every scene snapshotted (start, middle, boundaries, last frame = black).

## Built
| SC | ground | primary FX | notes |
|---|---|---|---|
| 078 | paper | #2 R5 isotype | 12 A39 graduates (56 px icons in a 1.45× camera); 4 turn vermilion on "smartest", hop to a dashed East lane, walk in 8 fps steps, turn **navy** + "East" on 503.64 (self-correction: only East shown), walk off; push into darkness. Faint Stanford-seal watermark (own SVG). Opens on seg05's frozen 192 px graduate at frame centre, which settles into slot 1 (seamless match). |
| 079 | night | #8 streaks (warmer, faster) | 1938 yellow halate counts 1925→1938; "he decides to change this"; "two favorite students" + two bone graduates rise, then push to camera. |
| 080 | night | #10 Vox layered (s09) | s09 as approved, re-timed (Bill 515.72 / Hewlett 515.96 / David 516.84 / Packard 517.24). **Dropped s09's "Two of Terman's students" top label** (text policy: not narrated here; SC079 carries "two favorite students"). Packard card flies to its SC081 position. |
| 081 | paper | #19 markups | California outline (from us_states.geojson) draws on; Packard card pinned at Palo Alto; vermilion circle; "Stanford" label; navy arrow East, card slides out leaving the pin hole; "already gone". |
| 082 | night | #13 count + #16 plate | GE Schenectady postcard (sepia, fringe), GE monogram, "General Electric", around **$100** (yellow count) a month. |
| 083 | paper | #12 collage fork | Hewlett card + tag; two hand-drawn ink arrows; upper → Harvard/Widener card "studies"; lower → dashed "?" card; camera follows the lower branch into the iris. Arrows are ink, not vermilion/navy (both branches lead East; keeps West=vermilion clean). |
| 084 | night | #9 shutter (faster callback) | Bell Labs West St → GE panorama 1907 (pan) → RCA Camden 1937 → Westinghouse; iris cuts 538.62 / 540.32 / 541.56 / 542.47 (last one opens on the map). "a job" on the first plate. |
| 085 | paper | #20 + R10-C | USGS 1899 Palo Alto topo (grey, crop made for this scene), tilted rotateX 18° / rotateZ −6°; yellow rough marker Quad → Palm Dr → University Ave → Waverley → 367 Addison, camera tracks it; yellow circle + vermilion pin "1"; "THE PLAN" kicker, "a company"; expo dive into the pin. |
| 086 | night | #17 2.5D (s10) | s10 layers/math as approved, re-timed: California 549.03, PALO ALTO choke 549.91 behind the roof, dolly continues through 556.31. s10's lower third ("367 Addison Avenue / two students, one garage") dropped — no text there per EDIT_NOTES. CC BY-SA credit. |
| 087 | paper | #5 document | Thesis title page (recreation, DECISIONS Q3), 3D tilt, halftone, "his thesis" tag, rough yellow highlighter on OSCILLATOR, push in. |
| 088 | night | #16 HQ photo | HP 200A, fringe/vignette, settle + slow zoom to the dial, "audio oscillator" odometer, vermilion circle on the dial. CC BY-SA credit. |
| 089 | paper | #2 diagram | Oscillator node → ink signal arrow → "audio equipment makers" node (RCA 1937 cabinet assembler, tinted) + "for consumers"; vermilion sine draws along the line (12 fps). |
| 090 | night | #14 weave | 1940 headphone-testing footage (Prelinger), weave + flicker; procedural bone sine overlay: gentle → distorted from 575.3 → snaps clean at 577.75; "test", "good enough — or not?". |
| 091 | paper | #12 collage + #13 fill | thesis card ("PhD" tag, then "thesis" as narrated) → HP 200A card → own-made "$" price tag; "commercialize" yellow fill → ink; "all the research"; $ tag flips. |
| 092 | night | #18 choke | Four 1882 gold certificates (tinted, halftone) floating up at 12 fps over faint streaks; MONEY yellow choke; "to get it off the ground" (cued on "to" 592.47 rather than "off", so the phrase starts with its first word). |
| 093 | paper | #13 random + #19 underline | Fellowship letter (A54) flips in, pinned, Hewlett/Packard portraits taped on; "fellowship" random letters; "he makes sure they get it"; vermilion underline. |
| 094 | night | #7 textures + #14 flicker | Cross-dissolve (0.45 s) to the garage world at 0.62 brightness, light leak, flicker; fade to black from 599.43 — fully black on the last frame (DECISIONS Q7). No caption on the cut-off sentence. |

## New assets (made, all derived from existing ones)
- `assets/maps/old/usgs_palo_alto_1899_seg06_crop_grey.jpg` (+ colour `_crop.jpg`): 1500×1200 crop of the USGS topo at px (1150,1000)–(2650,2200).
- `assets/cutouts/seg06/`: `hewlett_cut.png`, `packard_cut.png` (≤1400 px copies of the cutouts), `gold_{20,50,100,1000}.jpg` (1400 w), `harvard_widener_1600.jpg`, `garage_backdrop_2440.jpg` (the s10 backdrop at its display size).

## Helpers (segment-local, not in fx.js — candidates for promotion)
- `gate(a, b, fn)`: temporarily wraps `FX.onFrame` so that any FX per-frame effect created inside `fn` (streaks, weave, roughDefs/markupDefs boil) only runs in [a, b]. Works with every existing FX helper without changing fx.js.
- `drawPath(svg, d, opts, t, dur, ease)`: dashoffset draw-on for an arbitrary path (route marker, sine wave).
- Scenes toggle `display:none` outside their windows (built while laid out, then hidden). This keeps them out of the render tree, which matters because of the lint heavy-overlay warning (28 elements).

## Open issues / notes for the lead
- Lint warnings only (no errors). They cover file size, heavy-overlay count (mitigated with display:none), duplicate img discovery (plate + fringe copies, as in the samples), and the video's local `data-start` (76.99 is composition-local, which is correct).
- SC077→SC078 match uses seg05's icon geometry (centre, 192 px). seg05's icon is bone on night; SC078 cuts to ink on paper by design.
- SC089 uses an RCA 1937 cabinet-factory photo for the "makers" node because A49 (radio/speaker cutout) is ❌.
