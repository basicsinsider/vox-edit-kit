# cts13 — THE AFTERMATH (master 1192.625–1286.292, DUR 93.667) — editor notes

Plan with exact word cues: `project/cartels/EDIT_NOTES_cts13.md`. 15 scenes, every second covered, no empty grounds.

| scene | what | effect · ref |
|---|---|---|
| sc001 | real front pages of Sat 21 Nov 2026 (Reforma, Milenio, El Informador, El Debate) drop on a dark desk → push onto El Debate's "Ahora Guasave: noche de terror…" | stop-motion drops, camera push, focus hunt |
| sc002 | Los Mochis smoke columns that night (blur-fill card), dateTag LOS MOCHIS · 20 NOV 2026 | whip |
| sc003 | diptych: burning car ("burning") + burning blockade on an empty avenue ("blocking roads") | hard cut on action |
| sc004 | sinaloa_night: northern Sinaloa in ember, Mex 15 drawn, fire pins at the 4 blockade municipalities named by SEDENA's communiqué (Ahome, Guasave, Guamúchil, Navolato), push to Guasave where a gas-pump and a store glyph catch fire | map fill + route + radio rings · ref ast_d02865717c824c47 |
| sc005 | ★ ballpark callback: cts01's fan card (same position/size/grade as cts01 sc002) rewinds (12 reversed stills + tracking lines) and plays again | rewind |
| sc006 | the real AP report on npr.org (firefighter Paola Sánchez, "thousands … took shelter … in grocery stores") | text contrast call-out (veil + key-word wipe) + pen underline |
| sc007 | Infobae (21 Nov 2026), real headline "Hombres armados irrumpen en clínica del IMSS en Guasave y obligan a médicos a atender heridos" (shared news/n01_infobae_imss), camera push + pen underlines on its two clauses as Sam says them; no "public" label | paper desk · pen underlines |
| sc008 | "while all of that was going on": split fires (AJE) / SEDENA's plane boarding, the plane panel takes the frame | split screen |
| sc009 | mexico_night: olive Air Force flight Sinaloa → MEXICO CITY with plane glyph (SEDENA: "aeronave de la Fuerza Aérea Mexicana") | route draw |
| sc010 | ★6 SEDENA's real post (9:44 AM · 21 Nov) → push into its video, the real 30.8 s video takes the thumbnail's place; bar + "0:30" (yellow key number) on "30 second"; spotlight on the cuffed hands, then the lowered head | focal call-out |
| sc011 | rebuild of ref ast_0455523fccc84f71: Amb. Ronald D. Johnson's official portrait in B/W on steel blocks, cards FORMER GREEN BERET / CIA seal + CIA OFFICER | paper collage |
| sc012 | his real post (screenshot header) + pull-quote of the REAL wording, word by word with Sam: "Results like these don't happen overnight. They are built on sustained cooperation and trust. […] We will continue the hunt." — pen underlines | §10.7 quote |
| sc013 | north_america_night: MEXICO CITY (olive, his FBI photo token) → pull back north, steel arc to WASHINGTON, D.C. | camera pull-back |
| sc014 | CT.file (ember, CAPTURED): rows CHARGED · Washington DC, 2012 (highlighted) / EXTRADITION · Requested by the US | motif |
| sc015 | callback to cts06's prisoner waffle (same 10-col 52/62 px grid, ember batch colours, title, legends, DOJ cards, "92" label-box) refilling 29/26/37; slot #93 blinks + pen circle on "special treatment" | isotype · cts06 design |

Checks: lint `0 error(s), 12 warning(s)` (nested media basis / duplicate-media / file length — same as other segments); `sync_audit … 0 cue(s) flagged`;
`tl.duration()` = 93.667 (headless dump); hold audit: every key animation ends ≥ 0.5 s before its cut (only camera drifts/ambient run through).
Snapshots looked at: every scene start/middle/end and every cut at ±0.05 s.

Accuracy decisions: quote = Johnson's real post text (x_json `USAmbMex_2124198738474508514`, "sustained", not Sam's "constant"); clinic = Infobae's real headline
(IMSS clinic), no "public" label; "90 some" → 92; blockade places from SEDENA's communiqué; flight origin drawn from "Sinaloa" (departure airport not
public), no Guasave airport claim; slot #93 is only an open slot (no claim).

Assets: mine in `assets/cartels/cts13/` (SOURCES.md; 1.7 MB): NPR page capture, map overlay PNGs (`project/cartels/gen/cts13/map_assets.py`), rewind stills, CIA seal (PD). Shared: see SOURCES.md last line.
Footage reuse: x02 post, x_isidro_plane_boarding (different window, 4.5–8.1 s) and m1_kuroda_fans_a are each their 2nd use (cts01) — by design (callbacks).

Gotchas for the lead / MANUAL:
- Labels positioned by a map-camera `onUpdate` must use `left/top`, not GSAP x/y — a `rise()` on the same label overwrote its x/y (SINALOA jumped to the frame top).
- `<img>` elements created in the script were not drawn in snapshots in time for an early frame (rewind stills showed black); static `<img>` tags work.
- `FX.textCallout` dims the page by opacity — on a white web page over a dark desk that turns the page grey; a paper-white veil between the page and the
  key-word copy (pass a dummy `dimEl`) gives the Vox look.
- `work/cts13` sandbox needs `vo_ct.mp3` / `transcript_ct.json` symlinks (make_sandbox.sh doesn't link them yet).
