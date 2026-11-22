# cts11 — THE CONVOY AND THE CLIFF (master 976.208–1078.417, 102.208 s) — NOTES
Built from `project/cartels/gen/cts11_template.html` + `build_cts11.py` (inlines the map outlines from
`assets/cartels/cts11/derived/paths.json`); derived assets by `project/cartels/gen/cts11_assets.py`. Edit the TEMPLATE, then rebuild.
Plan with exact cues: `project/cartels/EDIT_NOTES_cts11.md`.

## Scenes (11)
| id | master | what | effects / ref |
|---|---|---|---|
| sc001 | 976.21–986.86 | mexico_relief → push into the Sierra Tarahumara (chihuahua_relief registered inside the same camera by the affine kit-to-kit formula, cross-fades in for sharpness); outside-Chihuahua dimmed, state outline drawn, steel radio pulse on "CIA operation", steel search reticle on "find", region lit (dots + outline) on "deep in the mountains"; dateTag "Chihuahua, Mexico · Apr 2026" | relief map, radio waves, region highlight — ast_d02865717c824c47 |
| sc002 | 986.86–994.40 | isotype: 4 steel CIA figures vs 60 olive figures (12 fps fill, counter 60+ in yellow), ski masks drop onto the 4 CIA (steel) heads on "ski masks" (fix round 1 #13: the Americans wore the masks, not the Mexicans); "Source: The New York Times" | isotype (MANUAL ref #5), counter |
| sc003 | 994.40–1001.10 | real lab footage (FGE Chihuahua via CBS): camp → reactors/tanks (pen circle "gas tanks") → chemical totes (pen circle "chemicals"), plate on its own blurred fill | footage plate, pen markups, chromatic aberration |
| sc004 | 1001.10–1006.32 | ★5 substitute: chihuahua_night tilted in 3D, framed Copper Canyon (Sierra Tarahumara) clip graded day-for-night | 3D map plane — ast_e93e1bd1813e40ef |
| sc005 | 1006.32–1015.50 | cross-section diagram (labelled "illustration"): truck drives to the ledge, leaves it and fades (no impact/wreck), dashed fall line, ruler counts to 300 FT (yellow), "Height per The New York Times"; then the diagram steps back and four quiet markers: 2 CIA officers (steel), 2 Mexican officers (olive) — no names | diagram, counter — ast_c0cbc15573184e83 |
| sc006 | 1015.50–1027.40 | night map: region + the four markers; Zuany card (outside the region); olive radio waves + dashed call line + phone chip on "called him"; 2 witnesses (silhouettes, "Per The New York Times"); pulse back on "instructions"; the two steel markers lift out north on "get the American bodies" | dissolve in (quiet), radio waves, line draws — ast_22f35e73b57b4e0e |
| sc007 | 1027.40–1033.60 | jacket exhibit (labelled "illustration"; generic olive shield, no real seal): label "Mexican government logo", pen circle, patch peels off | line illustration, pen markup |
| sc008 | 1033.60–1051.80 | news desk: Al Jazeera, PBS/AP, CBS "We were not informed" (pen underline on "no clue"), Sheinbaum polaroid, PBS/AP report on top with highlighter on "adding she was unaware of collaboration between the U.S. and the local government in northern Chihuahua" | newspaper collage, underline, highlighter on body text |
| sc009 | 1051.80–1063.60 | mexico_night: Sheinbaum (olive, Mexico City) vs Maru Campos (ash, Chihuahua), "PAN · Opposition", "Morena", jagged fault line on "political fight" | map + portrait cards |
| sc010 | 1063.60–1074.40 | CT.file ×2 (olive): Zuany pushed back, Jáuregui on top; RESIGNED on both; row "Arrested 17 Oct 2026" + ARRESTED; Jáuregui out, Zuany forward, ON THE RUN (steel) | CT.file motif — ast_8693d810270e43fd |
| sc011 | 1074.40–1078.417 | mexico_night: Zuany's portrait travels north across the border into the US, "?" ; UNITED STATES on "United States"; "Per The New York Times" | route draw |
Transitions: whip · hard cut · light-flash whip (vertical) · hard cut · dissolve · slide up · whip · light-flash whip · slide x · whip.

## Checks
- lint (`npx --yes hyperframes@0.8.217 lint compositions/cts11.html` in work/cts11): **0 errors**, 6 warnings (nested media start basis ×4 =
  composition-local times as intended, duplicate img discovery, file size).
- `tools/sync_audit.py compositions/cts11.html --transcript transcript_ct.json`: **0 cues flagged**, every text cue −0.02…−0.06 s.
- headless timeline dump: `tl.duration()` = **102.208** = DUR; hold audit: only structural camera/slide tweens near cuts.
- Snapshots: every scene start/middle/end and every cut ±0.05 s looked at (batches of ≤ 8).

## Assets
- Shared: footage `x_chihuahua_narcolab_a/_b`, `m5_sub_chepe_canyon`; maps `mexico_relief/_night`, `chihuahua_relief/_night` + overlays;
  people `sheinbaum_1.jpg`, `campos_1.jpg`; news `n04_*` (cropped into cards). **`assets/cartels/people/` still has no SOURCES.md** —
  sheinbaum_1 / campos_1 are used on the assumption the gatherer logs them (Campos = woman at a desk with the Chihuahua state flag; please
  confirm the identity/source when the people log lands).
- Own: `assets/cartels/cts11/derived/` (SOURCES.md): Zuany + Jáuregui photos cropped from Infobae article pages (FGE Chihuahua photo
  captioned with Zuany's name; Jáuregui identified against the Reuters photo captioned "César Jáuregui"), 4 news cards, stills, paths.

## Deviations / substitutes
- ★5: `assets/cartels/footage/_raw/m5_batopilas_road.mp4` had NOT arrived → `m5_sub_chepe_canyon` 3.0–7.3 s (the only stretch without
  rails/bridge; train window cropped by a left-anchored 1.3× scale), graded day-for-night, framed over `chihuahua_night`; a still of 7.25 s
  holds the last ~1 s. If the Batopilas clip arrives, swap it into `#cts11-sc004-v` (card 900×540). No pin for the lab or crash.
- Four markers + the two "2 … officers" labels follow the record / CBS wording (2 CIA + 2 Mexican officers); Sam says "everyone inside,
  including two officers". No victim names.
- "Narco" figures/sources: 4 CIA / 60+ / 300 ft carry "per The New York Times" (unverified elsewhere, RESEARCH §3).
- Zuany tag uses RESEARCH's "Ex-special prosecutor, Chihuahua"; Jáuregui file row "State attorney general" (Sam's words).

## Gotchas for the lead / MANUAL
- My own helper `div(parent, cls, css, html)`: passing markup as the 3rd argument silently gives an EMPTY element (three tracked items were
  missing until a headless dump showed it). Keep the 4-argument call.
- Two kit maps in plate carrée can share one camera: chihuahua px → mexico px is affine (`x·0.29607 + 1576.96`, `y·0.285714 + 720`);
  put the close-up plate in a div with `scaleX/scaleY` and cross-fade it in during the push — sharp close-ups without a cut.
- `m5_sub_chepe_canyon` contains rail-track shots at 2.3–2.9 s and from 7.5 s — usable window 3.0–7.3 s only.
- CT.file supports one stamp per instance (text set at build time); a second/third stamp = a cloned `.ctm-fstw` with the same filter
  (`cloneStamp()` in the template) — maybe worth a `f.stamp2()` in the motif.
