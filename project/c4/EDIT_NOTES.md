# EDIT NOTES — CHUNK c4 "Taiwan: the chip rivalry" (Searching Lessons), VO local 0.00–601.44 (full audio 2077.72–2679.14)

Shot-by-shot plan for chunk c4. Read with `project/LONGFORM.md` (the long-form brief), `MANUAL.md` (**§10.1–10.9 override**
older sections; §5 effects; §6/§6.1 reference layouts; §10.6 call-outs; §10.7 painting-to-print), `project/intro/BRIEF.md`,
`project/c4/analysis/BEATS.md` (beats, ASR fixes, cues), `ASSETS_NEEDED.md` (IDs `E..` = exists, `N..` = needed),
`SEGMENTS.md` (who builds what) and `DECISIONS.md`. Prepared 2026-10-31 by the c4 director / edit planner.
Quality bar = the approved intro (`review/intro_720p.mp4`): same grounds, grain/dust stack, halation discipline, 12 fps
Vox easing, whips, call-outs. **This chunk must look like the intro continued.**

## 0. How to read this file

- **Times** = LOCAL VO seconds (`vo_c4.mp3` / `transcript_c4.json`; + 2077.72 = full audio). **104 scenes, C4S001–C4S104**,
  one per beat (C4S0NN covers C4B0NN), contiguous 0.00 → 601.44, no gaps. Scene boundaries are word starts.
- **Text cue `@t`** = start of the spoken word; first frame at `T(t) − 0.06`. Multi-word lines are revealed **word by word**
  (each word its own literal `T()`), MANUAL §4.4. Every `@t` in this file was checked by script: it is a real word start
  inside its scene.
- **Words** = exact narration under the shot (ASR names fixed). **Why** = why the picture matches those words (§10.1.3).
- **Ground**: `NIGHT` (dark/cinematic/archival/dark maps), `PAPER` (Texturelabs `_hires` paper, two layers, top ~90 %),
  `GRID` (real K+E 1960 grid / ruled scans or Texturelabs graph/lined `_hires`). Rhythm: ≤ 3 in a row on one ground, and
  PAPER+GRID combined ≤ 3 in a row (checked by script, §11.4).
- **FX** = MANUAL §5 numbers + §10 craft: `W` whip (`FX.whip`, direction given), `FW` light-flash whip, `CA` cut on action,
  `HC` hard cut on action (two moving shots), `PT` push-through, `PS` paper slide / torn-paper wipe, `cont.` = same layout
  continues (no transition), `FH` focus hunt (once per scene max, after a fast zoom/push), `CS` `FX.chokeSettle`.
  **No iris anywhere.** Never the same transition twice in a row (checked, §11.5).
- **Hold rule (§10.9)**: every scene's KEY animation (route, bars, count, stamp, cross) is **finished by scene end − 0.5 s**
  and holds; the cut rides the camera or a secondary motion. Each scene line "Lock" gives that time. A word spoken inside
  the last 0.5 s (e.g. `members` @13.04) gets a short ≤ 0.25 s entrance so it is still complete before the lock.
- **Glow**: `.halate` only on the scene's **hero** (marked **hero halate**); everything else `.clean`; paper never glows.
- **Ref** = intro pack `D01–D15` (`references/style-images/intro/`), original refs `R1–R12` (`references/style-images/1–12`,
  stills in `expected/layouts/`), the 2.5D stills, or a **named new reference idea** (described in the scene; collected in §11.2).
- **Palette for c4** (see BEATS §6): **celadon = Taiwan / ROC** (fills, rules, tabs — never text colour) · **red = CCP / PRC**
  (this chunk only — TSMC/Chang are absent; per-act mapping as c1 did for the West) · **US, Japan, UN, USSR, Mao/Chiang as
  persons = neutral** ink/bone/sepia · **yellow** = highlighter + the one key number (11, 1.5 billion, 40 years) ·
  **navy/blue not used** (it is UMC/Tsao's). Max two accents per frame (celadon + red).
- **Spellings**: Mao Zedong (ASR "Ma Zhadong"), Chiang Kai-shek, NTU / National Taiwan University, Security Council, General
  Assembly, Warsaw Pact, Meiji, CCP, ROC, brain drain (ASR "dang"), Chinese seat (ASR "seed"). No text on slips (BEATS §2b).
- **No face cam** in c4. **Copyrighted material allowed** (fair use, credited, §10.9): real UN photos, press photos, newspaper
  clippings, magazine covers. Credits: 13 px micro-credit bottom-right while on screen where customary.
- **Maps** from `assets/maps/kit/` (high-quality map kit — currently EMPTY: see ASSETS_NEEDED §4; until it lands use
  `assets/intro/maps/*` at native size only) — never flat grey/beige relief at full frame without the kit's shading.
- **SFX** lines are object events (local VO s) → `compositions/c4sNN.sfx.json` (vocabulary SEGMENTS §3.4). Restraint pass
  (§10.8) applies: the hero event per scene first.

## 1. Act A — How the UN works (0.00–37.87)
Music: light pulse + pizz-like texture; ticks on numbers; small lift on THE CHINESE SEAT 35.79.

### C4S001 · 0.00–8.00 · C4B001 · NIGHT
- **Words** "All of them have a veto. But that veto only works on resolutions that are in the jurisdiction of the Security Council."  **Why** the line is about the veto and where it applies — the real Security Council chamber, its table fenced off as 'the jurisdiction'.
- **FX** #16 plate + #4 hero + #19 markup box + §10.6.3 contrast call-out · **Ref** Pinterest idea: "Vox UN explainer — archival chamber photo with a hand-drawn boundary"
- **Visual** Real 1950s–60s Security Council chamber (horseshoe table, mural). Grade sepia-cool, chromaticAberration 0.12. On "veto" the frame punches in 8 % and the veil drops (contrast call-out) leaving only the horseshoe table lit. On "jurisdiction of the security council" a pen box (`FX.markup.box`, boil 4) draws around the table.
- **Text** `VETO` t-display 220 px **hero halate** @1.20 (chokeSettle) · `Security Council` t-label @6.88 (`security` word starts the label; `council` already in the label) on the pen box
- **Assets** N01 Security Council chamber photo
- **Camera** slow push 1.00→1.06; punch-in 8 % at 1.14 (cut-on-curve for the veil). **Lock** key animation done by 7.50. **Out** CA — camera keeps pushing into the table top; next scene opens on the same table as a top-down diagram
- **SFX** 1.10 circuit_clunk (veil) · 6.80 marker_scratch (box) · 7.80 whoosh_soft

### C4S002 · 8.00–13.71 · C4B002 · PAPER
- **Words** "There are five permanent member in the Security Council and six rotating members. So in total 11 members."  **Why** five permanent + six rotating = eleven: count the seats.
- **FX** #2 chart + #13 count · seat diagram · **Ref** R8 / D06 VARIATION — a horseshoe of 11 seat-dots (top-down Security Council table) instead of a hemicycle
- **Visual** Top-down horseshoe table drawn in ink on paper_cream (two paper layers, top 90 %). 5 large seat-discs fill ink @8.32 one per 1/12 s step; 6 outlined discs pop on the outer arc @10.80; a counter in the centre counts to 11 @12.72.
- **Text** `5 PERMANENT` t-label @8.32 · `6 rotating` t-serif-i @10.80 · `11` **yellow key number** t-display @12.72 (count 0→11, 12 fps) + `members` t-label @13.04
- **Assets** own SVG (seat diagram)
- **Camera** static, 2 % drift. **Lock** key animation done by 13.21. **Out** cont. — same diagram stays for C4S003
- **SFX** 8.30 pop_soft ×5 (dot_ticks 0.4 s) · 10.78 dot_ticks · 12.70 counter_ticks

### C4S003 · 13.71–21.31 · C4B003 · PAPER
- **Words** "Everyone gets one vote. But if there's a veto from a permanent member, that means doesn't matter if it's like 10 people on the side, it's not gonna pass."  **Why** one vote each, then one permanent veto blocks ten — the votes and the veto act out on the same seats.
- **FX** #2 + #19 cross + #18 highlighter · **Ref** R8 variation (continued)
- **Visual** Each seat gets an ink tick @14.35 ("one vote"); 10 seats tick 'yes' in a 12 fps wave @19.23; one permanent seat turns over a rubber-stamp card `VETO` (ink stamp + yellow highlighter swipe under it) @16.11; the resolution card in the middle gets an ink cross @20.59.
- **Text** `one vote` t-serif-i @14.35 · `VETO` stamp @16.11 · `10` t-display @19.23 · `not gonna pass` t-label @20.59 (cross drawn with it)
- **Assets** own SVG; stamp texture
- **Camera** slow pull-out 1.05→1.0. **Lock** key animation done by 20.81. **Out** PS — paper slides away left, revealing night
- **SFX** 14.33 tick_soft · 16.09 stamp_thud · 19.21 dot_ticks · 20.57 pencil_scribble · 21.20 paper_slide

### C4S004 · 21.31–25.79 · C4B004 · NIGHT
- **Words** "That's not how things are in the General Assembly, which has a lot more jurisdiction."  **Why** "General Assembly" — the UN emblem (round) match-zooms into the round emblem above the GA rostrum.
- **FX** #15 cutting-the-curve match cut + `FH` + #4 · **Ref** — (intro IS005 technique)
- **Visual** Start on the UN emblem (round world + laurels) on paper-tinted night; expo.inOut zoom (12 fps) with cut at peak velocity @22.40 into the real GA hall photo whose round emblem sits in the same place; focus hunt as it lands (@23.1).
- **Text** `GENERAL` @22.91 + `ASSEMBLY` @23.39 **hero halate** · `a lot more jurisdiction` t-serif-i word-by-word: `lot` @24.27, `more` @24.51, `jurisdiction` @24.67
- **Assets** N03 UN emblem SVG · N02 GA hall photo (wide, emblem visible)
- **Camera** curve-cut zoom; then slow pull-out to show the hall's scale. **Lock** key animation done by 25.29. **Out** CA — the pull-out continues into the 2.5D dolly
- **SFX** 22.38 whoosh_big · 23.00 air_swell

### C4S005 · 25.79–32.11 · C4B005 · NIGHT
- **Words** "And importantly here, General Assembly has a jurisdiction over who should get what seat."  **Why** the GA decides 'who gets what seat' — the hall in depth, then one delegate desk isolated.
- **FX** #17 2.5D no.1 (GA hall) + §10.6.3 contrast call-out · **Ref** 2.5D-quad VARIATION (hall rows instead of an arch)
- **Visual** GA hall cut into 4 layers (rostrum + emblem backdrop, far rows, mid rows, foreground desks with nameplates, haze between). Dolly z −80→150, x drift. On "who should get what seat" the veil drops (hard cut at the dolly's peak) leaving one desk + empty chair lit.
- **Text** `jurisdiction` t-label @28.59 · word-by-word `who` @30.11 `should` @30.51 `get` @30.75 `what` @31.07 `seat` @31.39 (t-serif-i, `seat` in yellow highlighter)
- **Assets** N02 GA hall photo ≥ 3000 px (layers)
- **Camera** 2.5D dolly (cam ease); `FH` focus hunt when the move lands. **Lock** key animation done by 31.61. **Out** W→ whip right
- **SFX** 25.80 air_swell · 30.09 circuit_clunk · 31.90 whoosh

### C4S006 · 32.11–37.87 · C4B006 · NIGHT
- **Words** "Meaning a vote in the General Assembly decides who the Chinese seat belongs to."  **Why** "the Chinese seat" — the real 'CHINA' nameplate on the ROC delegation's desk.
- **FX** #16 plate + §10.6.5 focal blur · **Ref** —
- **Visual** Real UN photo of the ROC delegation desk with the CHINA nameplate (1950s–60s). Focal blur: sharp circle on the nameplate, rest softly blurred; the sharp spot drifts from the vote button/hand ("vote") to the nameplate.
- **Text** `vote` t-label @32.99 · `THE` @35.55 `CHINESE` @35.79 `SEAT` @36.27 t-display 140 px (**hero halate**)
- **Assets** N04 'CHINA' nameplate photo
- **Camera** slow push 1.0→1.08. **Lock** key animation done by 37.37. **Out** FW light-flash whip left
- **SFX** 32.97 tick_soft · 35.77 boom_low (very soft) · 37.80 whoosh

## 2. Act B — The yearly vote & the Africa vote war (37.87–120.00)
Music: ostinato builds 59–113; thin to a held chord on 'The US is with Taiwan' 115.76.

### C4S007 · 37.87–43.15 · C4B007 · PAPER
- **Words** "Now, ever since the CCP started claiming that they're to China, every single year,"  **Why** the CCP claims China, every year — the 1949 proclamation photo, then calendar pages flip.
- **FX** #10 Vox layered + #13 text fill · **Ref** s09 layered VARIATION
- **Visual** Real photo of Mao proclaiming the PRC (1949, Tiananmen) as the subject panel, tinted red→paper duotone; behind it two offset panels (Tiananmen gate, crowd) drift at their own speeds. @42.35 a stack of blank tear-off calendar pages flips at 12 fps in the corner (no years printed).
- **Text** `CCP` `.label-box` red @39.55 · `China` t-serif-i @41.71 · `every single year` t-label @42.35
- **Assets** N08 PRC proclamation 1949 photo (+ crowd/gate crops) · calendar pad (own SVG)
- **Camera** drift right 30 px. **Lock** key animation done by 42.65. **Out** CA — calendar flip continues as the map comes in
- **SFX** 39.53 paper_slide · 42.33 paper_flip ×4 · 43.10 whoosh_soft

### C4S008 · 43.15–48.59 · C4B008 · NIGHT
- **Words** "one of the countries, especially from the Warsaw Pact that is like close to China or the close to CCP would"  **Why** "Warsaw Pact … close to the CCP" — the Pact countries light up on the map and link to China.
- **FX** #3 map + #20 map callout + #19 arrow · **Ref** R12 VARIATION (relief map, several countries filled, glowing edge)
- **Visual** Map kit Eurasia dark relief; the 8 Warsaw Pact countries fill neutral bone-grey halftone with 6 px glow @44.59; camera pans east; a pen arrow draws from the bloc to China, which fills red @47.79.
- **Text** `WARSAW PACT` t-label 34 px @44.59 (leader line) · `CCP` `.label-box` red @47.79
- **Assets** N36 map kit Eurasia relief + country masks
- **Camera** pan east (cam ease) then settle; `FH` after the pan. **Lock** key animation done by 48.09. **Out** W↓ vertical whip down onto the desk
- **SFX** 44.57 map_pin · 47.10 marker_long · 47.77 pop_soft

### C4S009 · 48.59–54.67 · C4B009 · PAPER
- **Words** "bring up a resolution basically saying, Hey, let's kick out this government that's sitting in sitting in Taiwan"  **Why** the yearly resolution to kick out Taiwan's government — the real UN draft document, its 'expel' line called out.
- **FX** #5 document on a tilted 3D page + §10.6.4 text contrast call-out + two paper layers · **Ref** Pinterest idea: "archival UN document with a typewriter-paper stack"
- **Visual** Real UN draft resolution page (UN Digital Library scan) on two paper layers, tilted, sepia + halftone growing with the push. @50.91 the paragraph fades to 20 % and only the line about expelling the representatives in Taiwan returns through a feathered wipe; pen underline under it.
- **Text** `RESOLUTION` t-label @49.07 · `kick out` t-serif-i @50.91 · `Taiwan` `.label-box` (celadon rule) @54.11
- **Assets** N07 UN draft resolution scan
- **Camera** push 1.0→1.15 to the paragraph. **Lock** key animation done by 54.17. **Out** CA — page keeps sliding up as the diagram drops in
- **SFX** 48.60 paper_rustle · 50.89 marker_scratch · 54.09 pop_soft

### C4S010 · 54.67–59.07 · C4B010 · PAPER
- **Words** "and let's give the CCP the Chinese seat, including the permanent veto."  **Why** the seat (with its veto) moves from the ROC to the CCP — a relationship diagram.
- **FX** #2 + #19 arrows (D15) · **Ref** D15 VARIATION — two circles + an object (the seat) moving between them
- **Visual** Left circle: Taiwan relief (celadon), right circle: CCP (red, Tiananmen crop). A chair icon with the 'CHINA' nameplate sits under the left circle; on "give the CCP the Chinese seat" a pen arrow draws and the chair slides right at 12 fps; a small key tag 'veto' hangs on the chair.
- **Text** `CCP` @55.39 (red ring label) · `CHINESE` @56.19 `SEAT` @56.59 t-display · `permanent veto` t-label @57.87
- **Assets** own SVG chair; E10 Taiwan relief; N08 crop
- **Camera** static, 2 % push. **Lock** key animation done by 58.57. **Out** W← whip left
- **SFX** 55.37 pop_soft · 56.17 marker_long · 56.80 dot_slide

### C4S011 · 59.07–65.39 · C4B011 · NIGHT
- **Words** "Now, every year this resolution is very healthy defeated, but this has kind of become like a habit."  **Why** every year it's defeated — real headlines of the yearly UN votes drop onto a lamp-lit desk.
- **FX** #5 newspapers (stack montage) + stamp · **Ref** Pinterest idea: "newspaper stack on a dark desk, one per year" (s06 page treatment)
- **Visual** 4 real front pages/clippings ('U.N. again bars Red China' type headlines, 1950s–60s) drop one on another at 12 fps under a desk lamp (R9 lamp pool); each gets an ink `DEFEATED` stamp; camera rises slowly.
- **Text** `every year` t-label @59.31 · `DEFEATED` stamp @62.59 · `habit` t-serif-i @64.99
- **Assets** N06 newspaper clippings ×4
- **Camera** rise + slight rotate. **Lock** key animation done by 64.89. **Out** CA — the last page slides out as the graph paper slides in
- **SFX** 59.30 paper_slide · 60.50 paper_slide · 62.57 stamp_thud · 64.97 paper_slide

### C4S012 · 65.39–70.72 · C4B012 · GRID
- **Words** "They bring it up, it gets defeated, but every year they're noticing. How the votes are falling down."  **Why** "votes are falling down" — a line that steps down year after year.
- **FX** #2 line chart (D05) + stamps · **Ref** D05 VARIATION (era band → shaded 'yearly' columns; shapes only, no values/years)
- **Visual** On a K+E grid scan: a line draws year by year, each point a small 'defeated' tick @66.75, the margin above the line shading shrinks; the line visibly drops @70.00; hold.
- **Text** `defeated` t-label @66.75 · `VOTES` @69.44 · `FALLING` @70.00 `DOWN` @70.32 t-display
- **Assets** E16 grid paper (ke1960_10x10_grid_black_hires) 
- **Camera** slow drift right with the line. **Lock** key animation done by 70.22. **Out** W↑ whip up
- **SFX** 66.73 tick_soft · 67.6–70.2 tick_soft (stopwatch, 0.5 s) · 70.70 whoosh

### C4S013 · 70.72–74.08 · C4B013 · NIGHT
- **Words** "And as new countries are being born in Africa, that"  **Why** new countries being born in Africa — African countries appear one by one with a burn reveal.
- **FX** #3 map + burn reveal · **Ref** R11 VARIATION on night (dark relief, regions popping)
- **Visual** Map kit Africa dark relief; countries burn-reveal in sequence (bone fill + rim) — shapes only, no years.
- **Text** `NEW` @71.12 `COUNTRIES` @71.44 t-label · `AFRICA` t-display **hero halate** @73.28
- **Assets** N36 map kit Africa relief + admin-0 masks
- **Camera** slow push 1.0→1.08. **Lock** key animation done by 73.58. **Out** cont. — the camera pushes into one country
- **SFX** 71.10 burn_crackle (1.8 s) · 73.26 air_swell

### C4S014 · 74.08–82.56 · C4B014 · NIGHT
- **Words** "means there's a new country that now Taiwan and the CCP have to fight over, at least diplomatically speaking, to make sure they fall in your camp."  **Why** each new country is fought over by Taiwan and the CCP — a tug of war for one country.
- **FX** #3 + #20 + #19 arrows · **Ref** Pinterest idea: "tug-of-war infographic" (two ropes from two flags to one country)
- **Visual** One new African country isolated (contrast call-out). A celadon line (rope) runs left to a small Taiwan relief, a red line right to China; both tighten alternately at 12 fps.
- **Text** `Taiwan` t-label @76.24 · `CCP` red label @77.20 · `FIGHT OVER` t-display @78.00 · `your camp` t-serif-i @81.76
- **Assets** N36 Africa map; E10 Taiwan relief
- **Camera** camera pulls back to show both sides. **Lock** key animation done by 82.06. **Out** PS — paper slides in from right
- **SFX** 74.10 circuit_clunk · 77.98 gate_creak (rope) · 81.70 whoosh_soft

### C4S015 · 82.56–88.64 · C4B015 · PAPER
- **Words** "Now, Taiwan does this, they send in aid, they send in diplomat missions, you know, they send in whatever they can"  **Why** Taiwan sends aid and diplomatic missions — a telegram plus a real photo of an ROC mission in Africa.
- **FX** #13 typewriter text + D08 telegram · **Ref** D08 VARIATION (diplomatic cable on Western-Union-style form; typeset recreation, no fake seals)
- **Visual** Cable form (two paper layers) typed on word: lines appear as he says them; a real photo of an ROC agricultural/diplomatic mission in Africa is paper-clipped to the corner @86.00.
- **Text** typed `AID` @84.88 · `DIPLOMAT MISSIONS` @86.00 · `WHATEVER THEY CAN` @87.76
- **Assets** E18 telegram_western_union_1959 (form ref) · N11 ROC mission in Africa photo
- **Camera** push 1.0→1.1 to the photo. **Lock** key animation done by 88.14. **Out** CA
- **SFX** 84.86 letter_ticks · 86.00 paper_slide · 87.74 letter_ticks

### C4S016 · 88.64–92.80 · C4B016 · PAPER
- **Words** "to convince these countries to come on the Taiwanese side, ROC side."  **Why** countries come to the ROC side — the map tilts in and countries fill celadon.
- **FX** #3 map R11 · **Ref** R11 VARIATION (beige map, coloured regions, leader labels)
- **Visual** Beige Africa map (vintage atlas look) — a few countries fill celadon with watercolour edge @88.96; a leader label box gathers them.
- **Text** `convince` t-serif-i @88.96 · `ROC SIDE` `.label-box` celadon rule @92.00
- **Assets** N36 map kit beige Africa
- **Camera** slow drift. **Lock** key animation done by 92.30. **Out** W→ whip right
- **SFX** 88.94 pop_soft ×3 · 92.00 pin_pop · 92.75 whoosh

### C4S017 · 92.80–96.96 · C4B017 · NIGHT
- **Words** "CCP does the same thing. Unfortunately, CCP is just a lot bigger."  **Why** "CCP does the same thing … just a lot bigger" — China in red at true scale beside Taiwan (ref 12 is literally China in red).
- **FX** #3 relief + region fill + glow · **Ref** R12 (China filled red, halftone, glowing edge) — direct reuse, our palette
- **Visual** Grey relief East Asia; on "CCP" China fills red (halftone + 6 px glow); on "same thing" mirrored dashed arrows out to Africa; on "bigger" the camera pulls back so tiny celadon Taiwan sits beside it.
- **Text** `CCP` red label @92.80 · `same thing` t-serif-i @93.60 · `BIGGER` t-display @96.48
- **Assets** N36 map kit East Asia relief + China mask; E10
- **Camera** pull back 1.2→1.0; `FH` focus hunt when the move lands. **Lock** key animation done by 96.46. **Out** CA — pull-back continues as the bars draw
- **SFX** 92.78 burn_crackle(short) · 93.58 marker_long · 96.46 whoosh_soft

### C4S018 · 96.96–101.36 · C4B018 · GRID
- **Words** "They have a lot more access to a lot more land and people, their resources are bigger than Taiwan."  **Why** more land, more people, more resources — three paired bars, red long, celadon short (no numbers).
- **FX** #2 horizontal bars · **Ref** D04 VARIATION (horizontal bars, serif title with italic emphasis; shapes only)
- **Visual** On graph paper: title 'a lot *more*'; three pairs of bars grow at 12 fps: LAND, PEOPLE, RESOURCES (red long / celadon short), no axis values.
- **Text** `land` @98.88 · `people` @99.28 · `resources` @99.84 (t-label row labels) · `Taiwan` t-label @100.88 (celadon key)
- **Assets** E16 grid paper (ke1960_mm_grid_green_hires, desat)
- **Camera** slow push. **Lock** key animation done by 100.86. **Out** W↓
- **SFX** 98.86 dot_ticks · 99.26 dot_ticks · 99.82 dot_ticks · 101.30 whoosh

### C4S019 · 101.36–104.32 · C4B019 · PAPER
- **Words** "So slowly, CCP is winning this fight."  **Why** "slowly, CCP is winning" — a balance scale tips toward red.
- **FX** #16 cut-out + #13 · **Ref** new ref: "vintage brass balance scale cut-out" (Pinterest editorial still-life)
- **Visual** Brass balance-scale cut-out on paper; celadon pan rises, red pan sinks slowly (cam ease, 12 fps).
- **Text** `CCP` red label @102.24 · `WINNING` t-display @103.20
- **Assets** N41 balance-scale photo (PD/CC)
- **Camera** static. **Lock** key animation done by 103.82. **Out** cont. (tilt down onto the GA hemicycle on the same paper)
- **SFX** 101.40 gate_creak (scale) · 103.18 tick_soft

### C4S020 · 104.32–113.60 · C4B020 · PAPER
- **Words** "A lot more African countries are going towards the CCP, agreeing with CCP's point of view that the Chinese should seat should go to them versus Taiwan."  **Why** more African countries side with the CCP on the seat — the General Assembly as a dot hemicycle filling red.
- **FX** #2 parliament dots + #18 highlighter · **Ref** D06 / R8 VARIATION — GA hemicycle, African block highlighted
- **Visual** Hemicycle of member-state dots (grey); title highlight on 'African countries'; the African wedge flips red in 12 fps waves; the chair icon with 'CHINA' at the centre; the celadon arc shrinks.
- **Text** title `A lot more African countries` word-by-word, `African` @104.96 highlighter · `CCP` @107.60 · `Chinese seat` @110.40 · `Taiwan` @113.12
- **Assets** own SVG (dots)
- **Camera** tilt continues then settles; 3 % push. **Lock** key animation done by 113.10. **Out** W↑
- **SFX** 104.94 highlighter_swipe · 105.6–108 dot_ticks (2.4 s) · 113.10 pop_soft

### C4S021 · 113.60–120.00 · C4B021 · NIGHT
- **Words** "Even then, not a big issue. The US is with Taiwan, and it should all be good."  **Why** "The US is with Taiwan" — Eisenhower and Chiang in Taipei, 1960.
- **FX** #16 plate + #14 light weave · **Ref** —
- **Visual** Real 1960 photo/footage of President Eisenhower's motorcade with Chiang Kai-shek in Taipei (US gov PD). Fringe blur, vignette, CA 0.12; slow push.
- **Text** `not a big issue` t-serif-i @114.72 · `THE US` t-label @115.76 · `Taiwan` @116.72 (celadon rule)
- **Assets** N13 Eisenhower in Taipei 1960
- **Camera** push 1.0→1.06. **Lock** key animation done by 119.50. **Out** PS — torn-paper wipe
- **SFX** 113.60 air_swell (projector_loop low 6 s)

## 3. Act C — Teaser: the seismic event (120.00–144.83)
Music: low boom on 'seismic' 130.16, bed drops to a pad, softer layer from 134.51.

### C4S022 · 120.00–127.44 · C4B022 · PAPER
- **Words** "Now we'll come back to this diplomatic front, diplomatic war that is happening between the ROC and the CCP in the 70s,"  **Why** the diplomatic war ROC vs CCP, to be continued in the 70s — a war-room map with pins and a bookmark tab.
- **FX** #3 + #12 pins + §10.6.2 pen · **Ref** new ref: "WWII war-room table map with pins" (Churchill War Rooms style), our palette
- **Visual** World map on paper (vintage colour atlas plate); celadon and red pins on countries; a pen front-line squiggles between them @122.80; a paper index tab 'the 70s' slides in from the edge @126.72.
- **Text** `DIPLOMATIC WAR` t-label @122.80 · `ROC` @124.96 · `CCP` @125.84 · `the 70s` tab @126.72
- **Assets** N36b vintage atlas world plate
- **Camera** slow pan. **Lock** key animation done by 126.94. **Out** CA — tab slide continues; cut to the scope
- **SFX** 122.78 marker_long · 124.94 pin_pop · 125.82 pin_pop · 126.70 paper_slide

### C4S023 · 127.44–134.51 · C4B023 · NIGHT
- **Words** "because there's gonna be a big event, almost a seismic event that changes. The equation tremendously."  **Why** "a seismic event that changes the equation" — a seismograph trace on an oscilloscope spikes.
- **FX** #11 screen (Tektronix scope) + #4 hero · **Ref** new ref: "USGS drum seismograph" read on our oscilloscope screen
- **Visual** Tektronix 475A scope (E15) with a calm trace; on "seismic" the trace spikes and the whole frame shakes 4 px for 0.5 s; then still.
- **Text** `big event` t-label @128.64 · `SEISMIC` t-display **hero halate** @130.16 · `the equation` t-serif-i @132.83
- **Assets** E15 tektronix_475a_scope_frame
- **Camera** slow push. **Lock** key animation done by 134.01. **Out** FW
- **SFX** 128.62 crt_hum · 130.14 boom_low · 132.80 tone_blip · 134.40 whoosh

### C4S024 · 134.51–139.71 · C4B024 · NIGHT
- **Words** "But before we get to that, let me explain how the Taiwanese economy is at this point,"  **Why** "how the Taiwanese economy is at this point" — 1960 Taiwan street/industry footage.
- **FX** #1 footage + #14 weave · **Ref** —
- **Visual** 1960 'Taiwan: The Face of Free China' footage: Taipei boulevard high angle (traffic, bicycles).
- **Text** `TAIWANESE` @137.31 `ECONOMY` @138.19 t-label
- **Assets** E03 taiwan_1960_taipei_boulevard_high_angle.mp4
- **Camera** slow push. **Lock** key animation done by 139.21. **Out** CA
- **SFX** 134.50 projector_loop (5 s, low)

### C4S025 · 139.71–144.83 · C4B025 · PAPER
- **Words** "while they are competing with the CCP to basically, you know, win favors overseas."  **Why** competing with the CCP overseas — back to the war-room map, celadon and red pins race outward.
- **FX** #3 + #19 arrows · **Ref** war-room map (C4S022 motif)
- **Visual** Same war-room map, wider; celadon and red pen arrows race outward to countries.
- **Text** `competing` t-serif-i @140.35 · `CCP` @141.15 · `overseas` t-label @143.87
- **Assets** N36b
- **Camera** pan. **Lock** key animation done by 144.33. **Out** HC (hard cut on action: the map whips into film running backwards)
- **SFX** 140.33 marker_scratch · 141.13 marker_scratch

## 4. Act D — Rewind: Japanese rule (144.83–230.82)
Music: tape-rewind riser 146.19; sombre drone 164.43–181.55; warm melodic layer from 'positives' 182.51.

### C4S026 · 144.83–147.87 · C4B026 · NIGHT
- **Words** "Now, this is where we have to back up just a little bit more"  **Why** "back up a little bit more" — film runs backwards on a projector, years rolling back.
- **FX** #14 weave + #13 random · **Ref** —
- **Visual** Projector-gate look: a filmstrip of the previous c4 frames runs backwards fast, sprocket holes, flicker.
- **Text** `BACK UP` t-display @146.19 (FX.text.random)
- **Assets** own (filmstrip from c4 frames) + scratches_01
- **Camera** fast reverse slide. **Lock** key animation done by 147.37. **Out** W←
- **SFX** 144.83 projector_loop (3 s, rate-shifted up = rewind) · 147.80 whoosh

### C4S027 · 147.87–154.83 · C4B027 · PAPER
- **Words** "because Taiwan was actually ruled by Japan before the ROC came over, before World War II."  **Why** Taiwan ruled by Japan — a real 1935 Japanese-era Taiwan Exposition poster.
- **FX** #16 poster as B-roll (§10.5) + timeline label · **Ref** —
- **Visual** 1935 Taiwan Exposition poster (Japanese era, colour) on paper, slow push; at "before the ROC came over" a ghost celadon 'ROC' tab waits at the right edge; 'World War II' tick at the bottom.
- **Text** `RULED` @150.27 `BY` @150.91 `JAPAN` @151.15 t-display · `ROC` @152.67 t-label (celadon tab) · `World War II` @154.03
- **Assets** E14 taiwan_expo_1935_poster.jpg
- **Camera** push 1.0→1.08. **Lock** key animation done by 154.33. **Out** CA
- **SFX** 150.25 paper_slide · 152.65 pop_soft

### C4S028 · 154.83–161.39 · C4B028 · NIGHT
- **Words** "In fact, Japan took over the island of Taiwan in 1890s, during the Meiji era, if you know Japanese history,"  **Why** Japan takes the island in the 1890s, Meiji era — a Meiji-era woodblock print of the 1895 landing in Taiwan.
- **FX** #16 + #13 odometer + #12 inset with torn edge · **Ref** —
- **Visual** Colour ukiyo-e triptych of Japanese troops in Taiwan (1895), pan across; Meiji Emperor portrait inset (torn-edge card) @158.43.
- **Text** `1890s` t-display **hero halate** odometer @157.31 · `MEIJI ERA` t-label @158.43
- **Assets** N15 1895 ukiyo-e print · N15b Meiji Emperor portrait
- **Camera** pan left→right. **Lock** key animation done by 160.89. **Out** W↓
- **SFX** 157.29 odometer_tick · 158.41 paper_slide

### C4S029 · 161.39–164.43 · C4B029 · GRID
- **Words** "and this rule continues until the end of World War II."  **Why** rule continues until the end of WWII — a timeline bar on ruled paper.
- **FX** #2 timeline (R7 era band) · **Ref** R7 VARIATION (era band = Japanese rule)
- **Visual** Ruled ledger paper; a band grows from '1890s' to a marker 'end of World War II' at 12 fps.
- **Text** `rule` t-label @161.79 · `END OF WORLD WAR II` word-by-word `end` @163.15 `World` @163.47
- **Assets** E16 ke1960_business_ruled_orange_hires (desat)
- **Camera** drift. **Lock** key animation done by 163.93. **Out** CA
- **SFX** 161.77 dot_slide · 163.13 tick_soft

### C4S030 · 164.43–171.39 · C4B030 · NIGHT
- **Words** "Now, there are a lot of problems with Japanese rule of Taiwan, and I'm sure if you guys know anything about Japanese history in China,"  **Why** problems with Japanese rule; Japanese history in China — sombre layered archival of the Japanese army in China.
- **FX** #10 Vox layered (dark) + #14 · **Ref** s09 VARIATION (night)
- **Visual** Desaturated 1937–38 Japanese troops in China photos (non-graphic: marching columns), tinted panels drift.
- **Text** `problems` t-serif-i @165.39 · `Japanese history in China` word-by-word `Japanese` @169.47 `history` @170.03 `in` @170.43 `China` @170.59
- **Assets** N17 Japanese army in China (non-graphic)
- **Camera** slow push. **Lock** key animation done by 170.89. **Out** cont.
- **SFX** 164.43 air_swell (low, sombre)

### C4S031 · 171.39–174.35 · C4B031 · NIGHT
- **Words** "you know that they can get pretty brutal."  **Why** "pretty brutal" — same image, veil and push.
- **FX** §10.6.3 contrast call-out + CS · **Ref** —
- **Visual** Punch-in 10 % on the marching column; lifted-black veil.
- **Text** `BRUTAL` t-display @173.63 (chokeSettle, bone, clean — no glow)
- **Assets** N17
- **Camera** push. **Lock** key animation done by 173.85. **Out** PS
- **SFX** 173.61 circuit_clunk

### C4S032 · 174.35–181.55 · C4B032 · PAPER
- **Words** "Now, things aren't as bad as some of the worst stories we have heard from Japan, but that doesn't mean there wasn't any brutality."  **Why** "not as bad as the worst stories, but … brutality" — a real colonial-police photo on stained paper, pen circle.
- **FX** #16 + §10.6.2 pen markup · **Ref** —
- **Visual** Japanese colonial police in Taiwan photo (pre-1945, PD) on paper_stained (multiply), pen circle on the officers @180.51.
- **Text** `worst stories` t-serif-i @176.67 · `brutality` t-label @180.51
- **Assets** N17b Japanese colonial police in Taiwan
- **Camera** slow drift. **Lock** key animation done by 181.05. **Out** FW
- **SFX** 180.49 marker_scratch

### C4S033 · 181.55–184.67 · C4B033 · NIGHT
- **Words** "But there were positives from the Japanese rule."  **Why** "there were positives" — a 1930s Taipei street photo warms up.
- **FX** #8 streaks + #4 hero · **Ref** —
- **Visual** Japanese-era Taihoku (Taipei) street photo; grade lifts from cold to warm sepia; streaks open behind the title.
- **Text** `POSITIVES` t-display **hero halate** @182.51
- **Assets** N16f 1930s Taihoku street
- **Camera** push. **Lock** key animation done by 184.17. **Out** W→
- **SFX** 182.49 air_swell · 184.60 whoosh

### C4S034 · 184.67–190.51 · C4B034 · PAPER
- **Words** "Japan invested heavily in building infrastructure, building railways, ports, hydropower, electricity,"  **Why** infrastructure, railways, ports, hydropower, electricity — a collage poster, one photo per word.
- **FX** #12 collage + D07 poster layout + stamps · **Ref** D07 VARIATION (collage poster: photos + typographic box + stamps)
- **Visual** Typographic box 'INFRASTRUCTURE' + Japanese-era photos pinned on words: railway, port, hydropower plant, power lines.
- **Text** `INFRASTRUCTURE` box @186.75 · `railways` @187.87 · `ports` @188.43 · `hydropower` @188.91 · `electricity` @189.71 (t-label captions)
- **Assets** N16a railway · E08 keelung_port / N16b · E04 Sun Moon Lake still / N16c · N16d power lines
- **Camera** pan across. **Lock** key animation done by 190.01. **Out** cont.
- **SFX** 187.85 paper_slide · 188.41 paper_slide · 188.89 paper_slide · 189.69 paper_slide

### C4S035 · 190.51–194.74 · C4B035 · PAPER
- **Words** "and primary school for everyone. So they were really building a system."  **Why** primary school for everyone → a system — school photo joins the collage, pen lines link everything.
- **FX** #12 + #19 · **Ref** D07 continued
- **Visual** Kōgakkō pupils photo pins @190.75; pen lines connect all cards into a network; label-box 'A SYSTEM'.
- **Text** `primary school` @190.75 · `for everyone` @191.71 · `A SYSTEM` .label-box @193.87
- **Assets** N16e primary school pupils
- **Camera** pull back. **Lock** key animation done by 194.24. **Out** W↓
- **SFX** 190.73 paper_slide · 192.5 marker_long · 193.85 pop_soft

### C4S036 · 194.74–199.14 · C4B036 · NIGHT
- **Words** "That gave Taiwan a shot at being pretty good economy."  **Why** "a shot at a good economy" — the 1935 bird's-eye painting of Taiwan.
- **FX** #16 painting as B-roll · **Ref** —
- **Visual** 1935 bird's-eye colour painting of Taiwan, slow pan across the island's towns/railway.
- **Text** `a shot` t-serif-i @196.42 · `GOOD` @198.10 `ECONOMY` @198.42 t-label
- **Assets** E14 taiwan_birdseye_1935.jpg
- **Camera** pan. **Lock** key animation done by 198.64. **Out** CA
- **SFX** 194.70 air_swell

### C4S037 · 199.14–204.98 · C4B037 · NIGHT
- **Words** "They also invested heavily in the agricultural system that kept increasing Taiwanese yield for a very long time."  **Why** "agricultural system that kept increasing yield" — a rising yield line over a ghosted Taiwan and its rice paddies.
- **FX** #2 line chart (D13) + #16 ghost footage · **Ref** D13 VARIATION — dark line chart over a ghost map; ghost = Taiwan relief + 1960 paddy footage at 15 %
- **Visual** Night ground; Taiwan relief ghosted at 12 %, paddy-field footage (Face of Free China) multiplied at 15 % inside the island mask. A celadon line draws left→right and keeps climbing (no axis values, no years — shape only); a dot rides the tip; hold 0.5 s at the top.
- **Text** `AGRICULTURAL` @200.74 `SYSTEM` @201.54 t-label · `increasing` t-serif-i @202.42 · `yield` end-label @203.54
- **Assets** E10 taiwan_relief_grey · N40a paddies clip (Face of Free China)
- **Camera** camera rides up with the line (cam ease). **Lock** key animation done by 204.48. **Out** W← whip left
- **SFX** 200.72 dot_slide · 202.40 tick_soft (stopwatch 1.2 s) · 204.90 whoosh

### C4S038 · 204.98–210.66 · C4B038 · PAPER
- **Words** "And even after after Japan, this is gonna be very useful for the government that takes over Taiwan."  **Why** "even after Japan, this is useful for the government that takes over" — Japan's files are handed to the next government.
- **FX** #12 desk collage + #19 arrow · **Ref** R9 desk VARIATION (light desk, no cork) — Pinterest idea "archive folders handed over on a desk"
- **Visual** Top-down desk on paper_fiber: a manila folder tabbed 'Japan' holds mini prints of the C4S034–035 cards (railway, port, dam, school). On "government" it slides across to a second folder with a celadon tab; pen arrow between them.
- **Text** `Japan` tab t-label @206.34 · `useful` t-serif-i @208.18 · `government` celadon tab t-label @208.98
- **Assets** own (reuses the C4S034 photos small)
- **Camera** top-down drift right. **Lock** key animation done by 210.16. **Out** FW light-flash whip
- **SFX** 206.32 paper_slide · 208.96 paper_slide · 210.60 whoosh

### C4S039 · 210.66–214.18 · C4B039 · NIGHT
- **Words** "In fact, in 1940, so right before World War II starts,"  **Why** "In 1940, right before World War II" — the year over the Japanese-built Governor-General's Office (today's Presidential Office).
- **FX** #13 odometer + #8 streaks + #4 hero · **Ref** s01 VARIATION (year card over footage instead of black)
- **Visual** 1960 footage of the Presidential Office (built by Japan as the Governor-General's Office), darkened to 35 %, streak canvas behind the year.
- **Text** `1940` t-display 280 px **hero halate** odometer @211.30 · `World War II` t-label @212.90
- **Assets** E01 taiwan_1960_presidential_office_taipei.mp4
- **Camera** slow push 1.0→1.05. **Lock** key animation done by 213.68. **Out** PT — push through the building's doorway into the tilted map
- **SFX** 211.28 odometer_tick · 212.88 tick_soft

### C4S040 · 214.18–222.66 · C4B040 · NIGHT
- **Words** "you could easily make an argument that Taiwan was the most developed piece of land piece of country in East Asia outside of Japan."  **Why** "Taiwan was the most developed … in East Asia outside of Japan" — tilted East Asia map; Taiwan emits rings; Japan outlined as the exception.
- **FX** #3 map + §10.6.7 radio waves + §10.6.3 contrast call-out + #20 · **Ref** D10 VARIATION (tilted close-up atlas; rings instead of route lines)
- **Visual** Map kit East Asia shaded relief on a tilted plane (rotateX 28°, rotateZ −6°, lens blur far edge). Taiwan fills celadon (watercolour edge) and emits rings @216.82; contrast call-out isolates Taiwan; @220.34 the camera pulls to show East Asia; @221.78 Japan gets a dashed pen outline (excluded).
- **Text** `MOST DEVELOPED` t-label @216.82 · `East Asia` t-serif-i @220.34 · `Japan` t-label @221.78
- **Assets** N36 map kit East Asia relief + Taiwan/Japan masks
- **Camera** tilted push, then pull-back; `FH` focus hunt when the move lands. **Lock** key animation done by 222.16. **Out** CA — pull-back lands on the paper atlas
- **SFX** 216.80 circuit_clunk · 217.00 tone_blip (rings, soft) · 221.76 marker_scratch

### C4S041 · 222.66–230.82 · C4B041 · PAPER
- **Words** "So it was really doing pretty good economically speaking, at least when looking at peers that are just close by."  **Why** "doing pretty good … compared with peers close by" — a vintage atlas plate; Taiwan circled, its neighbours ticked.
- **FX** #3 old map + §10.6.2 pen markups · **Ref** D10 / R10 VARIATION (vintage colour atlas, pen marks)
- **Visual** Two paper layers: a 1930s colour atlas plate of East Asia; pen circle round Taiwan @226.50, small pen ticks next to the nearby countries @229.06.
- **Text** `economically` t-serif-i @226.50 · `PEERS` t-label @229.06
- **Assets** N36b vintage atlas East Asia plate
- **Camera** slow drift left. **Lock** key animation done by 230.32. **Out** W↑ whip up (sky → bombers)
- **SFX** 226.48 marker_scratch · 229.04 pencil_scribble · 230.75 whoosh

## 5. Act E — War damage, the nationalists, US aid (230.82–274.27)
Music: darker pulse from 230.82; relief on 'luckily' 264.35; lift on 1.5 BILLION 269.39.

### C4S042 · 230.82–235.94 · C4B042 · NIGHT
- **Words** "Now, unfortunately, during war, a lot of bombing takes place, a lot of stuff does get destroyed."  **Why** "during war, a lot of bombing … destroyed" — real USAAF footage of raids on Formosa.
- **FX** #1 footage + #14 weave + #16 · **Ref** —
- **Visual** 1944–45 USAAF strike footage/photos over Formosa (bomb run, smoke over a harbour). Gate weave amp 0.8, flicker; no gore.
- **Text** `BOMBING` t-label @232.82 · `destroyed` t-serif-i @235.14
- **Assets** N19 USAAF Formosa raid footage (NARA / archive.org)
- **Camera** static (footage moves). **Lock** key animation done by 235.44. **Out** PT — push through the smoke into the map
- **SFX** 232.80 boom_low (soft) · 230.9 projector_loop (5 s)

### C4S043 · 235.94–241.62 · C4B043 · PAPER
- **Words** "So when the nationalists come running to Taiwan, they do face a lot of economic issue."  **Why** "the nationalists come running to Taiwan" — routes from the mainland to the island on a tilted vintage map.
- **FX** #3 D10 routes · **Ref** D10 VARIATION (tilted vintage colour map + route lines)
- **Visual** Tilted vintage map of the Taiwan Strait (E13 1943 map + kit); several dashed ink routes draw from mainland ports to Taiwan's ports @236.58; Taiwan fills celadon @238.42.
- **Text** `THE NATIONALISTS` .label-box (celadon rule) @236.58 · `Taiwan` t-label @238.42
- **Assets** E13 formosa_1943_japanese_aviation_map.jpg (+json) · N36 kit strait
- **Camera** track along the routes. **Lock** key animation done by 241.12. **Out** W→
- **SFX** 236.56 marker_long · 238.40 pop_soft · 241.55 whoosh

### C4S044 · 241.62–245.86 · C4B044 · NIGHT
- **Words** "There's hyperinflation, there's electric grid is not top-notch,"  **Why** "hyperinflation … electric grid not top-notch" — 1949 banknotes stack absurdly; a period bulb flickers.
- **FX** #13 FX.text.random + #16 cut-outs · **Ref** Pinterest idea: "banknote stack still-life, hard light"
- **Visual** Real 1949 banknote cut-outs (old Taiwan dollar, huge denominations) drop into a growing stack at 12 fps under a hard lamp; @243.62 the lamp (a 1940s bulb cut-out) flickers twice.
- **Text** `HYPERINFLATION` t-display @241.86 (random letters) · `electric grid` t-label @243.62
- **Assets** N21 1949 banknotes · N16d period bulb / power-line photo
- **Camera** push 1.0→1.08. **Lock** key animation done by 245.36. **Out** CA
- **SFX** 241.84 paper_rustle ×3 · 243.60 crt_off (flicker)

### C4S045 · 245.86–253.14 · C4B045 · NIGHT
- **Words** "especially considering how many people are gonna come, a few million people are gonna come from China who just did not want to live under communist rule."  **Why** "a few million people … from China who did not want to live under communist rule" — a crowded 1949 ship arriving.
- **FX** #16 plate + #14 weave · **Ref** —
- **Visual** Real 1949 photo/footage of a ship packed with soldiers and civilians arriving in Keelung/Kaohsiung. Fringe blur; slow push.
- **Text** `A` `FEW` @248.34 `MILLION` @248.58 `PEOPLE` @248.98 t-display word-by-word · `communist rule` t-serif-i @252.10
- **Assets** N20 1949 refugee ship photo/footage
- **Camera** push 1.0→1.06. **Lock** key animation done by 252.64. **Out** W↓
- **SFX** 245.90 air_swell · 252.95 whoosh

### C4S046 · 253.14–258.99 · C4B046 · GRID
- **Words** "So the Taiwanese population grows a lot, and they have to somehow manage to make sure they keep it."  **Why** "the Taiwanese population grows a lot" — isotype people fill the island.
- **FX** #2 isotype grid (D03) · **Ref** D03 VARIATION (pictograms fill an island silhouette instead of rows)
- **Visual** Graph paper; Taiwan outline (ink); person pictograms (ink) fill it row by row at 12 fps, then overflow the outline edges — shape only, no numbers.
- **Text** `POPULATION` t-label @254.58 · `grows` t-serif-i @255.14
- **Assets** N38 pictogram SVG · E10 outline
- **Camera** static, slow push. **Lock** key animation done by 258.49. **Out** CA — overflow motion carries the cut
- **SFX** 254.56 dot_ticks (2 s)

### C4S047 · 258.99–264.11 · C4B047 · NIGHT
- **Words** "under control where you know people are not just starving, protesting, or just you know starting a revolution."  **Why** "under control … not starving, protesting, or starting a revolution" — three dark panels, one per word.
- **FX** #10 Vox layered (night) · **Ref** s09 VARIATION
- **Visual** Three tinted archival panels slide in on their words: empty rice bowls / a ration queue, a street crowd, a torn propaganda wall — non-specific period images, desaturated.
- **Text** `control` t-label @259.23 · `starving` @260.91 · `protesting` @261.63 · `revolution` t-serif-i @263.39
- **Assets** N25b archival panels (ration line, crowd, wall)
- **Camera** each panel drifts at its own speed. **Lock** key animation done by 263.61. **Out** FW
- **SFX** 260.89 paper_slide · 261.61 paper_slide · 263.37 paper_slide · 264.05 whoosh

### C4S048 · 264.11–268.19 · C4B048 · PAPER
- **Words** "Now luckily American aid does help. Between 50s to 65,"  **Why** "American aid does help — between the 50s and 65" — the US-aid handshake emblem on a real flour sack.
- **FX** #18 FX.chokeSettle reveal + timeline ticks · **Ref** —
- **Visual** Real photo of a US-aid flour sack with the handshake emblem; the emblem chokes in (rough) and settles; a thin ink timeline under it ticks '50s … '65.
- **Text** `AMERICAN AID` t-label @265.07 · `'50s` @266.83 · `'65` @267.55
- **Assets** N22 US-aid handshake emblem / flour sack photo
- **Camera** push 1.0→1.06. **Lock** key animation done by 267.69. **Out** CA
- **SFX** 265.05 stamp_thud (soft) · 266.81 tick_soft · 267.53 tick_soft

### C4S049 · 268.19–274.27 · C4B049 · NIGHT
- **Words** "America sends roughly 1.5 billion in American aid that helped the island stay afloat."  **Why** "America sends roughly 1.5 billion in aid … stay afloat" — one thick flow from the US to Taiwan.
- **FX** #2 Sankey (D11) + #13 count · **Ref** D11 VARIATION (one flow, ghost Pacific)
- **Visual** Ghost Pacific map (E12 at 15 %); a thick bone flow band runs from the US coast to Taiwan, which lights celadon; counter in the band.
- **Text** `1.5` @269.39 **yellow key number** (count 0→1.5, 12 fps) + `BILLION` @269.95 · `afloat` t-serif-i @273.55
- **Assets** E12 pacific_relief_grey (+json)
- **Camera** pan west with the flow. **Lock** key animation done by 273.77. **Out** PS — paper slides over
- **SFX** 268.20 dot_slide (flow) · 269.37 counter_ticks

## 6. Act F — Land reform (274.27–351.94)
Music: bright melodic layer + steady pulse; small stings on INDUSTRIALISTS 321.30 / 343.94.

### C4S050 · 274.27–283.31 · C4B050 · PAPER
- **Words** "And on top of that, there were a lot of land reforms that were implemented by Taiwanese government that kinda worked out really, really, really well inadvertently."  **Why** "a lot of land reforms … worked out really well, inadvertently" — a real 1950s land-reform poster.
- **FX** #16 poster as B-roll + label · **Ref** —
- **Visual** Colour 1950s 'land to the tiller' poster, slow push; label-box over it.
- **Text** `LAND REFORMS` .label-box @276.19 · `inadvertently` t-serif-i @282.27
- **Assets** N23 land-reform poster
- **Camera** push 1.0→1.08. **Lock** key animation done by 282.81. **Out** W←
- **SFX** 276.17 paper_slide · 283.25 whoosh

### C4S051 · 283.31–289.23 · C4B051 · GRID
- **Words** "Like they weren't planning on doing this. So the way they did land reforms was they took people who had a lot of lands and"  **Why** "they took people who had a lot of lands" — a landowner holding many parcels (relationship diagram starts).
- **FX** #2 D15 diagram · **Ref** D15 VARIATION (landowner / farmer / company circles on ruled paper)
- **Visual** Ruled paper; a portrait circle (period landowner photo, ink duotone) with a cluster of field-parcel squares around it that pop at 12 fps @288.43.
- **Text** `weren't planning` t-serif-i @283.79 · `a lot of lands` t-label @288.43
- **Assets** N23c landowner photo · own parcels SVG
- **Camera** static. **Lock** key animation done by 288.73. **Out** cont.
- **SFX** 288.41 dot_ticks

### C4S052 · 289.23–295.23 · C4B052 · GRID
- **Words** "basically gave them to other people who are farming the land and just like hey you're the new owner."  **Why** "gave them to people farming the land: you're the new owner" — parcels slide to the farmer; a deed is stamped.
- **FX** #2 D15 + stamp · **Ref** D15 continued
- **Visual** Second circle (farmer photo); parcels slide across along a pen arrow @291.47; a deed card drops and gets stamped `NEW OWNER` @294.27.
- **Text** `farming` t-label @291.47 · `NEW OWNER` stamp @294.27
- **Assets** N23b land deed (real or typeset) · N23d farmer photo
- **Camera** static. **Lock** key animation done by 294.73. **Out** FW
- **SFX** 291.45 dot_slide · 294.25 stamp_thud · 295.15 whoosh

### C4S053 · 295.23–301.79 · C4B053 · NIGHT
- **Words** "So this is something other countries have tried too. Unfortunately does not go really well but what the Taiwanese government did is uh"  **Why** "other countries have tried … does not go well … but the Taiwanese government" — dark world map, then the push to Taiwan.
- **FX** #3 world map + #19 · **Ref** —
- **Visual** Dark world basemap; a few anonymous pen crosses appear on other continents @298.35 (no country names); camera pushes to Taiwan (celadon) @299.55.
- **Text** `other countries` t-serif-i @296.35 · `not go really well` t-label @298.35 · `Taiwanese government` t-label @299.55
- **Assets** E11 world_basemap_desat (+json) / N36 kit
- **Camera** push to Taiwan. **Lock** key animation done by 301.29. **Out** CA
- **SFX** 298.33 pencil_scribble · 299.53 whoosh_soft

### C4S054 · 301.79–307.47 · C4B054 · PAPER
- **Words** "when they took away lands from big landowners they gave them shares into state owned companies"  **Why** "they gave them shares into state owned companies" — a real share certificate, highlighted.
- **FX** #5 tilted document + #18 highlighter + two paper layers · **Ref** —
- **Visual** Real 1950s Taiwanese share certificate (engraved guilloche border) tilted on two paper layers; highlighter swipe across the 'shares' line.
- **Text** `big landowners` t-label @303.39 · `SHARES` @304.91 · `state-owned companies` t-serif-i @305.87
- **Assets** N24 share certificate scan
- **Camera** push 1.0→1.12. **Lock** key animation done by 306.97. **Out** W↑
- **SFX** 304.89 highlighter_swipe · 307.40 whoosh

### C4S055 · 307.47–316.26 · C4B055 · PAPER
- **Words** "so now these landowners who were a little bit managerial before have now an incentive to make sure the state companies are running well"  **Why** "now these landowners … have an incentive to make sure the state companies are running well" — diagram: landowner → shares → company.
- **FX** #2 D15 + #19 arrows · **Ref** D15 continued (third circle = factory)
- **Visual** Back on the diagram: the landowner circle gains a share-certificate chip; pen arrow to a factory icon circle; @313.31 'incentive' tag; the factory's gear turns @315.23.
- **Text** `INCENTIVE` .label-box @313.31 (yellow highlighter) · `running well` t-serif-i @315.23
- **Assets** own SVG
- **Camera** drift. **Lock** key animation done by 315.76. **Out** CA
- **SFX** 313.29 pop_soft · 315.21 gear tick (tick_soft)

### C4S056 · 316.26–322.34 · C4B056 · NIGHT
- **Words** "They probably weren't planning or hoping that this happens, but they have now turned these managers into industrialists."  **Why** "turned these managers into industrialists" — a 1950s state-owned factory in 2.5D.
- **FX** #17 2.5D no.2 · **Ref** 2.5D-campus VARIATION (factory hall: backdrop, machines, foreground workers)
- **Visual** 1950s Taiwanese state-owned factory photo cut into 3 layers; dolly in; title tucked behind the foreground machine.
- **Text** `managers` t-label @320.26 · `INDUSTRIALISTS` t-display **hero halate** @321.30
- **Assets** N24b 1950s factory photo ≥ 3000 px
- **Camera** 2.5D dolly; `FH` focus hunt when the move lands. **Lock** key animation done by 321.84. **Out** W→
- **SFX** 321.28 boom_low (soft) · 322.30 whoosh

### C4S057 · 322.34–330.66 · C4B057 · NIGHT
- **Words** "And on top of that, these new people who are now, you know, creating agricultural land or cultivating land. They were cultivating it before too, but now they own the piece of land."  **Why** "cultivating it before too, but now they own the piece of land" — 1960 farmer ploughing his field.
- **FX** #1 footage + #14 weave · **Ref** —
- **Visual** Face of Free China 1960: farmer with a water buffalo ploughing a paddy; a celadon outline traces the plot boundary @329.70.
- **Text** `cultivating` t-serif-i @326.82 · `OWN` t-label @329.70
- **Assets** N40a Face of Free China (farm segment)
- **Camera** static. **Lock** key animation done by 330.16. **Out** PS
- **SFX** 322.40 projector_loop (8 s)

### C4S058 · 330.66–335.78 · C4B058 · PAPER
- **Words** "If they produce any surplus, they can, you know, sell it for a profit, so there's an incentive for them."  **Why** "if they produce any surplus they can sell it for a profit" — a 1950s market collage.
- **FX** #12 collage + #13 count · **Ref** —
- **Visual** Collage on paper: real 1950s–60s Taiwan market photo, baskets of rice; a pile of coins grows @333.78.
- **Text** `SURPLUS` t-label @331.62 · `profit` t-serif-i @333.78 · `incentive` @334.66
- **Assets** N25 market photo
- **Camera** drift. **Lock** key animation done by 335.28. **Out** CA
- **SFX** 331.60 paper_slide · 333.76 coin pops (pop_soft)

### C4S059 · 335.78–344.90 · C4B059 · GRID
- **Words** "So the pr the people who were cultivating the land before now became producers, farmers, and the people who own the land before now became industrialist."  **Why** "cultivators became producers, farmers; owners became industrialists" — before→after columns.
- **FX** #2 transformation diagram · **Ref** new ref: "before / after arrow infographic" (two columns, morphing icons)
- **Visual** Graph paper, two columns: farmer pictogram → 'producers, farmers'; landowner pictogram → factory/industrialist pictogram, arrows draw.
- **Text** `PRODUCERS` @340.50 · `farmers` @341.14 · `INDUSTRIALISTS` @343.94
- **Assets** own pictograms
- **Camera** static. **Lock** key animation done by 344.40. **Out** W↓
- **SFX** 340.48 pop_soft · 343.92 pop_soft · 344.85 whoosh

### C4S060 · 344.90–351.94 · C4B060 · NIGHT
- **Words** "That's gonna help, at least in the short term, the Taiwanese economy because of new incentive structures that are being built."  **Why** "help the Taiwanese economy because of new incentive structures" — staircase bars over ghost Taiwan.
- **FX** #2 chart (D13b) · **Ref** D13 VARIATION (staircase bars instead of a line)
- **Visual** Night; ghost Taiwan; celadon bars step up at 12 fps (shape only), each step a small arrow 'incentive'.
- **Text** `Taiwanese economy` t-label @347.46 · `INCENTIVE STRUCTURES` @349.46
- **Assets** E10
- **Camera** drift up. **Lock** key animation done by 351.44. **Out** FW
- **SFX** 349.44 dot_ticks · 351.85 whoosh

## 7. Act G — Dictatorship & White Terror; Mao (351.94–387.85)
Music: cold drone; near-silence under 'Thousands … executed' 368.42.

### C4S061 · 351.94–357.54 · C4B061 · PAPER
- **Words** "Now, politically speaking, at this point, Taiwan is not a democracy that we know of right now."  **Why** "Taiwan is not a democracy that we know of right now" — an empty ballot box gets a pen cross.
- **FX** #16 cut-out + §10.6.2 pen cross · **Ref** Pinterest idea: "civics-textbook object still-life on paper"
- **Visual** Period wooden ballot-box photo cut-out (halftone) centred on paper_cream; on "democracy" a two-stroke pen cross draws over it (boil 4, multiply).
- **Text** `politically` t-label @352.26 · `NOT` @355.14 `A` @355.38 `DEMOCRACY` @355.46 t-display word-by-word
- **Assets** N26c ballot-box photo
- **Camera** static, 2 % push. **Lock** key animation done by 357.04. **Out** CA — the cross's last stroke carries the cut
- **SFX** 352.24 paper_slide · 355.44 pencil_scribble

### C4S062 · 357.54–362.90 · C4B062 · GRID
- **Words** "In fact, it does not become a democracy for a very long time, almost 40 years from 1949."  **Why** "almost 40 years from 1949" — a timeline of 40 ticks from 1949.
- **FX** #2 timeline + #13 count · **Ref** R7 VARIATION (timeline with a bracket instead of a line)
- **Visual** K+E grid; a tick labelled 1949 at the left; on "40" a bar grows right at 12 fps across 40 small ticks; a pen bracket under it.
- **Text** `40 YEARS` **yellow key number** @361.14 (count 0→40) · `1949` t-label @361.94
- **Assets** E16 ke1960_cross_section_green_hires (desat)
- **Camera** drift right with the bar; `FH` focus hunt when the move lands. **Lock** key animation done by 362.40. **Out** W→
- **SFX** 361.12 counter_ticks · 362.85 whoosh

### C4S063 · 362.90–368.42 · C4B063 · NIGHT
- **Words** "It stays a dictatorship, a one party state. It goes through a period that's called white terror."  **Why** "a dictatorship, a one party state … a period called white terror" — dark layered archival: party rally, prison island.
- **FX** #10 Vox layered (night) + #4 hero · **Ref** s09 VARIATION (night)
- **Visual** Two tinted panels: a 1950s KMT party rally (portraits, banners) and the Green Island prison camp; cold bone tint; drift at different speeds.
- **Text** `DICTATORSHIP` t-label @363.62 · `one-party state` t-serif-i @364.66 · `WHITE TERROR` t-display **hero halate (cool)** @367.30
- **Assets** N26b 1950s KMT rally photo · N26 Green Island prison photo
- **Camera** slow push. **Lock** key animation done by 367.92. **Out** cont. — camera keeps drifting into the prison panel
- **SFX** 362.90 air_swell (low) · 367.28 boom_low (very soft)

### C4S064 · 368.42–372.66 · C4B064 · NIGHT
- **Words** "Thousands of people are executed, especially if they are against the party that's ruling."  **Why** "thousands of people are executed" — the prison corridor, a sharp spot moving along the cell doors.
- **FX** §10.6.5 focal blur · **Ref** —
- **Visual** Real prison corridor (Jing-Mei / Green Island White Terror memorial), focal blur travels along the cell doors (long extreme ease). Non-graphic.
- **Text** `THOUSANDS` t-label @368.42
- **Assets** N26 prison corridor photo
- **Camera** slow push. **Lock** key animation done by 372.16. **Out** cont.
- **SFX** 368.40 air_swell (low)

### C4S065 · 372.66–376.25 · C4B065 · NIGHT
- **Words** "And yeah, not the best place to live."  **Why** "And yeah, not the best place to live" — hold the corridor; light dims one step; no text (aside line).
- **FX** #16 hold + vignette · **Ref** —
- **Visual** Same corridor, vignette tightens, a band of window light fades.
- **Text** none (aside)
- **Assets** N26
- **Camera** slow drift. **Lock** key animation done by 375.75. **Out** W← whip left
- **SFX** 376.15 whoosh_soft

### C4S066 · 376.25–383.37 · C4B066 · PAPER
- **Words** "Pretty harsh dictatorship, but still what's happening in Taiwan is nothing compared to what Mao Zedong is about to do in China."  **Why** "harsh dictatorship, but … nothing compared to what Mao Zedong is about to do in China" — Mao's painted portrait; China dwarfs Taiwan.
- **FX** #16 painting as B-roll + #3 inset map · **Ref** Pinterest idea: "portrait card + mini map inset, museum-label style"
- **Visual** Paper ground; Mao's official painted portrait as a card (ink rule frame); inset relief map: China fills red @382.89, tiny celadon Taiwan beside it.
- **Text** `harsh dictatorship` t-serif-i @376.89 · `MAO ZEDONG` .label-box @380.89 · `China` t-label @382.89
- **Assets** N27 Mao painted portrait · N36 East Asia relief
- **Camera** push 1.0→1.06. **Lock** key animation done by 382.87. **Out** CA
- **SFX** 380.87 paper_slide · 382.87 burn_crackle (short)

### C4S067 · 383.37–387.85 · C4B067 · NIGHT
- **Words** "He goes through like bunch of crazy stuff. And on top of that, by the way."  **Why** "he goes through a bunch of crazy stuff" — Great Leap Forward posters as B-roll.
- **FX** #16 posters + internal W whip · **Ref** —
- **Visual** Two colour propaganda posters (1958 Great Leap Forward), full-frame, one whip between them @384.40; the aside "And on top of that, by the way" stays on the second poster.
- **Text** `crazy stuff` t-serif-i @385.13
- **Assets** N27b Great Leap Forward posters ×2
- **Camera** push. **Lock** key animation done by 387.35. **Out** PS — paper slides over
- **SFX** 384.38 whoosh · 387.80 paper_slide

## 8. Act H — Open doors, brain drain, NTU (387.85–485.46)
Music: warm pulse returns 393.69; playful accent on the slogan 436–444; rhythm out under 'not actually true' 457.78.

### C4S068 · 387.85–393.69 · C4B068 · PAPER
- **Words** "Taiwanese dictatorship is a bit different than the Chinese dictatorship in many different ways, one of them being"  **Why** "Taiwanese dictatorship is a bit different than the Chinese dictatorship" — a serif title with the emphasis word.
- **FX** R6 serif title + #18 highlighter · **Ref** R6 VARIATION (two-row title, highlighted emphasis instead of a red italic)
- **Visual** Paper; serif title builds word by word: 'Taiwanese dictatorship' (celadon rule) / 'a bit *different*' / 'Chinese dictatorship' (red rule).
- **Text** `Taiwanese` @387.85 `dictatorship` @388.57 · `different` t-serif-i + highlighter @389.85 · `Chinese` @390.57 `dictatorship` @390.97
- **Assets** own
- **Camera** static. **Lock** key animation done by 393.19. **Out** W↑
- **SFX** 389.83 highlighter_swipe · 393.60 whoosh

### C4S069 · 393.69–399.37 · C4B069 · NIGHT
- **Words** "that Taiwan did not shut off its doors, meaning it did not just force people to stay inside."  **Why** "Taiwan did not shut off its doors … did not force people to stay inside" — the departure doors at Taipei's airport swing open.
- **FX** #16 + PT push-through · **Ref** —
- **Visual** 1960s Taipei Songshan Airport departure hall/doors photo; doors open (cut-out panels slide) and the camera pushes through into the next scene.
- **Text** `did` @394.57 `not` @394.73 `shut` @394.89 `its` @395.37 `doors` @395.53 t-display word-by-word
- **Assets** N29 Songshan Airport 1960s photo
- **Camera** push through the doors. **Lock** key animation done by 398.87. **Out** PT
- **SFX** 395.51 gate_creak · 398.80 whoosh

### C4S070 · 399.37–408.25 · C4B070 · PAPER
- **Words** "And remember, from the Japanese times, the universities and other educational institutes, including lower level educational institutes, are still pretty good."  **Why** "from the Japanese times, the universities and other educational institutes … still pretty good" — collage of the Japanese-built university (today NTU) and schools.
- **FX** #12 collage + torn edges · **Ref** Pinterest idea: "university archive scrapbook page"
- **Visual** Paper collage: Taihoku Imperial University building (Japanese era, today NTU), a 1950s classroom, a school gate; torn edges, pinned stop-motion.
- **Text** `Japanese times` t-label @400.33 · `UNIVERSITIES` t-display @401.53 · `pretty good` t-serif-i @407.21
- **Assets** N28 Taihoku Imperial University / NTU photos · N28c classroom
- **Camera** pan. **Lock** key animation done by 407.75. **Out** CA
- **SFX** 401.51 paper_slide · 403.45 paper_slide

### C4S071 · 408.25–415.05 · C4B071 · GRID
- **Words** "That means Taiwan is producing a lot of smart people and it's not forcing them to stay inside, so they can go overseas."  **Why** "Taiwan is producing a lot of smart people … they can go overseas" — graduate pictograms fill a grid then walk off.
- **FX** #2 isotype (D03) · **Ref** D03 VARIATION (graduate icons that leave the grid)
- **Visual** Grid paper: graduate icons (assets/icons/graduate*.svg, ink) fill rows at 12 fps; @414.17 a column of them slides off the right edge.
- **Text** `SMART PEOPLE` t-label @410.33 · `overseas` t-serif-i @414.17
- **Assets** E24 assets/icons/graduate*.svg
- **Camera** static, then pan right. **Lock** key animation done by 414.55. **Out** W→
- **SFX** 410.31 dot_ticks · 414.15 dot_slide · 414.95 whoosh

### C4S072 · 415.05–420.17 · C4B072 · NIGHT
- **Words** "Kinda like a brain drain that's happening in the third world right now. A lot of smart people just leave."  **Why** "brain drain … in the third world … smart people just leave" — glowing arcs leave many countries on a dark world map.
- **FX** #3 world map + flow arcs + #4 hero · **Ref** new ref: "migration flow map, glowing arcs on a dark globe" (Pinterest data-art)
- **Visual** Dark world basemap; bone arcs leave many countries (shape only) toward North America/Europe at 12 fps.
- **Text** `BRAIN DRAIN` t-display **hero halate** @415.53 · `third world` t-label @416.97 · `leave` t-serif-i @419.45
- **Assets** E11 world_basemap_desat_2560 (+json)
- **Camera** slow pan. **Lock** key animation done by 419.67. **Out** CA
- **SFX** 415.51 air_swell · 416.95 dot_slide

### C4S073 · 420.17–424.05 · C4B073 · PAPER
- **Words** "In fact, sometimes smart people study in their country and then leave."  **Why** "study in their country and then leave" — a diploma, then a suitcase and ticket slide over it.
- **FX** #12 still-life collage · **Ref** —
- **Visual** Paper: a 1960s diploma (real scan or typeset recreation without seals) → suitcase cut-out + airline ticket slide over it.
- **Text** `study` t-serif-i @422.33 · `leave` t-label @423.61
- **Assets** N29b diploma · N29c suitcase / airline ticket
- **Camera** push. **Lock** key animation done by 423.55. **Out** W↓
- **SFX** 422.31 paper_slide · 423.59 paper_slide · 423.95 whoosh

### C4S074 · 424.05–431.70 · C4B074 · NIGHT
- **Words** "In Taiwan, they were actually kind of like celebrating that. I don't know if they were celebrating that, but what I really mean to say is that top Taiwanese universities at the time."  **Why** "in Taiwan they were actually kind of celebrating that … top Taiwanese universities" — the NTU palm boulevard, 1960s.
- **FX** #16 plate + #14 light weave · **Ref** —
- **Visual** 1960s photo of NTU's Royal Palm Boulevard / main gate; slow push.
- **Text** `"celebrating"` t-serif-i @425.89 · `top` @429.33 `Taiwanese` @429.65 `universities` @430.37 t-label word-by-word
- **Assets** N28 NTU 1960s photo
- **Camera** push 1.0→1.06. **Lock** key animation done by 431.20. **Out** CA
- **SFX** 425.87 air_swell

### C4S075 · 431.70–435.46 · C4B075 · PAPER
- **Words** "Their recruiting slogan was basically leaning into the trend."  **Why** "their recruiting slogan was basically leaning into the trend" — a vintage felt pennant + recruiting flyer.
- **FX** #16 cut-outs + #13 text fill · **Ref** new ref: "vintage college pennant / recruiting brochure" (Pinterest ephemera)
- **Visual** Paper; felt pennant (celadon) and a typeset recruiting flyer slide in at 12 fps.
- **Text** `RECRUITING` @432.02 `SLOGAN` @432.58 t-label
- **Assets** own pennant SVG (felt texture) · typeset flyer
- **Camera** push. **Lock** key animation done by 434.96. **Out** cont. — the camera pans onto the newspaper page
- **SFX** 432.00 paper_slide

### C4S076 · 435.46–440.90 · C4B076 · PAPER
- **Words** "One of the slogan was come come to NTU, which is the National Taiwan University."  **Why** the quoted slogan "come come to NTU, National Taiwan University" — painting-to-print: a colour NTU campus image revealed as a picture in a newspaper column; the pull-quote is underlined word by word.
- **FX** §10.7 painting-to-print + pen underline per word · **Ref** Lincoln reel (§10.7) VARIATION
- **Visual** Full-frame colour 1960s NTU campus postcard; eased 1.2 s pull-back + upward pan reveals it printed in a typeset newspaper column (Crimson Pro, sepia, halftone); caption 'NATIONAL TAIWAN UNIVERSITY'; bold serif pull-quote underlined word by word.
- **Text** pull-quote `Come,` @436.50 `come` @436.82 `to` @437.38 `NTU` @437.78 · caption `National Taiwan University` @439.22
- **Assets** N28d colour NTU postcard
- **Camera** pull-back + pan up (cam ease). **Lock** key animation done by 440.40. **Out** cont.
- **SFX** 436.48 marker_scratch ×4 (pen underline) · 435.50 paper_rustle

### C4S077 · 440.90–444.18 · C4B077 · PAPER
- **Words** "And the second part of the slogan goes, Go go go to America."  **Why** "Go go go to America" — the second half of the slogan, the next pull-quote line on the same page.
- **FX** §10.7 continued + pen underline · **Ref** §10.7 VARIATION
- **Visual** Camera slides down the column: second pull-quote line; a small 1960s airliner photo in the next column.
- **Text** `Go,` @442.58 `go,` @442.82 `go` @443.14 `to` @443.30 `America` @443.54
- **Assets** E20 jfk_1981_panam747 (or a 1960s airliner photo)
- **Camera** slide down. **Lock** key animation done by 443.68. **Out** W→
- **SFX** 442.56 marker_scratch ×4 · 444.10 whoosh

### C4S078 · 444.18–450.66 · C4B078 · NIGHT
- **Words** "So they were kind of telling people, hey, you come here, it's a good university, and then you can go to the United States, get a higher paying job."  **Why** "come here, good university, then go to the United States, get a higher paying job" — a yellow marker route from Taipei across a dark Pacific.
- **FX** #3 map + R10 route · **Ref** R10 VARIATION on night (dark Pacific relief, glowing yellow route, pins)
- **Visual** Dark Pacific relief: pin at Taipei @446.82; yellow rough marker route across the ocean to the US west coast @448.26; label-box at the end.
- **Text** `good university` t-serif-i @446.82 · `United States` t-label @448.26 · `HIGHER-PAYING JOB` .label-box @449.46
- **Assets** E12 pacific_relief_grey (+json)
- **Camera** track east with the route; `FH` focus hunt when the move lands. **Lock** key animation done by 450.16. **Out** CA — camera keeps tracking
- **SFX** 446.80 map_pin · 448.24 marker_long · 449.44 pop_soft

### C4S079 · 450.66–457.78 · C4B079 · NIGHT
- **Words** "Now, in the future, this does reverse. And a lot of people say it reversed because these people just loved Taiwan and they came back."  **Why** "this does reverse … people loved Taiwan and they came back" — the route runs back west.
- **FX** #3 map + R10 route reversed · **Ref** R10 VARIATION
- **Visual** Same map; a second route draws back from the US to Taiwan; heart-shaped pen doodle near Taiwan.
- **Text** `REVERSE` t-label @452.58 · `"loved Taiwan"` t-serif-i @455.86 · `came back` @457.06
- **Assets** E12
- **Camera** track west. **Lock** key animation done by 457.28. **Out** FW
- **SFX** 452.56 marker_long · 457.70 whoosh

### C4S080 · 457.78–461.54 · C4B080 · PAPER
- **Words** "That's not actually true. That's just not how human mind works, right?"  **Why** "That's not actually true … not how human mind works, right?" — the 'loved Taiwan' quote card is crossed out.
- **FX** §10.6.2 pen cross + #13 · **Ref** —
- **Visual** Paper; a small typeset quote card '"they loved Taiwan"' (the claim he paraphrases, on screen only his words 'loved Taiwan'); a pen cross draws over it on "true".
- **Text** card `"loved Taiwan"` (carried from C4S079) · `NOT` @458.10 `TRUE` @458.58 t-display · `human mind` t-serif-i @459.86
- **Assets** own
- **Camera** static, 2 % push. **Lock** key animation done by 461.04. **Out** cont. — the camera tilts down the same sheet onto ruled lines
- **SFX** 458.56 pencil_scribble

### C4S081 · 461.54–465.94 · C4B081 · GRID
- **Words** "Because if they truly love Taiwan, they would not have left. Let's just be honest, right?"  **Why** "if they truly love Taiwan, they would not have left" — a hand-drawn logic arrow on ruled paper.
- **FX** §10.6.2 pen arrow + circle · **Ref** Pinterest idea: "hand-drawn logic diagram in a notebook"
- **Visual** Ruled notebook paper (two layers): 'love Taiwan' → pen arrow → 'would not have left', with 'left' circled.
- **Text** `love` t-serif-i @462.58 · `LEFT` t-display @463.94
- **Assets** E16 paper_lined_01_hires
- **Camera** static. **Lock** key animation done by 465.44. **Out** W↓
- **SFX** 462.56 marker_scratch · 463.92 marker_scratch · 465.85 whoosh

### C4S082 · 465.94–473.78 · C4B082 · NIGHT
- **Words** "The government implements an incentive structure that makes it just attractive for smart people to come back, especially people who are in the technological sector."  **Why** "the government implements an incentive structure … smart people to come back, especially … technological sector" — icons pulled back to Taiwan.
- **FX** #2 pictogram flow + #3 map · **Ref** new ref: "Vox magnet-pull infographic" (a magnet drawing particles)
- **Visual** Night; Taiwan relief (celadon) on the left; graduate icons stream from the right edge back toward it at 12 fps; on "technological" each icon flips into a chip icon.
- **Text** `INCENTIVE STRUCTURE` t-label @467.54 · `come back` t-serif-i @470.82 · `technological sector` t-label @472.50
- **Assets** E10 + E24 icons + own chip icon
- **Camera** slow pull-back. **Lock** key animation done by 473.28. **Out** CA
- **SFX** 467.52 tone_blip · 470.80 dot_slide · 472.48 tick_soft

### C4S083 · 473.78–480.18 · C4B083 · NIGHT
- **Words** "So that's something we'll talk about in a second. A lot of people say, Oh, this was just patriotism or this was just love for the land and they came back."  **Why** "a lot of people say, oh, this was just patriotism or love for the land" — the claims pinned on a cork board.
- **FX** R9 cork board + lamp pool · **Ref** R9 VARIATION (claims instead of people; one string)
- **Visual** Cork board under a lamp; two handwritten note cards pinned on their words; a red-free (ink) string between them; the C4S082 'later' tab pinned in the corner ("we'll talk about in a second").
- **Text** note `PATRIOTISM` @476.82 · note `love for the land` @478.18
- **Assets** E22 cork_01.jpg (CC BY — credit)
- **Camera** push. **Lock** key animation done by 479.68. **Out** PS
- **SFX** 476.80 pin_pop · 478.16 pin_pop · 480.10 paper_slide

### C4S084 · 480.18–485.46 · C4B084 · PAPER
- **Words** "Not entirely true. I'm sure there were a few people who did that just for that, but not everyone."  **Why** "not entirely true … a few people … but not everyone" — a row of returnee icons; only two marked.
- **FX** #2 isotype (D03) · **Ref** D03 VARIATION (one row, highlight two)
- **Visual** Paper; a row of 20 returning-graduate icons; on "a few" two of them get a small celadon heart; on "not everyone" the rest get a grey underline.
- **Text** `not` @480.18 `entirely` @480.50 `true` @480.98 · `a few` @482.42 · `not everyone` @484.42
- **Assets** E24 icons
- **Camera** static. **Lock** key animation done by 484.96. **Out** W←
- **SFX** 482.40 pop_soft · 484.40 marker_scratch · 485.40 whoosh

## 9. Act I — Generals → engineers (485.46–535.53)
Music: very low martial texture under Chiang 500–514; clean pulse from 'technocratic' 520.65.

### C4S085 · 485.46–492.01 · C4B085 · NIGHT
- **Words** "Another thing to talk about Taiwan politically speaking is that when the government came over."  **Why** "another thing politically … when the government came over" — 1949–50 arrival of the ROC government.
- **FX** #1 footage + #14 · **Ref** —
- **Visual** Archival 1949–50 photo/footage of ROC officials/troops arriving in Taiwan (or the 1960 Presidential Office footage, a different section from C4S039).
- **Text** `politically` t-label @487.86 · `government` @490.33 `came` @490.89 `over` @491.29 t-serif-i word-by-word
- **Assets** N30e 1949 government arrival photo / E01
- **Camera** push. **Lock** key animation done by 491.51. **Out** CA
- **SFX** 485.50 projector_loop (6 s)

### C4S086 · 492.01–500.01 · C4B086 · PAPER
- **Words** "A lot of the leaders were all Chinese leaders who were running this island of Taiwan while they were Taiwanese elites in the country."  **Why** "a lot of the leaders were all Chinese leaders … while there were Taiwanese elites" — two bars topped with portrait circles: who ran the island.
- **FX** #2 D02 VARIATION · **Ref** D02 VARIATION (two bars topped with group-portrait circles; shapes only)
- **Visual** Paper; two bars rise at 12 fps, topped with circle crops from a 1950s cabinet photo (mainland leaders, tall bar) and a 1950s Taiwanese gentry photo (short bar); no numbers.
- **Text** `CHINESE LEADERS` t-label @494.33 · `Taiwanese elites` t-label @498.17
- **Assets** N30b 1950s ROC cabinet photo · N30f Taiwanese gentry photo
- **Camera** static, slow push. **Lock** key animation done by 499.51. **Out** W↑
- **SFX** 494.31 dot_ticks · 498.15 dot_ticks · 499.95 whoosh

### C4S087 · 500.01–505.77 · C4B087 · NIGHT
- **Words** "And a lot of these leaders were also like military people. You know generals, commanders, those people who are running,"  **Why** "military people … generals, commanders" — an archival line-up of ROC generals; pen circles on the uniforms.
- **FX** #16 plate + #19 markup circles · **Ref** —
- **Visual** 1950s photo of ROC generals; pen circles pop on two uniforms on the words.
- **Text** `MILITARY` t-label @501.61 · `generals` @502.81 · `commanders` @503.37 (t-serif-i)
- **Assets** N30c ROC generals photo
- **Camera** push 1.0→1.06. **Lock** key animation done by 505.27. **Out** CA — the push continues into the 2.5D portrait
- **SFX** 502.79 marker_scratch · 503.35 marker_scratch

### C4S088 · 505.77–509.29 · C4B088 · NIGHT
- **Words** "including the main guy, leader, Chiang Kai-shek."  **Why** "including the main guy, leader, Chiang Kai-shek" — a 2.5D uniform portrait of Chiang Kai-shek.
- **FX** #17 2.5D no.3 + #4 hero · **Ref** 2.5D VARIATION (portrait: backdrop, body, cap/face, foreground haze; title tucked behind his shoulder)
- **Visual** Chiang Kai-shek uniform portrait cut into layers; dolly in; title behind the shoulder.
- **Text** `CHIANG` @507.37 `KAI-SHEK` @508.09 t-display **hero halate**
- **Assets** N30 Chiang Kai-shek portrait ≥ 3000 px
- **Camera** 2.5D dolly; `FH` focus hunt when the move lands. **Lock** key animation done by 508.79. **Out** FW
- **SFX** 507.35 boom_low (soft) · 509.20 whoosh

### C4S089 · 509.29–514.25 · C4B089 · PAPER
- **Words** "Very cool name, and he's a general guy. Very good general, but he's a military guy nonetheless."  **Why** "very good general, but he's a military guy nonetheless" — a real magazine cover of Chiang in uniform on a desk.
- **FX** #5 document/magazine on a desk + #16 · **Ref** —
- **Visual** A real period magazine cover of Chiang Kai-shek (TIME-style, fair use, credited) lies on paper; camera pushes to the uniform; pen underline under his insignia @512.57.
- **Text** `general` t-serif-i @510.49 · `MILITARY` @512.57 `GUY` @513.05 t-label
- **Assets** N30d magazine cover (fair use)
- **Camera** push 1.0→1.1. **Lock** key animation done by 513.75. **Out** CA
- **SFX** 510.47 paper_slide · 512.55 marker_scratch

### C4S090 · 514.25–523.05 · C4B090 · GRID
- **Words** "That slowly starts fading away in like 15, 2, and slowly more technocratic people start running the country"  **Why** "that slowly starts fading away … more technocratic people start running the country" — general icons fade, engineer icons replace them.
- **FX** #2 isotype (D03) · **Ref** D03 VARIATION (replacement animation)
- **Visual** Graph paper; a row of peaked-cap pictograms; one by one they fade at 12 fps and are replaced by hard-hat/slide-rule pictograms. No years on screen (unclear ASR '15, 2').
- **Text** `fading away` t-serif-i @515.85 · `TECHNOCRATIC` t-label @520.65
- **Assets** own pictograms
- **Camera** static. **Lock** key animation done by 522.55. **Out** W→
- **SFX** 515.83 dot_ticks (2 s) · 520.63 pop_soft · 522.95 whoosh

### C4S091 · 523.05–527.21 · C4B091 · NIGHT
- **Words** "that we'll talk about more specifically, more engineers start running the country."  **Why** "more engineers start running the country" — archival 1960s engineers at drafting tables / dam site.
- **FX** #16 plate + #14 + #4 hero · **Ref** —
- **Visual** 1960s Taiwan engineers (unnamed) at drafting tables or at the Shihmen Dam site; slow push.
- **Text** `ENGINEERS` t-display **hero halate** @525.45
- **Assets** N31 1960s Taiwanese engineers photo
- **Camera** push. **Lock** key animation done by 526.71. **Out** PS
- **SFX** 525.43 air_swell

### C4S092 · 527.21–532.49 · C4B092 · PAPER
- **Words** "So that plays a big role because engineers clearly think differently than generals."  **Why** "engineers clearly think differently than generals" — split sheet: blueprint vs military map.
- **FX** #12 two-paper split + §10.6.2 · **Ref** Pinterest idea: "split-screen paper comparison (blueprint | war map)"
- **Visual** Left half paper_blueprint_01 with an engineering drawing (gears); right half a military staff map with arrows; a pen line splits them.
- **Text** `engineers` t-label @529.13 · `differently` t-serif-i @530.57 · `GENERALS` t-label @531.77
- **Assets** E16 paper_blueprint_01_hires · N36b old map
- **Camera** static. **Lock** key animation done by 531.99. **Out** cont.
- **SFX** 529.11 paper_slide · 531.75 paper_slide

### C4S093 · 532.49–535.53 · C4B093 · PAPER
- **Words** "And engineers think a lot more about the economy."  **Why** "engineers think a lot more about the economy" — the blueprint's gear drawing turns into a rising economy line.
- **FX** #2 line + morph · **Ref** —
- **Visual** Camera slides onto the blueprint half; the gear drawing's outline morphs into a rising bone line (shape only).
- **Text** `THE ECONOMY` t-label @534.97
- **Assets** E16 blueprint
- **Camera** slide left. **Lock** key animation done by 535.03. **Out** W↓
- **SFX** 534.95 tick_soft · 535.45 whoosh

## 10. Act J — Special economic zones (535.53–601.44)
Music: layers build from 540.09; groove on the import→export loop; open ending into c5.

### C4S094 · 535.53–540.09 · C4B094 · NIGHT
- **Words** "By the late 60s we are already seeing like the effect of this."  **Why** "by the late 60s we are already seeing the effect" — title over 1960 Taipei footage.
- **FX** #13 odometer + #8 streaks + #4 hero · **Ref** s01 VARIATION
- **Visual** Taipei North Gate traffic footage (1960), darkened; streaks; title rolls in.
- **Text** `LATE 60s` t-display **hero halate** @535.77 (odometer on '60s') · `effect` t-serif-i @538.97
- **Assets** E02 taiwan_1960_taipei_north_gate_traffic.mp4
- **Camera** push. **Lock** key animation done by 539.59. **Out** CA
- **SFX** 535.75 odometer_tick

### C4S095 · 540.09–547.66 · C4B095 · NIGHT
- **Words** "Taiwan is one of the first countries in Asia to set up a special economic zone that lot of countries in Asia now celebrate"  **Why** "Taiwan is one of the first countries in Asia to set up a special economic zone … countries in Asia now celebrate" — Asia map, Taiwan rings first, others follow.
- **FX** #3 map + §10.6.7 radio waves + #20 · **Ref** R12 VARIATION (relief, one region + rings)
- **Visual** Map kit Asia dark relief; Taiwan celadon with rings @543.53; later small neutral pings in other Asian countries @546.73 (shape only).
- **Text** `first` t-label @541.29 · `SPECIAL ECONOMIC ZONE` t-label @543.53 · `celebrate` t-serif-i @546.73
- **Assets** N36 Asia relief
- **Camera** slow pull-back. **Lock** key animation done by 547.16. **Out** PS
- **SFX** 543.51 tone_blip · 546.71 dot_ticks

### C4S096 · 547.66–554.70 · C4B096 · PAPER
- **Words** "And set up, including China itself. Taiwan was ahead of China too, but unfortunately people probably don't know a lot about Taiwan because China is just so much bigger."  **Why** "including China itself. Taiwan was ahead of China … China is just so much bigger" — two timeline markers, then China's block swells.
- **FX** #2 timeline + #16 photo · **Ref** R7 VARIATION (two markers on one axis)
- **Visual** Paper; a timeline: celadon marker 'Taiwan' first, red marker 'China' later with a real early Shenzhen SEZ billboard photo card; on "so much bigger" the red block scales up.
- **Text** `China` red label @548.62 · `AHEAD` @549.82 `OF` @550.06 `CHINA` @550.14 · `so much bigger` t-serif-i @554.06
- **Assets** N33 early Shenzhen SEZ photo
- **Camera** static. **Lock** key animation done by 554.20. **Out** W← whip left
- **SFX** 548.60 paper_slide · 549.80 pop_soft · 554.04 whoosh_soft

### C4S097 · 554.70–560.70 · C4B097 · GRID
- **Words** "So if they copy a strategy from a different country, they're just gonna have a bigger impact. You know, they're gonna have a bigger success."  **Why** "they're just gonna have a bigger impact … a bigger success" — two bars, a halftone skyline at the base.
- **FX** #2 bars (D01) + halftone cut-out · **Ref** D01 / R1 VARIATION (bars + dashed threshold + halftone skyline at the base)
- **Visual** Graph paper; small celadon bar and a towering red bar with watercolour tops; halftone Shenzhen skyline cut-out across the base; dashed line at the small bar's height.
- **Text** `bigger impact` t-serif-i @558.14 · `BIGGER SUCCESS` .label-box @559.66
- **Assets** N33b Shenzhen skyline photo (halftone cut-out)
- **Camera** static, punch-in at the end. **Lock** key animation done by 560.20. **Out** CA (punch-in mid-move)
- **SFX** 558.12 dot_ticks · 559.64 pop_soft

### C4S098 · 560.70–564.22 · C4B098 · PAPER
- **Words** "But Taiwan sets up different type of special economic zone."  **Why** "Taiwan sets up different type of special economic zone" — an old city map of Kaohsiung, the zone site circled.
- **FX** #3 old map + #19 circle · **Ref** D09 VARIATION (old city map)
- **Visual** 1940s US Army city plan of Takao/Kaohsiung (PD), tilted slightly; pen circle around the harbour-side site of the zone.
- **Text** `DIFFERENT TYPE` t-label @562.22 · `special economic zone` t-serif-i @563.10
- **Assets** N34b Takao/Kaohsiung 1945 AMS city plan
- **Camera** push to the circle. **Lock** key animation done by 563.72. **Out** W→
- **SFX** 562.20 marker_scratch · 564.15 whoosh

### C4S099 · 564.22–569.42 · C4B099 · NIGHT
- **Words** "One of them is like export processing zones where companies can set up factories and then"  **Why** "export processing zones where companies can set up factories" — the real export processing zone, in 2.5D.
- **FX** #17 2.5D no.4 + #4 hero · **Ref** 2.5D VARIATION (factory hall: backdrop, assembly rows, foreground workers)
- **Visual** Real 1960s photo of the Kaohsiung Export Processing Zone factory floor cut into layers (or E09 Nanzih EPZ factory photo); dolly.
- **Text** `EXPORT` @565.18 `PROCESSING` @565.82 `ZONES` @566.46 t-display **hero halate** · `factories` t-label @568.22
- **Assets** N32 EPZ factory photo ≥ 3000 px / E09 nanzih_epz_ose_factory.jpg
- **Camera** 2.5D dolly; `FH` focus hunt when the move lands. **Lock** key animation done by 568.92. **Out** PS
- **SFX** 565.16 boom_low (soft) · 568.20 air_swell

### C4S100 · 569.42–575.42 · C4B100 · PAPER
- **Words** "they can import whatever they want and they have to pay no tariffs and they can build the final product and export it."  **Why** "import whatever they want … no tariffs … build the final product and export it" — a customs flow diagram.
- **FX** #2 flow diagram + #19 arrows + stamp · **Ref** new ref: "Vox customs / tariff flow explainer" (crates → gate → factory → ship)
- **Visual** Paper; dashed zone border; crates enter @569.74; a tariff gate lifts and a 'tariff' stamp is crossed out @572.14; crates become a boxed product @573.90; a ship cut-out leaves @574.70.
- **Text** `IMPORT` @569.74 · `NO TARIFFS` @572.14 · `final product` t-serif-i @573.90 · `EXPORT` @574.70
- **Assets** own SVG + N35 1960s cargo ship cut-out
- **Camera** pan right with the flow. **Lock** key animation done by 574.92. **Out** cont.
- **SFX** 569.72 paper_slide · 572.12 stamp_thud · 574.68 whoosh_soft

### C4S101 · 575.42–582.62 · C4B101 · PAPER
- **Words** "By the way, no tariffs only if you're importing stuff to export. You know, if you're importing stuff to sell in Taiwan, that's probably a different lawsuit there."  **Why** "no tariffs only if you're importing to export … to sell in Taiwan, different" — the second path is gated.
- **FX** #2 flow + #18 highlighter · **Ref** same diagram (C4S100)
- **Visual** A second branch 'sell in Taiwan' appears; its gate stays down with an ink TARIFF stamp; the rule line is highlighted on 'only'.
- **Text** `no tariffs` t-label @575.90 · `only` highlighter @576.62 · `sell in Taiwan` t-label @580.06
- **Assets** own
- **Camera** pan down. **Lock** key animation done by 582.12. **Out** FW
- **SFX** 576.60 highlighter_swipe · 580.04 stamp_thud · 582.55 whoosh

### C4S102 · 582.62–589.58 · C4B102 · NIGHT
- **Words** "But if you're in this economic zone, you import stuff, you put it into your final product and export, there's no no tariff at all."  **Why** "in this economic zone, you import stuff, put it into your final product and export … no tariff at all" — satellite view of the zone with a looping yellow route.
- **FX** #3 satellite + D14 district highlight + yellow route · **Ref** D14 VARIATION
- **Visual** Satellite imagery of Kaohsiung harbour; the zone outlined/filled celadon; yellow rough route ship → zone → ship loops.
- **Text** `import` t-label @584.38 · `export` t-label @586.86 · `NO TARIFF` t-display @588.70
- **Assets** N34 satellite imagery Kaohsiung (Esri/Sentinel-2, credit)
- **Camera** slow push; `FH` focus hunt when the move lands. **Lock** key animation done by 589.08. **Out** W↓ whip down onto the TV
- **SFX** 584.36 marker_long · 588.68 pop_soft

### C4S103 · 589.58–596.30 · C4B103 · NIGHT
- **Words** "And the benefit for companies doing that is if they do this in Taiwan, they get access to cheap labor that Taiwan has,"  **Why** "companies get access to cheap labor that Taiwan has" — EPZ workers footage on a Tatung TV.
- **FX** #11 TV (Tatung) + #1 · **Ref** s04 VARIATION (Tatung set, Taiwanese maker)
- **Visual** Tatung TV; 1960s–70s EPZ assembly-line footage (women assembling electronics).
- **Text** `benefit` t-serif-i @589.90 · `CHEAP LABOR` t-label @594.38
- **Assets** E15 tatung_tv20cge_frame · N32c EPZ assembly footage
- **Camera** push into the screen. **Lock** key animation done by 595.80. **Out** CA
- **SFX** 589.60 crt_click · crt_hum (6 s)

### C4S104 · 596.30–601.44 · C4B104 · NIGHT
- **Words** "and in return Taiwan gets taxes, revenues, jobs, all that kind of stuff."  **Why** "in return Taiwan gets taxes, revenues, jobs, all that kind of stuff" — a dark list, each item pulled into focus.
- **FX** D12 dark list + focus pull + #13 fill · **Ref** D12 VARIATION (three items, blurred bars, focus pull per word)
- **Visual** Night; three rows each with a blurred celadon bar; the focus pulls row by row on the words; slow push out toward c5.
- **Text** `Taiwan` t-label @597.02 · `TAXES` @598.14 · `REVENUES` @598.94 · `JOBS` @599.66 (t-display, FX.text.fill)
- **Assets** own
- **Camera** slow push-out (hands into c5). **Lock** key animation done by 600.94. **Out** end of chunk — FW into c5 'made in Taiwan'
- **SFX** 598.12 tick_soft · 598.92 tick_soft · 599.64 tick_soft · 601.30 whoosh

## 11. Coverage tables

### 11.1 Effects (MANUAL §5 + §10)
| effect | scenes |
|---|---|
| #1 B-roll footage | 024, 042, 057, 085, 103 |
| #2 charts / isotype / diagrams | 002, 003, 010, 012, 018, 020, 029, 037, 046, 049, 051, 052, 055, 059, 060, 062, 071, 082, 084, 086, 090, 093, 096, 097, 100, 101 |
| #3 maps (incl. burn reveal C4S013) | 008, 013, 014, 016, 017, 022, 025, 040, 041, 043, 053, 066, 072, 078, 079, 082, 095, 098, 102 |
| #4 film-title hero | 001, 004, 023, 033, 039, 063, 072, 088, 091, 094, 099 |
| #5 documents / newspapers / magazine | 009, 011, 054, 089 |
| #8 light streaks | 033, 039, 094 |
| #10 Vox layered | 007, 030, 047, 063 |
| #11 screen / TV (scope, Tatung) | 023, 103 |
| #12 collage / pins / torn edges | 022, 028, 034, 035, 038, 058, 070, 073, 092 |
| #13 text animations (count, odometer, random, typewriter, fill) | 002, 007, 015, 019, 026, 028, 039, 044, 049, 058, 062, 075, 080, 094, 104 |
| #14 gate weave | 021, 024, 026, 030, 042, 045, 057, 074, 085, 091 |
| #15 curve cut | 004 |
| #16 hi-quality plate / posters / paintings | 001, 006, 019, 021, 027, 028, 032, 036, 037, 042, 044, 045, 050, 061, 065, 066, 067, 069, 074, 075, 087, 089, 091, 096 |
| #17 2.5D | 005, 056, 088, 099 |
| #18 rough reveal / highlighter | 003, 020, 048, 054, 068, 101 |
| #19 markups (pen circles, arrows, crosses) | 001, 003, 008, 009, 010, 014, 022, 025, 032, 033, 035, 038, 040, 041, 052, 053, 055, 061, 062, 069, 076, 077, 079, 080, 081, 087, 089, 092, 098, 100 |
| #20 map callouts | 008, 014, 040, 095 |
| §10.6.3 contrast call-out | 001, 005, 009, 014, 031, 040 |
| §10.6.4 text contrast call-out | 009 |
| §10.6.5 focal blur | 006, 064 |
| §10.6.7 radio waves | 040, 095 |
| §10.7 painting-to-print | 076, 077 |
| FH focus hunt | 004, 005, 008, 017, 040, 056, 062, 078, 088, 099, 102 |
| whips W / FW, CA, HC, PT, PS | see §11.5 (never the same twice in a row) |
| no iris | ✔ none |

### 11.2 Reference layouts
| ref | c4 scene(s) (VARIATION, never copied) | | ref | c4 scene(s) |
|---|---|---|---|---|
| D01 bars + threshold + halftone object | C4S097 (halftone skyline) | | D09 old city map | C4S098 (Takao/Kaohsiung 1945 plan) |
| D02 bars topped with portraits | C4S086 (two bars, group portraits) | | D10 tilted map + routes | C4S040 (rings), C4S041, C4S043 (routes) |
| D03 isotype grid | C4S046 (island fill), C4S071 (graduates leave), C4S084, C4S090 (replacement) | | D11 dark Sankey over ghost map | C4S049 (US → Taiwan aid flow) |
| D04 horizontal bars, serif title | C4S018 (land / people / resources) | | D12 dark list + focus pull | C4S104 (taxes, revenues, jobs) |
| D05 line chart + era band | C4S012 (votes falling) | | D13 dark line over ghost map | C4S037 (yield), C4S060 (staircase) |
| D06 parliament dots + highlighted title | C4S020 (GA hemicycle, African block) | | D14 satellite + district + yellow route | C4S102 (export zone loop) |
| D07 collage poster | C4S034–035 (Japanese infrastructure) | | D15 relationship diagram | C4S010 (seat moves), C4S051–052, C4S055 (land reform) |
| D08 telegram | C4S015 (diplomatic cable) | | | |
| R1 bars + building | C4S097 | | R7 line + era band / timeline | C4S029, C4S062, C4S096 |
| R4 ranked bars + portraits | (via D02) C4S086 | | R8 dot semicircle | C4S002–003 (horseshoe), C4S020 |
| R5 isotype | (via D03) | | R9 cork board / lamp pool | C4S011 (lamp desk), C4S038, C4S083 |
| R6 serif title, emphasis word | C4S068 | | R10 old map + yellow marker route | C4S078–079 (night variation) |
| R11 beige map, regions, leader labels | C4S013 (night), C4S016 | | R12 relief, region filled + glow | C4S008, C4S017 (China red = ref 12), C4S095 |
| 2.5D (quad / campus) | C4S005 GA hall, C4S056 factory, C4S088 Chiang Kai-shek, C4S099 export zone | | R2 / R3 | skipped (owner) |

**New reference ideas (my own search, described so editors can look them up):** (1) Vox UN explainer — archival chamber photo
with a hand-drawn boundary (C4S001); (2) top-down Security Council horseshoe seat diagram (C4S002–003); (3) newspaper stack on
a dark desk, one per year (C4S011); (4) tug-of-war infographic (C4S014); (5) vintage brass balance scale still-life (C4S019);
(6) WWII war-room table map with pins (C4S022, C4S025); (7) USGS drum seismograph read on our oscilloscope (C4S023);
(8) banknote stack still-life (C4S044); (9) before/after arrow infographic (C4S059); (10) civics-textbook object still-life
(C4S061); (11) migration flow map, glowing arcs (C4S072); (12) vintage college pennant / recruiting brochure (C4S075);
(13) hand-drawn notebook logic diagram (C4S081); (14) Vox magnet-pull infographic (C4S082); (15) split-screen paper comparison
blueprint | war map (C4S092); (16) Vox customs/tariff flow explainer (C4S100–101); (17) museum-label portrait card + mini map
(C4S066); (18) university archive scrapbook page (C4S070).

### 11.3 Face cam
None (LONGFORM: the narrator is off camera after the intro). ✔

### 11.4 Ground rhythm (N night · P paper · G grid)
```
001N 002P 003P 004N 005N 006N 007P 008N 009P 010P 011N 012G 013N 014N 015P 016P 017N 018G 019P 020P 021N 022P 023N 024N 025P 026N
027P 028N 029G 030N 031N 032P 033N 034P 035P 036N 037N 038P 039N 040N 041P 042N 043P 044N 045N 046G 047N 048P 049N 050P 051G 052G
053N 054P 055P 056N 057N 058P 059G 060N 061P 062G 063N 064N 065N 066P 067N 068P 069N 070P 071G 072N 073P 074N 075P 076P 077P 078N
079N 080P 081G 082N 083N 084P 085N 086P 087N 088N 089P 090G 091N 092P 093P 094N 095N 096P 097G 098P 099N 100P 101P 102N 103N 104N
```
Checked by script: no run of > 3 on one ground, and PAPER+GRID combined never > 3 in a row. ✔

### 11.5 Transitions in order (never the same type twice in a row; `cont.` = no cut)
CA, cont., PS, CA, W→ whip right, FW light-flash whip left, CA, W↓ vertical whip down onto the desk, CA, W← whip left, CA, W↑ whip up, cont., PS, CA, W→ whip right, CA, W↓, cont., W↑, PS, CA, FW, CA, HC, W←, CA, W↓, CA, cont., PS, FW, W→, cont., W↓, CA, W← whip left, FW light-flash whip, PT, CA, W↑ whip up, PT, W→, CA, W↓, CA, FW, CA, PS, W←, cont., FW, CA, W↑, CA, W→, PS, CA, W↓, FW, CA, W→, cont., cont., W← whip left, CA, PS, W↑, PT, CA, W→, CA, W↓, CA, cont., cont., W→, CA, FW, cont., W↓, CA, PS, W←, CA, W↑, CA, FW, CA, W→, PS, cont., W↓, CA, PS, W← whip left, CA, W→, PS, cont., FW, W↓ whip down onto the TV, CA, end of chunk. ✔

### 11.6 Palette check
Celadon = Taiwan/ROC (C4S009–010, 014, 016–018, 020–022, 025, 043, 046, 049, 053, 060, 066, 068, 076, 082, 095–097, 102, 104).
Red = CCP/PRC only (C4S007–008, 010, 014, 017–020, 022, 025, 066, 068, 096–097). Navy/blue unused. Yellow key numbers: `11`
(C4S002), `1.5 billion` (C4S049), `40 years` (C4S062); all other yellow = highlighter (VETO C4S003, seat C4S005, African
C4S020, SHARES C4S054, INCENTIVE C4S055, different C4S068, only C4S101).

### 11.7 Checks done on this plan
- No gaps: 104 scenes = 104 beats, 0.00 → 601.44. ✔  - Every text `@t` is a word start inside its scene (script). ✔
- No face cam. ✔  - Hold ≥ 0.5 s before each cut ("Lock" per scene). ✔  - ≤ 3 same ground in a row. ✔
- No transition type twice in a row. ✔  - Cohesive with the intro: same grounds (night/paper/K+E grid), same texture
  stack, same call-out vocabulary, same TVs/screens family (Tektronix scope, Tatung), same 2.5D method, same palette tokens.

## 12. Open questions (defaults in DECISIONS.md)
1. CCP = red in c4 (TSMC's red). OK, or should the CCP be dark ink and only the PRC map fill red? → default **red**, coordinate with c3/c5.
2. "in like 15, 2" (517.29–519.69) — unclear ASR; **no years shown** until Krish confirms what he said.
3. NTU slogan: show the original Chinese (來來來，來台大；去去去，去美國) as small typographic texture under his English words? → default **yes, small, decorative**.
4. Real UN draft-resolution text in C4S009: highlight the 'expel' line of a real document (its words, not ours) → **yes**.
5. Brutality (C4S030–032) and White Terror (C4S063–065): non-graphic archival only → **yes**, no bodies/executions.
6. Chiang Kai-shek appears unnamed in C4S021 (Eisenhower visit) before he is named at 507.37 → **fine** (no label on him there).

