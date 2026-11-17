# NVIDIA motifs — THE SCOREBOARD and THE LINE (build once, paste everywhere)

Two graphics recur across the video and must look identical in every segment. They live in the kit, not in your file:
`lib/nv_motifs.js` (defines `window.NV`) + `lib/nv_motifs.css` (classes `nvm-*`). `tools/build_index.py` and
`tools/build_master.py` load both automatically for every composition whose id starts with `nv` (after fx.js / palette_nvidia.css),
so you only add an empty `<div>` and call the API. Demo of everything: `compositions/nvmotif.html` (40 s, id `nvmotif`);
stills in `project/nvidia/motif_stills/`.

Rules
- Call `NV.scoreboard(...)` / `NV.line(...)` **before `FX.mount`** (the marker boil registers with `FX.onFrame`); pass
  `gate:[a, b]` (composition-local seconds of the scene window) so the boil only runs in that scene.
- Every time argument is composition-local: text-bearing cues `T(master)`, structural cues `S(master)` (MANUAL §4.4).
- Calls must be made in **chronological order** per instance (the line tracks which chips are banned as you go).
- Hide-on-call: anything you animate (`intro`, `revealRow`, `markRow`, `addChip`, `drawAxis`, `drawLine`) is hidden from frame 0
  until its time; anything you don't animate is shown already built. Never put the root inside a `display:none` scene while
  calling (nothing measures, but keep the habit — MANUAL §4.2).
- Give each instance a unique `prefix` (`"nvs07-sc012-sb"`); all ids inside are `prefix-…`.
- Do not restyle the motifs in your composition (no overrides of `nvm-*`); position the root only (`left/top` inline style).
- Don't put `transform`/`scale` tweens on the root with CSS centring; use the returned `cam` (line) or scale the root itself.

## MOTIF 1 — THE SCOREBOARD (night ground)

```html
<div id="nvs07-sb"></div>      <!-- inside your night shot; full size: 1680 px wide at left 120 / top 118 (override inline) -->
```
```js
const sb = NV.scoreboard($("sb"), {
  prefix: SEG + "-sb",
  state: { 1: "x", 2: null, 3: null, 4: null },   // results already stamped before this scene: null | "x" | "check" | "q"
  row4Text: null,                                 // null = empty dashed 4th row; "The renting loophole" = filled
  compact: false,                                 // true = 540 px corner card for face cam (left 96 / top 72 by default)
  tally: null,                                    // null = no tally line; "" = tally slot, shown by setTally()
  gate: [S(1572.4), S(1596.0)],
});
```
Returns `{ el, rows, intro, revealRow, markRow, fillRow4, setTally, hideTally, out }`:

| call | does |
|---|---|
| `sb.intro(tl, t0, {rows:[t1,t2,t3,t4], words:[[…],…]})` | kicker wipes in, ice rule draws, rows wipe in left→right (12 fps, `FX.ease.out`). Default row stagger 0.4 s from t0+0.45. `words` = optional per-row word cues (job text word by word). Returns end time. |
| `sb.revealRow(tl, n, t, {words:[T(..),…]})` | one row wipes in (same move as intro). |
| `sb.markRow(tl, n, "x"\|"check"\|"q", t)` | marker glyph drawn on (✗ two strokes 0.5 s, ✓ 0.45 s, ? 0.5 s + dot), lands 1.22× and settles over 0.9 s, cell tint fades in, label wipes in ("NOT WORKING" red-light / "WORKING" volt; "?" has no label). The newest stamp carries the single glow; the previous glow fades. Put `t` 0.06 s before the spoken verdict word. |
| `sb.fillRow4(tl, text, t \| [cue per word])` | dashed slot solidifies, tab fills ice, result tile slides in, words rise (array = one cue per word, use `T()`). |
| `sb.setTally(tl, "1 — 1", t)` / `sb.hideTally(tl, t)` | optional score line under the table (needs `tally:""`). One setTally per instance. |
| `sb.out(tl, t, d)` | whole board eases out (before a whip). |

Glyphs are SVG marker strokes (Haskoy lacks ✓/✗), boiling at 12 fps (permanent boil = hand markup, MANUAL §10.1.2).
Colours: tab/rule = ice (the ban is Washington's), ✗ = flag red, ✓ = volt, ? = yellow (the only yellow on the board).

### Cue examples (master times from `transcript_nv.json`; check every word yourself)
```js
// 386–405 · introduce the board (no verdicts yet); 4th row empty — "there's a fourth row … and it's empty" 392.46–394.14
const sb = NV.scoreboard($("sb"), { prefix: SEG + "-sb", gate: [S(386.0), S(406.0)] });
sb.intro(tl, S(386.30), { rows: [S(386.9), S(387.3), S(387.7), S(392.40)] });   // row 4 slot appears on "fourth"
// 864–889 · row 1 judged: "it's not working" (working @ 889.00)
const sb = NV.scoreboard($("sb"), { prefix: SEG + "-sb", gate: [S(885.5), S(892)] });
sb.markRow(tl, 1, "x", T(888.78));                // on "not" 888.84
// 1572–1595 · row 2: "it is working" (working @ 1581.46) + "the score is one to one" (one @ 1590.02)
const sb = NV.scoreboard($("sb"), { prefix: SEG + "-sb", state: { 1: "x" }, tally: "", gate: [S(1575.4), S(1595.2)] });
sb.markRow(tl, 2, "check", T(1581.08));           // on "is" 1581.14 → "working"
sb.setTally(tl, "1 — 1", T(1589.96));
// 2126–2147 · row 3: "I don't think it's working" (don't @ 2138.90)
sb = NV.scoreboard(..., { state: { 1: "x", 2: "check" } }); sb.markRow(tl, 3, "x", T(2138.84));
// 2351–2355 · row 4: "I don't know how to rank this part" (rank @ 2354.19) — filled earlier when the loophole is named
sb = NV.scoreboard(..., { state: { 1: "x", 2: "check", 3: "x" }, row4Text: "The renting loophole" });
sb.markRow(tl, 4, "q", T(2354.13));
```
The 4th row's text is chart text the plan must mark (MANUAL §0 "no narration captions"): fill it where the plan says, with
`fillRow4(tl, "The renting loophole", [T(..), T(..), T(..)])`.

### Compact (face cam)
`compact: true` → 540 px card (night 82 % + ice top rule), 25 px job text balanced on ≤ 2 lines, mark-only result cell
(no label), ≥ 22 px everywhere. Default position left 96 / top 72; on a face cam put it on the side away from the face
(narrator framed right → card left) and never over the face (MANUAL §10.10.1). Reveal it yourself, e.g.
`gsap.set(el,{clipPath:"inset(0% 100% 0% 0%)"}); tl.fromTo(el,{clipPath:"inset(0% 100% 0% 0%)",x:-30},{clipPath:"inset(0% 0% 0% 0%)",x:0,duration:0.9,ease:FX.choppy(FX.ease.out,0.9,12),immediateRender:false}, S(..))`
(see `nvmotif` scene B).

## MOTIF 2 — THE LINE (paper, graph-paper texture)

```html
<div id="nvs05-ln"></div>     <!-- a full-frame layer inside your shot; NV.line draws its own two paper layers -->
```
```js
const ln = NV.line($("ln"), {
  prefix: SEG + "-ln", lineAt: 0.62, gate: [S(488.0), S(612.0)],
  chips: [ { id: "a100", name: "A100", power: 0.80 }, { id: "h100", name: "H100", power: 0.92 },
           { id: "a800", name: "A800", power: 0.555 }, { id: "h800", name: "H800", power: 0.555 },
           { id: "h20",  name: "H20",  power: 0.405 }, { id: "rtx4090", name: "RTX 4090", power: 0.70 } ],
});
```
Geometry (`NV.lineGeom`): axis x = 400; power 0 → y 900, power 1 → y 180; chip cards 74 px high, centred on their power;
columns from x 486 every 206 px in the order of `chips` (override per chip with `col` or `x`). A card "right on the line"
sits just under it: `power = lineAt − 0.065`. Max 6 columns inside the safe area.

| call | does |
|---|---|
| `ln.drawAxis(tl, t, {bottom:T(..), top:T(..), dur})` | pen axis drawn up with arrow head + 10 % rungs; "WEAKEST" / "MOST POWERFUL" on their cues. |
| `ln.drawLine(tl, t, {dur:1.1, tag, zone, cant, can})` | ice-dark marker line drawn left→right, "THE LINE" label-box, hatched ice zone above, zone labels "CAN'T SELL TO CHINA" / "CAN SELL" on their cues. |
| `ln.addChip(tl, id, t, {name, power, col})` | volt chip card drops in (12 fps), tick on the axis. Unknown ids need `name` + `power`. |
| `ln.ban(tl, id, t)` | card dims, red ✗ over the chip icon, red "BANNED" tag stamps on, axis tick turns red. |
| `ln.moveLine(tl, newPower, t, dur=1.4, {autoBan:true})` | line + zone glide to the new height; every added chip the line passes over is banned as the line crosses it. |
| `ln.cam` | the camera div (paper inside): push/drift it, `scale ≥ 1` only. `ln.chip(id)` = a card element, `ln.Y(p)` = its y. |

### Cue examples (488–611)
```js
ln.drawAxis(tl, S(494.6), { bottom: T(498.48), top: T(499.52) });          // "weakest" 498.54, "most powerful" 499.58
ln.drawLine(tl, S(501.2), { tag: T(501.52), cant: T(503.20), can: T(505.12) }); // "line" 501.58, "above" 503.26, "below" 505.18
ln.addChip(tl, "a100", S(512.9)); ln.addChip(tl, "h100", S(513.3));          // "covered two chips"
ln.ban(tl, "a100", S(515.0)); ln.ban(tl, "h100", S(515.3));
ln.addChip(tl, "a800", S(552.7)); ln.addChip(tl, "h800", S(553.1));          // "right there on the line"
ln.moveLine(tl, 0.47, S(569.5), 1.6);                                        // "moves the line below this new chip"
ln.addChip(tl, "h20", S(579.6));                                             // "right below this new line"
ln.addChip(tl, "rtx4090", S(605.4)); ln.ban(tl, "rtx4090", S(610.9));        // "regular video game chips … banned"
```
Chip names (A800/H800/H20 on screen) are chart labels: Sam doesn't say them, the plan decides whether they are shown — the
chips are the true chips he describes. Names always as NVIDIA writes them (A100, H100, A800, H800, H20, RTX 4090).

## Do / don't
- DO keep both motifs pixel-identical across segments: same prefixes pattern, no CSS overrides, same lineAt (0.62 → 0.47).
- DO cue verdict marks on the verdict word ("not", "is working", "don't think", "rank"), 0.06 s before.
- DO add your scene's grain/dust/vignette on top (night: grain 0.9 / dust 0.42 / vignette 0.4; paper: 0.3 / 0.14 / 0.22).
- DON'T add a second glow or yellow element in a scoreboard frame (the "?" or the 1 — 1 tally is the yellow/hero).
- DON'T scale the full scoreboard down for a corner — use `compact:true` (scaled text drops below 22 px).
- DON'T call `markRow` for a row that also has a `state` value (the static mark is replaced from frame 0).
- DON'T move the line up — `moveLine` never un-bans a chip.
- Timeline length stays your `data-duration`; snapshot your scene's first and last 0.6 s (hold rule MANUAL §10.9).
