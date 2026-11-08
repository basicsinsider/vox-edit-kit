# pys07 — NOTES (segment editor, 2026-11-08)
Master 706.20–798.00 (91.80 s; `tl.duration()` = 91.800 checked in headless Chrome, full seek 0→91.8 without errors).
Plan: `project/paraguay/EDIT_NOTES_pys07.md`. Assets: `assets/paraguay/pys07/` (+ SOURCES.md), generator `project/paraguay/gen/pys07_assets.py`.

## Scenes (17 shots, 16 scene layers)
| id | master | picture | ground / effect |
|---|---|---|---|
| sc001 | 706.20–710.30 | FACE W, "with the benefit of hindsight" | face |
| sc002 | 710.30–716.20 | Stake timeline: Peña sash card (plum), plum bar Aug 2023 → **March 2025** (yellow highlighter) carrying a Ueno share certificate | paper, 12 fps bar, focus hunt |
| sc002n | 716.20–718.26 | ABC Color 5 Apr 2025 headline "…Peña dice que vendió sus acciones", plum pen underline; "sells his stake" | desk + web page, push |
| sc002 (back) | 718.26–721.46 | Timeline again, certificate gone, bracket "roughly two years"; push into the cut | paper |
| sc003 | 721.46–726.58 | Vox layered: Peña (plum duotone) ↔ ueno tower (teal duotone), pen link "investor", money chips pour into the bank — "money from the government" | night, layered panels drifting over blurred Asunción night |
| sc004 | 726.58–731.22 | FACE M + bone stamp CONFLICT / OF / INTEREST slammed beside him (word by word) | face, stamp |
| sc005 | 731.22–737.15 | FACE W, "wasn't the only law" | face (jump cut) |
| sc006 | 737.15–740.02 | BCP HQ on the Asunción skyline (native-res crop), label BANCO CENTRAL DEL PARAGUAY on "central"; "a pretty strong law" | night photo push |
| sc007 | 740.02–746.26 | Formula: dashed placeholders → EQUITY / rule / DEBT, drawn "≥", **12%** (yellow) | graph paper + cream, vertical whip |
| sc008 | 746.26–756.98 | Ref-1 bars: cash + short-term-assets cushion, dashed 12 % threshold, label-box "at least 12%", teal LOANS tower rises with a camera pull-back | stained paper, slide ←, camera zoom-out |
| sc009 | 756.98–760.72 | FACE C (no text) | face |
| sc010 | 760.72–764.10 | FACE M "above board" (framing change exactly at EDL join 760.717) | face |
| sc011 | 764.10–774.90 | Ueno's report sheet (logo mask, our type): ratio gauge to 15 % past the plum 12 % line; tilt down; bad loans count 0.00→**0.58%** (yellow highlighter); half-filled 1 % square "nearly half a percent" | desk + sheet, count 12 fps |
| sc012 | 774.90–777.60 | FACE W "sounds really good" | face, whip ← |
| sc013 | 777.60–783.67 | Magnifying glass slides over 0.58 % (sharp 1.45× copy inside the lens, rest focal-blurred), plum pen circle, "suspiciously good" | desk, focal blur + lens |
| sc014 | 783.67–792.72 | Bar chart 0–5 %: three "normal healthy bank" bars in a 2–4 % band (**2 to 4%** yellow) vs Ueno's tiny teal bar "just 0.5%" + logo | cream paper, vertical whip |
| sc015 | 792.72–796.55 | FACE M "too good to be true" (starts at EDL join 792.717) | face |
| sc016 | 796.55–798.00 | Stinger: 0.58 % (halate yellow hero) — crack on "It", splits and falls apart on "was." — "It was." | light-flash whip, cut on action into pys08 |

First scene: fresh face-cam shot. Last scene: the two halves of 0.58 % still falling at 798.00 (cut on action).

## Effects / layouts used
Whips ×6 (horizontal ±, vertical ±, light-flash), hard cuts on action ×5, paper slide, jump cuts; timeline with travelling token; news-page
evidence with pen underline; Vox layered panels; stamp call-out beside the face cam; formula build with placeholders; ref-1 bars + dashed
threshold + label-box; isotype-ish half square; count-up; **magnifying-glass focal call-out (new)**; bar chart with range band; crack/split
number stinger (new); focus hunt ×2; highlighter ×4 (each the one key number/phrase of its scene).

## Face cam
sc001 4.10 + sc004 4.64 + sc005 5.93 + sc009 3.74 + sc010 3.38 + sc012 2.70 + sc015 3.83 = **28.32 s / 91.80 = 30.9 %** (target ≈35 %; the remaining
lines are numbers that need a picture). Edges checked frame by frame (ffmpeg tiles at 24 fps): sc001 uses `data-media-start` 706.24 (not 706.20)
because the source frame at 706.20 is still the previous take (EDL join 706.233) — 40 ms lip offset, invisible. Joins 737.15, 760.717, 792.717
are exactly on cuts; 756.817 and 780.967 fall inside B-roll / before a face shot starts. Framing origin 1000 px 160 px (head never cropped in C).

## Decisions / deviations
- "just 0.5%" at 791.27: ASR said "0.5%", I re-ran Parakeet on the raw window (`asr_win.sh 1064.5 1070` → "just point five percent") → shown as
  "0.5%" (his words). The stinger shows 0.58 % (the number from the report) as an image, not as a quote.
- "of above" (ASR) — no text on it; the drawn "≥" carries "or above".
- ABC article (shared/docs, fair use) added for "sells his stake" — not in the lead's brief, but it's the real report of the sale; the
  timeline continues around it.
- sc002 axis tick "AUG 2023" is a chart label (not spoken) — the lead's brief asked for the inauguration start.
- Credits on screen: ROC presidency CC BY 2.0 (Peña sash), Infobae · Reuters · Cmasi CC BY-SA (sc003), Cmasi CC BY-SA (BCP), ABC Color.

## For the sound designer
`compositions/pys07.sfx.json` (39 markers, master seconds). The ending wants a crack/stinger (`paper_tear` + `boom_low` marked — a glass/ice
crack sample would be better if the library has one). Money chips in sc003 marked `dot_ticks` (coin clinks if available).

## Gotchas for MANUAL
- A highlighter span with `z-index:-1` inside an inline-block disappears behind an opaque shot background: give the wrapper `isolation:isolate`
  (lint warns `negative_z_index` but it renders correctly then).
- Magnifier call-out: lens = circle `overflow:hidden` holding a full-frame copy of the scene (same cam transform), scaled ×1.45 with
  `transform-origin` = lens centre, `left/top` = −lens corner, all written from one tweened proxy `onUpdate` (seek-safe); the base copy gets
  `blur()` = focal blur. Size the content so the target fits the lens after magnification (a 220 px number at 1.75× overflowed a 520 px lens).
- Showing the same scene layer twice around a cutaway: list it twice in the SC array (two show/hide windows) — its timeline keeps running underneath.
- A tween that ends even 0.02 s after DURATION lengthens the timeline — check `tl.duration()` (headless `--no-sandbox` dump works as root).

## Open issues
- Face cam 30.9 % (< 35 %).
- sc011 tilt: the ratio row leaves through the top edge during the tilt (camera move on a document — intended).
- Lint warnings only (nested media start basis, file size, negative z-index); 0 errors for pys07.
