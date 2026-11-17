# nvs11 — NOTES (editor, 2026-11-17)
Master 1046.000–1174.583 (DUR 128.583, 3086 frames). 17 scenes, all edited visuals (no face cam exists for part 2: 0 % on camera).
Plan with exact words/cues: `project/nvidia/EDIT_NOTES_nvs11.md`.

## Scenes (ground · transition in)
001 data hall plate + volt streaks (night) · 002 compute-share chart 60 → ~80 / ~1 % (paper, whip) · 003 Pacific night map: smuggling
routes vs US compute (map, hard cut) · 004 Caixin rationing article (paper, slide up) · 005 China map → Beijing pin → ZHIPU AI card, sales
−80 %, 1 of 5 customers served (map, vertical whip) · 006 ByteDance HQ + TikTok/ByteDance logos (night, hard cut) · 007 phone switches off,
holiday calendar, compute meter (paper, slide x) · 008 China map → Hangzhou pin → DeepSeek card (map, whip ←) · 009 monitor goes dark,
"12 hours", outage status strip (night, hard cut) · 010 Liang Wenfeng card + leaked-call pages, UNVERIFIED stamp (night, flash whip) ·
011 "2 years behind" timeline + 1/20 compute circles (paper, slide up) · 012 isotype researchers vs chips (night, vertical whip) ·
013 substation plate (night, hard cut) · 014 atlas spread: electricity China ≫ US (paper, whip) · 015 wall of GB200 racks "as many chips
as we want" (night, slide from left) · 016 two real Fortune articles: data-center backlash, Memphis can't power Colossus (paper, flash
whip) · 017 mirror matrix US/China × chips/electricity (paper, slide up) → accelerating push = cut on action into nvs12.
First scene: fresh shot (data hall). Last: matrix push-in ending exactly at 1174.583.

## Reference ids used
`ast_3d5f46c4c01248c5` (sc002 chart), `ast_3c804bab5fc04bfb` (sc005 + sc008 pins linked to cards), `ast_309797d0b3974b01` (sc009 —
no real outage headline exists in shared/news, so rebuilt as "one bold fact on a dark screen" rather than an article), `ast_29cb2d6f990c442a`
(sc010 pages + highlights), `ast_cba454c51d9a4a1c` (sc014 atlas spread). Effects: plate push, streaks, whips (plain/vertical/flash), hard
cuts on action, slides, map camera with counter-scaled labels/pins, route draw, count-ups, highlighter, pen markups (arrow, underline,
bracket, box, circles), stop-motion pin-ons, isotype, Vox layered multiplication, focus on real documents.

## Checks
- `npx --yes hyperframes@0.8.217 lint` (sandbox work/nvs11): 0 errors for compositions/nvs11.html (warnings: duplicate_media for the two
  china_night.jpg maps in sc005/sc008, file length).
- `python3 tools/sync_audit.py compositions/nvs11.html --transcript transcript_nv.json`: 0 cue(s) flagged (all text cues −0.06; two are
  listed as +0.02 only because the audit matched them to the short word just before the intended one: 1129.66 "computing", 1153.89 "United").
- Timeline dump (headless, seeked through every 0.5 s): duration 128.583 == DUR, no runtime errors.
- Snapshots: every scene at start+0.3 / middle / last 0.5 s, looked at; hold rule checked against the timing of every key animation
  (every key animation ends ≥ 0.5 s before the next transition starts).

## Assets
Shared: places/cern_data_centre_aisle, bytedance_fangheng_beijing, substation_750kv; hardware/cutouts/gb200_nvl72_rack_front_cutout;
news/s09_caixin_ration, s08_fortune_memphis (cropped); people/liang_1 (cropped, card size); logos bytedance, tiktok, deepseek_wordmark,
flag_us; icons person, chip, power_bolt, check, cross; maps kit world_night/world_overlay (derived Pacific crop), china_night/china_overlay.
Own (`assets/nvidia/nvs11/`, 2.5 MB, SOURCES.md + generator `gen_nvs11_assets.py`): Fortune 16 Jun 2026 "Data center hate is snowballing…"
page capture (first-party only, JS off), Memphis crop, Pacific-centred night map + China/US masks, China fill mask, Liang crop.
Missing/substituted: no Zhipu AI logo (typeset name tag, allowed per brief); no DeepSeek outage headline (status-strip chart instead);
no headline for "no public support" in shared → found and captured the real Fortune piece.

## Deviations from the lead's plan
- Lead row 003 (map with pins for the companies) split: sc003 = Pacific map (smuggled vs US compute), sc004 = real Caixin article on "we can
  see the result inside China", pins+cards in sc005/sc008.
- Lead row 005 "phone UI of feature toggles": built as our neutral illustration (no product UI, no app names).
- Lead row 009/010 (electricity / mirror): split into substation plate (filler line), atlas spread, racks wall, two real articles, matrix.
- Electricity bars proportional to Ember 2024 demand (China 10,066 vs US 4,401 TWh) with no numbers on screen; credit "Data: Ember".

## For the lead / MANUAL
- Gotcha: a Pacific-centred map strip (lon 70–300°) can't cover a 16:9 frame when pulled back far enough to show China and the US — crop
  the world base with enough latitude (here 80°N–60°S) so scale ≥ 1080/height at the widest framing.
- Helper: CSS `mask-image: url(country.svg)` + `mask-size`/`mask-position` (a solid-fill SVG path exported from the kit overlay) gives a
  textured country fill or silhouette at any scale with one file; the same mask with a dotted radial-gradient background makes a "compute
  density" fill (sc003).
- Capturing a news page from this box: puppeteer-core (from the npx cache) + the HyperFrames chrome-headless-shell, JS off, request
  interception allowing only the site's own host — ad hosts otherwise hang the page (`--screenshot` CLI never returned).
