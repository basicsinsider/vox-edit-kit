# cts05 — NOTES (segment editor, 2026-11-22)
Master 358.208–450.917 (DUR 92.708). Plan: `project/cartels/EDIT_NOTES_cts05.md`. 13 scene layers (sc005 holds both of the
lead's "label" and "terrorist group" rows as one paper board with seven camera moves).

## Scenes built
| id | master | picture | effects · ref |
|---|---|---|---|
| sc001 | 358.208–364.620 | case-file timeline Jan–Feb 2025: FBI card 4 Feb (cts04 continuity) ← pen bracket ← INAUGURATION 20 Jan, EO 14157 tag | graph paper, pen arrow, 12 fps pops |
| sc002 | 364.620–368.560 | Day-One signing photo (PD, @VP), cool charcoal duotone, push to the pen | whip →, dateTag WASHINGTON, DC · 20 JAN 2025 |
| sc003 | 368.560–372.300 | EO 14157 Federal Register page, push to title; highlighter "Foreign Ter- / rorist Organizations" on the words | hard cut on action, highlighter |
| sc004 | 372.300–382.620 | the 8 FTOs (FR 20 Feb 2025) as a halftone tile grid with a yellow "8" callout + bracket; Sinaloa / CJNG light ember on their words, "El Mencho" tag; FTO stamp on "terrorist" | flash whip ↓ · **ref ast_ebb77f26d0fc4b3f** |
| sc005 | 382.620–416.950 | explainer board: FTO tag (the "label") swings in, pen circle; CRIMINAL → handcuffs (ARREST) → courthouse (COURT); TERRORIST GROUP: ember node, 5 helpers, MONEY / SUPPLIES, steel bars slam on "prison"; pull back on "major deal" | paper slide, drawn icons, camera moves |
| sc007 | 416.950–420.010 | White House (DoD photo), push | whip ←, dateTag THE WHITE HOUSE · OCT 2025 |
| sc008 | 420.010–425.770 | NBC News header "…'armed conflict' with cartels, administration tells Congress": bone pen underlines on "Congress", then "'armed conflict'" | hard cut, pen markups |
| sc009 | 425.770–431.690 | NBC body: "The designation essentially puts drug cartels in the same legal category as terrorist groups like Al Qaeda…" highlighted on "cartel members … Al Qaeda" | slide ↑, highlighter (body size) |
| sc010 | 431.690–435.300 | grid callback: steel crosshairs lock onto all 8 on "targets" | flash whip → · ref ast_ebb77f26d0fc4b3f |
| sc011 | 435.300–440.030 | collage: US/Mexico flags on poles, Trump (steel halftone cut-out) vs Sheinbaum (olive halftone cut-out), steel pressure arrow shoves her card on "pressure", MEXICO label on "Mexico" | slide →, **ref ast_4b7fb0fe0a134429** |
| sc012 | 440.030–442.620 | Rose Garden 2 Apr 2025, Trump with the Reciprocal Tariffs board — ONLY on "Liberation Day and all the tariffs we saw" (SEGMENTS §4: no Liberation-Day text, no Mexico on it) | whip →, dateTag ROSE GARDEN, WHITE HOUSE · 2 APR 2025 |
| sc013 | 442.620–447.450 | "trade": CBP aerial of the World Trade Crossing, Laredo; MEXICO / Rio Grande / UNITED STATES / Laredo, Texas labels (constant screen size); dashed truck-flow line on "trade" | hard cut on action |
| sc014 | 447.450–450.917 | the frame tears to the DEA "rainbow" fentanyl M30 pills; FENTANYL tag on "drugs"; holds 0.59 s into cts06 | paper-tear clip wipe (ragged edge) |

## Checks
- `npx --yes hyperframes@0.8.217 lint compositions/cts05.html` → 0 errors, 1 warning (file length).
- `python3 tools/sync_audit.py compositions/cts05.html --transcript transcript_ct.json` → 0 flagged (16 text cues; the two "+0.02"
  lines are nearest-word artefacts: 388.08 = "criminal" 388.14, 398.16 = "terrorist" 398.22, both −0.06).
- Timeline dump (headless): `tl.duration()` = 92.708 = DUR.
- Snapshots: every scene start/mid/end and every cut ±0.05 s looked at (no empty or black frames; sc004 and sc005 got content on frame 1
  after the first pass showed 1 s of bare ground; sc001→sc002 whip moved to 364.62 so the EO tag holds 0.6 s).
- Holds ≥ 0.5 s before every cut checked from the cue list.

## Assets
New (all logged in `assets/cartels/cts05/SOURCES.md`, 13 MB): Day-One signing (PD, = people/trump_eo_day1_1.jpg), Sheinbaum 2025 (Eneas,
CC BY 4.0 — credited on screen), White House South Lawn (DoD PD), Rose Garden tariff board (White House PD, Daniel Torok), Laredo World
Trade Crossing (CBP PD), DEA rainbow fentanyl (PD), US/Mexico flags (PD); derived halftone duotone cut-outs (`project/cartels/gen/cts05_assets.py`
+ remove-background), NBC header copy + NBC body crop (frozen copies — the news gatherer re-captured `n_armed_nbc*.jpg` at 04:51 and
changed their size/crop mid-build).
Shared used: `docs/d01_eo14157_p1.jpg`, `news/n_armed_nbc.jpg` / `_k2.jpg` (copied). PBS article not used (cookie banner; NBC's k2 paragraph
names Al Qaeda directly).
Missing / substituted: no al-Qaeda image (the NBC paragraph carries it); `people/` has no SOURCES.md yet — I fetched my own copies from
Commons with known licences instead of using `people/sheinbaum_1.jpg` (different crop, unknown source).

## Gotchas for the lead / MANUAL
- `remove-background` failed with "installing onnxruntime-node failed": the CUDA download step is blocked. Fix:
  `npm install onnxruntime-node@1.21.1 --onnxruntime-node-install-cuda=skip --prefix ~/.cache/hyperframes/optional/onnxruntime-node@1.21.1`
  — then it runs on CPU (~2–6 s per still).
- `make_sandbox.sh` doesn't link `vo_ct.mp3` / `transcript_ct.json` — `ln -sfn ../../vo_ct.mp3 work/ctsNN/` by hand.
- Shared news captures can be regenerated by gatherers with new pixel sizes: copy the exact files you key coordinates to.
- A ragged "paper tear" transition = clip-path polygon (seeded jitter) driven by a proxy tween's onUpdate, a paper-coloured copy 16 px
  ahead gives the torn white edge (sc014).
