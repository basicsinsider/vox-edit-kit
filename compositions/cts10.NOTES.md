# cts10 — NOTES (master 891.500–976.208, 84.708 s) · the CIA on Chihuahua's raids
Plan: `project/cartels/EDIT_NOTES_cts10.md`. 11 scene layers (sc001–sc007, sc009 board with internal camera moves for sc009–sc012,
sc013, sc014 incl. the sc015 punch-in, sc016 incl. sc017). Character code held for the whole segment: steel = CIA/the American(s),
olive = state police / Mexican officers, ember = cartel target, ash = prisoner / unknown.

Built
- sc001 Zuany card (El Universal archive photo, duotone) + CIA seal + steel pen thread; dateTag CHIHUAHUA · FALL 2025 (NYT timeline).
- sc002 Vox layered background of REAL SSPE (Chihuahua state police) training photos + sand strip: real state-police badge on "state police",
  olive pictograms, steel figure walks in on "an American", dashed bracket on "new special forces unit".
- sc003 graph-paper range pictogram (back view, like the real range photo): olive shooters + hits at 12 fps; steel figure watches (pen eye),
  steps into lane 5 on "training right alongside them".
- sc004 night blueprint: tactical stack at a door; three steel dots join on "CIA officers"; door swings, stack flows in on "raids".
- sc005 five identical operator pictograms; the American's steel drains to olive on "blending in"; gear sweep; rifles on "rifles".
- sc006 jacket illustration; REAL Chihuahua coat of arms printed on it on "state logo"; pull back to a rack of identical jackets.
- sc007 our own rugged tablet (no brand/OS) in gloved hands, abstract block-map HUD; LIVE + ticking clock on "live"; route on "directions";
  intel cards on "intelligence"; push into the screen + focus hunt.
- sc009 ref ast_91abea88b76c4b43 rebuilt: graph-paper desk, dark card with an isometric cut-away safe house (walls rise at 12 fps), ember tag
  CARTEL SAFE HOUSE word by word; steel cover wedge at the entrance; olive dots file in; camera to the phone sketch card (scan, abstract rows);
  interview room: table, ash prisoner chair, olive chair, steel chair on "sat in", lamp pool.
- sc013 six raid-plan cards; warm wash drains on "rosy"; bone pen X's on four; push through the bar card (cut on action).
- sc014 top-down bar plan: boss (ember) at a table, slips out the back; team (olive + 2 steel) enters; dashed ghost + glass; punch-in +
  pen scribbles on "visibly annoyed the Americans".
- sc016 paper node diagram: ?s on "suspect", one node turns unknown on "somebody", dotted leak + radio rings to the target on "tipping off";
  Zuany card slides in, name tag, pen "?" — Sam's implication only, no accusation drawn; steel thread to the CIA seal on "helping the Americans".
Transitions: whip →, slide, flash whip ↓, hard cut on action, whip ←, hard cut, flash whip →, vertical whip ↑, push-through, whip →.

Checks: lint `compositions/cts10.html` 0 errors (2 warnings: file length; duplicate img src = the Zuany photo used in sc001 and sc016 by
design). sync_audit `--transcript transcript_ct.json`: 0 flagged (all text cues −0.06; "CARTEL" and "BAR" are matched to the preceding
"a" by the audit but sit −0.06 before their own words). Headless dump: tl.duration() = 84.708, 392 tweens, no JS errors over a 0.5 s seek
sweep. Snapshots of every scene (start/middle/end) and every cut ±0.05 s looked at.

Assets: `assets/cartels/cts10/` (SOURCES.md): 2 SSPE photos (chihuahua.gob.mx press gallery, Jan 2025 course), Zuany (El Universal),
coat of arms (CC BY-SA, credited), state-police badge (CC0), CIA seal (PD). Shared assets: none beyond textures/motifs (CT.dateTag, CT.credit).
Deviations: no "real" raid footage exists — raids are diagrams by design. The SSPE course photos with instructors in tan clothing were
rejected (could be misread as the CIA officer). The SSPE photos are generic state-police training (Jan 2025), never labelled as the CIA
training. `assets/cartels/people/` had no Zuany photo, so I sourced my own (cts09 may hold a different one — lead may unify).

Gotchas for the lead/MANUAL: (1) a camera div with left/top offsets breaks `at()` framing math (my first sc009 pass framed everything
off by the offset) — keep camera divs at 0,0 and size them to cover; (2) GSAP `y` on an SVG `<g>` with a transform attribute again sent
the sc002 figures to the origin (known §4.2 gotcha) — use a proxy writing the attribute; (3) one snapshot batch showed a proxy-driven
state (iso walls) already "risen" before its start; a fresh single snapshot was correct — I added seek-safe hold tweens (proxy held at its
start value from 0 to the start) for state that only an onUpdate writes.
