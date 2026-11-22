# cts01 — COLD OPEN (master 0.000–68.167, DUR 68.167) — editor notes

Generated file: `compositions/cts01.html` is BUILT by `python3 project/cartels/gen/build_cts01.py` from
`project/cartels/gen/cts01_template.html` (map data inlined from the kit json + `cts01_aerial.json` / `cts01_city.json`).
Edit the template, then rebuild. Derived assets: `project/cartels/gen/cts01_assets.py` → `assets/cartels/cts01/derived/`.
Refined plan: `project/cartels/EDIT_NOTES_cts01.md`.

## Scenes (14)
| id | master | picture | effect / ref |
|---|---|---|---|
| sc001 | 0.00–3.40 | ★1 LMP broadcast on a flat-screen monitor, push in; date tag GUASAVE, SINALOA · 20 NOV 2026 on "baseball" | hard open, TV framing, CT.dateTag |
| sc002 | 3.40–11.28 | ★1 fan phone video on blurred fill; inset map card Mexico → zoom box → Sinaloa close-up, GUASAVE pin on "Guasave", Sinaloa outline + label on "Sinaloa"; contrast call-out on the ducking fans | zoom box (ast_671f213364e14029), FX.contrastCallout |
| sc003 | 11.28–14.80 | ★1 LMP broadcast, player in the "Kuroda" jersey walking off | hard cut on action |
| sc004 | 14.80–18.40 | kit Esri z18 aerial of Kuroda Park, pull back, OSM stadium outline + KURODA PARK on "stadium", ember radio pulses outside the walls on "gunfight" | whip-out, FX.radioWaves |
| sc005 | 18.40–24.16 | ★2 two vertical phone videos: tracers over the street, then the helicopter firing slides in on "helicopters" | light-flash whip, two-up panels |
| sc006 | 24.16–30.30 | ★2 Noroeste vertical (burning trailers on the highway) → hard cut → AJE wide (truck + cars burning) | hard cuts |
| sc007 | 30.30–32.00 | kit z16 aerial of Guasave, 8 ember X blocks pop at 12 fps on "block the way" (no number) | whip, rough markers |
| sc008 | 32.00–36.18 | SEDENA airbase walk, heavy blur + vignette, sharpens on "one man" | focus pull |
| sc009 | 36.18–41.00 | 2.5D: halftone duotone cut-out of Meza Flores, EL CHAPO ISIDRO word by word (hero glow) | 2.5D, flash cut |
| sc010 | 41.00–44.20 | two cards: Meza Flores / Joaquín "El Chapo" Guzmán (2017 extradition photo), pen ≠ on "not related" | slide, FX.markup.pen (ref ast_8693d810270e43fd) |
| sc011 | 44.20–57.86 | CT.file (ember) on a sand desk + the real FBI Ten Most Wanted poster sliding under it on "FBI's"; rows LIST / REWARD typed on "10" / "$5"; yellow highlighter on $5,000,000; WANTED on "catch" | CT.file, highlighter (ref ast_8693d810270e43fd) |
| sc012 | 57.86–60.10 | SEDENA: detainees escorted up the ramp of an Air Force plane; date tag 21 NOV 2026 | hard cut |
| sc013 | 60.10–61.70 | the same file, CAPTURED (olive) on "had him" | whip ← |
| sc014 | 61.70–68.17 | the real @Defensamx1 post (cropped to header + text), push in; yellow highlighter on "derivado de la coordinación entre organismos de inteligencia de la Secretaría de la Defensa Nacional y de los E.U.A."; steel pen under "de los E.U.A." on "the United States" (first steel of the video); small translation label | slide ↑, highlighter, pen |

## Checks (2026-11-22)
- lint (`npx --yes hyperframes@0.8.217 lint compositions/cts01.html`): 0 errors, 13 warnings (nested media data-start "ambiguous" — this
  segment starts at master 0, so local = global; duplicate-media warning for the blurred-fill copies; file length).
- sync_audit: 13 text cues, all −0.06 s, "0 cue(s) flagged".
- timeline duration (headless dump): 68.167 == DUR; seek through the whole timeline: 0 errors; hold audit: no key animation ends < 0.5 s
  before a cut.
- Snapshots looked at: every scene start/middle/end and every cut at −0.05/+0.05 s (no black or empty frames).

## Deviations from the lead's plan
- sc012/sc013 order: footage first ("By the end of the night, the Mexican army"), then the file's CAPTURED stamp on "had him". CT.file sets
  the stamp word at build time, so CAPTURED is a second file instance in the same layout (the first one keeps WANTED).
- sc012 date tag shows the date only (21 NOV 2026): the airfield in the boarding video is not identified in SOURCES.
- sc008 uses the airbase walk (daylight-dusk, 21 Nov) heavily blurred/graded under "had come for one man" — it is the true man; it is sharp
  only for ~0.8 s.
- Translation label under the SEDENA post ("…coordination between the intelligence agencies of Mexico's Defense Ministry and the U.S.",
  marked "SEDENA · 21 Nov 2026 · translated") = explanatory document text, not narration. Remove it if the lead disagrees.
- Roadblock X's (sc007) sit on main roads of Guasave as an illustration — no count, no claim of exact locations (none published).
- The inset map's wide view is my own crop of `americas_satdesat` (the kit's `mexico_*` was not there yet when I built it); the close-up,
  both aerials and the stadium outline are the kit files.

## Assets / open items for the lead
- `assets/cartels/people/` and `assets/cartels/news/` still have NO SOURCES.md: the lines for meza_fbi_photo_1, meza_fbi_poster_1,
  guzman_2017_1 and x02_defensa_communique are listed in `assets/cartels/cts01/SOURCES.md` — please carry them over.
- Reused later by design: the cold-open clips return in cts13. meza_fbi_photo_1 is used 3× here (2.5D, card, file) — the same person, one scene arc.
- `hyperframes remove-background` fails on this box (onnxruntime-node binary download 404 — it tries the CUDA build); the Meza cut-out
  was keyed by flood fill instead (plain studio background).

## Gotchas worth adding to MANUAL
- `tools/make_sandbox.sh` doesn't link `vo_ct.mp3` / `transcript_ct.json`: `ln -sfn ../../vo_ct.mp3 work/<seg>/` by hand.
- CT.file: one stamp word per instance (text set at build) — for WANTED → CAPTURED use a second instance with the same options.
- A wide map + close-up inside a small inset card: run two cameras, zoom the wide one into its zoom box (ease-in) and hard-swap to the
  close-up at peak speed; labels follow image points via a proxy tween's onUpdate (`follow()` in the template).
- A cropped X post (header + text only, white fade at the crop) leaves room under it for a translation line and keeps the credit clear.

## Fix round 1 (2026-11-22, Agent A) — FIXES_ROUND1 #1/#7 + English on screen
Timeline v1 unchanged (DUR 68.167, every cue on its v1 word). Edit the template + `python3 project/cartels/gen/build_cts01.py`.
- sc001: arrives from the cts00 pre-roll — starts mid-push (scale 1.12 in the inline style, so frame 0 = frame 1); the date tag moved to
  cts00 (no repeat).
- sc002: the fan video CONTINUES from the pre-roll cut (`derived/fans_cont_slow.mp4` = source 4.5–10.4 s at 0.67×): no repeated frames,
  and the old man ducking behind the rail lands on "ducking" (contrast call-out ellipse re-aimed at him).
- sc008 hook "come for **one man**": ember target brackets snap round the walked man at 35.30 (12 fps, 3 steps) + a 2-step punch-in.
- sc009 hook "EL CHAPO ISIDRO": words SLAM in at 12 fps (scale 1.25 → 1) on their cues, frame shake (plain `tl.set`s at 12 fps) after
  CHAPO and ISIDRO, extra flash on ISIDRO.
- NEW sc011p 51.46–53.70 ("and the US government was offering"): hard cut to the real FBI poster full-frame, fast tilt from the header to
  the REWARD line, highlighter on "offering a reward of up to $5 million" (52.78, holds 0.5 s), hard cut back to the file for "$5".
- sc014 ENGLISH: the @Defensamx1 post is now a small "Original post · Spanish" card under a paper translation card (Crimson Pro): “It is
  reported that, as a result of coordination between intelligence agencies of the Ministry of National Defense and of the U.S., carried
  out as part of bilateral cooperation with that country…” (kicker "SEDENA (Mexico’s Defense Ministry) · 21 Nov 2026 · translated",
  credit "… · translated"). Highlighter on "coordination between intelligence agencies" at 65.0 (+ the same phrase in the original),
  steel underline under "and of the U.S." on "the United States" 66.81. Translation = my literal rendering of the post's first sentence.
- Checks: lint 0 errors / 13 warnings; sync_audit 0 flagged (13 cues, all −0.06); headless dump DUR 68.167, seek 0→68.167 no errors;
  snapshots looked at: 0.0/0.042/0.5, 3.35/3.45, 5.0, 8.95, 9.6, 35.1, 35.7, 36.13/36.23, 36.3–37.6, 40.5, 51.41/51.51, 52.3, 53.4,
  53.65/53.75, 56.0, 61.3, 61.6, 62.3, 65.8, 67.6, 68.1.
- Gotcha: when reading a 2-column contact sheet of snapshots, the right column is offset by 960 px — I first "saw" the 2.5D title jump
  900 px; it didn't. Check single frames before debugging.
