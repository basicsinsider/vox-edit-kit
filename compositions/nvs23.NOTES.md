# nvs23 — NOTES (master 2267.958–2402.000, DUR 134.042, 15 scenes)

Plan: `project/nvidia/EDIT_NOTES_nvs23.md`. First scene: FACE M (fresh shot after nvs22's B-roll). Last: FACE W → freeze → night.

## Built
| scene | master | what | effect / ref |
|---|---|---|---|
| sc001 | 2267.96–2274.60 | FACE M — "the funniest part" | face, clean |
| sc002 | 2274.60–2280.53 | China night map: red DATA WALL on "cannot", citizens + data tokens bounce off it on "out of the country" | map, counter-scaled labels/icons |
| sc003 | 2280.53–2284.62 | Tom's Hardware 13 Jun 2025 headline (suitcases of hard drives, training in Malaysia), pen underline | article card over blurred copy, push (whip in, covers join 2280.53) |
| sc004 | 2284.62–2296.05 | ROUTE: plane + suitcase CHINA → MALAYSIA, data centre + TRAINING bar, MODEL file back, four weak chips | ref `ast_c0cbc15573184e83` (glowing route, waypoint label boxes) on a Blue Marble desat crop |
| sc005 | 2296.05–2307.28 | paper chart TRAINING (30 volt chips, MALAYSIA) → MODEL → RUNNING (4 grey chips, citizens fill red, CHINA) | paper ×2, isotype 12 fps (slide ↑) |
| sc006 | 2307.28–2313.95 | FACE W on the join | face |
| sc007 | 2313.95–2330.03 | DEBATE collage: Huawei Atlas 900 (red duotone, China flag) vs Malaysian data halls (Sedenak aerial, Malaysia flag), KL skyline ghost; AI-lab logos; orders fly to Malaysia; arrow to Huawei crossed; tilt down → race bars Huawei stalls, TSMC + NVIDIA ahead | ref `ast_4b7fb0fe0a134429` (two sides back to back, flags, the contested thing between) |
| sc008 | 2330.03–2351.48 | map: KL data centres + access lines to China, CHINA/MALAYSIA labels; glide to the strait, TAIWAN + red rings; ice switch flips OFF, DC dark, lines cut; China's red dims | ref `ast_4f6fcd9750634ef3` (terrain map + conflict), world-night crop (light-flash whip in; join 2347.13 covered) |
| sc009 | 2351.48–2357.55 | FACE C (1.42) + compact SCOREBOARD (✗ ✓ ✗, row 4 "The renting loophole"), "?" on "rank" T(2354.13), held 3.4 s | motif NV.scoreboard compact |
| sc010 | 2357.55–2362.43 | NPR 12 Nov 2026 "Nvidia CEO Jensen Huang steps down amid alleged spy scandal", underline on "spy" | article card, push |
| sc011 | 2362.43–2372.36 | FACE M, punch to W on "So if you have" | face |
| sc012 | 2372.36–2377.16 | FULL SCOREBOARD final state, "?" re-stamped, push (top 170) | motif full board (vertical whip in) |
| sc013–sc015 | 2377.16–2402.00 | FACE C → M (join 2385.40) → W (join 2394.97); video ends 2400.56, freeze of the last frame, fade to night 2400.50–2401.90, night held to 2402.00 | designed ending (no end card exists in the repo) |

Face cam: 6.64 + 6.67 + 6.07 + 9.93 + 8.24 + 9.57 + 5.59 = 52.7 s / 134.0 s = **39 %**. Every face shot starts on a join or a cut;
framing changes exactly on 2385.40 and 2394.97. Face framings W 1.0 / M 1.25 / C 1.42, origin 1000px 60px (C 1.44 touched the hair).
Transitions: hard cut, whip, cut, slide, cut(join), whip ←, light-flash whip, cut(join), whip, cut, vertical whip, cut, jumps — never twice in a row.
Temp VO `data-duration` 132.66 (vo_nv.mp3 is 2400.648 s, so it does not run past the file).

## Checks
- lint (0.8.217, sandbox `work/nvs23`): 0 errors for compositions/nvs23.html (warnings only: nested media start basis, file size, duplicate img discovery).
- `sync_audit.py compositions/nvs23.html --transcript transcript_nv.json`: 0 cues flagged (7 text cues, all −0.06…−0.09 s before their word).
- Timeline dump (headless, local gsap): `tl.duration()` = 134.042, no runtime errors over a full seek.
- Snapshots looked at: every scene start/middle/end, every hard cut ±0.05 s, every whip/slide at the cut instant, the ending 2400.41–2402.0.
- Holds: every key animation ends ≥ 0.5 s before its cut (sc002 bounce 0.55, sc007 NVIDIA bar 0.57 before the whip starts).

## Shared assets used
news/s15_tomshw_suitcases.jpg (first use), news/s01_npr_resign.jpg (first use in a composition), hardware/huawei_atlas900_superpod_1.jpg,
places/kuala_lumpur_skyline.jpg, maps/kit/aerial_johor_data_centers_z16.jpg (Sedenak Tech Park), maps/kit/china_night.jpg, world_night /
world_satdesat crops, logos (flags China/Malaysia, Huawei, DeepSeek, ByteDance, Alibaba, TSMC, NVIDIA), icons. Own derived files:
`assets/nvidia/nvs23/derived/` (SOURCES.md; generator `project/nvidia/gen/nvs23_assets.py`, 2.7 MB).

## Deviations / decisions for the lead
- sc003 and sc010 add two REAL headlines (Tom's Hardware suitcases; NPR resignation) for "flying to Malaysia" and "since the spy affair came out" —
  both are the exact events Sam names (RESEARCH §1, §23). The NPR headline spells "Nvidia" (it is their page).
- The route scene starts at 2284.62 (not 2280.58) because the headline covers "AI employees are actually flying to Malaysia"; the outbound flight
  plays under "with the information they need to train a new model". No Chinese city is named (Sam names none): the start is a CHINA box.
- Debate: both arguments Sam gives are reasons to keep the loophole, so the ref's "two people facing apart" became Huawei vs the Malaysian data
  centre (where the orders go), not two debaters. Race labels are logos only (no text).
- Malaysian data centres placed at Kuala Lumpur in the route/switch maps (WSJ story: engineers flew to Kuala Lumpur); the debate card uses the
  Sedenak (Johor) aerial — both are real Malaysian data-centre sites, neither is labelled with an operator.
- Map scenes use world-kit crops (one frame holds S China, Taiwan and Malaysia) instead of `southeast_asia_*`, whose 7030-px height could not
  frame China and Malaysia together at ≥ 1920 px width coverage.

## Gotchas worth adding to MANUAL
- A face-cam file that ends before the composition (here 2400.60 vs 2402.00): put a still of the LAST decodable frame under the `<video>` in the
  same framing wrapper; when the video's data-duration ends, the still shows with no black frame, and the fade runs over it.
- Lint 0.8.217 errors (`gsap_non_transform_motion`) on tweening `left/top` even of a 0×0 map pin: move a child with x/y instead (inside a
  counter-scaled pin the child's units are screen px).
