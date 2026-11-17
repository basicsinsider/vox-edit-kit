# nvs03 — NOTES (master 229.500–362.292, DUR 132.792, 18 scenes)
Plan: `project/nvidia/EDIT_NOTES_nvs03.md`. Source: `compositions/nvs03.html` is BUILT from `project/nvidia/gen/nvs03_template.html` by
`python3 project/nvidia/gen/build_nvs03.py` (inlines the shared icon paths + country silhouettes) — edit the template, then rebuild.
Derived map assets: `project/nvidia/gen/nvs03_assets.py` → `assets/nvidia/nvs03/derived/` (SOURCES.md there; 3.7 MB, no new downloads).

## Scenes
sc001 FACE M (whip-in landing) · sc002 balance scale (ref `ast_0659daaead12498d`, paper) · sc003 FACE W · sc004 FACE M (join 247.37) ·
sc005 shop-counter diagram (paper, icons, pen ✗) · sc006 FACE C (light-flash whip, join 261.22) · sc007 US→China country diagram (paper) ·
sc008 FACE W (join 271.20) · sc009 tilted China relief + Google/Facebook/YouTube stopped at the coast + 2009/2010 … 2022 strip (ref
`ast_d02865717c824c47`) · sc010 foreign company → CHINA box → partnership → trade secrets / technology handed over (paper collage) ·
sc011 FACE C · sc012 world night map: China → US → Germany/UK/France → global south → WTO at Geneva (camera path, counter-scaled labels) ·
sc013 FACE C · sc014 FACE W (join 319.62) · sc015 triptych: cooling tower | uranium pellets | Trinity (weave) → ENRICHED URANIUM + ice lock →
cutting-the-curve match cut to the NVIDIA AD102 die (AI CHIPS) → ✓ / ✗ · sc016 tilted Taiwan Strait satellite, China red, three red arrows,
Taiwan in ice-light (ref `ast_4f6fcd9750634ef3`, arrows instead of tanks) · sc017 FACE M · sc018 FACE C punch-in on "The main question".
Transitions vary: whip, hard cut, slide x, flash whip, slide y, vertical whip, curve cut. Grounds never > 3 in a row.

## Face cam: 45.6 s / 132.8 s = 34.3 %. Framings W 1.0 / M 1.25 / C 1.46, origin (1000, 100) (C at 1.52 cropped his hair when he leans).
Joins 247.37, 261.22, 271.20, 319.62 = framing changes; 270.82, 283.13, 307.47 inside B-roll; 229.53 (0.03 s into the segment): sc001 lands
from a whip smear for its first 4 frames so the take join is hidden. **Lead**: first scene = face cam landing from a whip smear (pairs with any
outgoing nvs02 shot); last scene = face cam C with a slow push, ends at 362.292 → nvs04 may hard-cut or whip.

## Text on screen (all labels, no narration captions)
UNITED STATES / CHINA (scale), CHINA + 2009 / 2010 / US CHIP BAN 2022 (map strip: years of the YouTube/Facebook 2009 and Google 2010 blocks
from RESEARCH §5), FOREIGN COMPANY / CHINA / PARTNERSHIP / CHINESE COMPANY / TRADE SECRETS / TECHNOLOGY (diagram), CHINA / UNITED STATES /
GERMANY / UK / FRANCE / GLOBAL SOUTH (map), ENRICHED URANIUM / AI CHIPS (object labels), CHINA / TAIWAN. No WTO case names (RESEARCH: the
"global south IP cases" are unverified → only the real WTO logo, no case label).

## Shared assets used
logos: flag_us, flag_china (greyscale medallions), google, facebook, youtube, wto · icons: person, chip, ban, lock, check, cross, factory ·
hardware: cooling_tower_1, mushroom_cloud_trinity_1945, uranium_pellets_1, gpu_die_ad102_closeup · maps kit: china_night, east_asia_satdesat,
world_night (cropped) + overlays · face cam master. Credits on screen for CC-BY(-SA) photos and map data.

## Checks
lint (0.8.217, sandbox): 0 errors for nvs03 (only the usual nested_media_start_basis warnings, as in pys02). sync_audit: 22 cues, 0 flagged
(all −0.06 s; three are matched to a neighbouring short word at +0.02). Timeline dump: tl.duration() = 132.792, 278 tweens, no JS errors.
Snapshots of every scene (start+0.3 / middle / last 0.5) looked at; fixes made: scale lowered 66 px + bigger chip, shop diagram re-centred and
enlarged, stained paper turned down (coffee rings), China map pulled out to show the whole country, year labels spaced, JV box re-centred and
docs side by side, US map framing kept inside the crop, stray off-frame labels faded, uranium crop on the pellets, label below the zoomed circle.

## Gotchas for MANUAL
- A camera key whose visible height exceeds the crop above/below shows a black band: check `cy − 540/s ≥ 0` and `cy + 540/s ≤ H` at every key
  (US framing at s 0.55 needed cy ≥ 982).
- Counter-scaled map labels stay rendered when the camera leaves them: a label half off-frame reads as a stray letter — fade earlier labels at
  each big camera move.
- Whip-in on the first frame of a segment hides an EDL take join that sits < 1 frame after the segment start.

## QA fixes (lead review, 2026-11-17)
- sc015 AI CHIPS circle: RTX 4090 gaming die (AD102) → A100 SXM4 data-center GPU die (hardware/a100_sxm4_board_1.jpg, scaled 2.2 on the die); credit adds "A100 data-center GPU: NVIDIA". Edited in the template, rebuilt with build_nvs03.py.
