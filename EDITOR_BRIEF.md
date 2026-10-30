# Editor brief (all six segment editors)

You build ONE segment of a 10-minute documentary edit as a HyperFrames sub-composition.
Project root: the folder containing this file.

## Read first (in this order)
1. `MANUAL.md` — all of it. It is the style law (palette, fonts, textures, effect recipes, HyperFrames gotchas).
2. `SEGMENTS.md` — your segment's time range, scenes, continuity rules and conventions.
3. `EDIT_NOTES.md` — your scenes (exact on-screen text, word cue times, effects, assets, SFX). Follow it; improve
   craft freely, but don't drop effects or reference layouts assigned to you (coverage is planned across segments).
4. `DECISIONS.md` (lead's answers to open questions) and `ASSETS_NEEDED.md` (where assets landed; ✅/🔁/❌).
5. The approved samples in `compositions/s01…s11` — copy their structure and effect calls. `lib/fx.js` is the
   effect library (use it; add new helpers only if truly needed, and then ALSO document them in MANUAL.md §5).
6. Look at `references/style-images/*` and `references/reels/*.jpg` for the look you're matching.

## Deliverables
- `compositions/segNN.html` — one templated sub-composition; root:
  `<div id="root" data-composition-id="segNN" data-vo-start="SEG_START" data-duration="DURATION" data-width="1920" data-height="1080">`
  Scenes inside are absolutely-positioned layers shown/hidden by the one timeline (see SEGMENTS.md §3).
  Prefix ids `segNN-scNNN-…`. Cue everything with `T(vo_seconds)`.
- `<audio id="segNN-vo" class="temp-vo" src="vo10.mp3" data-start="0" data-duration="DURATION" data-media-start="SEG_START" data-volume="1">` for your own previews (the assembler strips it).
- `compositions/segNN.sfx.json` — per-object SFX markers (SEGMENTS.md §3.4).
- A short `compositions/segNN.NOTES.md`: what you built, deviations from EDIT_NOTES and why, assets missing/substituted.

## How to work
- Make a private sandbox: `tools/make_sandbox.sh segNN`, then preview ONLY there:
  `cd work/segNN && python3 tools/build_index.py segNN --root . && npx hyperframes lint && npx hyperframes snapshot --at … --no-end -o .snap/x`
  Never write `index.html` in the project root (other editors work in parallel).
- Build scene by scene. After each 2–3 scenes, snapshot their key moments and LOOK at the PNGs. Fix layout, overlap,
  readability, cropping, timing before moving on. Check at least the start+0.3 s and middle of every scene.
- Run `python3 tools/sync_audit.py compositions/segNN.html` — on-screen words land 0–120 ms before their spoken word.
- Performance: gate per-frame `FX.onFrame` work to its scene window; prefer ≤2560 px images; reuse one streak canvas.
- Missing asset (❌): pick the closest existing asset or make a typographic/graphic treatment; never leave blanks.
  Don't download new media unless it's essential and quick (free/PD/CC only, log it in SOURCES.md).
- Text = exactly what the narrator says (no fact-checking); only ASR name spellings are corrected (BEATS.md §2).
- Keep text minimal: key words only, one text animation at a time, always readable (contrast, size ≥ 22 px labels).
- Finish with `npx hyperframes lint` = 0 errors in your sandbox, sync_audit clean, notes written. Then report:
  scenes built, effects used, any open issues.
