# nvs01 — NOTES (master 0.000–109.250, DUR 109.250) — cold open + the Hong Kong / Shenzhen "video"

Plan with exact cues: `project/nvidia/EDIT_NOTES_nvs01.md`. 24 scenes, all built, every second covered.

## Built
| scene | master | what | ref / effect |
|---|---|---|---|
| sc001 | 0.00–2.80 | RTX 4090 cut-out with volt rim, ice pen line on "ban"; title IS THE CHIP BAN / ACTUALLY WORKING? word by word (cold-open caption) | `ast_290885ff9bcc4687` (title in a rounded banner frame), halate |
| sc002 | 2.80–11.12 | Vox layers: Commerce (Hoover) building + Capitol, tag U.S. DEPARTMENT OF COMMERCE; torn-paper strip with the real SDNY press release, red pen under "Unlawfully Divert" | `ast_2b0b05b6a7bd471a`, layered #10 |
| sc003 | 11.12–20.96 | real Al Jazeera card (highlighter on "stepped down" / "allegations of Chinese espionage"), Jensen cut-out grey + volt outline, name tag, RESIGNED · 12 NOV 2026, real NBC card + pen under "suspected Chinese spy" | `ast_4b76d56ab5214313` |
| sc004/005 | 20.96–23.12 | FACE M → C exactly on the 21.72 join | face cam |
| sc006 | 23.12–25.44 | Jensen close portrait, shadow sweep ("if he knew") | photo plate |
| sc007 | 25.44–28.24 | real 7 Oct 2022 BIS rule page tilted, push, pen under DEPARTMENT OF COMMERCE | document #5 |
| sc008 | 28.24–29.95 | FACE W | |
| sc009 | 29.95–34.24 | timeline 2022–2026, rule pinned at OCT 7, 2022, ice bar to NOV 2026 on "a few years" | timeline #12 |
| sc010 | 34.24–36.00 | FACE C | |
| sc011 | 36.00–38.62 | GPU under the ice ban line, pen "?" on "success" (callback) | markups |
| sc012 | 38.62–40.62 | FACE W (join→join) | |
| sc013 | 40.62–54.96 | "this video" (DECISIONS §5): modern monitor + player bar; Golden Computer Arcade sign + pen arrow HONG KONG; RTX 4090 in hand + circle; stall with price tags + tags HONG KONG = UNITED STATES; 4 HK stall shots; RTX 5090; push-through into the screen | `ast_1aa75f10abbb4a75` |
| sc014 | 54.96–63.53 | PRD satellite: HONG KONG → volt ferry route + ferry icon + ferry photo inset → SHEKOU, CHINA fill, SHENZHEN, push + zoom box opening into the Huaqiangbei Esri z17 aerial (HUAQIANGBEI pin) | `ast_c0cbc15573184e83`, `ast_671f213364e14029`, map #3 |
| sc015 | 63.53–65.85 | 2.5D SEG Plaza (shared layer set), title SEG PLAZA tucked behind the tower | 2.5D #17 |
| sc016 | 65.85–68.09 | 16 RTX 4090 cut-outs fill a dark Huaqiangbei stall at 12 fps | layered + stop-motion |
| sc017 | 68.09–69.53 | FACE M ("multiple rooms") | |
| sc018 | 69.53–72.81 | footage: RTX 4090 running in a lit PC | footage plate, CA grade |
| sc019 | 72.81–82.41 | isotype: 8 GPU icons into a server (counter 1→8, yellow), pen arrows to AI COMPANY / UNIVERSITY / CHINESE MILITARY (red) | R5 isotype + markups |
| sc020 | 82.41–84.97 | FACE C ("caveat") | |
| sc021 | 84.97–94.33 | card → DGX server → NVL72 rack rising, camera pulls back, 2 TONS (yellow hero) | product cut-outs, count |
| sc022 | 94.33–101.77 | SE Asia night map: rack icons ride volt routes into red CHINA; drop to SINGAPORE; real Tom's Hardware headline + Megaspeed logo pinned to Singapore | map routes #3 |
| sc023 | 101.77–103.37 | FACE M | |
| sc024 | 103.37–109.25 | tactical map (grid, ruler, boxed spaced labels, volt heat glow): SINGAPORE + rings, MALAYSIA outline, pull back to other countries (THAILAND, VIETNAM labelled); still drifting at the cut | `ast_b30b6aa33937428e`, radio waves |

First shot: cold-open title at 0.00 (no Sam in 0–10 s). Last shot: tactical map, camera moving at 109.25 (cut on action into nvs02's face cam).
Transitions: whip, slide, hard cut, punch-in, light-flash whip, vertical whip, cut on the push, monitor push-through, zoom-box — never the same twice in a row.

## Face cam
8 shots (W/M/C varied; framing changes on the 21.72 join; 38.62 and 40.62 are shot edges): 20.96–21.72 M, 21.72–23.12 C, 28.24–29.95 W,
34.24–36.00 C, 38.62–40.62 W, 68.09–69.53 M, 82.41–84.97 C (origin shifted to 1080 px: he leans right there), 101.77–103.37 M
= 13.2 s of 109.25 s = **12 %** (1–2.6 s pops). Clean: grain/dust/vignette at 0 on face shots. Origin 960 px 0 px (head never cropped at the top).

## Checks
- lint (0.8.217, sandbox `work/nvs01`): **0 errors in nvs01.html** (the 25 errors listed are other projects' missing face-cam files);
  warnings only: nested_media_start_basis_ambiguous (same as every segment), file size.
- `sync_audit.py compositions/nvs01.html --transcript transcript_nv.json` → **0 cue(s) flagged** (25 text cues; 48.18 is UNITED STATES on
  "United" 48.24 — the audit pairs it with "the" 48.16).
- Timeline dump (headless): **tl.duration() = 109.25** = DUR. Hold audit: only secondary drifts end near cuts (panels, GPU sway); TONS fixed to hold 0.5 s.
- Snapshots: every scene at start+0.3 / middle / last 0.5 s looked at (10 batches) and fixed: face-cam origin, Jensen portrait framing,
  monitor sign crop, price-tag text, ferry inset position, China fill strength, zoom box timing, 2.5D side edges (s = 1.0 fit), isotype
  counter sync + right margin, empty start of sc021, map label clipping, centred boxed labels.

## Shared assets used
news: s01_aljazeera, s01_nbc (crops), s07_doj_sdny (crop), s02_tomshw_megaspeed2b (crop) · docs: bis_rule_2022-10-07_p1 (twice: sc007, sc009 card) ·
people: huang_cut_2, huang_6 · places: commerce_hoover_building_1, us_capitol_west_1, hk_golden_computer_arcade_sign / stall_1 (twice) / stall_2,
hk_wanchai_computer_centre_stall / entrance, hk_shekou_ferry_boat, huaqiangbei_stall_2, layers_huaqiangbei_seg/* · hardware: cutouts/rtx4090_fe (sc001, sc011,
sc016, sc021 — the recurring "chip"), dgx_h100_system, cutouts/gb200_nvl72_rack_front · footage: gpu_rtx4090_gigabyte_in_hand, gpu_rtx5090_fe_slow_orbit,
gpu_rtx4090_gigabyte_in_pc_rgb · icons: gpu_card, server_rack, ferry (CSS masks) · logos: megaspeed · maps: pearl_river_delta_satdesat, aerial_shenzhen_huaqiangbei_z17,
southeast_asia_night (+ overlays). Own derived files: `assets/nvidia/nvs01/derived/` (7.4 MB, SOURCES.md, generator `project/nvidia/gen/nvs01_assets.py`).

## Deviations / for the lead
- No Hong Kong mall footage exists (all clips are free-licence B-roll); "the video" is photos of the real HK computer malls + RTX footage in the monitor (DECISIONS §5).
  When Krish supplies the Gamers Nexus clip, swap it into `#nvs01-sc013-v1..v5` (screen 1272×716).
- No headline names Jensen + "helping China get the chips" — the NBC "suspected Chinese spy" card covers that line; no invented text.
- Megaspeed: the Tom's Hardware headline does not name Megaspeed; it is paired with the real Megaspeed logo pinned to Singapore (Sam: "likely what Megaspeed was doing").
- 2 TONS is Sam's number (UNVERIFIED in RESEARCH) — no source label. UNIVERSITY stands for "a research facility at a university".
- huaqiangbei_stall_2 is a 2013 electronics stall (no free photo of a GPU room exists) — used only as the dark background behind the GPU cut-outs.

## Gotchas worth adding to MANUAL
- A `mlab` label with a box (padding/background) and no fixed width can't be centred with the `left:-800px;width:1600px` trick — centre it with
  `gsap.set(inner,{xPercent:-50})` (rise() only tweens y, so xPercent survives).
- 2.5D from a portrait layer set: fit s = 1.0 (photo as wide as the frame) instead of 0.62 + side fill — the shrunken planes showed their rectangle edges
  (each plane's scale (P−z)/P doesn't cover the frame); photo-edge cuts in near layers need a mask feather.
- Face cam (NVIDIA master): transform-origin 960 px 0 px keeps the hair in frame at M/C; at 82–85 s he leans right (origin 1080 px).

## QA fixes (lead review, 2026-11-17)
- sc013 monitor ("no shortage of these cards"): Seagate/WD hard-drive and SanDisk stalls replaced with GPUs — v3 = hardware/rtx4090_fe_box_1 (boxed RTX 4090 under the HK = US price tags); grid g1 rtx_3090_vs_4090_cards, g2 hk_wanchai_computer_centre_entrance (HK), g3 gpu_rig_8cards_2, g4 rtx4090_fe_press; v1 (Golden Computer Arcade sign) kept; credit line updated.
- sc013 grid: g1 is already on screen at the v3→v4 switch (49.20) — the 12 fps pop left the monitor empty for 3 frames.
- sc007 + sc009: BIS rule p1 → docs/bis_rule_2022-10-07_threshold_p26.png (reuse limit); sc007 pen now underlines that page's "Commerce Control List" heading (pdftotext bbox), push origin 900 300; credits = 87 FR 62186, p. 62211.
