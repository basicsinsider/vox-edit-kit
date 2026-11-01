# ivs07 — NOTES (segment editor, 2026-11-01)

Master 781.38–949.00 (DUR 167.62; VO ends 946.81 "see." — the lead pads the VO with silence to 949.00).
Root `data-vo-start="781.38" data-duration="167.62"`. Plan: `project/ivan/EDIT_NOTES_ivs07.md` (30 scenes, every second covered).
**Generated file**: edit `project/ivan/gen/ivs07_src.html`, then `python3 project/ivan/gen/ivs07_build.py` (it inlines the simplified
Russia/Ukraine/Belarus paths + rail-city pixels from the Eastern-Europe map kit into `compositions/ivs07.html`).

## Checks
- Lint (sandbox, 0.8.217): **0 errors in ivs07** (the 2 errors the run reports are missing face-cam webms in intro02/intro03 — not mine);
  warnings only `nested_media_start_basis_ambiguous` (local data-starts, intended), file size, duplicate img (sc20 sharp + blurred copy).
- `sync_audit.py --transcript transcript_iv.json`: 0 flagged; every text cue is a literal `T(word start)`, applied at −0.06 s.
- Headless timeline dump (puppeteer + HF chrome, seek through the whole timeline): no console/page errors, `tl.duration()` = 167.62.
- §10.9 hold audit: every scene's key animation ends ≥ 0.5 s before its cut, except caption last-words that are SPOKEN < 0.5 s before
  a cut (sc23 "with" 908.78 → cut 909.26: the word lands with a 0.15 s rise and holds 0.42 s). Transitions/camera drifts are the motion
  the cuts ride on (cut on action).
- Snapshots of every scene (start/middle/end) looked at in 8 batches (≤ 8 frames each); fixes made: sc05 caption/grid collision, sc06
  first caption missing CSS + map left-edge gap + lighter fills, sc08 number size, sc20 focus box onto a face, sc23 caption off the
  silhouette, sc28 opening framed on the face, sc30 captions moved off Ivan's silhouette.

## Face cam — 12 shots, 55.7 s = 33.2 % of 167.62 s (33.6 % of the spoken 165.54 s)
sc01 wide (781.38–785.06) · sc07 medium 1.24 · sc10 close 1.5 · sc12 wide · sc15 medium-close 1.32 · sc17 wide · sc19 close 1.55 ·
sc21 medium 1.25 · sc24 wide · sc25 close 1.55 · sc27 medium 1.25 · sc29 1.4 — framing changes at every shot, 2–4 % push inside each.
Clean: grain/dust/vignette are set to 0 on every face scene (`ground("face")`). Text on him = per-word ink `.label-box` strips (one box per
word, appearing on its word) in the upper-left wall column (x 96, y 150) — clear of his face in every framing, readable on wall or poster.
`data-media-start` = master second (no offset added; the lead measures lip sync).

## First / last scene (boundary hand-off)
- First (781.38): face cam WIDE, static frame with a slow 3.5 % push — fresh shot after ivs06's outgoing motion.
- Last (940.17–949.00): BBC shot of Ivan's silhouette facing a sunset sea, slow push 1.00→1.07; closing line word by word, the image
  holds untouched to 948.35 (1.54 s after "see." ends at 946.81; text out 947.90–948.50), then fades to night 948.35–948.97. No title card (as asked).

## Effects / layouts used
Whips (plain ×5, light-flash ×2, vertical ×2), paper slides (×3, up and sideways), hard cuts on camera pushes, CCTV flash cut; map kit
(Eastern Europe night) with Russia/Ukraine overlays, rail routes drawn on, supply-train dots, break X's, radio rings from Moscow; isotype
row of grey men (ref 5 variation), isotype grid of 30 locomotives struck through, isotype pull-back of a dot field (brass cluster = 300–500
inside Russia's population); D08-style typeset report card with a stamp + typewriter lines; case-file card (Foma print + FOMA tag + counted
key number with brass highlighter + pen question mark); surveillance stills (REC, ticking timecode, corner brackets, focus box hunting,
DSLR focus hunt); Esri airbase aerial with a tightening perimeter; focal-blur call-out (§10.6.5) across a Moscow crowd + box markup;
passport card flip (rotateY) onto a grey-man ID page; typeset secure-chat thread with ticks + trust meter, then D15-style node (Lubyanka)
fed by an oxblood line; split azure/oxblood duotone behind a BBC silhouette (multiply); **painting-to-print reveal (§10.7)** for "Putin
won't live forever" (colour portrait full frame → pull-back/pan to our typeset newspaper column, colour → halftone print, pull-quote,
headline "What comes after Putin" set word by word with pen underlines); BBC footage ×5.
New in-house variations worth promoting: `flab()` per-word label-box strips for face cam; split-duotone silhouette (two-colour wall via
multiply); trust meter + forwarded-bubbles line; isotype pull-back with a CSS radial-gradient dot field (thousands of dots, zero DOM cost).

## Deviations / decisions (Krish asleep)
- Closing line shows the full spoken phrase "a future they may / never get to see" (8 words, two lines, word by word) — shorter would
  either reword the narrator or be a half-sentence; it is the final image and reads cleanly. Everything else is 2–5 words.
- sc03 shows "trains carrying military supplies" (not "…to the front") so the caption finishes before the paper slide.
- Freedom of Russia flag: drawn as the plain white-blue-white flag with the stripe in `--sky` (in palette); no emblem.
- The newspaper page is our own typeset page (section label "The future", no masthead, greeked body). Photo caption "Vladimir Putin".
- sc18 "arrest people": BBC courtroom-cage clip of a treason defendant (face visible as broadcast by the BBC); the BBC's "22 years for
  treason" title is cropped off. If the lead prefers no identifiable defendant, swap to `bbc_silhouette_wall.mp4` (same CCTV treatment).
- `tools/build_index.py` does not recognise `ivs*` ids (regex `seg|intro|c\d+s`); I used a private patched copy
  (`/tmp/ivs07tools/build_index.py`, adds `ivs`). **Lead: add `ivs` to that regex** so editors don't need a copy. `make_sandbox.sh`
  also doesn't link `vo_iv.mp3` / `transcript_iv.json` (I linked them by hand in work/ivs07).

## Gotchas for MANUAL §4.2
- Kit country paths (Russia) contain long antimeridian runs: instead of dropping sub-paths with > 400 px jumps (which deleted Russia's
  main ring entirely — the fill vanished), clamp all points to a box a little larger than the camera's reach; fills stay valid.
- On the dark `eastern_europe_night` map an overlay fill at 0.6 still reads as a red slab at these zooms — 0.42 (Russia) / 0.55 sky (Ukraine) keep the relief visible.
- A face-cam `.label-box` wrapping several words shows an empty ink box before the later words are spoken; one `.label-box` per word
  (padding = word gap, `margin-right:-1px`) grows like a strip and never shows empty ink.

## Assets
`assets/ivan/ivs07/{photos,footage,derived}/SOURCES.md` (6 Commons photos, 5 BBC clips, 2 derived). Kit: `eastern_europe_night.jpg`,
`eastern_europe_overlay.svg` (paths), `aerial_ivanovo_severny_airbase_z16.jpg`. Motif: grey man (inlined path). 14 MB total.
SFX markers: `compositions/ivs07.sfx.json` (54 markers, master seconds; one hero per scene + moves; no face-cam SFX).
