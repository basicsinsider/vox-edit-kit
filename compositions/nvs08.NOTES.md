# nvs08 — 775.250–864.750 (89.50 s) · "the big fish" · NOTES (segment editor, 2026-11-17)
Plan: `project/nvidia/EDIT_NOTES_nvs08.md` (13 scenes, exact word cues). Composition id `nvs08`, timeline duration dumped = 89.5.

## Built
| scene | master | picture | ref |
|---|---|---|---|
| sc001/sc002 | 775.25–782.89 | Sam M → W (framing jump on the 781.22 join) | — |
| sc003 | 782.89–792.81 | case-file flat lay: REAL indictment p1 (S.D.N.Y.), small Liaw polaroid + tag "WALLY LIAW / Supermicro co-founder" on "co-founder", Supermicro card, SDNY press-release clipping, stamp CASE ONGOING on "ongoing" | ast_8693d810270e43fd |
| sc004 | 792.81–797.61 | Supermicro server footage (Computex 2023), "$1.5 BILLION" yellow counter + "ALLEGED" (Sam's number, no source label) | — |
| sc005 | 797.61–808.09 | Pacific night map: volt route US → Southeast Asia (region pin only — company unnamed), dashed hollow building = fake company, red route into CHINA (fill), dotted decoy to SOUTH KOREA | ast_c0cbc15573184e83, ast_b30b6aa33937428e |
| sc006 | 808.09–815.29 | Sam C | — |
| sc007 | 815.29–831.29 | cork board: hair-dryer polaroid, barcode sticker peels off REAL CHIPS card and flies to FAKE OR OLDER CHIPS card, twine; then the real indictment warehouse still (dummy servers, 17:01) pinned + push on "running" | ast_1587dee18be645e2 (+ style ref 9) |
| sc008 | 831.29–836.76 | REAL indictment p16, yellow highlighter on "Surveillance cameras recorded their work", pan down to the stills | §10.6.6 |
| sc009 | 836.76–839.96 | the surveillance still (hair dryer) on a security monitor, bone pen circle + arrow on "caught" | ast_1aa75f10abbb4a75 |
| sc010 | 839.96–846.92 | Sam M | — |
| sc011 | 846.92–853.24 | Megaspeed logo, then the real Tom's Hardware article (23 Dec 2025, Megaspeed accused of smuggling) slides in, pen underline "Singapore-based Megaspeed"; blurred copy as layered background | — |
| sc012 | 853.24–858.92 | Sam W | — |
| sc013 | 858.92–864.75 | Southeast Asia night map: region lights up, five "?" pins (Vietnam, Thailand, Malaysia, Singapore, Indonesia), "SOUTHEAST ASIA" on the word; still pushing at the end (cut on action into nvs09) | — |

Transitions: slide ↑, hard cut on push, flash whip, hard cut, whip ←, slide →, cut on pan, vertical whip, slide →, cut, flash vertical whip.
First shot: Sam on camera (M). Last shot: SE-Asia map push (B-roll) at 864.75.

## Face cam
5.97 + 1.67 + 7.20 + 6.96 + 5.68 = 27.48 s / 89.50 s = **30.7 %**. Joins 781.22 (framing change) and 846.92 (cut out of FC) respected; the rest fall in B-roll.

## Checks
- lint (0.8.217, sandbox): 0 errors for nvs08 (only the usual `nested_media_start_basis_ambiguous` warnings for the timed videos, as in pys02).
- `sync_audit.py --transcript transcript_nv.json`: 14 cues, all −0.06 s, 0 flagged.
- timeline dump: duration 89.5; seek 0→89.5 without errors; no key animation ends < 0.5 s before a cut (only face-cam push / card drift tweens run to the cut).
- snapshots of every scene (start+0.3, middle, last 0.5 s) looked at.

## Deviations from the lead's plan
- Row 007 (Megaspeed + "no one knows"): Megaspeed gets the real article + logo (true thing named), Sam on camera only for the "no one knows / true insider" aside — keeps FC at 30 %.
- Row 006: instead of a typeset "CCTV" monitor, the REAL indictment page 16 + the REAL DOJ still on a monitor (no invented CCTV UI / timestamp text).
- Map: the indictment does not name the Southeast-Asian company or its country, so the pin is a region marker in the South China Sea, not a country.
- String on the board is neutral twine (red = China in this palette).
- "Pretending like it's in South Korea" is UNVERIFIED (RESEARCH §10) — shown as Sam says it (dotted decoy line), no source text.

## Assets
Shared: docs/doj_indictment_liaw_p1.png, doj_indictment_liaw_hairdryer_p16.png, doj_indictment_warehouse_stills_p15.png (crop), news/s07_doj_sdny.jpg,
s07_still_warehouse_tomshw.jpg (crop), s02_tomshw_megaspeed.jpg (also likely used in nvs01 → 2 uses max), people/liaw_1.jpg (crop, shown ≤ 250 px),
logos/supermicro.svg, megaspeed.png, hardware/cutouts/hairdryer_cutout.png, footage/server_grace_hopper_internals.mp4, icons (server_8gpu, barcode_label,
factory — inlined), maps kit pacific_night + southeast_asia_night, textures cork_01 (CC BY credit on screen).
Own derived files: `assets/nvidia/nvs08/` (SOURCES.md; generator `project/nvidia/gen/nvs08_assets.py`), 3 MB, no new downloads.
Missing: `assets/nvidia/shared/docs/` has no SOURCES.md (the indictment PNGs are unlogged there — lead/gatherer should add it).

## For the lead / MANUAL
- Fast hold-audit without puppeteer: inline the template into a page with gsap + fx.js, run `chrome-headless-shell --no-sandbox
  --allow-file-access-from-files --virtual-time-budget=8000 --dump-dom` and write results into a `data-` attribute (root needs `--no-sandbox`).
- Face cam (NVIDIA): transform-origin `1000px 60px` keeps Sam's hair in frame at 1.25/1.55 (origin 250 px cropped his head).
- `assets/nvidia/shared/icons/*.svg` use `currentColor`: inline the path markup (an `<img>` renders black).

## QA fixes (lead review, 2026-11-17)
- sc007 cork board: REAL / FAKE cards + barcode sticker pinned from the whip landing (815.29) and the hair-dryer polaroid pinned face-down, flipping over on "hair dryer" (820.45) — no empty board; sfx: two card pin_pops removed, 820.45 retyped card_flip.
- Checked local 21.5–23.5: the flat grey frame at 22.38 is the peak of the light-flash whip at 797.61 (< 0.12 s, 22.33 blur → 22.45 map) — left as is.
