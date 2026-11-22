# cts02 — NOTES (master 68.167–158.917, 90.75 s)
Plan with exact cues: `project/cartels/EDIT_NOTES_cts02.md`. Generator for derived map/print assets + inlined map paths:
`.venv/bin/python project/cartels/gen/cts02_assets.py` (rewrites the `// @@PATHS-BEGIN … // @@PATHS-END` block in this composition).

## Built (13 beats in 8 shots)
| beat | master | treatment | refs |
|---|---|---|---|
| sc001–002 | 68.167–85.38 | CASE BOARD (sand board on a dark wall, lamp pool): opens on the Isidro TARGET FILE already stamped CAPTURED (match to cts01), pulls back, drifts over the pinned prints, lands on El Mencho's CT.file (DATE / name / KILLED / RAID / INTEL rows on their words), steel thread toward the seal | ast_1587dee18be645e2 · CT.file |
| sc003 | 85.38–92.03 | light-flash whip → real Chihuahua lab footage, dateTag CHIHUAHUA · APR 2026, CIA seal pops on "CIA" | — |
| sc004 | 92.03–98.33 | vertical whip → @SecWar strike feed in a steel HUD monitor, 70+ counter (yellow, the one glow) + BOATS, kicker SINCE SEP 2025 | SEGMENTS §6 surveillance screen |
| sc005 | 98.33–108.75 | hard cut on action → night map (kit americas_night crop): US steel, route US → Caracas on "flew", back to New York on "captured", RPP arrival footage card + name tag NICOLÁS MADURO on "president", push in | — |
| sc006 | 108.75–113.25 | whip back to the board, wide: 5 cases, steel threads converge on the Great Seal, big pen "?" on "What is going on?" | MANUAL ref 9 (string board) |
| sc007 | 113.25–117.05 | TITLE "US vs CARTELS" (see below) — US on "war", vs + CARTELS on "cartels"; push-through into the black bar | ast_e1ede4fafbd84a66 |
| sc008 | 117.05–122.86 | out of black: SEDENA tarmac photo (Meza Flores + 2 detainees, faces barred by SEDENA, no label on who is who), push, tones to sepia on "his story" | — |
| sc009–011 | 122.86–139.18 | kit `sinaloa_relief`: B/W FBI portrait pinned (ember pin), name chip, BORN 1982 odometer, NORTHERN SINALOA region (OSM `#rg-northern_sinaloa`, region, not a birthplace pin) → state outline draws + glow, “Silicon Valley” tag → circle portraits El Mayo (Culiacán) / El Chapo (Badiraguato) with leader lines, ember pen circle on El Chapo | ast_22f35e73b57b4e0e, MANUAL ref 4 variant |
| sc012–013 | 139.18–158.917 | dark spotlit table, polaroids (Guasave, Los Mochis, El Fuerte, Topolobampo, Malverde shrine Culiacán on "cartel"), timeline strip 1982 / 1990s / TEENAGER bracket, ember pen circle on "only jobs paying well", final accelerating push into the shrine photo (cut on action into cts03) | ast_e8562eb310434ee1 |

## TITLE BLOCK for cts14 ("IS IT WORKING?")
Self-contained function `makeTitle(root, {prefix, seed, items})` in this file (search "TITLE BLOCK"). Copy the function plus the CSS rules
`.c2-tt*` and `.c2-fill`/`.c2-svg` (rename the prefix), give it an empty full-frame `<div>` and call:
```js
const TT = makeTitle($("tt"), { prefix: SEG + "-tt", seed: 11, items: [
  { text: "IS IT", kind: "bar", size: 180, dy: -26 }, { text: "WORKING?", kind: "bar", size: 180, dy: 14 }] });  // kind "chip" = Crimson italic on bone (our "vs")
TT.ground(tl, S(cut));            // steel block (left), ember block (right), steel ring arc draw-on, document collage ground
TT.build(tl, [T(w1), T(w2)]);     // one cue per item: 12 fps torn-ink slap (3 steps) + bone tape strip
TT.push(tl, S(a), S(b), 1.05);    // slow push
TT.through(tl, S(t), 0.5);        // optional push-through into the first bar, ends on full ink black (#16130f)
```
Ground = paper_cream_02 + EO 14157 p1 / FTO designation p1 (real docs, `assets/cartels/docs/`) multiplied at ~0.3 + newsprint + stained paper.
No glow (paper). Bars: Haskoy 800 bone on ink with halftone multiply, torn clip-path from `FX.rng(seed)`.

## Checks
- lint (`npx --yes hyperframes@0.8.217 lint compositions/cts02.html`): 0 errors, 5 warnings (nested media data-start = local, intended;
  duplicate img = the two tarmac layers; file length).
- `sync_audit.py --transcript transcript_ct.json`: 0 flagged; 21 cues at −0.06 (two show +0.02 only because the audit pairs them with the
  neighbouring "the": 81.45 = "Mexican" 81.51, 130.62 = "Silicon" 130.68).
- Timeline dump (headless, seek 0→90.75): `tl.duration() = 90.75` = DUR, no runtime errors.
- Snapshots of every shot (start/middle/end) and every cut ±0.05 s looked at; no empty/black frames (the 117.05 cut lands on the
  intended ink-black push-through; table opens with the first polaroid already landing).

## Assets
Shared: people/meza_fbi_photo_1, mencho_mugshot_2 (1986 SFPD/DEA), zambada_1, guzman_booking_1, meza_sedena_tarmac_1; footage
x_chihuahua_narcolab_a, x_boat_strike_secwar, x_maduro_stairs_stewart; docs d01/d02 p1 (title texture); kit sinaloa_relief + americas_night.
Mine (`assets/cartels/cts02/`, 4.4 MB, SOURCES.md): CIA seal + Great Seal (PD), 5 Commons photos of northern Sinaloa/Culiacán (CC BY/BY-SA,
credited on screen), caribbean_night crop, 3 print stills.
Deviations: no CIA seal on the April card of the board (the seal is on the lab footage instead); Caro Quintero not shown (no photo in
people/) — "biggest names" = El Mayo + El Chapo; the 1990s are carried by the timeline strip (photos are modern, never labelled 1990s);
the Mexico-wide `mexico_*` map was not needed (the Sinaloa crop covers every place named).

## For the lead
- cts01 should end on the same Isidro file: CT.file ember, tag "Sinaloa", rows [List: FBI Ten Most Wanted, Reward: $5,000,000], stamp
  CAPTURED (cts02 sets the stamp state directly, no slam). If cts01 uses different rows, change `fA` rows here to match.
- Gotchas: `make_sandbox.sh` doesn't link `vo_ct.mp3`/`transcript_ct.json` (link them by hand). Kit OSM state paths are clipped to the crop —
  the clip edge forms a >400 px jump, so an antimeridian "jump" filter drops the whole state (keep it off for regional kits).
  Push-through scale origins computed from `offsetLeft` at build time are unreliable (fonts not yet loaded): end the move with a black
  cover fade instead.

## Fix round 1 (2026-11-22, Agent A) — FIXES_ROUND1 #7 (intro packaging) + English on screen
Timeline v1 unchanged (DUR 90.75, every text cue on its v1 word).
- Board opening (68.17–75.6), a move every ~2 s: hold+push → fast pull-back 68.85 (1.7 s) → 12 fps punch-in on "very, very" 71.93 →
  whip-pan down to the earlier cases (prints) on "this has happened before" 73.85 → El Mencho's file 75.55 (as before).
- NEW Tapalpa insert 80.90–82.62 ("killed in a raid by the Mexican army"): hard cut to the Infobae aerial (m3_tapalpa_aerial_a media
  5.6–7.45; true place, not the exact cabin), CT.dateTag TAPALPA, JALISCO · 22 FEB 2026, credit Infobae; hard cut back to the file
  (RAID row already typed, INTEL types on 82.65 as before). This clip is used twice in the video (also cts08) — within the rule.
- NEW trailer strobe 112.625–113.25 ("Is this a war…"): 2-frame B/W flashes (fire, burning street, El Mencho, lab, boat, Maduro, the
  arrest) with 1-frame board gaps, flash on 113.21 → TITLE slam 113.29 (unchanged cues).
- Title beat: second hit on "working?" (116.01: 12 fps punch of the type row + flash) before the push-through; out of black faster
  (0.3 s, was 0.7) into the tarmac photo.
- ENGLISH: the tarmac photo now starts at scale 1.2 (→ 1.32) so SEDENA's Spanish watermark ("Defensa · Secretaría de la Defensa
  Nacional", top-left) is out of frame. Rest of cts02 checked: board/prints/polaroid captions are English or place names; the lab credit
  "Fiscalía de Chihuahua" is a proper name; soldiers' vest lettering (EJÉRCITO / GUARDIA NACIONAL) is incidental unit names.
- Checks: lint 0 errors / 6 warnings; sync_audit 0 flagged; headless dump DUR 90.750, seek 0→90.75 no errors; snapshots looked at:
  0.4, 2.5, 4.0, 6.0, 12.68/12.78, 14.40/14.50, 17.3, 44.48–45.13 (strobe + title cut), 47.95, 48.95, 49.6.
