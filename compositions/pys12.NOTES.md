# pys12 — NOTES (segment editor pys12, 2026-11-08)

Master 1294.50–1456.50 (162.00 s). Plan: `project/paraguay/EDIT_NOTES_pys12.md` (built as planned; deviations below).
Composition is generated: template + generator in the editor's scratchpad (`gen.py` inlines the Paraguay outline paths from
`assets/maps/kit/south_america_overlay.svg` and `world_overlay.svg` into `__PY_SA__` / `__PY_W__`). Edit `compositions/pys12.html`
directly from now on — the paths are already inlined.

Checks: lint 0 errors for pys12 (the 9 lint errors in the sandbox are other projects' missing Ivan/intro face-cam files);
`sync_audit` 0 flagged — 202 cues at −0.06, 13 shown as +0.02 are the audit matching a cue to the *previous* short word (e.g. "the" 1313.23 vs
"United" 1313.31): each is word start − 0.06 of its own word. Snapshots of every scene (start / middle / end) looked at; fixes made after
looking: clipboard overflow, BREAKING NEWS tag over the Telefuturo clock, Senate tag on the building, Telefuturo clock/logo in the board crop,
white text on a white shirt (sc001 scrim), label-box gaps, escalation text touching the "?" marks, echo timeline too small, law page too empty,
underline that never showed (see gotchas). Timeline = 162.00 s (last tween ends exactly at 1456.50).

## Scenes (30 shots)
| id | master | what |
|---|---|---|
| sc001 | 1294.50–1297.33 | Última Hora: prosecutors open the Grupo Vázquez vault — "all this investigation" (fresh shot) |
| sc002 | 1297.33–1301.87 | FACE W — "Paraguay's place / in international finance" |
| sc003 | 1301.87–1304.50 | South America atlas (kit), Paraguay tierra, labels PARAGUAY/BRAZIL/BOLIVIA/ARGENTINA/Asunción, label-box "still a developing country" |
| sc004 | 1304.50–1315.55 | Ref-6 horizontal trust bars (no numbers — none spoken): PARAGUAY short tierra, UNITED STATES / EUROPE long ink |
| sc005 | 1315.55–1321.27 | IMF HQ (plum duotone) + IMF seal (plum-light) — "the IMF assessment" (paper-style slide in) |
| sc006 | 1321.27–1325.00 | FACE M — “this is a good country” |
| sc007 | 1325.00–1328.30 | Paraguay's file card; the IMF seal STAMPED on it — "that sign of approval" |
| sc008 | 1328.30–1336.05 | night chart: borrowing-rate line drops, money dots flow into a bridge that draws itself — "lowers their borrowing rate" → "fund infrastructure" |
| sc009 / sc010 | 1336.05–1346.22 | FACE C (no text) / FACE W "sends its people" → "once a year" |
| sc011 | 1346.22–1355.02 | THE CHECKLIST (clipboard, IMF seal on the clip): 4 lines word by word, plum pen ticks, header "their checklist" lands last |
| sc012 | 1355.02–1359.00 | Americas night map: IMF/Washington → Asunción flight, plane rides the dashed route, camera follows south; labels on every place |
| sc013 | 1359.00–1363.30 | Telefuturo live (BCP board announces the Ueno resolution, its own chyron) on a modern monitor — "literally last week" → BREAKING NEWS tag |
| sc014 | 1363.30–1367.04 | FACE M — "assessors were in the country" |
| sc015 | 1367.04–1374.10 | BCP HQ on the skyline (plum duotone) tagged "the central bank"; Senate session card slides in, tagged; plum arrow Senate → BCP; "do something about all these reports" |
| sc016 | 1374.10–1379.85 | pressure gauge: "political pressure / on the central bank", needle into the plum zone, "not bury it" |
| sc017 | 1379.85–1386.51 | FACE W — "looks like corruption" → "a much bigger problem" |
| sc018 | 1386.51–1398.55 | ZOOM-OUT ESCALATION: one cracked teal bank → pull back: 32 banks all get "?" → pull back: inside a plum government palace (new layout) |
| sc019 | 1398.55–1403.03 | FACE M — "could not actually bury this" |
| sc020 | 1403.03–1407.00 | callback: push back in to the one bank, others dim, plum pen box — "just a one bank problem" |
| sc021 | 1407.00–1410.60 | FACE W — "a common occurrence" |
| sc022 | 1410.60–1415.39 | echo timeline (night): ghost banks crack and fall one after another as the camera pans left into the past — "banking crises / have happened before in Paraguay" |
| sc023 / sc024 | 1415.39–1424.05 | FACE M "a very unique law" / FACE C (his opinion, no text) |
| sc025 (+ sc026) | 1424.05–1440.62 | THE LAW: typeset page (plum rule, small Paraguay mark), "This law basically says", his clause types itself word by word (52 literal cues), pen underline on "under the table", FACE W insert 1433.90–1436.05 ("and you don't do anything about it"), then a punch-in and the yellow highlighter on "criminally held liable" (body text) |
| sc028 | 1440.62–1446.22 | Telefuturo: BCP board at the press table (cropped past clock/chyron/logo) — "all the people on the board" → "a personal incentive" → "dis" pops in tierra-light |
| sc029 / sc030 | 1446.22–1453.62 | FACE M "trying to bury this" / FACE W "if this thing becomes bigger" |
| sc031 | 1453.62–1456.50 | the looming gavel (CC BY 2.0, plum duotone) — "everyone could face / criminal charges"; slam (shake + flash) on "charges", push accelerates into the cut |

First scene: vault-raid footage, fresh shot. Last scene: gavel slam, push continuing into the cut (hand-off motion → pys13's unanimous vote).

## Effects / layouts used
whips ×11 (horizontal, vertical, light-flash), paper slide, hard cuts on action / at framing changes; map kit atlas + night maps with
screen-constant labels (helper `mapCam`), flight route + plane; ref-6 bars; stamp; line chart draw-on; clipboard checklist with pen ticks
(markupDefs boil 4); TV monitor for footage; tag call-outs + pen arrow; gauge; zoom-out escalation (new layout: one → all → government);
pen box (markup); stop-motion echo timeline (new layout); typewriter law page + pen underline + yellow highlighter on body text; text swap
gag ("dis"); photo slam with shake/flash. No 2.5D in this segment (nothing here deserved depth more than the escalation pull-back).
Glow: none (no halate hero needed). Yellow: only the highlighter on "criminally held liable".

## Face cam
sc002 4.54 + sc006 3.73 + sc009 4.47 + sc010 5.70 + sc014 3.74 + sc017 6.66 + sc019 4.48 + sc021 3.60 + sc023 4.04 + sc024 4.62 + sc026 2.15
+ sc029 3.84 + sc030 3.56 = **55.13 s of 162.00 = 34.0 %**. Framings W/M/C alternate; no face-cam shot crosses an EDL join (joins 1294.57,
1335.97, 1354.97, 1398.52, 1429.12, 1438.97 — sc009 starts at 1336.05 and sc019 at 1398.55, after their joins). First 0.33 s / last 0.6 s
of every face shot checked frame by frame on the master: he is mid-sentence and gesturing in all of them — no glances, reaches or settling.

## Deviations / decisions
- The law: RESEARCH.md has nothing on it, so the page is a typeset recreation of the NARRATOR's paraphrase (his words, word by word) with
  no article number, title or date (never invent a legal citation). Header = his words "This law basically says".
- No empty board chairs: the ending uses the gavel only (stronger single image, and the board's real faces are already in sc028).
- "IMF assessors in the country last week": RESEARCH found no press confirmation — shown as narrated (the flight is generic, no date).
- sc013 shows the BCP press conference footage under "this news became breaking news" (that announcement IS the breaking news) — pys13 may
  also use Telefuturo BCP footage for the vote; we use `bcp_board_a` here (with its chyron) and `bcp_board_b` (cropped) in sc028.
- Gavel used as SFX twice (1437.55 "criminally held liable", 1455.30 "criminal charges") — 18 s apart; sound designer may pitch one.

## Assets
New: `assets/paraguay/pys12/photos/gavel.jpg` (Commons "Legal Gavel (27571702173).jpg", Blogtrepreneur, CC BY 2.0) — logged in
`assets/paraguay/pys12/SOURCES.md`. Shared: uh_vazquez_raid_1, x_telefuturo_bcp_board_a/b, imf_hq, imf_seal, bcp_building, senado_sesion,
flag_paraguay; maps south_america_atlas, americas_night.

## Gotchas for MANUAL (lead)
1. A GSAP `scaleX` tween on an element whose CSS initial transform is `scaleX(0) rotate(-0.6deg)` never became visible (degenerate matrix:
   GSAP can't decompose a zero-scale rotated matrix). Keep the CSS start state a pure `scaleX(0)` (the highlighter `.p12-hlb` worked).
2. Drawing an overlay (route, plane) in SCREEN space over a map camera driven by a proxy tween: create the overlay's clock tween AFTER the
   camera tween — GSAP renders children in start-time order, so an overlay tween that starts earlier reads last frame's camera (lags 1 frame).
3. A wide SVG inside a panning camera: after `svg.style.left/width = …` in the script, the snapshot showed the content at 1920/4320 scale
   (as if the class width `.p12-mk {width:1920px}` still applied; cause not isolated) — putting size/offset in an id rule in the composition
   CSS fixed it.
4. Word-by-word reveal inside a `.label-box` without the box showing early or gappy: make each word its own `.label-box` span with no
   whitespace between spans, the space as `&nbsp;` inside the span, inner paddings zeroed — the boxes abut into one strip that grows per word.
5. Telefuturo BCP clips: `x_telefuturo_bcp_board_b.mp4` at scale 1.5, origin `62% 0%` crops away the clock (top-left), the logo
   (top-right) and the chyron (bottom); `bcp_board_a` is best kept whole on a monitor (its chyron is the breaking news).
6. `mapCam(cam, labelsHost, labels, cx, cy)` (in pys12): one proxy {fx, fy, s} drives a `transform-origin:0 0` map camera and keeps
   Haskoy/`t-label` place labels at constant screen size (positions written in onUpdate) — reusable for any kit map push/pan.

## Fix round 1 (Krish, 720p review — MANUAL §0 "No narration captions")
- Removed every caption that only repeated the narration: sc001, sc002, sc003 label-box, sc004 serif title, sc005, sc006, sc007, sc008
  (both titles), sc010, sc013 ("literally last week"), sc014, sc015 bottom line, sc016 ("on the central bank", "not bury it"), sc017,
  sc018 (all three), sc019, sc020, sc021, sc022 (both), sc023, sc028 (incl. the "dis" gag), sc029, sc030, sc031. The dark corner scrims on
  face-cam shots were removed with their text (face cam is clean now).
- Kept: map labels (sc003, sc012 incl. Washington/IMF/Asunción + route), chart text (sc004 bar labels; its chart title is now a static
  "Foreign investors' *trust*" that appears with the chart, not word-cued), "BORROWING RATE" axis label, the clipboard checklist items
  (header now a static "Checklist"), the gauge label "POLITICAL PRESSURE", the IMF seal + stamp, BREAKING NEWS tag, central bank / Senate tags,
  the law page with its typed clause + underline + highlighter (header now a static "The law"), credits.
- No scene became empty (every one still has its picture/graphic). Timings, transitions, face cam (34.0 %) and duration 162.00 unchanged.
- sfx.json: removed the 'dis' pin_pop (1445.32); all other markers are on objects/moves, kept (42 markers).
- Checks: lint 0 errors for pys12, sync_audit 0 flagged, changed scenes snapshotted and looked at (sc001, sc004, sc011, sc016, sc025, sc028, sc031).
