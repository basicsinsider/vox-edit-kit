# nvs06 — NOTES (master 559.583–647.042, 87.458 s, 2099 frames)

Plan: `project/nvidia/EDIT_NOTES_nvs06.md` (18 scenes, exact word cues). Built all of them; every second covered.

## First / last shot (boundary hand-off)
- First: sc001 White House (graphite plate, slow push) on "Now, of course, the administration" — fresh shot after nvs05's line;
  it also covers the EDL join at 559.93 so no face-cam jump in the first 0.35 s.
- Last: sc018 face cam M (646.42–647.042, framing change on the 646.42 join, slow push = motion for the cut into nvs07's B-roll).

## THE LINE (one `NV.line` instance, ids/powers/lineAt exactly as `compositions/nvmotif.html`)
- Start state = nvs05's end: A100 0.80 / H100 0.92 banned (`ban()` fired at 559.70/559.80 while the layer is still hidden, done by 560.8),
  A800 / H800 0.555 just under the line at 0.62. Axis/line not re-drawn (shown built).
- sc003: "OCTOBER 2023" date tag (t-label, ice-dark; my own div appended into `ln.line`, so it rides with the line — the motif's CSS is
  untouched) on "year"; `moveLine(0.47, S(569.47), 1.6)` on "moves" → A800/H800 auto-banned as the line passes.
- sc005: `addChip("h20")` on "right below this new line", camera punch-in (1.4) on the gap, pen circle (FX.markup.pen, ink) on "most powerful".
- sc011: `addChip("rtx4090")` on "Regular", `ban("rtx4090")` on "banned"; slow push 1.0 → 1.012 so the whole board (5 banned chips) reads.
- Same layer is shown in three windows; `ln-shot` transform/filter reset at every window start (the whip leaves it offset).
- Camera pushes on the full board are kept ≤ 1.012 (as nvs05) when the "THE LINE" tag is in frame: the tag sits at x 96, so any push puts it inside the margin
  (1.06 put it on the frame edge in the first snapshot pass).

## Raimondo quote (DECISIONS §2, RESEARCH §7)
Her real wording, Reagan National Defense Forum, 2 Dec 2023: "If you redesign a chip around a particular cut line that enables them to do AI,
I'm going to control it the very next day." Attribution "GINA RAIMONDO · DEC 2, 2023". Underlined in step with Sam's paraphrase: pen under
"I'm going to control it" on "I'm gonna do" (594.35), pen under "If you redesign a chip" on "the new chip" (595.79), yellow highlighter on
"the very next day" (597.60, done 598.15, holds to the cut 598.70). Name tag "GINA RAIMONDO / U.S. COMMERCE SECRETARY" on "the commerce secretary".
Collage rebuilt from ref `ast_0455523fccc84f71` (B/W official at a podium centre, geometric colour blocks + small triangles in ICE instead of red,
two tinted side photos: Commerce Hoover Building = ice, NVIDIA HQ sign = volt). Photo is `raimondo_2.jpg` (Bletchley Park, Nov 2023 — no free
photo of the Reagan forum exists); nothing on screen says where the photo was taken.

## Reference ids used
`ast_0455523fccc84f71` (sc006 collage), `ast_309797d0b3974b01` (sc013 real article + highlighted phrase). `ast_e2a78874f76a4410` NOT used — see deviations.

## Face cam
sc002 M, sc004 C, sc007 M, sc008 C, sc010 W, sc015 M, sc016 C, sc017 W, sc018 M = 3.60 + 5.32 + 4.33 + 2.31 + 2.04 + 6.42 + 0.60 + 3.40 + 0.62
= 28.64 s = **32.7 %**. Every join in range (559.93, 574.23, 598.57, 603.03, 612.38, 622.97, 642.42, 643.02, 646.42) is either inside B-roll or
a framing change exactly on it. Close-ups use transform-origin 1000 px 60 px (130 px cropped his hair at 1.55); W/M 1000 px 130 px. Clean
(grain/dust/vignette at 0 on face shots). sc015–sc018 are four framings of one continuous on-camera passage (the joins 642.42/643.02 are only
0.6 s apart, so sc016 is a 0.6 s close punch on "Nonetheless").

## Effects / treatments
Photo plates with fringe + push (White House, Capitol), THE LINE motif ×3 (different camera each time), Vox collage + pull-quote with pen
underlines and highlighter, footage (RTX 4090 in a PC, light CA grade), vintage screen #11 with CRT power-on (IBM 5154 monitor showing the
Cray Y-MP, scanlines, push-in), real article with body-text highlighter + camera push + focus hunt, PS2 cut-out drop. Transitions: hard cuts on
joins, cuts on action into the line, whip (585.47), CRT power-on (615.27), light-flash whip (622.97), vertical whip (632.45).

## Shared assets used
places/white_house_north_1, us_capitol_west_1, commerce_hoover_building_1, nvidia_hq_voyager_sign; people/raimondo_2; footage/
gpu_rtx4090_gigabyte_in_pc_rgb (0.4–2.44 s); hardware/cray_ymp_1988_gsfc, cutouts/ps2_console_cutout; news/s05_deseret_ps2 (via my crop);
assets/intro/screens/ibm_5154_monitor_frame.png; textures paper_stained_01_hires, paper_cream_01/02, paper_lined_01_hires, paper_fiber_01.
Own: `assets/nvidia/nvs06/derived/deseret_ps2_crop.jpg` (SOURCES.md there). Credits on screen for every CC BY(-SA) / fair-use item.
Footage credit verified on the Commons file page: author BornInGame (YouTube CC BY) — footage/SOURCES.md says "uploader per file page".

## Deviations from the lead's rows
- 001: White House 2.3 s before the face cam (covers the 559.93 join; "the administration").
- 005: RTX-4090-in-a-PC footage under "regular video game chips that I probably have in this" — then back on Sam for "PC, oh you guys can't see it".
- 007: no BIS-748P form / "EXPORT LICENCE REQUIRED" stamp: the PS2 licence requirement was Japan's (MITI, RESEARCH §8); a US form would be
  untrue (and no real blank form exists — docs/SOURCES.md). The real 2000 article's body text "export controls" is highlighted instead,
  so ref `ast_e2a78874f76a4410` (letterhead document) is not used.
- 006: the 1990s beat has no export-control document (none real in shared/docs) — the Cray on the period monitor + an object tag only.
- 008: a Capitol plate (tag "U.S. CAPITOL") covers "AI regulation here in the United States"; face cam from 636.00.

## Checks
- lint (sandbox, 0.8.217): 0 errors for nvs06 (warnings only: nested media start basis on the face-cam clips, duplicate img = plate fringe copies).
- `sync_audit.py compositions/nvs06.html --transcript transcript_nv.json`: 13 text cues, all −0.06 s, 0 flagged.
- Timeline dump (puppeteer + chrome-headless-shell): `tl.duration()` = 87.4583 = DUR; no page errors; the only tweens ending < 0.5 s before a
  cut are the whips' outgoing smears (structural).
- Snapshots of every scene (start/middle/end + whip mid-frames) looked at; fixes made: H100 side card unreadable (black-ground press shot) →
  NVIDIA HQ sign; THE LINE pushes reduced (tag on the edge); close-up origin; Capitol tag / highlighter re-timed for the 0.5 s hold.

## For the lead / MANUAL
- A segment that must continue a motif's state (bans) can fire `ln.ban()` in the first frames while the line layer is still hidden — no
  static "banned" state option exists in `NV.line`; a `state` option for THE LINE (like the scoreboard's) would make this cleaner.
- `NV.line`'s "THE LINE" tag sits on the 96 px margin, so any camera push > ~1.02 on the full board puts it out of the safe area.
- Underlines that must match a phrase's width without measuring: wrap the phrase in an inline-block span holding an absolutely-positioned
  `<svg viewBox="0 0 100 10" preserveAspectRatio="none">` with `pathLength="100"` + `vector-effect="non-scaling-stroke"` — draw by
  dashoffset 100 → 0 (set the path's opacity 0 until its draw, or the round cap shows a dot — lint `svg_round_cap_hidden_dash`).
- SVG presentation attributes (`stroke="var(--x)"`) — I used hex values to be safe; `el.style.stroke = "var(--x)"` (as nv_motifs does) is the safe way to use tokens.
