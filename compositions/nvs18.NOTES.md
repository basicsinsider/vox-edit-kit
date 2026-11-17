# nvs18 — NOTES (master 1822.167–1893.917, 71.750 s; no face cam)

## Wafer chart geometry, handed to nvs19 (reuse exactly)
- Ground: `--night` #0d1012 with the usual hall gradient (`radial-gradient(ellipse 72% 62% at 50% 46%, mix(ash-dark 52 %, night) → night 74 %)`).
- Wafer disc: SVG in the 1920×1080 frame, **centre (960, 560), radius 448**; fill radial gradient #2c3438 (at 42 %/38 %) → #181d20;
  rim stroke #c3c7c8 (= `--ash-light`), 4 px, opacity 0.75; notch at the bottom: V from (944, 1007) to (960, 990) to (976, 1007).
- Dies: **10 × 10**, die **54 px** square (rx 4), pitch **62 px** (gap 8); grid 612 px wide → top-left die at **(654, 254)**,
  die (col c, row r) at x = 654 + 62c, y = 254 + 62r. All 100 dies sit inside the disc (corner 438 px from centre).
- Colours: **working = `--volt` #86c232**, stroke `--volt-light` #c9ec8f 2 px, `drop-shadow(0 0 7px rgba(134,194,50,0.6))`;
  **failed = dark graphite #3a4247**, stroke #2a3034 2 px, no glow; untested (only before the test sweep) = #1c2225 with a dashed
  #6b7378 outline (6 4).
- Text: title "YIELD" (Haskoy 800, 128 px, `.clean`, left 96 / top 96); counter "100 CHIPS" (Haskoy 64 px, left 96 / top 262);
  legend at left 1490: 44 px squares at top 420 (GOOD) / 500 (FAILED), `t-label` 28 px.
- My final state: a mixed pattern (seeded rng 1818, edge dies fail more often; 61 good) — illustrative only, NO number is shown
  (Sam gives none here). nvs19 sets its own 10 % / 30 % / 99 % states on the same grid.

## What I built (plan + cues: `project/nvidia/EDIT_NOTES_nvs18.md`)
13 scenes; face cam 0 % (part 2 audio only). First scene: paper Lutnick + quote card (fresh shot; continues nvs17's quote).
Last scene: the wafer chart with a slow camera drift running to 1893.917 (nvs19 opens on its Texas map).
- sc001 Lutnick + real quote card (highlighter) · sc002 Lutnick on a modern TV + broadcast rings · sc003 quote card flies to Xi
  (Vox layered) · sc004 China night map: border becomes a wall, volt chip cards bounce off at Hong Kong, NVIDIA H200 lifts ·
  **sc005 HERO 600,000** (ref `ast_db095fac62b54549`): yellow odometer numerals rise BEHIND the real Kwai Tsing cranes (sky keyed
  from the photo, cranes/hills in front), label HONG KONG · sc006 crates | CCP flag + barrier arm drops | Chinese buyers' logos,
  red lock + marker circle, crates stop at the barrier · sc007 night port + red pen "?" · sc008 US/China race lanes + the chips
  China won't take (dashed pen arrow) · sc009 fab footage · sc010 Huawei layered panels + logo card + red arrow up · sc011 VOLUME
  isotype (order tickets pile up beside a factory) · sc012 real wafer pull-back, YIELD · sc013 wafer chart (match dissolve).
- Effects: Vox layered ×3, highlighter, radio waves, map with fill/wall/routes + constant-size labels, odometer, sky-key
  integration, isotype, pen/marker markups (circle, ?, arrows), race bars, footage plate + focus hunt ×2, match dissolve.
  Transitions: whip, slide, hard cut on push, flash whip, slide, vertical whip, hard cut, whip, slide, hard cut, flash whip,
  dissolve — never the same twice in a row. Grounds: paper/night alternate, never > 2 in a row.
- Reference ids: `ast_db095fac62b54549` (sc005). References/style: Vox layered #10, isotype R5.

## Assets
- Shared: people/lutnick_cut.png, xi_cut.png, xi_symposium_2025.jpg; footage/lutnick_speaking_oval_office_2025_a.mp4,
  fab_wafer_lithography_st.mp4, fab_chip_assembly_st.mp4; places/huawei_hq_bantian_1.jpg, huawei_store_1.jpg (1920 copies);
  hardware/wafer_300mm_dies.jpg; logos huawei, flag_china, flag_us, alibaba_wordmark, bytedance, tencent_wordmark, baidu;
  icons chip, lock, factory; maps/kit china_night + overlay.
- Own (`assets/nvidia/nvs18/`, SOURCES.md, 8 MB): 3 Kwai Tsing photos (Commons CC BY 4.0 / CC BY-SA 3.0 / 4.0), derived sky-keyed
  crane foreground, China map crop + outlines, Huawei 1920 copies. Generator: `project/nvidia/gen/nvs18_assets.py`;
  composition generator: `project/nvidia/gen/nvs18_template.html` + `build_nvs18.py` (edit the template, re-run the build).

## Deviations / decisions
- sc001 drops the Xi/Zhongnanhai plate of the lead plan: "even if that was the plan" stays on Lutnick + his quote (the plan);
  Xi comes in sc003 with "Chinese government", where the card slides to the China side as planned.
- The 600,000 port is labelled HONG KONG and the chip NVIDIA H200 (RESEARCH §20: Reuters 5 Nov 2026, ~600,000 H200 held in Hong
  Kong; "the most powerful chip NVIDIA is allowed to sell" = H200). Sam says only "a port" — remove the labels if the lead disagrees.
- No "customs gate closed in red" on the photo itself: the closing barrier is its own diagram scene (sc006) so the hero stays clean.
- Lutnick TV footage is the Oval Office swearing-in (the only Lutnick footage); no fake chyron / "LIVE" bug.
- Order tickets carry lines + a barcode only (no invented text).

## Checks
- lint (0.8.217, sandbox `work/nvs18`): 0 errors for nvs18 (warnings only: nested media data-start, file size, z-index −1 inside the
  highlighter span which has its own stacking context — verified visible in snapshots).
- `sync_audit.py compositions/nvs18.html --transcript transcript_nv.json`: 8 text cues, all −0.06 s, 0 flagged.
- Headless timeline dump: `tl.duration()` = 71.75 (= DUR), 0 runtime errors over a full 0.25 s seek; the only tweens ending
  < 0.5 s before a cut are camera drifts (hold rule OK).
- Snapshots: every scene start/middle/end + every cut at ±0.05 s looked at; no black frames.
- SFX: `compositions/nvs18.sfx.json` (46 markers, vocabulary types only).

## Gotchas (for MANUAL)
- Sky-key integration for "numbers behind architecture": key the sky out of the same photo (bright + low saturation + connected to
  the top row, `nvs18_assets.py cranes_fg`) and stack photo → numerals (multiply) → keyed photo; give the numerals their own slow
  scale so they parallax against the plate.
- `FX.whip(..., {vertical:true})` with the default dist 700 leaves a dark band for a frame — pass `dist ≈ 120` for vertical whips.
