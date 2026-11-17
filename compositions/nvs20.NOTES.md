# nvs20 — NOTES (editor, 2026-11-17)

Segment: master 1991.333–2103.000 (DUR 111.667), 9 scenes, no face cam (part 2 is audio only). Plan: `project/nvidia/EDIT_NOTES_nvs20.md`.
No partial files from an earlier attempt existed (no nvs20 composition/notes/asset folder) — built from scratch.

## Checks
- Lint (sandbox work/nvs20, 0.8.217): **0 errors in nvs20.html** (warnings: duplicate_media_discovery_risk for the two huang_9 plate imgs,
  file length). The run's 25 errors are all other compositions' missing face-cam files.
- `sync_audit.py compositions/nvs20.html --transcript transcript_nv.json`: **0 cue(s) flagged** (every text cue −0.06 s; the title cue
  2062.22 and "Value" 2095.77 are matched by the audit to the neighbouring "the" but sit −0.06 before "number"/"value").
- Headless timeline dump: `tl.duration()` = **111.667**, no console errors. Hold audit: remaining hits are camera pushes/drifts only.
- Snapshots of every scene (start+0.3, middle, end) and every cut at ±0.05 s looked at; fixed: wafer layout off-frame, long blur open,
  empty frames after the sc004 whip / sc005 hard cut / sc007 slide, Huawei hop path, lined-paper punch hole (now 2700 px wide at −320 px),
  headline underline position + contrast.

## Scenes (first / last)
First: sc001 Jensen Huang at the Dwarkesh podcast table (huang_9 plate, rack focus, name tag) — fresh shot.
Last: sc009 value-chain staircase; ends on a push up the stairs (cut on action) into nvs21.
sc002 = callback to nvs02-sc004 (paper bars 17/60) varied as NIGHT wafer pies (real 300 mm wafer photo, red sector, yellow 60 %, pull-back
to a smaller "Before 2022" 17 % wafer + growth arrow). sc007 = waffle chart rebuilt from ref `ast_0b23d2c7a06c4bb3` (10×10, red box 60 % for
chips → squares flip → title swaps to "computing power" → 10 squares + yellow 10 % box; strike on the old 60 %).

## Effects / transitions
Photo plate + fringe + focus pull, wafer pie chart + counts, pen ring/arrow/check/strike/cross markups, paper diagram, Vox layered collage
(tinted panels, pull-back), product cut-outs with power bars + equals sign, conveyor isotype (phones → chips, red wash, stall), waffle chart,
article card with pen underline, staircase draw-on + isotype hops. Transitions: flash whip, paper slide →, whip ←, hard cut on action,
vertical whip, slide ↑, whip ←, slide from left — never the same twice in a row. Grounds: N N P N N N P N P.

## Assets (all shared, nothing new downloaded)
people/huang_9.jpg, huang_cut_2.png, xi_cut.png; hardware/wafer_300mm_dies.jpg, wafer_cleanroom_worker.jpg, gpu_die_ad102_closeup.jpg,
cutouts/iphone_original_2007_back_cutout.png, iphone18pro_cutout.png (shown as "iPhone 18", no "Pro"), h100_sxm_cutout.png (sc007 ghost,
sc008 "NVIDIA chips"); places/tsmc_fab14b.jpg; news/s03_register_h200_2025.jpg (real headline, credited); logos/flag_china.svg, huawei.svg,
huawei_wordmark.svg, nvidia_wordmark.svg; icons chip, ban, power_bolt, datacenter, factory. Textures: paper_cream_01/02, paper_stained_01,
paper_graph_01, paper_lined_01, newsprint_01, grain/dust.

## Decisions / for the lead
- "an iPhone." at 2028.60 is ASR for "an iPhone 18" → label "iPhone 18" cued there. Year tags 2007 / 2026 (true release years) under the phones.
- Numbers on screen = Sam's: 60 %, 17 % (no source label), 10 % (credited "Computing power: Epoch AI, Oct 2026" per RESEARCH §22).
- sc008 "From the CCP point of view": Xi Jinping cut-out tagged "Xi Jinping · CCP" + the real Register headline (H200 sales allowed,
  9 Dec 2025) for "they have permission… more powerful NVIDIA chips". The chip shown is the H100 cut-out, unlabelled (generic NVIDIA chip).
- sc004 uses stills instead of the fab footage (both fab clips are already used by nvs02/nvs04).
- No MANUAL gotchas beyond the known ones; the inline headless dump harness (template body + local gsap + fx.js, seek loop, hold audit
  over `getChildren`) worked in < 10 s.

## QA fixes (lead review, 2026-11-17)
- nvs20.sfx.json: marker 2056.4 type `drop` (unknown to place_sound.py) → `dot_slide`.
