# nvs04 — NOTES (master 362.292–472.667, DUR 110.375, 16 scenes) · plan: `project/nvidia/EDIT_NOTES_nvs04.md`

## Built
sc001 paper "is it working?" gauge, needle hunting (pen draw-on) · sc002 FC M · sc003 three person cards, same gauge, three different
readings · sc004 FC W→M · sc005 **THE SCOREBOARD** full intro (`NV.scoreboard`, results empty, row 4 = empty dashed slot, table at
top 171 = vertically centred per DECISIONS §9; on "fourth" rows 1–3 dim + push + ice-light pen box round row 4) · sc006 FC M→C (reframe at
the 403.25 join) + compact scoreboard (row-4 slot glows on "blank" / "fill that in", wipes out on "Let's get started") · sc007 FC W→M ·
sc008 US satellite, volt chip, US fills ice, UNITED STATES · sc009 whip-pan west → Taiwan (southeast_asia_satdesat), TAIWAN, zoom box on
Hsinchu → Esri aerial inset with TSMC Fab 12A pin (ref `ast_671f213364e14029`), ice pen arc from the east on "how does the US decide" ·
sc010 GPU floorplan drawing itself on blueprint, NVIDIA logo stamps in the title block, volt "Market value" bar (no figure — Sam gives none)
· sc011 NVIDIA HQ Santa Clara plate + tag, the floorplan as a card + ice lock on "control" · sc012 fab footage in a monitor + toolbox
chart (Applied Materials, Lam Research, KLA, ASML / Synopsys, Cadence — RESEARCH §6), US flags on "American made", Dutch flag on
"Western made" · sc013 FC C · sc014 graph-paper flow: chip ← US tools & software → Commerce Dept. seal gate → buyer passes / buyer ✗ ·
sc015 FC M · sc016 world night map, KEVIN WOLF name tag (DECISIONS §2), 12 real chip-fab pins pop on "every chip on the planet", ice rings
from Washington, D.C. turn every pin ice on "under American law", ice lines DC → fabs on "American stuff".
Transitions: cut, slide, cut, whip, flash-whip, cut (join), slide, whip, slide, flash-whip, cut on action, whip, slide, cut, whip — never
twice in a row. First scene: fresh paper shot. Last: camera drift on the world map (cut on action into nvs05).

## Face cam: 35.9 s of 110.4 s = 32.5 % (plan ≈ 35 %)
Every FC shot starts at an EDL join or after a graphic, and changes framing at joins inside it (403.25). Deviation: the segment does NOT
open on Sam — the face cam jumps at the 362.42 join (3 frames of the previous take before it), so the first FC shot is 367.70–370.08.

## Shared assets used
places/nvidia_hq_voyager_sign.jpg · footage/fab_wafer_lithography_st.mp4 + fab_chip_assembly_st.mp4 (0–4.2 s, ST montage; credited) ·
logos/nvidia_wordmark.svg, flag_us.svg, commerce_dept_seal.svg · icons/chip, person, lock, factory · kit maps us_satdesat,
southeast_asia_satdesat, aerial_hsinchu_park_z17, world_night (derived ½ copy) · textures paper_cream_01/02, fiber, graph, blueprint.
Own derived files: `assets/nvidia/nvs04/` (SOURCES.md, generator `gen_nvs04_assets.py`). Nothing missing or substituted; Dutch flag drawn
as three CSS stripes (no shared file).

## Checks
lint 0.8.217: 0 errors in nvs04 (warnings only: nested media start basis, file size) · sync_audit: 9 text cues, all −0.02…−0.06, 0 flagged ·
`tl.duration()` = 110.375 = DUR · hold ≥ 0.5 s checked on every scene end (sc003 settle and sc014 ✗ moved earlier for it).

## Gotchas for the lead / MANUAL
- Several `tl.to()` tweens on one plain proxy object driven through `onUpdate` (needle angles) rendered wrong angles in snapshots; an HTML
  element rotated by GSAP with explicit `fromTo` from-values is reliable.
- A segment camera tween that runs to the last frame must end ≤ DUR: a 7.8 s drift pushed `tl.duration()` to 110.438 (found with a
  headless timeline dump — `waitForFunction` hangs on this box; a fixed 12 s wait after `goto` works).
- Kit `pacific_*` ends at 115°W, so the US West Coast is at its frame edge; use `us_*` for the US + whip-pan to `southeast_asia_*` for Taiwan.
- Map pins on a world view at scale ≈ 0.3 need r ≈ 60+ (r 22 read as specks).
