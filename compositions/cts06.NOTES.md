# cts06 — NOTES (segment editor, 2026-11-22)
Master 450.917–540.417 (DUR 89.5). Plan: `project/cartels/EDIT_NOTES_cts06.md` (14 scenes, exact word cues).

## What I built (scene · effect · ref)
- sc001 450.917–462.97 — EO 14194 Federal Register pages on a night desk: camera drift over the header during "unlike China or India or Korea"
  (Mexico's order ONLY, no country comparison — SEGMENTS §4), pen underline "products of Mexico", highlighter "additional 25 percent ad valorem
  rate of duty" + a "25%" ink label box (yellow) in the page margin, pen circle on "fentanyl", contrast call-out on the DTO/fentanyl paragraph
  ("the statements"). MANUAL #5 / §10.6.
- sc002 462.97–473.69 — rebuilt ref **ast_3d5f46c4c01248c5**: "U.S. goods imports, *by country*" (2024, US$ bn, Census). Mexico olive, five
  others ash; $505.9 BN yellow label box; steel pen arrow + "25% TARIFF", Mexico's bar shudders on "huge threat". Slide in.
- sc003 473.69–477.98 — Sheinbaum (olive duotone) ↔ Trump (steel duotone) cards, dashed phone line, handset badge on "phone" + radio rings,
  date tag "PHONE CALL · 3 FEB 2025". Whip.
- sc004 477.98–482.70 — AP photo: Guardia Nacional on patrol at the border, Ciudad Juárez, 5 Feb 2025. **No number** (the "100,000" slip,
  DECISIONS #3). Hard cut.
- sc005 482.70–487.66 — desk callback: rack focus from the tariff order to the overlooked DOJ release (date sharp, headline kept blurred
  so "29" isn't readable before it's spoken); the order slides off. Flash whip.
- sc006 487.66–491.18 — GN troops deploying (El Imparcial, Feb 2025) + **10,000** counter (yellow halate hero). Vertical whip.
- sc007 491.18–499.26 — rebuilt ref **ast_0b23d2c7a06c4bb3** (waffle): 29 ember tiles on "29", DOJ release 27 Feb 2025 card, pen underline
  "Taken into U.S. Custody". Slide up.
- sc008 499.26–503.30 — FBI Ten Most Wanted poster of Rafael Caro-Quintero (PD): pen circle on the "Photograph taken in 1985" photo,
  highlighter "FELONY MURDER OF A FEDERAL AGENT". Whip.
- sc009 503.30–505.50 — Enrique "Kiki" Camarena (DEA portrait) on the RCA XL-100 TV (past = vintage screen), CRT power-on, name tag. Hard cut.
- sc010 505.50–510.95 — 40-year ruler 1985→2025: 1985 poster photo ↔ 2025 US arrival photo, steel dot chases, **40 YEARS** (yellow hero),
  steel "25% TARIFF" stamp on "tariffs". Whip.
- sc011 510.95–521.26 — waffle grows: +26 (AUG 2025) +37 (JAN 2026) with the DOJ releases stacking, total **92** (yellow), dashed empty slots
  blink on "this will just continue". Slide.
- sc012 521.26–532.30 — callback to cts04's revolving-door board (matched to `cts04.NOTES.md`: `cts04/derived/graph_tile.jpg` ground, ink axis,
  sand arrest cards with year + olive ARRESTED stamp, big ember-dark RELEASED stamps, ember ↻ arrows): REWIND pan (horizontal smear + scanlines),
  Isidro's FBI photo + name on "El Chapo Isidro", cards drop on "four times", RELEASED + arrows on "came out four times". Vertical whip.
- sc013 532.30–536.78 — Altiplano federal prison gate + SSPC trucks (Gabinete de Seguridad clip, Jan 2026) on its blurred fill; ember radio
  rings from the prison on "running their cartels from prison". Whip.
- sc014 536.78–540.417 — ADX Florence (BOP, PD) print + "U.S. federal supermax prison"; steel bars slam in 3 frames on "American prison" + shake.
  Flash whip.

## The prisoner waffle — for cts13's callback (92)
Sand paper ground (paper_cream_02 + paper_stained_01_hires multiply 0.35). Title "Cartel prisoners sent to the U.S." Haskoy 800 ink 58 px at
left 200 / top 132, crossed by an ink rule (y 206, x 160–1160, 3 px) and a short vertical tick (x 186, y 120–240) as in the ref; subline
t-label 22 px ink-soft "EXPELLED FROM MEXICO · SOURCE: U.S. DEPT. OF JUSTICE". Grid: 10 columns, origin (200, 300), pitch 62 px, tiles 52 px
with a 2 px border and faint horizontal scan lines; 100 faint empty cells (2 px ink 16 %) mark the grid from the start. Batches fill
row-major at 12 fps (2-frame pop from scale 1.4): Feb 2025 = 29 tiles `--ember` / border `--ember-dark`; Aug 2025 = 26 tiles `--ember-dark`
/ border #4f1b06; Jan 2026 = 37 tiles `--ember-light` / border `--ember-dark`. Legend column at x 860 aligned to the row where each batch
starts (rows 0 / 2 / 5): swatch 40 px + Haskoy 48 px number + t-label date. Total at row 8: label-box "92" (yellow on ink, 64 px) + "TOTAL".
Dashed slots (3 px dashed ink-soft) blink on after tile 92. DOJ release cards (640 px wide, tilted 2.2 / −1.6 / 1.2°) stack at x 1150–1824.
Code: `board()` in `compositions/cts06.html` (constants GX/GY/P/BATCH/DOCS) — copy it, or use a still of master ≈ 520.5.

## Data / accuracy
- Chart: U.S. Census Bureau "Top Trading Partners – December 2024" (goods, Census basis, US$ bn), page saved in
  `assets/cartels/cts06/data/` — verified on census.gov 2026-11-22: Mexico 505.9, China 438.9, Canada 412.7, Germany 160.4, Japan 148.2, Vietnam 136.6.
- 10,000 = Sheinbaum's own post (3 Feb 2025, verified via api.fxtwitter: "10 mil elementos de la Guardia Nacional"). 29/26/37 = DOJ releases (shared docs).
- 92 is shown as the grid total (lead's plan; Sam says "90 some" later in cts13).

## Assets
New (all logged in `assets/cartels/cts06/SOURCES.md`, 2.9 MB): FBI Caro-Quintero poster top (PD), Caro Quintero US arrival photo (Excélsior,
813 px, used as a 600 px card), AP Juárez GN patrol, El Imparcial GN deployment, La Crónica Sheinbaum 3 Feb 2025, Trump official portrait (PD),
ADX Florence (BOP, PD, 960 px — used ≈1.1× as a framed print), Census page. Shared: docs d03 p1/p2, d06/d07/d08; people camarena_1,
meza_fbi_photo_1; footage x_prisoner_transfer_convoy; c5 RCA XL-100 frame (CC BY-SA, credited); cts04 graph_tile.
Substitutes / missing: no photo of the actual Sheinbaum–Trump call exists (none published) → two portraits + a drawn phone line. No
photo of the Feb 2025 plane boarding of the 29 → the DOJ release + the waffle. ADX image is low-res (only BOP/Commons PD version found).

## Checks
- `npx --yes hyperframes@0.8.217 lint compositions/cts06.html` → 0 error(s), 4 warning(s) (nested media data-start is composition-local;
  duplicate img discovery (same DOJ/EO images used twice); gsap_callback_dom_measurement (count/pen onUpdate only write values); file length).
- `sync_audit.py --transcript transcript_ct.json` → 25 text cues, all −0.06 s, "0 cue(s) flagged".
- Headless dump: `tl.duration()` = 89.5 = DUR; seek 0–89.5 every 0.25 s, 0 runtime errors.
- Snapshots looked at (14 batches): every scene start/middle/end and every cut ±0.05 s; hold rule checked — cuts moved to 503.30, 510.95,
  532.30 so every key animation holds ≥ 0.5 s.
- `compositions/cts06.sfx.json`: 53 markers, all types exist in place_sound.py.

## Gotchas for the lead / MANUAL
- `tools/make_sandbox.sh` does not link `vo_ct.mp3` / `transcript_ct.json` — add `ln -sfn ../../vo_ct.mp3` etc. by hand (or add them to the script).
- Shared docs were re-captured while I worked (d06 changed from 3840 to 1800 px wide between two listings) — re-check bboxes in the doc JSON
  right before building on them.
- Readable-before-spoken trap: a real document shown before its number is narrated (DOJ "29 Wanted Defendants" headline 6 s early) — keep it
  blurred (masked blur copy with a sharp ellipse on the date) until the word.
- An SVG drawn under DOM cards hides markups that overlap the cards (cts04's ↻ arrows) — give the svg `z-index` above the cards.
- `at()` camera helper with rotation compensation (centres a page point correctly at any rotation) — in cts06.html, worth adding to fx.js.

## Fix round 1 (2026-11-22, Agent B)
- #10 (v1 08:00 ≈ 480 s, sc004): Sam misspoke "100,000 troops" — a printed correction slip (paper card, bottom-right, over legs/grass
  only): "10,000 TROOPS*" with a yellow highlighter on 10,000, slides up on "100,000" T(479.20); note "* Correction: 10,000 — not 100,000"
  (Crimson Pro italic) on "troops" T(480.00); holds to the cut at 482.70. Audio untouched. sfx: paper_slide 479.2 + highlighter_swipe 479.5.
- sc006 label "Guardia Nacional" → "Guardia Nacional · National Guard" (English gloss). English sweep: the Altiplano prison sign in the
  sc013 SSPC clip is small and glossed by the date tag "Altiplano Federal Prison, State of Mexico"; everything else English.
