# SEGMENTS — "US vs Cartels", Searching Lessons — master 0.000–1341.912 s (22:22), 24 fps, 1920×1080
Lead: the Cartels session (2026-11-22). Owner: Krish. Narrator: Sam. Read `project/cartels/BRIEF.md` + `AGENT_COMMON.md` first.
This file is the shared plan for the 14 segment editors; `EDIT_NOTES.md` § ctsNN is your shot plan.

## 0. Binding design notes — check EVERY frame
1. **No narration captions** (MANUAL §0): never put Sam's spoken words on screen as captions/kickers/lower thirds. Allowed text: map
   labels and places, name tags, chart/graph text (titles, values, axes, legends, explanatory labels), document/newspaper/screenshot
   text, credits and date tags (`CT.credit`, `CT.dateTag`), the motif text (THE DEAL, TARGET FILE), the title card, and lines marked
   QUOTE in EDIT_NOTES (a real published quote with name + date). When in doubt, no text.
2. **Placement like a graphic designer**: 96 px side margins, 72 px top/bottom; one focal point; text on a grid line / photo edge / its
   object; nothing touching the frame edge or another element; nothing over a face.
3. **Clean, meaningful text**: 2–5-word phrases; one text idea at a time; spelled right (RESEARCH.md §SPELLINGS — accents included:
   Sinaloa, Guasave, Beltrán Leyva, Nemesio Oseguera Cervantes, Claudia Sheinbaum, Nicolás Maduro, Guillermo Zuany, Chihuahua…).
4. **Contrast**: light text only on dark areas (soft scrim on busy photos), ink only on paper; thin lines/text on night use the LIGHT
   shades (`--ember-light`, `--steel-light`, `--olive-light`). Check every text frame at 100 %.
5. **Map labels** on every map: every country/state/city named while the map is up (MEXICO, UNITED STATES, SINALOA, SONORA, GUASAVE,
   ARIZONA, CHIHUAHUA, EL PASO, VENEZUELA, CARACAS …) — Haskoy 800 caps for countries/states, `t-label` 22–28 px + dot for cities;
   constant screen size during camera moves.
6. **Accuracy**: every visual is the TRUE thing under the exact words (right person, place, year, unit). Numbers on screen = what Sam
   says, EXCEPT the known slips listed in §4 (show the correct figure or none). Never a made-up headline, post, document or "source:"
   line. Real article/document images come from `assets/cartels/news|docs` (SOURCES.md has headline text + bboxes).
7. **No gore, ever** (BRIEF rule 3). Violence is implied: smoke, burnt-out empty vehicles, tracers in the sky, convoys, documents,
   headlines, maps, silhouettes. Never bodies, blood, wounded people, crash wreckage with people, cartel propaganda. "Killed" numbers
   are shown as chart/map text on neutral grounds. The El Mencho / influencer rumour is NOT narrated — never show it.
8. Animations finish and HOLD ≥ 0.5 s before a cut; cuts on action; whips (3 kinds), never the iris; glow only on the ONE hero element
   of a night scene; never the same treatment twice in a row; ≤ 3 scenes in a row on the same ground (paper / night / footage).

## 1. Inputs (repo root)
- **VO**: `vo_ct.mp3` (preview copy of `project/cartels/media/vo_ct.wav`) — 1341.912 s. Never process it. Word timings: **`transcript_ct.json`**
  (master seconds, Parakeet; names fixed for Zuany/Mencho/Sinaloa/Sheinbaum/Beltrán Leyvas/Guasave/Green Beret/labs/boats). Readable,
  timed: `project/cartels/script_clean.txt` (still shows a few ASR slips: "Fausidro" = Fausto Isidro, "Old Chapo"/"all Chapo in C drill" =
  El Chapo Isidro, "Barry" = bury, "plane house" = plain house). The original script is `project/cartels/script.txt` — the VO is a
  condensed improvisation of it: build what Sam SAYS.
- Shared assets (each with SOURCES.md + `_sheet.jpg`, LOOK at the sheets): `assets/cartels/footage/` (Guasave ballpark, helicopter
  tracers, burning trucks, Tapalpa aerial, arrest video, airport walk + plane boarding, Chihuahua meth lab, boat strike, Maduro in NY,
  prisoner-transfer convoy, armored convoy, Los Mochis smoke), `assets/cartels/people/` (+ `cutouts/`), `assets/cartels/places/`,
  `assets/cartels/logos/`, `assets/cartels/docs/`, `assets/cartels/news/`. Some folders may still be filling — re-list midway.
- Maps: `assets/maps/kit/README.md` → section "Cartels project" (north_america, mexico with state ids, sinaloa, chihuahua, aerials of Kuroda
  Park / Davis-Monthan AFB / Tapalpa) + existing `americas_*`, `us_*`, `world_*`. `tools/ct_maps.py` if present.
- Motifs: `lib/ct_motifs.{js,css}` (auto-loaded for `ct*`), docs `project/cartels/MOTIFS.md`, demo `compositions/ctmotif.html`:
  **CT.deal** (THE DEAL: "America finds · Mexico arrests"), **CT.file** (TARGET FILE dossier + stamps), **CT.dateTag**, **CT.credit**.
  Use them; never rebuild them by hand.
- Krish's references: `references/inspo-assets/` (INDEX.md, `img/<id>.*`). EDIT_NOTES names the reference id per scene — open it, read it
  for STRUCTURE, rebuild it in our style (MANUAL §6.1), never copy it.

## 2. Palette — `lib/palette_cartels.css` (auto-loaded for `ct*`). Swatch `references/palette_cartels.png`.
| colour | tokens | means |
|---|---|---|
| **Ember** (roadblock-fire orange) | `--ember` #ec6424 (= `--vermilion`), `--ember-dark` #8a3311, `--ember-light` #f7b48c | **The cartels**: territory, bosses' tags, roadblocks, drug routes and flows, cartel numbers |
| **Steel** (federal slate blue) | `--steel` #6f93b4 (= `--navy`), `--steel-dark` #2f4a63, `--steel-light`/`--sky` #bcd1e4 | **The United States**: White House, CIA, FBI, DEA, Treasury, the task force, drones, boat strikes, US on maps |
| **Olive** (army olive drab) | `--olive` #9a9a4e (= `--celadon`), `--olive-dark` #50512a, `--olive-light` #d3d39c | **Mexico's state**: Sheinbaum, SEDENA, Navy, National Guard, special forces, Mexico on maps when the state is meant |
| **Yellow** | `--yellow` #f4cf3d | ONLY the highlighter and the ONE key number of a scene |
| Charcoal / sand | `--night` `--paper` `--paper-2` `--ink` `--bone` `--ash*` | grounds, ink, photo tints; Venezuela, China etc. neutral |
Max two accents per frame. Photos/footage: desaturated or charcoal-duotone so accents pop; news footage may keep muted colour (fire stays
warm — it reads as ember naturally). Night map fills ≈ 0.5 opacity with light-shade strokes; on paper use DARK shades for thin lines/text.

## 3. The split (contiguous, master seconds on the 24 fps grid; `project/cartels/segments.json`)
| seg | start–end (dur) | covers (Sam's words) |
|---|---|---|
| cts01 | 0.000–68.167 (68.2) | COLD OPEN: Guasave ballpark → helicopters, burning trucks → "come for one man" → El Chapo Isidro, FBI list, $5M → caught → "with help from the United States" |
| cts02 | 68.167–158.917 (90.8) | not a one-time thing: El Mencho, April CIA raid, 70+ boats, Maduro → the question + TITLE → Fausto Isidro born 1982, Sinaloa = "Silicon Valley", 90s, teenager |
| cts03 | 158.917–264.167 (105.3) | gunman for the Beltrán Leyvas, partners of El Chapo, 2008 split + war, armed wing, 2010 Sonora ambush, survives, routes north (boat/coast/highway → Arizona), drugs, fentanyl, 2013 Treasury |
| cts04 | 264.167–358.208 (94.0) | the nickname (two stories), arrested 2011/2014/2014/2015 and walked out, charged 2012 in the US, Dec 2024 fentanyl stash (a ton of pills), Feb 2025 FBI Ten Most Wanted |
| cts05 | 358.208–450.917 (92.7) | Trump's day-one order, 8 groups → terrorist organizations, why the label matters, "armed conflict" notice to Congress (al-Qaeda), pressure on Mexico, Liberation Day/tariffs → drugs |
| cts06 | 450.917–540.417 (89.5) | 25% fentanyl tariff on Mexico, Mexico's #1 export market, Sheinbaum's call + troops, 29 prisoners flown to the US (Caro Quintero / Camarena), 26 + 37 more, prisons |
| cts07 | 540.417–651.500 (111.1) | THE DEAL (America finds, Mexico arrests), CIA spy drones, CIA vs military rules, the task force in Arizona ("Narco Hunters"), target package |
| cts08 | 651.500–768.458 (117.0) | boat strikes (Sep 2025, >70, ~250 killed), Maduro captured in Caracas → New York/Brooklyn, El Mencho = biggest catch, who gets credit (Mexico vs US, SOTU), "do more than hand off information?" |
| cts09 | 768.458–891.500 (123.0) | Chihuahua (below Texas/New Mexico, El Paso route), NYT investigation, Guillermo Zuany, visa cancelled, witnesses, why the CIA used him, visa back |
| cts10 | 891.500–976.208 (84.7) | Zuany introduces an American, training, CIA on raids blending in (state logo jackets, tablets), the safe-house raid, failed raid at a bar, tip-offs |
| cts11 | 976.208–1078.417 (102.2) | April: the big CIA operation — meth lab in the mountains, convoy of 60+, empty lab, night drive, truck off a cliff (300 ft), Zuany's instructions, scandal, Sheinbaum "no clue", resignations, AG arrested, Zuany on the run in the US |
| cts12 | 1078.417–1192.625 (114.2) | the net closing (El Pichón killed, El Sagitario arrested + flown, money people, Chuy Peñuelas killed), Trump–Sheinbaum in China (APEC), "cartels running Mexico", Friday = Revolution Day, Lobos + Murciélagos, ring round the house, arrest, plain white house |
| cts13 | 1192.625–1286.292 (93.7) | "two days ago", region goes crazy (trucks burning, roads blocked, gas station, the ballpark callback), grocery stores, clinic, Air Force plane to Mexico City, the 30-s video, ambassador Johnson's post, charged in DC since 2012, extradition, 92 sent |
| cts14 | 1286.292–1341.912 (55.6) | IS THIS WORKING? (Narcos joke) → mostly yes: weaker drugs, fewer overdose deaths, bosses caught faster, Mexico doing it → cartels not going away ($12 bn, a line for the top job) → slowed down "just a bit" — END |

## 4. Spellings, numbers and Sam's slips (RESEARCH.md is the authority)
- Names: **Fausto Isidro Meza Flores "El Chapo Isidro"** (never "Al Chapo"); **Nemesio Oseguera Cervantes "El Mencho"**; **Beltrán Leyva**;
  **Los Mazatlecos**; **Guillermo Zuany** (Zuany Portillo); **César Jáuregui Moreno**; **Ronald D. Johnson** (US ambassador); Brig. Gen.
  **Maurizio Calabrese** (task force); **Joint Interagency Task Force–Counter Cartel (JIATF-CC)**; **Rafael Caro Quintero**; **Enrique "Kiki"
  Camarena**; **Pedro Inzunza Coronel "El Pichón"**; **Pedro Inzunza Noriega "El Sagitario"**; **Jesús González Peñuelas "Chuy Peñuelas"**;
  **Germán Rolando Gálvez Meza "El Serafín"**; units **"Lobos"** (Guardia Nacional) / **"Murciélagos"** (Ejército).
- Slips — do NOT put these on screen: "100,000 troops" (cts06: show **10,000** only on the later "sending 10,000 troops"); "Liberation Day"
  is not the Mexico tariff (cts05: a Liberation-Day board image only on "Liberation Day and all the tariffs we saw"; the Mexico 25% =
  EO 14194, 1 Feb 2025); "unlike China…" (cts06: show Mexico's order only, no "only Mexico" comparison); "15 miles from the border"
  (cts07: pin Tucson / Davis-Monthan AFB, NO distance label); "the top state prosecutor" (cts09: tag "Special prosecutor, Chihuahua");
  "born in northern Sinaloa" (cts02: show the northern Sinaloa region as where he grew up / operates, no "born here" pin); "first time"
  meeting (cts12: tag "APEC · Shenzhen · 18 Nov 2026" only); "90 some" (cts13: show **92**); Sam's paraphrase of Trump's SOTU line
  (cts08: no quote marks — use the real headline/quote from news if available); "30 second" video (cts13: fine, the clip is 30.8 s).
- "Narco Hunters" is Sam's own nickname — show the official name first, then a playful "NARCO HUNTERS" tag clearly as a nickname.
- Date tags: the Guasave operation = **20 Nov 2026**; El Mencho = **22 Feb 2026**; Chihuahua crash = **19 Apr 2026**; Maduro = **Jan 2026**
  (check RESEARCH for the exact day); FTO designation **20 Feb 2025**; EO **20 Jan 2025**.

## 5. No face cam (BRIEF rule 2)
The whole video is edited visuals. Usual density (a new image/move every 3–6 s), never a black or empty frame. Sam's asides ("You guys can
figure out why in your own head", "This is just our nickname, by the way", "Narcos on Netflix") are where the edit can smile with him.

## 6. Creative direction — a true-crime investigation told like a Vox explainer
Tone: urgent cold open, then a curious, wry investigation (Sam is conversational). Three visual worlds:
- **THE NIGHT** (charcoal ground): real footage from Guasave, the arrest, convoys, smoke — framed in house style (vertical social clips in a
  phone/post frame or a blurred fill, `CT.credit` on every clip, `CT.dateTag` where it helps), film texture, light chromatic aberration.
- **THE CASE FILE** (sand paper): documents, FBI/State posters, executive orders, news pages, the TARGET FILE motif, charts, timelines,
  mugshot boards, red-string boards — highlighter on body-size text, pen markups, text call-outs.
- **THE MAP** (night/satellite relief): Mexico and its states, northern Sinaloa, the border, Chihuahua's Sierra Tarahumara, the Caribbean
  and Pacific; cartel territory/routes in ember, US in steel, Mexican state in olive; burns, routes drawn on, pins, radio waves, contrast
  call-outs, 3D-tilted relief planes (refs ast_d02865717c824c47 / ast_e93e1bd1813e40ef / ast_b30b6aa33937428e).
Recurring motifs: THE DEAL (introduced cts07; echoed cts08 Mencho credit, cts09 Chihuahua "way around" = `cross`, cts12 the arrest,
cts14 "Mexico is actually doing it"); TARGET FILE (cts01 Isidro WANTED, cts02 Mencho KILLED, cts04 Isidro's file filling up, cts09 Zuany,
cts12 the net/CAPTURED). Footage screens: this is a 2020s story — phone frames for social clips, a TV-news monitor for broadcast clips,
a CIA-style tablet/drone feed for surveillance beats (built, not a fake real UI: abstract HUD lines only), a vintage TV only for the past
(1985 Camarena, 1990s Sinaloa).
Effects: the full kit (MANUAL §5/§6/§10): 2.5D at most once per segment (best moments: cts01 Isidro reveal, cts08 Maduro, cts12 the
house), Vox layered backgrounds, collage boards, newspaper reveals, painting-to-print for a quote, charts/isotypes/counters, text animations,
contrast/text/focal call-outs, DSLR focus hunt, radio waves, whips. Charts: numbers as narrated, built in the order he says them, 12 fps,
one key number in yellow. Reuse: never the same photo/clip more than twice in the whole video unless the story needs it (cold-open clips
return in cts13 by design — "That's where the baseball game you saw at the start comes from").

## 7. Files, ids, timing, checks
- `compositions/ctsNN.html`, composition id `ctsNN`, root
  `<div id="root" data-composition-id="ctsNN" data-vo-start="SEG_START" data-duration="DUR" data-width="1920" data-height="1080">`.
- Temp VO for previews: `<audio id="ctsNN-vo" class="temp-vo" src="vo_ct.mp3" data-start="0" data-duration="DUR" data-media-start="SEG_START" data-volume="1">`.
  No other audio tags. All `<video>` muted, each with an `id`.
- `const SEG="ctsNN", SEG_START=…, SEG_END=…; const T = s => +(s - SEG_START).toFixed(3); const S = T;` — every text cue a literal
  `T(<master word start − 0.06>)` from `transcript_ct.json`; long lines word by word. Structural cues `S()`.
- Refine the lead's rows into `project/cartels/EDIT_NOTES_ctsNN.md` (same table format as `project/nvidia/EDIT_NOTES_nvs10.md`: id
  ctsNN-scNNN, master start–end on word starts, exact words, picture + WHY it matches the words, ground/effect, ref id, text + cue times,
  transition, SFX) before building.
- Your own extra assets → `assets/cartels/ctsNN/` (photos/, footage/, derived/) + `SOURCES.md`. Openly accessible pages only; never log in;
  never fabricate; never work around a paywall; no gore. Footage: h264 ≤ 1080p, 24 fps, no audio, 2–8 s trims.
- Sandbox: `zsh tools/make_sandbox.sh ctsNN` → `cd work/ctsNN && python3 tools/build_index.py ctsNN --root .` → lint / snapshot there. Never
  write the root `index.html`. Shared 4 CPU cores: snapshot in batches of ≤ 8 frames, one batch at a time; delete `.snap` when done.
- Checks before done: `npx --yes hyperframes@0.8.217 lint` 0 errors for your composition; `python3 tools/sync_audit.py compositions/ctsNN.html
  --transcript transcript_ct.json` clean (every text cue ≤ 0 and ≥ −0.12 s); snapshots of every scene (start+0.3, middle, last 0.5 s) and of
  every cut at −0.05/+0.05 s LOOKED AT against the words and §0; timeline duration == DUR (dump `tl.duration()`);
  `compositions/ctsNN.sfx.json` (types that exist in `tools/audio/place_sound.py` — grep it; master seconds; one hero per scene + camera
  moves/entrances); `compositions/ctsNN.NOTES.md` (what you built, effects + reference ids used, shared assets used, deviations, missing
  assets, helpers/gotchas for the lead).
- Don't edit `lib/*`, palette files, `tools/*`, MANUAL.md or other editors' files. Never commit.
- Fewer, better scenes (≈ 3–7 s each) beat many rushed ones — but every second of your range is covered, no gaps, no black frames
  (show a scene with `tl.set` at `t − 0.002`, every clip's `data-duration` reaches past its cut).
