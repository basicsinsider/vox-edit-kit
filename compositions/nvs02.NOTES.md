# nvs02 — NOTES (editor, 2026-11-17)

Segment: master 109.250–229.500 (DUR 120.250), 27 scenes. Refined plan: `project/nvidia/EDIT_NOTES_nvs02.md`.

## Checks
- `npx --yes hyperframes@0.8.217 lint` (sandbox work/nvs02): 0 errors in nvs02.html (warnings only: the usual nested_media_start
  notices on timed face-cam videos, duplicate img discovery, file length). The 25 errors in that run are in other compositions.
- `tools/sync_audit.py compositions/nvs02.html --transcript transcript_nv.json`: **0 cue(s) flagged** (every text cue −0.06 s; the
  "UNITED STATES" cue at 169.18 is matched to "a" 169.16 by the audit but sits −0.06 before "US" 169.24).
- Timeline dump (puppeteer + chrome-headless-shell, seek 0→120.25): `tl.duration()` = **120.25**, no page/console errors.
- Hold audit (tweens ending < 0.5 s before a cut): fixed sc001, sc004, sc005, sc015, sc019; remaining hits are camera/ground moves only.
- Snapshots of every scene (start+0.3, middle, last 0.5 s) looked at; fixes made for label overlaps, title-bar text roughness (now only
  the ink bars are torn, the type is clean), map framing/margins, press-release push, close-up head crop (C = 1.42), flag/label overlap.

## Face cam
Intro pops (to 162.2): 113.43–115.56 (C), 143.96–146.36 (M), 151.83–153.48 (W), 160.20–162.2 (M) = 4 pops of 1.7–2.4 s.
After 162.2: 162.2–164.28, 174.79–177.35, 191.19–197.59 (M→C), 205.19–207.45, 218.48–225.19 (M→C) = 20.0 s of 67.3 s = **≈ 30 %**
(a little under 35 %: the lines in between are all explanatory — law, map, date, presidents, step chart). Whole segment 23 %.
Framing changes on the joins 113.43, 151.83, 162.33 (M→W), 218.48; no face-cam shot runs across a join with the same framing.

## Reference ids used
`ast_1b3c60efa9fc4241` (sc003 halftone portrait + bold type), `ast_3d5f46c4c01248c5` (sc004 bars, serif title with italic word),
`ast_06720d0b255d4d29` (sc005 curves on black), `ast_e1ede4fafbd84a66` (sc009 title card — the JOB-card design family),
`ast_4b7fb0fe0a134429` (sc022 two leaders with the chained object between).

## Effects
Halftone cut-out, bar chart + count (yellow key number + highlighter), line chart draw-on, isotype-free price bars (12 fps drops),
pinned-card board with pull-back, torn-paper title card, photo plate + fringe, 3D document tilt + focus hunt, Pacific map (fills,
counter-scaled labels, drawn barrier, camera pan, object hitting the wall), footage, document push + body-text highlighter +
odometer, duotone cut-outs with drawn chains + lock, step chart, markup ring + slash. Transitions: whips (plain, vertical,
light-flash), hard cuts on action, paper slides, punch-ins.

## Assets
Shared: people/huang_4.jpg (+ derived halftone), biden_cut.png, trump_cut.png; hardware/cutouts/h100_sxm_cutout.png (sc001, sc015,
sc027); places/commerce_hoover_building_1.jpg; news/s03_bis_press_2022.jpg; docs/bis_rule_2022-10-07_p1.png (sc009 texture, sc019,
sc022 card); footage/fab_wafer_lithography_st.mp4, fab_chip_assembly_st.mp4; logos/flag_us.svg, flag_china.svg; maps/kit/pacific_night.
Own derived files: `assets/nvidia/nvs02/derived/` (SOURCES.md there): halftone, pacific China/US fill SVGs, fab still.
Nothing missing or substituted. Numbers on screen = Sam's (60 %, 17 % — no source label; RESEARCH says Huang said "mainstream chips").

## Deviations from the lead's plan
- 001: instead of a 6 s face cam (pops must be 1–2 s) → chips-through-the-ban graphic, then the pop on "what does that say about the ban?".
- 002 split into a podcast portrait shot (ref 1b3c) and a separate bar-chart shot (ref 3d5f); bars in the order spoken (NOW first).
- 004 pop shortened, the "whole picture" line gets a pull-back board of the three charts.
- 006 split: pop (151.83–153.48), Commerce building for "the people who implemented it", pop on "decide".
- 007 uses the real BIS **press release** (7 Oct 2022); the Federal Register rule page is used for the date (009) and the title texture.
- 008 split around a face-cam emphasis ("the most powerful part is very important") + fab footage for the machines + second map beat.
- 013: no "STILL IN PLACE" stamp (would be a narration caption) — H100 + drawn ban ring + China label instead.

## Boundaries
First shot: fresh night graphic (nvs01 ends on a map → no map at my start). Last shot: H100 + ban ring, push-in (ease-in 228.95–229.50)
= cut on action into nvs03.

## Gotchas / helpers for the lead (MANUAL candidates)
- `FX.markup.pen` defaults to `multiply`: on night grounds pass `blend: "normal"` or the line disappears.
- `tools/halftone.py` on a 1080 px portrait crop loses the face (dots too coarse): upscale the crop 2× first, then `--cell 8`.
- A filter on a title bar distorts its text too — put the torn-edge filter on a background child (`.n2-tbg`), text on top.
- Pacific kit map at s ≥ 0.4463 (2420 px tall) can't show the US and China together — pan, and anchor the US label right-aligned.

## QA fixes (lead review, 2026-11-17)
- sc019: OCTOBER 7 odometer tightened (dur 0.6, stagger 0.03): settles by master 187.60 (≤ 0.81 s after "October") and holds; snapshots 76–81 s every 0.5 s checked.
