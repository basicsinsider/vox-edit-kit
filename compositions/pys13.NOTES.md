# pys13 — NOTES (editor pys13, 2026-11-08) — THE FINALE, master 1456.50–1621.87 (DUR 165.37)

Plan: `project/paraguay/EDIT_NOTES_pys13.md` (40 scenes, every second covered, words → picture reason). Built from a small template +
macro builder (scratchpad), output `compositions/pys13.html`. Lint: 0 errors for pys13 (only the repo-wide `nested_media_start_basis_ambiguous`
warnings every segment has). `tools/sync_audit.py --transcript transcript_py.json`: 0 flagged — every text cue = word start − 0.06.
Timeline: DUR 165.37 (FX.mount). Snapshots of every scene looked at (11 batches ≤ 8 frames).

## First / last scene
- First: sc001 FACE W (fresh shot; pys12 ends on a gavel into it). Face cam starts at media 1456.54 (the EDL join is at 1456.517 — avoids one frame of the previous take piece).
- Last: sc040 DESIGNED ENDING — the "tax the poor" post (face blurred) goes viral (hearts pop), then on "adding more fire" it BURNS AWAY (burn_b feImage
  threshold + ember ring) into the protest fire footage (silhouette with raised arms); "already mad about" lands at 1621.26; fade to night 1621.50→1621.87.

## Effects / layouts used
2.5D (sc008 hero: ueno sign letters cut out over an in-painted plate, dolly, "lights out" flicker at 12 fps on "done"; halate hero title) ·
whips ×9 (incl. light-flash sc015, vertical sc013/035/040) · paper slide (sc019) · cut on action (phone push → ATM, crowd push → closed branch,
montage, directors → car) · rubber stamps (A BAD BANK, UNDER ARREST) · pen markups (ballot ticks, jar + return arrow, receipt strikes, circle on the
vote board, circle on "Tax The Poor", box round the ueno tower) · isotype-ish ballots (unanimous vote) · our own phone-app UI (PIN → spinner →
error toast → balance dash; no real ueno branding) · portrait-video cards over blurred fills (ATMs, Regimiento) · landscape phone frame (resignation
video) · counter + label-box key number ($1,500 yellow) + notes stack + month strip · case card on stained paper (Vázquez) · tilted newspaper page
with push + focus hunt (ABC Color homepage) · map (americas_night kit + Paraguay tierra fill + US outline, PARAGUAY / UNITED STATES / Asunción /
New York labels counter-scaled in screen space, dashed route drawn dash-by-dash) · censor stamp beat on the face cam (#$%!) · burn-away reveal ·
fade to night. New layouts: till receipt (sc015), app-outage UI (sc009), plum "state takeover" wash on a building (sc004).

## Face cam
sc001 W, 005 W, 006 M, 007 C, 011 W, 014 C, 016 M, 020 W, 021 C, 025 C, 027 M, 032 W, 034 M, 036 C, 038 W = 55.2 s / 165.37 s = **33 %**.
All shots start/end on or between EDL joins (none crosses one); first 0.3 s / last 0.55 s of every shot checked frame-wise (he is talking, no
reaching/glancing). Face-cam framing origin moved to 1000,150 (220 cropped his hair at C 1.55).

## Deviations / decisions
- **The 1.5 s hold past the last word is not possible inside DUR 165.37**: the master ends 0.15 s after "about." (1621.72); SOUND_PLAN P13 also says
  "no hold beyond the master". The ending image is established from 1619.10; fade 1621.50→1621.87. If the lead pads the VO, extend sc040 + the
  `#pys13-night` fade (last tween in the script).
- Lead's notes honoured: no uh_directivos_tacumbu, no Peña drone clip. BCP press conference: pys12 uses board_a 2.0–6.35 + board_b 0.5–6.15, so I
  use only board_b 29.4–35.6 (Carvallo named on screen = "the head of the board") and 10.0–14.8 (regulators); the "take it over" beat is a graphic
  on the ueno tower photo instead of board footage. carvallo_fiscalia: pys10 uses 0.4–3.5 → I use 13.0–17.1. Resignation video: pys01 uses 20–23.4 → I use 5.5–11.1.
- ueno_sign_hq_reuters.jpg is also used in pys01/03/06 — here it is the 2.5D hero with a lights-out treatment (different look); swap if the lead prefers.
- Peña "house arrest" (his words) over the Regimiento gate footage (where press says he is held) — as the brief suggests.
- "they can wait for weeks or months" — on screen only "weeks or months". "they don't have any of their accounts" (sc020) — no text (ambiguous slip).
- Brief mentioned "maybe another bank / cash payouts" — the narrator does not say these in the take, so no text for them ("we don't exactly know").
- "Paraguayan" spelled correctly (ASR "Peregrine"); "Ueno" (ASR UNL / "one oh").

## Bleep
sc036: censor stamp "#$%!" (ink box, bone border, 2-step punch + shake) at T(1600.54); sfx marker {"type":"bleep","t":1600.60,"dur":0.24}.

## Assets
`assets/paraguay/pys13/SOURCES.md` (15 footage trims, 2.5D layers, blurred story, map overlays). Private person (president's daughter): face + hair blurred in
the derived image; credit line says "face blurred".

## Gotchas for MANUAL
- A plate under a 2.5D cut-out must have the subject IN-PAINTED (masked normalised blur: blur(img·keep)/blur(keep)) — then the plate can be scaled
  independently of the cut-out to cover the frame during the dolly; without it the cut letters ran off-frame or doubled.
- Per-layer `transform-origin` = (perspective-origin − layer left/top) so `scale = (P−z)/P` keeps the rest frame identical.
- Burn-AWAY with the c3s01 filter: tween the alpha offset 13 → −2.6; keep the ember ring narrow (second matrix offset +0.8, not +2.2) or the
  ring paints big flat orange blobs.
- Telefuturo/NPY clips: the lower third starts ≈ 66 % of frame height and a weather/logo bug sits top-left/right — scale 1.75 with origin (x, 25 %).
- Haskoy renders "#$%!" fine (checked); Haskoy's em-dash is tiny — draw a bar for a "—" balance.
- Mixed vertical clips (720×960): portrait card over a blurred still of the same subject reads better than a 2.7× cover crop.
