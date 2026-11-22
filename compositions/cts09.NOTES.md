# cts09 — CHIHUAHUA & ZUANY (master 768.458–891.500, 123.042 s) — editor notes, 2026-11-22
Built from `project/cartels/gen/cts09_template.html` → `python3 project/cartels/gen/build_cts09.py` (inlines the map paths from
`project/cartels/gen/cts09_paths.json`) → `compositions/cts09.html`. Edit the TEMPLATE, then rebuild. Derived assets:
`.venv/bin/python project/cartels/gen/cts09_assets.py` → `assets/cartels/cts09/derived/` (SOURCES.md there). Shot table: `project/cartels/EDIT_NOTES_cts09.md`.

## Scenes (17)
| id | master | what | refs / effects |
|---|---|---|---|
| sc001 | 768.458–781.51 | kit `mexico_night` on a 3D-tilted plane; Chihuahua lifts out as the relief cut-out (olive tint + glowing edge); TX/NM outlines + labels; ember Mex 45 route with heat glow → arrow into EL PASO pin + rings; HUD corner ticks; camera push | ast_b30b6aa33937428e, ast_d02865717c824c47 |
| sc002 | 781.51–785.83 | real Infobae page (10 Nov 2026) reporting the NYT investigation; highlighter on "The New York Times"; CT.dateTag "The New York Times · 10 Nov 2026" | document + highlighter |
| sc003 | 785.83–790.63 | CT.deal (night) build → `cross` (the CIA's way around) | MOTIFS |
| sc004 | 790.63–798.75 | CT.file (steel, "Case file" · Chihuahua) over an editorial collage: name, photo, rows State/Role "Special prosecutor"/Before "Police commander" | ast_6f5b26e350ad486a |
| sc005 | 798.75–803.67 | Zuany at a Fiscalía podium (duotone), steel reticle lock, contrast call-out | §10.6.3 |
| sc006 | 803.67–809.83 | `chihuahua_night`: steel CIA officers + olive state police icons pair up, travel out with trails + radio rings | isotype pairs |
| sc007 | 809.83–818.90 | stylised visa (no number/seal/fields), ember CANCELLED stamp on "canceled" | prop + stamp |
| sc008 | 818.90–825.27 | El Universal paragraph (citing the NYT): highlighter on "revocado la visa de Zuany" + "presuntos vínculos con cárteles de la droga", ember pen circle | §10.6 |
| sc009 | 825.27–847.56 | case board on a dark desk: Zuany polaroid, 4 anonymous WITNESS cards, ember strings, 2022 note with two olive badges, INVESTIGATION folder buried under papers, witness 3 circled, slides into a U.S. WITNESS PROTECTION folder | ast_8693d810270e43fd |
| sc010 | 847.56–851.40 | Zuany office photo + steel pen "?" | pen markup |
| sc011 | 851.40–857.32 | callback to cts07 sc006 RULEBOOK (same look: ink balance, DoD/CIA seals on starbursts, "Who they can work with" grids); CIA grid turns steel on "almost anyone", crossed-out MILITARY grid comes up on "military" | cts07 / ast_0659daaead12498d |
| sc012 | 857.32–867.32 | isotype grid of 30 cops/officials; 26 turn ember on "bought off"; COPS / OFFICIALS legend; steel reticle finds one clean figure | isotype |
| sc013 | 867.32–872.70 | his case file again (rows Visa: Cancelled · Accused: 2022 police murders), ember PROBLEM stamp | CT.file |
| sc014 | 872.70–877.72 | night balance: steel open door vs a clean record; beam tips to the door on "worth more" | metaphor chart |
| sc015 | 877.72–884.36 | the CANCELLED visa; the steel "America" panel (find reticle) slides in and the card is drawn onto it | prop |
| sc016 | 884.36–889.60 | El Universal paragraph: highlights "el Times afirma, con base en testimonios de nueve funcionarios", "Zuany acompañó a agentes de la CIA", "recuperó su visa" | document |
| sc017 | 889.60–891.50 | CANCELLED lifts, steel REINSTATED stamp on "came back" | stamp |
Transitions: whip, hard cut, slide ↑, whip, flash whip, hard cut, slide ←, vertical whip, whip, slide ↑, hard cut on action, whip, hard cut, slide ←, vertical whip, hard cut.

## Checks
- `npx --yes hyperframes@0.8.217 lint compositions/cts09.html` → 0 errors, 3 warnings (duplicate img discovery — the same photo used in two scenes; file size; a build-time getTotalLength flagged as callback).
- `python3 tools/sync_audit.py compositions/cts09.html --transcript transcript_ct.json` → 0 cue(s) flagged (every text cue −0.06 s, CLEAN RECORD −0.08 vs "clean").
- Headless timeline dump: `tl.duration()` = 123.042 = DUR; no tween runs past the end; seek 0…123 s every 0.5 s without errors.
- Snapshots: every scene (start/middle/end) and every cut ±0.05 s looked at; hold ≥ 0.5 s checked by a timeline dump (fixed: sc016 last highlight, sc015 card move, sc017 push length).

## Accuracy / deviations
- Zuany's title = "Special prosecutor" (Sam: "top state prosecutor", SEGMENTS §4). "Accused" wording for the 2022 murders (RESEARCH §6).
- No NYT page is available (nytimes.com blocked → relay); the NYT investigation is shown through the real Infobae / El Universal pages that report it, with the date tag 10 Nov 2026 (NYT publication date per Infobae).
- No Zuany photo existed in `assets/cartels/people/`: both photos are cropped from the Infobae article captures (lead images of articles about him; the podium one is captioned as Zuany, credit Fiscalía de Chihuahua).
- Operations in sc006 have no pins/place names (the reporting gives no locations) — the pairs head generically into the state with rings.
- Balance used twice (sc011 callback, sc014 door vs record) — not consecutive, different ground and design.
- Witnesses = silhouettes; no victims shown; the visa is a clearly stylised graphic.

## For the lead
- Seals in sc011: shared `assets/cartels/logos/{dod,cia}_seal.svg` (cts07 uses `assets/cartels/cts07/logos/*.png`, which has no SOURCES.md yet).
- Gotchas: (1) a CSS `rotateX` tilt on a map plane magnifies the lower half a lot — at perspective 2400 / rotateX 26° / scale 1.24 the planned framing came out ~2× too tight; 16° / 1.1 with camera scale 0.46→1.0 works. (2) `hyperframes snapshot` ≈ 2.5 min per batch here (startup-bound) — batch 8 frames. (3) A text label placed in screen space over a moving map camera drifts off its city: put it inside the camera layer and counter-scale it (1/s).

## Fix round 1 (2026-11-22, #19 "text needs to be English again")
- sc002 (781.51–785.83), sc008 (818.90–825.27, v1 13:43 ≈ 823 s), sc016 (884.36–889.60): each Spanish page is now a small original ("Original · Spanish", same yellow highlights) under an English translation card (`.c9-xl`: paper card, Cooper Hewitt kicker "<outlet> · <date> · translated from Spanish", Haskoy headline / Crimson Pro body). Highlighter sweeps (`xlMark`) and the ember underline on "drug cartels" (`xlUnder`, replaces the pen circle) keep the original cue times; slow push instead of the page camera. Credits end "· translated"; sc002's credit moved to bottom-right (date tag stays bottom-left). No English source of the NYT story is openly reachable (nytimes 403), so translation it is. Built in the template → `build_cts09.py`.
- Left as is: "SE BUSCA / INFORMACIÓN" banner fragments in the background of the Fiscalía podium photo (sc004 collage / sc005) — real signage in a news photo, partly cropped.
