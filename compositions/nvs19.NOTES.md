# nvs19 — NOTES (editor, 2026-11-17)
Master 1893.917–1991.333 (DUR 97.417, 2338 frames). 11 scenes, all edited visuals (part 2 has no face cam: 0 % on camera).
Plan with exact words/cues: `project/nvidia/EDIT_NOTES_nvs19.md`.

## Wafer chart geometry (shared with nvs18 — matched to its NOTES)
sc004 OPENS on nvs18's exact framing: hall-gradient night ground, disc centre (960, 560), r 448, rim #c3c7c8 4 px @ 0.75, V notch at the
bottom, 10×10 dies 54 px (rx 4), pitch 62, die (c, r) at (654 + 62c, 254 + 62r); working = volt #86c232 + volt-light 2 px stroke + glow,
failed = #3a4247 / #2a3034 stroke. It starts with all 100 dies failed (nvs19 sets its own states: 10 % → 30 %), then at 1910.85 the whole
wafer group slides to x −300 / scale 0.86 (centre 660, r ≈ 385) to make room for the YIELD number on the right. Lit order = FX.rng(1919).
Note: nvs19 is NOT cut straight from nvs18's wafer — it opens on the Kilby IC / Texas map / TI card (1893.9–1910.7), the wafer returns at 1910.7.

## Scenes (ground · transition in)
001 Kilby's 1958 IC, graphite print + gate weave + focus hunt (night · segment start, fresh shot) · 002 US night map: TEXAS fills volt,
SILICON VALLEY pin + CALIFORNIA, pen X, push to DALLAS (map · light-flash whip) · 003 founder card — Kilby portrait cut with volt outline,
TI engineers print, TEXAS INSTRUMENTS word by word, rule, "1958" slam on "late 50s" (paper · slide up) · 004 THE WAFER CHART 10 % → 30 %,
legend 100 chips made / 30 work (night · whip) · 005 real 300 mm wafer, yellow 99.3 → 99.5 → 99.7 %, meter (night · hard cut on push) ·
006 TSMC Fab 14B + logo + TAIWAN (night · vertical whip) · 007 TSMC flywheel: VOLUME → BELOW COST → HIGH YIELD → LOWER PRICE → PROFIT →
NEXT FACTORY → NEXT CHIPS, loop closes, pull back on "topic for a different video" (paper · slide x) · 008 two tracks: chips VOLUME → BETTER
vs other industries BETTER → VOLUME, CHIPS tag, pen circle on "before" (paper · whip ←) · 009 China map, Huawei pin + logo, NVIDIA chips
pushed out east (map · flash whip) · 010 Chinese AI companies (DeepSeek, Alibaba, Tencent, Baidu) → arrows → Huawei Atlas 900 SuperPoD +
Huawei (night · hard cut on action) · 011 the flywheel callback in red around Huawei: ORDERS → YIELD → LEARNING → NEXT CHIPS, dashed ring
spins up, accelerating push = cut on action into nvs20 (night · vertical whip). Last frame: push still accelerating at 1991.333.

## Reference ids / effects
`ast_8453bcb46af0421b` (sc003 founder timeline card: cut-out portrait with thick coloured outline, sepia building print, big year + rule,
heading column — rebuilt with volt outline, ink type, no invented tagline). Effects: archival print + weave + focus hunt, map camera with
counter-scaled labels/pins + fill/outline draw + pen cross, stop-motion pin-ons, word-by-word heading, wafer isotype at 12 fps, counts,
halate key number (sc005 only), meter, plate pushes, flow-diagram loop with arcs drawn on, label boxes + pen arrows/circle, logo tiles,
map tokens. Transitions: flash whip, slide y, whip, hard cut, vertical whip, slide x, whip, flash whip, hard cut, vertical whip.

## Checks
- `npx --yes hyperframes@0.8.217 lint` (sandbox work/nvs19): 0 errors for compositions/nvs19.html (warnings: duplicate_media, file length).
- `python3 tools/sync_audit.py compositions/nvs19.html --transcript transcript_nv.json`: "0 cue(s) flagged" (all text cues −0.06; three
  listed +0.02 are matched to the neighbouring short word: lower 1945.54, next 1949.78, volume 1957.67).
- Headless timeline dump (local gsap + chrome-headless-shell, seek every 0.25 s): duration 97.417 == DUR, no runtime errors; hold audit:
  only camera pushes / incoming slides / the map-camera proxy end < 0.5 s before a cut — every key animation holds ≥ 0.5 s.
- Snapshots looked at: every scene start+0.3 / middle / last 0.5 s and every cut at ±0.05 s (no black/empty frame; whips show the kit's
  usual edge smear for 1 frame).

## Assets
Own (`assets/nvidia/nvs19/`, 3.4 MB, SOURCES.md + `gen_nvs19_assets.py`): US west night crop + states/Texas/California masks, China night
2560 + fill mask/outline (the earlier attempt's china_mask was wrong — red spilled into Mongolia/India — regenerated from kit #c-china),
TSMC Fab 14B 2560. Shared/other: pd16 kilby_first_ic_1958_ti, kilby_notebook_ti, ti_engineers_dallas_kilby (DECISIONS §10, never the
AI-generated Commons file); hardware wafer_300mm_dies (also used by nvs18 sc012 → 2 uses), huawei_atlas900_superpod_1; logos tsmc, huawei,
huawei_wordmark, nvidia_wordmark, deepseek_wordmark, alibaba_wordmark, tencent_wordmark, baidu, flag_taiwan; icons chip, factory, car.
Logos of Chinese firms shown as ink silhouettes on bone tiles (palette); Huawei keeps its red (= China).
Nothing missing. Numbers = Sam's (10 %, 30 %, 100/30, 99.3/99.5/99.7 %; UNVERIFIED per RESEARCH §21 → no source label). "1958" = the
date of Kilby's IC (RESEARCH §21 verified) on the "late 50s" line; "Jack Kilby" is a name tag (Sam doesn't name him).

## Deviations from the lead's plan
- Row 001 split into IC print / map / founder card; row 002–003 split into chart / real wafer / TSMC plate; flywheel nodes as spoken.
- Row 006 split: map (forcing NVIDIA out) + AI companies → Huawei + red flywheel callback (instead of recolouring the TSMC wheel in place).

## For the lead / MANUAL
- Gotcha: a flow-diagram "camera that travels node to node" at ≥ 1.2× crops the ring's far nodes to slivers at the frame edge; with a
  ring that fills the frame keep the camera at 1.0 with small pans (6 % toward the active node) and pull back at the end.
- sync_audit matches cues to the NEAREST word start, so a −0.06 cue before a word that follows a 0.08 s word is reported as +0.02.
