# x01 · Russia → Saint Petersburg drone strike → "90% lost their home" (sample, 18 s)

Built from the user's R12-style reference (grey relief map, country in red + halftone + glowing edge, tilted plane).
Edit `tools/x01_template.html`, then `python3 tools/gen_x01.py` (inlines `assets/maps/russia/russia_spb.json`).

| time (s) | beat | effects |
|---|---|---|
| 0.0–2.7 | Russia on a grey relief map (tilted 20°), fills vermilion from the centre with halftone + glowing edge; RUSSIA rises in | R12, #3, #4, #13 rise |
| 2.7–5.9 | log-space push ~100× into Saint Petersburg through 3 nested relief maps; pin + label (random letters) | #3, #13 random |
| 5.0–11.4 | 300 drones from the west / south-west over the Gulf of Finland; ~72 % shot down (interceptor streak from 7 air-defence sites + air burst), the rest strike: flash, shock ring, camera shake; the urban area burns red (halftone, charred cores, embers), smoke drifts east | #3, #20, #18-style halftone |
| 11.4–11.8 | paper sheet slams in at 12 fps with a torn leading edge | transition |
| 11.85–18 | R1/R6 bars on paper: "Who *lost* their home"; vermilion bar to 90 % (watercolour top, ink label box counting 0→90 %), navy 10 %; Vox markup arrow "nine in ten" + rough circle on 90 % | #2, R1, R6, #13 count, #19 |

Open points
- **No voiceover yet**: cues are scene seconds (`T()`/`S()` = identity). When the narration exists, set the window and
  rewrite text cues as `T(vo)` on the spoken words, then run `tools/sync_audit.py`.
- On-screen words are placeholders until the narration exists ("Who lost their home", "nine in ten",
  "Still have a home 10%"). Change them to the narrator's exact words.
- No sound (samples leave point 6 out). SFX markers for the full edit: whoosh on the zoom, drone buzz bed, pops on
  intercepts, low booms on strikes, burn crackle, paper slam, bar ticks, marker scratch.
- No Cyrillic in our three fonts, so there is no "Россия" line like the reference's 中国.
