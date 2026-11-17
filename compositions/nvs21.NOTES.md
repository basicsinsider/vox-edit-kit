# nvs21 — NOTES (master 2103.000–2182.542, 79.542 s, 8 scenes) — plan: `project/nvidia/EDIT_NOTES_nvs21.md`

## Built
| sc | master | picture | ground / effect | in |
|---|---|---|---|---|
| sc001 | 2103.00–2108.79 | the fact just told (nvs20: Beijing pushes the orders to Huawei): Vox layered background — Huawei Atlas 900 SuperPoD (front, Huawei mark) over Huawei HQ Bantian (back), panels drifting at their own speeds; on "questions" four bone pen question marks scribble on | night, layered bg #10, pen markups | fresh shot (nvs20 ends on a lined-paper sketch, so this opens on night photos) |
| sc002 | 2108.79–2117.99 | puzzle diagram: red CCP barrier rises; CHINESE AI COMPANIES node (DeepSeek / Alibaba / ByteDance marks); NVIDIA H100 → volt arrow stops at the barrier, crossed out; Huawei → thin line stalls half way, "…" and dims; the node glows on "that the Chinese companies want" | night diagram, 12 fps | whip |
| sc003 | 2117.99–2123.43 | bar chart "AI models": AMERICAN (ice, OpenAI / Anthropic / DeepMind marks) vs CHINESE (red, DeepSeek / Alibaba / ByteDance) nearly level; ink pen bracket on the gap on "close", pen "?" on the question | paper ×2, bars 12 fps (style-images #6 structure) | slide ↑ |
| sc004 | 2123.43–2143.70 | THE SCOREBOARD (`NV.scoreboard`, state 1 ✗ / 2 ✓): close on the empty dashed row 4 (slot lights on "fourth"); pull out to the whole board on "scorecard"; rows 1/2/4 dim on "level three"; `markRow(3,"x")` T(2138.84) on "don't"; holds 4.9 s | motif; camera on a wrapper (results column kept out of frame in the close-up, so no cut-off labels) | light-flash whip |
| sc005 | 2143.70–2146.98 | Howard Lutnick at the Oval Office podium (White House footage, PD), name tag HOWARD LUTNICK / COMMERCE SECRETARY | footage, slow push | hard cut on the board drift |
| sc006 | 2146.98–2149.62 | LEVEL FOUR card — nvs05 sc001's JOB card copied (volt band, ice brush ring, ink bar, bone Haskoy 200 px, tape); bar widened to 1420 px for "LEVEL FOUR" | paper card (ref `ast_e1ede4fafbd84a66`) | slide ← |
| sc007 | 2149.62–2158.02 | SCOREBOARD (rows 1–3 stamped): `fillRow4("The renting loophole", T(2150.12))` on "loophole" — result tile empty; ice-light marker ring round row 4 on "big loophole"; small push (≤ 1.067) on "kept it till the end" | motif | whip ← |
| sc008 | 2158.02–2182.542 | US-West night relief map: volt DATA CENTER pops beside the COMPANY pin (SF Bay), slides into the Nevada desert as a fibre line stretches; pull back, five more data centers pop in empty land; population rings round the company; data pulses on the fibre; on "stretch… really far away" a second data center flies west across the Pacific and off frame toward Asia, line stretching behind it, camera pulling out/panning west; pulses still running at the cut | night map (derived plate + us_night detail layer), counter-scaled icons/labels, radio waves, one driver tween | hard cut on the board push |

- No face cam (part 2 audio only). Developments every 2–6 s throughout.
- First scene: night layered photos (fresh shot). Last scene: the Pacific map, camera still pulling out and data pulses running along the
  stretched line toward Asia → cut on action into nvs22's Malaysia map.
- Reference ids: `ast_e1ede4fafbd84a66` (via the nvs05 card). Motif: SCOREBOARD ×2 (two instances `nvs21-sba`, `nvs21-sbb`).
- On-screen text: only labels (CCP, CHINESE AI COMPANIES, AMERICAN / CHINESE / AI MODELS, DATA CENTER, COMPANY), the name tag, the LEVEL
  FOUR card and motif text. No narration captions.

## Checks
- lint (sandbox `work/nvs21`): 0 errors in nvs21 (the 25 errors are other projects' missing face-cam files); nvs21 warnings only
  `nested_media_start_basis_ambiguous` (video data-start is composition-local), `duplicate_media_discovery_risk` (the same logo in two
  scenes), file length.
- `sync_audit … --transcript transcript_nv.json`: 16 cues, 0 flagged (all −0.06 s, two read +0.02 against the short neighbour word).
- Headless timeline dump: `tl.duration()` = 79.5417 = DUR, no runtime errors, no tween past DUR.
- Snapshots looked at: every scene start/middle/end and every cut at ±0.05 s; key animations hold ≥ 0.5 s before each cut (sc003's
  "models" label finishes 0.32 s before the whip starts — it is a label on its word, the scene's key moves end 1.7 s earlier).

## Assets
- New (derived, `assets/nvidia/nvs21/`, 3.7 MB, SOURCES.md): Pacific night plate from world_night + US-West detail crop of us_night
  (`project/nvidia/gen/nvs21_assets.py`).
- Shared used: huawei_atlas900_superpod_1, huawei_hq_bantian_1, h100_sxm_cutout, lutnick_speaking_oval_office_2025_a (0.5–4.0 s), logos
  (huawei, huawei_wordmark, nvidia_wordmark, deepseek, alibaba, bytedance, openai, anthropic, google_deepmind), icons/datacenter.
- Nothing missing or substituted. The data-center positions on the map are illustrative (no real sites named or labelled).

## For the lead / MANUAL
- Map scenes with many moving parts: drive everything (camera, counter-scaled labels, moving icons, stretching lines, pulses) from ONE
  proxy tween's `onUpdate` that computes the frame analytically from time — seek-safe, no ordering issues between tweens.
- Full-board scoreboard: any camera scale above ≈ 1.02 pushes the result labels past the 96 px margin; for a close-up keep the result
  column completely out of frame (cx = 1400 − 960/s) instead of cutting "NOT WORKING" mid-word.
- A whole-Pacific plate needs the world crop stitched across the antimeridian; kit world_night and us_night match in tone, so a us_night
  layer can sit on top as a detail layer for close-ups (mask-feathered edges).
