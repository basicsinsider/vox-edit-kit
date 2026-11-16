# SEGMENTS — "Is the chip ban actually working?" (NVIDIA / the US chip ban on China), Searching Lessons — master 0.00–2402.00 s

Lead: the NVIDIA session. Owner: Krish. Never block on questions — decide sensibly and write it in your NOTES.
Read first: `project/nvidia/BRIEF.md` (Krish's binding rules), `CLAUDE.md`, `MANUAL.md` (ALL; §0, §4.2 gotchas, §5, §6, §10 incl. §10.10
override older sections), `EDITOR_BRIEF.md`, then THIS file, your rows in `project/nvidia/EDIT_NOTES.md` (the lead's shot plan — follow it;
improve craft freely, never drop an assigned reference/motif), `project/nvidia/RESEARCH.md` (names, spellings, facts, visual leads),
`project/nvidia/MOTIFS.md` (the shared SCOREBOARD and THE LINE graphics), then the quality bar: the Paraguay edit
(`project/paraguay/SEGMENTS.md`, `EDIT_NOTES_pys0*.md`, `compositions/pys0*.html` — copy their structure, face-cam handling, map labels,
transitions) and Ivan (`project/ivan/FIXES_ROUND1.md`). Look at `references/palette_nvidia.png`.

## 0. Krish's binding design notes — check EVERY frame
1. **No narration captions** (MANUAL §0): never put Sam's spoken words on screen as captions/kickers/lower thirds. Allowed text: labels on
   maps and places, name tags, chart/graph text (titles, values, axes, legends, explanatory labels), document/newspaper/screenshot text,
   credits, the SCOREBOARD/THE LINE motif text, and the quotes marked QUOTE in EDIT_NOTES (Raimondo, Lutnick). When in doubt, no text.
2. **Placement like a graphic designer**: 96 px side margins, 72 px top/bottom; one focal point; text anchored to a grid line, photo edge
   or its object; consistent spacing; nothing touching the frame edge or another element; nothing over a face/subject.
3. **Clean, meaningful text**: short complete phrases (2–5 words); one text idea at a time; spelled right (RESEARCH.md §SPELLINGS).
4. **Contrast**: light text only on dark areas (soft scrim on busy photos), ink only on paper; thin accent lines/text on night use the
   LIGHT shade (`--volt-light`, `--red-light`, `--ice-light`). Check every text frame at 100 %.
5. **Map labels on every map**: every country/city named while the map is up (CHINA, TAIWAN, HONG KONG, SHENZHEN, SINGAPORE, MALAYSIA,
   UNITED STATES …) — Haskoy 800 caps for countries, `t-label` 22–28 px + dot for cities; constant screen size during camera moves.
   Markups on the right spot. Face-cam shot edges frame-exact (check the first 0.3 s / last 0.6 s of every face-cam shot).
6. **Accuracy** (Krish, this video): every visual matches the exact words under it; names, chips, places, years and numbers are the
   true ones (RESEARCH.md) and the numbers on screen are the ones Sam SAYS. Never a made-up headline, tweet, document or "source:" line.
   Real article/document images come from `assets/nvidia/shared/news|docs` (each has a JSON with the exact headline + bbox).
7. Animations finish and HOLD ≥ 0.5 s before a cut; cuts on action; whips (3 kinds), never the iris; glow only on the ONE hero element of
   a night scene; never the same treatment twice in a row; ≤ 3 scenes in a row on the same ground (paper / night / face cam).

## 1. Inputs (repo root unless noted)
- **VO master**: `vo_nv.mp3` (preview) — 2400.62 s = 40:01; three raw takes cut by the lead's EDL (`project/nvidia/EDL.json`). Never
  process it. Word timings: **`transcript_nv.json`** (master seconds, Parakeet — ASR spellings need fixing, see RESEARCH.md);
  readable: `project/nvidia/script_clean.txt`. There was no script: the narration is the script.
- **Face cam**: `assets/facecam/nvidia_facecam_master.mp4` — 1920×1080, 30 fps, aligned to master time (frame at master t = media time
  t). It has picture ONLY for **0.00–934.98 s (part 1) and 2267.95–2400.62 s (part 3)**; 934.98–2267.95 is BLACK (part 2 was recorded
  as audio only — Krish confirmed there is no face cam) → segments nvs10–nvs22 are edited visuals throughout, usual density, never a
  black or empty frame. If the file is missing run `bash input/nvidia_join.sh`. Sam sits centre-frame at a mic in front of a bookshelf
  (clock left, globe right); both sides of the frame are busy — text beside him needs a scrim.
- Shared assets: `assets/nvidia/shared/{people,logos,hardware,places,news,docs,footage,icons}/` (each with SOURCES.md + `_sheet.jpg`).
  Maps: `assets/maps/kit/` → README section "NVIDIA project" (southeast_asia, china, pearl_river_delta, aerials of Huaqiangbei,
  Memphis Colossus, Johor) plus the existing `east_asia_*`, `pacific_*`, `taiwan_*`, `us_*`, `world_*`, `aerial_hsinchu_park_*`.
- Krish's reference library: `references/inspo-assets/` (INDEX.md, `img/<id>.*`, contact sheets). EDIT_NOTES names the reference id for
  each scene built from one — open that image, read it for STRUCTURE, rebuild it in our style (MANUAL §6.1), never copy it.

## 2. Palette — `lib/palette_nvidia.css` (auto-loaded for `nv*` compositions). Three story colours + yellow; shades only.
| colour | tokens | means |
|---|---|---|
| **Volt** (lime green) | `--volt` #86c232 (= `--celadon`), `--volt-dark` #3f6410, `--volt-light` #c9ec8f | **The chips & NVIDIA**: GPUs, racks, servers, data centers, computing power, Jensen Huang |
| **Flag red** | `--red` #dc2f3c (= `--vermilion`), `--red-dark` #7e151e, `--red-light` #f6a4a9 | **China**: the country on maps, Huawei, Chinese AI labs/models, smuggling routes into China, the CCP |
| **Ice** (cold cyan) | `--ice` #2a9fc9 (= `--navy`), `--ice-dark` #115973, `--ice-light`/`--sky` #9fdcf0 | **Washington / America**: the ban, "the line", Commerce, Biden & Trump, US labs/models, US law |
| **Yellow** | `--yellow` #f5d033 | ONLY the highlighter and the ONE key number of a scene (and the scoreboard "?") |
| **Graphite** | `--paper` `--paper-2` `--ink` `--night` `--bone` `--ash*` | grounds, ink, photo tints; Taiwan, Malaysia, Singapore, Hong Kong etc. are neutral |
Rules: max two accents per frame; the story's pair is ice ↔ red (US vs China) with volt (the chips) moving between them. Photos desaturated /
graphite duotone so accents pop (colour only for hero shots, product shots and news footage); every fill under a texture. Map fills:
China red (night maps fill-opacity ≈ 0.5, strokes `--red-light`), US ice; chips/routes of chips volt. On paper use the DARK shades for
thin lines/text (`--volt-dark`, `--ice-dark`, `--red-dark`); lime on cream has poor contrast — never volt text on paper.

## 3. The split (contiguous, master seconds on the 24 fps grid; one editor per segment; machine-readable: `project/nvidia/segments.json`)
| seg | SEG_START | SEG_END | DUR | face cam | story (what the viewer must get) |
|---|---|---|---|---|---|
| nvs01 | 0.000 | 109.250 | 109.250 | intro pops | COLD OPEN "Is the chip ban actually working?"; the government cares — NVIDIA's CEO just stepped down over the alleged Chinese-spy affair ("we don't even know if he knew"); years since the ban, hard to judge. "Take a look at this video": banned NVIDIA GPUs in a Hong Kong mall at US prices → ferry to Shenzhen → the biggest electronics market on the planet, rooms full of GPUs → 8 cards = a server → AI company / university / maybe the military; caveat: big players need the two-ton servers — and those are moving in too (Megaspeed; Singapore, Malaysia). |
| nvs02 | 109.250 | 229.500 | 120.250 | intro pops to 162.2, then ≈35 % | What does that say about the ban? Jensen's podcast claim: China now makes 60 % of the world's chips, 17 % before the ban; Chinese models catching up, insanely cheap → TITLE QUESTION "Was the chip ban a mistake?" / why keep it. Then the overview: a US law stopping the most powerful AI chips (and the machines that make them) going to China; passed October 7th, 2022; Biden introduced it, Trump kept it — extended, rolled back, now weaker; still in place. |
| nvs03 | 229.500 | 362.292 | 132.792 | ≈35 % | Is the ban even fair? Free trade… but no one has a right to buy; China already banned Google, Facebook, YouTube; forced partnerships and trade secrets; IP theft called out by Germany, the UK, France, WTO cases; deeper: chips are like uranium (energy vs bomb → enriched uranium controlled); AI dual use; China talks about invading Taiwan. Main question: is the ban WORKING? |
| nvs04 | 362.292 | 472.667 | 110.375 | ≈35 % | Define "working": top three answers → THE SCOREBOARD (fourth row left blank). First: NVIDIA doesn't make the chips — made in Taiwan — so how does the US decide? Design is NVIDIA's intellectual property; the machines and software are American/Western; anything made with American technology falls under the rule → "every chip on the planet is under American law". |
| nvs05 | 472.667 | 559.583 | 86.917 | ≈35 % | JOB ONE: keep the chips out of China. 2022: the government draws THE LINE on a ranking of chips; it covered two chips (the two best); devastating for NVIDIA — China was a quarter of sales while demand exploded; NVIDIA quickly designs a new chip right on the line. |
| nvs06 | 559.583 | 647.042 | 87.458 | ≈35 % | A year later the administration moves the line below the new chip; NVIDIA designs another just under the new line; the Commerce Secretary: "…ban the new chip the very next day" (QUOTE); cat and mouse; even gaming chips banned (the PC aside); regulation is slow and broad — the 90s supercomputer rules that caught the PlayStation. |
| nvs07 | 647.042 | 775.250 | 128.208 | ≈40 % (personal anecdotes) | Chips still get in: individuals carry them; Facebook Marketplace ("imagine this video bombs…"); legal to sell, illegal to take, hard to police — too many people, small profit ($2,000 → $2,300–2,500 pays the ticket); the 2010s iPhone resale memory; limited government resources vs $300 profits. |
| nvs08 | 775.250 | 864.750 | 89.500 | ≈30 % | So the government goes after the big fish: a co-founder of one of the biggest US server companies arrested — ~$1.5 billion of servers to a fake Southeast Asian company passing them to China; auditors fooled with a hair dryer and swapped barcodes; the warehouse camera recorded it; Megaspeed probably similar; others in Southeast Asia. |
| nvs09 | 864.750 | 935.000 | 70.250 | ≈40 % (must END off camera) | VERDICT JOB ONE: small chips get in, big chips get in → not working (SCOREBOARD ✗). "A joke"? But if a YouTuber can find this, the government knows — two presidents keep it. Maybe the goal isn't keeping chips out — it's keeping America's LEAD in AI. |
| nvs10 | 935.000 | 1046.000 | 111.000 | none (audio only) | Why smuggling can't reach scale: training = feed the internet to chips for months; a cluster; NVIDIA's newest rack = a refrigerator, 3,000 lb like a small car, the electricity of 100 homes, liquid cooling, plumbing; a frontier lab needs thousands; one Memphis data center = 800,000 homes, more compute than everything smuggled into China; vs China's biggest: 7 %. |
| nvs11 | 1046.000 | 1174.583 | 128.583 | none | In this sense the ban works really well: US share of AI compute 60 % (2022) → ~80 %, China ~1 %. Inside China: a big AI company cut sales 80 %; ByteDance turns features off on holidays; DeepSeek went dark ~12 hours; its founder (leaked call): two years behind, 1/20 of the compute, more researchers but not enough chips. Irony: China has the electricity, the US has the chips. |
| nvs12 | 1174.583 | 1260.375 | 85.792 | none | Three ways to track the lead: chips (20× more); test scores (gap 30 points → 3); time (7–8 months, steady for three years). China prefers the test scores — and labs build models to ace the tests. |
| nvs13 | 1260.375 | 1356.292 | 95.917 | none | The US government ran its own unseen test: Chinese models good, but not as good as claimed; the gap is larger on unseen questions; the counter-argument; caveats — "I want the big picture". Shouldn't the gap be much larger with 5 % of the chips? |
| nvs14 | 1356.292 | 1445.542 | 89.250 | none | Factors nobody says aloud: smuggling — you don't admit illegal chips, especially when you sell in America; DeepSeek likely used far more NVIDIA chips than admitted. "Take a look at this chart": Chinese models upgrade right after American ones — suspicious. |
| nvs15 | 1445.542 | 1572.417 | 126.875 | none | Distillation: ask the AI how it thinks; safeguards, cat and mouse; tens of thousands of fake accounts reverse-engineer a new model and apply it to theirs; US labs complained and now share attack information (Anthropic, OpenAI, Google) → harder, shut down quicker → the gap is widening again a little. |
| nvs16 | 1572.417 | 1698.208 | 125.792 | none | SCOREBOARD: job two ✓ — one to one. JOB THREE, Jensen Huang's argument: refuse to sell and China builds its own — you create a competitor; better: everyone built on American chips and software (every AI engineer codes on NVIDIA; the keyboard analogy; switching = redoing everything). He is biased (fiduciary duty) — which doesn't make him wrong. |
| nvs17 | 1698.208 | 1822.167 | 123.958 | none | Job three = keep China hooked. NVIDIA's China share 95 % → "0 %" (technically). Who sells instead? Huawei: ~200,000 chips last year (US government), private estimates > half a million, 1.5 million expected this year. Then the Commerce Secretary: last summer a stronger chip was allowed and Howard Lutnick said on live TV: QUOTE "…so they can stay addicted to the American technology." |
| nvs18 | 1822.167 | 1893.917 | 71.750 | none | He didn't have to say it publicly: now China itself blocks NVIDIA chips — roughly 600,000 sit at a port, the CCP gives no permission. Why? What a chip company needs most is VOLUME, because volume improves YIELD (of 100 chips, how many work). |
| nvs19 | 1893.917 | 1991.333 | 97.417 | none | The chip industry was created in Texas (Texas Instruments); a good yield then: 10 %, later 30 % (100 made, 30 work); today 99-point-something at TSMC — won by taking all the volume, selling under cost, learning, reinvesting in the next factory. Volume first, then better. So Beijing forces NVIDIA out → orders to Huawei → better yield → next generation. |
| nvs20 | 1991.333 | 2103.000 | 111.667 | none | "China makes 60 % of the world's chips" (17 % before 2022) — scary? iPhone 1 vs iPhone 18: both iPhones. Count compute, not chips: China ≈ 10 % of the world's computing power. That is exactly what the CCP wants to fix: push orders to Huawei so it climbs the value chain. |
| nvs21 | 2103.000 | 2182.542 | 79.542 | none | More questions than answers: no US chips, no good Huawei chips — how are Chinese models so close? The fourth level. SCOREBOARD job three ✗ (and the Commerce Secretary isn't helping). LEVEL FOUR, the big loophole: a data center doesn't have to be next to the company using it — middle of nowhere… stretch that really far. |
| nvs22 | 2182.542 | 2267.958 | 85.417 | none | Malaysia: data centers with the most powerful chips, rented by Chinese companies (someone legal owns it — a Malaysian firm, an American firm, "maybe even the Commerce Secretary himself"); log in or fly down; legal under Malaysian, Chinese, even US law — the renting loophole was never closed; renting is big business: about as much compute rented abroad as China has at home. |
| nvs23 | 2267.958 | 2402.000 | 134.042 | ≈40 % + sign-off on camera | Funniest part: Chinese law keeps citizens' data in the country → employees FLY to Malaysia with the data, train there, bring the model back, run it on weaker chips. The debate: keep the loophole (starves Huawei of orders; the US can switch the data centers off in a Taiwan war) or close it. SCOREBOARD row 4 "?": "I don't know how to rank this part". Comment below; "My name is Sam, I'll see you in the next video." Designed ending: hold 1.5 s past the last word (ends 2400.44), fade to night by 2402.00. |

Boundary hand-off: each segment starts with a fresh shot and ends on a cut-on-action or whip; write your first and last scene in NOTES.
nvs09's last shot and nvs10's first are B-roll (the face cam ends at 934.98); nvs22 ends on B-roll, nvs23 may open on B-roll or on Sam
(picture exists from 2267.96).

## 4. Spellings and numbers on screen — `project/nvidia/RESEARCH.md` is the authority (SPELLINGS + NUMBERS tables)
ASR → correct: "Jin Sun Huang / Jen Senhuang / Jensen Huan" → **Jensen Huang** · "Mega Speed" → **Megaspeed** · "Deep Seek" → **DeepSeek** ·
"Byte Dance" → **ByteDance** · "Enthropic" → **Anthropic** · "Lutnik" → **Howard Lutnick** · "cars" (49–73 s) = **cards** (graphics cards) ·
NVIDIA is written **NVIDIA** · Huawei · TSMC · Texas Instruments · Shenzhen · Hong Kong · Huaqiangbei · Malaysia · Singapore.
Numbers exactly as spoken (no "corrections", no invented source lines): 60 % / 17 % (chips made in China), October 7th 2022, "a quarter of
their sales", two tons, 8 cards, $2,000 → $2,300–$2,500, $300, ~$1.5 billion, 3,000 pounds, 100 homes, thousands of racks, 800,000 homes,
7 %, 60 % → ~80 % (US compute), ~1 % (China), 80 % cut, 12 hours, two years behind, one twentieth, 20×, 30 points → 3 points, 7–8 months,
5 %, tens of thousands of fake accounts, 95 % → 0 %, 200,000 / half a million / 1.5 million (Huawei chips), 600,000 chips at a port,
yield 10 % → 30 % → "99.3, .5, .7 %", iPhone 1 vs iPhone 18, 10 % of computing power. If RESEARCH.md notes that the public record differs
from what Sam says, show Sam's number and simply leave off any source label.
Sensitive lines: the "Jensen Huang … affair with an alleged Chinese spy" story (11–25 s, 2355–2362 s, 2385 s) is shown ONLY with what
RESEARCH.md / `assets/nvidia/shared/news` actually found (real headlines). If nothing real was found for a line, keep Sam on camera or use
a neutral Jensen Huang portrait/NVIDIA treatment with no invented text — never a fabricated headline, never the word "spy" in our type
unless it is inside a real published headline. "Not that October 7th" (188 s): no visual for the aside — stay on the date graphic or Sam.

## 5. Face cam (BRIEF rule 1; MANUAL §10.5)
- nvs01: **no narrator in 0–10 s.** From 10 s to 162.2 s (end of the intro, inside nvs02) he pops in **often, 1–2 s each** (≈ 8–10 pops in
  nvs01, ≈ 4 in nvs02's first 53 s), on lines where he addresses the viewer or asks a question ("Again, we don't even know…", "Take a look
  at this video", "Now, there is a caveat", "So if the chips are already making their way into China…", "Was the chip ban a mistake?").
- nvs02 (from 162.2 s) – nvs09 and nvs23: **≈ 35 % of the time on camera** (shots of 2–8 s; ≈ 65 % edit) — when he talks to the viewer,
  asks a question, jokes or tells a personal story (the PC aside, "imagine this video bombs", the iPhone memory "I'm not saying I did it",
  "if a random YouTuber like me can find this", the sign-off). Report your actual % in NOTES.
- nvs10–nvs22: no face cam exists. Do not fake it. Keep the pacing alive instead: a new shot or a clear development every 3–6 s.
- Vary framing every face-cam shot: wide 1.0, medium 1.2–1.3, close 1.5–1.6 (transform-origin ≈ 120 px above his face so the head isn't
  cropped; he is centred) — this hides the jump cuts of the trimmed take; slow 2–3 % push inside a shot. **Clean & modern: no grain, dust,
  grade or vignette on him.** Allowed beside him: our clean chart/label text with a scrim, the compact SCOREBOARD (MOTIFS.md).
- **Cuts inside the take**: `project/nvidia/segments.json` lists each segment's EDL joins (master seconds). A face-cam shot must NOT run
  across a join with the same framing — change framing exactly at the join (punch-in/out) or cover the join with B-roll.
- Timed `<video>`: `id` required, muted, `data-start` = scene start, `data-media-start` = master second at that start, visibility by
  data-start/data-duration (MANUAL §4.2). A 30 fps face cam rendered at 24 fps needs no lip-sync offset.

## 6. Creative direction — a policy explainer told like an investigation; Paraguay/Ivan quality, new variations
Tone: curious, even-handed, a little wry (Sam's asides are funny — let the edit smile with him). Three visual worlds: the SERVER HALL
(night ground, volt glow, racks, chips, data), WASHINGTON PAPERWORK (paper ground: rules, the line, charts, documents, ice ink) and the
MAP (night/satellite maps of the Pearl River Delta, Southeast Asia, China, the Pacific; routes of chips in volt, China in red).
Recurring motifs (identical everywhere — `project/nvidia/MOTIFS.md`, `lib/nv_motifs.*`): **THE SCOREBOARD** (nvs04 intro, nvs09 ✗,
nvs16 ✓, nvs21 ✗, nvs23 ?) and **THE LINE** (nvs05, nvs06). Section title cards "JOB ONE / JOB TWO / JOB THREE / LEVEL FOUR" share one
design: reference `ast_e1ede4fafbd84a66` rebuilt (ink bar with bone Haskoy caps over a document texture + one ice and one volt block).
Charts use the narration's numbers only, built in the order he says them, counted/drawn at 12 fps, one key number in yellow.
Screens for footage: this is a 2020s story — phone, laptop, security-monitor (the warehouse camera), TV-news monitor; vintage sets only
for the past (the 1990s PlayStation/supercomputer beat, Texas Instruments 1958).
Effects: the full kit (MANUAL §5/§6/§10): maps with burns/routes/pins/labels, 2.5D (the two layer sets in `shared/hardware|places`, at
most 1 per segment), Vox layered backgrounds, collage/case-file boards, newspapers/article reveals with highlighter on body-size text,
painting-to-print for a quote, charts/isotypes/counters, text animations, contrast and text call-outs, focal blur, DSLR focus hunt,
radio-wave rings. Reference layouts: the ids in EDIT_NOTES + `references/style-images/1–12`. Reuse: never the same photo/clip more than
twice in the whole video unless the story needs it (the shared folders are used by all 23 editors — say in NOTES what you used).

## 7. Files, ids, timing, checks
- `compositions/nvsNN.html`, composition id `nvsNN`, root
  `<div id="root" data-composition-id="nvsNN" data-vo-start="SEG_START" data-duration="DUR" data-width="1920" data-height="1080">`.
- Temp VO for previews: `<audio id="nvsNN-vo" class="temp-vo" src="vo_nv.mp3" data-start="0" data-duration="DUR" data-media-start="SEG_START" data-volume="1">`.
  No other audio tags. All `<video>` muted.
- `const SEG="nvsNN", SEG_START=…, SEG_END=…; const T = s => +(s - SEG_START).toFixed(3); const S = T;` — every text cue a literal
  `T(<master word start − 0.06>)` from `transcript_nv.json`; long lines word by word. Structural cues `S()`.
- Your plan: the lead's rows in `project/nvidia/EDIT_NOTES.md` § nvsNN. Refine them into `project/nvidia/EDIT_NOTES_nvsNN.md` (same table
  as `project/paraguay/EDIT_NOTES_pys03.md`: id nvsNN-scNNN, master start–end on word starts, exact words, picture + WHY it matches the
  words, ground/effect, text + cue times, transition, SFX) before building; keep the assigned reference ids and motifs.
- Assets: shared ones first; your own finds go to `assets/nvidia/nvsNN/` (photos/, footage/, derived/) + `SOURCES.md` (subject, URL,
  licence or "© owner, fair use", author, date, size). Rules for sourcing: `project/nvidia/AGENT_COMMON.md` (openly accessible pages only;
  never log in; never fabricate). Look at every image before using it. Footage: h264 ≤ 1080p, 24 fps, no audio, 2–6 s trims.
- Sandbox: `tools/make_sandbox.sh nvsNN` → `cd work/nvsNN && python3 tools/build_index.py nvsNN --root .` → lint / snapshot there. Never
  write the root `index.html`. Many editors share 4 CPU cores: snapshot in batches of ≤ 8 frames, one batch at a time.
- Checks before done: `npx --yes hyperframes@0.8.217 lint` 0 errors; `python3 tools/sync_audit.py compositions/nvsNN.html --transcript
  transcript_nv.json` clean (every text cue ≤ 0 and ≥ −0.12 s); snapshots of every scene (start+0.3, middle, last 0.5 s) LOOKED AT against
  the words and §0; `compositions/nvsNN.sfx.json` (vocabulary: project/c2/SEGMENTS.md §3.4 + MANUAL §10.8 types; master seconds; one hero
  per scene + camera moves/entrances); `compositions/nvsNN.NOTES.md` (what you built, effects + reference ids used, face-cam %, shared
  assets used, deviations, missing assets, anything for the lead). Timeline duration must equal DUR (dump `tl.duration()`).
- Don't edit `lib/*`, palette files, `tools/*`, MANUAL.md or other editors' files. Report useful helpers / gotchas in NOTES.
- Fewer, better scenes (≈ 4–8 s each off-camera) beat many rushed ones — but every second of your range is covered, no gaps.
