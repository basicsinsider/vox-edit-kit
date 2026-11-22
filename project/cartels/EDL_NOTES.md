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

## Fix round 1 (Frame.io review 2026-11-22, Agent V) — VO timeline v1 → v2
Comments read headless from https://f.io/2aztAOX5 → `project/cartels/review1_comments.json` (19 threads, numbers 1–21, replies kept).
All changes are TIMELINE OPS on v1 (`project/cartels/fix1_ops.json`, chosen by `tools/ct_fix_cuts.py`), applied identically to the VO
(`tools/ct_fix_remap.py` → `work/fix1/vo_v2.wav`, `vo_v2_master.wav`, `transcript_v2{,_vo}.json`, `sfx/`, `music_cuesheet_v2.json`, `map.json`)
and to the picture (`tools/ct_fix_assemble.py`). Every op = whole frames on the 24 fps grid; audio joins = 6 ms equal-power crossfade
(10 ms inside the /s/ of #12) taken from the removed span, samples otherwise untouched; picture = the same frames removed.
**v2 = 4.5 s cold open (cts00, preroll 108 frames) + map(v1)**: v1 1341.917 s (32206 fr) → 1310.625 s (31455 fr) + 4.5 = **1315.125 s (31563 fr)**.

| type | ops | removed |
|---|---|---|
| pauses after a sentence (silence < −55 dBFS ≥ 0.30 s → 0.36 s left) | 96 | 17.375 s |
| pauses at a comma (→ 0.28 s) | 31 | 6.000 s |
| mid-phrase hesitations (→ 0.22 s) | 29 | 5.333 s |
| #4 repeated "and he controls the routes," | 1 | 2.083 s |
| #12 over-long /s/ in "gets" (inside the fricative) | 1 | 0.208 s |
| #18 voiced mouth sound in a pause ("anybody. ⟨x⟩ As long as") | 1 | 0.292 s |
| **total** | **159** | **31.292 s** (no insertions) |

Rules: deletion ≥ 60 ms after the word's decay and ≥ 80 ms before the next onset; only removals ≥ 3 frames; position = minimum visual
jump on the delivered 720p. Not cut: 7 pauses that sit entirely inside a fast picture move / whip / title reveal (116.58 title card,
158.50, 303.38, 702.17, 818.63, 1045.25, 1249.83 — jump 16–92 on a 0–255 scale). Checks: every op re-transcribed ±3 s with and without
it (Parakeet + Whisper, `tools/ct_fix_check.py`); the windows flagged by the concatenated runs were re-run alone (`single`, both engines) —
all differences were window-edge words or ASR noise (Parakeet returns 0 words for some short files — re-padding fixes it). Global check:
full-length ASR of vo_v2 vs v1 — Whisper: the only word change at a join is the intended #4 deletion; Parakeet: same (other diffs =
spelling/number variants and chunk dropouts ≥ 2 s from any join, re-checked).

Review notes (v1 → v2 master TC):
- #6 1:09 "dead space" → v2 1:11: "Now, [0.80 s] if this was…" cut to 0.28 s + 3 more pauses within 8 s (−0.92 s); #15 4:50 → 4:44 and
  #14/#15 area "with machete [0.68] and [0.57] if you think about his line of work, [0.65] which…, [0.71] kinda" all tightened (−1.4…−1.6 s
  per 8 s); #9 6:58 → 6:49 and the whole VO: 156 pause ops.
- #4 3:56 → 3:52:23 (join at 3:49:10): 1st "and he controls the routes," deleted v1 230.625–232.708 (50 fr). The picture loses the same 2.08 s of the
  cts03 Sinaloa map zoom-out (visible jump in the move — cts03's editor may want to ease that move).
- #12 3:35 "gets" → 3:34: NOT an edit (v1 = raw sample-exact, nearest join 8 s earlier): the raw take has a 380 ms /s/ (ZCR 7 kHz) after a
  120 ms vowel ("ge…ssss"); 5 frames of the steady hiss removed with a 10 ms crossfade → 170 ms /s/; Parakeet + Whisper still read "gets".
- #14 4:45 "machete" (t silent): the raw has ONE take ("…clearing bushes with Mache.", raw 310.47; Parakeet raw, Whisper small.en v1,
  Whisper medium.en raw 296–322 all hear "mache"; no pickups at the end of the raw) → no swap possible; needs a re-record from Sam
  ("…clearing bushes with a machete") — for Krish.
- #18 9:59 → 9:45:15 (the join at 9:44:20): a 160 ms voiced mouth sound in the pause after "anybody." removed (598.000–598.292); a scan of every word gap ≥ 0.15 s
  for voiced non-word sound (periodicity > 0.6, > −46 dBFS, ≥ 80 ms) found no other one (5 hits = word tails).
- #20 15:08 "he ends up other CIA officers" → v2 14:51:19: NO words were cut — v1 903–912 is sample-identical to raw 999.3–1008.3 (max diff
  0.0 at lag 0), no EDL join between 897.3 and 921.7; raw Parakeet, v1 Parakeet and v1 Whisper all read "and then he and some other CIA
  officers start going on raids". Sam runs "he and some" together; there is no other take (raw has one) → nothing to restore; report to Krish.
- #2 / #9 levelling: `tools/ct_fix_mix.py` (see FIXES_ROUND1 rule 3). VO alone: LRA 7.3 → 5.1 LU, speech 3 s loudness p5–p95 spread
  8.1 → 5.8 LU, per-minute speech medians 4.3 → 0.5 LU apart; ride clamp −4…+6 dB (used −4.0…+3.8, p5/p95 −2.7/+2.8) around the speech
  median, ±6 s median, ±2 s smoothing — passages are evened out, the delivery inside a sentence keeps its shape. 2:04 (#2) gets ≈ +2 dB.

Every op (v1 TC (s) → v2 master TC incl. the 4.5 s pre-roll; m:ss:ff; `left` = silence left in the pause):

| # | v1 | v2 | type | length | left | words around it |
|---|---|---|---|---|---|---|
| 1 | 0:06:04 (6.167) | 0:10:16 | pause/comma | −0.250 s (6 fr) | 0.29 | a city called Guasave, | in the state of |
| 2 | 0:18:03 (18.125) | 0:22:09 | pause/end | −0.125 s (3 fr) | 0.395 | a gunfight going on. | This is what was |
| 3 | 0:31:15 (31.625) | 0:35:18 | pause/end | −0.375 s (9 fr) | 0.365 | to block the way. | All of this was |
| 4 | 0:38:06 (38.250) | 0:42:00 | pause/end | −0.167 s (4 fr) | 0.373 | man. El Chapo Isidro. | And yes, that's the |
| 5 | 0:39:09 (39.375) | 0:42:23 | pause/comma | −0.125 s (3 fr) | 0.285 | Chapo Isidro. And yes, | that's the same nickname |
| 6 | 0:43:19 (43.792) | 0:47:06 | pause/end | −0.333 s (8 fr) | 0.387 | but they're not related. | They are just as |
| 7 | 0:46:11 (46.458) | 0:49:14 | pause/end | −0.167 s (4 fr) | 0.363 | just as accomplished, though. | This El Chapo is |
| 8 | 0:57:16 (57.667) | 1:00:15 | pause/end | −0.167 s (4 fr) | 0.373 | could help catch him. | By the end of |
| 9 | 1:07:22 (67.917) | 1:10:17 | pause/end | −0.125 s (3 fr) | 0.375 | from the United States. | Now, if this was |
| 10 | 1:08:11 (68.458) | 1:11:03 | pause/comma | −0.500 s (12 fr) | 0.29 | the United States. Now, | if this was one |
| 11 | 1:13:15 (73.625) | 1:15:19 | pause/end | −0.167 s (4 fr) | 0.383 | be very, very interesting. | But this has happen |
| 12 | 1:15:11 (75.458) | 1:17:11 | pause/end | −0.125 s (3 fr) | 0.365 | this has happen before. | Just this February, the |
| 13 | 1:25:04 (85.167) | 1:27:01 | pause/end | −0.125 s (3 fr) | 0.385 | intelligence helped find him. | Then in April again, |
| 14 | 1:31:19 (91.792) | 1:33:13 | pause/end | −0.167 s (4 fr) | 0.393 | where CIA helped out. | Out in the ocean, |
| 15 | 1:36:16 (96.667) | 1:38:06 | pause/none | −0.167 s (4 fr) | 0.233 | more than 70 boats | that were carrying drugs. |
| 16 | 1:41:12 (101.500) | 1:42:22 | pause/comma | −0.167 s (4 fr) | 0.303 | January of this year, | the US flew into |
| 17 | 1:48:13 (108.542) | 1:49:19 | pause/end | −0.167 s (4 fr) | 0.393 | trafficker in the world. | So this all raises |
| 18 | 1:51:06 (111.250) | 1:52:08 | pause/end | −0.292 s (7 fr) | 0.388 | a pretty simple question. | What is going on? |
| 19 | 2:02:15 (122.625) | 2:03:10 | pause/end | −0.167 s (4 fr) | 0.383 | story explains a lot. | His name is Fausidro, |
| 20 | 2:05:09 (125.375) | 2:06:00 | pause/comma | −0.250 s (6 fr) | 0.32 | His name is Fausidro, | and he was born |
| 21 | 2:13:07 (133.292) | 2:13:16 | pause/end | −0.125 s (3 fr) | 0.375 | of Mexican drug trafficking. | A lot of the |
| 22 | 2:28:19 (148.792) | 2:29:01 | pause/end | −0.292 s (7 fr) | 0.388 | was available to everyone. | And in fact, it |
| 23 | 2:43:03 (163.125) | 2:43:02 | pause/none | −0.208 s (5 fr) | 0.222 | group of brothers called | the Beltrán Leyvas. These |
| 24 | 2:45:09 (165.375) | 2:45:03 | pause/end | −0.167 s (4 fr) | 0.373 | called the Beltrán Leyvas. | These brothers were partners |
| 25 | 3:06:22 (186.917) | 3:06:12 | pause/none | −0.125 s (3 fr) | 0.255 | there's a civil war | between the groups. When |
| 26 | 3:17:22 (197.917) | 3:17:09 | pause/none | −0.125 s (3 fr) | 0.245 | the guy in charge | of shooting and killing. |
| 27 | 3:19:15 (199.625) | 3:18:23 | pause/end | −0.167 s (4 fr) | 0.373 | of shooting and killing. | This war is where |
| 28 | 3:26:08 (206.333) | 3:25:12 | pause/end | −0.167 s (4 fr) | 0.383 | the desert in Sonora. | Somewhere between 20 to |
| 29 | 3:35:02 (215.083) | 3:34:02 | fricative | −0.208 s (5 fr) |  | year old Isidro gets | a reputation of being |
| 30 | 3:50:15 (230.625) | 3:49:10 | repeat | −2.083 s (50 fr) |  | the north of Sinaloa | and he controls the |
| 31 | 3:58:04 (238.167) | 3:54:21 | pause/end | −0.208 s (5 fr) | 0.382 | along the main highway. | This is basically a |
| 32 | 4:01:21 (241.875) | 3:58:09 | pause/end | −0.250 s (6 fr) | 0.37 | straight shot towards Ariz. | Cocaine, meth, heroin, and |
| 33 | 4:17:19 (257.792) | 4:14:01 | pause/none | −0.125 s (3 fr) | 0.255 | was treating his group | as its own cartel. |
| 34 | 4:20:01 (260.042) | 4:16:04 | pause/none | −0.208 s (5 fr) | 0.252 | its own cartel. Meaning | in the US eyes, |
| 35 | 4:28:05 (268.208) | 4:24:03 | pause/end | −0.167 s (4 fr) | 0.383 | where he gets it. | Now the obvious answer |
| 36 | 4:32:14 (272.583) | 4:28:08 | pause/end | −0.250 s (6 fr) | 0.36 | it from El Chapo. | And in Mexico, he's |
| 37 | 4:39:19 (279.792) | 4:35:07 | pause/end | −0.250 s (6 fr) | 0.38 | how he got it. | You see, his name |
| 38 | 4:44:19 (284.792) | 4:40:01 | pause/none | −0.417 s (10 fr) | 0.243 | clearing bushes with machete | and if you think |
| 39 | 4:46:00 (286.000) | 4:40:20 | pause/none | −0.292 s (7 fr) | 0.248 | bushes with machete and | if you think about |
| 40 | 4:48:13 (288.542) | 4:43:02 | pause/comma | −0.292 s (7 fr) | 0.288 | his line of work, | which means clearing out |
| 41 | 4:51:01 (291.042) | 4:45:07 | pause/comma | −0.375 s (9 fr) | 0.305 | clearing out his rivals, | kinda explains how he |
| 42 | 5:12:07 (312.292) | 5:06:04 | pause/comma | −0.125 s (3 fr) | 0.305 | And all four times, | he walked out. Every |
| 43 | 5:14:12 (314.500) | 5:08:06 | pause/none | −0.125 s (3 fr) | 0.225 | walked out. Every single | time. This was despite |
| 44 | 5:14:23 (314.958) | 5:08:14 | pause/end | −0.208 s (5 fr) | 0.362 | out. Every single time. | This was despite the |
| 45 | 5:23:06 (323.250) | 5:16:16 | pause/end | −0.125 s (3 fr) | 0.375 | by the US government. | But in Mexico, apparently, |
| 46 | 5:29:07 (329.292) | 5:22:14 | pause/end | −0.125 s (3 fr) | 0.395 | and kept walking out. | You guys can figure |
| 47 | 5:37:14 (337.583) | 5:30:18 | pause/none | −0.250 s (6 fr) | 0.23 | December 2024, Mexican authorities | found a massive fentanyl |
| 48 | 5:43:06 (343.250) | 5:36:04 | pause/none | −0.250 s (6 fr) | 0.25 | We're talking huge. Like | huge. They found more |
| 49 | 5:44:08 (344.333) | 5:37:00 | pause/end | −0.125 s (3 fr) | 0.395 | talking huge. Like huge. | They found more than |
| 50 | 5:50:11 (350.458) | 5:43:00 | pause/end | −0.167 s (4 fr) | 0.393 | measuring unit. One ton. | Because of this, just |
| 51 | 6:07:02 (367.083) | 5:59:11 | pause/comma | −0.208 s (5 fr) | 0.282 | his very first day, | where he basically said |
| 52 | 6:12:02 (372.083) | 6:04:06 | pause/end | −0.125 s (3 fr) | 0.375 | are now terrorist organizations. | Because of this order, |
| 53 | 6:19:07 (379.292) | 6:11:08 | pause/comma | −0.208 s (5 fr) | 0.302 | ran by El Mencho, | all became a terrorist |
| 54 | 6:20:14 (380.583) | 6:12:10 | pause/none | −0.292 s (7 fr) | 0.228 | El Mencho, all became | a terrorist organization. Now, |
| 55 | 6:26:05 (386.208) | 6:17:18 | pause/none | −0.250 s (6 fr) | 0.26 | just a label, because | if the government thinks |
| 56 | 6:32:02 (392.083) | 6:23:09 | pause/comma | −0.125 s (3 fr) | 0.305 | cartels before this order, | then the government's job |
| 57 | 6:36:08 (396.333) | 6:27:12 | pause/end | −0.125 s (3 fr) | 0.365 | take you to court. | But if it says |
| 58 | 6:40:22 (400.917) | 6:31:23 | pause/none | −0.250 s (6 fr) | 0.22 | it becomes a crime | for anyone to help |
| 59 | 6:52:15 (412.625) | 6:43:10 | pause/none | −0.125 s (3 fr) | 0.255 | now go to prison | for helping a terrorist |
| 60 | 6:55:02 (415.083) | 6:45:18 | pause/end | −0.167 s (4 fr) | 0.393 | helping a terrorist group. | This was a major |
| 61 | 7:03:13 (423.542) | 6:54:01 | pause/none | −0.208 s (5 fr) | 0.252 | in an armed conflict | with these terrorist cartels. |
| 62 | 7:11:08 (431.333) | 7:01:15 | pause/end | −0.208 s (5 fr) | 0.382 | it treated Al Qaeda. | They are targets now. |
| 63 | 7:13:08 (433.333) | 7:03:10 | pause/end | −0.125 s (3 fr) | 0.385 | They are targets now. | Now, all the while |
| 64 | 7:30:16 (450.667) | 7:20:15 | pause/end | −0.250 s (6 fr) | 0.38 | to do with drugs. | You see, unlike China |
| 65 | 7:40:08 (460.333) | 7:30:01 | pause/none | −0.125 s (3 fr) | 0.235 | that was pretty clear | in the statements that |
| 66 | 7:49:16 (469.667) | 7:39:06 | pause/end | −0.125 s (3 fr) | 0.385 | country on this planet. | So any type of |
| 67 | 7:57:16 (477.667) | 7:47:03 | pause/comma | −0.208 s (5 fr) | 0.282 | and by the end, | There was a promise |
| 68 | 8:02:08 (482.333) | 7:51:14 | pause/end | −0.167 s (4 fr) | 0.363 | stop this drug flow. | But the deal did |
| 69 | 8:07:10 (487.417) | 7:56:12 | pause/end | −0.167 s (4 fr) | 0.363 | pay much attention to. | At the same time, |
| 70 | 8:11:02 (491.083) | 8:00:00 | pause/comma | −0.125 s (3 fr) | 0.305 | troops to the border, | they also round up |
| 71 | 8:18:23 (498.958) | 8:07:18 | pause/end | −0.167 s (4 fr) | 0.373 | to the United States. | One of the guys |
| 72 | 8:24:13 (504.542) | 8:13:04 | pause/end | −0.125 s (3 fr) | 0.395 | an American DEA agent. | This was a guy |
| 73 | 8:30:09 (510.375) | 8:18:21 | pause/end | −0.208 s (5 fr) | 0.362 | it because of tariffs. | And then Mexico does |
| 74 | 8:36:05 (516.208) | 8:24:12 | pause/none | −0.167 s (4 fr) | 0.243 | January of this year | with 37 more prisoners. |
| 75 | 8:38:10 (518.417) | 8:26:13 | pause/end | −0.167 s (4 fr) | 0.363 | with 37 more prisoners. | I'm pretty sure this |
| 76 | 8:40:21 (520.875) | 8:28:20 | pause/end | −0.125 s (3 fr) | 0.375 | this will just continue. | Now, one reason US |
| 77 | 9:00:06 (540.250) | 8:48:02 | pause/end | −0.125 s (3 fr) | 0.385 | in an American prison. | Now, out of all |
| 78 | 9:06:21 (546.875) | 8:54:14 | pause/end | −0.250 s (6 fr) | 0.37 | United States and Mexico. | The deal is basically |
| 79 | 9:11:00 (551.000) | 8:58:11 | pause/none | −0.125 s (3 fr) | 0.235 | will not come into | Mexico, at least officially. |
| 80 | 9:21:09 (561.375) | 9:08:17 | pause/end | −0.125 s (3 fr) | 0.385 | or take them out. | The US gets to |
| 81 | 9:49:18 (589.750) | 9:36:23 | pause/end | −0.167 s (4 fr) | 0.363 | rules than the military. | The military has strict |
| 82 | 9:54:06 (594.250) | 9:41:07 | pause/end | −0.208 s (5 fr) | 0.382 | and can't work with. | The CIA can pretty |
| 83 | 9:58:00 (598.000) | 9:44:20 | noise | −0.292 s (7 fr) |  | much work with anybody. | As long as that |
| 84 | 10:20:01 (620.042) | 10:06:14 | pause/none | −0.125 s (3 fr) | 0.245 | let's just call it | Narco Hunters. This is |
| 85 | 10:36:05 (636.208) | 10:22:15 | pause/none | −0.125 s (3 fr) | 0.235 | know about a cartel | and turn it into |
| 86 | 11:05:21 (665.875) | 10:52:04 | pause/end | −0.125 s (3 fr) | 0.365 | boats were carrying drugs. | Now these strikes are |
| 87 | 11:13:18 (673.750) | 10:59:22 | pause/end | −0.250 s (6 fr) | 0.36 | who have been killed. | And then in January |
| 88 | 11:31:01 (691.042) | 11:16:23 | pause/end | −0.292 s (7 fr) | 0.388 | in Brooklyn right now. | That's a very big |
| 89 | 11:35:08 (695.333) | 11:20:23 | pause/end | −0.208 s (5 fr) | 0.382 | every single cartel boss. | Venezuela had a lot |
| 90 | 11:54:11 (714.458) | 11:39:21 | pause/none | −0.167 s (4 fr) | 0.253 | are a lot of | Videos on YouTube that |
| 91 | 11:59:17 (719.708) | 11:44:23 | pause/end | −0.167 s (4 fr) | 0.363 | was a major success. | Officially, the Mexican government |
| 92 | 12:09:13 (729.542) | 11:54:15 | pause/end | −0.292 s (7 fr) | 0.398 | gave some extra information. | But the American side |
| 93 | 12:16:09 (736.375) | 12:01:04 | pause/none | −0.167 s (4 fr) | 0.233 | reporters behind the scenes | have said that the |
| 94 | 12:40:02 (760.083) | 12:24:17 | pause/end | −0.167 s (4 fr) | 0.373 | part in this operation. | Now this is where |
| 95 | 12:48:01 (768.042) | 12:32:12 | pause/end | −0.167 s (4 fr) | 0.383 | just hand off information? | Well, that was already |
| 96 | 13:05:17 (785.708) | 12:50:00 | pause/comma | −0.125 s (3 fr) | 0.305 | a few weeks ago, | this is where the |
| 97 | 13:26:23 (806.958) | 13:11:03 | pause/none | −0.125 s (3 fr) | 0.235 | with state police units | and take them along |
| 98 | 13:44:21 (824.875) | 13:28:22 | pause/end | −0.250 s (6 fr) | 0.36 | wanted to go after. | And on top of |
| 99 | 13:49:18 (829.750) | 13:33:13 | pause/end | −0.208 s (5 fr) | 0.362 | that was not pretty. | Four witnesses accused him |
| 100 | 14:17:02 (857.083) | 14:00:16 | pause/end | −0.125 s (3 fr) | 0.385 | anyone, unlike the military. | The problem in Mexico |
| 101 | 14:21:23 (861.958) | 14:05:10 | pause/comma | −0.167 s (4 fr) | 0.293 | off pretty much everyone, | cops and officials. So |
| 102 | 14:46:19 (886.792) | 14:30:02 | pause/comma | −0.208 s (5 fr) | 0.312 | the New York Times, | once he started helping, |
| 103 | 14:51:08 (891.333) | 14:34:10 | pause/end | −0.167 s (4 fr) | 0.373 | just came back automatically. | Zuany starts helping the |
| 104 | 15:11:22 (911.917) | 14:54:20 | pause/end | −0.125 s (3 fr) | 0.365 | with the Mexican unit. | They are basically blending |
| 105 | 15:21:17 (921.708) | 15:04:12 | pause/end | −0.250 s (6 fr) | 0.36 | can blend in easily. | More importantly, though, they |
| 106 | 15:26:03 (926.125) | 15:08:16 | pause/end | −0.208 s (5 fr) | 0.372 | them on these raids. | This is apparently to |
| 107 | 15:30:00 (930.000) | 15:12:08 | pause/end | −0.167 s (4 fr) | 0.373 | live in real time. | Mostly they're using this |
| 108 | 15:36:22 (936.917) | 15:19:02 | pause/comma | −0.167 s (4 fr) | 0.293 | a cartel safe house, | one of the Americans |
| 109 | 15:46:18 (946.750) | 15:28:18 | pause/end | −0.167 s (4 fr) | 0.383 | questionings of a prisoner. | Now the situation wasn't |
| 110 | 15:51:07 (951.292) | 15:33:03 | pause/end | −0.208 s (5 fr) | 0.382 | rosy as it sounded. | A lot of these |
| 111 | 16:01:19 (961.792) | 15:43:10 | pause/comma | −0.125 s (3 fr) | 0.315 | boss had already left, | which visibly annoyed the |
| 112 | 16:10:04 (970.167) | 15:51:16 | pause/comma | −0.250 s (6 fr) | 0.29 | tipping off the targets, | which was definitely interesting |
| 113 | 16:15:23 (975.958) | 15:57:05 | pause/end | −0.125 s (3 fr) | 0.365 | who's helping the Americans. | But anyways, let's continue. |
| 114 | 16:23:12 (983.500) | 16:04:15 | pause/end | −0.125 s (3 fr) | 0.385 | the state of Chihuahua. | The job is to |
| 115 | 16:32:17 (992.708) | 16:13:17 | pause/none | −0.125 s (3 fr) | 0.235 | officers wearing ski masks | to hide their faces. |
| 116 | 16:34:05 (994.208) | 16:15:02 | pause/end | −0.208 s (5 fr) | 0.382 | to hide their faces. | They find the lab |
| 117 | 16:46:00 (1006.000) | 16:26:16 | pause/end | −0.125 s (3 fr) | 0.375 | middle of the night. | This is when one |
| 118 | 16:51:18 (1011.750) | 16:32:07 | pause/end | −0.208 s (5 fr) | 0.362 | falls about 300 feet. | Killing everyone inside, including |
| 119 | 17:02:07 (1022.292) | 16:42:15 | pause/comma | −0.167 s (4 fr) | 0.303 | people who were there, | his instructions were to |
| 120 | 17:31:12 (1051.500) | 17:11:16 | pause/end | −0.167 s (4 fr) | 0.363 | operating inside of Mexico. | This also became a |
| 121 | 17:39:10 (1059.417) | 17:19:10 | pause/comma | −0.125 s (3 fr) | 0.295 | from the opposition party, | so it was basically |
| 122 | 17:44:00 (1064.000) | 17:23:21 | pause/comma | −0.125 s (3 fr) | 0.285 | on top of that, | Zuany and his boss, |
| 123 | 17:47:22 (1067.917) | 17:27:16 | pause/comma | −0.167 s (4 fr) | 0.313 | the state's attorney general, | both had to resign, |
| 124 | 17:58:06 (1078.250) | 17:37:20 | pause/end | −0.167 s (4 fr) | 0.363 | in the United States. | Now, if you look |
| 125 | 18:04:15 (1084.625) | 17:44:01 | pause/end | −0.167 s (4 fr) | 0.393 | around El Chapo Isidro. | Last November, Mexico's Navy |
| 126 | 18:19:20 (1099.833) | 17:59:02 | pause/end | −0.167 s (4 fr) | 0.393 | to the United States. | Through this year, they |
| 127 | 18:23:07 (1103.292) | 18:02:09 | pause/end | −0.125 s (3 fr) | 0.385 | one at a time. | And then just last |
| 128 | 18:33:05 (1113.208) | 18:12:04 | pause/end | −0.208 s (5 fr) | 0.372 | firefight with the Navy. | So piece by piece, |
| 129 | 18:43:18 (1123.750) | 18:22:12 | pause/end | −0.167 s (4 fr) | 0.393 | a summit in China. | Now, of course, officially |
| 130 | 18:47:22 (1127.917) | 18:26:12 | pause/end | −0.125 s (3 fr) | 0.385 | main topic of conversation. | But Trump also publicly |
| 131 | 18:52:00 (1132.000) | 18:30:11 | pause/end | −0.167 s (4 fr) | 0.393 | cartels are running Mexico. | I'm guessing it came |
| 132 | 18:54:16 (1134.667) | 18:32:23 | pause/end | −0.125 s (3 fr) | 0.395 | during the conversation, too. | And then on Friday, |
| 133 | 18:56:08 (1136.333) | 18:34:12 | pause/comma | −0.167 s (4 fr) | 0.303 | And then on Friday, | The mission was on. |
| 134 | 19:06:19 (1146.792) | 18:44:19 | pause/end | −0.167 s (4 fr) | 0.373 | forces started moving it. | The units that were |
| 135 | 19:14:21 (1154.875) | 18:52:17 | pause/comma | −0.125 s (3 fr) | 0.315 | who go by wolves, | and the other is |
| 136 | 19:17:16 (1157.667) | 18:55:09 | pause/comma | −0.125 s (3 fr) | 0.295 | Army Special Forces unit, | and they go by |
| 137 | 19:19:15 (1159.625) | 18:57:05 | pause/end | −0.125 s (3 fr) | 0.375 | go by the bats. | According to the Mexican |
| 138 | 19:31:17 (1171.708) | 19:09:04 | pause/none | −0.125 s (3 fr) | 0.225 | directions without being noticed | and set up a |
| 139 | 19:35:12 (1175.500) | 19:12:20 | pause/end | −0.250 s (6 fr) | 0.38 | could not run anywhere. | They got hit with |
| 140 | 19:43:02 (1183.083) | 19:20:04 | pause/none | −0.125 s (3 fr) | 0.235 | new number two guy | and the guy who |
| 141 | 19:52:08 (1192.333) | 19:29:07 | pause/end | −0.125 s (3 fr) | 0.375 | where he grew up. | Now, this just happened |
| 142 | 19:59:03 (1199.125) | 19:35:23 | pause/end | −0.125 s (3 fr) | 0.395 | whole thing went down. | But right after the |
| 143 | 20:03:06 (1203.250) | 19:39:23 | pause/end | −0.125 s (3 fr) | 0.385 | the region went crazy. | His people started burning |
| 144 | 20:20:06 (1220.250) | 19:56:20 | pause/end | −0.208 s (5 fr) | 0.382 | the shooting to stop. | There are also reports |
| 145 | 20:28:00 (1228.000) | 20:04:09 | pause/comma | −0.292 s (7 fr) | 0.298 | that was going on, | El Chapo Isidro was |
| 146 | 20:41:08 (1241.333) | 20:17:10 | pause/comma | −0.125 s (3 fr) | 0.305 | cuffed behind his back, | and he keeps his |
| 147 | 20:57:16 (1257.667) | 20:33:15 | pause/end | −0.125 s (3 fr) | 0.375 | constant cooperation and trust. | And then he says |
| 148 | 21:01:23 (1261.958) | 20:37:19 | pause/end | −0.375 s (9 fr) | 0.365 | on hunting these bosses. | Now, if you're wondering |
| 149 | 21:13:15 (1273.625) | 20:49:02 | pause/end | −0.125 s (3 fr) | 0.395 | Washington, DC since 2012. | And the US has |
| 150 | 21:22:02 (1282.083) | 20:57:10 | pause/end | −0.292 s (7 fr) | 0.368 | sent 90 some guys. | So I don't think |
| 151 | 21:25:23 (1285.958) | 21:01:00 | pause/end | −0.292 s (7 fr) | 0.388 | given any special treatments. | So now we get |
| 152 | 21:38:09 (1298.375) | 21:13:03 | pause/comma | −0.333 s (8 fr) | 0.287 | this actually working? Well, | for the first time |
| 153 | 21:43:00 (1303.000) | 21:17:10 | pause/comma | −0.125 s (3 fr) | 0.315 | answer is mostly yes, | at least on things |
| 154 | 21:56:00 (1316.000) | 21:30:07 | pause/none | −0.167 s (4 fr) | 0.233 | getting caught or killed | faster than we have |
| 155 | 22:03:13 (1323.542) | 21:37:16 | pause/end | −0.125 s (3 fr) | 0.375 | catching or the killing. | Now of course all |
| 156 | 22:07:06 (1327.250) | 21:41:06 | pause/end | −0.125 s (3 fr) | 0.385 | cartels are going away. | They're in a business |
| 157 | 22:13:23 (1333.958) | 21:47:20 | pause/end | −0.292 s (7 fr) | 0.398 | want the top job. | I'm sure the drug |
| 158 | 22:15:05 (1335.208) | 21:48:19 | pause/none | −0.250 s (6 fr) | 0.23 | top job. I'm sure | the drug smuggling will |
| 159 | 22:17:13 (1337.542) | 21:50:21 | pause/comma | −0.125 s (3 fr) | 0.305 | drug smuggling will continue, | but at least for |
