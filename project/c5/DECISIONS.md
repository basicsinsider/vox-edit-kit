# Decisions — chunk c5 (planner defaults; Krish / lead may override)

1. **Colour code (lead's cross-chunk decision, LONGFORM.md end)** — c5 is a political chunk: **red** = PRC / CCP / the Communist bloc
   (China solid red, the Soviet Union red hatch, Mao paintings and Cultural Revolution posters keep their red, lightly muted);
   **celadon** = Taiwan / ROC / the Taiwanese government; **navy** = the United States and its allies, only where a contrast with red is needed
   (flags, the Cold-War triangle, wavering US allies); everyone else neutral (India, Pakistan, GI/TI/RCA, Terman, the UN, Kissinger's influence
   flows); **yellow** = highlighter + one key number per scene (`9 to 10%`, `2 days`, `an hour`, `2`) and the D14 marker route. Max two accents per
   frame. TSMC/UMC don't appear in c5 (no red/blue clash). Flags = single-colour halftone prints (US navy, PRC red, ROC ink).
2. **"RAC" @32.03 = RCA** on screen (the company that matters later); lead listens once to confirm.
3. **Unnamed people stay unnamed in text**: "Taiwanese leader" = Chiang Kai-shek photos, "the secretary of the state at the time" = William P.
   Rogers chip, "the Chinese leadership" = Zhou Enlai card — pictures identify them, on-screen words stay the narrator's. (If Krish wants ID
   labels, add a 22 px t-label under each — cheap change.)
4. **Map place labels** Kinmen / Matsu (C5S090) as small geographic labels, like other map labels; the narration says only "the islands".
5. **No fact-checking**: C5B063 says *Kissinger* will go to China to meet Mao — the picture is the real 15 July 1971 televised announcement
   (N61), the text is only his words ("later in the year", "China", "Mao Zedong"). Real newspaper headlines that would contradict the
   narration are not used as overlays; real documents keep their own printed words.
6. **Jeff Bezos quote** (C5S106) — shown as he presents it: pull-quote "compromise is never a good solution", caption JEFF BEZOS, painting-to-
   print reveal. (It is a paraphrase; Krish's rule = no fact-check.)
7. **§10.7 painting-to-print reveals**: Bezos (C5S106) and Bush's "US policy is not abandoning Taiwan at all" (C5S117, mirrored); the
   callback C5S122 reuses the Bush column. Typeset columns, never a real masthead/date.
8. **2.5D (3 moments)**: Mao on Tiananmen (C5S037), the PIA 707 on a night tarmac — "behind the scenes" (C5S058), the UN General Assembly
   hall as the vote approaches (C5S109).
9. **Curve cut**: carrier → satellite Strait (C5S092), the only `expo.inOut`.
10. **TVs**: Tatung (C5S014, Taiwanese assembly), RCA 1970–71 colour set (C5S067 — RCA is in this story), Sony Trinitron rewind (C5S087).
11. **Charts without narrated values** (growth bars, smile curve, ladder, influence flows, UN dots, Bush/Kissinger columns) are shapes only —
    no axis values, years or counts. The growth bars' 9–10 % band is the only number, as narrated.
12. **The conference** (C5B018–C5B029) is never named on screen (the narrator doesn't name it); programme = typeset with his topic words.
13. **Fred Terman** reuses c1's Terman assets (callback "the guy we have talked about"), spelled TERMAN (ASR "Turman").
14. **Typeset recreations** (cable, schedule, patient chart, agenda, columns, org chart, calendar) carry only narrated words or neutral
    filler blurred out; no seals, letterheads, signatures or real mastheads. Real dates appear only inside real documents/props (memo, treaty,
    October 1971 calendar).
15. **Profanity / slips**: no text on "pissed off" (scribbles say it), on "abandoning abandoning um", "Bush one", "the strip", "UN set" etc.
16. **First-word cues**: when a scene's first cue is its first spoken word, the cut moves to `S(word) − 0.06` (picture and word arrive together).
17. **Key-animation hold**: every scene's key animation finishes ≥ 0.5 s before its out (whips centred on the boundary → ≥ 0.66 s before);
    the "Key anim done" time in EDIT_NOTES is the deadline. Words in the last 0.6 s of a scene use a 0.35 s entrance.
18. **UN vote motif** (D06 dots, seat/nameplate) must match c3/c4 — lead passes c4's spec to the c5s03 editor before it builds C5S097.
19. **Map kit**: all maps from `assets/maps/kit/` (M01–M07). Until it lands, editors block layout with the intro maps but must swap before render.
20. **Fuseli's The Nightmare** for "their worst dreams are coming true" (painting as B-roll, the words made literal).
21. **Chunk joins**: c4→c5 continues the EPZ push (C5S001); c5→c6 ends on the UN voting board still moving (cut on action into c6).

## Lead overrides (2026-10-31)
- Kissinger vs Nixon: the narrator says Kissinger is going to China — show KISSINGER (photos/footage of Kissinger, 1971 secret
  trip, Pakistan/PIA), not Nixon's 15 July address, so the picture matches the words. Nixon's address only where the narrator
  talks about Nixon/the announcement.
- Unnamed people (Chiang Kai-shek, Rogers, Zhou Enlai): small t-label ID labels are OK (visual labels of an object on screen),
  kept minimal.
- UN vote graphic: reuse c4's spec (project/c4/EDIT_NOTES.md, its D06 GA hemicycle scene) so the look matches.
- Periscope Film clips (assets/c5/footage/*, burned-in "periscopefilm.com" caption): do NOT use them and do not crop/mask the
  watermark (MANUAL: never strip watermarks). Use stills (Ken-Burns/2.5D), the c3/c4/c6 PD newsreel clips and intro fab
  footage instead; note any gap. (lead, 2026-10-31)
