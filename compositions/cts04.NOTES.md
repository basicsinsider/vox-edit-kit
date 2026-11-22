# cts04 — NOTES (segment editor, 2026-11-22) · master 264.167–358.208 (DUR 94.042)

Plan: `project/cartels/EDIT_NOTES_cts04.md` (12 scenes, exact word cues). Assets: `assets/cartels/cts04/` (+ SOURCES.md), generator
`project/cartels/gen/cts04_assets.py` (needs the raw downloads; URLs in SOURCES.md).

## Built
| sc | master | picture | effect / ref |
|---|---|---|---|
| 001 | 264.17–268.48 | real DOJ release (2019) "also known as “Chapo Isidro,”" | night desk, tilted page push, yellow highlighter on "nickname" |
| 002 | 268.48–276.56 | Guzmán booking photo (CC0) + Isidro FBI photo as pinned cards; tags JOAQUÍN "EL CHAPO" GUZMÁN / "EL CHAPO ISIDRO" | paper, duotone cards, pen arrow; ref ast_8453bcb46af0421b |
| 003 | 276.56–280.16 | CHAPO branches in two: story 1 (Guzmán, ticked) / story 2 (empty card, "?") | night chalk-pen tree, hero glow on CHAPO |
| 004 | 280.16–285.44 | dictionary: CHAPO → CHAPEAR, RAE definition built on "clearing / bushes / machete", English gloss | lined paper, typewriter, highlighter; ref ast_05ca6a314e6642fa |
| 005 | 285.44–293.36 | ink brush field swaying; ember machete swipe clears it on "clearing out his rivals"; CHAPO rises | night, procedural pen drawing + clip wipe (no people, no weapons on anyone) |
| 006 | 293.36–298.21 | the two stories as cards + big pen "?"; machete card comes forward on "how he operates" | night desk |
| 007 | 298.21–336.42 | THE REVOLVING DOOR BOARD (see below) | grid paper, real clippings, stamps, pen markups, camera board moves; ref ast_b2e1defddf434c8c |
| 008 | 336.42–341.41 | the real seizure photos (Gabinete de Seguridad, Harfuch's post 4 Dec 2024), Vox layered background | night, duotone back plate + two colour cards drifting, CT.dateTag "SINALOA · 3 DEC 2024", CT.credit |
| 009 | 341.41–346.77 | punch-ins into the truck bed on "huge … like huge" | hard cuts on the push, focus hunt |
| 010 | 346.77–350.77 | drawn dial scale, pill sacks drop, needle → just past 1; "1,000 KG" on "measuring", **1 TON** (yellow key number) on "One ton" | paper, 12 fps |
| 011 | 350.77–354.25 | real FBI Ten Most Wanted poster, push header → photo; steel label "ADDED 4 FEB 2025" pinned beside the photo on "February" | night desk |
| 012 | 354.25–358.208 | CT.file (ember) already holding Charged / Arrested / Seized; List row types "FBI Ten Most Wanted" on the words; WANTED stamp on "list" (holds 0.57 s) | TARGET FILE motif |
Transitions: whip → · hard cut · flash whip ↑ · whip ← · hard cut · paper slide → · whip ← · hard cut · whip ↓ · flash whip → · whip ↑.
Grounds: night, paper, night, paper, night, night, paper, photo, photo, paper, night, paper.

## The "revolving door" look — for the cts06 callback (521–540 s)
Grid-paper board (`assets/cartels/cts04/derived/graph_tile.jpg`, background-size 1962 px, repeat + paper_cream_01 multiply 0.45).
A hand-inked horizontal year axis (ink #1d1a16, 5 px), tick + Cooper Hewitt label per year (24 px), years 300 px apart.
**Above** the axis = "UNITED STATES" lane (t-label 26 px, steel-dark): the 2012 charge — a white clipping of the FBI poster sentence with a
yellow highlighter on "originally indicted on May 2, 2012", a steel pin on the axis + dashed steel-dark lead, label-box
"CHARGED IN THE US · 2012" (steel-dark box, bone Haskoy 40 px). **Below** = "MEXICO" lane (olive-dark label): four pinned sand cards
270×214 (Haskoy year 80 px, small olive-dark "ARRESTED" stamp box), slightly rotated (−2.5/2/−1.5/2.5°), 2014 twice (second "+1 MONTH");
then a big ember-dark **RELEASED** stamp (Haskoy 42 px, 4 px border, rotated −11/−6°) slammed across each card, an ember hand-drawn
circular arrow (↻, r 38, boiling pen filter) on each card's corner = the revolving door; a yellow label-box **4×** sits in the empty
2012–2013 gap of the Mexico lane; an ember dot with a bone ring runs along the axis and dips through every card; a black pen ellipse
circles all four RELEASED. A thick ember line then keeps running along the Mexico lane to a "DEC 2024" ember-dark label-box.
To echo it: reuse the same tile + card/stamp styling (classes `.c4-arr` / `.c4-stamp` in cts04.html are local — copy the CSS), or simply
show a 3-s crop of this board (render frame ~ master 331.5 = everything on, pen ellipse included).

## Shared assets used
docs/d09_doj_mezaflores_2019.jpg · people/guzman_booking_1.jpg (via derived crop) · people/meza_fbi_photo_1.jpg · people/meza_fbi_poster_1.jpg.
NOTE: `assets/cartels/people/` still had no SOURCES.md when I finished — the Guzmán booking photo is Commons CC0 (I checked the Commons
listing; logged in my SOURCES.md); the FBI poster/photo are public domain.

## Deviations / decisions
- "chapear": RESEARCH did not cover it; I verified the DLE definition through a search result quoting dle.rae.es (the site answers 403 here).
  If the lead prefers zero risk, sc004 can lose the "2. tr. Am. Cen.…" line — the definition is the real DLE wording.
- "the other chapo": no source for a Spanish "El otro Chapo" nickname, so the second tag is his documented alias "EL CHAPO ISIDRO" (FBI/DOJ).
- Arrest years are "per Guacamaya Leaks" — shown via the real EjeCentral clipping and its credit; no other source label.
- Seizure date tag "Sinaloa · 3 Dec 2024" (not Ahome — the two raids' exact towns differ between reports; the post says "en Sinaloa").
- sc011 uses a pinned label instead of CT.dateTag: the night date tag was unreadable over the white poster.
- sc003/sc005/sc006 halate "CHAPO" is the one glow of each night scene.

## Checks
- lint (`npx --yes hyperframes@0.8.217 lint compositions/cts04.html`): 0 errors, 3 warnings (duplicate img discovery — the Guzmán crop is
  used in 3 scenes; gsap_callback_dom_measurement — onUpdate only writes text/attributes from build-time samples; file length).
- `python3 tools/sync_audit.py compositions/cts04.html --transcript transcript_ct.json`: 25 cues, all −0.06 s, 0 flagged.
- Headless timeline dump: `tl.duration()` = 94.042 = DUR; no runtime errors when seeking 0–94 s every 0.5 s. Hold audit: every key
  animation ends ≥ 0.5 s before its cut except camera pushes / secondary drifts (cut on action).
- Snapshots looked at: every scene start/middle/end and every cut ±0.05 s (12 batches).

## Gotchas for the lead / MANUAL
- `tools/make_sandbox.sh` does not link `vo_ct.mp3` / `transcript_ct.json` → lint error audio_src_not_found in the sandbox; I added the links by hand.
- `paper_graph_01_hires.jpg` tiled with `background-repeat` shows a dark scan corner/edge as a stray line across the board — use a crop to
  whole grid cells (cts04 `graph_tile.jpg`).
- A camera framing at scale s on a photo plate must keep `y ≤ 0` (py ≥ 540/s) or a band of ground shows at the top (sc009 first pass).
