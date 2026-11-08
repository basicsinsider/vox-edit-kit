# pys03 — NOTES (segment editor, 2026-11-08)

Master 213.60–332.60 (DUR 119.00). Plan: `project/paraguay/EDIT_NOTES_pys03.md` (scene table, words → picture). 24 scenes, as planned
(the composition is the reference for exact times). Derived assets: `project/paraguay/gen/pys03_assets.py`; sources `assets/paraguay/pys03/SOURCES.md`.

## Checks
- `npx --yes hyperframes@0.8.217 lint` (sandbox work/pys03): 0 errors in pys03.html (warnings = the same `nested_media_start_basis_ambiguous`
  face-cam warnings every Ivan segment has, + file length).
- `tools/sync_audit.py compositions/pys03.html --transcript transcript_py.json`: 0 flagged, 123 cues. Every text cue is a literal
  `T(word start − 0.06)`; 9 lines show "+0.02" only because the audit matches the short word before ("a", "on", "of", "the") — each is −0.06 to its own word.
- Snapshots LOOKED at (8 batches, ~55 frames): every scene at its text moments + transitions (tear, slide, whips), the 2.5D, both maps, last 0.5 s.
- Timeline duration 119.00. Key animations hold ≥ 0.5 s before each cut (sc005 cross moved to 231.35, sc009 licence 255.45, sc022 rise 323.35).

## Scenes / effects / layouts
sc001 ueno sign photo + push · sc002 fake sepia "history card" (LOC photo of the Palacio de López, "born in **1950**" yellow key number + highlighter)
· sc003 **tear transition** (new: the card is rebuilt in two clip-path halves with a jagged seam that fall away on "kidding", revealing him laughing)
· sc005 ledger page (paper_lined + stained, ink rows, teal profit line, bank drawn then pen-crossed) · sc006 **painting as B-roll** (Matsys, *The
Moneylender and His Wife*) in a frame + right text column, camera push + focus hunt + pen circle on the coins · sc008 **Credicentro** film-title
over teal light streaks (halate cool, the hero) · sc009 flow diagram (loans out / deposits crossed / licence with empty seal) · sc011 family tree
(3 generations, teal links, "2015" key number, link jumps to the youngest) · sc012 **2.5D** (Miguel Vázquez: clean plate + cut-out + title layer,
dolly + focus hunt) · sc014 **Paraguay night map** (tierra fill, PARAGUAY / BRAZIL / ARGENTINA / Asunción labels, teal business pins, push)
· sc015 **org chart** GRUPO VÁZQUEZ (Credicentro drops into the dashed group; itti, Pagopar, Hendyla, La Tribuna, Crónica, 650 AM pinned at 12 fps)
· sc017 collage of industries (4 taped prints) · sc019 **world night map** (ASIA / SOUTH AMERICA / MIDDLE EAST fill as named, UNITED STATES grey,
PARAGUAY tierra) · sc020 **isotype** (ref 5: family node wired to 24 businesses that fill teal) · sc022 **J-curve** (ref 7 variation: hatched loss
area revealed with the line, bracket "a very long time", "profitable") · sc024 money-flow diagram on night (one glowing Credicentro box feeding six
losing companies; dots flow; on "problem" a crack + the glow dies + the flow stutters; camera keeps pushing into the cut).
Transitions: whip ×6 (2 vertical, 2 light-flash), slide ×2, tear, hard cuts on EDL joins / on action. Never the same twice in a row.
Grounds: N P F F P N F N P F P N F N P F P F N P F P F N.

## Face cam — 37.3 s of 119.0 = **31 %**
sc003 M 4.68 · sc004 W 2.45 · sc007 W 5.85 · sc010 C 2.25 · sc013 W→C 6.25 · sc016 M 4.70 · sc018 W 3.55 · sc021 C→W 5.50 · sc023 M 2.05.
Below the ≈ 35 % target on purpose: the segment opens on an EDL join at 213.933 (a different take for the first 0.33 s, hands visibly jump) so
sc001 is B-roll, and the explanatory lines need graphics. Edges checked frame by frame (24 fps tiles, 15 windows): every face shot ends at or
before a join (226.533 → cut 226.40, 245.283 → 245.25, 275.417 → 275.40) or changes framing exactly on it (316.017). Framing origin changed to
(1040, 140) so C (1.55) never crops his head. No face shot runs across a join with the same framing.

## Boundaries
- First scene: fresh shot (ueno bank sign, slow push) at 213.60 — pys02's last shot can cut straight in.
- Last scene: money-flow night diagram, camera accelerating into the crack at 332.60 (cut on action) — pys04 ("By 2020, around COVID…") starts fresh.

## Deviations / decisions
- "Credit Central" → **Credicentro** on screen (RESEARCH). No free Credicentro logo/photo (archive.org snapshot of credicentro.com.py didn't load)
  → typeset in our type, never a copy of their logo.
- "Vasquez group" → **GRUPO VÁZQUEZ**. Company cards from RESEARCH/Bloomberg Línea (itti tech, Pagopar payments, Hendyla e-commerce, La Tribuna &
  Crónica newspapers, 650 AM radio); category labels are chart labels, not narration.
- Miguel Vázquez: name only as a small photo-ID tag (he isn't named in the narration; SEGMENTS brief identifies him). Photo = shared press photo
  (no SOURCES row in shared/ yet — gatherers: please log `shared/photos/miguel_vazquez.jpg`, `ueno_sign_hq_reuters.jpg`, `asuncion_skyline.jpg`).
- Family groups: map regions only (ASIA, SOUTH AMERICA, MIDDLE EAST) — no specific conglomerate names (keeps it generic and accurate).
- Text on asides: none on "I'm just kidding" (the tear is the gag) or "And that's important…".

## For the lead / MANUAL (gotchas)
1. **Tear transition** (new, reusable): build the outgoing card's markup once as a string, inject it into the outgoing scene AND two full-frame
   halves inside the incoming scene; give the halves `clip-path: polygon()` along a shared jagged seam (FX.rng points every 60 px) and their
   final camera state; on the word, rotate/translate them away (0.6 s, `FX.choppy(E.in)`), then hide.
2. **2.5D clean plate without OpenCV**: grow the known background into the dilated subject mask ring by ring with normalised convolution
   (`gaussian_filter(img*w)/gaussian_filter(w)`, scipy) — 40 passes of σ 14 fill a person-sized hole; blur 6 px in CSS. Without it the
   blurred backdrop still contains the subject and shows a white halo around the cut-out ("sticker"). PIL `GaussianBlur` refuses mode "F".
3. World maps for a whole-globe framing: crop `world_night.jpg` to a 16:9 window and write region SVGs in the crop's world-pixel viewBox
   (`viewBox="x0 y0 w h"` — no path transforms needed); decimate sub-paths (≥ 6 px steps) → the borders SVG drops from 4.4 MB to 0.8 MB.
4. Commons thumbs: non-standard widths (1600, 2400) now FAIL; 1280/1920 work (commons_thumb.sh).
5. Face-cam origin (1040, 200) cropped his hair at C 1.55 after the push → (1040, 140) for this face cam.
6. `ink()` with a hand-guessed path length shows a stray dash piece before its cue — measure with `getTotalLength()` (scenes are
   `visibility:hidden`, geometry is available).

## SFX
`compositions/pys03.sfx.json` — 52 markers (hero per scene + whips/moves): paper_tear + rewind on the joke, marker_scratch on the crossed bank /
circle / deposits, stamp_thud on 1950 / 2015 / GRUPO VÁZQUEZ, pin_pop on map pins & prints, tone_blip on the region fills, dot_ticks on the
isotype, circuit_clunk + boom_low on the crack. No bleeps in this segment.
