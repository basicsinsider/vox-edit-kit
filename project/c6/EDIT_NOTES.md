# EDIT NOTES — CHUNK c6 "Taiwan: the chip rivalry" (Searching Lessons), VO local 0.00–598.01 (full audio 3277.14–3875.12)

Shot-by-shot plan for chunk c6. Read with `project/LONGFORM.md`, `MANUAL.md` (**§10.1–10.9 override older sections**; §5
effects; §6/§6.1 reference layouts), `project/c6/analysis/BEATS.md` (beats, ASR fixes, cues), `ASSETS_NEEDED.md` (asset IDs
`E..` = exists, `N..`/`M..` = needed), `SEGMENTS.md` (who builds what) and `DECISIONS.md`. Prepared 2026-10-31 by the
director / edit planner. The approved intro (`review/intro_720p.mp4`, `project/intro/EDIT_NOTES.md`) is the look and the
quality bar — this chunk reuses its grammar (paper/grid charts ↔ night archival plates, label-boxes, serif-italic captions,
celadon Taiwan, lamp-lit desks, Vox layered panels) with new variations.

## 0. How to read this file

- **Times** = LOCAL VO seconds (`vo_c6.mp3`; absolute = local + 3277.14), scene boundaries on word starts from
  `transcript_c6.json`. **107 scenes, C6S001–C6S107**, contiguous, 0.00 → 598.01, no gaps (checked by script).
  Median scene 5.3 s (range 2.2–9.5 s) — a touch longer than the intro (4.2 s) because this chunk is narrative history.
- **Text cue `@t`** = start of the spoken word; the text's first frame sits at `T(t) − 0.06` (0–120 ms before the word).
  Lines longer than one word are revealed **word by word** (each word its own literal `T()`), MANUAL §4.4.
- **Words** = the exact narration under the shot (ASR names corrected). **Why** = why the picture matches those words
  (Krish's rule, MANUAL §10.1.3).
- **Ground**: `NIGHT` (dark/cinematic/archival plate, lamp-lit desk, dark map), `PAPER` (paper_cream / stained / fiber /
  blueprint `_hires` — two layers, top ~90 %), `GRID` (real graph / ruled papers: `paper_graph_01_hires`,
  `paper_lined_01_hires`; K+E scans only as cards at native size — §10.9). Rhythm rule: ≤ 3 in a row on the same ground;
  PAPER+GRID combined also ≤ 3 (checked in §15). **No FACE ground — no face cam after the intro (§10.9).**
- **FX** = MANUAL §5 numbers + §10 craft: `W` whip (`FX.whip`, direction given), `FW` light-flash whip, `CA` cut on action,
  `PT` push-through, `PS` paper slide, `CRT` picture collapses to a CRT line, `FH` focus hunt (`FX.focusHunt`, once per
  scene max), `CS` `FX.chokeSettle`. **No iris.** Easing `FX.choppy(FX.ease.out|inOut|in, dur, 12)`; camera `FX.ease.cam`.
- **Animations finish + hold ≥ 0.5 s (12 frames) before the Out** (§10.9): every key animation in a scene is timed to
  complete ≥ 0.5 s before the listed out-time; `CA` exits use the camera or a secondary motion only (see §15.6).
- **Glow**: `.halate` only on the scene's **hero** (marked "hero halate"); everything else `.clean`. Paper never glows.
- **Ref** = Krish's intro pack `D01–D15` (`references/style-images/intro/`), the older `R1–R12`, the approved stills in
  `expected/layouts/`, or a NEW variation idea **V1–V6** (described in §14) / a named "Pinterest idea".
- **Palette for c6** (`lib/palette.css`; meanings fixed for the whole video): **celadon** `#9fc7b2` = Taiwan / the ROC
  government and its people (fills, underlines, dots — never body text) · **PRC / CCP = ink** `#141b24` (neutral dark; the real
  red of PRC flags only lives inside desaturated archival photos) · US, UN, Japan, USSR, RCA = neutral (bone / grey photo
  tones) · **yellow** = highlighter + the one key number of a scene (`2/3`, `12 YEARS`, `0%`) and the D10/D14 marker route ·
  **red (TSMC / Morris Chang) and blue (UMC / Robert Tsao) are NOT used in c6** — no company of theirs is in this chunk; keeping
  them out preserves their meaning for c7+. Max two accents per frame.
- **Spellings on screen** (BEATS §2a): George H. W. Bush, Henry Kissinger, Tanzania, Chiang Kai-shek, Chiang Ching-kuo
  (narrator says "Chang Ching Kuo" — never print "Chang"), Deng Xiaoping, Mao Zedong, Sun Yun-suan, K. T. Li, Sarah Paine,
  Pan Wen-yuan, Fei Hua, RCA, "10 Major Projects". No text on slips/asides (BEATS §2b) — notably never "get Taiwan in",
  never "communism with Chinese characteristics", never "greatly".
- **The secretary general is a grey silhouette until "Fei" @590.06** (like the intro's Morris Chang reveal). The telecom
  official is **never named or captioned** (narrator doesn't name him).
- **Quotes** are the narrator's paraphrases — on screen attributed "(paraphrased)", never in quotation marks as a verbatim
  document; typeset recreations never carry a real masthead, seal or signature.
- **Assets**: true images first (§10.9: copyrighted press photos / footage / newspapers allowed as fair use, credited with a
  13 px micro-credit where customary). Reuse allowed when the story needs it; counts in ASSETS_NEEDED.
- **SFX** lines are object events (LOCAL VO s) → copy into `compositions/c6sNN.sfx.json` (vocabulary: intro SEGMENTS §3.4).
  The sound pass applies the §10.8 restraint (hero per scene + moves + ambience).


## 1. Act I — The Hail Mary: the 'important question' (0.00–45.45)
Music: low dark pulse under a drone; drop to near-silence on "kicked out" 42.49; one low hit on "China" 43.21.

### C6S001 · 0.00–2.48 · C6B001 · NIGHT
- **Words** "Taiwan doesn't know this, too. So"
- **Why** the line continues c5's uncertainty ("Taiwan doesn't know this" = doesn't know how the vote will go) → the ROC delegation in its seat under the CHINA nameplate, before the vote, in soft focus.
- **FX** #1 + #16 plate (fringe blur, CA 0.12) + `FH` reversed (sharp → soft = not knowing) · **Ref** —
- **Assets** N01 UN General Assembly hall 1971, ROC delegation seated (UN Photo / AP)
- **Text** none (aside; picture carries it)
- **Camera** slow push 1.00→1.05 (cam ease). **Out** W→ @2.42.
- **SFX** 0.00 air_swell (J-cut, continues c5 room tone `hum` dur 2.4) · 2.40 whoosh.

### C6S002 · 2.48–8.64 · C6B001–C6B002 · PAPER
- **Words** "George Bush tries another hail mary. Not a hail mary, he has done this before, but he tries to see if he can do this."
- **Why** "George Bush tries another Hail Mary… he has done this before" → Bush (the man) + a Hail Mary (a long desperate football pass) + 'before' (the same move stacked up from earlier years).
- **FX** #10 Vox layered backgrounds + #19 markup (pen arc) · `CS` on the name · **Ref** intro IS002 layout as VARIATION (portrait right → left, panels stacked vertically instead of fanned)
- **Assets** N02 George H. W. Bush at the UN, 1971 (cut-out); N03 vintage American-football long-pass photo/illustration (1930s–60s); N04 three earlier UN 'important question' resolution pages (UN ODS scans) as a stack
- **Text** `GEORGE H. W. BUSH` label-box (ink fill, bone text) @2.48 · `Hail Mary` t-serif-i 96 px @4.16 (`Mary` @4.56) — a pen arc (markup.arrow, ink) traces the long pass over the football panel @4.16 · `done this before` t-label @6.00 as the resolution stack fans out (3 pages, 12 fps)
- **Camera** drift left 40 px; last 6 frames slide down onto the top page of the stack. **Out** PT (push into the top resolution page) @8.58.
- **SFX** 2.46 paper_slide · 4.14 marker_long (arc, 0.8 s) · 6.00 paper_rustle · 8.56 whoosh_soft.

### C6S003 · 8.64–13.69 · C6B003 · NIGHT
- **Words** "The hail mary is basically that he's gonna try to pass a resolution before the main resolution."
- **Why** "pass a resolution before the main resolution" → two real UN resolution papers on a lamp-lit desk: a small one is slid in FRONT of the big 'main resolution'.
- **FX** #5 document treatment (tilted 3D page, sepia, halftone) + 12 fps card slide · **Ref** R9 lamp pool (variation: desk, no cork)
- **Assets** N05 UN draft resolution pages 1971: A/L.632 (US 'important question' draft) + A/L.630 (Albania draft = main resolution) — UN ODS/Dag Hammarskjöld Library scans
- **Text** `resolution` t-label on the small page @11.44 · `before` serif-i @11.92 · `main resolution` label-box @12.32 (`resolution` @12.80)
- **Camera** slow push toward the small page. **Out** CA — the small page lifts toward camera @13.6 (cut while it moves).
- **SFX** 8.66 lamp_click · 11.40 paper_slide · 12.30 paper_slide (2nd take, −2 st) · 13.60 whoosh_soft.

### C6S004 · 13.69–21.13 · C6B004 · PAPER
- **Words** "Which basically says that hey, this Taiwan question is an important question, which means you cannot vote on this with just a majority."
- **Why** "this Taiwan question is an important question… you cannot vote on this with just a majority" → the real draft's body text; the words 'important question' are highlighted; 'majority' crossed.
- **FX** #18 highlighter (body text only, §10.6.6) + §10.6.4 text contrast call-out + #19 pen cross · **Ref** Pinterest idea: 'UN document close-up with yellow highlighter, Vox text call-out'
- **Assets** N05 (A/L.632 page, 2nd use); two paper layers (paper_cream_01 + paper_fiber_01 top 90 %)
- **Text** `Taiwan question` t-label @15.21 (celadon underline) · highlighter stroke on the printed words 'important question' @17.05 (stroke 0.9 s) · paragraph fades to 20 % + punch-in 10 % @18.4, key words return · `majority` t-serif @20.57 with a pen cross drawn after it (@20.9)
- **Camera** punch-in 1.0→1.1 (cam ease) at 18.4. **Out** W↓ @21.07.
- **SFX** 17.03 highlighter_swipe · 18.40 whoosh_soft · 20.90 pencil_scribble · 21.05 whoosh.

### C6S005 · 21.13–25.29 · C6B005 · GRID
- **Words** "You need two thirds to decide any kind of resolution on that."
- **Why** "You need two thirds to decide any kind of resolution" → a threshold chart: a dashed line at two-thirds height that the bars must clear.
- **FX** #2 chart (bars 12 fps, watercolour tops) + #13 `FX.text.count` · yellow key number · **Ref** D01 (variation: bars in ink/grey, threshold at ⅔, halftone UN Secretariat building across the base instead of the parliament)
- **Assets** paper_graph_01_hires (+_norm overlay); N06 UN Headquarters NYC 1960s–70s photo → `tools/halftone.py --sky-key` cut-out
- **Text** `TWO-THIRDS` label-box, **yellow key number** `2/3` t-display 220 px @21.45 (counts 0→2/3 as the dashed line rises 12 fps) · `resolution` t-label @24.01
- **Camera** static; last 6 frames punch-in on the dashed line. **Out** CA (punch-in mid-move) @25.2.
- **SFX** 21.43 counter_ticks (0.5 s) · 21.6 dot_ticks (bars) · 25.18 whoosh_soft.

### C6S006 · 25.29–29.77 · C6B006 · NIGHT
- **Words** "So people are first voting on just to decide if this is a important question or not."
- **Why** "people are first voting… to decide if this is a important question or not" → real photo of the 1971 General Assembly voting (delegates, voting board).
- **FX** #1 + #16 plate + #14 light weave (amp 0.4) + `FH` after the push · **Ref** —
- **Assets** N07 UN GA 1971 voting photo / the electronic voting board (UN Photo; AP) — 1 use
- **Text** `first` t-label @25.93 + `voting` @26.17 · `important question?` t-serif-i @28.49 (`question` @28.97)
- **Camera** push 1.0→1.12 to the voting board, `FH` @27.2. **Out** FW (light-flash whip, ←) @29.71.
- **SFX** 25.31 projector_click · 26.0 crt_hum (board, dur 3.5) · 29.69 whoosh.

### C6S007 · 29.77–34.97 · C6B007 · PAPER
- **Words** "And in that vote, we can see that US does not have a majority, right?"
- **Why** "in that vote… the US does not have a majority" → the Assembly as a dot hemicycle: the US side fills and stops short of the majority line.
- **FX** #2 dot-matrix semicircle (12 fps fill) + dashed majority line · **Ref** D06 / R8 (VARIATION: the arc sits low like the GA horseshoe, dots are tiny placards, title top-left serif with italic emphasis)
- **Assets** own graphic (dots in the real 1971 'important question' proportions — no numbers printed, DECISIONS #2); paper_stained_01_hires
- **Text** title t-serif `In that *vote*` @30.01 (`that` @30.17, `vote` @30.41 italic) · `US` t-label @32.49 on the grey arc · `not` @33.29 + `majority` @33.85 on the dashed line (ink)
- **Camera** slow drift right. **Out** continuous (same chart, camera keeps sliding) → C6S008.
- **SFX** 30.0 dot_ticks (fill, 1.6 s) · 33.80 tick_soft.

### C6S008 · 34.97–38.09 · C6B008 · PAPER
- **Words** "So China has more than enough votes to get Taiwan in."
- **Why** "China has more than enough votes" → the Beijing side of the same hemicycle fills past the majority line.
- **FX** #2 continued + yellow highlighter on the title's key word · **Ref** D06 continued
- **Assets** same graphic
- **Text** `CHINA` label-box (ink fill) @35.29 · `more than enough votes` t-serif-i word by word @35.85/36.09/36.25/36.49 · NO text on 'get Taiwan in' (slip)
- **Camera** drift continues; at 37.9 the camera starts a fast tilt up. **Out** W↑ @38.03.
- **SFX** 35.27 dot_ticks (1.2 s) · 37.98 whoosh.

### C6S009 · 38.09–41.69 · C6B009 · NIGHT
- **Words** "That means as soon as that vote comes to the floor in just a few minutes,"
- **Why** "as soon as that vote comes to the floor in just a few minutes" → the GA floor from above, a clock hand sweeping = minutes.
- **FX** #1 plate + #19 markup (clock-face circle drawn around the hall clock) · 12 fps · **Ref** —
- **Assets** N08 UN GA hall wide, rostrum + floor (UN Photo 1970s); N09 the hall's clock or a 1970s wall clock cut-out
- **Text** `the floor` t-label @40.25 · `a few minutes` serif-i @41.05 (`minutes` @41.29)
- **Camera** slow crane-down 0→−60 px. **Out** CA (crane continues into the next shot) @41.6.
- **SFX** 38.11 air_swell · 40.9 tick_soft (×4, clock).

### C6S010 · 41.69–45.45 · C6B009 · NIGHT
- **Words** "Taiwan is getting kicked out. China is officially in the United Nations."
- **Why** "Taiwan is getting kicked out. China is officially in the United Nations." → the real photo of the PRC delegation taking the 'CHINA' seat; Taiwan's celadon marker drops out of the frame.
- **FX** #16 plate + §10.6.3 contrast call-out on the CHINA nameplate (hard cut on the push) + #4 hero title · **Ref** —
- **Assets** N10 PRC delegation (Qiao Guanhua) seated behind the CHINA nameplate, UN GA Nov 1971 (UN Photo/AP); celadon Taiwan chip = own graphic
- **Text** `TAIWAN` t-label with celadon chip @41.69 → `kicked out` clean @42.49 (chip falls off-frame, 12 fps) · `CHINA` t-display **hero halate** @43.21 · `officially in the United Nations` t-label word-by-word @43.69/44.09/44.25/44.41/44.81
- **Camera** ease-in push to the nameplate; contrast call-out cuts in at peak velocity @43.21. **Out** W← @45.39.
- **SFX** 42.47 whoosh_soft (chip falls) · 43.19 boom_low + circuit-breaker clunk (contrast) · 45.37 whoosh.


## 2. Act II — The walk-out (45.45–72.64)
Music: pulse out; sustained pad/strings (INSTRUMENTS stem only); space around "crying" 57.69.

### C6S011 · 45.45–49.53 · C6B010 · PAPER
- **Words** "So everyone can see what's about to happen, and Taiwan can see what's about to happen."
- **Why** "everyone can see what's about to happen, and Taiwan can see" → the GA seating plan: every delegation's name card turns toward one seat — Taiwan's (ROC).
- **FX** #12 cards (12 fps) + #19 pen arrows converging · **Ref** NEW ref V1 'Assembly seating chart' (Pinterest: vintage theatre/parliament seating plan, typeset rows of name cards)
- **Assets** own graphic: GA seating plan typeset in Cooper Hewitt on paper_cream_02 (real 1971 member names in seat order — public record), ROC seat = celadon
- **Text** `everyone` serif-i @45.77 (all cards flip toward the ROC seat, 12 fps stagger) · `TAIWAN` t-label celadon underline @47.69 · pen arrows converge @48.3
- **Camera** slow push to the ROC seat. **Out** PT (push into the celadon seat) @49.47.
- **SFX** 45.75 paper_rustle (card flips) · 48.30 marker_long · 49.45 whoosh_soft.

### C6S012 · 49.53–54.49 · C6B011 · NIGHT
- **Words** "So Taiwan just walks up to the front, officially just withdraws from the United Nations."
- **Why** "Taiwan just walks up to the front, officially just withdraws from the United Nations" → THE moment: the ROC delegation (Chow Shu-kai) at the rostrum / leaving — in depth.
- **FX** #17 **2.5D #1** (backdrop hall + delegates mid + Chow Shu-kai fg) + light rays + haze · `FH` when the dolly stops · **Ref** 2.5D-quad / 2.5D-campus (expected/layouts) as variation: interior instead of exterior
- **Assets** N11 ROC delegation at the rostrum / walking out, 25 Oct 1971 (AP/UN Photo) ≥ 3000 px + 2.5D layer set 🛠
- **Text** `walks up to the front` t-label @50.65 · `WITHDRAWS` t-display **hero halate** @52.73 · `from the United Nations` clean @53.29/53.45/53.61/53.93
- **Camera** dolly z −80→120 + x drift toward the rostrum; `FH` @53.0. **Out** CA (dolly still moving) @54.43.
- **SFX** 49.55 air_swell · 50.6 whoosh_soft (dolly) · 52.71 boom_low (very soft).

### C6S013 · 54.49–58.41 · C6B012 · NIGHT
- **Words** "Now, after they withdraw, I think people are crying right?"
- **Why** "after they withdraw… people are crying" → archival newsreel of the delegation leaving the hall (moving faces).
- **FX** #1 footage + #14 gate weave + flicker (amp 0.6) inside a projector frame · **Ref** —
- **Assets** N12 newsreel 25–26 Oct 1971 ROC delegation leaving the UN (AP Archive / British Pathé / Reuters on YouTube — © fair use), 6–10 s
- **Text** `withdraw` t-label @55.45 · `crying` t-serif-i clean @57.69
- **Camera** none (footage moves). **Out** W→ @58.35.
- **SFX** 54.51 projector_loop (dur 3.9) · 58.33 whoosh.

### C6S014 · 58.41–65.21 · C6B013 · PAPER
- **Words** "Some of the Taiwanese delegations is cr some of the people from the Taiwanese delegation are crying. They don't exactly know what's gonna happen in the future."
- **Why** "some of the people from the Taiwanese delegation are crying. They don't exactly know what's gonna happen in the future." → close crops of delegation faces as torn photo cards; then they blur into fog = an unknown future.
- **FX** #12 collage (torn edges, halftone multiply, 12 fps pin-ups) + reverse focus hunt at 'future' · **Ref** D07 collage (VARIATION: three portrait crops in a row, no poster type)
- **Assets** N11/N12 stills (2nd use as crops) + N13 a second press photo of ROC delegates (AP)
- **Text** `Taiwanese delegation` t-label @61.69 (`delegation` @62.25) · `crying` t-serif-i @62.73 · `the future` serif-i @64.57/64.65 as the cards defocus
- **Camera** slow pull-back. **Out** CA (pull-back continues, cards drift) @65.15.
- **SFX** 61.67 paper_slide ×3 (staggered) · 64.6 air_swell.

### C6S015 · 65.21–72.64 · C6B014 · NIGHT
- **Words** "We have well we have a clip of George H. W. Bush just sitting there with his head in his hands, and while the Taiwanese delegation is walking out."
- **Why** "a clip of George H. W. Bush just sitting there with his head in his hands… while the Taiwanese delegation is walking out" → the real photo/clip of Bush, head in hands at the US desk.
- **FX** #16 plate + §10.6.3 contrast call-out (on Bush) + #19 pen circle around his hands · **Ref** markup-map_SC064 (markups riding on the photo) as variation
- **Assets** N14 **George H. W. Bush head in hands, UN, 25 Oct 1971** (AP/UPI — the famous one) ≥ 1600 px; or the AP newsreel clip if found (prefer clip)
- **Text** `GEORGE H. W. BUSH` label-box @66.81 · pen circle around his hands @68.89 (`head in his hands`: `head` @68.89 `hands` @69.45 serif-i) · `walking out` t-label @71.61 (an ink arrow points off-frame to the exit)
- **Camera** push to Bush; contrast call-out hard-cuts in at @68.6 (peak of an ease-in push). **Out** PS (the photo slides down onto a printed page) @72.58.
- **SFX** 66.79 pop_soft · 68.6 circuit-breaker clunk · 68.9 marker_scratch · 72.56 paper_slide.


## 3. Act III — The famous pictures (72.64–102.08)
Music: pad; a light ironic pizz/ostinato enters at "dancing" 80.00, thins under the walk-back.

### C6S016 · 72.64–76.48 · C6B015 · PAPER
- **Words** "One of the most famous pictures, probably in Taiwan, they still remember this to very day."
- **Why** "one of the most famous pictures, probably in Taiwan… remember this to this very day" → the same picture is now printed in a Taiwanese newspaper/history page.
- **FX** #5 newspaper (sepia, halftone grows with zoom) — pull-back reveal (the photo-in-print idea of §10.7 without a quote) · **Ref** §10.7 Lincoln reel (pull-back part only)
- **Assets** N15 a real Taiwanese newspaper/textbook page carrying the Bush or walk-out photo (聯合報 / 中央日報 archives, history textbook scan — © fair use); fallback: typeset page in our fonts with N14 printed in a column (no fake masthead)
- **Text** `most famous pictures` t-label @72.96 (`famous` @73.12, `pictures` @73.44) · `TAIWAN` t-label celadon @74.32 · `to this very day` serif-i @75.68/75.92/76.16
- **Camera** pull-back + upward pan 1.2 s (cam ease). **Out** W↓ @76.42.
- **SFX** 72.66 paper_slide · 76.40 whoosh.

### C6S017 · 76.48–80.00 · C6B016 · NIGHT
- **Words** "There are a lot of African countries, especially Tanzania, that's"
- **Why** "a lot of African countries, especially Tanzania" → a rich satellite/atlas map of Africa: many countries glow faintly, then Tanzania is singled out.
- **FX** #3 map (map kit, satellite) + #20 call-out: §10.6.3 contrast call-out on Tanzania + pin + label · **Ref** D14 satellite-with-district look (VARIATION: continent scale, the district = Tanzania)
- **Assets** M01 `assets/maps/kit/` Africa satellite/atlas (≥ 3840 px) + country outlines (Natural Earth admin-0)
- **Text** `African countries` t-label @77.12 (outlines draw on 12 fps) · `TANZANIA` label-box @78.72 (contrast call-out hard-cut @78.6)
- **Camera** ease-in push from Africa to Tanzania. **Out** CA (push continues) @79.94.
- **SFX** 77.10 marker_long (outlines) · 78.6 circuit-breaker clunk · 78.72 map_pin.

### C6S018 · 80.00–84.16 · C6B016 · NIGHT
- **Words** "dancing, basically trying to rub it into the Taiwanese delegation that they lost."
- **Why** "that's dancing, basically trying to rub it into the Taiwanese delegation that they lost" → THE famous photo of the Tanzanian delegates dancing in the GA aisle.
- **FX** #16 plate + #14 light weave (it's press film) + slow zoom · **Ref** —
- **Assets** N16 **Tanzanian delegation dancing in the UN GA, 25 Oct 1971** (AP/UPI) ≥ 1600 px
- **Text** `dancing` t-serif-i clean @80.00 · `rub it in` t-label @81.12 (`rub` 81.12) · `lost` serif-i @83.52
- **Camera** slow zoom 1.0→1.08 on the dancers. **Out** W← @84.10.
- **SFX** 80.0 air_swell (crowd murmur ambience `crowd`, dur 4.0, very low) · 84.08 whoosh.

### C6S019 · 84.16–88.64 · C6B017 · GRID
- **Words** "And this is happening all before the main vote that has taken place. Taiwan has withdrawn and they're dancing."
- **Why** "this is happening all before the main vote… Taiwan has withdrawn and they're dancing" → an order-of-events strip: WITHDRAWN ✓ → DANCING → MAIN VOTE (still ahead, greyed).
- **FX** #12 timeline axis + travelling dot (12 fps) + #18 rough stamp ✓ · **Ref** D05/R7 era-band idea as a horizontal ledger timeline (VARIATION)
- **Assets** paper_lined_01_hires; thumbnails of N11 + N16 (3rd use is a 120 px thumbnail — counts as reuse; OK under §10.9)
- **Text** `before` t-label @85.28 · `the main vote` serif-i @85.68 (greyed box at the right end) · `withdrawn` ✓ stamp @87.52 (celadon) · `dancing` @88.24 (thumbnail pops)
- **Camera** dot travels left→right; camera trucks with it. **Out** CA (truck continues) @88.58.
- **SFX** 85.26 tick_soft · 87.50 stamp_thud · 88.22 pop_soft.

### C6S020 · 88.64–92.24 · C6B018 · NIGHT
- **Words** "Now this becomes such a big deal that Tanzania tries to walk this back saying,"
- **Why** "this becomes such a big deal that Tanzania tries to walk this back" → real US newspaper front pages of 26 Oct 1971 slam down one on another.
- **FX** #5 newspapers (tilted 3D pages, sepia, halftone) + 12 fps stack · **Ref** Pinterest idea: 'headline pile-up, Vox newspaper stack'
- **Assets** N17 NYT 26 Oct 1971 front page ("U.N. Seats Peking and Expels Taipei") + 1–2 other papers (LA Times / Washington Post) — TimesMachine/newspapers.com previews, archive.org; © fair use
- **Text** `big deal` t-label @89.60 (as the 2nd page lands) · `TANZANIA` label-box @90.16 · `walk this back` serif-i @91.36
- **Camera** camera rises over the pile. **Out** PS (a typed card slides over the pile) @92.18.
- **SFX** 88.66 paper_flip · 89.58 paper_slide · 90.14 paper_slide · 92.16 paper_slide.

### C6S021 · 92.24–96.88 · C6B018 · PAPER
- **Words** "Hey, we weren't like we weren't celebrating that they're crying or they're getting kicked out or anything, you know?"
- **Why** "Hey, we weren't… celebrating that they're crying or they're getting kicked out" (Tanzania's walk-back, in the narrator's paraphrase) → a typed statement card attributed to Tanzania.
- **FX** #13 typewriter text (letters at 12 fps) + D08 telegram card · **Ref** D08 telegram (VARIATION: plain carbon-copy press statement, no masthead, no seals)
- **Assets** typeset card on paper_cream_01 (Haskoy mono-ish weight); attribution line `— Tanzania (paraphrased)`
- **Text** `we weren't celebrating` typed @92.48/92.56/93.84 (word starts: we 92.48, weren't 92.56, celebrating 93.84) · `crying` @94.80 · `kicked out` @95.60
- **Camera** slow push. **Out** W↑ @96.82.
- **SFX** 92.46 letter_ticks (typing, 1.4 s) · 94.78 letter_ticks · 96.80 whoosh.

### C6S022 · 96.88–102.08 · C6B019 · NIGHT
- **Words** "We weren't dancing, we were just standing up or something. We tried walking it back, but like this becomes a very, very big deal."
- **Why** "We weren't dancing, we were just standing up or something… this becomes a very, very big deal" → the dancing photo again; a pen question-mark call-out 'standing up?' over the obviously dancing arms; headlines fly back in.
- **FX** #19 pen markup (§10.6.2, boil 4/s) + #16 + focal call-out (§10.6.5) on the dancers · **Ref** markup-map_SC064 variation (pen on photo)
- **Assets** N16 (2nd use, different crop)
- **Text** `weren't dancing` serif-i @97.28 · pen circle + `standing up?` t-label @98.16 · `very, very big deal` t-label word-by-word @101.04/101.28/101.52/101.68 as 3 headline strips (N17 crops) whip in
- **Camera** focal spot slides across the dancers. **Out** FW (light-flash whip →) @102.02.
- **SFX** 97.26 marker_scratch · 98.14 pencil_scribble · 101.0 paper_slide ×3 · 102.00 whoosh.


## 4. Act IV — Bush blames Kissinger (102.08–137.75)
Music: low drone; dark pulse returns on "domino" 136.71.

### C6S023 · 102.08–110.00 · C6B020 · PAPER
- **Words** "But nonetheless, this is one I want to show you this quote from George H.W. Bush. He later goes on to like, you know, give comments on everything that happened."
- **Why** "I want to show you this quote from George H. W. Bush. He later goes on to… give comments" → painting-to-print: a colour painting of Bush, then the pull-back reveals it printed in a newspaper column — the quote page.
- **FX** §10.7 painting-to-print reveal #1 (painting full-frame → pull-back + upward pan → column with rule frame, small-caps caption, pull-quote) · **Ref** §10.7 Lincoln reel
- **Assets** N18 colour painted portrait of George H. W. Bush (official portrait, Herbert E. Abrams / NPG — © fair use) ≥ 2000 px; typeset newspaper column (Crimson Pro / Haskoy, sepia newsprint, NO real masthead)
- **Text** `this quote` t-serif-i over the painting @103.92/104.08 · caption small caps `GEORGE H. W. BUSH` @104.64 (under the printed picture) · `later` t-label @106.56 (column headline area) · `comments` @108.40
- **Camera** full-frame painting → 1.2 s pull-back + upward pan @105.2, then slow drift. **Out** continuous (same page; camera slides down to the pull-quote) → C6S024.
- **SFX** 102.10 air_swell · 105.2 paper_rustle (pull-back) · 108.38 tick_soft.

### C6S024 · 110.00–116.64 · C6B021 · PAPER
- **Words** "And he basically says that we lost the vote because of the visit that Kissinger did during the vote to China."
- **Why** "we lost the vote because of the visit that Kissinger did during the vote to China" → the pull-quote in bold serif, underlined word by word as spoken; Kissinger's China visit pictured in the next column.
- **FX** §10.7 pull-quote pen underline per word + #18 rough + small inset photo pops · **Ref** §10.7 (pull-quote part)
- **Assets** same page + N19 Kissinger with Zhou Enlai in Beijing, Oct 1971 (White House / NARA — PD) as a printed inset
- **Text** pull-quote words appear + underline in sync: `we` @111.52 `lost` @111.76 `the` @112.16 `vote` @112.32 `because` @112.80 `of` @113.12 `the` @113.44 `visit` @113.60 · `KISSINGER` @114.08 (printed caption under the inset) · `to China` @115.92/116.08 · attribution `— George H. W. Bush (paraphrased)`
- **Camera** slow drift down the column. **Out** W→ @116.58.
- **SFX** 111.5 pencil_scribble (underlines, 4 s, soft) · 114.06 pop_soft (inset) · 116.56 whoosh.

### C6S025 · 116.64–124.56 · C6B022 · NIGHT
- **Words** "He's like, that vote is basically like cutting my legs out of under me while I'm trying to make sure that everyone still believes the US is with Taiwan"
- **Why** "that vote is… like cutting my legs out from under me while I'm trying to make sure that everyone still believes the US is with Taiwan" → split frame: Bush lobbying in New York | the floor under his card is literally cut by a pen line and drops.
- **FX** split-screen + #19 pen cut line + 12 fps drop + #16 · **Ref** NEW ref V4 'split-screen contrast' (editorial before/after split with a hand-drawn divider)
- **Assets** N20 Bush lobbying delegates at the UN, Oct 1971 (AP/UN Photo); N19 (2nd use) on the other side, dimmed
- **Text** `cutting my legs out` t-serif-i @118.88 (`legs` @119.44) — pen line slices under Bush's card @119.4, the lower strip drops 12 fps · `the US` t-label @122.96/123.20 · `with Taiwan` celadon underline @123.68/123.84
- **Camera** slow push on the Bush half. **Out** CA (the cut strip is still falling) @124.50.
- **SFX** 118.86 marker_scratch (cut) · 119.5 paper_tear · 123.66 pop_soft.

### C6S026 · 124.56–129.59 · C6B023 · NIGHT
- **Words** "while the administration is visiting, visiting China. So he says if it wasn't for that visit."
- **Why** "while the administration is visiting China. So he says if it wasn't for that visit" → the visit itself: Kissinger and Zhou Enlai in Beijing, full frame; the handshake circled.
- **FX** #16 plate + `FH` after the zoom + #19 pen circle · **Ref** —
- **Assets** N21 Kissinger–Zhou Enlai, Beijing, Oct 1971 — a different frame from N19 (NARA/White House PD; Xinhua ©)
- **Text** `the administration` t-label @124.80/125.04 · `visiting China` serif-i @125.76 / `China` @127.12 · pen circle on the handshake + `that visit` @128.80/128.96
- **Camera** fast zoom in @125.6 then `FH` @126.0. **Out** W↓ @129.53.
- **SFX** 125.58 whoosh_soft · 128.78 marker_scratch · 129.51 whoosh.

### C6S027 · 129.59–134.87 · C6B024 · PAPER
- **Words** "We might have won that vote, but because of that visit, Taiwan was out of the out of the United Nation,"
- **Why** "We might have won that vote, but because of that visit, Taiwan was out of the United Nations" → the hemicycle of C6S007 returns: the US arc creeps toward the line (might have won)… then Taiwan's celadon dot drops out of the Assembly.
- **FX** #2 D06 motif callback + 12 fps · **Ref** D06 (callback of C6S007, camera from the other side)
- **Assets** graphic from C6S007
- **Text** `might have won` serif-i @129.75 (`won` @129.99) · `TAIWAN` celadon dot + label @132.39 · `out` @132.95 (dot falls, 12 fps) · `United Nations` t-label @134.07
- **Camera** slow orbit 6°. **Out** PT (push after the falling celadon dot — it lands as the first domino's edge) @134.81.
- **SFX** 129.9 dot_slide · 132.93 pop_soft + whoosh_soft · 134.79 whoosh_soft.

### C6S028 · 134.87–137.75 · C6B025 · NIGHT
- **Words** "and then it has a cascading or like a domino effect."
- **Why** "then it has a cascading or like a domino effect" → a row of dominoes on a dark table under a lamp, each face a country flag (desaturated), starts to fall.
- **FX** 3D domino row (CSS 3D, perspective) + #4 hero title + 12 fps topple · **Ref** NEW ref V2 'domino row' (Vox 'domino theory' animation; Pinterest: tabletop domino chain macro)
- **Assets** own 3D dominoes; flag faces from Commons SVGs (PD), desaturated; first domino = Taiwan (celadon edge)
- **Text** `cascading` t-label @135.67 · `DOMINO EFFECT` t-display **hero halate** @136.71 (`effect` @137.19)
- **Camera** low dolly along the row, following the fall. **Out** CA (dominoes still falling — cut on the fall) @137.69.
- **SFX** 135.65 tick_soft · 136.7 dot_ticks (domino clacks, 1.0 s) · 137.67 whoosh_soft.


## 5. Act V — Dominoes: allies switch, Japan (137.75–156.47)
Music: one rhythmic track at full, low hits on the big moments; peak on "big hit" 155.43.

### C6S029 · 137.75–142.47 · C6B026 · NIGHT
- **Words** "Slowly allies are now switching their recognition from Taiwan to the CCP."
- **Why** "allies are now switching their recognition from Taiwan to the CCP" → world map: countries that recognised Taipei turn from celadon to ink one after another (the dominoes continue as a map).
- **FX** #3 map + burn reveal (celadon burns to ink with a charred ring, 12 fps) + #20 labels · **Ref** R11 (VARIATION: dark atlas instead of beige; regions + small leader labels) · D13 ghost-map tone
- **Assets** M02 map kit world atlas/satellite ≥ 3840 px + admin-0 outlines; burn_a/b.png
- **Text** `allies` t-label @138.55 · `switching recognition` serif-i @139.43/140.07 · `TAIWAN` celadon label @140.87 · `CCP` ink label-box @141.67
- **Camera** slow pan east across the map. **Out** W→ @142.41.
- **SFX** 138.6 burn_crackle (dur 3.6, soft) · 142.39 whoosh.

### C6S030 · 142.47–149.75 · C6B027 · PAPER
- **Words** "The biggest one for Taiwan, the biggest hit is from Japan, which is the biggest trade partner. It's they're becoming very close allies slowly."
- **Why** "The biggest hit is from Japan, which is the biggest trade partner. They're becoming very close allies" → ranked bars of Taiwan's trade partners topped with flag circles — Japan's is the tallest; then a link line Japan ↔ Taiwan.
- **FX** #2 bars topped with circles (12 fps) + rough link line · **Ref** D02 / R4 (VARIATION: flag discs instead of portraits, horizontal title top-right, no values, no numbers)
- **Assets** flag SVGs (PD), paper_stained_01_hires; ghosted halftone Tokyo 1970s skyline behind (N22)
- **Text** `biggest hit` t-label @143.83 · `JAPAN` label-box @144.87 (Japan's bar rises tallest, 12 fps) · title t-serif `the *biggest* trade partner` @145.83/145.99/146.39/146.71 · `close allies` serif-i @148.47 (link line draws Japan ↔ Taiwan)
- **Camera** slow push to Japan's disc. **Out** PT (push into the Japan disc) @149.69.
- **SFX** 143.8 dot_ticks (bars) · 144.85 pop_soft · 148.45 marker_long · 149.67 whoosh_soft.

### C6S031 · 149.75–156.47 · C6B028 · NIGHT
- **Words** "So Japan switching recognition from Taiwan to to China was definitely a big hit."
- **Why** "So Japan switching recognition from Taiwan to China was definitely a big hit" → the real 1972 Japan–PRC signing photo in Beijing.
- **FX** #16 plate + §10.6.5 focal call-out moving from the Japanese side to the Chinese side · **Ref** —
- **Assets** N23 Japan–China Joint Communiqué signing, Beijing, 29 Sep 1972 (Kyodo/Xinhua ©, fair use; or Commons PD-Japan photo) — no names on screen
- **Text** `JAPAN` t-label @150.23 · `switching recognition` serif-i @150.87/151.35 · `CHINA` t-label @153.99 · `big hit` t-display clean @155.43 (`hit` @155.83)
- **Camera** slow pan left→right with the focal spot. **Out** CRT (picture collapses to a line, becomes the TV of the next shot) @156.41.
- **SFX** 150.2 air_swell · 155.41 boom_low · 156.39 crt_off.


## 6. Act VI — Grief and anger at home (156.47–183.11)
Music: drone + soft keys; +2 dB lift in the VO gap 181.59–183.11.

### C6S032 · 156.47–161.11 · C6B029 · NIGHT
- **Words** "Back in Taiwan, everyone's seeing this, especially the dancing scene, that's really famous."
- **Why** "Back in Taiwan, everyone's seeing this, especially the dancing scene" → a 1970s Taiwanese TV set in a living room shows the dancing news footage.
- **FX** #11 TV (new set) + CRT power-on + glass glare + `data-color-grading` retro · **Ref** §10.1.7 better screens — Taiwanese set
- **Assets** N24 1970s Tatung/Sampo wood-cabinet TV photo (screen keyed, `*_screen.json`) — fallback ✅ `assets/intro/screens/tatung_tv20cge_frame.png`; on screen N12/N16 footage (dancing)
- **Text** `BACK IN TAIWAN` t-label celadon underline @156.47 · `the dancing scene` serif-i @158.87/159.03 · `famous` @160.31
- **Camera** slow push toward the screen. **Out** PT (push through the screen glass) @161.05.
- **SFX** 156.49 crt_click + crt_hum (dur 4.6) · 161.03 whoosh_soft.

### C6S033 · 161.11–164.71 · C6B030 · PAPER
- **Words** "And they just cannot keep in the anger and the grief."
- **Why** "they just cannot keep in the anger and the grief" → 1971 Taipei: protesters/students against the UN decision, in Vox layered panels.
- **FX** #10 Vox layered backgrounds (2–3 tinted panels drifting at their own speed) + newsprint overlay · **Ref** intro IS002 Vox layered (VARIATION: three crowd panels, no portrait)
- **Assets** N25 Taipei protests / rallies after the UN withdrawal, Oct 1971 (CNA/UDN archive ©; Taiwan National Archives) — 2–3 photos
- **Text** `anger` t-serif 120 px @163.35 · `grief` t-serif-i @164.15
- **Camera** panels drift at 3 speeds. **Out** W← @164.65.
- **SFX** 161.13 paper_slide ×3 · 164.63 whoosh.

### C6S034 · 164.71–172.07 · C6B031 · NIGHT
- **Words** "We we have some comments from the economic minister that plays a big part in the technological revolution that Taiwan is about to have,"
- **Why** "comments from the economic minister that plays a big part in the technological revolution Taiwan is about to have" → the minister (Sun Yun-suan, unnamed here) as a halftone portrait; behind him a wafer glint + streaks = the coming tech revolution.
- **FX** #8 light streaks behind a cut-out + #16 · `CS` on the label · **Ref** —
- **Assets** N26 Sun Yun-suan 1970s portrait (ROC gov / Commons PD-ROC-exempt or Executive Yuan) ≥ 1600 px → cut-out; ✅ `assets/intro/photos/wafer_12in.jpg` (glint)
- **Text** `economic minister` t-label @166.47 (`minister` @167.03) · `technological revolution` serif-i @169.03/170.07 · `Taiwan` celadon @170.87
- **Camera** slow push 1.0→1.06; streaks open @169.0. **Out** CA (push continues) @172.01.
- **SFX** 166.45 pop_soft · 169.0 air_swell (streaks) · 172.0 whoosh_soft.

### C6S035 · 172.07–175.67 · C6B032 · PAPER
- **Words** "and he was just like, wow, they couldn't believe that this happened."
- **Why** "he was just like, wow, they couldn't believe that this happened" → his reaction as a typed card clipped beside his photo (narrator's paraphrase).
- **FX** #13 `FX.text.random` (letters in random order) + paper-clip card · **Ref** NEW ref V3 'personnel dossier / clipped note' (manila folder, paper clip, typed card) — first appearance
- **Assets** manila folder + clip (Texturelabs paper / own); N26 (2nd use, small)
- **Text** `wow` t-serif-i @173.27 · `couldn't believe` t-display @174.15 (`believe` @174.47) — attributed `— the economic minister (paraphrased)`
- **Camera** static, tiny drift. **Out** W↓ @175.61.
- **SFX** 173.25 paper_slide · 174.13 letter_ticks · 175.59 whoosh.

### C6S036 · 175.67–180.95 · C6B033 · NIGHT
- **Words** "They fought a war with the United States. They were on the winning side, and seems like they're just getting"
- **Why** "They fought a war with the United States. They were on the winning side" → Cairo Conference 1943: Chiang Kai-shek with Roosevelt and Churchill — allies of WWII.
- **FX** #1 + #14 gate weave (1940s) + #19 pen underline under the three · **Ref** —
- **Assets** N27 Cairo Conference, Nov 1943 (US Army Signal Corps — PD) ≥ 2400 px (+ optional 5 s newsreel of it, NARA)
- **Text** `fought a war` t-label @175.83 · `with the UNITED STATES` @176.71/177.03 · `winning side` serif-i @178.39 (pen underline under the three leaders)
- **Camera** slow push on Chiang. **Out** CA (push continues) @180.89.
- **SFX** 175.69 projector_loop (dur 5.2) · 178.37 marker_scratch.

### C6S037 · 180.95–183.11 · C6B033 · NIGHT
- **Words** "left out hanging."
- **Why** "…seems like they're just getting left out hanging" → the empty ROC seat at the UN, nameplate removed — left hanging (held through the 1.5 s pause).
- **FX** #16 plate, very slow drift; vignette tightens · **Ref** —
- **Assets** N28 empty delegation chair / removed 'CHINA' nameplate at the UN after 25 Oct 1971 (AP/UN Photo); fallback: N08 crop with the ROC seats empty
- **Text** `left out hanging` t-serif-i clean @180.95/181.27/181.59
- **Camera** slow drift right; hold through the pause. **Out** FW (light-flash whip ↑, into the night sky) @183.05.
- **SFX** 181.6 air_swell (bed lift in the VO gap) · 183.03 whoosh.


## 7. Act VII — 'Stay dignified and strengthen ourselves' (183.11–206.68)
Music: warm new layer on "statement" 194.04; swell under "Keep on fighting" 200.92.

### C6S038 · 183.11–188.63 · C6B034 · NIGHT
- **Words** "Now, by the night of the UN vote, I'm guessing the shock dissipates a bit."
- **Why** "by the night of the UN vote… the shock dissipates a bit" → UN Headquarters lit at night, New York; the word 'shock' dissolves into grain.
- **FX** #16 + #8 streaks (cool) + text dissolve (`FX.text.rise` reversed into grain) · **Ref** —
- **Assets** N29 UN Headquarters at night, 1960s–70s (UN Photo / Commons PD-USGov)
- **Text** `the night` t-label @183.83/184.07 · `of the UN vote` @184.39/184.71/185.27 · `shock` t-display @186.95, dissolves from 187.43 (`dissipates`)
- **Camera** slow crane up the Secretariat facade. **Out** CA (crane continues) @188.57.
- **SFX** 183.13 air_swell · 186.93 boom_low (soft) · 187.4 wind (dur 1.2).

### C6S039 · 188.63–193.56 · C6B035 · PAPER
- **Words** "This is when the leader, Chiang Kai-shek. Very cool name, hopefully I'm pronouncing that correctly."
- **Why** "This is when the leader, Chiang Kai-shek" (+ aside about the name) → Chiang Kai-shek's portrait card with his name; held through the aside.
- **FX** #12 card (torn edge, halftone multiply) + name label-box + `FH` once · **Ref** D07-like card on paper (VARIATION: single portrait card, celadon tape corners)
- **Assets** N30 Chiang Kai-shek colour portrait (official painting or 1960s–70s colour photo; ROC gov — PD in Taiwan) ≥ 2000 px
- **Text** `the leader` t-label @189.11 · `CHIANG KAI-SHEK` label-box (ink fill) @189.83 — no text on the aside
- **Camera** slow push 1.0→1.05, `FH` @190.4. **Out** W→ @193.50.
- **SFX** 189.81 pop_soft · 193.48 whoosh.

### C6S040 · 193.56–196.76 · C6B036 · NIGHT
- **Words** "Puts out a statement that's still very famous in Taiwan to this very day."
- **Why** "puts out a statement that's still very famous in Taiwan to this very day" → radio-wave rings spread from Taipei across a rich relief map of Taiwan (the message reaching the island).
- **FX** §10.6.7 radio-wave rings (on a flattened 3D map plane) + focal blur + #3 map (map kit relief) · **Ref** R12 (VARIATION: island lit celadon on dark relief, rings instead of a glow edge)
- **Assets** M03 map kit Taiwan shaded relief ≥ 3840 px + ✅ `assets/intro/maps/taiwan_mask.png` (alpha version)
- **Text** `statement` t-label @194.04 · `very famous` serif-i @194.92/195.08 · `TAIWAN` celadon @195.56
- **Camera** map plane tilted rotateX 30°, slow rotate. **Out** CA (rings still expanding as we cut) @196.70.
- **SFX** 194.02 tone_blip (rings, soft ×3) · 196.68 whoosh_soft.

### C6S041 · 196.76–201.96 · C6B037 · PAPER
- **Words** "The statement basically says, stay dignified and strengthen ourselves. Keep on fighting."
- **Why** "stay dignified and strengthen ourselves. Keep on fighting." → the real slogan as a hanging calligraphy scroll unrolling (莊敬自強 / 處變不驚); his English words land word by word beside it, each underlined by pen.
- **FX** scroll unroll (12 fps) + §10.7 pen underline per word + `CS` reveal on the last line · **Ref** NEW ref V5 'calligraphy scroll unroll' (Pinterest: hanging-scroll reveal, ink on rice paper)
- **Assets** N31 real photo/scan of the slogan 莊敬自強 處變不驚 (1971 calligraphy, banner, or Central Daily News 26 Oct 1971 front page — © fair use); paper_fiber_01 + paper_cream_02 (two layers)
- **Text** `stay` @198.28 `dignified` @198.76 `and` @199.40 `strengthen` @199.56 `ourselves` @200.20 (t-serif 72 px, each underlined as spoken) · `Keep on fighting.` t-display ink @200.92/201.16/201.32 (`CS` settle)
- **Camera** slow pull-back as the scroll finishes unrolling. **Out** W↑ @201.90.
- **SFX** 196.8 paper_rustle (unroll, dur 1.4) · 198.26 pencil_scribble (underlines, 2.2 s) · 200.9 stamp_thud (soft) · 201.88 whoosh.

### C6S042 · 201.96–206.68 · C6B038 · NIGHT
- **Words** "That was basically the message, and that's exactly what Taiwanese leaders are about to do."
- **Why** "That was basically the message, and that's exactly what Taiwanese leaders are about to do" → Taiwan's seat of government in motion (Presidential Office, Taipei) as archival film.
- **FX** #1 footage + #14 gate weave + #16 · **Ref** —
- **Assets** ✅ `assets/intro/footage/taiwan_1960_presidential_office_taipei.mp4` (8 s) — or N32 1970s ROC cabinet meeting newsreel if found (better match for 'leaders')
- **Text** `the message` t-label @202.68/202.84 · `Taiwanese leaders` serif-i @204.36/205.16
- **Camera** slow push. **Out** CA (traffic moving) @206.62.
- **SFX** 201.98 projector_loop (dur 4.7).


## 8. Act VIII — The engineer son: Chiang Ching-kuo (206.68–306.45)
Music: travelling pulse low; darker 244–262 (hostage); lift on "Deng Xiaoping" 271.41; calm under the engineers idea 295–306.

### C6S043 · 206.68–215.40 · C6B039 · PAPER
- **Words** "Now, the main leader behind this fight, at least economically speaking, is gonna be Chiang Kai-shek's son, whose name is Chiang Ching-kuo."
- **Why** "the main leader behind this fight, at least economically speaking, is gonna be Chiang Kai-shek's son, whose name is Chiang Ching-kuo" → the Chiang Kai-shek card (C6S039 motif) slides aside; the son's card slides out from behind it.
- **FX** #12 cards (12 fps slide) + label-boxes · **Ref** D07-like card (motif from C6S039)
- **Assets** N30 (motif card) + N33 Chiang Ching-kuo 1970s portrait (ROC gov PD-in-Taiwan) ≥ 2000 px
- **Text** `the main leader` t-label @207.00/207.16/207.40 · `economically` t-label small @209.32 · `CHIANG KAI-SHEK'S` @211.32 + `son` @212.76 (son's card emerges) · `CHIANG CHING-KUO` label-box @213.72
- **Camera** truck right with the son's card. **Out** W← @215.34.
- **SFX** 211.3 paper_slide · 213.70 pop_soft · 215.32 whoosh.

### C6S044 · 215.40–218.68 · C6B040 · NIGHT
- **Words** "Not being racist. That uh that is the name, Chiang Ching-kuo."
- **Why** "That is the name, Chiang Ching-kuo" (after the aside) → close on Chiang Ching-kuo's face; the name is re-stamped as the hero title.
- **FX** #16 + #4 hero title + #13 `FX.text.odometer` (letters lock) · **Ref** —
- **Assets** N33b a second Chiang Ching-kuo photo, colour if possible (1970s premier) — prefer different from N33
- **Text** no text on 'Not being racist' · `CHIANG CHING-KUO` t-display **hero halate** odometer locks @217.16 (lock done by 217.9, holds ≥ 0.5 s)
- **Camera** slow push. **Out** FW (light-flash whip →, lands on the split frame) @218.62.
- **SFX** 217.14 odometer_tick (0.6 s).

### C6S045 · 218.68–221.72 · C6B041 · PAPER
- **Words** "Now, this is where I wanna point out the contrast."
- **Why** "this is where I wanna point out the contrast" → split frame: father | son, a rough ink divider draws down the middle.
- **FX** split screen + #19 markup underline as divider + #18 rough · **Ref** V4 split-screen (2nd use, vertical divider, VARIATION)
- **Assets** N30 + N33 crops (motif)
- **Text** `the contrast` t-display ink @221.00/221.16
- **Camera** static. **Out** CA — left half pushes in (becomes next shot) @221.66.
- **SFX** 221.14 marker_long.

### C6S046 · 221.72–227.56 · C6B042 · NIGHT
- **Words** "Once again, the dad was the military guy, one of the most successful generals in Chinese history, maybe."
- **Why** "the dad was the military guy, one of the most successful generals in Chinese history" → Chiang Kai-shek in uniform: Generalissimo reviewing troops (archival film/photo).
- **FX** #1 + #14 weave + #4 hero title · **Ref** —
- **Assets** N34 Chiang Kai-shek in military uniform, 1930s–40s (Whampoa / WWII; PD) — film preferred (NARA / Pathé)
- **Text** `the dad` t-label @222.60 · `MILITARY` t-display **hero halate** @223.24 · `most successful generals` serif-i @224.52/224.76/225.24
- **Camera** slow push. **Out** W→ @227.50.
- **SFX** 221.74 projector_loop (dur 5.8) · 223.22 boom_low (soft).

### C6S047 · 227.56–235.48 · C6B043 · PAPER
- **Words** "And people around him who were ruling, you know, advising him on the on the governing of this island, all military people, generals and stuff."
- **Why** "people around him who were ruling… advising him on the governing of this island, all military people, generals" → an isotype ring of seats around one figure, every seat a general's peaked-cap pictogram; a halftone group photo of KMT generals ghosted behind; Taiwan outline faint.
- **FX** #2 isotype (icons pop at 12 fps) + halftone ghost · **Ref** D03 / R5 (VARIATION: icons in a ring/table instead of rows)
- **Assets** own pictograms (general cap / engineer helmet+compass) adapted from `assets/icons/graduate*.svg`; N35 group photo of KMT/ROC generals 1950s (PD-in-Taiwan) halftoned
- **Text** `ruling` t-label @229.32 · `governing` serif-i @231.96 + `this island` @232.60/232.76 (Taiwan outline celadon 15 %) · `ALL MILITARY` label-box @233.32/233.64 · `generals` @234.52
- **Camera** slow top-down rotate 4°. **Out** CA (rotation continues) @235.42.
- **SFX** 227.6 dot_ticks (icons, 1.4 s) · 233.30 stamp_thud (soft).

### C6S048 · 235.48–238.92 · C6B044 · NIGHT
- **Words** "Kid is very different. He he is, I think, an engineer."
- **Why** "Kid is very different. He is, I think, an engineer." → Chiang Ching-kuo cut-out on dark; blueprint lines draw over/around him (engineer).
- **FX** cut-out + blueprint line draw-on (stroke-dashoffset) + `CS` · **Ref** —
- **Assets** N33 cut-out (2nd use) + paper_blueprint_01_hires as a masked glow behind
- **Text** `very different` serif-i @236.20/236.36 · `ENGINEER` t-display clean @238.36
- **Camera** slow push. **Out** W↓ @238.86.
- **SFX** 236.2 marker_long (lines) · 238.84 whoosh.

### C6S049 · 238.92–244.28 · C6B045 · PAPER
- **Words** "He studied in Moscow in his teenage years, while he's studying in the Soviet Union, by the way."
- **Why** "He studied in Moscow in his teenage years, while he's studying in the Soviet Union" → a tilted vintage colour map of Eurasia: route China → Moscow drawn in rough yellow marker; a 1925 photo of the teenage Chiang Ching-kuo pops at Moscow.
- **FX** #3 tilted map plane + #18/#19 rough yellow marker route + pin + `FH` after the push · **Ref** D10 / R10 (VARIATION: continental scale, route west instead of east)
- **Assets** M04 vintage colour atlas map of Asia/USSR 1920s–30s (David Rumsey CC BY-NC → only if allowed; else Commons PD atlas scans) + json; N36 Chiang Ching-kuo in Moscow c. 1925–27 (PD)
- **Text** `MOSCOW` t-label + pin @239.64 · `teenage years` serif-i @240.68 (photo card pops) · `SOVIET UNION` t-label @242.84
- **Camera** camera tracks the route west, pushes to Moscow, `FH` @240.0. **Out** CA (push continues) @244.22.
- **SFX** 239.0 marker_long (route, 0.9 s) · 239.62 map_pin · 240.66 pop_soft.

### C6S050 · 244.28–247.64 · C6B046 · NIGHT
- **Words** "The dad turns on the communists, so Soviet Union basically"
- **Why** "The dad turns on the communists" → a 1927 newspaper headline: Chiang Kai-shek breaks with the communists (Shanghai, April 1927).
- **FX** #5 newspaper on a lamp-lit desk + #18 highlighter (body line) · **Ref** —
- **Assets** N37 1927 newspaper page on Chiang's split with the communists (NYT April 1927 / Chronicling America / archive.org — PD)
- **Text** `turns on the communists` t-label @244.84/245.32/245.48/245.56 · highlighter on the printed body line @245.6
- **Camera** push down the page. **Out** PS (a ledger page slides over) @247.58.
- **SFX** 244.30 paper_flip · 245.55 highlighter_swipe · 247.56 paper_slide.

### C6S051 · 247.64–254.45 · C6B046–C6B047 · GRID
- **Words** "takes him hostage for like 12 years. He's just stuck in this country. He went there to study and now he's stuck in this country for 12 years."
- **Why** "takes him hostage for like 12 years. He's just stuck… he went there to study and now he's stuck in this country for 12 years" → a ledger of years: twelve tick-boxes fill at 12 fps behind the teenage photo; HOSTAGE stamp.
- **FX** #13 `FX.text.count` 1→12 + #18 rough stamp + yellow key number · **Ref** R1/D01 label-box idea as a ledger count (VARIATION)
- **Assets** paper_lined_01_hires + ✅ K+E ledger scan as a card (`assets/intro/papers/ke1960_business_ruled_orange*`) at native size; N36 (2nd use)
- **Text** `HOSTAGE` stamp (ink, rough, settles) @248.04 · **yellow key number** `12 YEARS` count 1→12 @248.84 (count ends 249.6) · `stuck` serif-i @250.29 · `to study` t-label @252.05/252.13 · `12 years` re-highlighted @253.81
- **Camera** slow push on the ledger. **Out** CA (push continues) @254.39.
- **SFX** 248.02 stamp_thud · 248.82 counter_ticks (0.8 s) · 253.79 highlighter_swipe.

### C6S052 · 254.45–262.53 · C6B048 · NIGHT
- **Words** "He he gets sent to some freaking like plant to work to while his dad is like the leader of China because he's against the communists."
- **Why** "he gets sent to some… plant to work, while his dad is like the leader of China because he's against the communists" → 1930s Soviet heavy-machinery plant on film; an inset card of the father as China's leader.
- **FX** #1 footage + #14 gate weave + #16 + inset card (12 fps) · **Ref** —
- **Assets** N38 Uralmash / Soviet heavy-industry plant footage 1930s (archive.org Soviet newsreels, Net-Film ©) 8 s; N30 (inset, motif)
- **Text** no text on the 'plant' phrase · `his dad` t-label @259.17 (inset card slides in) · `leader of China` serif-i @260.05/260.29/260.45 · `against the communists` t-label @261.49
- **Camera** slow push on the furnace. **Out** W← @262.47.
- **SFX** 254.47 projector_loop (dur 8.0) · 259.15 paper_slide · 262.45 whoosh.

### C6S053 · 262.53–266.93 · C6B049 · PAPER
- **Words** "But yeah, so he's in Soviet Union, he's learns a lot. He went to a political school."
- **Why** "he's in Soviet Union, he learns a lot. He went to a political school." → an old city map of Moscow: pen circle on the school's location.
- **FX** #3 old city map + §10.6.2 pen circle · **Ref** D09 old city map (VARIATION: Moscow, sepia, tilted 12°)
- **Assets** M05 Moscow city plan 1910s–20s (Baedeker 1914 'Moskau' / Commons PD) ≥ 3000 px + json (Volkhonka St.)
- **Text** `learns a lot` serif-i @265.01 · pen circle + `political school` t-label @266.21/266.53
- **Camera** push to the circle. **Out** PS (two photo cards slide onto the map) @266.87.
- **SFX** 265.0 paper_rustle · 266.19 marker_scratch.

### C6S054 · 266.93–272.85 · C6B050 · PAPER
- **Words** "And guess who was one of his classmates at that political school? A young boy named Deng Xiaoping."
- **Why** "guess who was one of his classmates at that political school? A young boy named Deng Xiaoping" → two 1920s photo cards side by side: young Chiang Ching-kuo + a face-down card that flips to young Deng Xiaoping.
- **FX** #12 cards + card flip (12 fps) + #19 pen bracket 'classmates' · **Ref** D15 relationship (VARIATION: two cards + bracket instead of circles)
- **Assets** N36 (3rd use, small card) + N39 young Deng Xiaoping, c. 1920s (France/Moscow; PD) ≥ 1200 px
- **Text** `classmates` t-label @268.13 (pen bracket joins the two cards) · `DENG XIAOPING` label-box (ink) @271.41 as the card flips
- **Camera** static then slow push to Deng. **Out** CA (push continues) @272.79.
- **SFX** 268.11 marker_long · 271.39 paper_flip.

### C6S055 · 272.85–279.89 · C6B051 · NIGHT
- **Words** "The same person who's gonna go on to take over China after Mao Zedong, open up China, you know, implement this thing that turns around the economy,"
- **Why** "The same person who's gonna go on to take over China after Mao Zedong, open up China… turns around the economy" → cutting-the-curve: young Deng's face → older Deng (late 1970s), same zoom; Mao's portrait behind on 'Mao'.
- **FX** #15 `FX.curveCut` (young → old, cut at peak velocity) + `FH` after it lands · **Ref** —
- **Assets** N39 → N40 Deng Xiaoping c. 1979 (e.g. White House 1979 visit, NARA PD) ≥ 2000 px; N41 Mao portrait (Tiananmen gate, Commons)
- **Text** `the same person` t-label @273.01/273.33 · `MAO ZEDONG` t-label @275.41 (Mao portrait panel 1.0 s) · `open up China` serif-i @276.45/276.77/276.93 · `economy` @279.41
- **Camera** curve-cut zoom @274.2; `FH` @274.6. **Out** W→ @279.83.
- **SFX** 274.18 whoosh_big (curve) · 275.39 pop_soft · 279.81 whoosh.

### C6S056 · 279.89–285.09 · C6B052 · NIGHT
- **Words** "what is it called communism with Chinese characteristics or something. Socialism with Chinese characteristics."
- **Why** "…Socialism with Chinese characteristics" (after the self-correction) → the giant Deng Xiaoping billboard (Shenzhen), at dusk; the corrected phrase lands only when he says it.
- **FX** #17-lite parallax (billboard + sky as two layers) + #13 `FX.text.rise` · **Ref** NEW ref V6 'propaganda billboard' (Pinterest: dusk billboard with type set into the sky)
- **Assets** N42 Deng Xiaoping billboard, Shenzhen (Commons CC BY-SA / press ©)
- **Text** nothing during 'communism… or something' · `Socialism` @283.25 `with` @283.73 `Chinese` @283.89 `characteristics` @284.29 (t-serif-i, clean, word by word)
- **Camera** slow tilt up the billboard. **Out** CA (tilt continues) @285.03.
- **SFX** 279.91 wind (dur 3.3, low) · 283.23 air_swell.

### C6S057 · 285.09–291.73 · C6B053 · PAPER
- **Words** "But yeah, so Deng Xiaoping his classmate, but Kuo learns a lot. The kid learns a lot in uh in in Moscow."
- **Why** "Deng Xiaoping his classmate, but Kuo learns a lot… in Moscow" → back to the two classmate cards: Deng's card slides off; Chiang Ching-kuo's stays over the Moscow map.
- **FX** #12 card slide + map callback · **Ref** D09 callback (Moscow plan) + C6S054 cards
- **Assets** M05 + N36/N39 cards (motif)
- **Text** `classmate` t-label @287.01 (Deng card slides away) · `learns a lot` serif-i @288.29 · `MOSCOW` t-label @291.09
- **Camera** slow pull-back to the map. **Out** W↓ @291.67.
- **SFX** 287.0 paper_slide · 291.65 whoosh.

### C6S058 · 291.73–295.25 · C6B054 · GRID
- **Words** "He learns a lot about politics, engineering, but he also sees that"
- **Why** "He learns a lot about politics, engineering, but he also sees that" → an engineer's notebook: two tabbed sections POLITICS / ENGINEERING underlined in pen.
- **FX** #18 pen underline + tabbed notebook (2 paper layers) · **Ref** Pinterest idea: 'engineering notebook spread with tabs' (intro IS014 idea card VARIATION)
- **Assets** paper_graph_01_hires (+ paper_cream top 90 %)
- **Text** `politics` t-serif @292.61 · `engineering` t-serif @293.25 (pen underline each) · `sees` serif-i @294.53
- **Camera** slow push. **Out** PT (push into the 'engineering' tab) @295.19.
- **SFX** 292.59 pencil_scribble · 293.23 pencil_scribble (−2 st) · 295.17 whoosh_soft.

### C6S059 · 295.25–303.41 · C6B055 · NIGHT
- **Words** "if you put enough people in charge who are engineers, you can create like you can build industry in a country."
- **Why** "if you put enough people in charge who are engineers, you can… build industry in a country" → 1930s Soviet industrialisation poster + footage of plants/dams rising, Vox layered.
- **FX** #10 Vox layered (poster as B-roll §10.5) + #1 footage inset · **Ref** intro IS002 Vox layered (VARIATION: poster-led, diagonal panels)
- **Assets** N43 Soviet first five-year-plan poster (1929–32; Commons PD-RU/PD-old) colour; N44 Dneprostroi/Magnitogorsk construction footage 1930s (archive.org)
- **Text** `in charge` t-label @297.65 · `ENGINEERS` t-display clean @298.53 · `build industry` serif-i @301.65/302.05 · `country` @302.93
- **Camera** panels drift; slow push. **Out** W↑ @303.35.
- **SFX** 295.27 paper_slide · 298.5 projector_loop (inset, dur 4.0) · 303.33 whoosh.

### C6S060 · 303.41–306.45 · C6B056 · PAPER
- **Words** "The state could build industry if engineers are in charge."
- **Why** "The state could build industry if engineers are in charge" → a blueprint card spells the idea as an equation: STATE + ENGINEERS → INDUSTRY.
- **FX** #13 word-by-word + #19 pen arrow + blueprint ground · **Ref** Pinterest idea: 'blueprint equation card'
- **Assets** paper_blueprint_01_hires (+ _norm)
- **Text** `The state` @303.41/303.49 · `could build` @303.81/304.05 · `industry` @304.29 · `if engineers` @304.69/305.01 · `are in charge` @305.49/305.73/305.97 (t-display bone on blueprint, pen arrow draws to INDUSTRY @305.97)
- **Camera** static; last 6 frames slide right. **Out** CA (slide) @306.39.
- **SFX** 304.27 tick_soft · 305.95 marker_long.


## 9. Act IX — The engineers' cabinet (306.45–362.06)
Music: steady pulse + melodic stem; small lifts on Sun Yun-suan 329.66 and K. T. Li 344.30.

### C6S061 · 306.45–313.66 · C6B057 · NIGHT
- **Words** "So when he's in put when he's put in charge of like, hey, let's make Taiwan into an economic power because we don't have any of the options."
- **Why** "when he's put in charge… let's make Taiwan into an economic power because we don't have any of the options" → Chiang Ching-kuo as premier (1972 swearing-in / at his desk).
- **FX** #16 plate + #4 hero title · **Ref** —
- **Assets** N45 Chiang Ching-kuo sworn in as Premier, 1972, or at his desk (ROC gov / CNA)
- **Text** `in charge` t-label @308.69 · `TAIWAN` celadon underline @310.13 · `ECONOMIC POWER` t-display **hero halate** @311.09/311.49 · `no options` — none (no text on 'any of the options')
- **Camera** slow push. **Out** W← @313.60.
- **SFX** 306.47 air_swell · 311.07 boom_low (soft) · 313.58 whoosh.

### C6S062 · 313.66–318.14 · C6B058 · NIGHT
- **Words** "The world doesn't recognize us anymore, so we have to do something to become important again."
- **Why** "The world doesn't recognize us anymore, so we have to do something to become important again" → the world map dims to ink; only Taiwan stays lit celadon, then it glows brighter.
- **FX** #3 map + R12 region fill + glow edge + halftone · **Ref** R12 (VARIATION: world scale on the dark atlas, island alone)
- **Assets** M02 (motif) + M03 Taiwan relief mask
- **Text** `the world` t-label @313.90 · `doesn't recognize us` serif-i @314.14/314.46 · `become important again` t-label @316.94/317.34/317.66
- **Camera** pull-back from Taiwan to the world, then push back in. **Out** PS (a paper org-chart slides over the map) @318.08.
- **SFX** 314.4 boom_low (soft) · 316.9 air_swell · 318.06 paper_slide.

### C6S063 · 318.14–322.46 · C6B059 · PAPER
- **Words** "He first thing he does is basically, you know, change the cabinet around him."
- **Why** "the first thing he does is… change the cabinet around him" → a top-down cabinet table: seat cards shuffle around the premier's seat.
- **FX** #12 cards reshuffle (12 fps) + D15 diagram style · **Ref** D15 relationship diagram (VARIATION: round table seating, not a triangle)
- **Assets** own graphic; N46 1972 ROC cabinet (Executive Yuan) group photo, halftoned as the table's ghost
- **Text** `first` t-label @318.54 · `change the cabinet` serif-i @320.86/321.18/321.26
- **Camera** slow rotate of the table 6°. **Out** continuous → C6S064 (same table).
- **SFX** 320.84 paper_rustle (shuffle, 1.0 s).

### C6S064 · 322.46–329.26 · C6B060 · PAPER
- **Words** "He puts fills his cabinet with a lot of engineers, a lot of important guys, including the economic minister that plays a big role."
- **Why** "He fills his cabinet with a lot of engineers, a lot of important guys, including the economic minister" → the same table: general-cap icons flip to engineer icons one by one; one seat circles for the economic minister.
- **FX** #2 isotype flip (12 fps) + #19 pen circle · **Ref** D03 / R5 (callback of C6S047 icons — now flipping)
- **Assets** own pictograms (motif from C6S047)
- **Text** `ENGINEERS` t-display ink @324.78 (icons flip, 1.2 s) · `important` t-label @325.74 · `economic minister` serif-i @327.42/327.90 (pen circle on one seat)
- **Camera** push to the circled seat. **Out** PT (into the circled seat → dossier) @329.20.
- **SFX** 324.76 dot_ticks (flips) · 327.40 marker_scratch · 329.18 whoosh_soft.

### C6S065 · 329.26–337.26 · C6B061–C6B062 · NIGHT
- **Words** "His name is Sun Yun-suan. That's the guy we've talked about before, too. He's an electric engineer who studied in China when he came to Taiwan."
- **Why** "His name is Sun Yun-suan… He's an electric engineer who studied in China when he came to Taiwan" → Sun Yun-suan's personnel dossier on a lamp-lit desk: photo clipped, typed fields fill in; a mini route China → Taiwan on the card.
- **FX** NEW ref V3 dossier card + #13 typewriter fields + mini map route (pen) · **Ref** V3 'personnel dossier' (2nd use, full version)
- **Assets** N26 Sun Yun-suan (2nd use) + a second, younger Sun photo if found (N26b, 1940s–50s Taipower); manila folder; ✅ `assets/intro/maps/pacific_relief_grey.jpg` crop for the mini route
- **Text** `SUN YUN-SUAN` label-box @329.66 · `before` t-label small @332.46 · typed field `electric engineer` @333.58/334.22 · `China` @335.82 → `Taiwan` @336.70 (pen route draws on the card, celadon end)
- **Camera** push into the card, slight rotate. **Out** W↓ @337.20.
- **SFX** 329.64 paper_slide (folder) · 333.56 letter_ticks · 335.8 marker_long · 337.18 whoosh.

### C6S066 · 337.26–341.82 · C6B063 · PAPER
- **Words** "He was the one who fixed the energy grid when all the nationalists were fleeing over."
- **Why** "He was the one who fixed the energy grid when all the nationalists were fleeing over" → a blueprint of Taiwan's power grid: lines and substations light up across the island; ships (1949) arrive from the west.
- **FX** #3 map (blueprint styling) + line draw-on + pin pops + small ship icons sliding 12 fps · **Ref** Pinterest idea: 'blueprint infrastructure map'; R11 leader-labels
- **Assets** paper_blueprint_01_hires + Taiwan outline (M03 mask) + N47 1949 Nationalist retreat ships/troops at Keelung photo (PD-in-Taiwan) inset
- **Text** `fixed` t-label @337.98 · `ENERGY GRID` t-display @338.46 (lines draw 1.0 s) · `nationalists` t-label @340.06 · `fleeing` serif-i @340.86 (ships slide in)
- **Camera** slow push. **Out** CA (ships still sliding) @341.76.
- **SFX** 338.44 marker_long (grid) · 338.9 tone_blip ×3 (substations) · 340.84 paper_slide.

### C6S067 · 341.82–350.86 · C6B064 · NIGHT
- **Words** "Another important person in the story later is gonna be K. T. Li is a physicist, but now he has become like the treasury guy, the money guy inside of the country in the cabinet."
- **Why** "K. T. Li is a physicist, but now he has become like the treasury guy, the money guy" → K. T. Li's dossier card (motif): PHYSICIST typed, then struck through to TREASURY; 1970s New Taiwan dollar notes fan out.
- **FX** V3 dossier (3rd use, VARIATION: card rotated, ledger insert) + #19 pen strike + 12 fps fan · **Ref** V3
- **Assets** N48 K. T. Li 1970s portrait (ROC gov PD / Commons) ≥ 1600 px; N49 1970s NT$ banknotes (Commons, scans)
- **Text** `K. T. LI` label-box @344.30 · typed `physicist` @345.66 · pen strike + `treasury` @347.74 · `money guy` serif-i @348.62 (notes fan) · `cabinet` t-label @350.22
- **Camera** slow push, then truck right with the notes. **Out** W→ @350.80.
- **SFX** 344.28 paper_slide · 345.64 letter_ticks · 347.72 marker_scratch · 348.6 paper_rustle (notes) · 350.78 whoosh.

### C6S068 · 350.86–357.50 · C6B065 · NIGHT
- **Words** "And then there are a bunch of other people we'll talk about who are also engineers who are part of this uh cabinet that he's setting up,"
- **Why** "a bunch of other people we'll talk about who are also engineers who are part of this cabinet" → a cork board under a lamp: faces of the cabinet pinned, red-string replaced by ink string, 'engineer' tags.
- **FX** #12 cards pinned stop-motion + string draw-on + lamp pool · **Ref** R9 cork board (VARIATION: cabinet board, ink string, celadon pins = Taiwan's government)
- **Assets** ✅ `assets/textures/cork_01.jpg` (CC BY — credit); N50 3–4 more 1970s ROC cabinet portraits (engineer-ministers; ROC gov) — **no names on screen** (narrator: 'we'll talk about')
- **Text** `bunch of other people` t-label @351.58 · `ENGINEERS` tags pop @354.14 · `cabinet` serif-i @356.14
- **Camera** slow crane across the board. **Out** continuous → C6S069.
- **SFX** 350.88 pin_pop ×4 (staggered) · 354.12 marker_long (string).

### C6S069 · 357.50–362.06 · C6B066 · NIGHT
- **Words** "and they're gonna play an important role in a lot of projects, not just in the this technological project."
- **Why** "they're gonna play an important role in a lot of projects, not just in this technological project" → strings run from the faces out to many project cards; one card — a chip — is highlighted.
- **FX** string draw-on + #18 highlighter + `FH` on the chip card · **Ref** R9 continued
- **Assets** board continued; ✅ `assets/intro/photos/intel8088_chip.jpg` crop (chip card)
- **Text** `important role` t-label @358.38 · `a lot of projects` serif-i @359.10/359.26/359.42 · `technological project` label-box @360.94 (the chip card)
- **Camera** pull-back then rack to the chip card (`FH` @361.2). **Out** FW (light-flash whip →) @362.00.
- **SFX** 358.4 marker_long · 360.92 pin_pop · 361.98 whoosh.


## 10. Act X — Becoming Taiwanese (362.06–425.09)
Music: thin under 379–401; warm lift on "democracy" 419.49; playful tick at "spoil" 422.69.

### C6S070 · 362.06–368.78 · C6B067 · PAPER
- **Words** "Another thing he changes is that he starts having Taiwanese people who were already on the island when the nationalists came over."
- **Why** "he starts having Taiwanese people who were already on the island when the nationalists came over" → a vintage map of Taiwan: celadon dots (native Taiwanese) across the island; ink dots arrive from the west (1949).
- **FX** #3 vintage map + dot fills (12 fps) + #20 labels · **Ref** R11 (VARIATION: beige vintage Taiwan map, two dot populations)
- **Assets** ✅ `assets/intro/maps/formosa_1943_japanese_aviation_map.jpg` (+json) or M06 a 1940s–50s colour map of Taiwan
- **Text** `Taiwanese people` t-label celadon @364.70 · `already on the island` serif-i @366.06/366.54/366.86 · `nationalists` ink label @367.66
- **Camera** slow push. **Out** CA (ink dots still arriving) @368.72.
- **SFX** 364.68 dot_ticks (1.4 s) · 367.64 dot_slide.

### C6S071 · 368.78–376.05 · C6B068 · GRID
- **Words** "He's now having some of those elites. You know, rise up to the governing level where they're taking part in the decisions government is making."
- **Why** "some of those elites rise up to the governing level where they're taking part in the decisions" → a tiered pyramid of seats on graph paper: celadon dots climb into the top tier.
- **FX** #2 dots climbing (12 fps) + rough tier lines · **Ref** R8/D06 dots (VARIATION: stepped pyramid instead of hemicycle)
- **Assets** paper_graph_01_hires (2 layers)
- **Text** `elites` t-label @369.90 · `rise up` serif-i @371.33 · `governing level` label-box @372.29 · `decisions` t-label @374.53
- **Camera** tilt up with the climbing dots. **Out** W↑ @375.99.
- **SFX** 371.31 dot_slide (1.2 s) · 375.97 whoosh.

### C6S072 · 376.05–379.89 · C6B069 · NIGHT
- **Words** "Remember, still a one party state, they gonna change that down the line."
- **Why** "Remember, still a one party state, they gonna change that down the line" → the real KMT party emblem over a 1970s party congress photo; an arrow points 'down the line' to the right.
- **FX** #16 + #19 pen arrow · **Ref** —
- **Assets** N51 KMT party congress 1970s (ROC gov/CNA) + KMT emblem SVG (Commons PD)
- **Text** `ONE-PARTY STATE` t-display clean @376.93 · `change` serif-i @378.53 · `down the line` t-label @379.01 + pen arrow →
- **Camera** slow push. **Out** CA (arrow still drawing) @379.83.
- **SFX** 376.91 boom_low (soft) · 379.0 marker_long.

### C6S073 · 379.89–385.17 · C6B070 · NIGHT
- **Words** "But the reason now they're already thinking about change is because this I don't know where I heard this."
- **Why** "the reason now they're already thinking about change is because… I don't know where I heard this" → a lamp-lit shelf of history books (the narrator recalling a source); a question mark card.
- **FX** #16 + slow rack focus across spines (`FH`) · **Ref** Pinterest idea: 'dark library shelf, rack focus'
- **Assets** N52 shelf of history books (CC0 / Commons)
- **Text** `the reason` t-label @380.13/380.21 · `change` serif-i @382.21 · no text on the aside
- **Camera** rack along the shelf. **Out** PT (into one book) @385.11.
- **SFX** 380.0 page_turn (soft) · 385.09 whoosh_soft.

### C6S074 · 385.17–390.45 · C6B071 · PAPER
- **Words** "I think I heard this from Sarah Paine, you know? Uh she's she's great with uh especially Asian history."
- **Why** "I think I heard this from Sarah Paine… she's great with Asian history" → Sarah Paine's photo card + her book covers on Asian history.
- **FX** #12 cards + label-box · **Ref** D07-like card pair (VARIATION: photo + two book covers fanned)
- **Assets** N53 S. C. M. Paine portrait (US Naval War College — PD US gov) + N54 covers of her books (e.g. 'The Wars for Asia, 1911–1949', 'The Japanese Empire') — © fair use
- **Text** `SARAH PAINE` label-box @386.29 · `Asian history` serif-i @389.49/389.89
- **Camera** static drift. **Out** W← @390.39.
- **SFX** 386.27 paper_slide · 389.47 paper_slide (book) · 390.37 whoosh.

### C6S075 · 390.45–395.97 · C6B072 · NIGHT
- **Words** "Before this, they were like, hey, we are China, the world recognizes us, so we don't have to worry about Taiwanese people that much."
- **Why** "Before this… 'we are China, the world recognizes us'" → an ROC-era official map claiming all of China, the whole claim filled celadon.
- **FX** #3 vintage map + region fill (watercolour edge) + #20 label · **Ref** R12 (VARIATION: a claim-map, the big region is the claim)
- **Assets** N55 1950s–60s Republic of China official map showing the mainland + Taiwan (PD-in-Taiwan / Commons) ≥ 3000 px
- **Text** `we are China` t-display clean @391.73/391.81/392.05 · `the world recognizes us` serif-i @392.45/392.61/392.85/393.41 · `Taiwanese people` t-label small @394.61
- **Camera** slow pull-back to the whole claim. **Out** continuous → C6S076.
- **SFX** 391.7 air_swell.

### C6S076 · 395.97–401.41 · C6B073 · NIGHT
- **Words** "But now they're like, Well, we're not China anymore, so we have to get good at being Taiwanese."
- **Why** "now… we're not China anymore, so we have to get good at being Taiwanese" → the same map: the celadon drains from the mainland (burn reveal), only Taiwan stays lit.
- **FX** #3 burn reveal (celadon burns away from the mainland) + hero title · **Ref** R12 + s02 burn
- **Assets** N55 continued; burn_a/b.png
- **Text** `not China anymore` serif-i @397.97/398.13/398.53 · `BEING TAIWANESE` t-display **hero halate** @400.21/400.45
- **Camera** push from the mainland onto Taiwan, `FH` @399.6. **Out** W↓ @401.35.
- **SFX** 397.95 burn_crackle (2.0 s) · 400.19 chime_soft · 401.33 whoosh.

### C6S077 · 401.41–406.77 · C6B074 · PAPER
- **Words** "So one way they try to do this is like get more Taiwanese people into the ruling elite."
- **Why** "one way they try to do this is… get more Taiwanese people into the ruling elite" → a horizontal bar of the ruling elite: the celadon (Taiwanese) share grows from a sliver.
- **FX** #2 horizontal bars + serif title with italic emphasis word · **Ref** D04 / R6 (VARIATION: one stacked 100 % bar, before → after, no values)
- **Assets** paper_stained_01_hires; shapes only (no numbers)
- **Text** title word by word: `more` @403.49 `*Taiwanese*` @403.65 (celadon italic) `people` @404.53 `into the` @405.09/405.49 `ruling elite` @405.65/406.13
- **Camera** static. **Out** CA (bar done 406.2 and held; the camera slides right) @406.71.
- **SFX** 403.6 dot_ticks · 406.71 whoosh_soft.

### C6S078 · 406.77–413.09 · C6B075 · NIGHT
- **Words** "On top of that, they focus a lot more on the economy, get people rich. So hopefully, hopefully, you know, people are happy with the government."
- **Why** "they focus a lot more on the economy, get people rich… people are happy with the government" → a rising line over a ghosted map of Taiwan, with small 1970s prosperity photo cards popping along it.
- **FX** #2 dark line chart over ghost map (path draw-on) + photo pops · **Ref** D13 (VARIATION: one line, island ghost instead of a continent; photos as markers)
- **Assets** M03 ghost relief + N56 1970s Taiwan prosperity photos (Taipei shopping street, family with a TV/scooter — CNA/Taiwan archives) ×2
- **Text** `economy` t-label @408.69 · `get people rich` serif-i @409.17/409.41/409.57 · `happy` t-label @412.13 · `government` @412.69
- **Camera** camera tracks the line's head. **Out** W→ @413.03.
- **SFX** 408.7 marker_long (line, 1.2 s) · 409.5 pop_soft ×2 · 413.01 whoosh.

### C6S079 · 413.09–421.65 · C6B076 · PAPER
- **Words** "And on top of that, slowly there's gonna be democracy. In this story, Taiwan is gonna go from one party state to a democracy by the time we finish this story."
- **Why** "slowly there's gonna be democracy… Taiwan is gonna go from one party state to a democracy by the time we finish this story" → a timeline track: ONE-PARTY STATE on the left, a real ballot box/ballot at DEMOCRACY on the right, the 'this story' band in between.
- **FX** #2 line/track + era band + pin pops · **Ref** D05 / R7 (VARIATION: shaded band = 'this story', no years)
- **Assets** N57 Taiwan election ballot/ballot box photo (1990s; CEC / Commons) as the end marker; paper_cream_02
- **Text** `democracy` t-label faint @415.25 · `one party state` label-box @418.13 · `DEMOCRACY` t-display ink @419.49 · band label `this story` serif-i @420.69/421.09/421.25
- **Camera** slow truck along the track. **Out** continuous → C6S080 (same track).
- **SFX** 415.2 air_swell · 418.11 pop_soft · 419.47 stamp_thud (soft).

### C6S080 · 421.65–425.09 · C6B077 · PAPER
- **Words** "So I'm not trying to spoil anything, but that happens."
- **Why** "So I'm not trying to spoil anything, but that happens" → a strip of tape labelled 'spoiler' slaps over the DEMOCRACY end, then peels off again (light gag, same chart).
- **FX** tape slap (12 fps) + peel · **Ref** —
- **Assets** same chart; paper tape texture (Texturelabs / own)
- **Text** `spoil` t-label on the tape @422.69 · tape peels @424.37 (`happens`)
- **Camera** static. **Out** FW (light-flash whip ↑) @425.03.
- **SFX** 422.67 paper_tear (tape) · 424.35 paper_tear (peel, +2 st) · 425.01 whoosh.


## 11. Act XI — The 10 Major Projects (425.09–473.74)
Music: fullest pulse of the chunk on the list 438–446; recede at "none" 469.10.

### C6S081 · 425.09–432.86 · C6B078 · NIGHT
- **Words** "Now, the first thing this cabinet and the leader does is launch this infrastructure program that's called 10 Major Projects."
- **Why** "the first thing this cabinet and the leader does is launch this infrastructure program that's called 10 Major Projects" → the real 1970s Ten Major Construction Projects poster/stamp art in the dark, light streaks; '10' odometer locks as the hero title.
- **FX** #8 streaks + #4 hero title + #13 `FX.text.odometer` · **Ref** Pinterest idea: 'retro film-title over vintage poster art'
- **Assets** N58 Ten Major Construction Projects commemorative poster or ROC stamp sheet (1977–80; Chunghwa Post — © fair use / PD-in-Taiwan)
- **Text** `first` t-label @425.65 · `infrastructure program` serif-i @429.25/430.05 · `10` t-display **hero halate** odometer locks @431.17 (done 431.6) + `MAJOR PROJECTS` clean @431.65/432.05
- **Camera** slow push on the poster. **Out** CA (push continues) @432.80.
- **SFX** 425.11 air_swell · 431.15 odometer_tick (0.5 s) · 431.6 boom_low (soft).

### C6S082 · 432.86–438.14 · C6B079 · NIGHT
- **Words** "And this is really focused on building infrastructure and industry inside of Taiwan."
- **Why** "really focused on building infrastructure and industry inside of Taiwan" → 1970s Taiwan construction film: girders, cranes, a steel mill pour.
- **FX** #1 footage + #14 gate weave + #16 · **Ref** —
- **Assets** N59 1970s Taiwan construction newsreel (Sun Yat-sen Freeway / China Steel / Taoyuan airport construction — Taiwan Film & Audiovisual Institute, CNA, YouTube © fair use); ✅ `assets/intro/footage/taiwan_1960_steel_mill_molten.mp4` as the 'industry' insert
- **Text** `infrastructure` t-label @435.10 · `industry` t-label @436.06 · `inside Taiwan` serif-i celadon underline @437.18
- **Camera** none (footage moves); hard cut on the pour at 436.0. **Out** W↓ @438.08.
- **SFX** 432.88 projector_loop (dur 5.2) · 436.0 boom_low (pour, soft) · 438.06 whoosh.

### C6S083 · 438.14–446.62 · C6B080 · NIGHT
- **Words** "And it includes like ports roads, steel mills, shipyards, railways, nuclear plants, anything you can think of."
- **Why** "ports, roads, steel mills, shipyards, railways, nuclear plants, anything you can think of" → a sharp satellite map of Taiwan: each project pins in on its word with a small stamp-art card; the freeway draws as a yellow route.
- **FX** #3 satellite map + D14 yellow route + pins + stamp cards (12 fps) · **Ref** D14 (VARIATION: island scale, yellow route = Sun Yat-sen Freeway, cards instead of districts)
- **Assets** M07 map kit Taiwan satellite ≥ 3840 px (+ json lon/lat); N58 stamp art crops (6 cards)
- **Text** `ports` @439.82 (Taichung + Su-ao pins) · `roads` @440.78 (yellow route draws N→S, 1.2 s) · `steel mills` @441.74 (Kaohsiung) · `shipyards` @442.94 (Kaohsiung) · `railways` @443.90 (North-Link line draws) · `nuclear plants` @444.62 (Jinshan) · `anything you can think of` serif-i @445.50 — each a t-label beside its pin
- **Camera** slow pull-back so all pins fit by 445.5; holds 0.6 s. **Out** PS (paper sheet slides up over the map) @446.56.
- **SFX** 439.80 map_pin · 440.76 marker_long · 441.72 map_pin · 442.92 map_pin · 443.88 marker_long · 444.60 map_pin · 446.54 paper_slide.

### C6S084 · 446.62–451.74 · C6B081 · PAPER
- **Words** "They get a lot of money, they borrow money outside some of the money they get for zero interest rate from Saudi."
- **Why** "they borrow money outside, some of the money they get for zero interest rate from Saudi" → money flows (Sankey ribbons) from abroad into Taiwan; one ribbon labelled SAUDI ARABIA, '0 %' as the key number.
- **FX** #2 Sankey (ribbons draw on, 12 fps) + yellow key number · **Ref** D11 (VARIATION: on paper, flows right→left into the island, no amounts)
- **Assets** own graphic on paper_cream_01 (+ paper_fiber top 90 %); small Saudi Arabia + Taiwan map silhouettes (map kit)
- **Text** `money` t-label @447.34 · `borrow` @447.82 (ribbons start) · **yellow key number** `0%` + `zero interest` label @450.06 · `SAUDI ARABIA` t-label @451.02
- **Camera** slow push along the Saudi ribbon. **Out** continuous → C6S085.
- **SFX** 447.8 marker_long (ribbons, 1.6 s) · 450.04 counter_ticks (0.4 s) · 451.0 pop_soft.

### C6S085 · 451.74–456.94 · C6B082 · PAPER
- **Words** "I didn't know that was possible, but that happened. But yeah, they get a lot of money and invest a lot."
- **Why** "I didn't know that was possible, but that happened. But yeah, they get a lot of money and invest a lot" → the ribbons land in ten project boxes; the boxes fill.
- **FX** #2 Sankey continued + fills · **Ref** D11 continued
- **Assets** same graphic
- **Text** no text on the aside · `invest a lot` serif-i @455.82/456.30/456.46 (boxes fill 12 fps)
- **Camera** pan to the ten boxes. **Out** W→ @456.88.
- **SFX** 455.8 dot_ticks · 456.86 whoosh.

### C6S086 · 456.94–466.46 · C6B083 · NIGHT
- **Words** "And a lot of these work out like truly greatly. I don't know if that's proper grammar, but they work out really well. Some of them are still paying dividends to this very day."
- **Why** "a lot of these work out… really well. Some of them are still paying dividends to this very day" → then-and-now: 1970s freeway construction photo → the same freeway today (traffic at dusk).
- **FX** #16 + internal light-flash whip (then → now) + `FH` on landing · **Ref** Pinterest idea: 'then/now flash cut'
- **Assets** N60 Sun Yat-sen Freeway under construction 1970s (MOTC / CNA); N61 National Freeway 1 today (Commons CC BY-SA — credit)
- **Text** `work out` t-label @458.38 · `really well` serif-i @463.42/463.58 (after the flash) · `paying dividends` t-label @464.78/465.10 · `to this very day` @465.58/465.74/465.90
- **Camera** slow push; internal flash-whip @463.2; `FH` @463.6. **Out** CA (traffic moving) @466.40.
- **SFX** 456.96 air_swell · 463.18 whoosh (flash) · 465.9 tick_soft.

### C6S087 · 466.46–473.74 · C6B084 · NIGHT
- **Words** "But one important part of these 10 major projects, none of them were technological related. All of them were infrastructure related."
- **Why** "none of them were technological related. All of them were infrastructure related" → a dark list of the ten projects; focus pulls down the list; a TECHNOLOGY column stays empty, an INFRASTRUCTURE column fills with ticks.
- **FX** D12 dark list + focus pull + tick column (12 fps) · **Ref** D12 (VARIATION: two columns of ticks instead of amounts)
- **Assets** own typeset list (the ten official project names — public facts, in Cooper Hewitt t-label)
- **Text** `10 major projects` t-label @467.74 · `none` t-display clean @469.10 (TECHNOLOGY column header, empty dashes) · `technological` @469.98 · `ALL` @471.42 (ticks fill) · `infrastructure` serif-i @472.30
- **Camera** focus pull top→bottom. **Out** PS (a calendar page slides in) @473.68.
- **SFX** 467.7 tick_soft · 471.40 dot_ticks (ticks, 0.8 s) · 473.66 paper_flip.


## 12. Act XII — 'Bigger the better' and the Moon (473.74–536.57)
Music: airy layer from "technological breakthrough" 485.34; the chunk's biggest swell on "moon" 511.29.

### C6S088 · 473.74–479.34 · C6B085 · PAPER
- **Words** "Well, that changes just in a few months when the leader, Ching Chiang Ching-kuo,"
- **Why** "that changes just in a few months when the leader, Chiang Ching-kuo" → desk calendar pages flip (months); the Chiang Ching-kuo card (motif) lands on top.
- **FX** #12 page flips 12 fps + card · **Ref** —
- **Assets** N62 1970s desk/wall calendar pages (blank-month style, own or PD scan — no year printed); N33 card (motif)
- **Text** `a few months` serif-i @475.18/475.26/475.50 · `CHIANG CHING-KUO` label-box @477.50 (no text on 'Ching—')
- **Camera** static. **Out** continuous → C6S089 (card slides left into the diagram).
- **SFX** 475.2 paper_flip ×3 · 477.48 paper_slide.

### C6S089 · 479.34–483.42 · C6B086 · PAPER
- **Words** "he tells his secretary general, one of the guys who's also an engineer, basically telling him,"
- **Why** "he tells his secretary general, one of the guys who's also an engineer" → a relationship diagram starts: the Chiang Ching-kuo circle → a grey silhouette circle 'secretary general' (unnamed until 590.06).
- **FX** D15 relationship diagram (circles, arrows via `FX.markup.arrow`) · **Ref** D15 (VARIATION: horizontal chain, grey nodes)
- **Assets** N33 circle crop; silhouette (✅ `assets/intro/cutouts/silhouette_exec.png` style, a NEW matte cut from the Fei Hua photo N80 — never recognisable)
- **Text** `secretary general` t-label @480.06/480.62 · `engineer` tag @482.06
- **Camera** slow drift. **Out** W↑ @483.36.
- **SFX** 480.04 pop_soft · 482.04 marker_long · 483.34 whoosh.

### C6S090 · 483.42–491.58 · C6B087 · NIGHT
- **Words** "Hey, let's figure out some kind of technological breakthrough that Taiwan could take advantage of and become world class and whatever the technology is."
- **Why** "let's figure out some kind of technological breakthrough that Taiwan could take advantage of and become world class, whatever the technology is" → a memo on a lamp-lit desk; the premier's words type out.
- **FX** #13 typewriter (12 fps) + D08 memo + lamp pool · **Ref** D08 telegram (VARIATION: carbon-copy memo, no letterhead seals — typeset recreation)
- **Assets** typeset memo on paper_cream_02, lamp pool
- **Text** typed: `technological breakthrough` @485.34/485.98 · `Taiwan` @486.86 · `world class` @489.10/489.42 · `whatever the technology is` @490.14/490.62/490.78/491.26
- **Camera** slow push down the memo. **Out** continuous → C6S091.
- **SFX** 485.3 letter_ticks (typing, 6 s, soft).

### C6S091 · 491.58–495.61 · C6B088 · NIGHT
- **Words** "You come up with some proposal, let me know. And he says Bigger the better."
- **Why** "You come up with some proposal, let me know. And he says Bigger the better." → the memo's last line 'Bigger the better' — underlined twice in pen.
- **FX** #13 typed + §10.6.2 pen double underline + #4 hero (clean on paper — no halate) · **Ref** D08 continued
- **Assets** same memo
- **Text** typed `proposal` @492.46 · `Bigger the better` t-display ink @494.57/494.97/495.13 + pen double underline @495.2
- **Camera** punch-in 1.0→1.15 on the line. **Out** W← @495.55.
- **SFX** 492.44 letter_ticks · 495.2 pencil_scribble ×2 · 495.53 whoosh.

### C6S092 · 495.61–502.09 · C6B089 · PAPER
- **Words** "That was just initial instructions. The instruction had nothing to do with chips. It was just we gotta get good at technology."
- **Why** "The instruction had nothing to do with chips. It was just we gotta get good at technology." → a 1970s chip on paper gets a rough pen X; the word TECHNOLOGY spreads wide.
- **FX** #19 pen cross + #13 `FX.text.fill` (yellow pop → ink) · **Ref** —
- **Assets** ✅ `assets/intro/photos/intel8088_chip.jpg` (2nd use) or N63 a 1970s DIP IC macro (Commons CC)
- **Text** `nothing to do with` t-label @498.17 · `chips` @498.97 + pen X @499.2 · `TECHNOLOGY` t-display (fill) @501.29
- **Camera** slow pull-back. **Out** CA (pull-back continues) @502.03.
- **SFX** 498.95 marker_scratch (X) · 501.27 tick_soft.

### C6S093 · 502.09–508.81 · C6B090 · PAPER
- **Words** "One of the reasons these people later, there's like a lot of documentaries made here, and the reason they were so focused on technology at this point is"
- **Why** "there's like a lot of documentaries made here, and the reason they were so focused on technology at this point" → a film-strip collage of Taiwanese documentary stills pinned on paper.
- **FX** #12 collage + film-strip frames (12 fps pins) · **Ref** D07 collage poster (VARIATION: film-strip frames, sprockets)
- **Assets** N64 stills from Taiwanese documentaries about the chip industry (PTS / TaiwanPlus / CNA documentaries — © fair use, credited); film-strip frame PNG (own)
- **Text** `documentaries` t-label @504.57 · `technology` serif-i @507.45
- **Camera** slow truck across the strip. **Out** W→ @508.75.
- **SFX** 502.11 paper_slide ×3 · 508.73 whoosh.

### C6S094 · 508.81–513.69 · C6B091 · NIGHT
- **Words** "because they just saw the United States go to the freaking moon. They were like, damn, this is gonna be the future."
- **Why** "they just saw the United States go to the moon… this is gonna be the future" → Apollo 11 broadcast on a 1969 TV set (the Moon landing as people saw it).
- **FX** #11 TV (new set: a 1960s RCA Victor / wood console) + CRT power-on + Apollo footage graded · **Ref** §10.1.7 better screens
- **Assets** N65 1960s RCA Victor (or other console) TV photo, screen keyed + `_screen.json`; N66 Apollo 11 TV broadcast footage (NASA — PD)
- **Text** `UNITED STATES` t-label @509.85 · `MOON` t-display **hero halate** @511.29 · `the future` serif-i @513.29/513.37
- **Camera** push toward the screen. **Out** PT (push through the screen into the Moon) @513.63.
- **SFX** 508.83 crt_click + crt_hum (dur 4.8) · 511.27 air_swell.

### C6S095 · 513.69–519.85 · C6B092 · NIGHT
- **Words** "The future is gonna be something we can't even imagine. Like 50 years ago or 20 years ago, no one was imagining going to the moon,"
- **Why** "something we can't even imagine. Like 50 years ago or 20 years ago, no one was imagining going to the moon" → Aldrin on the Moon in depth; at '50 years ago' and '20 years ago' two small cards of older Moon fantasies drift in.
- **FX** #17 **2.5D #2** (sky / Aldrin / LM / foreground regolith) + haze + two inset cards · **Ref** 2.5D (expected/layouts) VARIATION: lunar surface, light from the left
- **Assets** N67 Apollo 11 AS11-40-5903 (Aldrin, NASA PD, 3000+ px) + 2.5D layer set 🛠; N68 Méliès 'A Trip to the Moon' (1902, PD) still; N69 1950s Moon illustration (Chesley Bonestell/Collier's ©, or PD pulp cover)
- **Text** `can't even imagine` serif-i @514.89/515.13/515.37 · `50 years ago` t-label @516.09 (card 1) · `20 years ago` t-label @517.05 (card 2) · `going to the moon` @519.05
- **Camera** dolly z −60→140, x drift; `FH` @518.0. **Out** CA (dolly still moving) @519.79.
- **SFX** 513.71 air_swell · 516.07 paper_slide · 517.03 paper_slide (+2 st).

### C6S096 · 519.85–525.69 · C6B093 · PAPER
- **Words** "and now they're imagining like, oh, very soon there's gonna be like regular flights to the moon. I'm sure that's what they're imagining at that point."
- **Why** "now they're imagining… regular flights to the moon" → Pan Am's 'First Moon Flights' Club card and a 1960s space-travel poster.
- **FX** #10 Vox layered (card + poster panels) + #13 word by word · **Ref** intro IS002 Vox layered (VARIATION: objects instead of a portrait)
- **Assets** N70 Pan Am 'First Moon Flights Club' membership card (1968–71; © Pan Am, fair use) + N71 1960s space-travel poster (PD/fair use)
- **Text** `regular` @522.89 `flights` @523.13 `to the` @523.53/523.61 `moon` @523.69 (t-serif-i 96 px) · no text on the aside 523.93–525.37
- **Camera** panels drift at two speeds. **Out** W↓ @525.63.
- **SFX** 519.87 paper_slide · 522.87 pop_soft · 525.61 whoosh.

### C6S097 · 525.69–530.65 · C6B094 · NIGHT
- **Words** "So they're like, we gotta be part of this future that you know some of the top people in the world are building."
- **Why** "we gotta be part of this future that… some of the top people in the world are building" → NASA Mission Control, 1969: the people building the future; a celadon dot (Taiwan) joins the network of lines.
- **FX** #16 + §10.6.7 radio rings / network lines + focal call-out · **Ref** —
- **Assets** N72 Mission Control, Houston, Apollo 11 (NASA PD)
- **Text** `part of this future` serif-i @526.89/527.13/527.29/527.45 · `top people` t-label @529.21/529.45 · `building` @530.17
- **Camera** slow push across the consoles. **Out** CA (push continues) @530.59.
- **SFX** 525.71 crt_hum (consoles, dur 4.9) · 526.87 tone_blip.

### C6S098 · 530.65–536.57 · C6B095 · PAPER
- **Words** "So he tells one of his top guys to go figure it out. Now, what this top guy does, he's the secretary general."
- **Why** "he tells one of his top guys to go figure it out… he's the secretary general" → the D15 diagram returns: arrow from Chiang Ching-kuo to the secretary-general silhouette, a task card attached.
- **FX** D15 diagram (motif) + task card · **Ref** D15 (callback of C6S089)
- **Assets** graphic from C6S089
- **Text** `top guys` t-label @531.69 · `figure it out` serif-i @532.57/532.81/532.97 · `SECRETARY GENERAL` label-box @535.45
- **Camera** slow drift right (space for the next node). **Out** continuous → C6S099.
- **SFX** 531.67 marker_long · 535.43 pop_soft.


## 13. Act XIII — Assembling the breakfast (536.57–598.01)
Music: soft pulse builds node by node (539.13 → 568.86 → 590.06); lift + hold on "breakfast" 593.74, carry into c7.

### C6S099 · 536.57–542.01 · C6B096 · PAPER
- **Words** "He first reaches out to one of the top telecommunication guy who's part of the government,"
- **Why** "He first reaches out to one of the top telecommunication guy who's part of the government" → a second arrow from the secretary general to a new node: an unnamed telecom official (silhouette + telephone-exchange icon).
- **FX** D15 diagram + new node pop · **Ref** D15 continued
- **Assets** silhouette node (own); N73 1970s Taiwan telecommunications lab / exchange photo as the node's backing image (Chunghwa Telecom history / CNA)
- **Text** `reaches out` t-label @537.29/537.85 · `TELECOMMUNICATION` label-box @539.13 · `government` @541.29
- **Camera** slow drift. **Out** PT (into the telecom node's image) @541.95.
- **SFX** 537.27 marker_long · 539.11 pop_soft · 541.93 whoosh_soft.

### C6S100 · 542.01–547.13 · C6B097 · NIGHT
- **Words** "and this telecommunication guy is working on transistors, which is kind of a new technology."
- **Why** "this telecommunication guy is working on transistors, which is kind of a new technology" → macro of early transistors.
- **FX** #16 + fast zoom + `FH` + #4 hero title · **Ref** —
- **Assets** N74 macro photo of 1950s–70s transistors (Commons CC BY-SA — credit) ≥ 2400 px
- **Text** `telecommunication` t-label @542.41 · `TRANSISTORS` t-display **hero halate** @544.41 · `new technology` serif-i @546.33/546.57
- **Camera** fast zoom in @543.9, `FH` @544.2, then slow drift. **Out** CA (drift) @547.07.
- **SFX** 543.88 whoosh_soft · 544.39 tone_blip.

### C6S101 · 547.13–554.94 · C6B098 · NIGHT
- **Words** "It's not like brand new, didn't just come out recently, but even in the '70s circuits and transistors are still like You know, new-ish."
- **Why** "even in the '70s circuits and transistors are still… new-ish" → an oscilloscope square wave on a Tektronix screen, beside a 1970s circuit board.
- **FX** #11 screen (oscilloscope) + `data-color-grading` + slide-in board · **Ref** §10.1.7 (oscilloscope)
- **Assets** ✅ `assets/intro/screens/tektronix_475a_scope_frame.png` + ✅ `assets/intro/footage/oscilloscope_fairchild_square_wave.mp4`; N75 1970s circuit board photo (Commons CC)
- **Text** `the '70s` t-label @550.25/550.41 · `circuits` @551.29 · `transistors` @552.01 · `new-ish` serif-i @553.98
- **Camera** slow truck from scope to board. **Out** W→ @554.88.
- **SFX** 547.15 crt_hum (dur 7.7) · 551.27 paper_slide (board) · 554.86 whoosh.

### C6S102 · 554.94–563.10 · C6B099 · PAPER
- **Words** "He reaches out to that guy, the secretary general, and then he reaches out to this random American guy who's just happens to be in the country at that point."
- **Why** "then he reaches out to this random American guy who's just happens to be in the country" → the D15 diagram adds a third node: a silhouette that flies in along a dotted route from the US to Taiwan (mini Pacific map behind).
- **FX** D15 + dotted route draw-on + plane icon (12 fps) · **Ref** D15 + D10 route (motif from the intro's Pacific map)
- **Assets** ✅ `assets/intro/made/pacific_beige.jpg` (mini map) + silhouette node
- **Text** `reaches out` @557.50/557.82 · `American` t-label @558.78 · `in the country` serif-i @561.58/561.74/561.90 (node lands on Taiwan, celadon)
- **Camera** pan with the route. **Out** CA (route still drawing into the node) @563.04.
- **SFX** 557.5 marker_long (route, 1.6 s) · 561.7 pop_soft.

### C6S103 · 563.10–569.58 · C6B100 · NIGHT
- **Words** "And he also works at like cutting edge technology back in the United States. He's a researcher engineer for this company called RCA."
- **Why** "he also works at cutting edge technology back in the United States… a researcher engineer for this company called RCA" → RCA Laboratories (Princeton) in its day; the RCA logo stamps on 'RCA'.
- **FX** #16 plate + #14 light weave + logo stamp · **Ref** —
- **Assets** N76 RCA Laboratories / David Sarnoff Research Center, Princeton, 1960s–70s (Hagley / Commons) ≥ 2000 px; N77 RCA logo (vintage 'RCA' lightning wordmark, SVG)
- **Text** `cutting edge` t-label @564.46 · `United States` @566.06 · `researcher engineer` serif-i @566.94/567.50 · `RCA` logo stamp @568.86
- **Camera** slow push. **Out** W↓ @569.52.
- **SFX** 563.12 air_swell · 568.84 stamp_thud · 569.50 whoosh.

### C6S104 · 569.58–575.26 · C6B101 · NIGHT
- **Words** "Gonna play a very important role that company. And this guy's name is Pan Wen-yuan. He's an RCA man."
- **Why** "this guy's name is Pan Wen-yuan. He's an RCA man" → Pan Wen-yuan's portrait, name super; small RCA badge pinned to the card.
- **FX** #16 + label-box + `CS` · **Ref** —
- **Assets** N78 Pan Wen-yuan portrait (ITRI / zh-Wikipedia / CNA; © fair use) ≥ 1200 px
- **Text** no text on 'Gonna play a very important role that company' · `PAN WEN-YUAN` label-box @572.62 · `RCA man` t-label @574.38 (badge pops)
- **Camera** slow push. **Out** CA (push continues; card slides into the diagram) @575.20.
- **SFX** 572.60 pop_soft · 574.36 pin_pop.

### C6S105 · 575.26–582.14 · C6B102 · PAPER
- **Words** "He comes to these annual conferences on a regular basis every single year. And he he just consults with the government."
- **Why** "He comes to these annual conferences on a regular basis every single year. And he just consults with the government." → a 1970s conference hall photo; a strip of year-tabs ticks one after another (no years printed); a 'consults' arrow to the government node.
- **FX** #12 + tick strip (12 fps) + D15 arrow · **Ref** Pinterest idea: 'calendar-tab repetition strip'
- **Assets** N79 1970s technical seminar in Taipei (CNA / ITRI history) or a generic 1970s conference hall (PD)
- **Text** `annual conferences` t-label @576.06/576.46 · `every single year` serif-i @578.22 (tabs tick) · `consults` @580.54 · `government` @581.66
- **Camera** slow drift. **Out** W↑ @582.08.
- **SFX** 576.0 tick_soft ×5 · 580.52 marker_long · 582.06 whoosh.

### C6S106 · 582.14–590.78 · C6B103 · PAPER
- **Words** "And the reason he consults with the government, by the way, is because he's an old classmate of this uh secretary general guy that we talked about. His name is Fei."
- **Why** "because he's an old classmate of this secretary general guy… His name is Fei." → Pan's card and the secretary-general silhouette sit side by side, a 'classmates' bracket joins them; the silhouette burns into Fei Hua's real face on 'Fei'.
- **FX** D15 + pen bracket + portrait burn reveal (#3 burn on a portrait, as the intro's Chang reveal) · **Ref** D15 + intro IS043 burn reveal (VARIATION: paper ground, celadon ring)
- **Assets** N78 card (motif) + N80 Fei Hua portrait (ROC gov / Commons) ≥ 1200 px; silhouette matte cut from it
- **Text** `old classmate` serif-i @585.10/585.50 · `secretary general` t-label @587.90 · `FEI HUA` label-box @590.06 (burn starts 589.8, done 590.6)
- **Camera** push to the silhouette. **Out** CA (burn finishing, push continues) @590.72.
- **SFX** 585.08 marker_long · 589.8 burn_crackle (0.9 s) · 590.04 pop_soft.

### C6S107 · 590.78–598.01 · C6B104 · NIGHT
- **Words** "So he reaches out to all of them. He's like, hey guys, let's meet for breakfast tomorrow, and then let's figure out what Taiwan needs to succeed."
- **Why** "he reaches out to all of them… let's meet for breakfast tomorrow, and then let's figure out what Taiwan needs to succeed" → a handwritten note on a lamp-lit table: 'breakfast tomorrow'; the three node cards slide in around a soy-milk bowl — the hand-off to c7's breakfast.
- **FX** D08 note (VARIATION: handwritten-style card in Crimson Pro italic, pen) + #12 cards slide + lamp pool + #4 hero · **Ref** D08 + R9 lamp pool
- **Assets** N81 Taiwanese soy-milk breakfast table, top-down (soy milk bowl, youtiao) — CC/PD or © fair use; cards N33/N78/N80 (motif)
- **Text** `all of them` t-label @591.74 (cards slide in) · `BREAKFAST` t-display **hero halate** @593.74 · `tomorrow` serif-i @594.22 · `what Taiwan needs` @595.90/596.14/596.70 · `to succeed` @596.94/597.10 (hold ≥ 0.5 s to 598.01)
- **Camera** slow crane down to the table. **Out** → c7 (hand-off: hold the table; c7 opens on 'We get to breakfast the next day').
- **SFX** 590.80 paper_slide ×3 · 593.72 chime_soft · 597.1 air_swell (carry into c7).

## 14. New reference variations (V1–V6) — my own reference search, rebuilt in our style (MANUAL §6.1)

No Pinterest pack for this chunk (LONGFORM): these six layouts were picked to fit c6's material, each described by structure
so an editor can build it from our parts. They sit next to D01–D15 / R1–R12 as tasteful variations, never copies.

| id | idea (where it comes from) | structure → our build | used in |
|---|---|---|---|
| V1 | **Assembly seating chart** — vintage theatre/parliament seating plans (Pinterest "seating plan typography") | a plan of rows of small name cards (Cooper Hewitt t-label), one seat celadon; cards flip at 12 fps to "look at" a seat; pen arrows converge (§10.6.2) | C6S011 |
| V2 | **Domino row** — the Vox "domino theory" animation idiom; tabletop domino-chain macro photography | CSS-3D row of dominoes on a dark lamp-lit table, faces = desaturated flags, first one celadon; topple at 12 fps; camera dollies with the fall (cut on action) | C6S028 |
| V3 | **Personnel dossier** — Vox/Johnny Harris "file card" look; manila folder with paper-clipped photo and typed fields | folder + clip + typed fields (`FX.text` typewriter, letters at 12 fps), pen strike-throughs for "became", lamp pool; a recurring motif for each named cabinet member | C6S035, C6S065, C6S067 |
| V4 | **Split-screen contrast** — editorial "then vs now / him vs him" spreads with a hand-drawn divider | two halves, rough ink divider drawn on (markup underline), one half pushes in to become the next shot; can also "cut" a card (Bush's legs) | C6S025, C6S045 |
| V5 | **Calligraphy scroll unroll** — Chinese hanging-scroll reveals (Pinterest "scroll reveal animation") | a real slogan photo/scan inside a scroll that unrolls (scaleY with a rod shadow, 12 fps), English words typeset beside, each pen-underlined on its word (§10.7 rhythm) | C6S041 |
| V6 | **Dusk propaganda billboard** — photographs of political billboards with type set into the sky | two-layer parallax (billboard / sky), slow tilt up, the corrected phrase rises word by word into the sky area | C6S056 |

## 15. Coverage tables

### 15.1 Effects (MANUAL §5 + §10)
| effect | scenes |
|---|---|
| #1 B-roll / archival plates & footage | C6S001, C6S006, C6S009, C6S012, C6S013, C6S023, C6S036, C6S042, C6S046, C6S052, C6S059, C6S082 |
| #2 charts | C6S005, C6S007, C6S008, C6S027, C6S030, C6S047, C6S064, C6S071, C6S077, C6S078, C6S079, C6S084, C6S085, C6S095 |
| #3 maps | C6S017, C6S029, C6S040, C6S049, C6S053, C6S062, C6S066, C6S070, C6S075, C6S076, C6S083, C6S106 |
| #4 film-title hero (halate) | C6S010, C6S012, C6S028, C6S044, C6S046, C6S061, C6S076, C6S081, C6S094, C6S100, C6S107 |
| #5 newspaper / document treatment | C6S003, C6S016, C6S020, C6S050 |
| #8 light streaks | C6S034, C6S038, C6S081 |
| #10 Vox layered | C6S002, C6S033, C6S059, C6S096 |
| #11 footage in a TV / screen | C6S032, C6S094, C6S101 |
| #12 collage / cards / timeline | C6S011, C6S014, C6S019, C6S039, C6S043, C6S054, C6S057, C6S063, C6S068, C6S074, C6S088, C6S093, C6S105, C6S107 |
| #13 text animations | C6S005, C6S021, C6S035, C6S044, C6S051, C6S056, C6S060, C6S065, C6S081, C6S090, C6S091, C6S092, C6S096 |
| #14 gate weave | C6S006, C6S013, C6S018, C6S036, C6S042, C6S046, C6S052, C6S082, C6S103 |
| #15 curve cut | C6S055 |
| #16 hi-quality plate | C6S001, C6S006, C6S010, C6S015, C6S018, C6S022, C6S025, C6S026, C6S031, C6S034, C6S037, C6S038, C6S042, C6S044, C6S052, C6S061, C6S072, C6S073, C6S082, C6S086, C6S097, C6S100, C6S103, C6S104 |
| #17 2.5D | C6S012, C6S056, C6S095 |
| #18 rough + highlighter | C6S004, C6S019, C6S024, C6S045, C6S049, C6S050, C6S051, C6S058, C6S069 |
| #19 markups (pen) | C6S002, C6S004, C6S009, C6S011, C6S015, C6S022, C6S025, C6S026, C6S036, C6S045, C6S049, C6S054, C6S060, C6S064, C6S067, C6S072, C6S092 |
| #20 map call-outs | C6S017, C6S029, C6S070, C6S075 |
| §10.6.2 pen markups / underlines | C6S002, C6S004, C6S011, C6S015, C6S022, C6S024, C6S025, C6S026, C6S036, C6S041, C6S053, C6S054, C6S055, C6S058, C6S060, C6S064, C6S065, C6S067, C6S072, C6S080, C6S091, C6S092, C6S106, C6S107 |
| §10.6.3 contrast call-out | C6S004, C6S010, C6S015, C6S017 |
| §10.6.4 text contrast call-out | C6S004 |
| §10.6.5 focal call-out | C6S022, C6S031, C6S040, C6S097 |
| §10.6.6 highlighter (body text) | C6S004, C6S008, C6S050, C6S069 |
| §10.6.7 radio-wave rings | C6S040, C6S097 |
| §10.7 painting-to-print / per-word underline | C6S016, C6S023, C6S024, C6S041 |
| burn reveal | C6S029, C6S076, C6S106 |
| focus hunt `FH` | C6S001, C6S006, C6S012, C6S026, C6S039, C6S049, C6S055, C6S069, C6S073, C6S086, C6S100 |
| chokeSettle `CS` | C6S002, C6S034, C6S041, C6S048, C6S104 |
| odometer / count / typewriter | C6S005, C6S017, C6S020, C6S021, C6S035, C6S044, C6S051, C6S059, C6S065, C6S067, C6S081, C6S090, C6S091, C6S102 |
| #6 sound | SFX lines per scene + music notes per act |
| #7 textures | every scene (grain + dust + vignette; paper scenes two paper layers) |
| #9 iris | **retired** (§10.1.6) — whips instead |

### 15.2 Reference layouts
| ref | scenes |
|---|---|
| D01 | C6S005, C6S051 |
| D02 | C6S030 |
| D03 | C6S047, C6S064 |
| D04 | C6S077 |
| D05 | C6S019, C6S079 |
| D06 | C6S007, C6S008, C6S027, C6S071 |
| D07 | C6S014, C6S039, C6S043, C6S074, C6S093 |
| D08 | C6S021, C6S090, C6S091, C6S107 |
| D09 | C6S053, C6S057 |
| D10 | C6S049, C6S102 |
| D11 | C6S084, C6S085 |
| D12 | C6S087 |
| D13 | C6S029, C6S078 |
| D14 | C6S017, C6S083 |
| D15 | C6S054, C6S063, C6S089, C6S098, C6S099, C6S102, C6S105, C6S106 |
| R1 | C6S051 |
| R4 | C6S030 |
| R5 | C6S047, C6S064 |
| R6 | C6S077 |
| R7 | C6S019, C6S079 |
| R8 | C6S007, C6S071 |
| R9 | C6S003, C6S068, C6S069, C6S107 |
| R10 | C6S049 |
| R11 | C6S029, C6S066, C6S070 |
| R12 | C6S040, C6S062, C6S075, C6S076 |
| V1 | C6S011 |
| V2 | C6S028 |
| V3 | C6S035, C6S065, C6S067 |
| V4 | C6S025, C6S045 |
| V5 | C6S041 |
| V6 | C6S056 |
| R2 (optional) / R3 (skip) | not used |
| expected/layouts 2.5D / markup-map | C6S012, C6S095 / C6S015, C6S022 |

### 15.3 2.5D, curve cut, TVs/screens, painting-to-print (the "big" moments)
| moment | scene | why there |
|---|---|---|
| 2.5D #1 — ROC delegation walks to the front | C6S012 | the emotional centre of the UN story deserves depth |
| 2.5D #2 — Aldrin on the Moon | C6S095 | "can't even imagine" — the wonder beat of the chunk |
| 2.5D-lite parallax — Deng billboard | C6S056 | two layers only (billboard + sky) |
| curve cut (#15) young Deng → old Deng | C6S055 | "the same person" — a literal match of one face across 50 years |
| TV: 1970s Taiwanese set (Tatung/Sampo) | C6S032 | "Back in Taiwan, everyone's seeing this" |
| TV: 1960s RCA Victor console | C6S094 | the Moon landing as people saw it; quietly sets up RCA (named 568.86) |
| screen: Tektronix oscilloscope | C6S101 | "circuits and transistors… new-ish" |
| painting-to-print (§10.7) | C6S023–C6S024 | the narrator quotes Bush |
| calligraphy scroll + per-word underline (§10.7 variant) | C6S041 | the narrator quotes Chiang Kai-shek's statement |
| burn reveals | C6S029 (world map), C6S076 (claim map), C6S106 (Fei Hua portrait) | recognition switching; "not China anymore"; the name reveal |

### 15.4 Ground rhythm (N night · P paper · G grid)
```
001N 002P 003N 004P 005G 006N 007P 008P 009N 010N 011P 012N 013N 014P 015N 016P 017N 018N 019G 020N 021P 022N 023P 024P 025N 026N 027P 028N 029N 030P 031N 032N 033P 034N 035P 036N 037N 038N 039P 040N 041P 042N 043P 044N 045P 046N 047P 048N 049P 050N 051G 052N 053P 054P 055N 056N 057P 058G 059N 060P 061N 062N 063P 064P 065N 066P 067N 068N 069N 070P 071G 072N 073N 074P 075N 076N 077P 078N 079P 080P 081N 082N 083N 084P 085P 086N 087N 088P 089P 090N 091N 092P 093P 094N 095N 096P 097N 098P 099P 100N 101N 102P 103N 104N 105P 106P 107N
```
Longest same-ground run: 3 (N 036–038, N 067–069, N 081–083); PAPER+GRID combined never more than 3 (max 2). ✔ (script-checked)

### 15.5 Transitions in order (never the same twice in a row; `cont.` = same set, no cut)
W→, PT, CA, W↓, CA, FW, cont., W↑, CA, W←, PT, CA, W→, CA, PS, W↓, CA, W←, CA, PS, W↑, FW, cont., W→, CA, W↓, PT, CA, W→, PT, CRT, PT, W←, CA, W↓, CA, FW, CA, W→, CA, W↑, CA, W←, FW, CA, W→, CA, W↓, CA, PS, CA, W←, PS, CA, W→, CA, W↓, PT, W↑, CA, W←, PS, cont., PT, W↓, CA, W→, cont., FW, CA, W↑, CA, PT, W←, cont., W↓, CA, W→, cont., FW, CA, W↓, PS, cont., W→, CA, PS, cont., W↑, cont., W←, CA, W→, PT, CA, W↓, CA, cont., PT, CA, W→, CA, W↓, CA, W↑, CA, → c7
✔ no type repeats back-to-back (script-checked). No iris anywhere.

### 15.6 "Finish + hold 0.5 s" check (§10.9) — scenes where the key animation ends close to the cut
| scene | key animation | must be done by | cut |
|---|---|---|---|
| C6S005 | bars + 2/3 count | 24.6 | 25.2 (punch-in is camera) |
| C6S010 | CHINA contrast call-out + label words | 44.85 | 45.39 |
| C6S028 | domino topple (cut is ON the fall = camera follows; the title hold 136.71→137.2) | 137.19 | 137.69 |
| C6S044 | odometer lock | 217.9 | 218.62 |
| C6S051 | 12-year count + stamp | 249.6 / 248.5 | 254.39 |
| C6S077 | elite bar growth | 406.2 | 406.71 |
| C6S083 | six project pins + yellow route | 445.9 | 446.56 |
| C6S087 | tick column | 472.3 | 473.68 |
| C6S091 | double underline | 495.0 | 495.55 — **tight**: draw the underline from 494.6 to 495.0 |
| C6S106 | Fei Hua burn | 590.6 (label 590.0) | 590.72 — **tight**: start the burn at 589.7 so it is done by 590.2 |
| C6S107 | last word "succeed" | 597.4 | chunk end 598.01 (hold; c7 continues the table) |
Editors check the last second of every scene in snapshots.

### 15.7 Palette check
Celadon = Taiwan / ROC only (C6S004, 010, 011, 019, 022, 027, 028, 032, 040, 047, 061, 062, 065, 070, 071, 074, 075–076, 077,
082, 097, 102). PRC/CCP = ink label-boxes (C6S008, 010, 029, 054). Yellow key numbers: `2/3` (C6S005), `12 YEARS` (C6S051),
`0%` (C6S084); yellow marker routes C6S049, C6S083; highlighter C6S004, C6S050. **No red, no blue** in c6.

### 15.8 Cohesion with the intro
Same motifs, new content: label-boxes + Cooper Hewitt labels + Crimson Pro italic captions; lamp-lit desk documents (intro
IS009 → C6S003, S065, S067, S090–091, S107); D15 diagram (intro IS024/027 → C6S089, 098–099, 102, 105–106 — this time grey
nodes then celadon); the grey-silhouette-then-reveal device (intro Morris Chang → C6S089→C6S106 Fei Hua); tilted vintage maps
(D10); celadon Taiwan relief (R12); grid-paper charts; Vox layered panels (IS002 → C6S002, 033, 059, 096).

## 16. Open questions (defaults in DECISIONS.md)
1. PRC colour — ink (default) vs vermilion red? → **ink** (red is TSMC's for the whole video).
2. Hemicycle dot counts in C6S007/008/027 — real 1971 proportions (≈ 55/59/15) without printed numbers? → **yes, shapes only**.
3. "Fei" — super `FEI HUA` (full, accurate) while the narrator says "Fei"? → **yes** (like "Hsinchu Science Park").
4. Bush / minister / Tanzania lines are the narrator's paraphrases → **attributed "(paraphrased)", no quotation marks**.
5. Unnamed telecom official → **silhouette + telecom-lab image, never named or captioned**.
6. Chiang Kai-shek's slogan in Chinese characters → **only as a real image** (our fonts have no CJK); English = his words.
7. "10 Major Projects" vs official "Ten Major Construction Projects" → **his words on screen**; official name only inside the
   real poster/stamp art.
8. Dancing photo used twice (C6S018, C6S022) + a thumbnail (C6S019); Bush head-in-hands photo printed again in C6S016 — allowed
   by §10.9 (story needs it).
