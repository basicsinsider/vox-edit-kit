# ivs02 — NOTES (segment editor, 2026-11-01)

`compositions/ivs02.html` · id `ivs02` · master 144.02–296.18 · DUR 152.16 (timeline dump: `tl.duration()` = 152.16, no
runtime errors on a 0.5 s seek sweep). **Generated** — edit `project/ivan/gen/ivs02_template.html` and run
`python3 project/ivan/gen/build_ivs02.py` (it fills `@S()/@D()` clip times and inlines the simplified Russia/Ukraine outlines
from `assets/ivan/ivs02/derived/ee_paths.json`, made by `project/ivan/gen/ivs02_paths.py`).
Plan: `project/ivan/EDIT_NOTES_ivs02.md` (scene table + "as built" changes). Assets: `assets/ivan/ivs02/SOURCES.md`.

Checks: lint 0 errors for ivs02 (27 warnings: `nested_media_start_basis_ambiguous` on every timed clip — local times are
intended — plus file size / duplicate img); `sync_audit` 0 flagged (every text cue = word start − 0.06); hold audit by timeline
dump: every key animation ends ≥ 0.5 s before its cut except the two noted below; snapshots of every scene (middle + last 0.45 s +
transition frames) looked at.

## What was built (35 scenes)
| # | master | picture | layout / effect | transition out |
|---|---|---|---|---|
| sc001 | 144.02–148.34 | FACE wide | key phrase "how far Ivan had gone" (ink on the wall, kicker bar, top-left grid cell) | hard cut |
| sc002 | 148.34–151.22 | BBC Mamoń walking | lower-third name card on a scrim (kicker + rule + name) | whip L |
| sc003 | 151.22–156.98 | 2015 Moscow opposition march (Nemtsov march), ash print taped on paper | print card + text column on the grid | cut on action |
| sc004 | 156.98–161.94 | BBC Mamoń reading his phone | typeset message bubbles with video thumbnails (Ivan's stills) stacking/scrolling | vertical whip |
| sc005 | 161.94–166.42 | BBC phone showing the explosive device | pen circle (boil 4) + label stack | light-flash whip |
| sc006 | 166.42–171.22 | Ivan's night airfield video | surveillance frame (REC blink, running timecode, corner brackets) + leader line to the lights | hard cut |
| sc007 | 171.22–176.82 | FACE medium 1.25 | "democracy campaigner" (serif italic) | hard cut |
| sc008 | 176.82–181.46 | BBC Mamoń in profile | slow push, no text | hard cut |
| sc009 | 181.46–185.15 | FACE close 1.55 | "wasn't as simple" | whip R |
| sc010 | 185.15–188.58 | BBC two men in a field (backs) | "face to face" lower-left | paper slide up |
| sc011 | 188.58–190.43 | typed page | redaction bars (12 fps) + "careful about what he revealed" | push-through into the bars |
| sc012 | 190.43–194.59 | grid of 6 stills from Ivan's videos | 3×2 board on 96 px margins, "?" tags | hard cut |
| sc013 | 194.59–201.07 | FACE wide | "impossible to verify" (out before the whip) | whip L |
| sc014 | 201.07–204.35 | grey-man card → azure "Ukrainian intelligence" tag | pen line + red pen "?" + "or not" | whip |
| sc015 | 204.35–209.45 | eastern_europe_night map | Mamoń portrait pin → arc to Kyiv, Ukraine lit sky, radio rings, hero "GUR" (halate cool) | whip |
| sc016 | 209.45–212.91 | case file | azure CONFIRMED stamp + shake | hard cut |
| sc017 | 212.91–215.75 | FACE medium 1.3 | "his story checked out" | jump cut (punch-in) |
| sc018 | 215.75–221.05 | FACE close 1.55 | clean | whip |
| sc019 | 221.05–225.15 | eastern_europe_atlas | Russia oxblood (multiply), 7 facility diamonds at 12 fps, azure crosshairs lock on | whip |
| sc020 | 225.15–228.51 | BBC Astana skyline | KAZAKHSTAN passport-style stamp + shake | cut on action (car) |
| sc021 | 228.51–230.55 | BBC Ivan's hands on the phone | "one particular mission" | push-through into the phone |
| sc022 | 230.55–238.75 | eastern_europe_satdesat | Kazan aircraft plant pin + pulse rings → pull-back to Moscow (distance line "hundreds of miles east") → pull-back to Kyiv, footage card travels along the azure route, "his Ukrainian handlers" | hard cut |
| sc023 | 238.75–243.87 | FACE wide + **satellite print behind the narrator** (remove-background cut-out from 239.95) | "a satellite image" | punch cut |
| sc024 | 243.87–246.10 | FACE close 1.5 | clean | whip |
| sc025 | 246.10–252.30 | split frame (new layout): left Esri "from space", right Ivan's night video "on the ground" | two 816×640 panels on the 96 px grid | push into the satellite |
| sc026 | 252.30–256.26 | Esri Kazan aircraft plant close-up | marker box on a hangar, "?" → azure tick, "confirm details" | whip |
| sc027 | 256.26–259.54 | FACE medium | "one rather big problem" (oxblood kicker bar) | hard cut |
| sc028 | 259.54–262.66 | BBC hooded figure at night | "get close enough" | cut on action |
| sc029 | 262.66–266.60 | BBC CCTV cameras | oxblood-light surveillance brackets, "Russia's security services" in `--oxblood-light` | paper slide L |
| sc030 | 266.60–271.62 | notebook (lined paper) | pencil street sketch, red X, spiral of checking loops, clock hand turning five hours (brass sweep), key number FIVE HOURS (brass on ink box) | push-through into the X |
| sc031 | 271.62–277.50 | Ivan's video digging the cache (lifted) | focus brackets, "someone might catch him" | hard cut |
| sc032 | 277.50–282.50 | BBC quiet home / kitchen | "a normal day" (serif italic) | hard cut |
| sc033 | 282.50–284.82 | FACE close | "no idea" | hard cut |
| sc034 | 284.82–289.62 | Guardian: police detaining protesters (sat 0.35) | "accused of helping Ukraine" (Ukraine in sky) | whip |
| sc035 | 289.62–296.18 | FACE medium 1.22 → 1.34 push | "kept on taking more assignments" | segment end — the push keeps moving |

**First scene:** face cam wide, static fresh shot (no motion inherited). **Last scene:** face cam medium with a continuing
push-in (scale 1.22→1.34 over 6.6 s), text still on screen — ivs03 can hard-cut or whip out of it.

## Face cam
11 shots, 47.7 s of 152.16 s = **31.4 %** (target ≈ 35 %). Framings alternate wide 1.0 / medium 1.22–1.3 / close 1.5–1.55
(origin 1018,380 or 1018,330 = his face), 2–3 % push inside every shot; no grain/dust/vignette on him (ground "face" sets the
texture stack to 0). Text beside him always ink on the light wall, top-left grid cell (x 96, y 120–260), which stays clear wall at
every framing. One cut-out shot (sc023). I kept B-roll on the narrative lines (Mamoń, the videos, the maps); the shortfall is ~5 s.
Lip sync: face-cam `data-media-start` = master second (file aligned to master time); no offsets added (lead measures after render).

## Deviations / open issues for the lead
- (Resolved meanwhile in the working tree, not by me: `tools/build_index.py` now matches `ivs\d+` and `tools/make_sandbox.sh` links
  `vo_iv.mp3` / `transcript_iv.json`. Before that I used a patched /tmp copy of build_index and symlinked the VO in work/ivs02.)
- Two text reveals end < 0.5 s before their cut because the spoken word is right at the cut: sc011 "revealed" (189.71) ends 189.95,
  push starts 190.15; sc001 "gone" (147.62) ends 147.86, hard cut 148.34 (0.48 s).
- Insert slots: none in this range. SFX: `compositions/ivs02.sfx.json` (58 markers, master seconds, hero per scene marked).
  New marker names used: none beyond the c2/c3 vocabulary (`string_draw`, `radio_pulse`, `switch_click`, `clock_tick` exist).
- The Esri Kazan mosaic is 3584×2816 (> the 1920 px guideline) because sc026 shows it 1:1 after the push (3.8 MB).
- The BBC "Shadowmen" Ivan-interview clips carry an "AI Anonymisation" tag under the logo (to y ≈ 222 px in the source): those three
  clips are cropped at x ≥ 410 (others at 240,120). ivs03–07 editors using BBC clips should check the top-left corner.
- On-screen "Mamoń" in sc015 is a label under his BBC portrait at "Mamoń" (204.75); the narrator says "Mamon" (ASR), spelled per §4.

## Gotchas found (for MANUAL §4.2)
- `FX.split(el,"words")` rebuilds the element from `textContent`: inner colour spans are lost (recolour the returned span), and the
  whitespace spans are `inline-block; white-space: pre` (fx.css `.word`) — a wrapped line then starts with a visible space. Set
  the whitespace spans to `display:inline; white-space:normal` after splitting (helper `words()` in ivs02).
- `wd(id, cues)` style helpers: count words vs cues — a missing cue silently reuses the last one (a word appeared 0.5 s late).
- A slide-in scene must not carry a paper background on the `.v2-scene` itself (it covers the outgoing shot for the whole slide) —
  c5s03's gotcha, confirmed; put the ground on the shot.
- Snapshots: an all-black frame at a whip start or as the batch's last frame was a capture glitch both times — re-snap that time.
- Headless timeline dump for long segments: inline the `<template>` into a page with gsap + fx.js and drive it with
  `/root/.npm/_npx/*/node_modules/puppeteer-core` + `~/.cache/hyperframes/chrome/…/chrome-headless-shell` (scripts in this
  session were throwaway; pattern as in MANUAL §4.2 "Hold-rule audit").

## Helpers in the composition (candidates for promotion)
`frame(id,a,b,s0,s1,ox,oy)` face-cam framing + push · `fcText(sc,cues,outAt,dur)` face-cam key phrase with kicker bar ·
`landIn(b,t)` incoming overscale+blur land (push-through) · `pushOut(a,t,{to,origin})` · `slideIn(b,t,{axis})` · surveillance
brackets (sc006/029/031) · redaction bars (sc011) · message bubbles (sc004) · travelling card along a sampled path (sc022).

## Fix round 1 (2026-11-02, project/ivan/FIXES_ROUND1.md)
Timeline still 152.16 s; lint 0 errors (ivs02); sync_audit 0 flagged; every changed scene snapshotted and looked at.
1. **Map labels** — new helpers `mlab()` (label anchored at map px, Haskoy 800 uppercase 0.04 em for countries, `t-label` for
   places, bone + soft shadow on night/satellite, ink on the atlas) and `camPath()` (the camera of a map scene is driven by one
   proxy tween, so every label is counter-scaled to a constant screen size during pushes/pull-backs). Label anchors for
   countries were checked inside the country polygon (point-in-polygon on ee_paths.json).
   - sc015: UKRAINE, Kyiv (+ existing Mamoń, GUR).
   - sc019 atlas: RUSSIA, UKRAINE, Moscow (dot), and every facility pin is now labelled: Dyagilevo airbase, Engels airbase,
     Kazan aircraft plant, Voronezh airbase (unlabelled generic pins removed; camera reframed so Ukraine is in frame).
   - sc022 (Krish's 3:55 example): Kazan aircraft plant, TATARSTAN (now stays), Moscow, "hundreds of miles east", RUSSIA,
     UKRAINE, KAZAKHSTAN, Kyiv, "his Ukrainian handlers"; the Moscow–Kazan distance line fades with its label before the final
     pull-back so it doesn't cross the Kazan label; the footage card fades on arrival so Kyiv stays readable.
   - sc023 print, sc025 panel: "Kazan aircraft plant" caption strip; sc026 Esri close-up: "Kazan aircraft plant", "airfield".
2. **Crimea** — all Ukraine fills/outlines use `#c-ukraine` (includes Crimea) + `#c-crimea`; Russia uses `#c-russia` (excludes
   it). Crimea is outside every framing in this segment anyway.
3. **Markups at full res** — sc029 CCTV brackets were static while the camera pans: they now track the camera cluster
   (keyframes every 0.6 s measured in snapshots). sc031 focus brackets moved onto the canisters; sc006 ring + leader moved onto
   the airfield lights. sc005 circle, sc019 crosshairs, sc026 box/tick checked — on target.
4. **Face-cam edges** (checked frame by frame in the source; take cuts from the EDL at 176.585, 185.035, 243.84, 293.895,
   295.895): sc007 now ends 176.56 (was showing 6 frames of the next take settling) → sc008 B-roll starts 176.56 (clip recut
   05:01.0–05:05.96); sc009 ends 185.02 (whip moved) → sc010 starts 185.02; sc023/sc024 cut moved to 243.895 so the punch-in
   lands exactly on the first frame of the new take; sc035 gets a punch-in at 293.937 (take cut inside the shot) and the last
   0.285 s (295.895–296.18, start of the next take) is a held last frame under the continuing push. All other face-cam edges are
   mid-take while he talks (no leftovers). Face cam now 47.4 s = 31.2 %.
5. sfx.json: whip 185.15 → 185.02, + cut whoosh 176.56, + label pop 233.45.
