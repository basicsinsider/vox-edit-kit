# US vs Cartels — FIX ROUND 1 (Frame.io review, Sam Shukla = narrator, Sanket), 2026-11-22
Review: https://f.io/2aztAOX5 (public; comments load only in a browser — headless Chromium/Playwright). Timecodes are on the delivered
720p (22:22, 24 fps, HH:MM:SS:FF) = the current master timeline "v1" (= transcript_ct.json times). CHECK every note against the actual
frame and words there first (some say "a few secs ago" / "a little earlier").

## The comments
| # | TC (v1) | who | note | owner |
|---|---|---|---|---|
| 1 | 00:00:00:00 | Sam | start with the clip AND its sound (crowd noise, panic) — like the protests (Paraguay X clip) | Agent A (cts00) + V (pre-roll) + sound |
| 6 | 00:01:09:04 | Sanket | dead space in VO, sentence said super slow | V |
| 7 | 00:01:58:03 | Sanket | intro packaging, music not good, intro slow → tighten intro: pacing, cut density, better music + build | A + sound |
| 2 | 00:02:04:09 | Sam | equalize the audio: raise low, lower high — "biggest issue"; reply: within a range, not one flat level | V (levelling) |
| 11 | 00:03:19:13 | Sanket | circle pics zoomed in — show the whole face/photo in each circle | B (cts03) |
| 12 | 00:03:35:18 | Sanket | "gets" said weirdly — AI edit? → check/fix the cut at that word | V |
| 4 | 00:03:56:06 | Sam | cut out the repeat sentence a little earlier ("he controls the routes, and he controls the routes") | V |
| 14 | 00:04:45:06 | Sanket | "machete" said wrong (t silent) → swap another take if one exists, else tell Krish | V |
| 15 | 00:04:50:06 | Sanket | VO pace super slow, edit | V |
| 8 | 00:05:02:09 | Sam | no foreign-language articles, or translate to English; happened a few secs earlier too | B (cts04) + sweep |
| 16 | 00:05:02:21 | Sanket | screenshots of Spanish text → English | B |
| 9 | 00:06:58:16 | Sam | audio editing is the weakest part | V |
| 10 | 00:08:00:13 | Sam | "10,000 troops*" on screen — I misspoke (audio stays) | B (cts06) |
| 18 | 00:09:59:01 | Sanket | audio needs cleaning here too | V |
| 19 | 00:13:43:00 | Sanket | text needs to be English again | C (cts09) |
| 20 | 00:15:08:21 | Sanket | "he ends up other CIA officers" — edit cut off part of the sentence? → restore words | V |
| 13 | 00:16:33:15 | Sanket | the AMERICANS wore ski masks, not the Mexicans | C (cts11) |
| 17 | 00:18:57:09 | Sanket | make this English | C (cts12) |
| 21 | 00:19:00:18 | Sanket | calendar in Spanish | C (cts12) |

## Rules for this round
1. **English on screen (new binding rule, Krish)**: no untranslated foreign-language article, screenshot, calendar, document or UI anywhere.
   Prefer an English-language source of the same fact. If a Spanish original must stay (an official post, a front page), overlay a clean
   English translation in house style (paper/ink card or scrim, Crimson Pro / Haskoy, the original visible small underneath, credit
   "translated"). Proper names (LOBOS / MURCIÉLAGOS, place names, the word CHAPEAR) stay, with an English gloss. Sweep EVERY segment.
2. **Timeline**: compositions stay on the v1 master timeline (do NOT retime cues). All VO timing changes are expressed in ONE file,
   `project/cartels/fix1_ops.json` (owner: Agent V), applied to picture AND audio at assembly:
   `{"preroll": P, "ops": [{"t": <v1 s>, "del": <s>}, {"t": <v1 s>, "ins": <s>, "src": "<raw in>-<raw out>"} …]}` — every `del`/`ins`
   length a whole number of frames (k/24 s); deletions only where the VO is silent (between or inside sentences); picture: frames removed
   at the same place (a 0.2–0.8 s jump inside a scene is acceptable, NVIDIA precedent), insertions = the picture frame held (freeze) while
   the restored words play. `preroll` P = the cold-open clip length (new composition `cts00`, its own audio), so v2 time = P + map(v1).
3. **Levelling (owner-approved exception for this video, Sam/Sanket's "biggest issue")**: NVIDIA's approved method (`tools/nv_fix_mix.py`):
   one slow gain ride on the WHOLE mix (VO speech-gated 3 s loudness, ±6 s median, ±2 s smoothing, clamped), then −14 LUFS-I and a peak
   limiter at −2 dBFS; no EQ, no compressor. Report VO LRA / short-term spread before → after; music limits stay relative to the VO.
4. Re-render only affected segments (Sonnet helpers, 720p `SCALE=720`), reassemble with the ops, deliver a new 720p (md5 check), then
   re-export the Premiere package (4K) to match.
