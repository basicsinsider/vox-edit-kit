# Ivan — Krish's fix round 1 (2026-11-02) — every segment editor reads this

Krish watched v2 (`review/ivan_720p.mp4`). His v2 timestamps → master seconds: before 78.0 equal; after it add 3.2917
(the dead air 78.0–81.2917 is cut at assembly). v3 will also cut two repeated words (below), so his next timestamps shift again.

## 1. Country / place labels on EVERY map (reference: `references/style-images/ivan/label_ref_china.png`)
- Every map shot labels what the narration talks about: **RUSSIA** and **UKRAINE** on every map where they are visible (also when the
  narrator isn't naming them in that second — the viewer must always know which country is which), plus every place he names while that
  map is on screen: Moscow, Kyiv, Warsaw, Poland, Kazakhstan, Tatarstan, Kazan, Yelabuga, the Spiderweb airfields (Olenya, Belaya,
  Dyagilevo, Ivanovo — and any other base we show), the Kirillov / Sarvarov sites, rail lines, etc. Airfields/sites: small pin + label.
  Example Krish flagged: his 3:55 = master ≈ 238.3 (ivs02) — places shown/narrated there have no labels.
- Look (from his reference, translated to our kit): country names in **Haskoy 800, uppercase, light tracking (~0.04 em)**, bone `#f0ede6`
  with a soft dark shadow on night/satellite maps, ink `--ink` (no shadow) on atlas/paper maps; size to fit the country and the framing
  (Krish: "change the size of text of the labels in accordance with what the video demands") — big countries ~48–80 px, regions ~30–40 px,
  cities/airfields `t-label` 22–28 px next to a small dot/pin (+ a short leader line if the spot is crowded). Placed at the visual centre of
  the land area, never across a border, a pin, an arrow or the frame edge; counter-scaled so the size stays constant during camera pushes
  (or let it grow with a push only if it stays inside the country). They appear with the map (a 0.5–0.8 s eased fade/rise, 12 fps) and stay
  while the map is up. Contrast check every label (MANUAL §10.10). No Cyrillic (our fonts' coverage isn't verified).
## 2. Crimea is part of Ukraine on every map
- Ukraine fills/outlines must include the Crimean peninsula; Russia's must not. The kit overlays `eastern_europe_overlay.svg` and
  `russia_overlay.svg` already do this (`#c-ukraine` includes Crimea, `#c-crimea` exists, `#c-russia` excludes it). World-kit
  (`world_*`, `world.json`) polygons put Crimea in Russia — if your map uses those, add Crimea (take `#c-crimea` from eastern_europe_overlay
  and re-project with the json formulas) to Ukraine's fill and cut it out of Russia's. No special Crimea label. Check every map frame.
## 3. Markups / circles on the right spot
- Circles, boxes, focus brackets must sit on the thing they point at (Krish: ~0:59 master 59 (ivs01) — the circle on the two generals sits
  on a sleeve, not on the face). Re-check EVERY markup in your segment at full resolution and fix the coordinates.
## 4. Face-cam shot edges — no leftover frames
- Krish: at his 6:15:15 (master ≈ 378.9, ivs03) the narrator has finished and reaches for his mouse on camera. For EVERY face-cam shot,
  look at the face cam source (`assets/facecam/ivan_facecam_master.mp4` at master time) frame by frame over the shot's last ~0.6 s and
  first ~0.3 s: if he stops talking, glances at his screen, reaches for the mouse, shifts, settles, opens/closes his mouth before/after the
  line — end the face-cam shot earlier / start it later so those frames are never shown (start the next B-roll a few frames early; the VO
  is a separate track, so his words still play over the B-roll). Be precise to the frame; don't cut away during an important on-camera
  gesture unless it's the leftover. Extract frames like: `ffmpeg -ss <t> -t 1 -i assets/facecam/ivan_facecam_master.mp4 -vf fps=24,scale=480:-1,tile=6x4 x.jpg`.
## 5. Words that will be removed at assembly (picture + audio together) — make these windows expendable
- ivs01: **97.875–98.1667** (a repeated "But") and the existing dead air **78.0–81.2917**. ivs05: **625.625–626.2917** (a repeated "which").
  The frames inside each window are dropped. Put a hard cut (scene change) exactly at the window START so the shot before and the shot after
  are different shots (the drop is then invisible); no text cue, key animation or face-cam word inside the window. Text cues of words after
  the window keep their master times (assembly handles it).
## 6. ivs07 only — rail lines (his 13:27:15 = master ≈ 810.9): draw railways as railway-track symbols (two parallel rails + cross-ties,
  or the classic map railway line: dark line with regular light/dark dashes) instead of single lines; trains ride on them.
## Output: 4K
- v3 renders at 3840×2160 (`--resolution 4k`, Chrome DPR 2 — the compositions stay 1920×1080). Nothing to change, but avoid tiny raster
  images blown up full-frame where a bigger source exists.
## Checks (same as before)
lint 0 errors (your segment), `sync_audit` clean, snapshots of every changed scene LOOKED at (labels readable, Crimea, circles, face-cam
edges), timeline duration unchanged, `sfx.json` updated if any event times moved, NOTES.md updated with a "Fix round 1" section.
