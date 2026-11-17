# nvs17 — NOTES (master 1698.208–1822.167, 123.958 s, 2975 frames)

Plan: `project/nvidia/EDIT_NOTES_nvs17.md` (15 shots, exact word cues). Every second covered; no face cam (part 2 is audio only) —
a new shot or a clear development every 2–5 s. Grounds alternate night/paper (never > 2 in a row). Assets generator:
`project/nvidia/gen/nvs17_assets.py` (China / SE-Asia outlines → `assets/nvidia/nvs17/derived/`, SOURCES.md there).
A previous attempt had left only reference crops in `work/nvs17_scratch/` (no composition) — built from scratch.

## First / last shot (boundary hand-off)
- First: sc001 China night map (fresh shot, slow push) on "Job three is basically keeping China hooked on American chips".
- Last: sc015 the real Bloomberg Law article, highlighter done 1821.22, camera push still moving at 1822.167 (cut on action into nvs18).

## Shots
sc001 China map + volt chips arriving along arcs (ref `ast_d02865717c824c47`) · waffle 10×10, 95 volt → 0, yellow % box counted
(ref `ast_0b23d2c7a06c4bb3`), shown twice (1702.54–1715.99; 1726.50–1736.87 with ghost "smuggled" squares + pen "?") · sc003 real Tom's
Hardware article (18 Oct 2025, "…from 95% to zero"), pen underline + focus hunt · sc004 SE-Asia map, Malaysia/Singapore → Shenzhen volt
route, China fills red · sc006 blurred racks + NVIDIA logo → focus snaps: Huawei Atlas 900 SuperPoD + Huawei logo hero · sc007 Huawei HQ
card, "U.S. ENTITY LIST / Added May 2019" (RESEARCH §19: 16 May 2019) · sc008 China map, Huawei badge at Shenzhen, red radio-wave rings ·
sc009 growth chart (ref `ast_06720d0b255d4d29`): 2025 200,000 (U.S. government, ice) / 500,000+ (private estimates), red curve + fan to
2026 1.5 MILLION (yellow, the one glow) · sc010 ink silhouette linked to China → resolves into Lutnick's official portrait, ice blocks +
Commerce building card, name tag (ref `ast_0455523fccc84f71`, varied vs nvs06: cut-out, blocks behind, card right) · sc011 real The
Register article (15 Jul 2025) "Nvidia to resume sales to China – with Trump administration approval", pen + highlighter on "permission
to sell the H20" · THE LINE (below) · sc013 modern TV (CSS bezel, no fake UI/chyron) with the CNBC frame, push into the screen ·
sc014 painting-to-print pull-back to his real words · sc015 real Bloomberg Law article with the same words highlighted.
Transitions: whip, hard cut, flash whip, vertical whip, hard cut, whip, cut, vertical whip, flash whip, whip, cut, whip, zoom-through
cut, vertical whip — never the same twice in a row.

## THE LINE (NV.line, ids/powers/lineAt exactly as nvs06)
Start state = end of nvs06: A100/H100 banned, line moved 0.62 → 0.47 (A800/H800 auto-banned), RTX 4090 banned — all stamped while the
layer is hidden (1698.4–1699.8). H20 shown built under the line. 1789.80 `moveLine(0.497)` UP ("stronger chip"; no chip is crossed, so
nothing is un-banned) with a dashed ghost of the old 0.47 line left behind; "JULY 2025" tag rides the line; H20 gets a volt-dark
"ALLOWED" tag on "allowed" (RESEARCH §4: the July 2025 H20 decision — not relabelled H200). 0.497 instead of a bigger nudge: at ≥ 0.50
the line would run through the banned A800/H800 cards (0.555). Camera: 1.0→1.008, then 1.5 punch to MOST POWERFUL + banned chips (pen
underline on "strongest"), then 1.5 on H20 + the gap between the ghost and the new line (pen circle on "a little bit"). At 1.5 the THE LINE
tag is fully inside or fully outside the frame (checked).

## Lutnick quote (DECISIONS §2, RESEARCH §20)
His real wording (CNBC, 15 Jul 2025), two pull-quotes: “We don’t sell them our best stuff, / not our second best stuff, / not even our
third best.” and “You want to sell the Chinese enough / that their developers get addicted / to the American technology stack.” —
attribution "HOWARD LUTNICK · CNBC · JULY 15, 2025". Lines appear on Sam's matching words (1809.88 / 1811.72 / 1813.64 / 1815.48 / 1817.24
/ 1818.44), underlines on "best" 1811.14, "second" 1812.90, "third" 1814.42, yellow highlighter on "addicted" 1818.02. The two
sentences are shown as two separate quotes (in the source the "addicted" sentence comes first), so nothing is spliced. The CNBC frame is
people/lutnick_2.jpg (Pennsylvania Energy and Innovation Summit, the same interview). The same words are then shown in the real Bloomberg
Law capture (news/s14) on "That was the whole quote".

## Shared assets used
news/s13_tomshw_zero, s03_register_h20_resume_2025, s14_bloomberglaw_lutnick; people/lutnick_cut (silhouette + portrait), lutnick_2;
places/huawei_hq_bantian_1, commerce_hoover_building_2; hardware/huawei_atlas900_superpod_2; logos/nvidia, huawei, huawei_wordmark,
flag_us; icons/chip; maps kit china_night, southeast_asia_night; textures paper_graph_01_hires, paper_cream_01/02, paper_stained_01_hires,
paper_lined_01_hires, paper_fiber_01, grain_01_norm, dust_02. Credits on screen for every CC BY(-SA) / fair-use item.

## Deviations from the lead's rows
- 001/002: the waffle starts at "Let's look at some numbers"; 1698.3–1702.5 gets its own China map shot ("hooked on American chips").
- 003: no 2019 headline exists in shared/news → factual "U.S. ENTITY LIST / Added May 2019" label beside the HQ photo (no "spying" in our type).
- 005: the Commerce building is a card inside the Lutnick collage, after a silhouette beat for "a random person … on purpose".
- 006: the line moves up only to 0.497 (see above); the real Register article (15 Jul 2025) covers "last summer … decided to allow".
- 007: the quote is set on a printed page (painting-to-print) after the TV push; the real Bloomberg Law article closes the segment.
- Segment-internal: sc004 ends at 1726.50 (not 1726.39) so the route/labels hold ≥ 0.5 s before the whip.

## Checks
- lint (sandbox, 0.8.217): 0 errors for nvs17 (the run's errors are all in other projects' compositions: missing face-cam files).
- `sync_audit.py compositions/nvs17.html --transcript transcript_nv.json`: 38 text cues, all −0.06 s, 0 flagged.
- Timeline dump (chrome-headless-shell, local gsap): `tl.duration()` = 123.9583 = DUR; no page errors; tweens ending < 0.5 s before a cut
  are camera moves only (sc009 push, sc015 push into the segment end).
- Snapshots of every scene (start / middle / end) and every cut at −0.05 / +0.05 s looked at: no black or empty frame. Fixes made: waffle
  final push cut the title (reduced), chart push cut the title (re-anchored), silhouette entered too late (blank paper 2 s), Register
  highlighter started at "the form of", the raised line ran through the A800/H800 cards, quote block top-heavy (re-centred, 57 px),
  Bloomberg crop cut "Howard" at the card edge, hold-rule fixes (arcs, route, attribution).

## For the lead / MANUAL
- `FX.markupDefs` resets the svg viewBox — a pen svg inside a scaled article card (native 2700×680 px) needs its viewBox set again after
  the call (already in MANUAL §4.2 for camera svgs; applies to any non-1920 svg).
- Grid-labelled crops of a capture (`PIL` ticks every 100 px) are handy for highlighter boxes, but read positions from the tick LABELS and
  confirm in a snapshot — a downscaled preview put the first Register highlighter 270 px too far left.
