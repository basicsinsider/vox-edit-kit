# cts07 — NOTES (segment editor, 2026-11-22)
Master 540.417–651.500 (DUR 111.083). 11 scenes, plan in `project/cartels/EDIT_NOTES_cts07.md`. Lint 0 errors (3 warnings: duplicate
img discovery for the reused seals, file size); `sync_audit` 0 flagged; `tl.duration()` = 111.083 (headless dump); every scene and cut
snapshotted and looked at.

## What was built
| scene | master | picture | effects / ref |
|---|---|---|---|
| sc001 | 540.417–547.450 | night relief US + Mexico; the border drawn by hand on "unwritten deal"; US steel / Mexico olive fills + labels; push accelerates into the border | map kit, constant-size labels (mapCam helper), cut on action; ref ast_671f213364e14029 |
| sc002 | 547.450–564.670 | **CT.deal full build** (motif introduction): line = "The border"; steel pen arrow (American forces) stops at the line, dashed path into Mexico crossed out; OFFICIALLY stamp; FINDS on "find", ARRESTS on "Mexican forces"; focus arrest + board kick on "kick the door in"; underline on "arrest them"; focus find on "its side of the deal"; punch into the reticle → flash cut | MOTIFS.md |
| sc003 | 564.670–573.200 | real TWZ article (18 Feb 2025): pen under the date, pen along the headline, circle "Mexican", highlighter "focused on finding labs / producing the narcotic Fentanyl inside Mexico", circle "unarmed" | §10.6 pen + highlighter, two pages on the desk |
| sc004 | 573.200–577.070 | unarmed MQ-9 (Predator B, USAF PD) push into the sensor ball ("cameras"), hard cut into a drone-camera view (Esri sierra, steel grade, abstract HUD brackets/crosshair/scan line); Sheinbaum card on "Mexico says it knew" | whip →, HUD |
| sc005 | 577.070–585.390 | CIA seal + ember cartel network; reticle sweeps and lights the nodes ("finding cartels"), locks on the top node, pen X ("taking out the top guys") | vertical whip |
| sc006 | 585.390–604.220 | **THE RULEBOOK** (see below) | paper slide ↑; ref ast_0659daaead12498d |
| sc007 | 604.220–608.380 | THE DEAL (built) focus FINDS; CIA seal pinned = piece one, DoD seal slams on "second piece"; push into the DoD seal | vertical whip ↑ |
| sc008 | 608.380–623.420 | Esri southern Arizona/Sonora: ARIZONA fill + label, TUCSON pin, border lights + MEXICO (**no "15 miles"**); zoom box with the Davis-Monthan AFB aerial + pin; official name word by word (Joint Interagency Task Force – Counter Cartel) → squeezes into JIATF-CC on "a lot to say"; NARCO HUNTERS sticker (word by word) + pen note "(our nickname)" | hard cut on the push; ref ast_671f213364e14029 zoom box |
| sc009 | 623.420–630.620 | desk: JANUARY 2026 calendar, 15th circled (JIATF-CC established 15 Jan 2026); Calabrese portrait (steel duotone) + name tag; Arab News/Reuters clipping, highlighter on "experience battling groups like / Al-Qaeda and Islamic State" (no quote marks) | whip ← |
| sc010 | 630.620–646.940 | DoD / CIA / FBI / DEA seals pop on their words round a JIATF-CC hub, fly into it; **CT.file** (steel) TARGET PACKAGE, NO PHOTO silhouette, rows typed: YOUR GUY · WHERE HE SLEEPS · WHO PROTECTS HIM · WAY IN · WAY OUT with pen doodles (circle round the silhouette, house, guards ring, in/out arrows) | slide ←; ref ast_8693d810270e43fd |
| sc011 | 646.940–651.500 | THE DEAL (built): small manila TARGET PACKAGE folder on FINDS slides over the line into ARRESTS on "handed off"; focus ARRESTS lands on "Mexico" and ends exactly at 651.5 | light-flash whip → |

## THE RULEBOOK — look for the cts09 callback (847–867 s)
Sand paper (paper_cream_02 + 22 % paper_graph_01_hires), a black ink **balance scale** centred at x 960: pivot knob (960,176), beam
880 px (ends ±440 from the pivot at y 190), post to a trapezoid base at y 470–500. Each pan = a short ink rod + grey dish (308×24); on the
LEFT pan the **DoD seal** (150 px) on a 12-point **steel-dark starburst** with a stack of four ink "rulebook" slabs beside it, label
**MILITARY** (Haskoy 54, ink) under it; on the RIGHT pan the **CIA seal** on a **steel** starburst, label **CIA**. The beam ends tipped
**−8° (military side down)**. Under it a t-label "WHO THEY CAN WORK WITH" (y 548) and two 5×4 person-icon grids (60 px icons, 96×92 cells):
left grid x 298–778 — 16 icons crossed by ink pen slashes and dimmed to 32 %, 4 steel (cells 1, 7, 11, 18); right grid x 1130–1610 —
all 20 steel. One CIA icon (cell 13) is pen-circled, a pen arrow runs to an **ember "bigger target" silhouette in a steel-dark reticle**
(x 1630–1800, y 650–890), and a steel-dark string runs from that person off the bottom-right edge. Final framing: push 1.1× toward
(1440,760). For the callback: rebuild the same scale/grids (or copy the sc006 block from `compositions/cts07.html`), start from the
end state (tipped, crossed, circled) and pull the string from the right edge to Zuany.

## Deviations from the lead's plan
- Drone beat: no narcolab frame (that is the 2026 Chihuahua meth lab, already used in cts02/cts11 — reuse + wrong lab/year); the
  "labs" are shown by the real article text instead, and the drone view is a generic Sierra Madre satellite feed with abstract HUD only.
- CNN drone screenshots are covered by a consent pop-up → TWZ article used (same day, same facts, says "unarmed").
- Calabrese: no quote card — the Arab News/Reuters paragraph is reported speech, highlighted without quote marks.
- Target package values = the field names Sam says (labels allowed as file fields); no invented facts; no stamp.
- Two extra THE DEAL instances (sc007 "second piece", sc011 hand-off) use the built state (no `build`), focus only.

## Shared assets used
news n03_twz_reapers (+_k1), n04b_arabnews_jiatf_calabrese (+_k1); people calabrese_1; map kit mexico_night/satdesat/overlay,
sinaloa_sat, aerial_tucson_davis_monthan_z16 (derived crops in `assets/cartels/cts07/derived/`, generator `project/cartels/gen/cts07_assets.py`).
My own: `assets/cartels/cts07/` (MQ-9 photo, Sheinbaum CC BY, four agency seals) — SOURCES.md there. 8.8 MB.

## For the lead
- `assets/cartels/people/` still has no SOURCES.md (Calabrese portrait credited "Photo: U.S. Air Force" from RESEARCH's af.mil link).
- `people/sheinbaum_1.jpg` is NOT byte-identical to Commons "Claudia Sheinbaum (2025) (cropped).jpg"; I downloaded the Commons file myself.
- Gotchas: (1) `CT.deal.focus()` runs 1.2 s — a focus at the segment's last second extends `tl.duration()` past DUR (fixed: start it
  1.2 s before the end). (2) Map labels as `.lab > div` with CSS `translate(-50%,-50%)`: set `xPercent/yPercent` with gsap instead, since
  GSAP owns the transform. (3) The TWZ k1 page needs measured word boxes (column projection) — my first eyeballed boxes were 300 px off.
  (4) An `ink(..., dash)` line created at t=0 shows from frame 0 of the composition — create static lines with `el()` and fade them.
