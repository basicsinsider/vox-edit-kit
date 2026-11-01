# SEGMENTS — "Ivan" (Searching Lessons), whole video 0.00–946.92 s — the shared plan for every segment editor

Lead: this session. Owner: Krish (asleep — never wait for answers; decide sensibly and write it in your NOTES).
Read first: `project/ivan/BRIEF.md` (Krish's binding rules for this video), `CLAUDE.md`, `MANUAL.md` (ALL; §0, §4.2 gotchas,
§5, §6, §10 override older sections), `EDITOR_BRIEF.md`, then this file, then the approved examples
(`compositions/c2s02.html`, `compositions/intro02.html` for face cam). Look at `references/palette_ivan.png`.

## 0. Krish's newest notes (2026-11-01, BINDING — he called these out on the Taiwan render)
1. **Placement / layout — think like a graphic designer.** Every frame has a grid: 96 px side margins, 72 px top/bottom safe area,
   a clear focal point, deliberate alignment (left edges line up; text blocks align to the image they describe), consistent
   spacing between label and object, nothing touching the frame edge or another element, nothing covering a face or the subject
   of a photo, balanced negative space. Text never floats randomly — it is anchored to a grid line, a photo edge, or the object.
2. **On-screen text must make sense and be clean.** Show a short phrase that is a complete idea (2–5 words: "FIVE HOURS",
   "a democracy campaigner", "300 – 500 Russians"), not random single words, never half-sentences. One text idea on screen at a
   time; remove the previous one before the next. Words still = the narrator's words (no rewording), spellings corrected.
3. **Contrast — everything must be visible.** Text and graphics must read clearly against their background: light text only on a
   dark area (add a soft scrim/gradient under it if the photo is busy), ink text only on paper. Oxblood on night needs the light
   shade (`--oxblood-light`) for thin lines/text; azure on night uses `--sky`. Never dark-on-dark or mid-grey on mid-grey. Check every
   text frame in a snapshot at 100 % and fix anything you have to squint at.

## 1. Inputs (all in the repo root unless noted)
- VO master: `vo_iv.mp3` (15:46.9 = 946.92 s). It is the narrator's take CUT by the lead (EDL `project/ivan/EDL.json`); never
  process it. Word timings: **`transcript_iv.json`** (master seconds; Parakeet — ASR spellings need fixing, §4).
- The script (for meaning/spelling only; the narrator paraphrases — on-screen text follows WHAT HE SAYS): `project/ivan/script_clean.txt` lines 2–30.
- **Face cam** (Krish, clean, 1920×1080, 30 fps): `assets/facecam/ivan_facecam_master.mp4` — **aligned to master time** (frame at
  master t = face-cam media time t; black during the 3 insert slots). So a face-cam `<video>` uses `data-media-start` = the master
  second at the clip's own start. (The lead measures/fixes lip sync after the first render — don't add offsets yourself.)
- **Insert slots** (the script asks for these clips; video + their own audio): the VO is silent there and the clip plays full-frame.
  | slot | master | clip (video, muted in the composition) | what it is | audio |
  |---|---|---|---|---|
  | 1 | 108.700–116.700 (8 s) | `assets/ivan/inserts/insert1.mp4` | Guardian: St Petersburg/Moscow anti-war protest, "No to war!" chants (has a burned "No to war!" subtitle — keep it) | lead mixes `assets/audio/ivan/insert1.wav` |
  | 2 | 407.900–425.900 (18 s) | `assets/ivan/inserts/insert2.mp4` | Guardian: Moscow local resident at the Kirillov blast site (burned English subtitles — keep) | `insert2.wav` |
  | 3 | 532.917–543.917 (11 s) | `assets/ivan/inserts/insert3.mp4` | SBU drone FPV footage, Operation Spiderweb, hitting a bomber | `insert3.wav` |
  Build each slot as its own scene: the clip full-frame (lightly framed in our look is OK: thin vignette, grain — no TV frame, keep it
  readable), a 13 px credit bottom-right ("Video: The Guardian" / "Video: Security Service of Ukraine (SBU)"), enter/exit with a
  designed transition. Don't put our text over their subtitles.
- Full source videos of the inserts (more B-roll, fair use, credit): `assets/ivan/footage/raw/src_protest.mp4` (160 s, Guardian protest
  footage), `src_dubbed.mp4` (117 s, Guardian, Kirillov blast site / police / Moscow snow), `src_fast.mp4` (282 s, SBU Spiderweb compilation:
  drone FPV over bombers, trucks, fires). Contact sheets: `assets/ivan/footage/index/{protest,kirillov_scene,spiderweb_sbu}_NN.jpg`.
- **BBC World Service documentary "Shadowmen"** (76 min, the narration's main source; Krish approved short clips, fair use, credit
  "Video: BBC World Service"): `assets/ivan/footage/raw/bbc_shadowmen.mp4` (25 fps; has a BBC logo top-left and burned subtitles —
  crop/scale ≥ 1.12 to push the logo out of frame or cover it; never show its subtitles under our text). Index: contact sheets every
  6 s `assets/ivan/footage/index/bbc_NN.jpg` (timecode on each thumb) and transcript `assets/ivan/footage/index/bbc_transcript.txt`
  (search "Ivan", "Foma", "Kirillov", "airfield", "Kazakhstan", "Warsaw"…). Ivan and Foma appear ANONYMISED in it (backs, hands,
  silhouettes, AI-anonymised faces) — perfect for our "never see Ivan's face" rule. Use clips of 2–6 s, trimmed with ffmpeg into
  `assets/ivan/<seg>/footage/` (h264, ≤1080p, 24 fps, no audio), each logged in that folder's SOURCES.md with the BBC timecode.
- Motif: `assets/ivan/motifs/grey_man.svg` — "the grey man" (faceless ash head-and-shoulders) = Ivan / Foma / an anonymous Russian helper.
- Maps: `assets/maps/kit/world_{atlas,night}.jpg` (16384 px, x=(lon+180)*45.511, y=(90-lat)*45.511) and
  `world_satdesat_21600.jpg` exist now. A map agent is building an **Eastern Europe / western Russia kit** in the same style
  (`assets/maps/kit/eastern_europe_{atlas,night,sat,satdesat}.jpg` + `.json` + `_overlay.svg` + landmask, ~20–62°E × 42–62°N) and Esri
  aerials (Moscow blast sites, the Spiderweb airfields, Yelabuga/Alabuga, Kazan). Check `assets/maps/kit/README.md` for the "Eastern
  Europe" section; until it lands, build your other scenes first, and if it never lands use a crop of the world maps.

## 2. Palette — `lib/palette_ivan.css` (loaded automatically for `iv*` compositions). FOUR colours + their shades ONLY.
| colour | tokens | means |
|---|---|---|
| **Oxblood** | `--oxblood` #b32a22 (= `--vermilion`), `--oxblood-dark` #6e1914, `--oxblood-light` #e3a199 | Russia: Kremlin, Putin's government, the Russian military, FSB, bombers |
| **Azure** | `--azure` #2563b0 (= `--navy`), `--azure-dark` #163c6b, `--sky` #93bde8 | Ukraine: GUR, SBU, Ukrainian drones, Kyiv |
| **Brass** | `--brass` #f2c232 (= `--yellow`), `--brass-dark` | ONLY the highlighter and the ONE key number of a scene (and Ukraine's flag) |
| **Ash** | `--paper` `--paper-2` `--ink` `--ink-soft` `--night` `--bone` `--ash` `--ash-light` `--ash-dark` | grounds, ink, photo tints, and **Ivan / Foma / the grey zone** (never red or blue) |
Rules: no other hues (no greens, no oranges, no purples); max two accents per frame; photos desaturated/duotoned toward ash so the
accents pop (archival/news photos: ash duotone or low saturation 0.2–0.4; real colour only for the insert clips and a few hero shots).
Map fills: Russia oxblood (on night maps the overlay rule from §4.2 — fill-opacity ≈ 0.6 on dark, light shade for strokes), Ukraine azure (`--sky` on night maps).

## 3. The split (contiguous, master seconds; one editor per segment)
| seg | SEG_START | SEG_END | DUR | story (what the viewer must get) |
|---|---|---|---|---|
| ivs01 | 0.00 | 144.02 | 144.02 | Cold open: Ivan's double life, "Russian patriot"; why he helps Ukraine (Russia must lose for Putin to go); he's not alone — Russians passing info on officers, helping attacks deep inside Russia; headache for the security services; Ivan was in the opposition; Feb 2022 invasion → **insert 1** (protests) → new laws, arrests, exodus; Ivan decides losing the war is the way. |
| ivs02 | 144.02 | 296.18 | 152.16 | Polish journalist Marcin Mamoń; met Ivan a decade earlier; strange videos (explosive device for a drone; materials near a military airfield); verifying; GUR confirms; Ivan's job: find military facilities; met in Kazakhstan; filmed a strategic aviation facility in Tatarstan, east of Moscow; satellite vs a man on the ground; the 5-hour assignment, home to a "normal day", family unaware, arrests; kept taking assignments. |
| ivs03 | 296.18 | 474.57 | 178.39 | Foma in Warsaw: a network (three dozen people, inside Russia and abroad), info on facilities/officers incl. home addresses; Ukrainian intelligence turns to Foma; training a volunteer to tail an officer; 25 years in prison; why: officers looking over their shoulders; Dec 2024 Gen. Igor Kirillov killed by a bomb outside an apartment building in Moscow; Ukrainian intelligence officer confirmed to the BBC → **insert 2** → Dec 2025 Gen. Fanil Sarvarov killed by a car bomb; Foma's people tracked him; "put two and two together"; senior officers unsettled — even in Moscow someone might be watching. |
| ivs04 | 474.57 | 594.35 | 119.78 | Ukraine reaches the aircraft: bombers kept hundreds–thousands of miles away; June 2025, a few months before Sarvarov; June 1st small drones over several airfields, bombers in flames; Operation Spiderweb, SBU, 18 months of preparation; drones brought in by four cargo trucks → **insert 3** → Tu-95 / Tu-22M3 bombers that fire missiles from inside Russian airspace; no longer built; 41 aircraft claimed; US intel: at least 10 strategic bombers lost; still enough missiles — but no airfield is safe anymore. |
| ivs05 | 594.35 | 675.59 | 81.24 | Ivan had talked about attacking strategic bombers more than a year before; footage of preparations; Ukraine struck; not saying Ivan was involved — SBU ≠ GUR; extraordinary scale; Yelabuga in Tatarstan (Shahed-type drone factory) struck; new defensive towers on satellite images; Foma's theory Ivan helped plan it — unproven; Mamoń can't tell which attacks; one thing he can't understand… |
| ivs06 | 675.59 | 781.38 | 105.79 | How has Ivan never been caught? known opposition figure, leaves Russia, meets journalists abroad, returns; what if he works for Russian intelligence too?; Warsaw: exiles helping volunteers fight Putin's army — one was a Russian double agent; even Ivan's handler can't rule it out; Ivan goes silent for weeks, months; back in touch: stopped by officers, car inspection, explosives in the car, not found; no journalist could verify; the fear never went away. |
| ivs07 | 781.38 | 946.92 | 165.54 | Others go after trains: Nov 2025, Freedom of Russia disabled dozens of locomotives; railways supply the army; how many? Foma: 300–500; tiny fraction of the population; not close to overthrowing Putin; but one person / a small group can matter; uncomfortable reality — some helping Ukraine are Russians; who can you trust (both sides); will it bring change?; Ivan doesn't know; "Putin won't live forever"; what comes after Putin; they risk everything for a future they may never see. Last frame: designed ending (title "IVAN" / Searching Lessons card is NOT requested — end on the closing line's image, hold 1.5 s past the last word, fade to night). |

Boundary hand-off: each segment starts and ends on a cut-on-action or whip. The outgoing editor ends with motion; the incoming starts with
a fresh shot (no shared layouts across boundaries needed). Write your first and last scene (look + motion direction) in your NOTES.

## 4. Spellings on screen (ASR → correct) — the narrator's words otherwise
Marcin Mamoń (ASR Mamon/Mamoy/Momon/Mulmon) · Foma (Fulma/Fomar/FOMA) · Igor Kirillov (Kirilov) · Fanil Sarvarov (Saravel/Saravol/Saravod/
Soravu) · GUR — he says "GRU"; Ukraine's agency is the **GUR** (show "GUR" — Krish's rule: accurate spelling of names) · SBU · Tatarstan
(Tartastan) · Yelabuga (Yebuga) · Shahed (Sahet) · Tu-95, Tu-22M3 (ASR "Q95", "QU-22") · Operation Spiderweb · Freedom of Russia ·
Kazakhstan · Warsaw · Vladimir Putin. Numbers as spoken: "February 2022", "five hours", "three dozen", "25 years", "December 2024",
"December 2025", "June 1st", "18 months", "four cargo trucks", "41 aircraft", "at least 10 strategic bombers", "300 to 500".
Don't put text on his asides/slips ("I'm pretty sure…", "which which").

## 5. Face cam (BRIEF rule 2) — per segment budget
- ivs01: **no narrator in 0–10 s.** From 10 s to ~120 s he pops in **4–6 times for 1–2 s each**, on lines where he speaks to the viewer
  ("Now, you might be wondering…", "So, you can probably see why…", "After all, how do you stop Ukraine…", "To understand why…", "But Ivan
  started looking at things differently"). After ~120 s: normal rule.
- ivs02–ivs07: **≈35 % of the segment's time on camera** (ivs02 ≈ 53 s, ivs03 ≈ 56 s excl. insert, ivs04 ≈ 38 s excl. insert, ivs05 ≈ 28 s,
  ivs06 ≈ 37 s, ivs07 ≈ 58 s), in shots of 2–8 s, on lines where he addresses the viewer, asks a question, or makes a point ("Now, you
  might be thinking…", "Now here's where Ivan's story gets particularly interesting", "Now I want to be clear…", "What if Ivan was secretly
  working for Russian intelligence, too?", "But how do you know who you can actually trust?", the ending). Report your actual % in NOTES.
- **Vary the framing**: wide (scale 1.0), medium (1.2–1.3, reframed on his face), close (1.5–1.6) — change framing at every face-cam
  shot so the jump cuts from the trimmed take are hidden; a slow 2–3 % push inside a shot is nice. Clean & modern: **no grain, dust, film
  grade, vignette or texture on him.** Allowed on top: our clean text treatments (lower-third style labels, a key phrase beside him in
  the empty side of the frame, on a grid — check contrast against the bookshelf; use a soft dark gradient on that side if needed).
- Graphics behind him (optional, 1–2 per segment max): `npx --yes hyperframes@0.8.217 remove-background clip.mp4 -o fg.webm -b bg.webm`
  on a short pre-cut (≤4 s; ~0.7 fps on CPU, so keep it short): room plate → our graphic → narrator → text. Cut the clip first with
  ffmpeg from `ivan_facecam_master.mp4` (`-ss <master start> -t <dur>`), then the composition uses `data-media-start="0"`.
- Timed `<video>` rules from MANUAL §4.2 (id required, `data-start` = scene start, visibility by data-start/duration). The face cam
  file has keyframes every 1 s.

## 6. Creative direction (BRIEF rule 6 — "be super creative") — the house style, new variations
Genre: **geopolitical espionage documentary**. Tone: tense, intimate, investigative (not business). Visual vocabulary to draw from:
anonymised BBC shots of Ivan/Foma, Moscow/St Petersburg street & winter photos, FSB/Lubyanka, Kremlin, protest photos 2022, OVD-Info
arrest counts style, law text (Russian criminal code article on "discrediting the army"), Polish journalist's notebook, Telegram/
Signal-style message bubbles (typeset, ours — not a real app UI copy), surveillance stills (CCTV frame, timestamp, focus box), redacted
documents (black bars that wipe off word by word), case files with paper clips, passport stamps (Kazakhstan, Warsaw), maps of Russia
with distance rings from Ukraine, satellite views of airfields (Esri) with bombers circled, Tu-95/Tu-22M3 photos (Commons has many,
CC BY-SA), SBU Spiderweb footage, cargo truck/container cut-aways (2.5D), Yelabuga satellite with towers circled, Russian railway/
locomotive photos, Freedom of Russia Legion flag (white-blue-white — show it desaturated/ash if it would add off-palette colour),
chess pieces / double-agent mirror motif for "working for both sides", a phone screen going silent (message ticks, "last seen…"),
traffic-police checkpoint photos for the car inspection, Soviet/Russian propaganda posters and paintings where they match a line.
Every one of these only where it matches the exact words (MANUAL §10.1.3).
Effects (MANUAL §5/§6/§10): use the full kit across the video — whips (3 kinds), cut on action, push-throughs, maps with burns/routes/
radio rings/distance rings, 2.5D (1–2 per segment at the moments that most deserve depth), Vox layered backgrounds, collage/case-file
boards (ref 9 cork board → an investigator's wall with red string = Foma's network!), newspapers/headlines (Kirillov, Sarvarov, Spiderweb
front pages — real 2024/25 headlines are copyrighted but allowed (fair use); or the painting-to-print reveal §10.7 for the "Putin won't
live forever" quote), charts (isotype for 300–500 vs Russia's population; ranked bars; counters for 41 vs 10), text animations, contrast
call-outs, focal blur, highlighter on body text, markups on satellite images, DSLR focus hunt, gate weave on old footage only.
Reference layouts: `references/style-images/intro/D01–D15.jpg` and `references/style-images/1–12` (MANUAL §6) — use the ones that fit and
make variations; also invent new ones in the house style (describe them in your notes).
Never the same treatment twice in a row; ≤3 scenes in a row on the same ground (paper / night / face cam).
Animations finish and HOLD ≥ 0.5 s before a cut (§10.9). Glow (`.halate`) only on the one hero element of a night scene.

## 7. Files, ids, timing, checks (same conventions as project/c2/SEGMENTS.md §3 — read it)
- `compositions/ivsNN.html`, composition id `ivsNN`, root
  `<div id="root" data-composition-id="ivsNN" data-vo-start="SEG_START" data-duration="DUR" data-width="1920" data-height="1080">`.
- Temp VO for previews: `<audio id="ivsNN-vo" class="temp-vo" src="vo_iv.mp3" data-start="0" data-duration="DUR" data-media-start="SEG_START" data-volume="1">`.
  No other audio tags (insert audio + music + SFX are mixed by the lead/sound designer). All `<video>` muted.
- `const SEG="ivsNN", SEG_START=…, SEG_END=…; const T = s => +(s - SEG_START).toFixed(3); const S = T;` — every text cue a literal
  `T(<master word start>)` from `transcript_iv.json`, default −0.06 s; long lines word by word.
- Your plan first: `project/ivan/EDIT_NOTES_ivsNN.md` (scene table: id ivsNN-scNNN, start–end on word starts, exact words, why this
  picture, ground, effects, text + cue times, assets, transition, SFX). Keep it short but complete; then build.
- Assets: `assets/ivan/ivsNN/` (photos/, footage/, derived/) + `SOURCES.md` in each folder (subject, URL, licence or "© owner, fair use",
  author, date, size). Free/PD/CC preferred; copyrighted news photos/footage allowed (fair use, credit). Never log in. Look at every
  image before using it. MANUAL §8.1 for where to search (Commons via `python3 tools/find_media.py commons-html "<q>"`, archive.org,
  `tools/commons_thumb.sh`); news sites' article images may download directly (try; if a site blocks, move on).
- Sandbox: `tools/make_sandbox.sh ivsNN` → `cd work/ivsNN && python3 tools/build_index.py ivsNN --root .` → lint / snapshot there.
  Never write the root `index.html`. Snapshots compete for 4 CPU cores with 6 other editors: snapshot in batches of ≤ 8 frames.
- Checks before you report done: lint 0 errors; `python3 tools/sync_audit.py compositions/ivsNN.html --transcript transcript_iv.json`
  clean (every text cue ≤ 0 and ≥ −0.12 s); snapshots of every scene (start+0.3, middle, last 0.5 s) LOOKED AT against the words,
  Krish's three notes (§0) checked on every frame; `compositions/ivsNN.sfx.json` (SFX vocabulary in project/c2/SEGMENTS.md §3.4, master
  seconds, one hero per scene + camera moves/entrances; insert scenes get no SFX); `compositions/ivsNN.NOTES.md` (what you built, effects
  and reference layouts used, face-cam %, deviations, assets missing/substituted, anything the lead must do). Timeline duration must equal DUR.
- Don't edit `lib/fx.js`, `lib/fx.css`, palette files or other editors' files. New helpers live in your composition; report useful
  ones in NOTES (the lead promotes them to MANUAL). Add gotchas you discover to your NOTES (the lead copies them into MANUAL §4.2).
- Work steadily; aim to finish in about 2.5 hours. Scope accordingly: fewer, better scenes (≈ 4–8 s each off-camera) beat many rushed
  ones — but every second of your range is covered, no gaps.
