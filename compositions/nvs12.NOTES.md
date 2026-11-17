# nvs12 — NOTES (master 1174.583–1260.375, 85.792 s; no face cam)

Built 10 scenes (plan + exact cues: `project/nvidia/EDIT_NOTES_nvs12.md`). Face cam 0 % (part 2 audio only).
- First scene: paper title card THE LEAD + three numbered tabs (fresh shot). Last scene: five identical test sheets, camera
  push accelerating from 1259.95 → cut on action into nvs13.
- Three measures = three chart designs: CHIPS isotype grid (night, 20 volt chips vs 1 + empty slots, 20× counted, the one glow),
  TESTS dual line chart with ice area + China red line, brackets 30 POINTS → 3 POINTS (paper graph, ref `ast_d3d145bc2ebb47ad`),
  TIME month ruler (paper lined) + three-lane 7-month gap chart (night). Plus a paired-bar chart (test score vs chips) for
  "close without enough chips".
- References: `ast_d3d145bc2ebb47ad` (sc003), `ast_e1ede4fafbd84a66` title-card family (sc001, sc008 callback).
- Effects: isotype, count, line/area draw-on, camera moves + focus hunt, pen circle/arrow markups, contrast by dimming,
  highlighter band, stencil metaphor, logo row, whips (plain, vertical, light-flash), slides, hard cuts on action.
- Shared assets: icons/chip.svg; logos deepseek, alibaba, bytedance, baidu, tencent_wordmark, openai, anthropic,
  google_deepmind, flag_china (credit "Logos © their owners, fair use"); textures only otherwise. No own downloads.

Deviations from the lead plan
- sc001 title text is "THE LEAD" (Sam says "track the lead"; "AI" is not spoken there). Tabs show icons, not words, until the
  sc008 recap (CHIPS / TESTING SCORES / TIME as chart labels; TESTING SCORES on its words).
- Added sc004 (paired bars) for 1208–1215 and sc007 (Chinese company logos) for "Chinese companies" before the tab-2 spotlight.
- 7–8 MONTHS / three-years beat split into two scenes; cut moved 1227.58 → 1228.00 and 1187.95 → 1188.15 so key animations hold ≥ 0.5 s.
- No years on the test chart / lanes (Sam gives none; RESEARCH: AI Index HumanEval 31.6 → 3.7, Epoch 7-month average). No source lines.
- "20×" shown unlabeled (RESEARCH: unverified as stated).

Checks: lint 0 errors for nvs12 (only the generic composition_file_too_large warning); `sync_audit` 0 cues flagged (all −0.06 s);
timeline dump `tl.duration()` = 85.792, 0 runtime errors over a full seek. SFX: `compositions/nvs12.sfx.json` (48 markers).

Gotchas (for MANUAL): the paper_lined_01_hires texture has a white punch hole at the left edge (~x 50, y 560) — offset the layer
(`left:-200px`) when anything sits near the left edge. Logos as bone/ink silhouettes: `filter: brightness(0) invert(0.94)` /
`brightness(0)` on the shared SVGs works; kit icons in colour via CSS mask-image on a coloured div (img currentColor = black).
