# ivs01 — NOTES (segment editor, cold open, master 0.00–144.02)

Built: `compositions/ivs01.html` (33 scenes, `data-duration` 144.02 = DUR), generated from
`project/ivan/gen/ivs01_template.html` by `python3 project/ivan/gen/build_ivs01.py` (it only inlines the map outline
paths from `assets/ivan/ivs01/derived/paths.json`). **Edit the template, then re-run the build** — don't hand-edit the output.
Derived maps: `project/ivan/gen/ivs01_assets.py`. Plan: `project/ivan/EDIT_NOTES_ivs01.md`. Assets + licences:
`assets/ivan/ivs01/SOURCES.md`. SFX markers: `compositions/ivs01.sfx.json` (53, master seconds, no SFX inside insert 1).

Checks: lint 0 errors in ivs01.html (the 2 project errors are intro02/intro03's missing face-cam webms, not this segment);
`sync_audit` 0 flagged — every text cue is a literal `T(word start)` drawn at `T(..) − 0.06`, long lines word by word;
snapshots of every scene (start/middle/end) looked at, layout/contrast fixed (see below).

## Scenes, effects, layouts
| scene | master | picture | effect / layout |
|---|---|---|---|
| sc001 | 0–2.20 | night relief map of Russia | outline draw-on, oxblood fill, surveillance reticle hunts + locks, focus hunt, camera push → cut on action |
| sc002 | 2.20–6.18 | BBC: Ivan watching distant lights at dusk | `IVAN` halate hero; **split-frame "double life"** (new): bone line cuts the frame, the right slice drops 34 px and turns ash-grey |
| sc003 | 6.12–9.58 | Moscow metro passengers (contact print on paper) | two papers, print card, pen circle (§10.6) |
| sc004 | 9.52–14.10 | BBC: Ivan (anonymised) on a ferry | push, left scrim |
| sc005 | 14.10–20.10 | grey man ↔ GUR emblem | D15 link-diagram variation on graph paper, dashed "secret" thread revealed by a clip wipe |
| sc006 | 20.04–23.52 | BBC: explosives hidden at night near an airfield | light-flash whip in, push |
| sc007 | 23.52–30.56 | BBC: Ivan under a drone → masked Ivan ("a patriot who loves his Motherland" in the doc) | hard cut, `a Russian patriot` halate hero |
| sc008/016/018/021/031 | 30.56 / 64.89 / 70.09 / 81.29 / 131.78 | face cam | 5 pops: wide 1.0→1.025 · medium 1.28 · close 1.55 · medium 1.32→1.29 (slow pull) · wide push 1.0→1.07; clean (grain/dust/vignette off) |
| sc009 | 32.40–37.16 | desaturated atlas map | Russia/Ukraine watercolour-multiply fills on their words, azure strike arrows + X marks, ink label box |
| sc010 | 37.10–43.80 | framed official portrait of Putin (oxblood duotone) on a dark wall | **frame drops crooked on "lose"** (new) |
| sc011 | 43.35–47.44 | isotype of grey men (ref 5 variation) | paper slide up, Ivan shrinks into his cell, 79 men fill at 12 fps outward |
| sc012 | 47.44–50.70 | BBC: Russian tanks on a road | push |
| sc013 | 50.64–56.57 | night EE map | network threads Kyiv → 10 Russian cities (D15 on a map) |
| sc014 | 56.12–60.57 | Gerasimov & Shoigu print in a case file | paper slide, paper clip, pen circle on the shoulder board |
| sc015 | 60.57–64.89 | sat-desat EE map | camera pull-back, arrows from the border, radio rings at Moscow / Engels / Dyagilevo / Ivanovo |
| sc017 | 66.65–70.09 | FSB HQ, Lubyanka (ash duotone) | CCTV focus brackets + blinking dot |
| sc019 | 71.69–74.76 | BBC: drone strike on a Kazan high-rise | ink label box over the light sky |
| sc020 | 74.70–81.29 | Moscow street crowd | focal blur travelling across three passers-by + bone pen circles; holds through the 3.8 s VO pause |
| sc022 | 83.13–92.09 | dossier: grey-man ID card, `IVAN` stamp, Bolotnaya 2011 rally print | D07 collage/dossier, camera push to the print, focus hunt |
| sc023 | 92.09–97.85 | opposition march, Feb 2012 | vertical whip, push |
| sc024 | 97.85–102.41 | rally crowd, Feb 2012 | **closing walls** (new): two oxblood-dark textured panels step in on "harder … harder" |
| sc025 | 102.41–108.76 | night EE map | Russia fill, Ukraine sky, 4 invasion arrows, `February 2022` brass key number, fires spread at 12 fps |
| sc026 | 108.70–116.70 | **insert 1** (`insert1.mp4`, Guardian "No to war!") | flash whip in, hard cut out, credit 13 px, light vignette/grain only, no text over their subtitle |
| sc027 | 116.70–119.61 | Guardian raw: marchers fill a street | push |
| sc028 | 119.16–124.56 | typeset Criminal Code page (Art. 280.3 header) | two papers, words revealed on cue, highlighter, two-hit `A CRIMINAL / OFFENSE` stamp |
| sc029 | 124.50–126.90 | arrests on Tverskaya, 24 Feb 2022 | vertical whip, push |
| sc030 | 126.90–131.78 | Vladikavkaz border traffic jam, Sept 2022 (tall print) | print rises, drift |
| sc032 | 133.62–140.00 | Kremlin at dusk | push + light dims on "losing the war" |
| sc033 | 139.94–144.02 | BBC: Ivan's silhouette at a ferry window | whip in; push still moving at 144.02 |

Transitions used: horizontal whips, vertical whips, light-flash whips (×2), paper slides (×3), hard cuts on action.
Reference layouts: D15 (sc005, sc013), D07 dossier (sc022), ref 5 isotype (sc011), ref 9-style case file (sc014).
Not used here: 2.5D (no time; the masked-Ivan shot is video) — the lead may want it in ivs02/03.

**First scene:** night map of Russia, camera pushing west→ in, reticle. **Last scene:** Ivan's silhouette at a window,
slow push-in still moving at 144.02 (hand-off = cut on action into ivs02's fresh shot).

## Face cam
5 pops, 1.60–1.84 s each, none before 30.56 s: 8.88 s on camera = **6.2 %** of the segment (all before ~134 s, as asked).
`data-media-start` = master start (no offsets added).

## Open issues for the lead
1. **VO pause 77.45–81.29 (3.8 s of silence)** after "…helping them do it." — an EDL join (the face cam shows Krish shifting in
   his chair there, so no face cam). I held sc020 (focal-blur crowd, slow push) over it. Consider tightening the EDL; if you do,
   every later cue in this segment shifts.
2. `tools/build_index.py` does not pick up `ivs*` compositions (its regex is `seg|intro|c\d+s`). I previewed with a patched copy
   (`/tmp/ivs01/build_index.py`, regex `seg|intro|ivs|c\d+s`); the shared tool is untouched — please add `ivs` there
   (check `build_master.py` too).
3. Timing changes vs the plan: several cuts moved one word later so text holds ≥ 0.4–0.5 s before transitions (sc003 6.12,
   sc005 14.10, sc006 20.04, sc010 37.10, sc011 43.80 landing, sc014 56.57 landing, sc015 60.57, sc020 74.70, sc025 102.41,
   sc030 126.90, sc033 139.94). A few word-level holds remain at ~0.3–0.45 s where the next line starts immediately (sc002
   "life"→whip, sc019 "country"→whip, sc032 "power"→whip).
4. "Art. 280.3" on the law page is the real article for "discrediting the army" (prop text, small); the narration's own words are
   the only large text there.
5. Grey-man icons in SVG: GSAP x/y/scale on an SVG `<g>` (even with `svgOrigin`) misplaced the figure; animating the inner
   `transform` attribute through a proxy object (`onUpdate`) works — gotcha for MANUAL §4.2.

## Fix round 1 (Krish, 2026-11-02) — applied
1. **Map labels** (helpers `country()` / `place()` / `counter()` in the template): Haskoy 800 caps, 0.04 em tracking; bone + soft
   shadow on night/sat maps, ink on the atlas. RUSSIA + UKRAINE on every map: sc001 (80 / 40 px, counter-scaled through the push),
   sc009 (72 / 52, ink), sc013 (64 / 46), sc015 (64 / 44, counter-scaled 1.32→1.0), sc025 (72 / 56). Places shown: sc015 MOSCOW,
   ENGELS AIR BASE, DYAGILEVO AIR BASE, IVANOVO AIR BASE (t-label 24 px beside the strike dots). No other place is named on a map
   in this segment. sc001 now also draws Ukraine's outline (sky).
2. **Crimea**: all fills/outlines come from the eastern_europe / russia kit overlays (`#c-ukraine` includes Crimea, `#c-russia`
   excludes it) — checked in snapshots of sc001, sc009, sc025.
3. **Markups**: sc014 circle moved from Gerasimov's sleeve to one ellipse around both faces (checked on a full-res gridded frame);
   sc020 crowd circles verified on the three passers-by, and the focal blur now opens wide at 77.10 so every circled person is
   sharp; sc003 circle verified on the face; sc017 CCTV brackets now frame the whole Lubyanka facade. sc015 camera no longer shows
   past the map's right edge (end centre x 960.5).
4. **Face-cam edges** (checked frame by frame at 24 fps): pop 1 30.56–32.40 — punch-in 1.0→1.2 at 31.53 hides a jump cut in the
   take; pop 2 now ends 66.45 (jump at 66.45 was inside), sc017 starts 66.45; pop 3 — reframe 1.55→1.3 at 70.41 (jump);
   pop 4 starts on the exact frame 81.292 (= window end); pop 5 now starts 131.917 (a jump cut sat 3 frames after the old start)
   with a punch-in at 132.44. Face cam now 8.54 s = **5.9 %**.
5. **Expendable windows**: hard scene cut at **78.00** (sc020 ends; new plain filler shot sc020b 78.00–81.292, nothing in it) and at
   **97.875** (sc023 → sc024; sc024's first animation is at 98.49). No text cue, key animation, face-cam or SFX marker inside either
   window. sc020's circles/focal moves finish by 77.55.
Checks: lint 0 errors in ivs01, sync_audit 0 flagged, duration 144.02, sfx.json updated (66.45 whoosh, 75.50 circles, 61.53 pins).
