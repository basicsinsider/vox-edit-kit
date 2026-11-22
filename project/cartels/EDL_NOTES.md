# US vs Cartels — VO clean-up (EDL), what was removed
Raw `us vs cartels.wav` 1486.155 s (24:46) → cut VO 1341.87 s (22:22): **144.3 s removed**, cuts only (quietest 10 ms, 4–12 ms fades,
float samples copied untouched — no EQ / compression / gain / normalisation). Tools: `project/cartels/gen/edl_keep.py` (phrase-anchored
keep list) → `build_edl.py` → `render_vo.py`; every removed span is in `project/cartels/EDL.json`.

| type | count | time removed |
|---|---|---|
| Repeated phrases / retakes (best take kept) | 24 | 73.3 s |
| Flubs, false starts, restarts (e.g. "But in tot, but in 2008", "Military has strict… The military has strict", "the CI int…", "bull the US military started", 3 stuttered "But on one raid on a cart…") | 15 | 35.2 s |
| Long dead pauses inside kept lines (any silence > 0.8 s cut to 0.5 s) | 40 | 30.0 s |
| Pauses at the joins between kept lines (no words removed) | 6 | 5.0 s |
| Leading/trailing silence | 2 | 0.8 s |
| Ums / ahs | 0 | — |

Ums/ahs: none found. Parakeet omits fillers, so every gap ≥ 0.15 s between words in the cut VO was scanned for voiced sound (pitch
periodicity): 8 candidates, each re-transcribed with Whisper on a 3.6 s window — all 8 are tails of real words (e.g. "original **El**
Chapo", "$5 million"), none is an um/ah. A full Whisper pass of the cut VO found no fillers and no stuttered repeats (6 adjacent-word
repeats are normal sentence joins: "…now. Now let's…"). One natural pause of 0.88 s remains at 4:45 ("…with machete. And if you think…").
Checks: a fresh Parakeet transcript of the cut VO matches the intended words (ratio 0.991); two leaked fragments at joins ("he had BEEN
already", "American PIT prison") were found that way and fixed before the edit. Kept on purpose (Sam's words, audio untouched): "100,000
troops" (record 10,000 — not shown on screen), "Liberation Day", "unlike China…", "15 miles", "top state prosecutor", "90 some".
