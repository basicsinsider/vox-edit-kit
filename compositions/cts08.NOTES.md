# cts08 — NOTES (editor, 2026-11-22)
Master 651.500–768.458 (116.958 s), 15 scenes, plan in `project/cartels/EDIT_NOTES_cts08.md`. Lint 0 errors (3 warnings: nested media
data-start is composition-local, file size); sync_audit 0 flagged (27 cues, all −0.06 … −0.03); tl.duration() = 116.958 (headless dump).
Every scene snapshotted (start/middle/end) and every cut at −0.05/+0.05.

## Built
boat-strike monitor → strike map (Caribbean → Pacific, ember wakes) → paper isotype chart 70+ / close to 250 → Caracas map (zoom box,
Maduro reticle, route to New York) → Maduro stairs footage → MDC Brooklyn → "message to every cartel boss" (ref ast_a9e2) → Venezuelan
hardware drains grey → HUD over Mexico → Tapalpa ★3 + El Mencho card → real front pages with pen underlines on La Jornada's kicker →
balance scale (ref ast_0659) → Trump/SOTU timeline + real quote → scale wobble → THE DEAL (CT.deal) pressed + crack.
Refs used: ast_671f213364e14029 (zoom box), ast_a9e2b4c194ec4f14 (gazing at the glowing object), ast_0659daaead12498d (balance scale).
Transitions: whip, slide, flash whip, hard cuts on action — never the same twice in a row.

## Deviations from the lead's rows
- Maps: built on a crop of kit `americas_night` (+ world_overlay borders) because `north_america_*` was not ready when built; it is now,
  but its bounds stop at lat 5° N and the Pacific strikes off Colombia/Ecuador sit at 1.6–4° N, so I kept one consistent base. Max camera
  scale 1.34× (soft but clean at 1080p). Swap possible later (formula in assets/cartels/cts08/SOURCES.md).
- 70+/~250 shown on a paper isotype chart instead of counters on the map (avoids the same map treatment twice in a row).
- "The system was ready": HUD reticle on the Mexico map instead of a second THE DEAL build (the deal is used once, at the end).
- "instrumental" headline: no real headline image in hand → the line is told by the balance scale + credit "U.S. officials via NYT".
- SOTU: no rostrum photo/clip available; used the CC0 White House photo of the Trumps heading to the Capitol for the 2026 SOTU + the real
  quote verified on ABC News (Sam's paraphrase is NOT put in quote marks).
- El Universal front page swapped for Reforma (Universal's front has an unidentified woman beside burning cars — kept away from any
  risk of the unnarrated influencer rumour).

## Assets
New (assets/cartels/cts08/, 6.5 MB, SOURCES.md): Maduro official portrait (CC0), MDC Brooklyn (CC BY 4.0), Su-30MK2 (CC BY-SA 4.0),
rocket launchers Caracas parade (CC BY-SA 2.0), derived map crop/overlays/silhouettes, Caracas Esri z12 inset, Maduro stairs still.
Generator: `project/cartels/gen/cts08_assets.py`.
Shared used: footage x_boat_strike_secwar, x_maduro_stairs_stewart, m3_tapalpa_aerial_a; people mencho_mugshot_2, meza_fbi_photo_1,
trump_sotu2026_arrive_1; news front_pages 2026-02-23 reforma/jornada/milenio.
Lead must check: people/ and news/ still had NO SOURCES.md — trump_sotu2026_arrive_1 provenance found (Commons CC0, logged in my
SOURCES.md); mencho_mugshot_2 / meza_fbi_photo_1 provenance not verified by me.
Strike dot positions are illustrative (credit says "Strike locations approximate").

## Gotchas
- A map camera tweened as a proxy `{x,y,s}` with `onUpdate` also positions constant-size labels/pins (screen layer) — no 1-frame lag
  that a gated `FX.onFrame` reading GSAP values would have (FX.mount's proxy tween runs before later-starting tweens).
- `world_overlay.svg` country paths: the 49th-parallel border is one 1270-px segment — a "> 400 px jump" antimeridian filter drops the
  whole lower-48 ring; use > 4000 px and filter by bbox instead.
- When a helper builds DOM with `div(null, …)` make sure it doesn't `appendChild` on null (froze the whole timeline after scene 1).
