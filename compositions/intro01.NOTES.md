# intro01 — NOTES (segment editor, 2026-10-31)

VO 0.00–92.13, scenes IS001–IS022, `compositions/intro01.html` (root `data-vo-start="0" data-duration="92.13"`), SFX
markers in `compositions/intro01.sfx.json` (80 markers). Checked in `work/intro01`: lint **0 errors**; `sync_audit`
**84 text cues, all −0.12…0.00 s**; every scene snapshotted (start/middle/end + every transition) and looked at.

## What was built (scene → visual → effects)
| scene | words | visual | effects / ref |
|---|---|---|---|
| IS001 | In 1983 | `1983` hero halate on light streaks | `FX.streaks`, odometer, push; **light-flash whip** out |
| IS002 | Robert Tsao, CEO of Taiwanese chip company UMC | Tsao cut-out (blue duotone + halftone) on paper; Taiwan relief panel with celadon @2.96, chip-die footage panel @3.68, UMC logo card @4.40; ROBERT/TSAO blue label boxes, CEO | #10 Vox layered, 12 fps slides; push into chip panel → cut on action |
| IS003 | was walking around his factory floor | E07 archival fab footage (manager walks the rows) | weave 0.6, CA 0.12, push |
| IS004 | …he has a unique insight | freeze of the same frame desaturates to 40 %, the walker (cut-out) stays bright, streaks bloom behind him; `insight` hero halate | `FX.chokeSettle`; **vertical whip up** |
| IS005 | …his industry and the future of the world | wafer (E20) → `FX.curveCut` @13.60 → NASA globe; `his industry` label, `the world` hero | curve cut, focus hunt 14.40, push into the map → cut on action |
| IS006 | Taiwan's exports of telephones to the United States | **D10** tilted vintage map: 1935/43 Formosa aviation map close-up → pull-out over a beige Pacific map, Taiwan celadon wash, halftone telephone pops on Taiwan, dashed ink route + celadon dot to the US | far-edge lens blur; **whip right** |
| IS007 | 4 million … 24 million | **D01**: celadon watercolour-top bars, dashed threshold, halftone telephone as the base object, ink label box counting 4→24 | `FX.text.count`, 12 fps bars; punch-in on the box → cut |
| IS008 | 6x increase in just 12 months | punched-in ink box `6×` (yellow key number) counting 1→6, `increase`, `12 months` + 12 ticks at 12 fps | **vertical whip down** |
| IS009 | UMC was making the chips inside those phones | lamp-lit desk: 1970 push-button phone film card + typeset UMC datasheet card (real UMC logo, drawn DIP chip, no invented text) | push + focus hunt, blue pen circle + arrow chip→phone, `phones`; **paper slide up** |
| IS010–011 | record profits in its first full year / the phone boom died, UMC's sales died with it | **D05** line chart (no axis values/years): UMC blue line to a record, RECORD stamp (settles), `first full year` band; camera slides right: ink "phone boom" line drops, UMC follows, pen arrow | stamp chokeSettle; camera follows the fall → cut on action |
| IS012 | as a chip factory … just for one product | E08 microscope-rows footage; bone markup arrows funnel into one telephone pictogram, rough cross after "product" | `FX.markup.arrow/cross`; **whip left** |
| IS013 | much more profitable … anything … in demand | **D04** serif title (blue italic `profitable`), six product-pictogram rows with blue bars; rows pop @51.28, bars grow @52.08 | cut on action (bars still growing) |
| IS014 | in 1983, this was a novel concept | **Tsao's idea card** (motif): K+E cross-section grid card, pencil sketch factory → five products, navy `1983` stamp, `a novel concept` with two highlighter strokes | `FX.markup.pen` (boil 4), chokeSettle; **paper slide up** |
| IS015 | pure play chip factory or foundry | typeset Webster-1913-style dictionary page (tilted 3D, halftone grows) + card `pure-play chip factory` / `foundry`; highlighter on the printed **Found·ry** entry | push + focus hunt; **light-flash whip** |
| IS016 | It just didn't exist in the world | dark empty world (NASA), radar sweep, `didn't exist`, hollow pin pulse @64.85 | dive toward Taiwan (push-through) |
| IS017 | Tsao could see the future … good idea | **2.5D #1** from the vase portrait (backdrop / `the future` / Tsao / vase) | dolly, focus hunt 68.0; **whip right** |
| IS018 | his board of directors … permission | E37 boardroom/blackboard footage, word-by-word lower third | weave, push, move with the gesture → cut |
| IS019 | pretty new business … a year ago | lined-paper ledger timeline: UMC logo at the start tick, blue dot travels to "now", bracket `a year ago` | 12 fps; **vertical whip up** |
| IS020 | Tsao needed their permission to reorient the whole thing | engraved-style compass rose (bone, our SVG) + torn-edge UMC Fab 8AB photo card (blue duotone, halftone) turning 90° on `reorient` | chokeSettle; keeps turning → cut on action |
| IS021 | uphill battle | Titian, *Sisyphus* (Prado, colour oil painting) fit to height over a blurred copy; pen arrow up the slope | rotation continues from IS020; **light-flash whip** |
| IS022 | the board was pretty excited … almost told him yes | **D06** semicircle master: 12 seat-dots, grey → blue clockwise; title word by word (blue italic `excited`), `almost`, a hovering YES stamp that never lands | camera tilts down @91.90 (hand-off) |

Halation only on the hero: `1983`, `insight`, `the world` — everything else `.clean`/ink. No red anywhere (rule for intro01).
Transitions vary: FW → CA → freeze → W↑ → CA → W→ → CA → W↓ → PS → (continuous) → CA → W← → CA → PS → FW → PT → W→ → CA → W↑ → CA → FW.

## Papers per scene (Lead's request: no paper twice in a row)
IS002 paper_cream_01 + cream_02 (90 %) · IS006 beige map + paper_cream_02 multiply · IS007–008 paper_cream_01 + **paper_graph_01** (90 %)
· IS010–011 paper_cream_02 + **paper_stained_01** (multiply 60 %) · IS013 cream_01 + paper_fiber_01 · IS014 cream_02 + fiber, card =
K+E `ke1960_cross_section_green_norm` (multiply) over cream_02 · IS015 cream_01 + newsprint_01 on the page · IS019 cream_02 +
**paper_lined_01** (90 %, desaturated) · IS022 cream_01 + cream_02 (90 %).

## Deviations from EDIT_NOTES (and why)
- **IS010 + IS011 are one scene layer** (`data-scene="IS010-IS011"`) — the plan says "continuous, same chart"; one layer avoids a duplicate chart.
- **IS009**: no telephone manual / UMC datasheet exists free (gatherer B) → typeset datasheet card (real UMC logo + drawn DIP chip, grey
  line placeholders, no invented part numbers/text) + the 1970 touch-tone phone clip (`pushbutton_phone_1970_hand.mp4`) on a film card.
- **IS015**: no PD dictionary scan → typeset recreation of Webster 1913-style entries (Foundation … Fountainhead; the Foundry entry is
  the 1913 wording "The act, art, or business of casting metals…"). No real masthead.
- **IS019**: the 1880 ledger scan carried unrelated handwriting (names) → replaced by `paper_lined_01` over cream (no handwriting).
- **IS020**: no PD compass-rose engraving → our own engraved-style SVG compass rose. The UMC building turns as a photo card (cleaner
  than a hand-cut building matte).
- **IS022**: 12 seats on a **single arc** (r 340) — two rows of 5+7 read as scattered dots at this count.
- **IS006**: the Pacific relief was too dark for a vintage paper map → baked `assets/intro/made/pacific_beige.jpg` (same pixel space).
  Celadon fill is a baked PNG wash (CSS masks inside the 3D plane rendered as a rectangle).
- **IS017** 2.5D uses the low-res vase portrait (853 px real) at ≤ 794 px display width (not full-frame), backdrop filled + blurred.
- No §10.7 painting-to-print in this segment (no quote/historic figure in 0–92 s). No face cam (rule: none before 10 s; inserts are 02/03).

## Assets made / added (all logged in the folder SOURCES.md)
- `assets/intro/paintings/sisyphus_titian_prado.jpg` — **N13 downloaded** (Commons, PD) — logged in paintings/SOURCES.md.
- `assets/intro/cutouts/phone_pushbutton_cutout.png` + `_halftone.png` — N09 (hand polygon; remove-background failed on the object).
- `assets/intro/cutouts/fab_walker_cutout.png` — IS004 walker (remove-background on the 2.9 s still + polygon trim).
- `assets/intro/made/`: `globe_blue_marble_desat.png` (N07, rendered from the NASA basemap), `world_desat_3840.jpg`, `pacific_beige.jpg`,
  `taiwan_celadon_wash.png`, `fab_walk_freeze_2p9.jpg`, `pushbutton_phone_1970_hand_f3p3.jpg`, `tsao_layers/{backdrop,tsao,vase}`.
- Credits on screen (13 px): Tsao vase portrait (NYCU Secretariat, IS002 + IS017), UMC Fab 8AB (ABOVE THE SKY, CC BY-SA 4.0, IS020),
  NASA Blue Marble (IS005, IS016).

## Usage count (photos/clips, intro budget ≤ 2)
Tsao vase portrait (E01): IS002, IS017 = **2 (budget used up)**. phone_pushbutton_brown: IS006, IS007 = **2 (used up)**.
E07 fab walk (IS003 + its freeze IS004 = same shot) 1 · E20 wafer 1 · E21 die macro 1 · E08 microscope rows 1 · E37 boardroom 1 ·
pushbutton_phone_1970_hand 1 · umc_fab8ab 1 · Sisyphus 1 · UMC logo (logo, IS002/IS009/IS019).

## Hand-off IS022 → IS023 (intro02 copies this)
At 91.90 the whole sheet `#intro01-sc022-sheet` (1920×1500) moves `y: 0 → −180` over 0.23 s with `ease: "power2.in"` (so it is still
accelerating at 92.13, ≈ 1560 px/s) — intro02 starts with the sheet at y −180 and continues down (decelerating) to the footnote.
At 92.13 the frame shows: title at y −30…+50 (cut off at the top), the YES stamp hovering (scale 1.2, y ≈ +14 → +2 hover), the 12 blue seats.

```html
<!-- sheet: paper_cream_01 + paper_cream_02 (90 % multiply), background-size 1920px 1500px -->
<div id="introNN-sheet" style="position:absolute;left:0;top:0;width:1920px;height:1500px">
  <div class="i1-p1" style="background-image:url('assets/textures/paper_cream_01.jpg')"></div>
  <div class="i1-p2" style="background-image:url('assets/textures/paper_cream_02.jpg')"></div>
  <div class="t-serif" style="position:absolute;left:0;top:150px;width:1920px;text-align:center;font-size:76px;color:var(--ink)">the board was pretty <i style="color:var(--navy)">excited</i></div>
  <svg viewBox="0 0 1920 1500" style="position:absolute;left:0;top:0;width:1920px;height:1500px"></svg>   <!-- seats, see JS -->
  <div class="t-serif-i" style="position:absolute;left:1270px;top:400px;font-size:72px;color:var(--ink)">almost</div>
  <div style="position:absolute;left:760px;top:330px;width:400px;height:220px;transform:translateY(2px) scale(1.2)">
    <div style="position:absolute;inset:0;border-radius:20px;background:rgba(20,27,36,0.35);filter:blur(22px);transform:translate(34px,70px) scale(0.9)"></div>
    <div class="t-display" style="position:absolute;inset:0;border:12px solid var(--ink);color:var(--ink);font-size:150px;line-height:186px;text-align:center;transform:rotate(-8deg);background:#e9e2d2">YES</div>
  </div>
</div>
```
```js
// 12 seats, D06 master: dot r 27 (54 px), single arc r 340 around (960, 960); base line y 1000 (x 490–1430, ink 3 px, 0.6);
// dashed guide arc r 400 (ink 2 px, dash 6 10, opacity 0.35). Grey #9a958c → blue #1d5c9e, filled clockwise from the left, 1/12 s per seat.
const cx = 960, cy = 960, R = 340, N = 12, seats = [];
for (let k = 0; k < N; k++) { const a = Math.PI - k / (N - 1) * Math.PI; seats.push([cx + Math.cos(a) * R, cy - Math.sin(a) * R]); }
seats.forEach(([x, y], i) => svg.insertAdjacentHTML("beforeend", `<circle cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="27" fill="#1d5c9e"/>`));
// (use string concatenation + getElementById if you look the circles up again: lint rejects template literals in querySelector)
```

## Idea card motif (IS014 → intro02 IS036, IS040)
```html
<div id="introNN-card" style="position:absolute;left:300px;top:100px;width:1320px;height:860px;transform:rotate(-1.5deg);background:#eee7d6;box-shadow:0 30px 70px rgba(20,27,36,0.35);overflow:hidden">
  <div style="position:absolute;inset:0;background:url('assets/textures/paper_cream_02.jpg') center/cover;mix-blend-mode:multiply;opacity:0.7"></div>
  <div style="position:absolute;inset:0;background:url('assets/intro/papers/ke1960_cross_section_green_norm.jpg') 0 0/1320px auto repeat-y;mix-blend-mode:multiply;opacity:0.55"></div>
  <svg viewBox="0 0 1320 860" style="position:absolute;left:0;top:0;width:1320px;height:860px"></svg>  <!-- pencil sketch -->
  <div class="t-display" style="position:absolute;left:1010px;top:70px;font-size:92px;color:var(--navy);border:8px solid var(--navy);padding:4px 22px 0;transform:rotate(7deg);mix-blend-mode:multiply">1983</div>
  <div class="t-serif-i" style="position:absolute;left:140px;top:690px;font-size:64px;color:var(--ink)">a <span style="background:linear-gradient(transparent 30%, rgba(242,211,59,0.9) 30%, rgba(242,211,59,0.9) 92%, transparent 92%)">novel concept</span></div>
</div>
```
Sketch (pencil `#3a4150`, `FX.markup.pen` width 5, `FX.markupDefs(…,{boil:4})`): factory polyline
`[[140,560],[140,340],[240,280],[240,340],[340,280],[340,340],[440,280],[440,170],[500,170],[500,560],[140,560]]`; five arrows from
(530,390) via (700, 390+(y+40−390)·0.55) to (870, y+50) for y = 110 + i·115; pictograms phone/tv/calc/pc/game (the `PICTO` table in
intro01.html, stroke 4.5) at translate(900, y).

## Open issues / for the lead
- Lint warnings `nested_media_start_basis_ambiguous` on the six `<video>`s are expected (data-start is composition-local, = VO time since this segment starts at 0).
- SFX: `phone_ring` @20.96 is marked optional; `focus_hunt` markers follow SOUND_PLAN §4.
- Snapshots in `work/intro01/.snap/a…k`. Not rendered (lead renders).
