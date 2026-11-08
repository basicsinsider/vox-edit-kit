# SEGMENTS — "Paraguay" (Searching Lessons), whole video 0.00–1621.87 s — the shared plan for every segment editor

Lead: this session. Owner: Krish. Never block on questions — decide sensibly and write it in your NOTES.
Read first: `project/paraguay/BRIEF.md` (Krish's binding rules), `CLAUDE.md`, `MANUAL.md` (ALL; §0, §4.2 gotchas, §5, §6, §10 incl.
§10.10 override older sections), `EDITOR_BRIEF.md`, then THIS file, `project/paraguay/DECISIONS.md`, `project/paraguay/RESEARCH.md`
(names, spellings, facts, photo leads — written by the research agent; may still be growing when you start), then the quality bar:
the Ivan edit (`project/ivan/SEGMENTS.md`, `project/ivan/EDIT_NOTES_ivs0*.md`, `project/ivan/FIXES_ROUND1.md`, `compositions/ivs0*.html`
— copy their structure, face-cam handling, map labels, transitions). Look at `references/palette_paraguay.png`.

## 0. Krish's binding design notes (MANUAL §10.10 + Ivan fix round 1) — check EVERY frame
1. **Placement like a graphic designer**: 96 px side margins, 72 px top/bottom; one focal point; text anchored to a grid line, photo edge
   or the object; consistent spacing; nothing touching the frame edge or another element; nothing over a face/subject.
2. **Clean, meaningful text**: short complete phrases (2–5 words) in the narrator's own words; one text idea at a time; no stray words.
3. **Contrast**: light text only on dark areas (soft scrim on busy photos), ink only on paper; thin accent lines/text on night use the
   LIGHT shade (`--tierra-light`, `--ueno-light`, `--plum-light`). Check every text frame at 100 %.
4. **Map labels on every map** (Ivan FIXES §1): PARAGUAY on every map where it's visible, plus every place named while the map is up
   (Asunción, Brazil, Argentina, Bolivia, the US …) — Haskoy 800 caps for countries, `t-label` 22–28 px + dot for cities; counter-scaled
   during camera pushes. **Markups on the right spot** (circles on faces/objects they point at). **Face-cam shot edges frame-exact**
   (no reaching for the mouse, glancing at the screen, settling — check the last 0.6 s / first 0.3 s of every face-cam shot frame by frame).

## 1. Inputs (repo root unless noted)
- **VO master**: `vo_py.mp3` (preview) — 1621.87 s = 27:02. It is Krish's raw take CUT by the lead (EDL `project/paraguay/EDL.json`);
  never process it. Word timings: **`transcript_py.json`** (master seconds, Parakeet; ASR spellings need fixing — §4).
  (The script `project/paraguay/src/script.txt` is a guide only — Krish improvised; on-screen text follows WHAT HE SAYS.)
- **Face cam**: `assets/facecam/paraguay_facecam_master.mp4` — 1920×1080, 30 fps, **aligned to master time** (frame at master t = media
  time t). A face-cam `<video>` uses `data-media-start` = the master second at the clip's own start. Clean, no grade. (gitignored — it's on
  this machine; never commit it.)
- **The X clip** (Krish: "use the footage from the X link in the intro"): `assets/paraguay/shared/footage/x_congress_src.mp4` — 720×1280
  vertical, 29.2 s, a crowd at night in Asunción dragging a congressman out (best action ≈ 3–11 s of the clip; contact sheet
  `x_congress_sheet.jpg`, 1 frame/s). Post: "Paraguayans dragging politicians out of Congress as anger mounts in Paraguay" — Truthseeker
  (@xx17965797n) on X, 6 Nov 2026. Its own audio (`x_congress_audio.wav`) is for the sound designer (crowd under the cold open), never in a
  composition.
- Research + shared assets: `project/paraguay/RESEARCH.md`, `assets/paraguay/shared/{photos,footage,logos,docs,maps}/` (+ SOURCES.md).
  Map kit for this story: `assets/maps/kit/` → see README "South America / Paraguay" section (being built by the map agent).

## 2. Palette — `lib/palette_paraguay.css` (auto-loaded for `py*` compositions). Three story colours + yellow; shades only.
| colour | tokens | means |
|---|---|---|
| **Tierra** (terracotta, Paraguay's red earth) | `--tierra` #cf5a33 (= `--vermilion`), `--tierra-dark` #7a2f18, `--tierra-light` #f1b296 | **Paraguay & its people**: the country on maps, depositors, pensioners, protesters, the crowd |
| **Ueno teal** | `--ueno` #1fa595 (= `--celadon`), `--ueno-dark` #0c5c54, `--ueno-light` #93e0d3 | **Ueno & the money machine**: the bank, its app, Grupo Vázquez, shell companies, the loans |
| **Plum** | `--plum` #7a3f8e (= `--navy`), `--plum-dark` #3e1f4c, `--plum-light`/`--sky` #cfa8dc | **Power**: President Peña, the Central Bank board, the Senate, regulators, the IMF |
| **Yellow** | `--yellow` #f3cd3a | ONLY the highlighter and the ONE key number of a scene |
| **Mate** (neutrals) | `--paper` `--paper-2` `--ink` `--night` `--bone` `--ash*` | grounds, ink, photo tints; everyone else (US banks, France, etc.) is neutral |
Rules: max two accents per frame; photos desaturated / mate duotone so accents pop (colour only for hero shots and the X clip/news footage);
every fill under a texture. Map fills: Paraguay tierra (night maps: fill-opacity ≈ 0.55, strokes in `--tierra-light`); neighbours neutral.

## 3. The split (contiguous, master seconds; one editor per segment)
| seg | SEG_START | SEG_END | DUR | story (what the viewer must get) |
|---|---|---|---|---|
| pys01 | 0.00 | 116.00 | 116.00 | COLD OPEN on the X clip ("That's a congressman in Paraguay getting dragged out by protesters"); protests spreading; the president forced to resign → rejected → house arrest; it started with one bank: **Ueno**; massive — 60 % of adults; vs 10 % of US adults at JPMorgan Chase; big four still short of 60 %; add all majors + smaller + regional ones → 60 % market share; imagine all collapsing in one day; that's Paraguay; but not the true scale: individual accounts insured (like the FDIC) → 97 % made whole; but individual accounts only ~30 % of the money; the rest = corporations + government incl. the National Pension Fund; what happens to the pension money / where did the money go; "let's look at exactly how we got here". |
| pys02 | 116.00 | 213.60 | 97.60 | Paraguay in 2026: the World Cup run (in the US); the politician's tweet after losing to France ("not gonna read this tweet"), called racist → "I didn't even mention this guy's skin color"; not the only global story; a boring success story in South America: 2024 investment-grade rating, first time in its history; $350 million in bonds on Wall Street for infrastructure; trusted by world investors, economy growing; strongest first half in history; but one bad news: one of the biggest banks was hiding a lot of its problems. |
| pys03 | 213.60 | 332.60 | 119.00 | Background: "born in 1950 — I'm just kidding"; an old, profitable company that wasn't technically a bank: loans at high interest (a bit of loan sharking), called "Credit Central"; no deposits without a licence; 2015 a new family member takes over: build a national conglomerate (Grupo Vázquez), buy/start businesses, diversify like Asian/South American/Middle East family groups; new businesses lose money for years — fine while the old one makes money… "you're seeing where the problem starts". |
| pys04 | 332.60 | 457.40 | 124.80 | 2020/COVID: tired of not taking deposits; 2021 merges with a struggling licensed bank → **Ueno** (modern fintech: apps, websites, online banking); big hit, accounts pouring in; crazy promos: 50 % back on card spending for new customers (limits: no private jet/car/house), daily necessities (groceries, gas); low-income people; many opened their first-ever bank account (positive, but a problem later); a few years later it buys a bank four times bigger — "how the hell do you buy something four times bigger than you?" |
| pys05 | 457.40 | 595.60 | 138.20 | The secret weapon: political capital. 2019–2020 Credit Central took outside investors; one = the then finance minister, who became president in 2023 (Peña says he was never directly involved) — any company benefits when the president is an investor; 2023: the bank's CEO picked to head the Central Bank — resigns, next day joins the regulator; so they could buy a bank four times bigger (struggling); the acquisition went wrong: an online bank suddenly with branches/people/real estate costs; the bought bank had burned its cash — bigger and in a worse position. |
| pys06 | 595.60 | 706.20 | 110.60 | Luckily for Ueno: political capital → real cash: after Peña took office, deposits from government agencies, incl. IPS (pensions); pension-fund laws: max 10 % of the fund in one bank → law changed → Ueno gets ~30 % of the entire pension money; a 2nd condition (only super-safe banks) set aside; eyebrows raised two years ago, protests, "looks sketchy" — president an investor, government money flowing in. |
| pys07 | 706.20 | 798.00 | 91.80 | Hindsight: the president sold his stake only in March 2025, ~2 years into office — a conflict of interest; capital-ratio rule (equity/debt ≥ 12 %: cash + short-term assets ≥ 12 % of loans); Ueno reported 15 % and bad loans of just 0.58 % — "suspiciously good"; a normal healthy South American bank: 2–4 %; "too good to be true — and guess what? It was." |
| pys08 | 798.00 | 940.60 | 142.60 | Back to the conglomerate: the group's money-losing businesses (media, tech, software…) had big loans from the bank; legal only up to 20 % (self-dealing); a big problem as they struggle; "owe a million — your problem; owe a billion — the bank's problem"; the bank can't let them fail but can't lend more legally → illegal: shell companies owned by low-level employees, created today, tens of millions in loans tomorrow, routed to the group's companies for payroll. |
| pys09 | 940.60 | 1042.60 | 102.00 | Unpaid loans for ~60 days must be written down (tell the accountant, regulators, investors); "creative accounting" — his accounting teacher: "creative accountants go to jail"; new loans to the same companies to pay the old ones, over and over, until too big to fail; more than $300 million to companies they owned themselves — the bank lending so they could pay it back so they could borrow more: a "merry-go-round". |
| pys10 | 1042.60 | 1207.80 | 165.20 | The central bank catches on (reports ≠ reality, "this bank is lying"); two options: write the loans down (stop being a bank / government takeover) or find a buyer; "the loan was a piece of [bleep]"; a buyer of suspicious origins: a company owned by the same group, with < $100,000 cash days before; Ueno lends to shell companies → ~$79 million → the buyer pays Ueno for its own bad loans ("someone's paying us $80 million"); investigators report it to the head of the central bank — the former CEO (CEO on Aug 14, central-bank head on Aug 15, two years ago); he allegedly buries it; investigations ongoing. |
| pys11 | 1207.80 | 1294.50 | 86.70 | How it fell apart: the report's author moved out of the department; two months later the report reaches **ABC Color** (one of the oldest/biggest newspapers), which publishes and keeps investigating — everything we know comes from the media, not the government; it happened last week; political pressure on the central bank, the president, everyone; senators from Peña's own party request an investigation — "one of the biggest banks in the country". |
| pys12 | 1294.50 | 1456.50 | 162.00 | Paraguay in international finance: developing country → investors rely on the IMF assessment (lower borrowing rates, infrastructure); the IMF team visits once a year — and was in the country last week as the story broke, while the Senate pressed the central bank; burying it would look like corruption (one bad bank vs every bank / the whole government); past banking crises → a unique law: central-bank board members who know and do nothing are criminally liable — a personal disincentive to bury it. |
| pys13 | 1456.50 | 1621.87 | 165.37 | The board does the right thing (despite its head being Ueno's former CEO): unanimous vote — a bad bank, the government takes over to make depositors whole (another bank? cash payouts? unknown); the bank is done: apps stop working, no balance, no withdrawals; low-income people can't wait weeks/months → protests everywhere; regulators: ~$1,500 a month; many had no other account → chaos, uncertainty, fear; arrests: Peña tried to resign (immunity for life) → the Senate rejects it and impeaches him → no immunity, house arrest; the board head (ex-Ueno CEO) arrested, the owner arrested, ~20 others; the president's daughter (20, in the US, Columbia) posted "tax the poor" on Instagram → viral, fuel on the fire. End: designed ending on the last line's image, hold 1.5 s past the last word, fade to night. |

Boundary hand-off: each segment starts with a fresh shot and ends on a cut-on-action or whip; write your first and last scene in NOTES.

## 4. Spellings on screen (ASR → correct) — RESEARCH.md is the authority; the narrator's words otherwise
**Ueno** — the bank (ASR: Bueno, Weno, Wano, Uano, Wino, UNO, Gweno, Vienna, Yunho, "one oh", UNL; brand writes it lowercase "ueno" —
use the logo where a logo fits, "Ueno" in our type) · **Santiago Peña** (Penya) · **Grupo Vázquez / the Vázquez group** (Vasquez group) ·
the predecessor company — he says "Credit Central": show the real name from RESEARCH.md · **Carlos Carvallo** (central-bank head, ex-Ueno
CEO) · **Banco Central del Paraguay (BCP)** — he says "the central bank" · **IPS** (Instituto de Previsión Social — he says "National Security
Institute for Paraguay": show "IPS" + "pensions") · **ABC Color** · **IMF** · **JPMorgan Chase** · **FDIC** · **Visión Banco** (the bank four times
bigger — confirm in RESEARCH.md) · Paraguay / Asunción. Numbers as spoken: "60%", "10%", "97%", "30%", "2024", "$350 million", "1950" (joke),
"2015", "2021", "50%", "2023", "10%", "roughly 30%", "March 2025", "12%", "15%", "0.58%", "2 to 4%", "20%", "60 days", "$300 million",
"$100,000", "$79 million", "$80 million", "August 14th / August 15th", "$1,500". (He says "2%" for the self-dealing limit once but means
20 % — show "20%" only where he says twenty.) No text on his slips/asides.
**Bleep**: "the loan was a piece of shit" (word at 1104.58–1104.90), "its own piece of shit" (1159.43–1159.59) and "people do stupid shit" (1600.60–1600.84): Krish asked to
bleep it. The lead mutes the word in the final mix and adds a bleep; editors: give it a graphic beat (e.g. a censor bar / "#$%!" stamp
in our type over the scene, 0.4 s) and add an `sfx.json` marker `{type:"bleep", t:<word start>, dur:<word length>}`.

## 5. Face cam (BRIEF rule 3) — per-segment budget
- pys01: **no narrator in 0–10 s.** From 10 s to the end of pys01 (116 s) he pops in **often, 1–2 s each** (≈ 7–10 pops), on lines where he
  talks to the viewer ("Now imagine what would happen…", "Well, that's kinda like what happened in Paraguay", "So hopefully it's starting to
  make a little sense…", "But even this doesn't tell you the true scale…", "So now the big question…", "So let's look at exactly how we got here").
- pys02–pys13: **≈ 35 % of the segment's time on camera** (shots of 2–8 s; ≈ 65 % edit), on lines where he addresses the viewer, asks a
  question, jokes, or makes a point (e.g. the "born in 1950 — I'm just kidding" joke, "how the hell do you buy something four times bigger
  than you?", the accounting-teacher story, "allegedly…", "where the hell is all that money"). Report your actual % in NOTES.
- Vary framing every face-cam shot: wide 1.0, medium 1.2–1.3, close 1.5–1.6 (origin ≈ ~120 px above his face so the head isn't cropped) —
  this hides the jump cuts of the trimmed take; slow 2–3 % push inside a shot. **Clean & modern: no grain, dust, grade, vignette on him.**
  Allowed: our clean text beside him in the empty side of the frame (scrim if needed), graphics behind him via remove-background
  (≤ 1 per segment, ≤ 4 s pre-cut; MANUAL §10.4) — optional.
- **Cuts inside the take** (the EDL joins, `project/paraguay/edl_frames.json` → `edit_in` = master second of each join): a face-cam shot
  must NOT run across a join with the same framing (a visible jump) — change framing exactly at the join, or cover the join with B-roll.
- Timed `<video>`: `id` required, `data-start` = scene start, `data-media-start` = master second at that start, visibility by
  data-start/data-duration (MANUAL §4.2).

## 6. Creative direction — geopolitical / financial-crisis documentary, Ivan quality, new variations
Tone: urgent, investigative, a little wry (Krish's asides are funny — let the edit smile with him on the jokes, never mock the victims).
Visual vocabulary (only where it matches the exact words): the X clip + news footage of the protests and Congress (Asunción), Ueno's
logo/app/cards/branches/ads ("50% off" promos), queues at bank branches, Santiago Peña (official photos, sash, Senate), Carlos Carvallo,
the BCP building, the Senate / impeachment vote, IPS building + pensioners, ABC Color front pages/articles (real headlines; fair use,
credit), the IMF logo/mission, World Cup 2026 Paraguay (players, France match), the politician's tweet (blur it / don't read it — he says
"I'm not gonna read this tweet"), Wall Street / bond certificates, investment-grade rating stamp, US bank logos (JPMorgan Chase, BofA,
Wells Fargo, Citi …) for the 60 % comparison, FDIC sign, shell-company paperwork (typeset registrations, "created today"), a literal
merry-go-round / carousel motif for the loans, a phone app that won't load (balance "—", spinner — our own typeset UI, not a copy of
Ueno's), $1,500 cash, house arrest, the "tax the poor" Instagram post (as reported — blur faces of private people), Columbia University.
Charts (data from the narration; the script's comments give the US numbers: Chase+BofA+Wells Fargo+Citi = 39 % combined; majors: U.S. Bank,
Capital One, Goldman Sachs, PNC, Truist, TD Bank; regionals: Fifth Third, Huntington, Charles Schwab, BNY Mellon, State Street, Morgan
Stanley): 60 % isotype of Paraguay adults vs 10 % Chase; stacked bars filling to 60 %; 97 % vs 30 % split (people vs money); pie/waffle of
who owned the deposits; 10 % → 30 % pension cap broken; capital ratio gauge 12 % vs 15 %; bad loans 0.58 % vs 2–4 %; the 20 % self-dealing
line; the $300 million merry-go-round flow diagram (bank → shell co → group co → back to the bank); timeline Aug 14 → Aug 15.
Maps: South America → Paraguay (map-kit style: night relief / satellite / atlas variants), Asunción (Esri aerial: Congress, BCP, Ueno HQ,
Mburuvicha Róga), Paraguay vs the US scale, the IMF team flying in from Washington, money routes.
Effects: the full kit (MANUAL §5/§6/§10) — whips (3 kinds), cut on action, maps with burns/routes/pins/labels, 2.5D (1 per segment at the
moment that most deserves depth), Vox layered backgrounds, collage/case-file boards (shell-company web = cork board + string), newspapers
(ABC Color reveal, highlighter on body text), painting-to-print for a quote, charts/isotypes/counters, text animations, contrast and text
call-outs, focal blur, DSLR focus hunt, screens for footage (modern phones/TV news monitors fit 2026 — not vintage TVs unless the line is
about the past, e.g. "this was like decades ago"). Never the same treatment twice in a row; ≤ 3 scenes in a row on the same ground (paper /
night / face cam). Animations finish and HOLD ≥ 0.5 s before a cut. Glow only on the one hero element of a night scene.
Reference layouts: `references/style-images/1–12`, `references/style-images/intro/D01–D15.jpg`, `references/style-images/ivan/` — use what
fits, vary, and invent new ones in the house style (describe them in NOTES).

## 7. Files, ids, timing, checks
- `compositions/pysNN.html`, composition id `pysNN`, root
  `<div id="root" data-composition-id="pysNN" data-vo-start="SEG_START" data-duration="DUR" data-width="1920" data-height="1080">`.
- Temp VO for previews: `<audio id="pysNN-vo" class="temp-vo" src="vo_py.mp3" data-start="0" data-duration="DUR" data-media-start="SEG_START" data-volume="1">`.
  No other audio tags. All `<video>` muted.
- `const SEG="pysNN", SEG_START=…, SEG_END=…; const T = s => +(s - SEG_START).toFixed(3); const S = T;` — every text cue a literal
  `T(<master word start − 0.06>)` from `transcript_py.json`; long lines word by word. Structural cues `S()`.
- Plan first: `project/paraguay/EDIT_NOTES_pysNN.md` — same table as `project/ivan/EDIT_NOTES_ivs03.md` (id pysNN-scNNN, master start–end on
  word starts, exact words, picture + WHY it matches the words, ground/effect, text + cue times, transition, SFX). Then build.
- Assets: `assets/paraguay/pysNN/` (photos/, footage/, derived/) + `SOURCES.md` per folder (subject, URL, licence or "© owner, fair use",
  author, date, size). Shared finds are in `assets/paraguay/shared/`. Never log in. Look at every image before using it. Search: Commons
  (`python3 tools/find_media.py commons-html "<q>"`, `tools/commons_thumb.sh`), archive.org, news-site article images (ABC Color, Última
  Hora, La Nación (PY), Reuters/AP/AFP via news pages — fair use, credit), official sites (presidencia.gov.py, bcp.gov.py, ips.gov.py, Flickr
  of the Paraguayan presidency — often CC BY), X/Twitter videos via `curl -sS https://api.fxtwitter.com/<user>/status/<id>` (gives the
  video.twimg.com mp4 URL). YouTube is blocked from this IP. Footage: h264 ≤1080p, 24 fps, no audio, 2–6 s trims.
- Sandbox: `tools/make_sandbox.sh pysNN` → `cd work/pysNN && python3 tools/build_index.py pysNN --root .` → lint / snapshot there. Never
  write the root `index.html`. Many editors share 4 CPU cores: snapshot in batches of ≤ 8 frames.
- Checks before done: `npx --yes hyperframes@0.8.217 lint` 0 errors; `python3 tools/sync_audit.py compositions/pysNN.html --transcript
  transcript_py.json` clean (every text cue ≤ 0 and ≥ −0.12 s); snapshots of every scene (start+0.3, middle, last 0.5 s) LOOKED AT against
  the words and §0; `compositions/pysNN.sfx.json` (vocabulary: project/c2/SEGMENTS.md §3.4 + MANUAL §10.8 types; master seconds; one hero per
  scene + camera moves/entrances); `compositions/pysNN.NOTES.md` (what you built, effects + layouts used, face-cam %, deviations, missing
  assets, anything for the lead). Timeline duration must equal DUR.
- Don't edit `lib/fx.js`, `lib/fx.css`, palette files or other editors' files. Report useful helpers / gotchas in NOTES (the lead copies
  them into MANUAL).
- Fewer, better scenes (≈ 4–8 s each off-camera) beat many rushed ones — but every second of your range is covered, no gaps.
