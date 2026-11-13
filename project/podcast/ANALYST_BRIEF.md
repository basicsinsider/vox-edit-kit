# Transcript analyst brief — podcast "TSMC vs UMC" (Searching Lessons), raw take 98:20

You analyse ONE time range of the raw transcript of a two-person video podcast. Host **Sam** tells the story (Robert Tsao / UMC vs
Morris Chang / TSMC, how Silicon Valley was made, how Taiwan copied it); co-host **Sunkit** asks questions and banters. There is no
script: the transcript is the story. Do not fact-check; do not rewrite. You only READ text (no audio/video work, no heavy jobs).

Inputs (repo root `/home/user/vox-edit-kit`):
- `project/podcast/raw_transcript.json` — words `{id,text,start,end}` in raw seconds (Parakeet ASR; names are often misheard:
  "Sao/Cao/Chao/Xiao" = Robert **Tsao**, "Shang" = Morris **Chang**, "Sin Shu/Shin Shu Park" = **Hsinchu** Science Park,
  "Turner/Termin/Kerman" = Frederick **Terman**, "Vanaver Busch" = Vannevar **Bush**, "Burdeen/Braden" = Bardeen/Brattain).
- `python3 project/podcast/gen_dump.py <t0> <t1>` — your range as timed lines `[first_word_id start_s] text`.
- `python3 project/podcast/gen_words.py <id0> <id1>` — every word with its id and start time (`|gapX` = pause after it).

## Deliverable 1 — `project/podcast/analysis/partK_cuts.json` (K = your part number)
A JSON list of word-id ranges to REMOVE from the take: `{"a": first_id, "b": last_id, "kind": "...", "why": "...", "text": "the removed words"}`.
The owner's rule: "Remove ums, ahs, errors, false starts, retakes and long dead pauses. The rest stays." So:
- CUT: filler tokens (um, uh, er, "you know" only when it is pure filler between a false start and its restart); stammers and doubled
  words ("he he he does" → keep one "he"); false starts that are restarted ("So at this time well / this is the nineteen hundreds." →
  cut the abandoned start); a sentence said twice (keep the better/complete take, normally the last); abandoned half-sentences that
  lead nowhere; garbled crosstalk fragments where the ASR text is nonsense AND removing them loses nothing; talk about the recording
  itself ("let me say that again", "can we cut that").
- KEEP: all story content, all of Sunkit's real questions and reactions, jokes, tangents and banter (it is a podcast, not a
  narration — do NOT tighten it into a script), natural short acknowledgements ("Yeah.", "Oh okay.") when they answer something.
- Each cut must leave a sentence that still reads naturally when the words before `a` and after `b` are joined. Prefer cutting whole
  abandoned clauses over single words inside a fluent sentence. When unsure, do not cut. Never cut across a speaker's punchline.
- Pauses are handled by a separate automatic pass — do not list silences.
- ASR text can be wrong: if a passage reads as nonsense but is probably fine speech misheard, leave it (note it in the notes file
  under "ASR doubtful" with ids so the lead can re-listen).
Expect roughly 40–120 cuts for ~19 minutes. Verify every range with gen_words.py (ids exact, inclusive, non-overlapping, inside your range).

## Deliverable 2 — `project/podcast/analysis/partK_notes.md`
1. **Outline**: the sections of your range in order — raw start–end (s), first/last word id, a 1–2 line summary, who is mainly speaking.
2. **Edited-section candidates.** After the first 5 minutes the video stays on the speakers EXCEPT where a visual is truly needed to
   explain the story or clearly improves the viewing experience (maps, charts, key names/numbers, documents, events, timelines,
   photos of the people/places/objects being introduced). List every candidate: raw start–end + word ids of the exact words it would
   cover (typically 6–40 s; longer only if the explanation really runs that long), the exact quote, what the viewer needs to SEE
   and why (e.g. "geography he describes can't be followed without a map", "three numbers compared → chart", "new person introduced
   → name + portrait"), the facts/names/numbers spoken (verbatim), and a rating: **A** = the story is hard to follow without it,
   **B** = clearly improves it, **C** = nice to have. Be selective: banter, opinions and simple narration need no visual.
3. **Names & spellings**: every person, company, place, product, date and number in your range: ASR form → correct spelling, with word ids.
4. **ASR doubtful** passages (ids) and anything the lead should re-listen to; places where both talk at once.

Finish by printing a 10-line summary (number of cuts, seconds removed estimate, number of A/B/C candidates, the outline headings).
Write only those two files. Do not commit, do not touch other files.
