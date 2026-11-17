# nvs07 — NOTES (master 647.042–775.250, DUR 128.208, 15 scenes)

Plan with exact cues: `project/nvidia/EDIT_NOTES_nvs07.md`. Checks: lint 0 errors for nvs07 (the 25 lint errors are other projects'
missing face-cam files); `sync_audit` 0 flagged (all text cues −0.06 s); `tl.duration()` = 128.208 (headless dump, no runtime errors).

## Scenes
| id | master | picture | ref / effect |
|---|---|---|---|
| sc001 | 647.04–653.30 | Pacific satdesat map: US (ice) → 8 volt chip routes cross the Pacific, camera rides the lead dot, lands on CHINA (red fill) | map routes, counter-scaled labels UNITED STATES / PACIFIC OCEAN / CHINA |
| sc002 | 653.30–657.90 | airport baggage carousel footage | footage plate, focus hunt |
| sc003 | 657.90–662.53 | Beijing Capital Airport arrival hall + place tag | photo plate + fringe |
| sc004 | 662.53–668.21 | three neutral listing cards (OUR design, not Facebook's UI; names/prices blurred), facebook "f" logo + "Marketplace" typed | paper, stop-motion cards |
| sc005 | 668.21–683.65 | FC M → C (673.49) → W (678.93) — the "video bombs" joke | face cam, clean |
| sc006 | 683.65–696.29 | isotype (R5): one traveller → ice ban mark on "illegal" → pull back, crowd of ~200 builds at 12 fps → one ice officer | paper isotype |
| sc007 | 696.29–707.33 | FC M → W exactly on the 702.03 join | face cam |
| sc008 | 707.33–710.93 | real BIS rule (Federal Register 13 Oct 2022) tilts in, push, highlighter on "Interim final rule" (body text) — "a very new law" | document, highlighter |
| sc009 | 710.93–713.97 | FC C | face cam |
| sc010 | 713.97–728.82 | travel flat-lay (ref `ast_acc78b28b2d84747`): boarding pass (generic prop), US polaroid (RTX 4090) $2,000 tag, CHINA polaroid (Huaqiangbei 2024) $2,300 → $2,500 (yellow), string, pen arrow to the ticket | paper (graph), polaroids, counter, pen |
| sc011 | 728.82–734.58 | FC M | face cam |
| sc012 | 734.58–744.02 | spotlit dark desk with polaroids (ref `ast_e8562eb310434ee1`): iPhone line-up (orig/3G/iPhone 4), iPhone 4 hero + US flag sticker, overseas polaroid (Shenzhen airport) + plane sticker, "×2" yellow halate | night, light-flash whip in |
| sc013 | 744.02–756.92 | FC C → W (748.90) → M (753.14), ends on the 756.92 join | face cam |
| sc014 | 756.92–761.14 | Herbert C. Hoover Building + tag U.S. DEPARTMENT OF COMMERCE · WASHINGTON | photo plate |
| sc015 | 761.14–775.25 | ice "ENFORCEMENT RESOURCES" bar splits into slivers onto 30 travellers; push to one, "$300" (yellow); pan to a ghost pallet of 8-GPU servers, pen cross ("not a dedicated smuggling operation"), push in → nvs08 | paper chart, pen cross |

First scene: fresh map shot at 647.042. Last: push into the crossed-out server pallets (cut on action into nvs08's "big fish").
Face cam: 15.44 + 11.04 + 3.04 + 5.76 + 12.90 = 48.2 s of 128.2 s = **37.6 %** (≈40 % target; "From the government's point of view"
went to the Commerce building rather than Sam). All joins (647.17, 691.42, 694.38, 741.67, 762.48, 771.58, 775.18) fall in B-roll; 702.03 =
framing change; 756.92 = FC ends. Framing origin 955px 60px (head not cropped at C 1.5).

## Text on screen (no narration captions)
Map labels; place/building tags; listing UI ("Graphics card", "Marketplace"); document text; flat-lay labels US / CHINA + spoken prices
$2,000 / $2,300 / $2,500; "×2" (he says "double"); chart label ENFORCEMENT RESOURCES; "$300". Yellow = one key number per scene.

## Assets used
shared: places/airport_baggage_hall_beijing, airport_baggage_hall_shenzhen, commerce_hoover_building_1, huaqiangbei_street_2024_1;
hardware/rtx4090_fe_box_1, rtx_3090_vs_4090_cards, iphone_original_2007_1; footage/airport_baggage_carousel, gpu_rtx4090_gigabyte_in_hand
(still); logos/facebook.svg, flag_us.svg; docs/bis_rule_2022-10-07_p1.png; icons person/suitcase/ban/server_8gpu/plane (inlined);
maps/kit pacific_satdesat + overlay. Own derived files: `assets/nvidia/nvs07/derived/` (SOURCES.md), generator
`project/nvidia/gen/nvs07_assets.py`.

## Deviations / substitutions
- Facebook Marketplace: no real listing (login wall, RESEARCH §9 UNVERIFIED) → neutral listing cards in our own type, facebook logo +
  "Marketplace" typed (lead's instruction). Prices on the cards are blurred (Sam gives none at that moment).
- Lead plan's "+$300" in sc006/flat-lay dropped: Sam doesn't say it there; the $300 appears only when he says "300 bucks" (770.56).
- Lead's sc005 (696–714 FC) gets a 3.6 s B-roll insert (the real BIS rule) on "this is a law… a very new law" for pacing.
- China polaroid uses a Huaqiangbei street photo (no free photo of GPU stalls exists — shared/places note).

## Gotchas for MANUAL
- A Pacific-wide route (US → China, 5,000+ px) leaves the camera ahead of its dots if both are eased separately: drive the camera from
  the LEAD dot's eased progress (one `u` tween, every dot and the camera computed in its `onUpdate`) so the dots stay in frame.
- Never name a class `hl` (again): a `.hl` boarding-pass label got fx.css's yellow highlighter.
- A dark ink price tag disappears on a dark desk — on night grounds use the halate yellow number instead.
- Pans across a paper chart: put the paper layers INSIDE the camera world (two mirrored `_hires` tiles) so the texture moves with it.

## QA fixes (lead review, 2026-11-17)
- sc008: BIS 2022 p1 → docs/bis_rule_2023-10-17_p1.png (also an interim final rule; reuse limit); highlight re-measured onto that page's own "Interim final rule" (pdftotext 78–149 × 245–254 pt → left 124 top 397 w 124); credit = Federal Register 88 FR 73458, 25 Oct 2023.
