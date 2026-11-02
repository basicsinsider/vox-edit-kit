# ivs05 — NOTES (master 594.35–675.59, 81.24 s)

Built from `project/ivan/gen/ivs05_template.html` → `python3 project/ivan/gen/build_ivs05.py` (inlines the map paths) →
`compositions/ivs05.html`. Edit the template, not the output. Derived assets: `project/ivan/gen/ivs05_assets.py`.
Plan: `project/ivan/EDIT_NOTES_ivs05.md`. Assets + credits: `assets/ivan/ivs05/SOURCES.md`.

## Scenes (18) — all snapshotted and looked at (start, middle, last 0.5 s)
| id | master | picture | layout / effect |
|---|---|---|---|
| sc01 | 594.35–597.71 | FACE A medium 1.25 | clean, 2 % push |
| sc02 | 597.71–600.67 | paper timeline → SPIDERWEB marker, pen bracket back "more than a year before" | D05-style timeline (new variation), cut on action in |
| sc03 | 600.67–605.47 | BBC Mamoń walking + OUR typeset message bubble from Ivan with a Tu-95 photo attachment | new layout: footage left (gradient into night) + message UI right |
| sc04 | 605.47–610.25 | Ivan's own dusk airfield footage (BBC) as a received video: REC dot, corner brackets, counter | viewfinder frame (new), "footage / preparation for an attack" |
| sc05 | 609.80–614.03 | case card: WHEN / WHERE redacted with black bars + pen "?" | redaction bars, pen markups (§10.6) |
| sc06 | 614.03–617.36 | SBU FPV: drone hits a bomber, fireball | full-frame footage, scrim + "struck those airfields" |
| sc07 | 617.36–623.12 | FACE B close 1.55 → wide 1.0 | dark label box (kicker + "Ivan was involved / in Spiderweb") |
| sc08 | 622.67–630.96 | SBU ≠ GUR node diagram, grey man (Ivan) wired to GUR | D15 variation, pen ≠ (Haskoy has no "="), vertical paper slide in |
| sc09 | 630.96–633.92 | FACE C′ medium-left 1.3 | clean |
| sc10 | 633.47–637.40 | chat history scrolls back to the first bomber message (callback to sc03) | new layout: chat column + big text left |
| sc11 | 637.40–640.64 | Russia-wide night map, 4 Spiderweb airfields (Olenya, Ivanovo, Dyagilevo, Belaya) ping | pull-back camera, radio rings, focus hunt, cut on the curve out |
| sc12 | 640.64–645.12 | Eastern Europe night map: Ukrainian drone route → Yelabuga, Tatarstan | route draw-on, pin + rings, push |
| sc13 | 645.12–649.68 | BBC (Ostorozhno Novosti) drone hits the Yelabuga plant, in a print plate + Shahed-136 cut-out | plate + cut-out column |
| sc14 | 649.68–654.88 | Esri z16 satellite of the Alabuga SEZ: pen outline + 16 tower markers | satellite markup (D14 variation), focus hunt |
| sc15 | 654.88–659.52 | FACE C close 1.5 | label "an interesting theory" |
| sc16 | 659.07–664.56 | cork board: Ivan (grey man) card ↔ Yelabuga satellite print, string, "couldn't prove it" stamped word by word | ref 9 investigator wall |
| sc17 | 664.56–668.80 | FACE D wide 1.0 | clean |
| sc18 | 668.80–675.59 | FACE E medium 1.35 → accelerating push to 1.47 | label "still couldn't understand" |

Transitions: hard cut in → cut on action → vertical whip → light-flash whip → paper slide → whip → hard cut → vertical slide →
hard cut → slide → vertical whip → cut on the curve (2-frame blur) → whip → light-flash vertical whip → hard cut → slide → hard cut → reframe.
**First frame**: face cam A (fresh shot). **Last frame**: face cam E pushing in (ease-in, still accelerating at 675.59) — ivs06 can cut on that motion.

## Face cam: 27.75 s of 81.24 s = **34 %** (A 3.36, B 5.76, C′ 2.96, C 4.64, D 4.24, E 6.79). Framing changes at every shot
(1.25 / 1.55 / 1.0 / 1.3 / 1.5 / 1.0 / 1.35→1.47). Clean: grain/dust/vignette set to 0 in face scenes; no grade. `data-media-start` = master
second (no lip-sync offset added — lead measures after render).

## Checks
- Lint (sandbox `work/ivs05`): 0 errors in ivs05 (warnings only: duplicate img source for the Tu-95/Alabuga reuse, file length).
- `sync_audit.py compositions/ivs05.html --transcript transcript_iv.json`: 0 flagged; every text cue = word start −0.06 (box reveals −0.10).
- Timeline length = 81.24 (last tween = sc18 push ends at 675.59).
- Hold rule: key animations finish ≥ 0.5 s before each transition, except word-on-cue text that the narrator speaks right before a cut
  (sc03 "bombers" 0.2 s, sc12 "Tatarstan" 0.2 s, sc10 "year" 0.4 s) — the key motion (bubble, route, scroll) finished long before.
- Krish §0: text blocks anchored to x = 96 / the plate or object edge; labels on face cam sit in a dark box over the mic/desk (never the face);
  light text only on dark grounds/scrims, ink only on paper; oxblood text on night uses `--oxblood-light`, azure lines on night use `--sky`.

## Deviations / decisions (Krish asleep)
- ASR "GRU" shown as **GUR** (SEGMENTS §4); "Mamon/Momot" not on screen. No text on "which which".
- sc04 → sc05 slide lands at 610.25 (0.22 s after "Although") so "preparation for an attack" can be read before the paper covers it.
- sc14 tower markers are **illustrative positions** along an outline of the complex (the Esri imagery predates the towers); the narration says
  "satellite images showed new defensive towers", so the picture is our markup on a real satellite image, not a claim of exact tower sites.
- sc11 uses the world kit's Natural Earth Russia polygon; at that scale Crimea may read inside the Russia fill (the world overlay has no separate
  Crimea path). In the Eastern Europe crop (sc12) Crimea is filled with Ukraine. Lead: change if the channel prefers otherwise.
- Cork texture desaturated (0.22) to stay in palette.
- The SBU / GUR emblems could not be fetched (Commons originals 429; the SBU svg thumb errors) → typographic nodes instead.

## For the lead
- `tools/build_index.py` only auto-discovers `seg|intro|cNs` ids — `ivs05` is not picked up (prints `[] total -0.5`). I wrote
  `work/ivs05/index.html` by hand (palette_ivan.css). Suggest adding `ivs` to the regex. `tools/make_sandbox.sh` also doesn't link
  `vo_iv.mp3` / `transcript_iv.json` (linked by hand).
- New helpers in the composition worth promoting: `popSvg(node, t, cx, cy)` — pops SVG nodes with `svgOrigin` (the
  `transformOrigin + transformBox:"fill-box"` pop rendered the first frames at a wrong position, seen in a snapshot); `frame(fw, t0, dur, s0, s1, ox, oy)`
  for face-cam framing/push; `labelBox()`.
- Gotcha: face-cam framing at 1.25–1.55 with the scale origin on the face centre crops the top of Krish's head — put the origin
  ~120 px ABOVE the face (y ≈ 150–210 in the 1080 frame) to keep headroom.
- SFX markers: `compositions/ivs05.sfx.json` (43, master seconds; one hero per scene marked in the notes).

## Fix round 1 (Krish, 2026-11-02 — `project/ivan/FIXES_ROUND1.md`)
- **Map labels** (style of `label_ref_china.png`: Haskoy 800 uppercase, +0.04 em, bone with soft dark shadow; places `t-label` 24 px
  next to a dot). New helper `camDrive(cam, init, keys, labels)` drives each map camera with a proxy tween and moves screen-space labels
  with it, so labels keep a constant size through the 1.45 → 0.65 pull-back. Labels fade in with the map (0.6 s, 12 fps).
  - sc11 Russia-wide: RUSSIA (72 px), UKRAINE (40 px), the four Spiderweb airfields by name (Olenya, Ivanovo, Dyagilevo, Belaya) next to
    their dots; final framing moved to centre (1650, 860) × 0.65 so Ukraine and Belaya both stay inside the safe area.
  - sc12 Eastern Europe: RUSSIA, UKRAINE, Moscow and Kazan (dot + label), Yelabuga (52 px, on its word) + TATARSTAN (32 px, on its word),
    now screen-space under the pin; route bent further north (control −200) so it clears the Kazan/Russia labels; pin rings smaller.
  - sc14 satellite: ALABUGA (56 px) inside the outline of the zone.
- **Crimea = Ukraine** in sc11: `#c-crimea` from `eastern_europe_overlay.svg` re-projected into the world-kit crop (`ivs05_assets.py` →
  `wide.crimea`), added to Ukraine's fill/outline and masked out of Russia's (mask on each blended path — a masked `<g>` isolates the group
  and kills `mix-blend-mode: overlay`, Russia went flat bright red; gotcha for MANUAL §4.2). sc12 already used the EE overlay (Crimea in Ukraine).
- **Markers re-checked** at full res: airfield dots (coordinates verified: Olenya 68.15N 33.46E, Ivanovo-Severny 57.06N 40.98E, Dyagilevo
  54.64N 39.57E, Belaya 52.92N 103.57E), Yelabuga/Moscow/Kazan dots from the kit json, satellite outline/towers round the zone, cork pins
  = string ends (470,229)/(1360,257). Airfield rings reduced (max 64) so they don't run through the labels.
- **Face-cam edges, frame-exact.** Source jump cuts found from `project/ivan/edl_frames.json` (edit_in + 37 s) and verified by
  frame-difference on the 30 fps master: 597.60, 617.40, 622.80, 656.73, 668.73, 675.33. New edges: A 594.35–597.625 · B 617.4167–622.7917
  (sc06 SBU clip runs to 617.4167; slide into sc08 lands 622.7917) · C′ 630.96–633.92 (no jump) · C 654.88–656.75 close 1.5 → 656.75–659.52
  medium 1.2 (reframe hides the 656.73 jump) · D 664.56–668.75 · E 668.75–675.3333 → 675.3333–675.59 punch-in 1.58→1.64 (the 675.33 jump
  is the start of ivs06's take; the reframe keeps it reading as a push). Before 617.40 the source is a frozen leftover — no longer shown.
  Face cam now 27.28 s = **33.6 %**.
- **Expendable window 625.625–626.2917** (repeated "which"): sc08 is now tight on SBU (scale 1.3) until a hard punch-out to the wide
  diagram exactly at 625.625. SBU pop shortened to 0.45 s (done 625.53). Inside the window only a static wide frame with a slow drift: no text,
  no animation start, no SFX. Next event ≠ at 626.52, "completely different" at 626.64.
- Timeline still 81.24 s; lint 0 errors (ivs05); sync_audit 0 flagged; sfx.json updated (597.625, 622.34, +2 soft whooshes).
