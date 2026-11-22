# cts12 — THE NET CLOSES (master 1078.417–1192.625, DUR 114.208) — editor notes

Plan: `project/cartels/EDIT_NOTES_cts12.md`. 13 scenes (the NET scene is shown twice: sc001 and the sc006 callback). Derived assets:
`assets/cartels/cts12/` (+ SOURCES.md), generator `project/cartels/gen/cts12_assets.py`.

| scene | master | build | ref |
|---|---|---|---|
| NET/sc001 | 1078.42–1090.30 | real CSS-3D relief plane (northern Sinaloa, kit relief) tilted 52°, portrait cards stand up on stalks (rotateX −52 inside a preserve-3d map), ember strings, olive dashed net ring; camera flies to El Pichón's card: KILLED, flat overlay (Secretaría de Marina · name · 30 Nov 2025) | ast_3c804bab5fc04bfb |
| sc002 | 1090.30–1095.40 | paper case board: El Pichón (KILLED) → string "Father" → El Sagitario, olive ARRESTED, 31 Dec 2025 · Culiacán | collage |
| sc003 | 1095.40–1100.00 | North-America night map: Mexico City → San Diego arc + plane, dateTag "Sent to the U.S. · 20 Jan 2026" | map |
| sc004 | 1100.00–1103.75 | three anonymous ember "Financial operator" cards flip face-down one at a time (12 fps) | — |
| sc005 | 1103.75–1114.05 | **CT.file** Jesús González Peñuelas "Chuy Peñuelas" (ember, NO PHOTO): Number two / U.S. reward $5,000,000 (yellow) / Navy raid 26 Oct 2026, KILLED | TARGET FILE |
| NET/sc006 | 1114.05–1116.90 | callback: every network card now stamped (KILLED/ARRESTED/GONE) drops away, the net tightens round Isidro | ast_3c804bab5fc04bfb |
| sc007 | 1116.90–1134.98 | White House APEC photo (Sheinbaum + Trump), name tags, dateTag "APEC · Shenzhen · 18 Nov 2026"; photo drops to a lower band under the real Infobae headline: pen under "acuerdo comercial bilateral" on "trade", ember pen under "cárteles controlan México" + translated line; article lifts, push in on the two | ast_50e87a4cab8146d1 |
| sc008 | 1134.98–1144.15 | typeset calendar NOVIEMBRE 2026 (Mon-first, 1 Nov = Sunday), pen circle VIE 20 on "Friday", olive wash + "DÍA DE LA REVOLUCIÓN" tape | — |
| sc009 | 1144.15–1147.00 | SEDENA armored convoy (hard cut) | footage |
| sc010 | 1147.00–1150.35 | El Universal photo of special forces (band on blurred fill) | — |
| sc011 | 1150.35–1159.90 | torn ink title bars on paper + olive block: LOBOS (+WOLVES tape) / MURCIÉLAGOS (+BATS), unit labels | ast_e1ede4fafbd84a66 |
| sc012 | 1159.90–1180.00 | tactical map on the night-graded Guasave z16 aerial: scan rings + reticle lock (no address claimed), 4 dashed olive arrows, outer/inner security rings (SEDENA wording), ember muzzle flashes, arrows push through | ast_d02865717c824c47 (tactical) |
| sc013 | 1180.00–1185.99 | **CT.file** Isidro (FBI photo) stamped **CAPTURED** on "arrested"; slides left, olive cards: Germán Rolando Gálvez Meza "El Serafín" (New number two) and José "N" (Financial operator, full name not released) | TARGET FILE |
| sc014 | 1185.99–1192.625 | still from SEDENA's arrest video inside the house (bare white walls), slow push, contrast call-out on the wall, dateTag "Guasave, Sinaloa · 20 Nov 2026" | — |

Accuracy: the two "number twos" are kept apart (Chuy Peñuelas = ember file, killed, Oct 2026; El Serafín = olive card, arrested with him).
Sam's "first time" → no "first" text. "National holiday" → calendar says Día de la Revolución only. The 3D net is a diagram: only Guasave
is pinned (no sierra pin for El Pichón, no locations for the others). Money people anonymous (names UNVERIFIED in RESEARCH).

Deviations from the lead's plan: (1) the "ending" CT.file CAPTURED sits at "arrested" (1180.25) — the words after it (the number two, the
money man, the house) get their own visuals; (2) the house is not 2.5D: the only true picture of it is SEDENA's 816×464 video — I used a
still (cts13 plays the same video 0–9.45 s; I avoided playing it here); (3) no wolf/bat glyphs (not drawn by hand — text + tapes only);
(4) "Narco"-style unit logos not used (none in the shared assets).

Checks: lint 0 errors (7 warnings: nested media start basis, duplicate fill/card media, getProperty in follow() callbacks, file size);
sync_audit 0 flagged (all text cues −0.04…−0.06 s); headless dump `tl.duration()` = 114.208, no runtime errors; every scene and every cut
(±0.05 s) snapshotted and looked at.

Gotchas for the lead/MANUAL: (a) cards standing on a CSS-3D tilted map need `transform-style: preserve-3d` on EVERY wrapper between the
tilted plane and the card (a plain host div flattens them back onto the ground); (b) `FX.focusHunt` sets a CSS filter — on a preserve-3d
element it flattens the whole 3D scene (cards lay down again); apply it to the shot wrapper outside the perspective root; (c) a scene shown
twice through `FX.whip` keeps the outgoing whip's x offset — reset the shot (`x:0, y:0, scale:1, filter:none`) before its second window;
(d) the APEC photo in `people/` is the Commons White House file (CC0) — `people/SOURCES.md` was still missing when I built this.
