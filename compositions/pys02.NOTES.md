# pys02 — NOTES (master 116.00–213.60, DUR 97.60) — Paraguay in 2026: World Cup, the tweet, the boring success story, "one bad news"

Plan: `project/paraguay/EDIT_NOTES_pys02.md` (scene table, words → picture reasons). Built as planned, 23 scenes; deviations below.
Checks: lint 0 errors for pys02 (only the common `nested_media_start_basis_ambiguous` warnings on face-cam videos, same as ivs*); `sync_audit`
0 flagged — every text cue is a literal `T(word start − 0.06)`; five cues read "+0.02" because the audit matches the nearest word (e.g. the cue
for "World" 121.84 is reported against "the" 121.82) — they are all −0.06 to their own word. Timeline = 97.60 (last tween = the hand-off push
ending 213.60). Snapshots of every scene (start/middle/end + every transition) looked at against the words and SEGMENTS §0.

## Scenes (as built)
| id | master | picture / effect | transition in |
|---|---|---|---|
| sc001 | 116.00–121.04 | Asunción skyline across the bay, slow push; PARAGUAY (halate hero) + "a very interesting country" | fresh shot |
| sc002 | 121.04–125.04 | Paper collage: two France v Paraguay photos pinned stop-motion with tierra tape, focus hunt; label-box "the World Cup" → "surprisingly well" | whip → |
| sc003 | 125.04–129.52 | Typeset social post (Celeste Amarilla avatar + name; body BLURRED, never readable) on a dark plum-tinted ground; "one of their politicians" | slide ↑ |
| sc004 | 129.52–132.62 | Mbappé (France) close-up, push-out; "lost to France" | hard cut on action (post push) |
| sc005 | 132.62–138.30 | FACE M; the blurred post sits on the empty wall beside him, blurs further on "I'm not gonna read this tweet", flies off on "you can do so" | whip → |
| sc006 | 138.30–141.84 | Paper: the post + anonymous reply cards multiplying (stop-motion, tierra = the people); "calling her racist" | paper slide ← |
| sc007 | 141.84–143.92 | Modern TV on a dark wall: her official portrait + plum name strap ("she went in front of TV") | whip ← |
| sc008 | 143.92–147.89 | FACE M, lower-left serif quote “I didn't even mention this guy's skin color.” word by word | hard cut |
| sc009 | 147.89–150.70 | FACE W — framing change exactly on the 147.883 EDL join, no text (the beat after the joke) | framing cut on the join |
| sc010 | 150.70–154.85 | Wall of 6 news screens all on the same story (blurred headlines); "the only global news story" → screens dim → 2026 (yellow halate) | vertical whip |
| sc011 | 154.85–156.56 | FACE M "not the case" | cut |
| sc012 | 156.56–163.92 | South America night map (kit), camera push to Paraguay; Paraguay fills tierra; BOLIVIA / BRAZIL / ARGENTINA / PARAGUAY labels counter-scaled; "a success story" → "a boring one" → "South America" (right lower third) | cut on the map push |
| sc013 | 163.92–169.50 | Paper rating ladder (Moody's notches B1…A3, logo in ink), dashed investment-grade line, Paraguay marker climbs Ba1 → Baa3; 2024 with yellow highlighter; INVESTMENT GRADE stamp | vertical whip ↓ |
| sc014 | 169.50–175.36 | FACE W: "safer for foreign investors" → "a big deal" | hard cut |
| sc015 | 175.36–178.09 | Lined paper timeline 1811 → 2024 (decade ticks), camera tracks along it, 2024 lands, yellow highlight + tierra pen circle; "the first time in its history" | paper slide → |
| sc016 | 178.09–181.93 | FACE C (no text on the close-up) | hard cut |
| sc017 | 181.93–185.69 | **2.5D** Wall Street: WALL ST sign cut out as the near layer over the NYSE flags/columns (sign inpainted out of the far plate), dolly + focus hunt; "$350 million" counter (yellow halate hero) + "in bonds" | light-flash whip |
| sc018 | 185.69–188.97 | Blueprint: an arch bridge drawn on in light lines (+ dimension line); "infrastructure projects" | hard cut on action (dolly) |
| sc019 | 188.97–193.41 | FACE M: "on the right path" → "trusted by world investors" | hard cut |
| sc020 | 193.41–201.10 | Graph paper: growth line draws up ("the economy was growing"), then half-year bars, the last (tierra) breaks the dashed record line; "first half of this year"; "the strongest growth" with yellow highlighter | vertical whip ↑ |
| sc021 | 201.10–203.94 | FACE W: "good news was all around" | hard cut (starts after the 201.083 join) |
| sc022 | 203.94–207.76 | Paper collage of the good news (stamp, $350 million, World Cup photo, growth bars) + a dark card that flips: "one bad news"; the others dim | slide ↑ |
| sc023 | 207.76–213.60 | The ueno tower from the air; a shadow sweeps over it and the photo darkens — "hiding a lot of its problems" ("problems" in ueno-light); the push accelerates into the cut (hand-off to pys03) | hard cut on action |

First scene: fresh Asunción shot. Last scene: push into the shadowed tower still accelerating at 213.60.

## Face cam
sc005 5.68 + sc008 3.97 + sc009 2.81 + sc011 1.71 + sc014 5.86 + sc016 3.84 + sc019 4.44 + sc021 2.84 = **31.15 s of 97.60 = 31.9 %** (target ≈ 35 %;
the 116.45 join right at the segment start and the joins at 138.37/139.08 made extra face-cam lines there impractical without jump cuts).
Framings vary W/M/C (origin 1030,210 ≈ 120 px above his face); every shot ends before / starts after an EDL join, or switches framing exactly
on it (147.89). Edges checked on face-cam frame strips (no mouse reaches/settling seen at 12 fps; please re-check at 24 fps in the render QA).

## Effects / layouts used
Plate + fringe + push (sc001), paper collage with stop-motion pins + tape + focus hunt (sc002, sc022), typeset social post with blurred body
(sc003/005/006), modern TV screen (sc007), screen wall (sc010), night map with fill + counter-scaled labels + camera path (sc012), rating-ladder
chart + stamp + highlighter (sc013), timeline track + pen circle (sc015), 2.5D (sc017), odometer-style counter `FX.text.count` (sc017),
blueprint draw-on (sc018), line + bar chart with record line + highlighter (sc020), card flip (sc022), shadow sweep (sc023).
Transitions: whip ×4 (incl. 3 vertical), light-flash whip, slides ×4, hard cuts on action, face-cam framing cut on the join.

## Deviations / decisions
- sc004/005 cut moved 132.40 → 132.62 and sc010/011 154.60 → 154.85 so "lost to France" and "2026" hold ≥ 0.3–0.5 s before the transition.
- "in country's history" (199.51–201.11) gets no extra text (one idea: the highlighted "the strongest growth"); the chart holds.
- The growth chart is schematic (no axis values, no years) — the narration gives no numbers; the "first half of this year" bar is the only labelled one.
- The rating ladder shows Moody's notation (Ba1 → Baa3 = Paraguay's 2024 upgrade per RESEARCH.md). "$350 million" shown as spoken (RESEARCH: it
  was ueno's own bond — picture is generic Wall Street, no issuer named).
- The tweet is a typeset recreation with the body blurred (never readable) and her real portrait/name; no handle, date or X logo invented.
- Face-cam M/W text sits in the lower-left over the desk/mic corner on a soft scrim (his face is centre-right).

## Assets
Own: `assets/paraguay/pys02/` (SOURCES.md): Celeste Amarilla official portrait (Commons, CC BY-SA 4.0, Congreso de Paraguay — credited on screen),
derived Wall St sign layer + inpainted far plate, South America borders/Paraguay fill SVGs. Shared: asuncion_skyline, wc_fra_par_mbappe_* (4),
wall_street_nyse, ueno_tower_aerial_reuters, logos/moodys.png.
**Credits (fix, after the shared SOURCES.md files landed):** on-screen credits now follow `assets/paraguay/shared/*/SOURCES.md`:
sc001 "Photo: P. S. F. Freitas / Wikimedia Commons, CC BY-SA 4.0"; sc002 / sc004 / sc022 World Cup photos "Bryan Berlin / Wikimedia Commons,
CC BY-SA 4.0" (sc022 credit newly added); sc010 screens "Photos: Bryan Berlin … · portrait: Congreso de Paraguay, CC BY-SA 4.0" (newly added);
sc017 "Photo: Carlos Delgado / Wikimedia Commons, CC BY-SA 3.0"; sc023 "Photo: © Reuters (fair use)"; sc013 Moody's logo "© Moody's, fair use"
(unchanged). Re-linted (0 errors), sync_audit clean, credit frames snapshotted and read. Still true: `shared/photos/paraguay_team_match.jpg` is
Morocco's team; `wall_street_sign.jpg` is not a valid image.

## Gotchas for MANUAL
- (fixed by the lead) `tools/build_index.py` now picks up `pys*`.
- fx.css `.hl` strikes again: a `.hl` headline bar inside my news screens painted a full yellow highlighter — renamed `.hb` (MANUAL §4.2 c5s03 note).
- Lint 0.8.217 errors (`gsap_non_transform_motion`) on tweening `top` — use `y`.
- 2.5D from one photo: if the near layer is cut from the same photo, the far plate still contains it and parallax shows it doubled — fill the
  cut region in the far plate first (numpy diffusion fill at ¼ scale, ~400 blur iterations, blended with a feathered mask: no OpenCV needed).
- `paper_lined_01_hires` has a punched hole near the left edge (reads as a white dot at ≈ x 96, y 540) — keep it off the focal area.

## SFX
`compositions/pys02.sfx.json` — 41 markers (whips/slides, pins, stamp, counter, pencil, highlighter, card flip, booms on 2026 / the tower cut,
riser on the hand-off push). Hero per scene marked `normal`.

## Fix round 1 (Krish, 720p review — MANUAL §0 "No narration captions")
- **Removed every narration caption**: sc001 "a very interesting country", sc002 "the World Cup"/"surprisingly well", sc003 "one of their politicians",
  sc004 "lost to France", sc006 "calling her racist", sc008 the skin-colour quote, sc010 "the only global news story", sc011 "not the case",
  sc012 "a success story"/"a boring one"/"South America", sc014 "safer for foreign investors"/"a big deal", sc015 "the first time in its history",
  sc017 "in bonds", sc018 "infrastructure projects", sc019 both lines, sc020 title "the economy was growing" + "the strongest growth" callout,
  sc021 "good news was all around", sc022 "one bad news" (card face is now a tierra "?" — the news "no one knew about"), sc023 both lines.
- **Kept** (graphics, not captions): PARAGUAY title on the skyline, map labels (sc012), Moody's ladder + 2024 + INVESTMENT GRADE stamp (sc013),
  2026 over the news wall (sc010), "$350 million" counter (sc017), chart labels sc020 "first half of this year" + new "Economic growth" axis label
  and "Previous record" line label, sc015 new "first investment grade" label under 2024, TV name strap (sc007), credits.
- **The real tweet**: Krish's screenshot `assets/paraguay/pys02/photos/celeste_amarilla_tweet_krish.png` (X / @CelesteSenadora quoting Diario Olé,
  translated view) replaces the blurred typeset post — sc003 full card on the dark ground, 3D tilt settling + push to the text + focus hunt (readable);
  sc005 the same post (top crop) on the wall beside him, no blur; sc006 the post centred among the reply cards. Credit "X / @CelesteSenadora" on all three.
- Timings, transitions, face cam (31.9 %) and duration (97.60) unchanged. sfx: removed the 197.40 highlighter marker (callout gone); notes updated.
- lint 0 errors, sync_audit 0 flagged (remaining text cues are the kept graphics), changed scenes snapshotted and looked at.
