# US vs Cartels motifs — THE DEAL, TARGET FILE, DATE TAG, CREDIT (build once, paste everywhere)

These graphics recur across the video and must look identical in every segment. They live in the kit, not in your file:
`lib/ct_motifs.js` (defines `window.CT`) + `lib/ct_motifs.css` (classes `ctm-*`). `tools/build_index.py` / `tools/build_master.py`
load both (after fx.js / palette_cartels.css) for every composition whose id starts with `ct`, so you add an empty `<div>` and call
the API. Demo of everything: `compositions/ctmotif.html` (26 s, id `ctmotif`); stills in `project/cartels/motif_stills/` (01–08).
Architecture copied from the NVIDIA motifs (`project/nvidia/MOTIFS.md`).

Colour code (palette_cartels.css): **ember = cartels, steel = USA, olive = Mexico's state, yellow = highlighter / key number only.**

## Rules (all motifs)
- Call the constructors **before `FX.mount`** (boiling line / rough-reveal filters register with `FX.onFrame`); pass
  `gate:[a, b]` (composition-local seconds of the scene window) so the boil only runs in that scene.
- Every time argument is composition-local: **text** cues `T(master)`, **structural** cues `S(master)` (MANUAL §4.4).
- Calls per instance in **chronological order** (focus/stamp states build on each other).
- Hide-on-call: anything you animate (`build`, `open`, `photo`, `row`, `stamp`, `cross`, `in`) is hidden from frame 0 until its
  time; anything you never animate is shown already built (e.g. a file with rows you never `row()` shows them typed).
- **Nothing measures layout** (fixed geometry, `pathLength=100`): the motifs work when built inside a scene that is `display:none`
  (tested: a file built in a hidden scene renders correctly). Keep the habit of building first, hiding last anyway (MANUAL §4.2).
- Unique `prefix` per instance (`"cts07-sc012-deal"`); every id inside is `prefix-…`, so several instances coexist.
- Don't restyle `ctm-*` in your composition; position/scale the root only. No `font-family` anywhere in your CSS.
- Glow: none of the motifs glow (paper never glows; the deal is a board). Your scene keeps its ONE hero glow elsewhere if any.
- Add your scene's grain / dust / vignette on top as usual (night 0.9 / 0.42 / 0.4, paper 0.3 / 0.14 / 0.22, footage 0.5 / 0.3 / 0.35).
- Motif labels are chart text (allowed, MANUAL §0). Keep them short; the plan decides; spell names exactly.

## MOTIF 1 — THE DEAL (`CT.deal`)
"Americans can find the bad guys, and Mexican forces would go in and kick the door in." Two panels split by **the line**:
left STEEL "AMERICA / FINDS" (surveillance-eye reticle icon), right OLIVE "MEXICO / ARRESTS" (handcuffs icon). Hero verbs
Haskoy 800 caps (`t-display`), labels Cooper Hewitt (`t-label`). Full board = panels 816 × 744 at y 206; the line at x 960.
```html
<div id="cts05-deal"></div>     <!-- a full-frame layer inside your shot (the motif is always 1920×1080, inset 0) -->
```
```js
const deal = CT.deal($("deal"), {
  prefix: SEG + "-deal",
  ground: "night",        // "night" (charcoal + halftone) | "paper" (two paper layers) | "none" (over your own photo/footage)
  compact: false,         // true = 300 px band (default top 640) for over a photo; pair with ground:"none"
  bandTop: null,          // compact band top in px (default 640 → bottom 940, leaves room for CT.credit at bottom-left)
  kicker: "The deal",     // small centred label above the board; null = none
  lineLabel: null,        // e.g. "The border" — t-label under the line
  labels: { findWho: "America", findVerb: "Finds", arrestWho: "Mexico", arrestVerb: "Arrests" },  // short!
  gate: [S(410.0), S(436.0)],
});
```
| call | does |
|---|---|
| `deal.build(tl, t, {find:T(..), arrest:T(..)})` | kicker opens from the centre, the line draws top→bottom (1.0 s), each panel wipes OUT of the line with a rough edge that settles (12 fps, long-tail ease), icons draw on, label + verb rise. With cues, each panel's VERB lands exactly on its cue (panel starts 0.5 s before). Without cues: left at t+0.25, right at t+0.55. Returns end time. |
| `deal.focus(tl, t, "find"\|"arrest"\|null)` | chosen half punches to 1.035, the other dims (night 62 %) and shrinks to 0.965; find = reticle turns 90° + pupil pulse, arrest = cuffs snap. `null` = both back. |
| `deal.stamp(tl, t, "Officially", {color:"--bone", rotation:-7})` | rubber stamp slams on in 3 frames over the board (ink-distress filter), board shakes, a light veil dims the rest. Default ink bone on night / ink on paper; `color` = any palette token. `deal.unstamp(tl, t)` lifts it. |
| `deal.cross(tl, t, {dur:1.6})` | "the CIA found a way around": a steel drone marker (the find icon in a disc) leaves the reticle, arcs over the line into the olive half with a steel trail; as it crosses, the line cracks (5 marker cracks) and boils hard for 1.1 s; a steel wash floods the olive panel. Permanent (the cracks stay). Returns end time. |
| `deal.out(tl, t, d=0.6)` | panels fold back into the line, everything else fades (ground stays). |
| `deal.panels.find / .arrest`, `deal.line` | elements, if you need to add your own markup. |

Example (master times are illustrative — take every word from the transcript):
```js
const deal = CT.deal($("deal"), { prefix: SEG + "-deal", gate: [S(612.0), S(640.0)] });
deal.build(tl, S(612.2), { find: T(614.31), arrest: T(616.92) });   // "find" / "kick the door in"
deal.focus(tl, S(618.0), "find");  deal.focus(tl, S(620.4), "arrest");
deal.stamp(tl, T(624.10), "Officially");                            // on "officially"
deal.unstamp(tl, S(627.0)); deal.cross(tl, S(627.3));               // "the CIA found a way around"
```

## MOTIF 2 — TARGET FILE (`CT.file`)
Manila folder + typed sheet on sand paper (two paper layers, MANUAL §10.6.1): accent edge strip, kicker "TARGET FILE" + tag,
paper-clipped photo on a mat (duotone ink→accent-dark / sepia-light + halftone) or a drawn **silhouette icon + "NO PHOTO"** (never
a fake face), NAME (Haskoy caps, wraps to 2 lines), "ALIAS" (Crimson Pro italic, curly quotes added for you), rule, 1–4 rows
`LABEL  value` typed char by char at 12 fps steps, and a rubber STAMP.
```js
const f = CT.file($("file"), {
  prefix: SEG + "-file",
  ground: "paper",          // "paper" (own sand ground + desk vignette) | "none" (lay it over your own ground)
  photo: "assets/cartels/people/meza_fbi_photo_1.jpg",   // null → silhouette placeholder
  photoPos: "50% 30%",      // object-position of the photo in its 320×396 window
  name: "Fausto Isidro Meza Flores", alias: "Chapo Isidro",   // alias null → no alias line
  rows: [["Reward", "$5,000,000"], ["List", "FBI Ten Most Wanted"], ["Charged", "Washington DC, 2012"]],   // ≤ 4 rows, values ≤ ~24 chars
  accent: "steel",          // ember (cartel file) | steel (US target package) | olive (Mexican state)
  kicker: "Target file", tag: "Sinaloa",   // header left / right (tag null = none)
  tilt: -1.4, scale: 1.06, x: 960, y: 548, // file centre in the frame; file is 1240 × 760 before scale
  stampAt: null,            // [left, top] in sheet px; default = right-aligned under the rows
  gate: [S(..), S(..)],
});
```
| call | does |
|---|---|
| `f.open(tl, t, {name:T(..), alias:T(..)})` | folder rises in with a tilt settle (1.3 s), sheet lifts out of it, header wipes, NAME wipes on its cue (default t+0.6), alias rises (default name+0.45), rule draws. |
| `f.photo(tl, t)` | photo drops onto the sheet and settles to its 2.4° tilt, paper clip slides on. (Without this call the photo/silhouette is already there.) |
| `f.row(tl, t, i, {cps:24, lead:0.15})` | row label wipes in at t, the value types from t+lead, 2 chars per 12 fps step (cps 24), accent block caret while typing. Put t ≈ 0.2 s before the spoken value; long values take (chars/24) s — start earlier or raise `cps`. Returns the end of typing. |
| `f.stamp(tl, t, "wanted"\|"captured"\|"killed"\|"run", text?)` | stamp slams in 3 frames (rotated −10°, multiply ink with distress) + a 6-frame shake. WANTED = ember, CAPTURED = olive, KILLED = ink, ON THE RUN = steel. Optional `text` overrides the word (keep it one or two words). Cue it 0.06 s before the verdict word. |
| `f.pushIn(tl, t, 1.07, {x, y, dur:1.8})` | smooth camera push toward a frame point (default: the stamp area). Keep scale ≤ 1.12 (the file must stay inside the 96 px margins). |
| `f.out(tl, t, d=0.7)` | file drops out of frame. |
| `f.cam`, `f.file`, `f.sheet` | elements (e.g. to add an `FX.markup` circle on the sheet — put the svg inside `f.sheet`). |

## DATE TAG (`CT.dateTag`) and CREDIT (`CT.credit`)
```js
const tag = CT.dateTag($("tag"), { prefix: SEG + "-tag", place: "Guasave, Sinaloa", date: "20 Nov 2026",
  pos: "tl",            // tl (default, 96/72) | tr | bl
  theme: "night",       // night (bone + soft scrim, for footage/photos) | paper (ink, no scrim)
  accent: null });      // null = bone tick; or "ember"/"steel"/"olive" when the place belongs to a side
tag.in(tl, S(..));      // rule + tick draw, text wipes in from the left at 12 fps; tag.out(tl, t)
CT.credit($("cr"), "Video: Al Jazeera English");          // bottom-left 96/72, Cooper Hewitt caps 22 px, shown from frame 0
CT.credit($("cr"), "Map: Natural Earth", { theme: "paper", pos: "br" });   // .in(tl,t) / .out(tl,t) if you need a fade
```
Format: place `City, State` + `DD Mon YYYY` (the motif uppercases); credit `Video: <outlet>` / `Photo: <outlet>` exactly as
logged in SOURCES.md. One credit per shot, always bottom-left unless the footage has a logo/caption there (then `pos:"br"`).
Keep the tag and the credit clear of burnt-in logos (choose the clip window / `pos`).

## Gotchas found while building
- `tools/build_index.py` does NOT discover `ct*` compositions: its id regex lists `seg|intro|ivs|pys|pd|c\d+s` and `nv…` only,
  so `build_index.py ctmotif` writes an EMPTY index (all-black snapshots). Until the lead adds `ct[a-z]*\d*` to that regex, add the
  host div to the sandbox `index.html` by hand (the `<link>/<script>` for ct_motifs are already injected).
- A rotation tween on the whole find icon turned the eye vertical — the icon is split into `spin` (reticle) and `core` (eye).
- The deal's `paper` ground uses paper_cream_01 + paper_stained_01_hires (stained + fiber read grey).
- Stamps are right-aligned (`right: 78px`) so long words (ON THE RUN) never get clipped by the sheet.
- `lint` on the whole sandbox lists other projects' errors; lint your file alone: `npx --yes hyperframes@0.8.217 lint compositions/<id>.html`.

## Do / don't
- DO keep the motifs identical across segments: no CSS overrides, same accents per side, same stamp words.
- DO cue verbs/stamps/names on the spoken word, 0.06 s before (T()).
- DON'T scale the full deal down to fit beside something — use `compact:true` (scaled text drops below 22 px).
- DON'T put a compact band and a credit both at the bottom-left without `bandTop` ≤ 640.
- DON'T invent file fields: every row value is what the narrator says / the plan marks; no fake seals, agency logos or signatures.
- Snapshot your scene's first and last 0.6 s (hold rule MANUAL §10.9): the stamp must hold ≥ 0.5 s before a cut.
