# "Paraguay" sound plan — the Ueno collapse, master 0.00–1621.87 s (`vo_py.wav` / `vo_py.mp3`)

Sound designer, phase 1 (2026-11-08). Sources: MANUAL §7, §10.3, §10.8; SEGMENTS.md §3 (story per segment), §4 (bleeps); DECISIONS.md §3–4;
quality bar `project/ivan/SOUND_PLAN.md`. Tracks / ids / why: `assets/audio/epidemic/LOG.md` ("Paraguay" sections). Measured stems, sections,
keys: `assets/audio/epidemic/ANALYSIS.md`. Cue sheet = `project/paraguay/music_cuesheet.json`, **generated** by
`project/paraguay/gen/make_cuesheet.py` (edit the tables there, re-run, rebuild §6). All music = Epidemic Sound (Krish's subscription), one
key family **E minor / G major** (new for this video: Ivan was D minor, Taiwan D/F/G/A minor). Tone: urgent, investigative financial-crisis
documentary; contemporary-classical pulses and drones; a Latin-American hint from acoustic/nylon guitars and plucks; a sly, light colour
where the narrator jokes; weight for the collapse, protests and arrests. No trailer action.

## 0. Measured facts (ffmpeg ebur128 / numpy, 2026-11-08)

| | value |
|---|---|
| `vo_py.wav` (= `vo_py.mp3`, 48 kHz stereo, 1621.87 s) | **−26.0 LUFS-I** (both files), true peak −1.7 dBTP, LRA 7.6 LU (low −30.5 / high −22.8). Never processed. |
| VO short-term (10 s windows) | −21.5 … −32.8 LUFS; loudest 0–60 s (cold open −22…−25), 530, 570, 880, 1110; quietest 1460–1530 and 1580 (the ending, −29…−31) |
| Bed target | fix round 1: `bed_lu_under_vo` 13 + the VO duck → **−41.8 LUFS ≈ VO − 16 LU** (§7.1; the first build was VO − 14) |
| Noise floor / gate | 20 ms frames: the floor (cut silences, room) sits at −75…−95 dBFS, speech mode ≈ −33 dBFS, a clear valley at −50…−60 → place_sound's gate `min(−45, VO_LUFS − 13.5)` = **−45 dBFS** is right for this VO (the Ivan fix doesn't change it). place_sound finds **70 pauses ≥ 0.6 s**; the ASR transcript only 3 (word ends are padded) — trust the level, not the words, for pauses |
| Speech density | 5408 words, median **3.3 words/s** (p90 3.9) — the densest VO so far: 88 of 163 ten-second windows ≥ 3.3 w/s. Few lifts possible; the cue sheet thins layers by hand (`auto` dips) under the densest explanations and lets the music breathe on the jokes |
| X clip own audio (`assets/paraguay/shared/footage/x_congress_audio.wav`) | 29.2 s, **−13.9 LUFS-I** (peak −0.1), silent 0–2.3 s, S −10.6…−19 → under the cold open at **−17 LU re the VO** (layer gain −27.9 dB); measured 0–5 s: whole bed −16.5 LU re VO |
| Bleeps | 1 kHz sine, exact word length, **VO − 3 LU** (−29 dBFS peak; checked: a stereo sine of amplitude A reads 20·log10 A LUFS) |
| Insert clips with their own audio | none (all other footage is muted `<video>`) → no `ducks` |
| Room tone / library loops | AMB_SCALE = db(min(0, VO + 25)) = −1 dB (≈ as tuned) |

## 1. Layers (vocabulary) — `assets/audio/epidemic/<track>/<track>_<stem>.wav`

| layer | track (stems used) | LUFS-I full / stems | bpm | sections (s, from ANALYSIS) | role |
|---|---|---|---|---|---|
| **DRONE** | `and_then` bass + instruments (pulse 1.1 / 1.6 = tempo-free; its drums are not used) | −14.0 / bass −17.3, instr −19.0 | free | instr quiet to 30, steady 30–290; bass from 40 | glue under every join |
| **WEIGHT** | `starfall` instruments, melody, drums, bass | −14.3 / −17.2, −17.5, −23.0, −15.8 | 82 | steady 14–78, build 78–84, peak 84–89 (bass + drums from 80), peak 101–123 | cold open; the board vote → "the bank is done" |
| **MONEY PULSE** | `dox` full (stems far under it) | −13.1 | 74 | steady 0–139, drop 139–148, silent 148–155, back 160, build 168–173 | the 60 % numbers; the merry-go-round |
| **WRY** | `in_disguise` instruments, bass, melody | −10.5 / −13.1, −17.1, −14.2 | 84 | steady 0–104, drop 104–110 | the tweet; "Luckily for Ueno…law gets changed" |
| **LATIN** | `andean_valley` instruments, drums, bass | −13.6 / −15.4, −19.5, −19.1 | 95 | quiet 5–23, steady 23–127 (drums 15+, bass 45+, melody 87+) | the boring success story |
| **HOPEFUL** | `we_picked_irises` instruments, melody, bass, drums (stems sum cleanly) | −16.2 / −22.1, −17.5, −19.8, −28.9 | 125 | swell 40–45, dip 75, drums 85+, peak 110–135, out 160 | background → 2015 heir → conglomerate |
| **BOOM** | `i_can_see_the_world` instruments, melody, drums, bass (stems sum cleanly) | −16.3 / −20.6, −20.6, −23.5, −21.1 | 142 | rise 0–40, drums 40+, breath at 90, peak 95–145 (bass), out 145 | the Ueno fintech boom |
| **INVESTIGATION** | `neon_noir` instruments, drums, melody, bass | −10.1 / −12.8, −15.3, −16.2, −12.0 | 85 | peak 35–50, accent 80, melody out 95–145, dip 150–175, peak 180–205 | political capital |
| **GUITAR TENSION** | `desert_whispers` instruments, melody, bass, drums | −10.1 / −11.7, −13.5, −18.5, −13.3 | 110 | intro 0–40, bass 35+, drums 45–135, crest 110–115 | hindsight → 0.58 % → "It was." |
| **MYSTERY** | `fake_photisms` full | −12.0 | 111 | quiet 0–30, steady 30–80, dip 85, back 90–105, fade 105–120 | self-dealing → shell companies |
| **SLOW BUILD** | `crossing_the_border` instruments, bass, drums | −12.0 / −17.6, −14.4, −17.6 | 80 | rise 0–105 (−32 → −2 LU), peak 105–210, out 210–240 | central bank → buyer → buried report → ABC Color |
| **CRIME SCENE** | `where_it_all_happened` instruments, bass, melody, drums | −13.1 / −18.2, −17.5, −18.3, −20.6 | 118 | band 0–20, thin 20–45, back 45, peak 75–145, out 145 | the IMF → the unique law |
| **PEOPLE / ENDING** | `buried_in_the_dirt` instruments, bass, melody, drums | −12.3 / −18.0, −22.1, −14.3, −18.3 | 90 | build 0–45, melody 65–105, peak 85–105, drop 110, tail 110–131 | apps dead → protests → arrests → coda |
| X-clip crowd | `assets/paraguay/shared/footage/x_congress_audio.wav` (cue-sheet `"file"`) | −13.9 | — | best 3–11 s | 0–6.6 under the cold open |
| protest / carousel | `sfx/protest_distant_chanting_walla`, `sfx/protest_distant_drums_chants`, `sfx/music_box_antique_melody` (cue-sheet `"file"` layers) | — | — | — | cold open 3.5–13; protests 1525–1547; merry-go-round 1030–1044.5 |

Rules kept from Ivan: one rhythmic track at a time (tracks change only at act boundaries, the tempo-free DRONE bridges every join);
stems of one track keep the same offset; exits on beats are quick (0.1–0.4 s), entries slow (1–3 s); a track returns only where the story
rhymes (Starfall = the country's anger: cold open ↔ the vote/collapse; DOX = the money machine: 60 % ↔ merry-go-round; In Disguise = the
narrator's irony: the tweet ↔ "that law gets changed").

## 2. Cue sheet (master seconds; offset = read position in the file at the layer's start)

| # | story (SEGMENTS §3) | in → out | layers | moves on words |
|---|---|---|---|---|
| P1 | pys01 cold open: X clip → protests → president → **one bank** → **60 %** → Chase 10 % → market share → "imagine…one day" → FDIC/97 % → 30 % → pensions → "how we got here" | 0.00 → 116.4 | X-clip crowd 0–6.6 (@3.0); chants 3.5–13; STARFALL instr + melody @14.2 to 27.2, drums 4.6–26.8; DRONE glue 14–40; DOX full @113 26.0–116.4; DRONE 48–76 + 100–128 | Starfall's melody return on "it all started with one bank" 18.80 (editor boom on the UENO logo 20.8); DOX in on "how big it was" 26.4; DOX's own drop/silence on "Now imagine…one day" 52.0 → 68 (drone floor), build on FDIC/97 % 80.7–84.9; −2 dB on the dense 39–50, 78–92; +1.5 from "So now the big question" 105.03; swell into "how we got here" 115.34 |
| P2 | pys02 World Cup → the tweet → "skin color" → **a boring success story** → investment grade → $350 M on Wall Street → strongest growth → "one bad news" | 116.6 → 206.0 | IN DISGUISE instr + bass @5 116.6–156, melody 127–150 (the tweet); DRONE 150–170; ANDEAN VALLEY instr @18 157.5–206, drums 162.5+, bass on "Wall Street" 184.5; DRONE 200–226 | wry under the tweet, out on "But that's not the case" 154.9; Latin colour from "Paraguay is actually a success story" 159.3; cut + sub hit on "one bad news" 205.59 |
| P3 | pys03 background: "born in 1950 — I'm just kidding" → the money lender ("a bit of loan sharking") → Credit Central → **2015** heir → conglomerate → "where the problem starts" | 213.8 → 333.0 | WE PICKED IRISES instr + melody + bass @37.8; drums @88.2 from 264.0; DRONE 324–346 | its 40–45 swell on the 1950 joke 217.9–220; dip on "Credit Central…not a bank" ~250; drums on "in 2015, the leadership changes" 263.7; peak = the conglomerate 286–311; −1.5 dB under the dense 229–244, 284–305; fades on "where the problem starts" 331.5 |
| P4 | pys04 COVID → 2021 merger → Ueno = fintech → boom → 50 % promos (limits joke) → groceries → low income → first accounts → **four times bigger** | 333.4 → 448.9 | I CAN SEE THE WORLD instr + melody @30, drums @40 from 343.4, bass @95 from 398.4; DRONE 440–470 | drums on "in 2021, he merges" 344.7; its breath at 393.4 (after "50% discount"), peak from "but nonetheless…huge hit" 398.1; ends dead on "four times bigger" 448.75 (editor boom 448.69); drone only for "how the hell do you buy something four times bigger than you?" 454.4 |
| P5 | pys05 the secret weapon: political capital → finance minister → president 2023 → "never directly involved" → CEO → central bank **the next day** → the acquisition goes wrong | 457.6 → 595.8 | NEON NOIR instr + drums @14.6, melody to 540, bass @30 from 473; DRONE 585–612 | its 35–50 peak on "then finance minister…become the president" 478.7–482.6; accent + stinger on "the next day he becomes part of the central bank" 524.28; −1.5 dB under the dense 490–509 |
| P6 | pys06 "Luckily for Ueno" → government deposits → IPS → the 10 % law → **"That law gets changed"** → 30 % → 2nd condition set aside → eyebrows, protests, "looks sketchy" | 596.0 → 706.4 | IN DISGUISE instr + bass @0 (sly reprise); DRONE 690–722 | enters on "Luckily for Ueno, though" 595.84; −2 dB under the law explanation 633–649; +0.5 and stinger on "That law gets changed" 650.32; −1.5 from "raising eyebrows" 686; the file's own drop ends the act |
| P7 | pys07 hindsight → March 2025 → conflict of interest → capital ratio 12 % → 15 % → 0.58 % → "suspiciously good" → 2–4 % → **"too good to be true. And guess what? It was."** | 706.2 → 797.35 | DESERT WHISPERS instr + melody @23.9, bass @35 from 717.3, drums @45 from 727.3; DRONE from 798.2 | bass/drums enter around "March 2025…sells his stake" 714–727 → "conflict of interest" 730.2; −1.5 dB under the ratio numbers 754–772; +1.5 crest from 786; **music cut dead on "It was." 797.27** + low hit |
| P8 | pys08 back to the conglomerate → loans to the group → self-dealing 20 % → "owe a million / owe a billion" → can't lend more legally → **shell companies** → "created today" → payroll | 812.0 → 932.0 | FAKE PHOTISMS full @0; DRONE 798–832 + 924–952 | after the cut, drone only for "this is where we come back to the beginning"; bass/melody arrive with "this is not illegal" ~840; −1.5 dB breath under the million/billion joke 877–884; its 90–105 return on "shell companies…created today" 905–916 |
| P9 | pys09 60 days → write it down → "creative accountants go to jail" → loans over and over → too big to fail → **$300 M** → "Merry go around" | 940.6 → 1042.5 | DOX full @37.3 (the money pulse returns); music box 1030–1044.5; DRONE 1034–1085 | −3 dB under the accounting-teacher joke 975–992; music box (carousel hint, −31) under "$300 million…merry-go-round"; DOX's own drop on "Merry go around" 1041.6 |
| P10–11 | pys10–11 the central bank catches on → "this bank is lying" → two options → "piece of [bleep]" → **the buyer** (owned by the same group) → < $100 k → $79 M → "piece of [bleep]" → $80 M → the report → CEO Aug 14 / head Aug 15 → **buries it** → two months → **ABC Color** → "last week" → pressure → senators of his own party | 1043.5 → 1294.0 | CROSSING THE BORDER instr @0 (+7 → 0 dB auto lift on its very quiet start), bass @75 from 1118.5, drums @125 from 1168.5; DRONE 1034–1085, 1268–1310 | slow build from "luckily the central bank did catch on"; stinger on "owned by the same group" 1125.14; peak 1148–1253 carries $79 M → $80 M → the report → "buries the report" 1193.27 (sub) → ABC Color 1233.54 (riser) → "last week" 1258.8; fades 1253–1283 |
| P12 | pys12 developing country → the IMF assessment → the mission was in the country last week → Senate presses → burying = corruption → past crises → **a unique law** → criminally liable | 1294.5 → 1440.5 | WHERE IT ALL HAPPENED instr + bass @0, melody @10 from 1304.5, drums @40 from 1334.5; DRONE 1432–1470 | thin under "investors rely on the IMF assessment"; full band (file 45) on "whatever IMF says is very important" 1337–1339; peak 1369–1439 (Senate → corruption → the law); its end = "criminally held liable whenever the thing blows apart" 1440 |
| P13 | pys13 the board does the right thing → unanimous → **"the bank is done"** → apps dead → no balance, no withdrawals → protests everywhere → ~$1,500 → chaos → resign → **Senate rejects + impeaches** → house arrest → board head, owner, ~20 arrested → the daughter: "tax the poor" → viral | 1456.6 → 1621.87 | STARFALL instr + melody @53.9, bass + drums @80 from 1482.6 — cut at 1486.7; BURIED IN THE DIRT instr + bass @0 from 1490.5, drums @20 from 1510.5, melody @65 1555.5–1601; protest drums/chants 1525.5–1547; DRONE 1596–end | Starfall (the cold-open track) builds into its 84 s peak exactly on "the bank is done" 1486.66 — **cut dead** + low hit; ~4 s of near-silence for the apps that won't work (editors' `app_error`); Buried in the Dirt rises for the people; protest chants under "protest all over the place" 1528.2; melody + stinger on "the Senate rejects…impeaches him" 1560.8/1562.36; peak on the arrests 1575–1595; its own drop on the bleep 1600.6; quiet tail under "tax the poor…more fire"; fades out by 1621.87 (no hold beyond the master) |

## 3. Stingers (cue sheet `stingers`, synced on the file's loudest point)

| s | word | sound | rel LU re VO |
|---|---|---|---|
| ~~18.80~~ | "it all started with one bank" | removed in phase 2: the editor's boom on the UENO logo 20.8 carries it | — |
| 27.68 | "Around **60%** of adults" | `boom_sub_bass_clean_01` | −28 |
| 115.34 | → "Let's look at exactly **how we got here**" | `swell_reverse_timpani_cymbal` (peaks on the word) | −27 |
| 205.59 | "there was **one bad news**" | `boom_sub_bass_clean_01` | −26 |
| ~~448.75~~ | "four times bigger" (music cut) | removed in phase 2: the editor's boom on "4×" 448.69 carries it (a stinger would drop it) | — |
| 524.28 | "**the next day** he becomes part of the central bank" | `boom_cinematic_deep` | −25 |
| 650.32 | "That **law gets changed**" | `boom_dark_cinematic_low_hit` | −27 |
| 797.27 | "too good to be true. And guess what? **It was.**" (music cut) | `boom_dark_cinematic_low_hit` | −22 |
| 1125.14 | the buyer: "owned by **the same group** that own the bank" | `boom_cinematic_deep` | −24 |
| 1193.27 | "he basically **buries** the report" | `boom_sub_bass_clean_01` | −25 |
| 1233.54 | → "It's called **ABC Color**" | `riser_reverse_cymbal_short` | −28 |
| 1486.66 | "**the bank is done**" (music cut) | `boom_dark_cinematic_low_hit` | −21 |
| 1562.36 | "the Senate rejects his resignation and then **impeaches** him" | `boom_cinematic_deep` | −23 |

An editor's `boom_low` / `riser` marker within ±0.6 s of a stinger is dropped automatically (no double hits).

### 3.1 Bleeps (cue sheet `bleeps`; DECISIONS §3)
| word (master) | dur | line |
|---|---|---|
| 1104.58 | 0.32 s | "the loan was a piece of [shit]" |
| 1159.43 | 0.16 s | "to buy its own piece of [shit]" |
| 1600.60 | 0.24 s | "people do stupid [shit]" |
place_sound.py adds a 1 kHz bleep of exactly that span (5 ms ramps, VO − 3 LU) to `sfx.wav` after the restraint pass (never dropped, never
capped). Editors' `{type:"bleep", t, dur}` markers within 0.3 s of these are merged (the cue sheet wins; others are added). **The lead mutes
the same three VO spans in the final mix** (the VO itself is never EQ'd/compressed/normalised — DECISIONS §3); use exactly these times.

## 4. SFX vocabulary for the editors (`compositions/pysNN.sfx.json`, master seconds)

Format as project/c2/SEGMENTS.md §3.4: `{"t": 1486.66, "type": "app_error", "scene": "pys13-sc004", "level": "soft|normal", "dur": <loops>, "note": "…"}`.
All existing types still work (whoosh_soft/whoosh/whoosh_big/whip, paper_*, marker_*, highlighter_swipe, pin_pop, map_pin, stamp_thud,
shutter, counter_ticks, focus_hunt, crt_*, boom_low, riser, plane_pass, radio_static, phone_vibrate, message_ping, keyboard, glitch,
siren_distant, door_knock, city_night, car_engine, car_door, heartbeat …). **New for Paraguay** (Epidemic recordings, `tools/audio/place_sound.py`;
common spellings are aliased, e.g. `censor`→bleep, `notification_app`/`app_ping`→app_notify, `error`→app_error, `kaching`/`cash`→cash_register,
`coin`→coins, `swipe`/`card`→card_swipe, `stamp`→rubber_stamp, `carousel`/`merry_go_round`→music_box, `flash`/`paparazzi`→camera_flash,
`cuffs`→handcuffs, `stadium`/`cheer`→stadium_crowd, `protest`/`chant`→crowd_chant, `murmur`/`walla`→crowd_murmur, `office`→newsroom):

| type | sound | use on |
|---|---|---|
| `bleep` (dur = word length) | 1 kHz censor tone, exact length | the three "shit"s (with the graphic beat) — already in the cue sheet |
| `app_notify` | phone notification tone | Ueno app screens, accounts pouring in, the viral post |
| `app_error` | mobile app error tone | "apps…would just not work", balance "—", spinner |
| `cash_register` | ka-ching (bell on t) | profits, "someone's paying us $80 million", 50 % back |
| `coins` (note "handful" → pile) | coin drop | cash / $1,500 / small depositors |
| `card_swipe` | card through a reader | "spend on your credit card…50% back" |
| `atm` (dur) | ATM buttons/beeps/cash flap excerpt | withdrawals, "no withdrawals" |
| `rubber_stamp` (alt `stamp_thud` + note "rubber/approved/rejected/stamp") | real rubber stamps (2 takes) | investment-grade stamp, "created today" registrations, the board's vote |
| `music_box` (dur; > 4.5 s = melody) | wind-up / antique music box — VERY low | merry-go-round graphic (one is already in the cue sheet at 1030–1044.5: don't double it) |
| `gavel` (note "twice" → x2) | courtroom gavel | Senate rejects / impeaches, "criminally liable" |
| `camera_flash` (dur > 1 s = press burst) | press-conference flashes / one modern flash | arrests, press photos, Peña's statements |
| `handcuffs` | handcuff ratchet click | "under arrest" (few: board head, owner, ~20 others) |
| `stadium_crowd` (dur) | distant stadium cheer, swells on t | World Cup clips/stills (keep under the VO: `level` soft) |
| `typewriter` (dur) | real Hermes typewriter (Epidemic mode) | ABC Color articles being typed, the report |
| `crowd_chant` (ambience, dur; note "drum/street" or "close") | distant protest chants (3 recordings) | protest footage, the X clip's follow-ups (≈ VO − 22 LU) |
| `crowd_murmur` (ambience, dur) | large indoor walla | Senate chamber, press room (≈ VO − 25 LU) |
| `newsroom` (ambience, dur) | small office + keyboards | ABC Color newsroom, central-bank office (≈ VO − 26 LU) |
| `city_night` + note "asuncion/paraguay/tropic/insect" (ambience, dur) | warm night city, traffic + insects | Asunción at night (Congress, the crowd) |
| `keyboard` (dur) | typing | the shell-company registrations, spreadsheets |
The editors never add music. One hero per scene + camera moves/entrances (§10.8 restraint pass drops the rest).

## 5. Levels

Estimated per act for the whole cue sheet (each act's layers built alone, then the global VO − 14 normalisation; calibrated against the
real place_sound build of 0–216 s: P1 −16.5 measured vs −17.1 estimated before the trims, P2 −14.8 vs −15.1). Trims (`TRIM` in
make_cuesheet.py): P1 +2, P3 −0.5, P4 −1.7, P7 −2, P8 +1.5, P9 +1, P12 −1.2, P13 −1.5.

| act | music re VO (LU) | act | music re VO (LU) |
|---|---|---|---|
| P1 cold open | −14.7 | P8 shell companies | −15.6 (phase 2: −16.1) |
| P2 tweet → success story | −14.7 | P9 merry-go-round | −14.8 |
| P3 background | −14.6 | P10–11 buyer → report → ABC Color | −13.1 |
| P4 fintech boom | −13.6 | P11 glue (1268–1294.5, drone tail only) | −16.7 |
| P5 political capital | −13.9 | P12 IMF → the law | −13.2 |
| P6 pensions (sly) | −15.3 | P13 the collapse → arrests → coda | −12.6 (the VO is quietest here, −28.3) |
| P7 → "It was." | −13.0 | | |

Test bed (place_sound, music only, 0–216 s, 2026-11-08, deleted after measuring): bed −40.0 LUFS (target −40.0), peak −22.1 dBFS; the
music never comes closer than **7.4 LU** to the VO in any 3 s window; X clip + Starfall 0–5 s −16.5 LU re VO, chants 5–13 s −14.9,
"one bank" 18–27 s −14.2, DOX drop 52–68 s −16.6, In Disguise −15.7, Andean Valley −15.8. The phase-2 full build must re-run
`act_levels.py` (the estimate ignores the voice-band pocket and pause lifts, ≈ ±0.6 LU).

## 6. Build / rebuild (run heavy audio jobs one at a time)

```bash
cd /home/user/vox-edit-kit
python3 project/paraguay/gen/make_cuesheet.py            # only if the cue tables changed
nice .venv/bin/python tools/audio/place_sound.py --vo vo_py.mp3 --transcript transcript_py.json --len 1621.87 \
  --markers 'compositions/pys*.sfx.json' --cues project/paraguay/music_cuesheet.json --out assets/audio/paraguay
nice .venv/bin/python tools/audio/act_levels.py --vo vo_py.mp3 --beds assets/audio/paraguay --cues project/paraguay/music_cuesheet.json --len 1621.87
nice .venv/bin/python tools/audio/measure_mix.py --vo vo_py.mp3 --beds assets/audio/paraguay --len 1621.87 --out renders/testmix_py.wav \
  && rm -f renders/testmix_py.wav
```
→ `assets/audio/paraguay/{music_bed.wav, sfx.wav, ambience.wav, timeline.json}` (+ music_report.json, sfx_placements.json incl. `bleeps`,
sfx_hierarchy.json). **Memory**: a 1622 s build holds several 1.25 GB float arrays (≈ 8–10 GB peak, estimated) — run it alone, with no
render or other audio job on the box; the 216 s test took 33 s. The Epidemic WAVs are gitignored: on a fresh machine re-download them
first (ids + commands in `assets/audio/epidemic/LOG.md`, "Paraguay" — 13 tracks incl. the And Then drone, 89 SFX ≈ 1.5 GB).
Quick test of the first minutes: same place_sound line with `--len 216 --markers 'compositions/none_*.sfx.json' --out renders/testbed_py`.

### place_sound.py / epidemic_bed.py changes made for Paraguay
- New SFX types `app_notify, app_error, cash_register, coins, card_swipe, atm, rubber_stamp, music_box, gavel, camera_flash, handcuffs,
  stadium_crowd` (GAIN table + `render_epidemic`), Epidemic Hermes `typewriter`, ambience types `crowd_chant, crowd_murmur, newsroom`
  (AMBTYPES, AMB in the hierarchy), `city_night` + "asuncion" → warm night with insects, `stamp_thud` + "rubber/approved" → rubber stamps;
  hierarchy RANK entries for all; aliases (§4).
- `bleep`: cue-sheet `bleeps` + editor `bleep` markers → `place_bleeps()` (1 kHz, exact length, VO − 3 LU), added to `sfx.wav` after the
  caps and the restraint pass; listed in `sfx_placements.json` → `bleeps`.
- Cue-sheet `"file"` layers can point outside the Epidemic folder with a relative path (`../../paraguay/shared/footage/x_congress_audio.wav`).

## 7. Phase 2 build — done 2026-11-08 (all 13 `compositions/pys*.sfx.json`, 617 markers)

`assets/audio/paraguay/{music_bed.wav, sfx.wav, ambience.wav, timeline.json}` + music_report / sfx_placements (incl. `bleeps`) /
sfx_hierarchy. Build 2 min 37 s on the free box. Two passes (2nd: P8 trim +1 dB, the 652.55 crack made the scene hero).
- **Marker edits** (cue sheet `marker_edits`, applied by place_sound by t + type; editors' files untouched): drop boom 207.76 (2 s after
  the "bad news" stinger), the 'flash' 232.42 (a white flash frame, not a camera), boom 331.8 (1.4 s before the 2020 boom), boom 653.56
  (third hit in 3 s), riser 1041.17 (fights DOX's drop + the music box — lead's note); retype booms 575.03/575.83/590.0 → thuds (five
  booms in 18 s → booms kept on the heroes 577.27/593.05), paper_tear 652.55/797.25/892.95 → **`crack`** (new type: Epidemic ice cracks; the
  hero 797.25 gets the long crack), dot_ticks 724.85 → **coins** (handful), 'crowd' 690.0 → crowd_chant (the alias meant office walla).
  Stingers 18.80 and 448.75 removed in favour of the editors' picture-synced booms (20.8 UENO logo, 448.69 "4×"); editor boom 797.4 dropped
  automatically (stinger 797.27). Gavels alternate takes in order of use (1437.55 single 01, 1455.30 single 02, 1560.76 single 01).
  `level: "loud"` (pys01) is read as normal; `marker_short` (pys13) → marker_scratch (alias added: it did not parse before).
- **Restraint pass**: kept 425 / 608 markers, dropped 183 (`sfx_hierarchy.json`).
- **Bleeps**: 3 placed, no doubles (the editors' three `bleep` markers merged into the cue sheet's): 1104.58+0.32, 1159.43+0.16,
  1600.60+0.24, 1 kHz, −29 dBFS peak.
- **measure_mix** (VO unmuted): mix **−25.9 LUFS-I vs VO alone −26.0 (Δ 0.1 LU ✓)**, true peak −1.6 dBTP (= the VO's); music −40.0 LUFS
  (−14.6 LU re VO while he speaks); SFX −42.9 LUFS, median −20.4 dB re the local VO peak, max −22.0 dBFS; ambience −57.5 LUFS.
- **act_levels** (music re VO while he speaks): P1 −14.9 · P2 −15.1 · P3 −15.8 · P4 −14.9 · P5 −14.7 · P6 −15.9 · P7 −13.5 · P8 −16.1 ·
  P9 −14.5 · P10–11 −13.5 · P11 glue −16.6 · P12 −13.6 · P13 −13.8 · whole −14.6.
- Checked cuts in the bed (RMS): "It was." 797.27 −42 → −48.5 dB; "the bank is done" 1486.66 −40 → −74 dB from +2 s (true silence until
  1490.5 for the dead apps); end fades to −76 dB by 1621.3.
- `tools/final_mix_paraguay.sh` fits the beds as built (three beds at unity, amix normalize=0, the bleep tones live in sfx.wav, its VO
  mute windows = §3.1 with 5 ms fades just outside the bleep's span). No conflict.

## 7.1 Fix round 1 — "music never drowns the voice" (Krish, 720p review, 2026-11-08: "too loud…around 7:20")
Built with the final `compositions/pys*.sfx.json` (600 markers → 419 kept). Changes:
- **VO-driven duck on the music bed** (`epidemic_bed.vo_duck`, now place_sound's default; cue sheet `vo_duck` = gap 12 LU, attack 50 ms,
  release 400 ms, max 15 dB): ducked 64 % of the time, mean −3.9 dB while ducked (max −16.3 with both passes). The VO is only read.
- Hot layers pulled down: I Can See the World peak −3 dB from 398.4 (the 7:20 area), Neon Noir 474–509 −3, Crossing the Border peak
  1146–1252 −3, Where It All Happened 1357–1440 −2.5, Buried in the Dirt 1573–1600 −3; DOX's +1.5 lift into "how we got here" removed;
  pause lifts ≤ 2 dB; booms (LOWTYPES) 2 dB lower in the SFX caps. `bed_lu_under_vo` 13.0 before the duck.
- Scan (`tools/audio/vo_music_scan.py`), music vs the VO while he speaks — before (the 720p beds) → after:

| | before | after |
|---|---|---|
| 3 s windows: median gap / p5 / min | 14.0 / 8.0 / **2.3 LU** | 14.8 / 12.8 / **11.0 LU** |
| 3 s windows < 12 LU | 30.5 % (188 spans) | **0.3 %** (32 spans, all ≥ 11.0) |
| 0.4 s windows (vs local speech level): p5 / % < 12 LU | 7.5 / 24.1 % | 12.3 / 2.9 % |
| 420–460 s, 3 s: median / min gap, % < 12 | 12.2 / 6.1 LU, 47.5 % | 14.5 / 11.2 LU, 1.0 % |
| worst minutes (3 s min gap) | 19:xx 2.3, 20:xx 3.2, 26:xx 3.4, 08:xx 4.5 | every minute 11.0–12.7 |
| music+sfx 3 s min gap | 2.3 | 6.3 (single hero booms: 153.8, 577.3, 593.1, 1270.2; whip 1358.9) |

- Levels: music −41.8 LUFS = **−16.0 LU re the VO** while he speaks (was −14.6); per act P1 −15.5 · P2 −15.5 · P3 −16.0 · P4 −16.6 ·
  P5 −16.2 · P6 −16.3 · P7 −14.8 · P8 −16.9 · P9 −15.4 · P10–11 −16.9 · P11 −16.2 · P12 −15.8 · P13 −16.1. measure_mix: mix −25.9 vs VO
  −26.0 LUFS-I (Δ 0.1 LU), true peak −1.7 dBTP; SFX median −20.7 dB re the local VO peak. Loudest music left: the cold open
  (18 s / 23 s, −34.6/−36.2 LUFS-S, where the VO is loudest, −19…−22 → gaps 14.6–15.2).

## 8. Open questions for the lead
1. **X clip media start**: the crowd layer reads the clip's audio from **3.0 s** over 0–6.6 (`XCLIP_MEDIA_START` in make_cuesheet.py) =
   EDIT_NOTES_pys01 sc001 (clip media 3.0–9.45 over master 0–6.45). **Confirmed in the built pys01.html**: `x_congress_trim.mp4` (= source 2.6–10.2) with data-media-start 0.4 over 0–6.6 → source 3.0 ✓. (The final
   pys01.sfx.json has no crowd marker at the open — no double.)
2. **Muting the bleeped words** is the lead's final-mix step (three spans in §3.1). Confirm with Krish that a hard mute of the word (no
   other processing) is fine under the "never alter the VO" rule — DECISIONS §3 says yes.
3. **Loudness**: VO −26.0 LUFS → the finished mix will read ≈ −25.8 LUFS integrated (bed 14 LU under). Louder delivery (YouTube ≈ −14) would be
   a whole-mix decision, never the VO alone.
4. **The wry colour (In Disguise)** is a quirky/sneaky pizzicato piece; it's kept low (−16/−17 rel, instruments + bass; melody only under the
   tweet). If Krish finds it too comic for "the law gets changed" (pension money), swap P6 to Fake Photisms (full) or Desert Whispers' intro.
5. No Paraguayan harp: none tasteful in the catalogue (searched harp / paraguayan harp / folk harp / harp south america). The Latin hint is
   carried by Andean Valley (P2), I Can See the World (P4) and Desert Whispers (P7).
