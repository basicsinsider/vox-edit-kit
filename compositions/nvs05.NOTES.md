# nvs05 — NOTES (master 472.667–559.583, DUR 86.917, composition `nvs05`)

## HAND-OFF FOR nvs06 (THE LINE end state — copy exactly)
```js
const ln = NV.line($("ln"), { prefix: SEG + "-ln", lineAt: 0.62, gate: [...], chips: [
  { id: "a100", name: "A100", power: 0.80 },  { id: "h100", name: "H100", power: 0.92 },   // BANNED (ln.ban at 514.24 / 514.54)
  { id: "a800", name: "A800", power: 0.555 }, { id: "h800", name: "H800", power: 0.555 } ] }); // under the line (addChip 552.70 / 553.10)
```
- lineAt **0.62**; columns default (a100 col 0, h100 col 1, a800 col 2, h800 col 3) — same as the `nvmotif` demo.
- To reproduce my last frame in nvs06: don't call drawAxis/drawLine/addChip for these four (they are shown built), and call
  `ln.ban(tl,"a100",t)` + `ln.ban(tl,"h100",t)` at least 1 s before the line scene first becomes visible (the ban tween takes 0.95 s),
  so both are already stamped BANNED when it appears.
  Then `moveLine(tl, 0.47, …)` bans A800/H800 as it crosses them (motif demo).
- My last frame (559.58): camera `ln.cam` back at scale 1.0, x/y 0 (it is mid pull-back until the last frame = cut on action). No cutout
  cards, no title on screen. nvs06 opens on the face cam (lead plan), so the hand-off is a cut.

## Scenes (see `project/nvidia/EDIT_NOTES_nvs05.md` for exact words/cues)
| id | master | picture | ref |
|---|---|---|---|
| sc001 | 472.667–476.55 | JOB ONE title card (document paper, volt torn band, ice brush ring, torn ink bar, tape) — "JOB"/"ONE" on his words | `ast_e1ede4fafbd84a66` |
| sc002 | 476.55–488.58 | FC M → W (483.62) → C (join 486.35); compact SCOREBOARD row 1 "Keep the chips out of China" word by word, rows 2–4 dimmed | motif |
| sc003 | 488.58–518.43 | THE LINE: "THE BAN / 2022" chart title, axis, line, zones; A100 + H100 drop and get BANNED; NVIDIA product photo cards | `ast_ebb77f26d0fc4b3f`, motif |
| sc004 | 518.43–523.13 | FC C ("devastating") | — |
| sc005 | 523.13–527.50 | waffle 5×4 = NVIDIA's sales, bottom row (a quarter) turns China red, CHINA legend + "A QUARTER" callout, ghost A100/H100 boards | `ast_0b23d2c7a06c4bb3` |
| sc006 | 527.50–531.02 | FC W | — |
| sc007 | 531.02–536.25 | night: dim world map, DEMAND axis, volt exponential curve (glowing head = the one hero), hub dots pop around the world (none in China) | `ast_06720d0b255d4d29` |
| sc008 | 536.25–543.61 | FC M → C on the aside "Very quickly, by the way" (542.45) | — |
| sc009 | 543.61–548.33 | engineering drawing of the new chip drawn on (package, volt die, HBM, pins, dimension), title block NVIDIA + "A800 · H800"; dashed ice limit drawn just above the chip on "around this law" | — |
| sc010 | 548.33–559.583 | THE LINE again (same instance): push to the gap under the line (scale 1.32, framed so no label is cut), focus hunt, A800 + H800 drop under the line on "right there on the line"; pull-back to 1.0 through the end | motif |

Transitions: whip → slide-up → hard cut → light-flash whip → cut → whip (−1) → cut → slide-up → whip (−1). Grounds never > 2 in a row.
Face cam **27.6 s / 86.9 s = 31.8 %** (476.55–488.58, 518.43–523.13, 527.50–531.02, 536.25–543.61); framing changes at every EDL join
inside a face-cam shot (486.35); joins 488.58, 518.43, 523.13 are scene cuts; 509.33 / 558.88 fall in B-roll.

## Checks
- lint (sandbox `work/nvs05`): 0 errors for nvs05 (only the generic `nested_media_start_basis_ambiguous` warnings on the 4 face-cam
  videos — data-start is composition-local, as in pys02 — and `composition_file_too_large`).
- `sync_audit.py compositions/nvs05.html --transcript transcript_nv.json`: 0 cues flagged (all −0.06 to their word; the +0.02 lines are
  the audit pairing a cue with the neighbouring short word).
- Timeline dump (headless): `tl.duration()` = 86.917 = DUR; max tween end 86.917; seek through every 0.5 s without errors.
- Snapshots looked at for every scene (start+0.3, middle, last 0.5 s). Holds: JOB ONE 0.6 s, chip cards 1.1 s, waffle 1.6 s, curve 0.55 s
  after the last hub dot, drawing 0.7 s after the limit line; sc010 ends on a camera move (cut on action).

## Shared assets used
face cam master; `hardware/cutouts/a100_sxm4_cutout.png`, `h100_sxm_cutout.png` (product cards in sc003 + ghosts in sc005);
`logos/nvidia_wordmark.svg` (title block); textures paper_stained_01_hires, newsprint_01/02(_norm), paper_cream_02, paper_blueprint_01_hires
(greyscaled + darkened — blueprint blue would read as ice = Washington), grain/dust; my derived `assets/nvidia/nvs05/derived/world_night_2400.jpg`.

## Deviations from the lead's plan
- JOB card runs to 476.55 (not 476.03) so "ONE" holds 0.6 s; FC starts there. Extra FC pieces (527.50–531.02 and 536.25–543.61 incl. the
  aside) to reach ≈ 32 %; the drawing therefore covers 543.61–548.33 only.
- No camera push in sc003: THE LINE fills the safe area edge to edge, so any zoom > ~1.01 cuts "THE LINE" tag or the zone labels; the
  push lives in sc010 at a framing chosen so labels are fully in or fully out.
- "Ladder" chips before the ban are not drawn (the motif's ruler rungs are the ranking board); A800/H800 names are on the title block of
  the drawing too (chart label, approved list in DECISIONS 9).
- New design for the shared "JOB card" family (first one built): ids/CSS in sc001 — other editors may copy it for JOB TWO/THREE, LEVEL FOUR.

## Gotchas worth adding to MANUAL
- THE LINE motif spans x 96–1824: any `ln.cam` scale above ~1.01 pushes the tag / zone labels past the 96 px margin or off-frame — punch-ins
  must be large enough to exclude labels completely (e.g. scale 1.32 centred at 690,528 shows the tag, A/H100 and A/H800 but no axis/zone
  text).
- One `NV.line` instance can serve two separate scenes (show the same scene div twice in the SC list); keep calls chronological and reset
  `ln.cam` with a `tl.set` while hidden.
- A dashed SVG line can't be drawn on with dashoffset — mask it with a solid copy whose dashoffset is tweened (`pen(..., {dash})` helper).
