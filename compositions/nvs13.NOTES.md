# nvs13 — NOTES (master 1260.375–1356.292, 95.917 s; no face cam)

Built 13 scenes (plan + exact cues: `project/nvidia/EDIT_NOTES_nvs13.md`). Face cam 0 % (part 2, audio only). A new shot or a clear
development every ≈ 2–5 s. First scene: fresh night shot of the real NIST page, cut on action from nvs12's push on the test sheets.
Last scene: accelerating push on the scores/chips chart → cut on action into nvs14 ("Well, this is where we get into the factors…").

- "The US government ran its own tests" = the real NIST CAISI page **"CAISI Evaluation of DeepSeek V4 Pro" (1 May 2026)** (RESEARCH §15),
  captured to `assets/nvidia/nvs13/` (PD). The shared `docs/nist_caisi_*` / `news/s10_nist_news` are the older Sept 2025 report, so not
  used for "recently". Real page shown twice (sc001 date highlight; sc008 KEY FINDINGS contrast call-out + 2 highlighter strokes).
- Two NIST figures REBUILT in our style with the report's own values (credit "Data: NIST CAISI, May 2026"): sc003 Fig 1 capability
  chart (US/China dots + trends, DeepSeek V4 Pro measured 800 vs "SELF-REPORTED" ghost ≈ Opus 4.6/GPT-5.4 level, per the page's key
  finding); sc005 Fig 3 paired bars, DeepSeek V4 Pro vs Claude Opus 4.6 on NON-PUBLIC (ARC-AGI-2, PortBench, CTF-Archive-Diamond) vs
  PUBLIC (HLE, SWE-bench Verified, Terminal Bench 2.0; = benchmarks reported by DeepSeek) — gaps bracketed. Sam says no numbers here
  except "5 %", so no numbers are printed on these charts.
- Other scenes: sealed test folder (Commerce seal, face-down sheets, ice lock); nvs12's red MODEL stencil callback that no longer fits
  the shuffled questions; ink balance with the U.S. TEST card vs a "?" card; blueprint "built to show" (T-square, dimension line pulled
  wider); ink caveat asterisks; Pacific night map US (ice) vs China (red) with a volt chip route; two generic video thumbnails (flags +
  lab logos + arrows, no titles, no real UI); a wall of one-sided thumbnails → pull back to the "big picture" evidence board; rewind into
  the question chart (scores ≈ equal, China column drops to where it "should" be, chips as area-true squares, 5 % = side √0.05, yellow
  5% the one glow).
- References: no inspo ids were assigned to nvs13; lead plan rows 001–005 followed (document #5, paired bars, balance, thumbnail wall +
  camera pull, question chart + "?" markup #19). Deviation: lead row 004's thumbnail wall is split into sc011 (two thumbnails, one per
  "would be easy") + sc012 (wall → board); row 003 split into balance (sc006) + blueprint (sc007); "chip war" line got a map (sc010).
- Effects: real document reveal + highlighter, contrast call-out, chart rebuilds (dot pops / dashed trends / bars at 12 fps), pen arrow,
  brackets, balance physics, blueprint draw-on, stop-motion stamps, night map fills + route + constant-size labels, collage board +
  long camera pull, focus hunts, rewind (scanlines + 12 fps smear), area squares + count. Transitions: cut-on-action, whip →, flash whip
  ↓, cut, slide ←, vertical whip ↑, cut, flash whip ←, cut, whip →, cut, slide ↑, rewind (never the same twice in a row).
- Grounds: N N P N P P B(lueprint) N P N N P N (≤ 3 in a row).
- Shared assets used: logos commerce_dept_seal, flag_us, flag_china, openai, anthropic, google_deepmind, deepseek, alibaba, youtube;
  icons lock, chip; textures (paper graph/cream/stained/fiber/blueprint, newsprint). Map: kit `world_night` + `world_overlay` (derived
  crop). Own: `assets/nvidia/nvs13/` (+ SOURCES.md, 2.3 MB), generator `project/nvidia/gen/nvs13_assets.py`.

Checks
- Lint (sandbox `work/nvs13`): 0 errors for compositions/nvs13.html (warnings only: duplicate_media_discovery_risk — the NIST page img is
  used in sc001 and sc008 — and composition_file_too_large). The 25 lint errors in the run belong to other compositions.
- `sync_audit`: "0 cue(s) flagged" (all 15 text cues at −0.06 s).
- Timeline dump (headless, local gsap): `tl.duration()` = 95.917 = DUR; full seek 0 → end, no runtime errors; hold audit: every key
  animation ends ≥ 0.5 s before its cut (remaining hits are camera pushes/cut-on-action moves and transitions).
- Snapshots: every scene at start/middle/end + every cut at −0.05/+0.05 s, looked at; no black/empty frame at any boundary.
- SFX: `compositions/nvs13.sfx.json` (60 markers, all types in place_sound's vocabulary).

For the lead / MANUAL
- `tools/make_sandbox.sh` must be run with zsh (`zsh tools/make_sandbox.sh nvs13`); run with bash, `${0:A:h}` expands to "" and it
  creates `/work/<seg>` with dangling symlinks at the filesystem root (happened here: `/work/nvs13` — harmless, removal was blocked by
  a safety check, please delete it).
- A label placed with gsap x/y each frame (constant-size map labels) must not also get `rise()` (it tweens y → overrides the placement).
- `filter: brightness(0)` turns the YouTube mark into a black blob (the white play triangle goes too): use `grayscale(1) contrast(1.25)`.
