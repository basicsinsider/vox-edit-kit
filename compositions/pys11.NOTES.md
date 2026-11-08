# pys11 — NOTES (master 1207.80–1294.50, DUR 86.70) — the report reaches ABC Color → media not government → pressure → Senate asks the BCP

Plan: `project/paraguay/EDIT_NOTES_pys11.md` (20 scenes, built as planned). Assets: `assets/paraguay/pys11/` (+ SOURCES.md), made by
`project/paraguay/gen/pys11_assets.py` (crops of the shared ABC screenshots; no new downloads).

## Scenes as built
| id | master | picture / effect |
|---|---|---|
| sc001 | 1207.80–1214.10 | FACE W, "this whole thing / fall apart" (first 0.12 s = still of the 1207.92 frame: EDL join at 1207.92) |
| sc002 | 1214.10–1218.25 | night desk, tear-off calendar: pen X marks march across two month sheets (12 fps), each sheet torn off; "two months after" |
| sc003 | 1218.25–1222.18 | paper org chart: plum BCP box → dashed department box; the author (plum, holding the report) slides out; "wrote this report" → "moved out of the department" |
| sc004 | 1222.18–1224.34 | FACE C |
| sc005 | 1224.34–1231.22 | Vox layered night (3 dark blurred ABC pages drifting at different speeds); the BCP memo card travels along a dashed pen path onto a newsprint stack; "somehow, some way" → "a newspaper in Paraguay" |
| sc006 | 1231.22–1235.38 | ABC Color logo pop + focus hunt over the blurred real homepage; "one of the oldest / and one of the biggest" |
| sc007 | 1235.38–1238.50 | FACE M |
| sc008 | 1238.50–1242.34 | **HERO newspaper** (MANUAL §5 #5): real ABC article (14 Sep 2026, "Senado acorrala al BCP…", about the BCP supervision memo) on a tilted 3D page, newsprint tint, halftone growing with the push, page → headline → body, rough yellow highlighter (two strokes) on "memorándum de la Gerencia de Supervisión del Banco Central del Paraguay"; "they published it" |
| sc009 | 1242.34–1246.82 | cork investigator's board: the report card centre + 5 real ABC follow-up clippings + ueno logo pinned stop-motion, red strings; label-box "everything else" |
| sc010 / sc011 | 1246.82–1252.02 / –1254.70 | FACE W "because of the media" / FACE C (framing change inside one take) |
| sc012 | 1254.70–1257.71 | paper slide: timeline — ABC logo + "now" dot, dashed line drawn far right as the camera pans to a plum government icon; "later down the line" |
| sc013 | 1257.71–1264.20 | FACE M "just happened last week" → "thanks to the media" (cut exactly at the 1264.20 join) |
| sc014 | 1264.20–1269.47 | modern phones on night with the real ABC articles: one phone, then three more slide in; "made public" → "subsequent investigations" |
| sc015 | 1269.47–1272.51 | Congreso Nacional at night (plum duotone): a jagged crack draws through it and the two halves shift apart (clip-path halves); "breaks the political back" |
| sc016 | 1272.51–1281.39 | paper: plum "political pressure" slab comes down (12 fps) on three cards: the central bank (BCP photo) / the president (Peña) / anyone else (silhouettes, dim on "not speaking up", the card leans toward Peña's on "side of the president") |
| sc017 | 1281.39–1284.40 | Congress facade photo card (plum duotone) over its blurred copy; "senators from his own party" + kicker PARTIDO COLORADO |
| sc018 | 1284.40–1289.71 | flat torn clipping of the same real ABC article (different treatment from sc008): pen circle on "Senado", label-box "request an investigation" → "ask the central bank" with the highlighter on "cuestionario que el Senado envió a la banca matriz" |
| sc019 | 1289.71–1291.57 | FACE W "is this bank actually good?" (cut at the 1291.57 join) |
| sc020 | 1291.57–1294.50 | ueno tower aerial (Reuters), push accelerating into the cut; "one of the biggest banks" |

Transitions: whips (horizontal, vertical, light-flash), hard cuts on action, paper slides — never the same twice in a row.
Grounds: face / night / paper / face / night / night / face / news / cork / face / face / paper / face / night / night / paper / night / paper / face / night (≤ 3 in a row).

## Effects & layouts used
Tilted 3D newspaper + halftone + camera push + highlighter (hero), flat newspaper clipping + pen circle + highlighter, Vox layered backgrounds,
cork board (ref 9) with stop-motion pins and string, org-chart diagram with pen strokes, stop-motion tear-off calendar (new), phone screens,
crack/split photo (new: clip-path halves + PEN-filtered jagged path), plum "pressure slab" diagram (new), focus hunt (sc006, sc008, sc009),
label-boxes, word-by-word text, duotone tints (plum = power), whips ×3 kinds, cut on action.

## Face cam
sc001 6.30 + sc004 2.16 + sc007 3.12 + sc010 5.20 + sc011 2.68 + sc013 6.49 + sc019 1.86 = **27.81 s / 86.70 s = 32.1 %**. Every shot sits between
EDL joins (1207.92, 1218.25, 1244.20, 1264.20, 1291.57); edges checked frame by frame (he is mid-sentence at every edge, no mouse/glance).
Framings: transform-origin now per framing (C 1000/110, M 1000/150, W 1000/220) so the close-ups don't crop the top of his head.

## Checks
lint: 0 errors in pys11 (repo-wide errors are other compositions' missing facecam files); warnings only duplicate-img + file length.
sync_audit: 0 flagged; every text cue = literal word start − 0.06 (8 lines show +0.02 because the audit matches a short neighbouring word).
Timeline duration 86.70. Snapshots of every scene looked at (start / middle / end).

## Deviations / open issues for the lead
- **"Partido Colorado" kicker** in sc017 is a name label (he says "his own party"), per the brief; drop it if Krish wants only his words.
- **Senate photos**: the shared Senate chamber photos are the Nov 2026 impeachment votes / a named opposition senator (Hugo Richer, Frente Guasu),
  so sc017 uses the Congress building facade instead — no individual is falsely shown as a Colorado senator.
- The same real ABC article (14 Sep 2026) appears twice (sc008 hero page: the memo = "the report"; sc018 clipping: "Senado acorrala al BCP" =
  the Senate pressing the BCP) — different treatments, and it is the article that literally matches both lines. The infographic
  "US$ 779.008.660" was not used (his words never give that number); the 780 M headline appears only as a small cork clipping.
- sc019 ends 0.1 s after the last word's text lands (the EDL join at 1291.57 forces the cut); sc003's last word holds 0.41 s.
- sc005/sc006 backgrounds are deliberately dark (tinted blurred ABC pages) so the bone text reads.
- Face still `derived/face_still_1207_92.jpg` comes from the gitignored face cam (138 KB) — commit it or regenerate with
  `ffmpeg -ss 1207.93 -i assets/facecam/paraguay_facecam_master.mp4 -frames:v 1 -q:v 2 …`.
First scene: face W (fresh shot). Last scene: push into the ueno tower still accelerating at 1294.50 (cut-on-action hand-off to pys12).

## Gotchas for MANUAL
- A dashed line can't be "drawn on" with dashoffset (the dash pattern is the dasharray): draw it with a mask path of the same `d` whose own
  dashoffset animates (`ink(..., {dash})` in pys11 — mask with `maskUnits="userSpaceOnUse"` and a big region).
- Splitting a photo along a drawn crack: two copies of the photo with complementary CSS `clip-path: polygon()` built from the same jagged point
  list (offset by the half's inset), then move the halves apart; the crack path itself on top with the PEN filter.
- Face-cam C framing with origin 1000 220 cropped the top of Krish's head in this take; origin y ≈ 110 for C, 150 for M keeps the head in.
- An EDL join 0.12 s after the segment start: hold a still of the post-join frame for those 3 frames instead of shifting `data-media-start`
  (keeps lip sync exact).
