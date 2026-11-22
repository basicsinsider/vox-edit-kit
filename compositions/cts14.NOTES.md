# cts14 — NOTES (cts14 editor, 2026-11-22) · master 1286.292–1341.912 (DUR 55.620) · THE ENDING

Plan: `project/cartels/EDIT_NOTES_cts14.md` (9 scenes, exact word cues). Data generator: `project/cartels/gen/cts14_data.py`
(inlines the CDC series + the Mexico overlay paths between `@@DATA-BEGIN/END`; re-run after editing the data block region).

## Scenes built
| sc | master | what | effects / ref |
|---|---|---|---|
| 001 | 1286.292–1290.30 | question card "is it / WORKING?" | cts02 `makeTitle` copied verbatim (classes renamed `c14-tt*`), chip + bar slaps on "Is"/"working", push-through into the bar |
| 002 | 1290.30–1297.80 | Narcos aside: flat TV in a dark room plays SEDENA's arrest walk; NARCOS logo slams on "Narcos"; TV switches off on "is this actually working?" | TV power on/off (12 fps), push |
| 003 | 1297.80–1311.90 | REAL CDC line chart 2015–Jun 2026: rise drawn on "for the first time in a long time", fall on "mostly yes", the fall holds under "weaker" (no inset), latest point counts 112,418 → **65,724** (yellow, the one glow) on "fewer", −42 % bracket | ref ast_06720d0b255d4d29 (glowing curve on black, milestone markers) |
| 004 | 1311.90–1318.30 | case board: Caro Quintero / Maduro / El Mencho / El Chapo Isidro on an ember string timeline (Feb 2025 → Nov 2026), stamps on "caught"/"killed", pen bracket under all four "IN 21 MONTHS" (Feb 2025 → Nov 2026) on "faster" | cts02 board look, stamps, FX.markup.pen |
| 005 | 1318.30–1323.72 | THE DEAL (`CT.deal`), ARRESTS on "Mexico", focus "arrest" | motif |
| 006 | 1323.72–1327.40 | "cartels not going away": m2_burning_trucks_a in a phone card on its blurred fill, `CT.dateTag` Northern Sinaloa · 20 Nov 2026 | light-flash whip |
| 007 | 1327.40–1331.30 | the Chihuahua lab (narcolab_b) closes into a giant "$12" knock-out on "twelve", BILLION (yellow) / A YEAR, source UNODC WDR 2025 | ref ast_db095fac62b54549 (numerals filled with the picture); multiply knock-out |
| 008 | 1331.30–1334.45 | the long line: 12 rim-lit silhouettes receding into fog, shuffling one step, beside an EMPTY `CT.file` (no photo, no name) | stop-motion 12 fps |
| 009 | 1334.45–1341.912 | night map (mexico_night): Sinaloa ember, US border states steel, Mex 15 north to Nogales with pulses that SLOW DOWN, pull-out; last 1.6 s dims to charcoal: "US vs CARTELS" small + SEARCHING LESSONS | screen-space constant-size labels, END card |

Transitions: push-through → TV on → line/hard cut → whip ← → hard cut on action → light-flash whip → vertical whip → hard cut on action → whip ←.

## Checks
- lint (`compositions/cts14.html`): 0 errors, 5 warnings (nested media data-start = composition-local, file size).
- sync_audit (`--transcript transcript_ct.json`): 11 cues, all −0.06 s, 0 flagged.
- headless timeline dump: `tl.duration()` = 55.62 = DUR; no key animation ends < 0.5 s before a cut (only camera/whip moves).
- Snapshots of every scene (start, middle, end) and every cut ±0.05 s looked at; fixes made: stamps moved off faces + paper backing,
  El Mencho crop, queue lighting/rim, file scale inside margins, map label overlap (SINALOA/Guasave) and US label off the top edge,
  "A YEAR" hold (cut moved 1331.25 → 1331.30).

## Data / deviations
- Overdose chart = predicted 12-month counts from gatherer B's CSV; verified Jun 2026 value against data.cdc.gov myself. "−42%" = −41.5 %.
- Lead QA fixes (2026-11-22): DEA pill inset REMOVED (its 76 %/29 % could only be seen via search snippets — dea.gov blocked);
  "ALL IN 2026" bracket replaced by "IN 21 MONTHS" spanning all four cards (Feb 2025 → Nov 2026). Re-snapshotted, lint/sync/duration re-run.
- Board photos reuse other editors' files: `assets/cartels/cts06/photos/caro_quintero_arrival_us_2025.jpg`, `assets/cartels/cts08/photos/maduro_portrait.png`
  (neither folder had a SOURCES.md line for them when I checked), `assets/cartels/people/mencho_mugshot_2.jpg`, `meza_fbi_photo_1.jpg`
  (`assets/cartels/people/` still has no SOURCES.md). Caro Quintero's stamp says "SENT TO U.S." (Feb 2025 transfer), not "caught".
- Clip reuse: x_isidro_airport_walk (2nd use, cts01), m2_burning_trucks_a (2nd use, cts01), x_chihuahua_narcolab_b (1st).
- New asset: `assets/cartels/cts14/logos/narcos_logo.png` (Commons, CC BY-SA 4.0, credited on screen) — `assets/cartels/cts14/SOURCES.md`.
- The question card reads "is it WORKING?" (DECISIONS 8); Sam says "Is this working?" — same card text the lead specified.

## Gotchas for the lead / MANUAL
- `tools/make_sandbox.sh` does not link `vo_ct.mp3` / `transcript_ct.json` into the sandbox → lint errors `audio_src_not_found`; I linked
  them by hand in `work/cts14/`.
- Knock-out numerals over footage: a night-coloured div with white text and `mix-blend-mode: multiply` inside an `isolation:isolate`
  wrapper above the `<video>` — outside goes charcoal, the numerals show the clip (no SVG mask / font-in-mask problem).
- Constant-size map labels during a pull-out: drive the camera with a proxy object `{px,py,s}` and place label divs in screen space in the
  same `onUpdate` (fade by scale thresholds).
