# nvs09 — NOTES (master 864.750–935.000, 70.25 s, 9 scenes) — plan: `project/nvidia/EDIT_NOTES_nvs09.md`

## Built
| sc | master | picture | ground / effect | in |
|---|---|---|---|---|
| sc001 | 864.75–877.50 | `china_night` map: ice pen line offshore (the ban, through the Taiwan Strait so Taiwan stays outside), China fills red, plane + volt GPU card → Shanghai, ship + volt rack → Shenzhen/HK, breach rings at the crossings, chips stream in and pile up inside China | night map, camera push 0.45→0.50, counter-scaled labels (CHINA, CHIP BAN) | fresh shot |
| sc002 | 877.50–880.80 | FACE M | face (clean) | hard cut on the map push |
| sc003 | 880.80–891.18 | THE SCOREBOARD (`NV.scoreboard`, full, top 170 px = centred; all results empty, row 4 empty dashed) → `markRow(1,"x")` at T(888.78) on "not" | night, slow push | whip → |
| sc004 | 891.18–897.98 | FACE W | face | hard cut |
| sc005 | 897.98–905.45 | FACE C (framing change exactly on the 897.98 join) | face | framing jump |
| sc006 | 905.45–913.08 | 7 Oct 2022 BIS rule p.1 (Federal Register) rises; ice pen circle on its title; Biden + Trump official-portrait cut-outs pop in either side with name tags; they lean apart on "don't agree"; ice pen arrows from both to the rule on "keeping this policy in place" | paper ×2, 12 fps pops, pen markups | slide ↑ |
| sc007 | 913.08–918.10 | FACE W (starts on the 913.08 join) | face | hard cut |
| sc008 | 918.10–921.95 | FACE M | face | punch-in |
| sc009 | 921.95–935.00 | race chart "AI computing power": US bar (ice) far ahead, China (red) short, bracket THE LEAD (the scene's one glow); 5 volt chips rise into China's bar, it grows ~45 px; ice pen circle round THE LEAD; camera still drifting at 935.00 (B-roll end — face cam picture ends 934.98) | night, bars 12 fps, pen bracket | light-flash whip |

- **Face cam: 26.44 s of 70.25 s = 37.6 %** (sc002, sc004, sc005, sc007, sc008). Framings M → W → C → W → M; every face-cam shot starts or
  changes framing on a join or a cut; joins 884.17 / 889.53 / 926.03 / 934.98 fall inside B-roll. Origin 1050px 110px, C = 1.44 (1.55
  cropped his hair at 1080p).
- First scene: fresh map shot. Last scene: the lead chart, camera drifting (cut on action into nvs10's B-roll).
- Reference ids: none assigned for nvs09 in the lead's plan (map #3, SCOREBOARD motif, collage, lead chart as planned).

## Checks
- lint (sandbox `work/nvs09`): 0 errors in nvs09 (the 25 errors are other projects' missing face-cam files); nvs09 warnings only
  `nested_media_start_basis_ambiguous` (face-cam data-start is composition-local, as in pys*) and file length.
- `sync_audit … --transcript transcript_nv.json`: 8 cues, all −0.06 s, 0 flagged.
- Timeline dump (headless): `tl.duration()` = 70.25 = DUR; no key tween ends < 0.5 s before a cut (only face-cam pushes run to their cut).
  The scoreboard glow settles at 890.67, so the cut to Sam sits inside "right" (891.18) for the 0.5 s hold.
- Snapshots looked at for every scene (start/middle/end).

## Assets
Shared: `people/biden_cut.png`, `people/trump_cut.png`, `docs/bis_rule_2022-10-07_p1.png`, icons `plane`, `ferry`, `gpu_card`,
`server_rack`, `chip`; map kit `china_night.jpg`. Own: `assets/nvidia/nvs09/derived/china_{fill,stroke}.svg` (from the kit overlay,
generator `project/nvidia/gen/nvs09_assets.py`, logged in `assets/nvidia/nvs09/SOURCES.md`). Nothing missing or substituted.

## For the lead / MANUAL
- Shared SVG icons (`fill=currentColor`) can be tinted without inlining: a div with `background:<colour>` + `mask-image:url(icon.svg)`
  (`icon()` helper in nvs09).
- A quick timeline dump without puppeteer: inline the template into a page with a LOCAL gsap copy (the CDN script does not load in
  `chrome-headless-shell --dump-dom`), run `chrome-headless-shell --headless --no-sandbox --dump-dom`, write results into a body attribute.
- Scoreboard `markRow` + its glow take ≈ 1.9 s after the cue — plan ≥ 2.4 s of board after the verdict word for the hold rule.
