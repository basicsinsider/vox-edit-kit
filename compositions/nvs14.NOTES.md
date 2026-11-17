# nvs14 — NOTES (master 1356.292–1445.542, 89.250 s; no face cam)

Built 12 scenes (plan + exact cues: `project/nvidia/EDIT_NOTES_nvs14.md`). Face cam 0 % (part 2, audio only). A new shot or a clear
development every 2–5 s. Grounds P N N P N N P N P N P P.
- First scene: fresh shot — three face-down cards slide onto a desk (the "factors"), taped shut on "don't want to talk about publicly".
  Last scene: the Epoch chart; red circle on "suspicious", holds 2.3 s, then an ease-in push from 1444.95 → cut on action into nvs15.
- Scenes: sealed cards → airport X-ray (GPU cards in a suitcase, on "smuggling") → waterline chart (CHINESE COMPANIES 1/20 vs AMERICAN
  COMPANIES; pull-back reveals the deep part + "?"; pen strike on the second "one twentieth") → podium with mics, empty speech bubble,
  hidden GPU card circled → ID-card board of Chinese AI companies + REVENUE + US card with strings (ref `ast_716e2cc68e364ca5`) →
  Pacific night map: US fills + consumer dots, pull-back, China fills, three routes China → US with packets → H100 print taped over,
  tape peels on "smuggled chips" → DeepSeek tile + radio rings, name tag "DeepSeek-R1 · Jan 2025" → REAL Sherwood News article
  (29 Jan 2025) with date box, highlighter on "the type and number of Nvidia GPUs DeepSeek used", outlined photo card + pen arrow
  (ref `ast_4b76d56ab5214313`) → chip stacks DEEPSEEK vs AMERICAN COMPANIES, dashed ghost stack + "?" above DeepSeek, ADMITTED bracket →
  desk callback (pen asterisk on "caveats", card 2 flips to a staircase on "another factor") → THE CHART.
- "This chart" (DECISIONS §4): Epoch AI's US-vs-China frontier staircase rebuilt on graph paper (ref `ast_d3d145bc2ebb47ad`: ruled
  title + source line), points read off Epoch's published chart (see `assets/nvidia/nvs14/SOURCES.md`); title "Top AI models, US vs
  China", source line "Data: Epoch AI · Epoch Capabilities Index (ECI) · CC BY", model labels GPT-4, o1, GPT-5, DeepSeek-R1, Qwen3 Max.
  Pen arrows from each US step to the Chinese step that follows (o1-mini→Qwen2.5-72B, o1→DeepSeek-R1, o3→R1 update, o3-pro→Qwen3,
  GPT-5→Qwen3 Max). No "copying" claim in our type (RESEARCH §16).
- Effects: stop-motion cards + tape, X-ray scan reveal, chart with camera pull-back, ink illustration + pen circle, pinned board +
  string draw, night map with constant-size labels + routes/packets, photo print + tape peel, radio-wave rings, real article +
  highlighter + outlined cut-out + arrow, isotype chip stacks with ghost stack, card flip, staircase line chart + pen arrows + circle.
  Transitions: push-cut, whip, slide ↑, vertical whip, cut on action, light-flash whip, cut on action, slide ←, whip ←, slide ↓, push-cut.
- Shared assets: icons gpu_card, chip; logos deepseek, alibaba, bytedance, baidu, tencent_wordmark, flag_us; hardware
  h100_sxm_board_2.jpg; news s11_sherwood_gpus.jpg (cropped); textures only otherwise. Own derived files: `assets/nvidia/nvs14/derived`
  (Pacific-centred night map 70°E–40°W + China/US masks, Sherwood crops) — no new downloads.

Deviations from the lead plan
- 001 split: sealed cards (1356–1361.7) + X-ray (smuggling) + waterline chart for the "one twentieth" line (the iceberg idea as a chart).
- 002/003: podium + board instead of "NO COMMENT" tape (no invented words on screen); the US map moved to the "US consumer market" line.
- 004: "ADMITTED vs ESTIMATED" became DEEPSEEK vs AMERICAN COMPANIES stacks with a dashed ghost stack + "?" (no numbers — Sam gives none);
  the DeepSeek-R1 name tag is factual (RESEARCH §16).
- No text on screen for the narration itself; all text = labels, chart text, name tag, real article, credits.

Checks: lint 0 errors for nvs14 (only the generic composition_file_too_large warning); `sync_audit` 0 cues flagged (all −0.06 s);
headless timeline dump `tl.duration()` = 89.25, 387 tweens, none past the end, 0 runtime errors over a full seek; every cut snapshotted
at −0.05/+0.05 s (no black frames). SFX: `compositions/nvs14.sfx.json` (47 markers, all types in place_sound's vocabulary).

Gotchas: GSAP `fromTo` with `immediateRender:true` on a yoyo blink (opacity 0.15 → 1) shows the element from frame 0 even after a
`gsap.set(opacity:0)` — use `immediateRender:false` for blinks. A map that must show both China and the whole US needs its own crop of
world_night (the kit Pacific base stops at 115°W; nvs11's crop stops at 67°W, where the US east coast sits on the edge).
