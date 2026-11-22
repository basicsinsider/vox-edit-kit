# cts03 — NOTES (editor, 2026-11-22)
Master 158.917–264.167 (105.25 s). Source: `project/cartels/gen/cts03_template.html` → `python project/cartels/gen/build_cts03.py`
(inlines `cts03_mapdata.json` from `cts03_assets.py`). Edit the template, not the built file. Plan: `project/cartels/EDIT_NOTES_cts03.md`.

## Built (8 layers, 10 shots)
A case board (paper) ×2 windows · B 2008 arrest photo (night) · C torn board ×2 windows · D armed-wing org chart (night, isotype) ·
E Sonora 2010 tilted satellite terrain · F routes-north showpiece (dark relief: northern Sinaloa fill, sea route, Mex 15 glow draw,
Arizona, drug chips, flow particles) · G DEA fentanyl photo · H Treasury 2013 release (pen circle, highlighter, contrast call-out).
Transitions: cut on action in, whip →, hard cut, invisible match cut (A→C), vertical whip, light-flash whip, hard cut, push-through,
hard cut, whip ←. Refs: ast_716e2cc68e364ca5 (board), ast_4f6fcd9750634ef3 (2010 on terrain), ast_c0cbc15573184e83 (routes).

## Checks
- lint (compositions/cts03.html alone): 0 errors, 1 warning (file length).
- sync_audit --transcript transcript_ct.json: 0 cues flagged (all −0.06).
- headless dump: tl.duration() = 105.25 = DUR; seek every 0.25 s, 0 errors. Hold audit: only camera moves/whips/flow end near cuts.
- Snapshots of every scene (start/mid/end) and cuts ±0.05 looked at.

## Accuracy decisions
- Brothers' stamps follow the record (Alfredo ARRESTED 2008, Arturo KILLED 2009, Héctor ARRESTED 2014) but are cued on Sam's words
  ("arrested" → Héctor, "killed" → Arturo). Carlos Beltrán Leyva is not shown (not narrated).
- 2008 date tag "Culiacán, Sinaloa · 21 Jan 2008" = arrest place/date (RESEARCH Ch 2); the photo is his presentation after the arrest.
- Sonora 2010 = Tubutama (RESEARCH: 1 Jul 2010); "20–30 KILLED" as Sam says; no imagery of violence. Pictogram men carry no weapons.
- Routes: Sam's "the main highway" = México 15 (RESEARCH Ch 2, kit `#hwy-mex15-north`); the sea route is schematic (Topolobampo →
  Bahía de Kino, offshore, landmask-checked) — no source claims an exact boat lane, so no labels on it.
- No "born here" pin; northern Sinaloa shown as his territory only (SEGMENTS §4).

## Assets
New in `assets/cartels/cts03/` (SOURCES.md): photos of Arturo (Expansión), Alfredo 2008 (El Universal), Héctor + El Chapo PGR photos
(Vanguardia composite), DEA fentanyl photo (PD), derived ID crops, graded map crops, Treasury page crop. Shared: people/meza_fbi_photo_1
(FBI; people/ still had no SOURCES.md when I built), docs/d10_treasury_ofac_2013_full (docs/ no SOURCES.md yet either), kit maps.
Substitutions: Héctor's photo is a 730-px composite (used ≤ 230 px wide, duotone) — a larger copy would be better if a gatherer finds one.

## Gotchas for the lead / MANUAL
- A layer shown in TWO windows after a whip must get its shot reset (`tl.set(shot,{x:0,y:0,scale:1,autoAlpha:1,filter:"none"})`)
  — FX.whip leaves the outgoing shot moved/hidden.
- Returning to a layer that sits EARLIER in the DOM: hide the outgoing layer at the cut (−0.001), not +0.05, or it covers the cut frame.
- Torn paper: two clones of the board, each clipped with a jagged `clip-path: polygon(...)` in px (points may run outside the box);
  content that must cross the tear lives in an unclipped overlay inside the same moving wrapper.
- Constant-size map labels on a 2D camera: drive the camera from a proxy `{cx,cy,s}` with `onUpdate` and position screen-space labels
  in the same function (`vector-effect: non-scaling-stroke` keeps line widths constant).
- `tools/audio/place_sound.py` aliases `card` → card_swipe; use `paper_slide` for cards/chips.

## Fix round 1 (2026-11-22, Agent B)
- #11 (v1 03:19 ≈ 199.5 s, scene D org chart): the four circle portraits (Arturo, Alfredo, Héctor + Isidro's node) now use square
  whole-head crops `assets/cartels/cts03/derived/circ_*.jpg` (generator `project/cartels/gen/cts03_circles.py`; where the source is
  tighter than the circle the margin is an edge-extended, blurred copy of the same photo). Arturo = people/arturo_beltranleyva_1 (the
  Expansión photo is too tight), Héctor = people/hector_beltranleyva_mugshot_3, Isidro = people/meza_fbi_photo_hires_2. Images fill the
  circle (no top offset). The rectangular board cards keep their id_* crops. English sweep: no Spanish text found in cts03.
