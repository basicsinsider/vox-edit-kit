# nvs15 — NOTES (master 1445.542–1572.417, 126.875 s; no face cam)

Built 15 scenes (plan + exact cues: `project/nvidia/EDIT_NOTES_nvs15.md`). Face cam 0 % (part 2 audio only). Shots/developments every 2–5 s.
- First scene: fresh shot — lab-notebook collage (two photo cards drop on graph paper). Last scene: night line chart, camera push
  accelerating from 1571.97 → cut on action into nvs16.
- Scenes: sc001 flasks/DISTILLATION collage (ref `ast_c5efacef3dbd4abf`) · sc002 own neutral chat UI (grey bars, no readable text, no
  product branding) → push through the AI avatar · sc003 the model's neural network, pulses · sc004 vault + lock, leaks, red way-around,
  cat-and-mouse chase · sc005 ink padlock + red key / ice patch, pen loop arrows · sc006 isotype of 390 masked red accounts + yellow
  TENS OF THOUSANDS + request lines to an ice "new model" · sc007 blueprint tracing: red pen copies the network into THEIR MODEL ·
  sc008 bars HOW GOOD + TIME/MONEY columns · sc009 real headline on a torn strip (ref `ast_2b0b05b6a7bd471a`; The Hacker News 11 Sep
  2026, pen underline + circle) + the three labs' logos · sc010 four US lab plates jolt apart ("hate each other") · sc011 pen alliance
  diagram on lined paper: links, shield, red attack arrows, memo cards, one lab hit · sc012 Pacific night map: CHINA → red attack arc
  (camera pan) → three ice AI-company markers off the US west coast, hit + radio-wave rings · sc013 cork board: Anthropic / OpenAI /
  Google cards on their names, ice strings, travelling note, solution card, shared checks · sc014 flask callback: ice valve, red pen
  bypass, stopwatch, ice clamp · sc015 night line chart THE GAP (ref `ast_d3d145bc2ebb47ad` structure; night variant, nvs12 used the
  paper one): converge → narrow to LAST FEW MONTHS → gap opens, yellow bracket on "widening".
- Transitions: whip, push-through cut, vertical whip, slide-y, light-flash whip, hard cut, slide-x, whip, hard cut, vertical whip,
  light-flash whip, slide-y, whip, hard cut — never the same twice in a row. Grounds alternate (≤ 3 in a row).
- Effects: collage cards + tape, own UI, network diagram, isotype, pen markups (FX.markup.pen/arrow/circle), tracing, bars/columns at
  12 fps, real headline with markups, map with fills + arc + radio waves (FX.radioWaves), cork case board + strings, line chart with
  camera narrowing + focus hunt, whips/slides/flash.
- Shared assets: news/s12_thehackernews.jpg (the only real headline — story 12); logos anthropic, openai, google, xai; icons person,
  lock, question, check, datacenter; maps kit pacific_night (+ own fills); textures graph/cream/fiber/stained/lined/blueprint/cork/
  halftone. Own derived files: `assets/nvidia/nvs15/` (SOURCES.md; generator `project/nvidia/gen/nvs15_assets.py`). No downloads.

Deviations from the lead plan
- 002/003 split into chat (sc002) + network "brain" (sc003); 003 lock/key split into vault (sc004, night) + padlock loop (sc005, paper).
- 006 "logos apart" became the real headline (sc009) + rivals (sc010); 007 split into the pen alliance (sc011), the map (sc012, "if China
  … tell other companies") and the named cork board (sc013). Bloomberg's "OpenAI, Anthropic, Google unite…" headline is not in
  shared/news, so no headline for "working together" — diagrams instead.
- The shield in 008 became an ice valve + clamp on the sc001 tube (callback), plus a stopwatch for "quicker".
- 009: no years / numbers on the gap chart (Sam gives none; RESEARCH §17 marks "widening" UNVERIFIED) and no source line.
- sc007/sc011/sc012 cut points moved to 1495.05 / 1529.30 so "THEIR MODEL" and the "attacked" ring hold ≥ 0.5 s.
- Map: the three AI-company markers are generic (datacenter icons), placed off the US west coast with leaders to the Bay Area (all three
  labs are HQ'd there); "UNITED STATES" is a map label (not spoken). Sam's "these AI companies" are named only in sc013.

Checks: lint 0 errors for nvs15 (warnings: composition_file_too_large, duplicate_media_discovery_risk for the 3 masked copies of the
headline crop — plain `<img>`, not timed media); `sync_audit` 0 cues flagged (all −0.06 s); headless timeline dump `tl.duration()` =
126.875, 0 runtime errors over a full 0.25 s seek; every scene snapshotted (start+0.3 / middle / end−0.5) and every cut at ±0.05 s.
SFX: `compositions/nvs15.sfx.json` (82 markers, all types in place_sound's vocabulary).

Gotchas (for MANUAL): (1) `gsap.set(svgEl, {transformOrigin:"Xpx Ypx"})` AFTER a scale tween with immediateRender: GSAP's smoothOrigin
shifts the element (the sc006 model ring landed 800 px off) — set `svgOrigin:"X Y"` (user space) BEFORE any scale tween on SVG.
(2) A pop (`steps(2)`) that starts exactly at a whip/cut leaves the first frames of the new shot empty — set the first elements visible
at t − 0.02 or start entrances ~0.3 s before the cut (scene still hidden, so they land ready). (3) A shared scratchpad folder is used by
several agents: write snapshots/previews into your own sub-folder (another agent overwrote my map.jpg mid-check).
