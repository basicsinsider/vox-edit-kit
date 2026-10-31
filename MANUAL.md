# Documentary Edit Kit — Instruction Manual

Give this folder plus a raw voiceover file to a fresh Claude Code session and say:
"Read MANUAL.md and edit this audio with the kit." Everything needed to rebuild the look is here:
the effects library (`lib/`), tools (`tools/`), working examples (`compositions/`), the user's visual
references (`references/`), textures, fonts list, and the agent pipeline.

**Keep this manual current.** Whenever you learn a new technique, fix a gotcha, or the user gives
feedback, update the relevant section and add a line to the Changelog at the bottom.

---

## 0. What the user wants (non-negotiables)

1. Documentary/explainer edit over a narrated voiceover. 1920×1080, 24 fps.
2. **Never touch the voiceover.** No EQ, compression, gain, noise reduction or re-timing. Unity gain.
   Delivered samples carry the original MP3 frames (stream copy); full edits mix the bed *under* it.
3. **Every on-screen word lands on the spoken word** (0–120 ms before it). See §4.4.
4. **Fonts: only Cooper Hewitt, Haskoy, Crimson Pro.** (Installed in `~/Library/Fonts`; copy into `assets/fonts/`.)
5. **One palette for the whole video** (§3.1). Consistent everywhere: West = vermilion, East = navy.
6. **Use every effect at least once, with variations** (different TVs, newspapers, maps, 2.5D scenes,
   chart styles). Never the same treatment twice in a row.
7. **Use all of the user's reference layouts** in `references/style-images/` (animated with our effects,
   in our fonts/palette) — except #3 "coin in pieces" (skip) and #2 "A Dollar's Worth" (optional; if used,
   animate it well). See §6.
8. **Sound:** marimba-led documentary bed + subtle SFX on every object. Free sources only. Never
   overpowers the voice (§7).
9. **On-screen text follows the voiceover exactly — no fact-checking.** Show stats and claims as narrated.
   Only fix ASR spelling of names (the analyst's corrections list).
10. Show the user 4–10 s samples first; only build the full edit after they approve. (Taiwan long-form, 2026-10-31: the
    style is approved — Krish wants each chunk delivered whole, **no key-scene samples** in between.)

---

## 1. Environment setup (any machine: Linux cloud session or macOS)

```bash
bash setup.sh          # ffmpeg/ffprobe, zsh, HyperFrames CLI + browser + agent skills, Parakeet ASR,
                       # .venv (numpy scipy pillow soundfile), fonts, Agent Reach. Safe to re-run.
export PATH=~/.local/bin:$PATH
npx hyperframes doctor # should report ffmpeg, ffprobe, Chrome OK
```
- Use `.venv/bin/python` for every Python tool in `tools/` (never the system python for numpy/scipy work).
- The shell tools in `tools/*.sh` are zsh scripts (`setup.sh` installs zsh on Linux).
- HyperFrames is pinned at **0.8.217** (package.json). Always call it as `npx --yes hyperframes@0.8.217 …`: a bare
  `npx hyperframes` silently fetches the newest release (0.8.222 on 2026-10-30). Its skills are installed by
  `npx hyperframes skills update`; as of 2026-10-30 that installs **`/hyperframes`, `/hyperframes-cli`,
  `/hyperframes-registry`, `/media-use`** (the older names `/hyperframes-core`, `/general-video`, `/hyperframes-animation`,
  `/hyperframes-audio` no longer exist — the composition contract is in `hyperframes/references/format.md`, grading/TV
  effects in `media-use/references/grading.md`). The skills describe the newest CLI (e.g. 30 fps defaults, `check`);
  this kit's own rules win (24 fps, `lint`, pinned version). Restart the session to load freshly installed skills.
- `setup.sh`'s `apt install` can fail with a dpkg error on cloud images; harmless when ffmpeg, ffprobe and zsh are
  already present (check `which ffmpeg zsh`).
- Cloud/sandboxed sessions may have restricted network access. If Instagram, archive.org, Wikimedia or the
  HyperFrames registry are blocked, say so to the user and continue with what's in the repo (all reels are
  already studied in `references/reels/`, all sample assets are in `assets/`).
- No GPU needed. Rendering 10 minutes took ~9 min on an M-series Mac; expect slower on cloud CPUs
  (render 4–10 s samples first; a full 10-minute render can take much longer — run it in the background).

- **Agent Reach** (`agent-reach`, installed by setup.sh from https://github.com/Panniantong/Agent-Reach) watches
  Instagram reels: its bundled yt-dlp is at `~/.local/share/uv/tools/agent-reach/bin/yt-dlp`
  (`yt-dlp -o reel.mp4 https://www.instagram.com/reel/<id>/`). Download → `ffmpeg … tile=8x6` contact sheet →
  `hyperframes transcribe` the reel's narration (tutorial reels explain their technique out loud).
- **zsh gotchas:** never name a shell variable `path` (it overwrites `$PATH`); `$i:a` inside strings is a
  path modifier — write `${i}`; `for p in "a b"` does not word-split — use `${=p}`.
- Wikimedia returns HTTP 429 for full-size originals under load: download standard thumbnail widths
  (`/thumb/x/xy/Name.jpg/1920px-Name.jpg`) with `tools/commons_thumb.sh "File name.jpg" out.jpg 1920`.
  Library of Congress / Chronicling America APIs were blocked (403/503); archive.org and Commons work.
  In claude.ai cloud sessions the **Commons API** (`commons.wikimedia.org/w/api.php`) can answer HTTP 429 to every
  request (shared datacenter IP) even with Full network access, while `upload.wikimedia.org` files still download:
  search with a pause between calls, or ask for the files through the fetch relay (§8.2).

## 2. Project layout

```
index.html              sample reel / master: mounts sub-compositions (generated by tools/build_index.py)
vo10.mp3                the voiceover (trimmed with -c copy — bit-identical)
transcript.json         word timestamps (npx hyperframes transcribe vo.mp3 --engine parakeet)
analysis/BEATS.md       beat sheet, ASR fixes, entities, key-word cues, fact check, story acts
EDIT_NOTES.md           per-beat edit plan (which effect, assets, cues)
lib/fx.css  lib/fx.js   THE STYLE: palette, fonts, typography classes, all effects (§4, §5)
compositions/*.html     one sub-composition per scene (templated). sNN-* = approved samples/templates
assets/                 fonts/ textures/ maps/ archival/ cutouts/ audio/ sfx/ (+ SOURCES.md per folder)
tools/                  build_index.py, render_samples.sh, sync_audit.py, halftone.py, commons_thumb.sh,
                        gen_s02.py (map generator), audio/ (sound generators)
references/             style-images/ (user's Pinterest refs), reels/ (contact sheets + notes)
```

## 3. Design system

### 3.1 Palette — defined once in `lib/fx.css :root`
| token | hex | use |
|---|---|---|
| `--paper` | #efe7d5 | light ground (charts, collage, newsprint scenes) |
| `--paper-2` | #e4d9c3 | panels on paper |
| `--ink` | #18222f | text/rules on paper (never pure black) |
| `--night` | #141312 | dark ground (cinematic, archival scenes) |
| `--bone` | #f4eee2 | text on night (never pure white) |
| `--vermilion` | #e5482a | primary accent: emphasis, **West**, bars, pins, markup circles |
| `--navy` | #23415e | secondary: **East**, water, cool fills |
| `--sky` | #a9c8de | light secondary (backgrounds, light East fills) |
| `--yellow` | #f2d33b | **only** the highlighter and the one key number of a scene |
| `--sepia-dark/light` | #2a2622 / #ede3cf | photo tint (duotone) |

Rules (why this works for editing): 60/30/10 — a neutral ground (paper or night) holds 60 %, ink and
grey photos 30 %, accent 10 %. Max two accents per frame. A colour always means the same thing across the
whole video (West/East), so the viewer learns the code once. Archival photos are desaturated/sepia so
accents pop. Alternate paper scenes (data, collage, documents) with night scenes (cinematic, archival,
titles) to give rhythm — never more than ~3 scenes in a row on the same ground.

### 3.2 Typography (classes in fx.css)
- `t-display` — Haskoy 800, tight: titles, big numbers, place names.
- `t-serif` / `t-serif-i` — Crimson Pro (italic for captions/"voice" lines, serif for chart titles).
- `t-label` — Cooper Hewitt 600, uppercase, tracked 0.18em: labels, kickers, sources, legends.
- Film-title finish (`halate`): halation glow (warm red-orange outer glows), 0.45px softness, grain from
  the overlay. Variants: `.halate.yellow` (key numbers), `.halate.cool`, `.halate.ink` (on paper).
- Paper scenes: crisp ink text (`t-ink`), `.label-box` (ink box + paper text, ref #1 "4%"),
  `.hl` highlighter span (animate `--hl` 0→1).
- Never declare `font-family` inside a composition's CSS (lint can't see fx.css @font-face) — use classes.
- Sizes: titles 64–300px, labels ≥ 22px, captions ≥ 38px. Keep 96px side margins.

### 3.3 Texture stack (Texturelabs — `assets/textures/`, see its SOURCES.md)
Normalise overlay textures to 50 % grey (`*_norm`) so blend modes add texture without shifting colour.
Blend by texture background: black bg → screen; white bg → multiply; normalised → overlay/soft-light.
Default stack on every scene (subtle!): `tx-grain` (grain_01_norm / grain_02_norm, overlay ~0.25–0.38,
jittered per frame by `FX.grain`) + `tx-dust` (dust_01/02/03, screen ~0.4–0.55, flipped every 2 frames by
`FX.dust`) + `.vignette`. Paper scenes add `paper-tex` (paper_cream_01, multiply) + `.folds`.
Print/newspaper adds halftone (halftone_01_norm overlay, or the canonical `halftone` treatment).

### 3.4 Changing or adding a texture (always from Texturelabs)
When the user asks for a different texture, it comes from **https://texturelabs.org** (free for commercial video
use, attribution optional; never redistribute the files publicly, never use them to train models).
1. Find candidates by category (`/category/grunge/`, `/category/paper/`, `/category/lensfx/`, …) or the site search.
   Each texture page is `https://texturelabs.org/textures/<name_NNN>/` and shows previews — read the pages with
   WebFetch / `agent-reach web read <url>` and pick 2–3 that fit (dark background = dust/scratches/leaks; light = paper).
2. **Downloading needs the site's own "Download" button** (it hands out a short-lived link). Do NOT script the site's
   download endpoint directly — that was blocked as circumventing the site. Use a browser tool if this session has
   one (click the large-size download, then fetch the link it gives). If no browser tool is available, give the user
   the exact page URLs and ask them to download the files and drop them in `assets/textures/_raw/` (or upload them).
3. Prepare each file: `.venv/bin/python tools/prep_texture.py assets/textures/_raw/<file>.jpg <descriptive_name>` —
   makes the 1920 px copy, hi-res copy and the 50 %-grey `_norm` version, and prints the right blend mode.
4. Add a row to `assets/textures/SOURCES.md`, swap the filename in the composition(s) (`.tx-grain`, `.tx-dust`,
   `.paper-tex`, halftone layers), keep it subtle (opacity rules in §3.3), snapshot before/after, and show the user.

## 4. HyperFrames rules that bite (read `/hyperframes` + its `references/format.md` once)

### 4.1 Composition skeleton (copy any `compositions/sNN-*.html`)
- Sub-composition = `<template>` containing `<style>`, the root `<div id="root" data-composition-id="sNN">`,
  and `<script>` (IIFE). The **head is discarded**. Prefix every id with the composition id (`sNN-…`).
- Asset URLs are relative to `index.html` (project root): `assets/...`, `vo10.mp3`.
- `index.html` loads gsap, `lib/fx.css`, `lib/fx.js` once (generated by `tools/build_index.py`).
- Each composition: `const tl = gsap.timeline({paused:true})` … `FX.mount(tl, DURATION)` …
  `window.__timelines["sNN"] = tl` (key = composition id = host id).
- Voiceover per scene: `<audio id="sNN-vo" src="vo10.mp3" data-start="0" data-duration="D" data-media-start="VO_START">`.
  For the full edit use one `<audio>` for the whole VO in index.html instead.
### 4.2 Determinism
- No Math.random/Date. Use `FX.rng(seed)`, `FX.noise2`. Per-frame procedural effects register with
  `FX.onFrame(fn)` *before* `FX.mount` (mount captures and resets the list per composition).
- Use `fromTo` with explicit start values; `immediateRender:true` for instant "appear" sets.
- A show/hide placed at timeline time **0** with `tl.fromTo`/`tl.set` may not render on frame 0 — set the initial state with
  `gsap.set(...)` outside the timeline (found by the intro02 editor, 2026-10-31).
- Opacity < 1 on a `preserve-3d` container flattens 3D (backface shows mirrored) — dim children instead.
- CSS `inset:` after `left/top` overrides them. Order matters.
- Never centre with CSS `transform: translateX(-50%)` on an element GSAP also moves — GSAP rewrites `transform` and the
  centring is lost (a label ran off-screen in the first full render). Position with left/width + text-align, or use `xPercent`.
- Map region overlays (mix-blend overlay on the desaturated basemap): on the dark satellite map of s02, West vermilion
  `#e5482a` at fill-opacity ≈ 0.6 (≥ 0.85 reads as a red slab, ≤ 0.45 turns brown); East uses the light East fill
  `--sky` `#a9c8de` at ≈ 0.8 (navy disappears under overlay on a dark map). On light/beige maps navy works.
- `mix-blend-mode` on any child of a `preserve-3d` container makes Chrome flatten the whole 3D context (layers lose their
  depth and land at the wrong place). Keep blended overlays (rays, haze with blend, grain) outside the 3D camera.
- A 3D-rotated element inside a `perspective` root can composite above its flat siblings (a scrim/shade drawn after it
  did nothing in s06). Put `perspective` on a dedicated wrapper that holds only the 3D layer.
- SVG filters: set `color-interpolation-filters="sRGB"`; `feTurbulence` output ranges are unpredictable —
  for threshold reveals use a pre-made equalised noise image via `feImage` + `feColorMatrix` alpha offset.
  Filters inside `<mask>` failed in Chrome — apply the filter to the shape directly (`feComposite in`).
- CSS `mask-image` uses the image's **alpha**: a greyscale (mode L) mask PNG such as `assets/intro/maps/taiwan_mask.png`
  masks nothing (the fill covered the whole frame in intro03). Convert it to white+alpha first (intro03:
  `assets/intro/derived/intro03/taiwan_mask_alpha.png`, made by `project/intro/gen/intro03_assets.py`).
- Country paths from the world JSONs (Russia, Fiji, …) cross the antimeridian: drop sub-paths with a > 400 px jump or they
  draw horizontal lines across the whole map when stroked.
- Lint 0.8.217 errors on tweening `letterSpacing` (layout snap) and on any `font-family` declared in composition CSS (also
  for credit lines) — animate scale/x instead and use the `t-label`/`t-serif` classes.
### 4.3 Check, look, render
```bash
python3 tools/build_index.py s05            # put one (or several) compositions in index.html
npx hyperframes lint                        # 0 errors before anything else
npx hyperframes snapshot --at 1,3.5,6 --no-end -o .snap/x   # LOOK at the frames (Read the PNGs)
tools/render_samples.sh s01 s05             # renders each, swaps in bit-exact MP3 VO (keeps mix if SFX)
```
Renders and snapshots both rewrite `index.html`: while a render runs in the root, snapshot in a sandbox
(`tools/make_sandbox.sh snap`, then `cd work/snap && python3 tools/build_index.py sNN --root .`).
Compare a render with the approved sample: `tools/compare_expected.sh renders/samples/sNN-x.mp4 expected/sNN-x.720p.mp4 out.jpg`.
Parallel editors: each works in a private sandbox so previews never collide —
`tools/make_sandbox.sh segNN` → `cd work/segNN && python3 tools/build_index.py segNN --root . && npx hyperframes snapshot …`
(compositions/, assets/, lib/ are symlinked; edit files in the main compositions/ folder).
Assembly: `python3 tools/build_master.py --out index.html` mounts segNN at `data-vo-start`, strips each segment's
`class="temp-vo"` slice, adds one continuous VO and the sound designer's `assets/audio/timeline.json` tracks.

### 4.4 Sync rule
Write every cue as `T(<voiceover seconds>)` where `const T = s => s - SCENE_VO_START;`, taking the word's
start time from `transcript.json` (or BEATS.md §4 key-word cues). Text should appear 0–120 ms before its
word; structural moves (exits, camera) may sit anywhere. Audit: `python3 tools/sync_audit.py compositions/*.html`.
Convention from the full edit: write **text** cues as `T(vo)` and **structural** cues (cuts, camera, exits, objects) as
`S(vo)` (same function) so the audit only checks words. The audit only sees **literal** `T(123.45)` calls — never write
`T(c)` over an array of numbers (those cues go unchecked); write the array as `[T(64.83), T(64.91), …]`. It also
matches each cue to the *nearest* word start, so a cue for a short word right after another can be reported against
its neighbour; and it only flags offsets outside −0.25…+0.12 s — read the list and make sure every text cue is ≤ 0.
Default: put the cue 0.06 s before the word. Longer lines are revealed **word by word**, each word on its own `T()`,
so no word is ever on screen before it is spoken (s03, s04, s06, s08, s11). A title like "The first class" lands on
its first spoken word ("the"), not on the key word. Long segments: one sub-composition per ~100 s, scenes as layers
gated by `FX.gate`, `display:none` outside their window (keeps the render's heavy-overlay count low).

## 5. Effect catalog (lib/fx.js API + where to see it)

Timing helpers: `FX.gate(a, b, fn)` wraps a per-frame fn so it only runs in its scene window (use it in every long segment). `FX.choppy(ease, dur, 12)` = "posterize time" (12 fps steps) — use on Vox-style moves,
bars, pops; keep camera moves smooth. `FX.split(el,'chars'|'words')`.

| # | Effect (user's point) | How | Example |
|---|---|---|---|
| 1 | B-roll matched to words | archival photos/film; plates with `.plate .img + .fringe` | s04–s10 |
| 2 | Animated charts/stats | paper aesthetic + refs §6; `FX.text.count`, bars with choppy scale, isotype grids, `.label-box` | s03, s01 |
| 3 | Maps | equirectangular basemap (`assets/maps`, NASA Blue Marble desat) + SVG paths in the same pixel space (`us_overlay.json`, x=(lon+128)*100, y=(52-lat)*100) inside a camera div; region fills `mix-blend-mode:overlay`; **burn reveal** = feImage noise (`burn_a/b.png`) + colour-matrix alpha threshold + charred ring (two thresholds, arithmetic composite); river `stroke-dashoffset` draw; pins + halos; satellite clouds + shadows drifting; foreground puffy cloud fly-through; camera push to the point of interest | s02 (`tools/gen_s02.py` + `tools/s02_template.html`) |
| 4 | Film-title typography | `.halate` classes + grain overlay | all |
| 5 | Newspapers/headlines | full-page scan on a tilted 3D page, sepia, halftone overlay that grows with zoom, camera push to headline, tinted blurred copy as background | s06 |
| 6 | Sound | §7 | — |
| 7 | Textures | §3.3 | all |
| 8 | Light streaks | `FX.streaks(canvas,{seed,speed,xfreq,lo,hi,gamma,tint,gain})` — fractal noise squashed into vertical streaks, evolving, levels crushed; canvas `blur(2.5px)`, opacity 0.3–0.7, screen | s01 |
| 9 | ~~Shutter~~ → **whip** (§10.1.6; Krish dislikes the iris) | was: `FX.iris(svg, {close:0.16, hold:2/24, open:0.28}).at(tl, cutTime)` (the default 0.2 s opening barely reads); swap shots exactly at the closed iris; shutter SFX ~0.15 s before (`<audio id="sNN-sfx-k" src="assets/audio/sfx/camera_shutter_mech*.wav" data-volume="0.3">`); a second, faster iris (`close:0.1, open:0.12`) for words < 0.6 s apart (New York → New Jersey); dark scrim at the bottom/top of bright plates so labels read | s05 |
| 10 | Vox layered backgrounds | 2–3 related images tinted with `FX.tintDefs(svg,id,dark,light)` (blacks→dark grey, whites slightly bright), offset/rotated panels with shadows, newsprint overlay, each drifting at its own speed; subject on top | s09 |
| 11 | Footage inside a vintage TV | transparent-screen TV PNG (`assets/textures/tv_frame_01.png`, screen bbox in `tv_frame_01_screen.json`), video under it with `data-color-grading='{"intensity":1,"adjust":{"saturation":-1,"contrast":0.1},"effects":{"chromaticAberration":0.35,"chromaticAngle":0,"scanlines":0.4,"scanlineCount":0.17,"scanlineSoftness":1,"crtCurvature":0.35,"filmArtifacts":0.45}}'` (keys: `npx --yes hyperframes@0.8.217 media-treatment --capability retro-glitch --json`); a black "tube" div behind the screen so the hole is dark before power-on; CRT power-on (scaleY 0.012→1 + white flash); glass glare. **Vary the TV** (find other sets, wood consoles, portable, 1930s radio-cabinet) | s04 |
| 12 | Collage / timelines | paper ground; photos tinted to the palette (`FX.tintDefs` ink→paper), halftone multiply, torn edges (`FX.roughDefs`), cards pinned with 12 fps stop-motion, timeline axis + travelling dot; Stanford→MIT swaps | s08 |
| 13 | Text animations (reusable) | `FX.text.fill` (yellow pop → settles to reading colour), `FX.text.random` (letters appear in random order), `FX.text.odometer` (slot-machine letters; reels lock to final glyph width), `FX.text.count` (numbers, 12 fps), `FX.text.rise` (blur-in). One text animation at a time on screen | s01, s04, s07, s09 |
| 14 | Old-footage gate weave + flicker | `FX.weave(el,{amp,flicker,seed})` on a wrapper | s07, s05, s11 |
| 15 | "Cutting the curve" match cut | `FX.curveCut(tl, wrap, a, b, t0, dur)` — both images in one wrapper share the expo.inOut zoom (12 fps); cut at peak velocity with a 2-frame blur | s07 |
| 16 | Hi-quality photo treatment | fringe blur (`.plate .fringe` radial-masked blurred copy), film dust, vignette, slow zoom | s07, s05 |
| 17 | 2.5D | cut the photo into depth layers (backdrop with subject removed + blurred, title layer, subject, foreground), place in a `perspective:1200px` stage; each layer is a full-frame plane (`inset:0`, origin 50% 50%) holding its image at the photo's own offsets (`layout.json` next to every layer set), set to `{z, scale:(P−z)/P}` so the rest frame equals the flat photo; fit the photo so the subject fills ~75 % of the width and fill side margins with a bigger, blurrier copy of the far plate; feather the cut edges of near layers (mask-image) so they never show as stickers; dolly camera (x drift ±150, z −80→150, rotationY ±3°); haze between layers, light rays, foreground blur (depth of field); title tucked behind the subject | s10 |
| 18 | Rough edges + highlighter | `FX.roughDefs(svg,id)` (boiling displacement at 12 fps) on text/paper; `FX.choke(tl, morph, t, from, dur)` = Simple Choker reveal (erode radius → 0, 12 fps); highlighter = yellow rect, multiply, rough filter, scaleX 0→1 choppy | s06, s04, s10 |
| 19 | **Vox markups** (circles, arrows, underlines, boxes, X) | `FX.markupDefs(svg,id)` (two stacked rough passes, 12 fps boil) + `FX.markup.circle/arrow/underline/box/cross(tl, svg, t, {…})` drawn on with dashoffset ("trim paths"). Put the svg **inside the camera layer** so marks track the photo | s11 |
| 20 | Map/document callouts | combine 19 with maps (circle a region, arrow to a pin, "look here first") | (use in edit) |

Cutouts: `npx hyperframes remove-background in.jpg -o out.png` works on people (soften halftone prints
with a blur first, then apply the matte to the original; it fails on buildings). Buildings: key plain skies
with `tools/halftone.py --sky-key`, or hand-draw a polygon mask (see garage layers in s10 / notes in §8).
`tools/halftone.py` renders any image as a 45° print dot screen (ref #1 look).

## 6. Reference layouts: turning the user's images into animated scenes

The user regularly sends reference images (Pinterest charts, maps, boards) and expects them to be **rebuilt as
animated scenes in OUR style** — our fonts, our palette, our textures, our Vox-style motion — never copied as-is
and never used as static pictures. The first batch is in `references/style-images/` (1–12). Every one of them
(except #3, which the user skipped, and #2, optional) was built in the approved 10-minute edit; the code is in
`templates/full-edit/segNN.html` (search the scene id) and a still of the result is in `expected/layouts/`.

| ref | look | build with | worked example (scene · file · still) |
|---|---|---|---|
| 1 | paper, vermilion bars with watercolour tops, dashed threshold, halftone building cutout, ink "4%" label box | bars scaleY at 12 fps, watercolour top via `assets/textures/watercolour_edge_mask_01.png`, `tools/halftone.py --sky-key` cutout, `.label-box` counter | SC013 · seg01 · `R1_SC013.jpg` (also `compositions/s03-gdp.html`) |
| 2 | (optional) duotone line chart over an engraved banknote | tint the note to navy/paper, SVG path draw-on, dot markers pop, value labels | not built yet — if used, animate the line draw + markers well |
| 3 | skip (user decision) | — | — |
| 4 | ranked bars topped with circular portraits/logos, ghosted building behind | bars + circle-masked cutouts (`remove-background`) or logos (`media-use resolve --type logo`), dashed threshold | SC006 · seg01 · `R4_SC006.jpg` |
| 5 | isotype pictogram grid | grid of `assets/icons/graduate*.svg` (or squares) filling in order, then moving | SC033 · seg02, SC078 · seg06 · `R5_*.jpg`, `compositions/s03-gdp.html` |
| 6 | horizontal bars, serif title with italic emphasis word | bars + `t-serif` title, emphasis word in vermilion italic | SC035 · seg03 · `R6_SC035.jpg` |
| 7 | line chart, shaded era band, end labels, annotations | SVG path draw-on, band fade, dot + label pops, bracket | SC029 · seg02 · `R7_SC029.jpg` |
| 8 | dot-matrix semicircle ("parliament"), highlighted headline phrase | dots placed on arcs, filled clockwise at 12 fps, `.hl` highlighter, leader labels | SC009 · seg01 · `R8_SC009.jpg` |
| 9 | cork board, pinned photos/notes, red string | `assets/textures/cork_01.jpg` (CC BY — credit), cards pinned stop-motion, string paths drawn on, lamp-pool lighting | SC066/SC074 · seg05 · `R9_SC074.jpg` |
| 10 | old street/topo map, yellow marker route, circle, numbered pin | `assets/maps/old/*` (with `.json` lon/lat→pixel), tilted plane, rough yellow marker draw-on (`FX.markup`), pin | SC053 · seg04, SC085 · seg06 · `R10*.jpg` |
| 11 | muted beige map, coloured regions, leader-line labels, big numbers | `assets/maps/us_beige.svg` (states as `#st-XX`), watercolour fills, leader labels, dotted route | SC017 · seg01 · `R11_SC017.jpg` |
| 12 | grey relief map, one region filled red with halftone + glowing edge | `assets/maps/*_relief_grey.jpg` + masks, region fill + halftone + glow; `tools/gen_relief.py` / `fetch_terrain.py` make relief maps for ANY country | SC075 · seg05, SC008 · seg01 · `R12*.jpg` |

### 6.1 Method for any NEW reference image (do this every time)
1. **Read the reference for structure, not style**: what kind of comparison it makes (ranking, share of a whole,
   trend, geography, connection, route), its layout grid, hierarchy, and the one "hero" element. Say this in one line.
2. **Translate the style to ours**: replace its fonts with Haskoy / Cooper Hewitt / Crimson Pro (§3.2); its colours
   with our palette tokens (§3.1 — map its main accent to `--vermilion`, its secondary to `--navy`, highlights to
   `--yellow`, its background to `--paper` or `--night`); add our texture stack (§3.3). Keep the layout idea.
3. **Use the narration's real numbers and words**, never the reference's content. Every label lands on its word (§4.4).
4. **Animate it with our Vox moves** (§5): elements build in the order the narrator explains them; bars/dots/icons
   at 12 fps (`FX.choppy`); lines and markups drawn on; numbers counted (`FX.text.count`); the key word highlighted
   or filled; a slow camera drift or push; a designed exit into the next scene. Never a static chart.
5. **Build it as a short sample first** (4–10 s on a real narration window), snapshot it, compare side by side with
   the reference image, and show the user before using it widely.
6. **Record it**: add a row to the table above (ref number, look, build, worked example) and save the reference
   image into `references/style-images/` with the next number, so future sessions can reuse it. Changelog line.
Vary every layout each time it's reused (different colour lead, orientation, density, entry animation).

## 7. Sound design (from the user's reference reel + rules)
- Bed: **marimba-led** documentary underscore (sits outside the voice's band, emotionally neutral, reads as
  "learning"). Adjacent textures: pizzicato strings/cellos/violin, light orchestra; layer soft strings or
  synth pads under it to feel modern. Free sources only (CC0/PD, CC-BY with credit, or synthesized — see
  `assets/audio/LIBRARY.md`). Music follows the story acts (BEATS.md §7) and turns on key moments.
- SFX on every object, subtle: whooshes on moves, paper slides on cards, pin pops on map pins, marker
  scratches on markups, highlighter swipe, ticks on counters/odometers, shutter clicks, projector loop on
  archival film, CRT click on TVs, low boom on big reveals, burn crackle on map burns, wind under clouds.
- Levels: VO untouched at unity; music ≈ −28…−32 LUFS under speech, may lift ~3 dB in gaps; SFX peaks far
  below VO. Details: `assets/audio/MIX_RULES.md` and `/media-use` (audio). (This VO measures −27.2 LUFS, so
  the bed is set relative to it instead: ~14 LU under the voice ≈ −41 LUFS.)

### 7.1 How to place sound (pipeline)
1. **Library** (`assets/audio/LIBRARY.md`): original synthesized score in cues + stems (marimba / pizz / pad),
   synthesized SFX, Kenney CC0 extras. Re-generate with `tools/audio/gen_music.py`, `gen_sfx.py`, `import_kenney.py`.
2. **Editors** write per-object markers in `compositions/segNN.sfx.json` (SEGMENTS.md §3.4 vocabulary;
   `t` = the frame the object event happens, loops/beds carry `dur`). Editors never add music.
3. **Sound pass**: `.venv/bin/python tools/audio/place_sound.py` renders three pre-mixed beds
   into `assets/audio/bed/` and writes `assets/audio/timeline.json`:
   - `music_bed_600s.wav`: cue sheet (`bed/music_cuesheet.json`, edit it to re-score) → `build_bed.py`;
     stems thinned where narration is dense (≥ 3.3 words/s); +1.5/+3 dB lifts in VO pauses (pauses
     found by READING the VO level; the VO itself is never processed); dynamic carve (−3 dB @ 2.5 kHz,
     −2 dB @ 1 kHz while the voice speaks); normalized to −41 LUFS.
   - `sfx_600s.wav`: every marker → a sound (most generated per event with a unique seed so repeats never
     sound identical), placed sample-accurately at `t − sync_offset`, at the MIX_RULES level. Audit trail:
     `bed/sfx_placements.json`.
   - `ambience_600s.wav`: projector / CRT hum / wind markers + room tone everywhere, vinyl under sepia/weave
     scenes, wind under cloud scenes.
4. `python3 tools/build_master.py` mounts the three beds at volume 1.0 next to `vo10.mp3` (three `<audio>`
   tags total: hundreds of per-SFX tags overload the renderer, so always pre-mix).
5. Check: test mix with ffmpeg (`amix=normalize=0`), measure VO-alone vs mix (should differ by < 1 LU),
   then render and listen. If a segment's timing changes, edit its `sfx.json` and re-run step 3 (~3 min).

## 8. Pipeline for a new 10-minute edit (agents)
1. **Setup**: §1; `hyperframes init`; trim audio with `-c copy`; transcribe (parakeet).
2. **Analyst agent** → `analysis/BEATS.md` (beats 4–12 s, ASR fixes, entities with timestamps, key-word
   cues, story acts/tone). No fact-checking: on-screen text follows the narration.
3. **Edit-notes agent** → `EDIT_NOTES.md`: for each beat: effect(s) from §5/§6, ground (paper/night),
   on-screen text (exact, with word cue times), assets needed (search terms, preferred sources), SFX cues.
   Coverage table proving every effect and reference layout is used, with variations; no effect twice in a row.
4. **Asset agent(s)** → `assets/...` + SOURCES.md (licence + URL for each), cutouts, halftones, layers.
5. **Editor agents** (parallel, by time segment) → `compositions/segNN.html`, following §3–§5 and copying
   the closest sample; snapshot every scene; `sync_audit`.
6. **Sound agent** → bed + SFX placed from the compositions' cue times (index.html audio track list).
7. **Assembly + QA**: index.html mounts segments back to back with the single VO; lint; snapshot sheet of
   every scene midpoint; render; watch for sync, readability, repetition; fix; re-render.

### 8.1 Sourcing playbook: archival photos, footage, newspapers, documents, B-roll
**Rule:** free sources only — public domain, CC0, CC BY / CC BY-SA (credit on screen + in SOURCES.md). No logins,
no paid stock, no watermarks, never BBC/Getty/AP. Match the narration exactly: right person, right place, right era.
Search: `python3 tools/find_media.py commons|archive|archive-texts|files "<query>"` (prints licence + size + URL).

| need | go to (in this order) | how |
|---|---|---|
| historical photos of people, places, buildings, events | Wikimedia Commons (huge PD set incl. Library of Congress, NARA, Smithsonian, Bain, Harris & Ewing, Detroit Publishing copies) → archive.org → NYPL Digital Collections → Smithsonian Open Access → Openverse (CC filter) | `find_media.py commons`; download with `tools/commons_thumb.sh "File name.jpg" out.jpg 1920` (widths 960/1280/1920/3840 work; originals and 2560 often fail with 429/400; sleep a few s between requests) |
| archival film / B-roll footage | archive.org: Prelinger Archives, NARA/Universal Newsreels, Ford Motor Co. collection, California Revealed (`copl_*`), home movies collections | `find_media.py archive "<topic> 1930s"` → `find_media.py files <id>` → `curl -L -o x.mp4 https://archive.org/download/<id>/<file>`; make a contact sheet (`ffmpeg -vf fps=1/4,scale=320:-1,tile=8x8`) to find the best 6–20 s; trim with ffmpeg to h264 ≤1080p, 24 fps, no audio. YouTube/other public-domain uploads: `agent-reach youtube search` + its yt-dlp, only if clearly PD/CC |
| old newspapers / front pages | archive.org (NYT and other scanned runs; search `archive-texts`), Chronicling America (LOC — often blocked from servers; try once), Commons | full-page scans ≥3000 px; record headline bounding boxes in SOURCES.md for the highlighter |
| books, yearbooks, documents, charters, bulletins | archive.org texts (university yearbooks, bulletins, books like Terman 1916), HathiTrust (full view = PD) | grab the page image (`files <id>` → `.jp2`/`.jpg`/page PDF → render the page). Can't find it? make a **typeset recreation** in our fonts on paper texture — never fake signatures, seals or official marks |
| period maps | USGS historical topo (PD), Library of Congress maps via Commons, David Rumsey only if CC BY (not BY-NC) | keep a `.json` with corner lon/lat → pixel formula next to each map |
| modern photos of places/companies | Commons (check licence: many are CC BY-SA → on-screen credit) | |
| logos | `npx hyperframes media-use resolve --type logo --entity "<Company>" --intent "<Company> logo" --project .` → `assets/logos/`; fallback Commons | |
| cutouts, halftones, 2.5D layers | `npx hyperframes remove-background` (people; blur halftone prints first), `tools/halftone.py`, hand polygon masks (`tools/cut_layers.py`) | see §5 #17 and the 2.5D layer sets in the full edit |
| textures | Texturelabs — §3.4 | |
| sound | §7 (synthesized score + SFX, Kenney CC0) | |

Every asset: look at it (Read the image / contact sheet) before using it; reject wrong subject, wrong era,
watermarks, low resolution (<1600 px long side for full-frame). Log it in the folder's `SOURCES.md`: subject, URL,
licence, author, date, dimensions (+ bboxes for documents). Mark it in `ASSETS_NEEDED.md` (✅ / 🔁 substitute / ❌).
When nothing real exists, use the closest true substitute and say so, or a typographic/graphic treatment — never a
blank and never an invented "archival" photo. Run several gatherers in parallel split by asset type (photos+logos+
cutouts / documents+footage+props / maps+layers+icons) — `example-docs/ASSETS_NEEDED.md` shows the format.
**Library of Congress (LOC):** its search site / JSON API (`www.loc.gov/...?fo=json`) refuses all scripted requests
(even from a home Mac — bot protection), but its **image servers work**: `tile.loc.gov` and `cdn.loc.gov`. Workflow:
find the photo on Wikimedia Commons (`find_media.py commons "<query>"` — LOC collections such as Detroit Publishing,
Harris & Ewing, Bain, Prints & Photographs are mirrored there; the file page gives the LOC call number / URL, e.g.
`https://www.loc.gov/pictures/item/2016800114/` or a `cph`/`det`/`hec` reproduction number), then download the
full-resolution file directly from the image server, e.g.
`https://tile.loc.gov/storage-services/service/pnp/det/4a20000/4a26000/4a26300/4a26364v.jpg` (pattern:
`/service/pnp/<collection>/<group>/<subgroup>/<id>v.jpg`; `v` = large JPEG, `r` = reference, `u` = uncompressed TIFF).
Prefer these over Commons thumbnails when you need more resolution. If you need LOC's own search, ask the owner to
search loc.gov in his browser and send the item links. Chronicling America newspapers now live on loc.gov — reach
them the same way, or use archive.org newspaper scans.
Other known blocks: Wikimedia 429 under load (throttle, use thumbnails).

### 8.2 When a site is blocked from a cloud session: the fetch relay
First make sure the cloud environment has **Full** network access (`CLOUD_SETUP.md`). If a source still refuses the
server (Instagram, Wikimedia rate limits, LOC), don't settle for worse media: add an entry per file to
`requests/fetch.json` (kinds: commons / url / instagram / youtube / texturelabs — format in `tools/fetch_relay.py`),
commit, push your branch, and tell the owner: "run `python3 tools/fetch_relay.py <branch>` on your Mac". It downloads
with the same sources, splits files over 95 MB, commits and pushes; you `git pull` and continue. Keep working on
other scenes while you wait.

### 8.3 Sound assets are regenerated, not stored
`assets/audio/music/` (≈620 MB of WAV) is not in the repo: `.venv/bin/python tools/audio/gen_music.py` rebuilds the
exact same score byte-for-byte in about a minute (setup.sh does this). The placed beds (`assets/audio/bed/`) are
built per project by `tools/audio/place_sound.py`.

## 10. Krish's round-2 rules (2026-10-31) — apply to every new edit

### 10.1 Critique of the rebuilt samples (fix everywhere)
1. **Glow (halation) is used intentionally.** `.halate` only on the ONE hero title or key number of a night scene
   (e.g. "12", "1891", "PALO ALTO"). Kickers, labels, captions, sub-lines and word-by-word narration lines use `.clean`
   (crisp bone + soft legibility shadow). Paper scenes never glow. If two things glow in one frame, one is wrong.
2. **Rough/boiling text must settle.** The roughen + 12 fps boil is a *reveal*, not a state: use
   `FX.chokeSettle(tl, morph, el, t, from, dur, cleanFilter)` — the edge boils while it chokes in, then the element
   gets a clean filter one 12 fps step later. Only permanent boil: hand-drawn markups and torn paper edges.
3. **Every visual matches the words being spoken at that moment.** No "mood" visuals over a line that says something
   else (e.g. a title card over "I don't think I need to tell you much"). Rhetorical/filler lines get a visual that serves
   the sentence they belong to, the narrator on camera (intro only), or the previous image held — never an unrelated scene.
   The edit plan names, for every shot, the exact words it covers and why that image fits them; QA reads the contact sheet
   with the transcript under each frame (§9). Krish's example was s04: the narration is "a student studying at Stanford
   or UC Berkeley … in the 1920s … opportunities in the West were scarce" but the screen showed a 1932 Berkeley commencement
   and a diploma — graduation footage under "scarce opportunities", wrong decade, wrong school. The footage must show
   what the line says (empty job boards / closed factories / a quiet 1920s West vs. a busy East), or the line gets a
   typographic/graphic treatment instead.
4. **One palette per video, researched for that story** — `lib/palette.css` (loaded after fx.css by build_index /
   build_master; same token names so every effect keeps working). Swatch + meaning in `references/palette_<video>.png`.
   Current video (Taiwan chips): red = TSMC/Morris Chang, blue = UMC/Robert Tsao (their real brand colours), celadon =
   Taiwan itself, yellow = highlighter/key number, everyone else neutral. Max two accents per frame. (Approved by Krish 2026-10-31.)
5. **Smooth Vox easing everywhere** (reel `DLQ4Wp9pqv3`, studied in `references/reels/REELS.md` → *ease*):
   velocity jumps up at once and decays over a long tail — entrances 1.0–1.6 s, moves 1.2–2 s, still posterized to 12 fps.
   Use `FX.ease.out` (entrances/pops), `FX.ease.inOut` (A→B moves), `FX.ease.in` (exits), `FX.ease.cam` (camera, never
   posterized), always wrapped: `ease: FX.choppy(FX.ease.out, dur, 12)`. Banned from now on: `back.out` overshoots,
   `power2/3.out` under 0.6 s for anything bigger than a label, `expo.inOut` for anything but the cutting-the-curve zoom.
   Same reel: Vox keeps a light chromatic aberration over everything (photos/footage: `data-color-grading`
   `effects.chromaticAberration` 0.1–0.15) and never uses flat solid colour — every fill sits under a texture.
6. **No iris shutter any more.** Image-to-image transitions are **whips** (reel `DdEHRimiG8Q`): `FX.whipDefs(svg,id)` on each
   shot + `FX.whip(tl, a, b, t, {dir, vertical, blurA, blurB})` — ~0.32 s, outgoing smears off with heavy directional blur,
   incoming smears in from the same direction and lands sharp; both overscale so the frame is never empty; whoosh SFX.
   The same reel also uses (a) a **hard cut on action** between two moving shots and (b) a **light-flash whip** (the smear
   passes through a bright frame) — vary the three. Never the same transition twice in a row.
7. **Better screens for footage.** Don't reuse the four museum TVs by default. Pick the screen for the story and era:
   1980s Taiwan → Tatung TVs (Taiwanese maker), Sony Trinitron, IBM PC 5150 / Apple II / terminal CRTs, cleanroom monitors,
   oscilloscopes, VCR-era sets, projector screens. Prefer real PD/CC photos with the screen keyed transparent
   (`*_screen.json`), TVs first because they look best, but anything with a screen that fits the line is allowed.

### 10.2 New techniques (from Krish's reference posts)
- **Cut on action** (`DOb0h6VCSpM`): every cut lands while something is moving — a bar rising, a camera push, a card
  sliding — so the eye is tracking motion and doesn't see the edit. Punch in (1× → 2×) / out mid-move to extend a scene.
  Never cut on a still frame. Plan each scene's last 6 frames as motion that the next scene continues.
- **DSLR focus hunting** (`DLdy8b5JpHC`): `FX.focusHunt(tl, el, t, {dur:0.8})` = box blur 0 → 4 → 6 → 0 px, right after a
  fast zoom or big move lands (photo cards, maps after a push, 2.5D dolly stops). Adds spatial realism; once per scene max.
- **Markups/callouts deep dive** (YouTube `CqHb6bVoxgI`, Chris Moran "How VOX Directs Your Attention") and **Vox sound
  design system** (YouTube `UgVgzSZVu-8`) — YouTube blocks the cloud IP; requested through the fetch relay
  (`requests/fetch.json`). Notes go here once studied.

### 10.3 Sound (round 2): Epidemic Sound, layered
Krish has an Epidemic Sound subscription: the **entire music bed comes from Epidemic Sound** (SFX may also come from other
free sources). Vibe reference: "Melting Glass" (Epidemic) — documentary, textural. Never one music track: build the bed in
layers (e.g. pad/drone + pulse + melodic layer + texture, using Epidemic **stems**), entering/leaving with the story beats.
Reference playlist (Krish, "Documentaries", 13 tracks + stems, saved in `references/audio/epidemic_playlist_documentaries.json`):
Melting Glass (Eden Avery, 134 bpm, contemporary classical, restless/sentimental) is the anchor; also Formations (Van Sandano,
dark pulses), Terms of Gravity, Imber, City Phases, Chrysotile (drone), Ostinato, Misguided Path, When Warriors Align…
— contemporary classical / pulses / drones, medium energy. Most have stems (bass, drums, instruments, melody).
**Access:** the official **Epidemic Sound MCP server** (`.mcp.json` in this repo → https://www.epidemicsound.com/a/mcp-service/mcp,
auth `Authorization: Bearer ${EPIDEMIC_SOUND_MCP_API_KEY}`). Krish creates the key at epidemicsound.com/account/api-keys and
stores it in the cloud environment as `EPIDEMIC_SOUND_MCP_API_KEY`; a new session then has `SearchRecordings`,
`SearchSimilarToRecording`, `DownloadRecording` (stems from the original track), `EditRecording` (cut to length),
`SearchSoundEffects`, `DownloadSoundEffect`. Downloads use his paid subscription (no new licence). Never use the public
low-quality preview MP3s in an edit. **Working (2026-10-31):** `python3 tools/epidemic_fetch.py <kosmosId> <name> FULL BASS
DRUMS INSTRUMENTS` → `assets/audio/epidemic/<name>/` (48 kHz WAV, gitignored — licensed to Krish's subscription; re-download
any time). The kosmosId of every playlist track is in the saved playlist JSON. Stem types via the API: FULL, BASS, DRUMS,
INSTRUMENTS (no MELODY download — derive it as full − bass − drums − instruments if needed). `tools/epidemic_mcp.py` is the
bare client (list tools / call any tool) for sessions that haven't loaded `.mcp.json`; key from env or `~/.secrets/epidemic_key`. Fallback without the key: Claude lists tracks/stems in `requests/epidemic.md`, Krish
downloads them into `assets/audio/epidemic/`. VO stays untouched; bed far under the voice.

**Phase-1 tooling (2026-10-31, intro):** downloads through the agent proxy get reset mid-file — `epidemic_fetch.py` now
resumes with curl (`-C -`, retries) and only accepts a WAV whose size matches its header; re-running finishes broken files.
SFX: `python3 tools/epidemic_sfx_fetch.py <id> <name> …` → `assets/audio/epidemic/sfx/`. Measure every track with
`.venv/bin/python tools/audio/epidemic_analyze.py` (LUFS per stem, 1 s short-term curve → quiet/build/peak sections, key
estimate — the API gives no key) → `assets/audio/epidemic/ANALYSIS.md`; derive MELODY with `tools/audio/epidemic_melody.py`
(full − other stems; fails when the master is limited, e.g. Anytime Soon). Pick tracks in one key family and put a tempo-free
drone/pad under the joins; only one rhythmic track at a time. Measure each VO (`vo_intro.mp3` = −24.1 LUFS, not −27.2) and set
the bed ≈ 14 LU under it. Run heavy audio jobs one at a time (the container OOM-restarts). Worked example: `project/intro/SOUND_PLAN.md`.

### 10.4 The Taiwan long-form edit (4 h 26 min) — workflow
- Inputs: `bash input/join.sh` → `input/Final Full Audio.mp3` (VO, 4:26:xx) and `input/Face Cam.mp4` (4:35, 29.97 fps).
  The first ~275.5 s of the full audio **is the face-cam take** (cross-correlation 0.96, face cam = full audio − 0.026 s).
  Intro VO = full audio 0–275.5 (`-c copy`); face-cam video is synced at media offset +0.026 s.
- **Intro rules:** narrator NOT on camera for the first 10 s (VO + edit only). After that the edit still dominates; the
  face cam appears **5–6 times, 1–3 s each**, on lines where he addresses the viewer (~171 "Guess who…", ~196 "That's the
  story…", ~246 "I'm your host, Sam", 251–270 the "face built for radio / camera lights" joke — allowed, still in 1–3 s pieces).
  Face cam stays **clean and modern** (no film grade/texture on him). Allowed on top of / around him: our text treatments, and
  **graphics behind him**: `npx --yes hyperframes@0.8.217 remove-background clip.mp4 -o fg.webm -b bg.webm` (≈0.7 fps on
  CPU; clean matte incl. mic) → layer order: room plate (bg.webm) → our chart/map/newspaper with the usual animations →
  narrator (fg.webm) → text.
- **Spelling:** on screen always the accurate spelling of every name/place, even when the narrator mispronounces it.
- Chunks: intro (~4.6 min), then the rest in **10-minute chunks**; each chunk is approved before the next. Krish sends
  Pinterest references per chunk → rebuild each with §6.1.
- **Within one chunk, never use the same photo or clip more than twice** unless the story truly needs it (track usage
  in the chunk's ASSETS list).
- ASR name fixes so far: Robert Tsao (ASR "Robot Cao", "Sao", "Xiao"), Morris Chang, TSMC, UMC, Hsinchu Science Park
  ("Shin Shu Park"), host "Sam", show "Searching Lessons" (check spelling with Krish).

### 10.5 Round-3 rules (Krish, 2026-10-31)
- **Paintings, oil paintings, illustrations and vintage posters are B-roll too** — same rule as photos: they must match the
  words. A colour painting of a famous figure often beats a B/W photo; pictorial maps (e.g. 1950s illustrated California maps)
  can stand in for maps. PD/CC/free only, logged. Examples Krish sent: illustrated California maps, Wild West poster art,
  a pictorial "Palo Alto — birthplace of Silicon Valley" map.
- **Vintage grid / ruled paper grounds** (Texturelabs `paper_graph_01`, `paper_lined_01`, `paper_stained_01`,
  `paper_torn_01` (Screen), `paper_blueprint_01` + the look of Creative Market "Vintage Ruled Grid Paper Textures" — reference only, not
  bought, never re-drawn as vector): real scans — archive.org `kecatalog` (K+E Graph Sheets Catalog 1960), old ledgers,
  engineering notebooks, Texturelabs paper. Files in `assets/intro/papers/` (and later a shared `assets/textures/papers/`).
- **Vintage instruction manuals / datasheets** of the era (archive.org, bitsavers) are prime visuals for tech topics.
- **Per-chunk reference packs**: Krish sends Pinterest refs per chunk (Drive folder → `references/style-images/<chunk>/Dnn.jpg`).
  Use as many as the narration allows; unused ones carry over to the next chunk; a layout may repeat (varied). For scenes he
  didn't supply, find similar Pinterest-style references yourself and note them in the plan.
- **Access from this cloud machine (2026-10-31):** Commons API 429 → `find_media.py commons-html` (HTML search works);
  YouTube ("sign in, not a bot"), Vimeo ("couldn't verify your connection") and Instagram (anonymous rate limit) block the
  datacenter IP even in a headless browser → list them in `requests/fetch.json` (fetch relay) or ask Krish to download and
  push them to `references/reels/raw/`. Google Drive public folders work (`embeddedfolderview?id=` + `drive.usercontent`).
- Multi-agent intro pipeline as in AGENT_BRIEFS (analyst ∥ gatherers A/B/C ∥ sound designer → planner → editors → sound
  placement → assembly/QA). Chunk files: `project/<chunk>/`, compositions `introNN` / `cKsNN`; build with
  `tools/build_master.py --prefix intro --vo vo_intro.mp3 --len 275.06 --timeline assets/audio/intro/timeline.json`.

### 10.6 Markups & call-outs — Chris Moran "How VOX Directs Your Attention" (`references/reels/videos/markups_callouts_youtube.mp4`)
Goal: guide the eye exactly where the narration is. One call-out at a time; pick the type by the material:
1. **Two paper layers**: when a document/paper ground is used, stack two paper scans, the top one at ~90 % opacity so the
   page behind bleeds through (more real than one flat texture).
2. **Pen / pencil markups** (`FX.markup.pen`): freehand polyline with nudged points — never a clean end-to-end line —
   ~5 px stroke, `multiply` so it bleeds into the paper and over the print, rough edge ≈ 0.7× stroke width
   (`FX.markupDefs(svg,id,{boil:4})` — pens boil 4×/s; markers/chalk 12), drawn on in ~1 s with a slight ease (trim paths),
   whole thing posterized 12 fps. Draw it OUT by trimming the start (`FX.markup.out`). Arrows: same pen, draw-on then out.
3. **Contrast call-out** (`FX.contrastCallout`): a lifted-blacks veil (faded paper colour) over everything except a
   feathered region (country, district, paragraph). It appears as a **hard cut**, timed to the peak velocity of an ease-in
   camera push (cut on the curve), + a short label + texture parented to the camera + a **circuit-breaker "clunk"** SFX.
4. **Text contrast call-out** (`FX.textCallout`): the paragraph fades to ~20 % while the frame punches in ~10 %, then only
   the key words return at full strength through a feathered left→right wipe, a beat after the zoom.
5. **Focal call-out** (`FX.focalBlur`): sharp circle, everything else softly blurred (compound blur by a radial gradient);
   move the sharp spot across the map/document as the narrator moves on — long, extreme easing.
6. **Highlighter** (Vox staple, use sparingly): only on **body-size text**, never on a big headline (a real highlighter tip
   can't cover a header in one stroke); stroke ≈ text x-height (~25 px at 1080p), multiply, constant-ish speed (mild ease, so
   it reads along), one stroke per line staggered, two displacement passes (small/strong = rough edge, large/weak = wobble).
7. **Radio-wave rings** (`FX.radioWaves`) from a point on a map (station, factory, city emitting influence): rings thick →
   thin (sawtooth), optionally on a flattened 3D plane, with a focal blur + light chromatic aberration.
Sound the call-outs: pen = marker/pencil scratch, contrast cut = circuit-breaker clunk, highlighter = swipe.

### 10.7 Painting-to-print reveal — Lincoln reel (`references/reels/videos/lincoln_newspaper.mp4`, 0–5 s)
Open full-frame on a **colour painting** of the person (word-by-word serif captions over it), then an eased ~1.2 s
**pull-back + upward pan** reveals the painting is a picture printed in a **newspaper column**: thin rule frame, small caps
caption under it ("MR. LINCOLN AND THE FLAG."), then a bold serif **pull-quote** of what the narration quotes, then body
text and neighbouring columns (sepia newsprint, halftone, slight tilt). The **pull-quote is underlined word by word in sync
with the spoken quote** (pen underline drawn on per word). The page is a **typeset recreation** (Crimson Pro / Haskoy, our
palette) — never a fake real masthead/date of an existing paper. Camera keeps a slow pull/drift afterwards; next scene cuts
on action. Use it whenever the narrator quotes someone or introduces a historic figure with a quote.

### 10.8 Sound design system — Chris Moran "The VOX Sound Design System" (`references/reels/videos/sound_bed_youtube.mp4`)
- **Library in six folders**: mechanical, tech, tactile, ambient, whooshes, miscellaneous (`assets/audio/sfx/<folder>/`).
- **Hierarchy & restraint** (overrides "SFX on every object"): in each scene sound only the most important thing that
  happens (the hero element / the big move); ignore small text and arrows when they'd compete. Bigger, bolder = louder.
- **Every camera move / push / element entrance gets a (low) whoosh**; stack a texture on top (paper movement under a
  card, book-slide for a sliding panel, cloth for collapsing panels, stopwatch ticks for a fast chart line, keyboard/click
  for UI, projector hum for film-themed scenes, a subtle digital texture for pixel effects).
- **Variation**: never the same sample twice in a row — pitch/rate-shift it (±1–3 semitones) or pick another take.
- **Timing**: SFX may sit a few frames off the motion (fits the 12 fps stop-motion feel); a scene's first SFX can lead
  the picture by a few frames (**J-cut**) so the brain is primed.
- **Ambience** per scene theme, very low (room tone, projector, factory hum, cleanroom air, restaurant murmur).
- **Levels**: dialogue peaks ≈ −6 dBFS (our VO stays untouched — we measure, never change it), music ≈ −20 dBFS
  (≈ 12–16 LU under the voice), SFX −10…−20 dB below the VO depending on importance. **Frequency pocket**: a (dynamic) EQ dip
  on the MUSIC bed in the voice band (≈ 1–4 kHz, −3…−6 dB while he speaks) — "make room for vocals". Never EQ the VO.

## 9. QA checklist
- [ ] VO identical to source (same level; no processing). [ ] Every text cue within 0–120 ms before its word.
- [ ] Only the three fonts. [ ] Palette only; West=vermilion/East=navy. [ ] ≤ 2 accents per frame.
- [ ] Every effect + reference layout used; no repeat back-to-back. [ ] On-screen claims match the narration.
- [ ] Textures subtle. [ ] SFX on objects, quiet. [ ] Credits for CC-BY assets.
- [ ] Every shot matches the words under it (§10.1.3). [ ] Glow only on the hero element. [ ] No boil after a reveal.
- [ ] Smooth long eases, 12 fps. [ ] Cuts on action; whips, no iris. [ ] No photo/clip used > 2× in a chunk.

## Changelog
- 2026-10-31 — intro03 editor: §4.2 gotchas (greyscale masks need alpha for CSS mask-image, antimeridian country paths, lint on letterSpacing tweens / font-family in credits).
- 2026-10-31 — 5 Texturelabs papers added by Krish (assets/textures/paper_{graph,lined,stained,torn,blueprint}_01, SOURCES.md
  "Added 2026-10-31"). Intro usage: graph → export bar chart IS007–008 (D01) + one intro03 chart; stained (multiply) →
  profits/crash line chart IS010–011 (D05) and Chang-vs-Tsao bars IS052 (D02); lined → board / "one condition" / approval
  chain (IS024–027); blueprint → "breaks ground across the street" (IS037–038); torn (Screen) → torn-paper wipe at 185.01 and
  the historic-images collage IS064 (D07). Rule: two paper layers (top ~90 %), never the same paper in consecutive scenes.
- 2026-10-31 — Krish's reference videos studied: §10.6 markups/call-outs (FX.markup.pen/out, FX.contrastCallout, FX.textCallout,
  FX.focalBlur, FX.radioWaves, pen boil 4/s), §10.7 painting-to-print newspaper reveal (Lincoln reel), §10.8 sound design system
  (six folders, hierarchy/restraint, whoosh+texture stacks, variation, J-cuts, levels, frequency pocket).
- 2026-10-31 — §10.3: Epidemic phase-1 tooling (resumable fetch, SFX fetch, stem analysis, derived melody), intro sound plan.
- 2026-10-31 — §10.5: paintings/posters as B-roll, vintage grid papers, manuals, per-chunk Pinterest packs, cloud access notes; intro pipeline launched.
- 2026-10-31 — Krish round 2: §10 added (intentional glow, settle-after-reveal, words↔visual rule, per-video palette
  `lib/palette.css` + Taiwan palette, Vox long-tail easing `FX.ease.*`, whip transitions `FX.whip` replace the iris, cut on
  action, DSLR focus hunt `FX.focusHunt`, better screens, Epidemic layered bed, long-form intro/chunk workflow).
- 2026-10-30 — Rebuild test (new cloud session): all 11 samples rebuilt from the docs (originals in `_approved/`). Learned
  and fixed: pin every CLI call to 0.8.217 (`render_samples.sh` used the newest release; s11 added to its defaults);
  current skill names (§1); Commons API 429 in cloud sessions (§1); sync audit only sees literal `T()` cues + word-by-word
  reveals (§4.4); s02 template cues were late (WEST +0.02, Mississippi label +0.28, Eli Lilly +0.58 s) and its fills
  off-palette — template now uses `S()` for structure, vermilion 0.6 / sky 0.8 (§4.2); blend modes flatten
  `preserve-3d` and 3D layers can sit above flat siblings (§4.2); TV grading payload (§5 #11); iris opening 0.28 s
  (§5 #9); 2.5D fitting/feathering (§5 #17) + `assets/archival/hp/layers/layout.json` (offsets were missing);
  `tools/compare_expected.sh`; snapshot in a sandbox while rendering (§4.3).
- 2026-10-29 — v1: samples s01–s10; palette locked; markups (s11) added from the Vox markup reel; paper-
  aesthetic chart (s03) from the user's Pinterest refs; sound brief from the Vox marimba reel; sync audit tool;
  halftone tool; verified 12 trillion-dollar companies for the map.
- 2026-10-30 — LOC: search API blocks all scripts, image servers (tile/cdn.loc.gov) work — workflow in §8.1; network check updated.
- 2026-10-30 — §8.2 fetch relay + CLOUD_SETUP.md (Full network, timeouts), §8.3 music regenerated by setup; USER_BRIEF.md (verbatim brief), AGENT_BRIEFS.md, SOURCES_INDEX.md + example-docs/sources/, expected/final_edit_720p.mp4.
- 2026-10-30 — §8.1 sourcing playbook + tools/find_media.py (Commons/archive.org search).
- 2026-10-30 — §3.4 added: how to fetch new Texturelabs textures (browser download or ask the user) + tools/prep_texture.py.
- 2026-10-30 — §6 rewritten: worked example + still for every reference layout, and the method for new reference images (§6.1). Map/relief/old-map assets added to the repo.
- 2026-10-30 — packaged as a GitHub repo (vox-edit-kit): setup.sh for Linux/macOS, portable .venv paths, expected/ previews of the 11 approved samples.
- 2026-10-29 — final 10-min render with sound: renders/taiwan_first10_final.mp4 — a 720p copy is in expected/final_edit_720p.mp4 (VO −27.2 LUFS, identical to raw). Map-heavy segments are generated from templates: templates/full-edit/generators/seg01/gen_seg01.py and seg03/gen_seg03.py (edit the template, re-run). Sound: tools/audio/place_sound.py rebuilds all three beds from compositions/segNN.sfx.json.
- 2026-10-29 — full 10-min edit built by 6 parallel editors (94 scenes, 600 s); first full render 8m47s on this Mac.
- 2026-10-29 — FX.choppy now ceil-steps (no 1/12 s delay at the start); FX.gate added (from seg01/seg06 editors).
- 2026-10-29 — user: no fact-checking; on-screen text follows the voiceover as spoken.
- 2026-10-29 — sound pass: `tools/audio/place_sound.py` pre-mixes music / SFX / ambience into three 600 s beds (assets/audio/bed/, timeline.json); §7.1 added; this VO is −27.2 LUFS so the bed sits ~14 LU under it (−41 LUFS).
- 2026-10-31 — Added 5 Texturelabs papers (graph, lined, stained, torn/folded, blueprint) to assets/textures (SOURCES.md). How the download works in a browser tool: click the size button (lg), the page POSTs to admin-ajax.php and gets back a `downloadlink` (signed S3 URL, valid 20 min) — fetch that URL. prep_texture.py now accepts a file that is already in `_raw/`.
