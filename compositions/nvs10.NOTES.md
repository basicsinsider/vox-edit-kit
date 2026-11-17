# nvs10 — NOTES (master 935.000–1046.000, DUR 111.000, 2664 frames)

Plan: `project/nvidia/EDIT_NOTES_nvs10.md` (12 scenes). No face cam (audio-only part 2) → 0 % on camera; edited visuals throughout,
a new shot or clear development every 2–5 s.

## Scenes (ground · effect · ref)
| id | master | picture | transition in |
|---|---|---|---|
| sc001 | 935.00–952.80 | grid-paper collage: H100 polaroid, pages, wire-globe network, pages feed the chip, calendar JAN→JUN, yellow sticky TRAINING (ref `ast_c5efacef3dbd4abf`) | first shot (fresh) |
| sc002 | 952.80–964.06 | night isotype: 1 chip → ~780 chips ring by ring, links, CLUSTER box, dive into the centre chip | whip → |
| sc003 | 964.06–971.26 | blueprint: GB300 NVL72 render panel + schematic lines (tag NVIDIA GB300 NVL72), then NVL72 rack cut-out vs home fridge with dimension brackets, REFRIGERATOR (ref `ast_b79f39f3b42f48f8`) | hard cut on action (dive) |
| sc004 | 971.26–977.18 | blueprint seesaw: rack tips it, 3,000 LB counts (yellow), small car (VW up!) levels it | whip ← |
| sc005 | 977.18–985.50 | paper isotype R5: rack → power cable → 10×10 houses light up (ice), 100 HOMES (yellow highlight), US tract-housing photo on "United States" | paper slide ← |
| sc006 | 985.50–994.46 | grid paper + black card isometric data hall: heat lines, ice coolant pipes, pump; real Colossus hose photo, LIQUID COOLING / PLUMBING tags, substation + cooling-tower cards (ref `ast_91abea88b76c4b43`) | whip ↑ |
| sc007 | 994.46–998.90 | 2.5D dolly down the xAI Colossus hall (shared `layers_datacenter_aisle`, modest push z 0→95), tag xAI COLOSSUS · MEMPHIS | light-flash whip |
| sc008 | 998.90–1003.66 | blueprint floor plan: one rack highlighted, ~2,500 racks fill six halls at 12 fps while the camera pulls back from 7× | hard cut on action |
| sc009 | 1003.66–1014.65 | paper: graphics card drops into a suitcase, red route → CHINA, camera pulls back to 0.3× over a field of 1,920 rack icons | whip ← |
| sc010 | 1014.65–1023.61 | US night map push, Tennessee (ice), pin MEMPHIS, zoom-box Esri aerial of xAI Colossus, 800,000 HOMES (ref `ast_671f213364e14029`) | hard cut on action |
| sc011 | 1023.61–1035.45 | paper bars R6, serif title "Computing *power*": MEMPHIS DATA CENTER (volt) vs EVERYTHING CHINA HAS SMUGGLED (red pieces that combine), pen circle | paper slide ← |
| sc012 | 1035.45–1046.00 | night R5 grids: MEMPHIS 100 volt cells vs CHINA'S BIGGEST 7 red cells, 7% (yellow); camera still pushing at the end | light-flash whip |

First scene: fresh paper collage. Last scene: night grids with a running camera push (cut on action into nvs11's data-hall plate).
Grounds: paper, night, night, night, paper, paper, photo, night, paper, map, paper, night (never > 3 in a row). Transitions never repeat
back-to-back (whip / cut / whip / slide / whip↑ / flash whip / cut / whip / cut / slide / flash whip).

## Checks
- lint (0.8.217, sandbox): **0 errors in compositions/nvs10.html** (2 warnings: duplicate rack-cutout img in sc003+sc004; file length).
- `sync_audit.py compositions/nvs10.html --transcript transcript_nv.json`: 23 cues, all −0.06 s, **0 cue(s) flagged**.
- timeline dump (headless): `tl.duration()` = **111.000** = DUR; no key animation ends < 0.5 s before a cut (only transitions/camera).
  Two cuts were moved for the hold rule: sc001→sc002 952.54 → 952.80 ("It sounds"), sc004→sc005 976.54 → 977.18 ("that rack").
- Snapshots of every scene (start, middle, end) looked at; fixed: calendar position, seesaw (pans → plank), label overlaps,
  "xAI" casing (t-label uppercases — `text-transform:none`), CHINA box showing before its word, chart margins.

## Assets
Shared: hardware/cutouts/h100_sxm_cutout, gb200_nvl72_rack_front_cutout (×2: sc003, sc004), refrigerator_cutout, rtx4090_fe_cutout;
hardware/gb300_nvl72_rack_render_2, car_vw_up_side, liquid_cooling_hoses_closeup, cooling_towers_2; places/substation_750kv,
suburban_tract_cincinnati_aerial, layers_datacenter_aisle/*; icons chip/server_rack/house/suitcase/power_bolt (inlined as symbols);
maps/kit us_night + us_overlay + aerial_memphis_xai_colossus_z16 (pins from its json). Derived (own): `assets/nvidia/nvs10/derived/`
(US crop + overlay + Tennessee fill + Colossus inset), made by `project/nvidia/gen/nvs10_assets.py`, logged in `assets/nvidia/nvs10/SOURCES.md`.
Credits on screen for every CC BY / BY-SA and press image.

## Deviations / for the lead
- The 3,000 lb comparisons use the GB200 NVL72 rack cut-out (only cut-out available); the product NAME shown is only on the GB300 NVL72
  render (RESEARCH §11). The two never share a frame.
- sc008 has no text (a "thousands" counter would invent a number). sc011/sc012 figures carry no source line (UNVERIFIED, DECISIONS 1).
- Memphis aerial = Colossus 1 (pins json); 800,000 homes per RESEARCH fits Colossus 2 — the on-screen tag says only "xAI COLOSSUS".
- Shared footage (dc_cooling_*) not used: `shared/footage` has no SOURCES.md yet, so no credit could be checked.
- sfx types are from place_sound's vocabulary; sc006's hero is `air_swell` (a water gurgle would fit better if the sound designer has one).
- Gotcha for MANUAL: `t-label` uppercases everything — brand names with lowercase letters (xAI) need `text-transform:none`.

## QA fixes (lead review, 2026-11-17)
- nvs10.sfx.json: marker 1005.40 type `drop` (unknown to place_sound.py) → `paper_slide` (its note contains "drop" → photo_drop sound).
