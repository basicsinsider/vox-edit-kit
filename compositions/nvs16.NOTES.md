# nvs16 — NOTES (master 1572.4167–1698.2083, 125.7917 s; no face cam)

Built 19 scenes (plan + exact cues: `project/nvidia/EDIT_NOTES_nvs16.md`). Face cam 0 % (part 2 is audio only); a new shot or a
clear development every 2–5 s.
- **First scene**: fresh paper shot, the articles of the previous minutes dropping onto a desk ("all this information").
  **Last scene**: the balance scale, camera push on Jensen's argument card accelerating from 1697.60 → cut on action into nvs17
  ("Job three…").
- **SCOREBOARD** (`NV.scoreboard`, never rebuilt): sc002 state {1:x}, rows 1/3/4 dim on "Second job", `markRow(2,"check", T(1581.08))`,
  board held 2.42 s after the stamp; sc004 state {1:x, 2:check}, `tally:""`, `setTally("1 — 1", T(1589.96))` on "one", row 1 lit on
  "One job, not so much successful", row 2 lit on "The second job is successful". `top:170px` as nvs09.
- **JOB THREE** card (sc005) = nvs05 sc001 copied (same CSS/moves; ink bar, volt band, ice ring, tapes; ref `ast_e1ede4fafbd84a66`).
- References: `ast_71a7df7876064062` (sc007 Jensen grid collage: cutout over cream/volt tiles + B/W close-up tiles),
  `ast_05ca6a314e6642fa` (sc013 keyboard, QWERTY circled in volt, keys lifting off), `ast_0455523fccc84f71` (sc016 B/W stage
  photo framed by volt bars, side photos, triangles), `ast_e1ede4fafbd84a66` (sc005).
- Effects: scoreboard motif, stop-motion card pile, 12 fps bar chart + pen bracket, JOB card, 3D card flip, grid collage + tile pops,
  China night map with counter-scaled icons + rings, logo cards on a slab + push/dim contrast, isotype + typing code, keyboard with
  floating keys, block building with pen cracks + lock, argument cards + pen arrows, layered portrait collage + tilt, path streams
  (chips / coins), pen chart, balance scale (proxy-driven beam + hanging pans) + pen circle. Transitions: whips (plain, light-flash,
  vertical), slides (y / x), hard cuts on pushes — never the same twice in a row.
- Shared assets used: people/huang_cut.png, huang_5, huang_6, huang_7; places/nvidia_hq_endeavor_logo; hardware/h100_sxm_board_1,
  cutouts/keyboard_qwerty_cutout; docs/bis_rule_2022-10-07_p1 (2nd use in the video, after nvs09); news/s08_tomshw_colossus,
  s09_caixin_ration, s10_nist_news, s11_aljazeera_deepseek; logos nvidia_wordmark, deepseek_wordmark, alibaba_wordmark, bytedance,
  baidu, tencent_wordmark, flag_china; icons chip, ban, factory, person, lock; maps/kit/china_night. Own: `assets/nvidia/nvs16/derived/`
  china_fill/stroke.svg (copied from nvs09, logged in SOURCES.md). No downloads.

Deviations from the lead plan
- 001 split: articles (1572.4–1574.7) → board ✓ → a paper lead chart for "America is still in the lead … the chip ban … keeping that
  lead" (lane chart: ice wall drops in China's lane, bracket THE LEAD) → board again for "one to one" (the 3–6 s pacing rule).
- 002 (job three, 7 s) split: JOB THREE card, then a ban card that flips to "chip → China" for "a completely different way of looking".
- 004 + 005 as planned but 004 on the China night map (chip bounces off the ice ban line, empty red slot = "wanting", red factory,
  red chip = "their own version") and a separate face-off shot for "created a competitor" (NVIDIA volt chip vs the red chip, label
  CHINA — no Huawei logo yet). 006 has no hands asset: keyboard photo + floating key caps; code window (generic CUDA-style kernel,
  tab "kernel.cu") for "learning to write code on NVIDIA chips". 007: no "REDO EVERYTHING" text (would be a narration caption) —
  cracks + a lock tell it. 008 split into portrait collage (biased / other people) + chips→China / money back + CEO revenue chart;
  "fiduciary duty" has no on-screen text (caption rule). 009 scale: Jensen medallion vs the argument card, tips on "biased", level
  on "does not necessarily mean … wrong", push + pen circle on "evaluate".
- Cuts moved for the hold rule: sc003→sc004 at 1589.25 (THE LEAD label holds 0.5 s), sc007→sc008 at 1610.45.

Checks
- `npx --yes hyperframes@0.8.217 lint` (sandbox work/nvs16): 0 errors for nvs16 (warnings only: composition_file_too_large,
  duplicate_media_discovery_risk for the 4 nvidia_wordmark imgs). The 25 errors in the run are other compositions' missing face cams.
- `python3 tools/sync_audit.py compositions/nvs16.html --transcript transcript_nv.json` → "0 cue(s) flagged" (all text cues −0.06 s;
  the NVIDIA kicker in sc016 is cued at 1672.24 for "NVIDIA" 1672.30, the audit pairs it with "of" 1672.22).
- Headless timeline dump: `tl.duration()` = 125.7917 = DUR, 0 errors seeking the whole timeline every 0.25 s; hold audit: no key
  tween ends < 0.5 s before a cut (only camera pushes / transitions).
- Snapshots of every scene (start, middle, end) and every cut ±0.05 s looked at: no black/empty frame at boundaries.
- `compositions/nvs16.sfx.json`: 62 markers, all types in place_sound's vocabulary.

Gotchas (for MANUAL)
- In a grid built from a letter map, don't reuse a tile-type letter as a photo key (my "c" = cream also matched a photo crop → every
  cream tile became a photo).
- Lint 0.8.217 errors (`gsap_non_transform_motion`) on tweening `left/top` of a map pin — tween a proxy {x,y} and write left/top in
  `onUpdate` (as nvs09's routes do).
