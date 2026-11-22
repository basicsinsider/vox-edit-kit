# "US vs Cartels" sound plan — master 0.000–1341.912 s (`project/cartels/media/vo_ct.wav` = `vo_ct.mp3`)

Sound designer, phase 1 (2026-11-22). Sources: MANUAL §0, §7, §10.3, §10.8 (incl. "Music limits — BINDING", the Ivan, Paraguay and NVIDIA
notes); SEGMENTS.md §3 (the 14 segments), §6 (tone: urgent cold open, then a curious, wry investigation; worlds THE NIGHT / THE CASE FILE /
THE MAP; motifs THE DEAL and TARGET FILE); BRIEF rule 3 (no gore — sound implies, never depicts); quality bar `project/nvidia/SOUND_PLAN.md`.
Tracks / ids / §10.8 checks: `assets/audio/epidemic/LOG.md` ("Cartels (2026-11-22)"). Measured stems, sections, keys:
`assets/audio/epidemic/ANALYSIS.md`. Cue sheet = `project/cartels/music_cuesheet.json`, **generated** by `project/cartels/gen/make_cuesheet.py`
(edit the tables there, re-run, rebuild §6). All music = Epidemic Sound, one key family **G minor / Bb major** (new: Ivan + Taiwan D minor / F,
Paraguay E minor / G, the podcast A minor / C, NVIDIA C minor / Eb). Tone: contemporary crime/geopolitics score — dark drone-pulses for the
night raids, sneaking pulses for Sam's explainer, crime-scene suspense for the CIA story, a near-silent drone for the cliff, a chase build for
the capture, a hopeful but unresolved ending. Latin colour only as texture (Running through the Dark's acoustic/plucked lines for Sinaloa);
no mariachi, no "narco" parody, no trailer action.

## 0. Measured facts (ffmpeg ebur128 / numpy, 2026-11-22; `work/sound/vo_ebur128_summary.txt`, `work/sound/vo_stats.txt`)

| | value |
|---|---|
| `vo_ct.wav` (48 kHz mono float32, 1341.870 s; md5 checked unchanged after every test) | **−32.1 LUFS-I**, true peak **−4.3 dBTP**, LRA 7.4 LU (low −36.4 / high −29.0). The quietest VO since Ivan → every threshold is relative to it. Never processed. |
| VO per act (LUFS-I) | C1–C2 0–123 −31.6 / −32.1 · backstory 123–264 −31.4 · nickname 264–358 −31.7 · Washington 358–540 −32.2 · THE DEAL 540–651 −31.7 · boats/Maduro 651–768 −32.5 · Chihuahua 768–976 **−30.6** · April op 976–1078 −33.1 · **net/capture 1078–1193 −35.0** · aftermath 1193–1286 −34.3 · ending 1286–1342 −33.4 |
| VO 10 s windows | −26.8 … −37.0 LUFS; quietest 1080 (−37.0), 1140, 1230, 1210, 1090, 1180 (the capture/aftermath — he drops his voice); loudest 770, 850, 760 (Chihuahua), 340, 870 |
| Activity gate | 20 ms frames, gate `min(−45, VO − 13.5)` = **−45.6 dBFS** → 65.7 % active (floor p5 −67.8, speech median −35.1 dBFS); **88 pauses ≥ 0.6 s** (median 0.66 s, max 1.22 s at 769.2). Works; no tool change needed |
| Speech density | 3960 words, **2.95 words/s** (10 s p10 2.5 / p50 2.9 / p90 3.5); 26 of 134 windows ≥ 3.3 w/s → few dense spans; `auto` dips thin layers by hand where they are |
| Bed target | `bed_lu_under_vo` **22** → −54.1 LUFS before the duck; the duck (gap 20 / gap_fast 18 / ceiling 20) takes ≈ 3 dB → ≈ **VO − 25 LU** while he speaks (test: −25.3) |
| SFX / ambience scaling | SFX_TRIM_DB = −3 + (VO + 27.2) = **−7.9 dB**; quiet-VO cap path (VO < −27.5: caps relative to the local VO peak only); AMB_SCALE = db(min(0, VO + 25)) = **−7.1 dB** |
| Insert clips with their own audio | none planned (all footage muted, BRIEF) → no `ducks`; bleeps none (no swearing) |

## 1. Layers (vocabulary) — `assets/audio/epidemic/<track>/<track>_<stem>.wav` (16-bit, only the stems used), all G minor

Pulse = onset-autocorrelation peak/median per stem (calibrated: sustained pad 2.6, noise 2.1, random swells 4.1, 120-bpm click 14.3).
Σ = stems-sum check over 60 s (residual re full; LU of Σ stems re full).

| layer | track (stems used) | LUFS-I stems | bpm | sections (s, ANALYSIS) | role |
|---|---|---|---|---|---|
| **DRONE** | `zone_of_deception` instruments (DEX 1200; Bb–C–D–F) — pulse **2.0**, bass 8.4 / drums 36.5 not used | −17.0 | free | quiet 0–29, steady 29–69, peaks 75–80, 84–90, 117–131, 164–172, 210–215 | glue under every join (offsets in its steady windows 30–69, 136–155, 179–204); alone for the cliff (C16) and the net-closing breath |
| **THE NIGHT** | `db_cooper` instruments, bass, drums (Craft Case; Σ +4 dB = stems mastered separately) | −18.9 / −23.1 / −25.8 | 120 | steady 10–80, build 80–84, **peak 84–94**, 97–110, drop 110–117 | cold open (C1); Caracas (C10); the aftermath + ballpark callback (C19) |
| **THE QUESTION** | `perplexed` full + bass (Michael Rothery; stems 5 LU under the full → `full`; bass pulse 1.7) | −11.2 / −17.4 | 120 | silent 0–11, quiet 11–20, steady 20–74, **peak 74–113** | "Is this a war on cartels? Is this actually working?" (C2, title) ↔ "Is this working?" (C21) |
| **SINALOA** | `running_through_the_dark` instruments, melody (Roots and Recognition, acoustic; Σ clean −9 dB) | −13.1 / −13.8 | 80 | quiet 0–10, steady 10–86, **peak 86–122** (from the instruments curve; full deleted) | his origins (C3); the routes north → Arizona → fentanyl (C5) |
| **THE WAR** | `symmetry` instruments, bass, melody (Christoffer Moe Ditlevsen; Σ clean −25.5 dB) | −12.8 / −22.2 / −17.5 | 89 | quiet 69–82, build 82–85, steady 85–99, **peak 99–157**, silent 170+ | 2008 split → civil war → the 2010 Sonora ambush (C4) |
| **WRY** | `have_we_met_before` melody, instruments (+ full on disk) (Jon Sumner; stems 4.8 LU under full) | −17.8 / −26.6 | 118 | quiet 2–34, steady 34–108 | the nickname, arrested four times and walked out (C6); the failed raids / tip-offs (C14) |
| **WASHINGTON** | `timepass` full (Marten Moses; stems 6.5 LU under → `full`) | −10.2 | 120 | build 12–15, steady 15–69, drop 69–74, quiet 74–90, build 90–95, steady 95–117 | day-one order → terrorist label → armed conflict → tariffs (C7); the ambassador + extradition (C20) |
| **PRISONERS** | `triple_fault` full + instruments (Robert Ruth; instruments pulse 2.1 = tempo-free texture) | −9.7 / −19.3 | 110 | steady 9–98, **peak 98–103**, drop 103–109 | 29 flown to the US → "40 years" (C8); who gets the credit for El Mencho (C11) |
| **THE DEAL** | `acrolith` instruments, bass (Anthony Earls) | −14.6 / −16.8 | 80 | steady 0–58, peaks 58–61, 69–74, drop 74–77, steady 77–111, **peak 111–117** | unwritten deal → spy drones → CIA rules → task force → "Narco Hunters" → target package (C9); CIA on Mexican raids → the safe house (C13) |
| **CHIHUAHUA** | `mortal_separation` melody, bass, instruments (Sage Oursler) | −18.0 / −18.7 / −21.9 | 90 | quiet 0–16, build 23–30, peak 30–42, drop 42–51, quiet 51–68, build 68–77, **peak 77–95**, peak 108–114, drop 114–122 | Zuany, the visa, the witnesses, why the CIA used him (C12) — the file's shape is the segment's |
| **APRIL** | `what_lurks_below` instruments, bass (Jon Björk; crime scene, sad) | −15.5 / −16.6 | 78 | steady 17–97, **peak 97–104**, drop 104–111 | meth lab → convoy → night drive (C15); after the silent cliff: scandal → "Zuany is still on the run" (C17) |
| **THE CAPTURE** | `honesty_matters` instruments, bass, melody, drums (Kikoru) | −20.2 / −22.4 / −20.7 / −21.0 | 101 | steady 3–39, quiet 39–59, build 59–64, steady 64–74, **peak 74–98**, steady 98–112 | the net closing → Revolution Day → Lobos & Murciélagos → the ring around the house → "they arrested him" (C18) |
| **ENDING** | `the_determination` melody, bass (Anna Dager & Hanna Ekström; Σ clean −9.7 dB; instruments pulse 17.7 not used) | −12.5 / −13.8 | free | quiet 0–37, steady 52–101, peak 101–127 | "mostly yes" → "not going away" → "slowed down just a bit" (C21), no cadence |

Rules kept from Ivan/Paraguay/NVIDIA: one rhythmic track at a time (tracks change at story boundaries; the tempo-free DRONE bridges every
join); stems of one track keep the same offset; exits on beats quick (0.8–2.5 s), entries slow (2–4 s); a track returns only where the story
rhymes (THE NIGHT = the three night raids: Guasave, Caracas, the aftermath; THE QUESTION = title ↔ end; SINALOA = his origins ↔ his routes;
WRY = "walked out four times" ↔ "somebody was tipping off the targets"; WASHINGTON = US pressure ↔ the US victory lap and extradition;
PRISONERS = what the US gets out of Mexico, twice; THE DEAL = "the CIA can work with anybody" ↔ CIA officers on Mexican raids).

## 2. Act map and cue sheet (master seconds; offset = read position in the file at the layer's start; full notes in make_cuesheet.py)

| act / segment | cue | story (SEGMENTS §3) | in → out | layers | moves on words (transcript_ct.json) |
|---|---|---|---|---|---|
| **COLD OPEN** cts01 0–68.2 | C1 | ballpark → helicopters → burning trucks → "come for one man" → El Chapo Isidro → FBI list, $5M → caught → "help from the United States" | 0 → 65 | NIGHT instr + bass @52 from frame 1, drums 18.4–58.5; DRONE 56–82 | urgent from 0.24 "That's a baseball game"; drums on "Those military helicopters" 18.4; build 80–84 = "come for one man" 32.1, **peak** = "one man" 35.4 → "El Chapo Isidro" 36.2; peak 97–110 = FBI list 50.2 → "$5 million" 53.8; drop = "the Mexican army had him" 59.3–61.2; drone alone + sub stinger "United **States**" 67.35 |
| **NOT ONE TIME → THE QUESTION** cts02 68.2–122.9 | C2 | El Mencho, April CIA raid, 70+ boats, Maduro → "Is this a war on cartels?" → TITLE | 68.5 → 123.5 | QUESTION full @33.7 (−1.5 dB 106–109), bass 104+; DRONE 117–137 | steady under the list 73.9–108; **peak** from "this all raises a pretty simple question" 109.0 → "war on cartels?" 113.9 → swell stinger "actually **working?**" 116.07 |
| **SINALOA** cts02–03 122.9–172.8 | C3 | born 1982 → "Silicon Valley of drug trafficking" → 90s → teenager → Beltrán Leyvas gunman | 123.5 → 174.5 | SINALOA instr @0, melody 129.5+; DRONE 166–190 | quiet entry under "Fausto Isidro…born in 1982" 123.6; melody on "Silicon Valley" 130.7; out before "But in 2008" 172.8 |
| **THE WAR** cts03 172.8–223.9 | C4 | 2008 split → civil war → armed wing → 2010 Sonora ambush → big boss → brothers fall | 172.5 → 228 | WAR instr @69.5, bass 188+, melody 199.5+; DRONE 220–240 | quiet = "gave him up" 174–183; build = "civil war" 183.1; **peak** = "In 2010…an ambush in the desert in Sonora" 202.4 → 219; out on "But Isidro survives" 223.9 |
| **THE ROUTES** cts03 223.9–264.2 | C5 | survives → north Sinaloa → routes by boat/coast/highway → Arizona → fentanyl → Treasury 2013 | 224.5 → 264.5 | SINALOA instr @72, melody 236+; DRONE 258–278 | **peak** = "a straight shot towards Arizona" 238.4–242.1 → drugs list → "fentanyl…matters the most" 245.8 → Treasury 252.6 |
| **THE NICKNAME** cts04 264.2–358.2 | C6 | two stories → arrested 2011/14/14/15, walked out → "figure out why" → Dec 2024 stash → one ton → FBI list | 264.5 → 358.5 | WRY melody @0, instr 298+ (−2 dB 329–332); DRONE 350–372 | quiet under the nickname stories; steady from "caught before multiple times" 298.2; the joke breathes (−2 dB) at 329.4; "One ton" 349.7 → "10 most wanted" 357.0 |
| **WASHINGTON** cts05–06 358.2–470.5 | C7 | day-one order → terrorist label → "crime to help you" → armed conflict, al-Qaeda → targets → tariffs → 25 % | 358.5 → 471.5 | WASHINGTON full @5 (−1.5 dB 396–414); DRONE 464–488 | build on "his very first day" 366.5; steady under the label; drop + quiet = "the way it treated Al Qaeda" 425.8 → "They are targets now" 431.7; build = "Liberation Day" 440.1; steady = "25%" 455.7 |
| **THE PRISONERS** cts06 470.5–540.4 | C8 | Sheinbaum's call → troops → 29 prisoners flown → 1985 DEA murder → 40 years → 26 + 37 → American prison | 471 → 541 | PRISONERS full @64 → 516, instr @20 515–541; DRONE 506–548 | steady under "on her phone" 476 → "29" 492.4 → "1985" 501.5; **peak** = "chasing for 40 years" 507.6; tempo-free instruments under "American prison" 539.3 |
| **THE DEAL** cts07 540.4–651.5 | C9 | unwritten deal → spy drones → CIA rules → task force in Arizona → "Narco Hunters" → target package | 541 → 651.8 | DEAL instr @0.2, bass 561.5+; DRONE 644–664 | steady under "an unwritten deal" 543.1 → "spy drones" 567.8; peak = "a bigger target" 598.4; peak = "southern Arizona" 608.2 → "task force" 613.5; drop = the beat before "Narco Hunters" 620.1 (the joke); "target package" 638.2 |
| **BOATS → MADURO** cts08 651.5–711.3 | C10 | boat strikes (>70, ~250 killed) → "another level" → Caracas → Maduro → Brooklyn → biggest catch | 652 → 711.6 | NIGHT instr @57.7 (−3 dB 666–674), bass 673+ (no drums); DRONE 704–726 | −3 dB under "close to 250 people…killed" (no weight on deaths); build = "another level" 674.2; **peak** = "fly into Caracas" 679.6 → stinger "**president**" 682.73 → Brooklyn 689.8; drop + felt sub = "El **Mencho**" 710.73 |
| **THE CREDIT** cts08 711.3–768.5 | C11 | Mexican operation vs CIA "instrumental" → State of the Union → "do more than hand off information?" | 712 → 769 | PRISONERS instr @40, full @68 from 740; DRONE 762–786 | "instrumental" 738.9 → "State of the Union" 745 → cut on "hand off information?" 768.5 |
| **CHIHUAHUA** cts09 768.5–891.6 | C12 | below Texas → El Paso → NYT → Zuany → visa cancelled → witnesses → why the CIA used him → visa back | 769 → 892 | CHIHUAHUA melody @0, bass 785+, instr 846+ (melody −2 / bass −3 dB 821–846); DRONE 884–904 | quiet = Chihuahua 772.9; build = "Guillermo Zuany" 792.9; peak = "The CIA liked him" 798.6; drop = "canceled his…visa" 812–819; quiet + dip under the murder accusations 820–846; **peak** = "why would the CIA work with a guy like this?" 847.6; drop = "visa just came back" 889.9 |
| **THE RAIDS** cts10 891.6–947.1 | C13 | Zuany helps → an American trains them → CIA on raids → tablets → the safe house → the questioning | 891.8 → 947.5 | DEAL instr @68.5, bass 900+; DRONE 940–962 | peak = "Zuany starts helping" 891.6; steady under training → tablets 924.0; **peak** = "a cartel safe house" 936.3 → "the phone they seized" 942.2 |
| **THE FAILED RAIDS** cts10 947.1–976.2 | C14 | not according to plan → the bar, boss already left → tip-offs | 948 → 977 | WRY melody + instr @40; DRONE 970–990 | "went to a bar" 956.7 → "tipping off the targets" 968.6 |
| **THE APRIL OPERATION** cts11 976.2–1006.4 | C15 | the biggest CIA operation → meth lab → convoy of 60+ → empty lab → the night drive | 976.5 → 1006.2 | APRIL instr @17, bass 983+ | "meth lab" 985.0 → "it's empty" 995.9 → "middle of the night" 1005.2–1006.4; **music stops** before "one of the trucks just goes off a cliff" |
| **THE CLIFF** cts11 1006.4–1018 | C16 | the truck goes off a cliff → 300 feet → everyone inside killed | 1003 → 1024 | **DRONE alone** | SOMBRE: no pulse, no stinger, no crash sound under "off a cliff" 1008.9 → "Killing everyone inside" 1012.2. Editors: `wind_pines` / `night_insects` only |
| **THE SCANDAL** cts11 1018–1078.4 | C17 | Zuany's instructions → "no clue" → political fight → resignations → AG arrested → Zuany on the run | 1017 → 1079 | APRIL instr @46 (−2 dB to 1030), bass 1050+; DRONE 1072–1096 alone 1079–1092 | returns sadder after the breath; "scandal" 1040.8; **peak** = "Zuany is still on the run" 1072.1 → "here in the United States" 1076 |
| **THE NET → THE CAPTURE** cts12 1078.4–1192.6 | C18 | right-hand man → father → money people → number two → Trump–Sheinbaum → Friday → Lobos & Murciélagos → ring → arrest → plain white house | 1092 → 1199 | CAPTURE instr + bass @0, melody 1151+, drums 1165–1187; DRONE 1186–1206 | drone alone for "the net closing" 1081.3; steady under the net; quiet 39–59 = "the cartels are running Mexico" 1128 → "The mission was on" 1137.5 → "Revolution Day" 1143.2; build = "cool names" 1147 → "wolves" 1154.1; **peak** = "a ring around the house" 1172.9 → stinger "they **arrested** him" 1180.31; steady = "a plain house with white walls" 1189.2 |
| **THE AFTERMATH** cts13 1192.6–1244.5 | C19 | "two days ago" → region goes crazy → trucks burning → ballpark callback → grocery stores → clinic → Air Force plane → the 30-s video | 1197 → 1244.5 | NIGHT instr + bass @69.5, drums 1209–1238; DRONE 1238–1258 | "the region went crazy" 1202.1; **peak** = "the baseball game you saw at the start" 1212.1 → grocery stores → clinic; peak = "an air force plane" 1231.1; drop = "30 second long video…head down" 1236–1243.5 |
| **THE AMBASSADOR** cts13 1244.5–1286.3 | C20 | the ambassador's post → "cooperation and trust" → keep hunting → charged in DC since 2012 → extradition → 92 sent | 1244.5 → 1286.8 | WASHINGTON full @15; DRONE 1280–1300 | "Green Beret" 1247.3 → "overnight" 1254.4 → "extradited" 1276.5 → "90 some" 1280.9 |
| **IS THIS WORKING? → END** cts14 1286.3–1341.9 | C21 | the question → Narcos joke → "mostly yes" → weaker drugs → caught faster → Mexico doing it → not going away → "slowed down just a bit" | 1286.5 → 1341.912 | QUESTION full @66 → 1299.5; ENDING melody @52 1297–1336.5 (−3 dB from 1324.5), bass @56 1301 → end (−3 → −6 dB from 1334); DRONE 1318 → end | riser stinger "Is this **working?**" 1289.11; "mostly yes" 1301.8; −3 dB from "doesn't mean cartels are going away" 1323.8; melody leaves under "the drug smuggling will continue" 1334.4; bass + drone fade under "slowed down just a bit" 1340.1 → 1341.912, no cadence |

## 3. Stingers (cue sheet `stingers`, synced on the file's loudest point; word times from `transcript_ct.json`)

| s | word | sound | rel LU re VO |
|---|---|---|---|
| 67.35 | COLD OPEN payoff: "…with the help from the United **States**" | `boom_sub_bass_clean_01` (felt, not heard) | −31 |
| 116.07 | TITLE: "And is this actually **working?**" (from "Is this a war on cartels?" 112.8) | `swell_reverse_timpani_cymbal` (peaks on the word) | −30 |
| 682.73 | MADURO: "…capture the country's **president**, Nicolas Maduro" | `boom_cinematic_deep` | −30 |
| 710.73 | "Of course, we're talking about El **Mencho**" (a death: felt only, no triumph) | `boom_sub_bass_clean_01` | −31 |
| 1180.31 | THE CAPTURE: "they **arrested** him" | `boom_dark_cinematic_low_hit` | −29 |
| 1289.11 | THE QUESTION returns: "Is this **working?**" | `riser_reverse_cymbal_short` | −31 |

Deliberately none on: the ambush (206.5 "20 to 30 men…killed"), the boat-strike deaths (666–674), the cliff (1006–1015), the clinic (1220) —
BRIEF rule 3 applies to sound too. An editor's `boom_low` / `riser` within ±0.6 s of a stinger is dropped automatically; in phase 2 prefer the
editor's picture-synced boom when they are < 2.5 s apart (MANUAL §10.8).

## 4. SFX / ambience vocabulary for the editors (`compositions/ctsNN.sfx.json`, master seconds; format as NVIDIA/Paraguay)

Marker format: `{"t": <master s of the event>, "type": "<exact name>", "scene": "ctsNN-scNNN", "dur": <s, loops/beds/moves>, "level": "normal"
(hero) | omitted (soft), "note": "<what it is; keywords below>"}`. One hero per scene + camera moves/entrances (the §10.8 restraint pass drops
the rest). **Every type below is wired in `tools/audio/place_sound.py` and its files are on this box** (preflight 2026-11-22: each type rendered).
Use ONLY these exact names (aliases exist but don't rely on them). Not available on this box (off-story, files not downloaded): `atm`,
`card_swipe`, `music_box`, `teletype`, `train_pass`, `crowd_chant`, `wind` + note "winter".

**New for Cartels (wired 2026-11-22)** — violence is far away, never close, never on a body:

| type | dur? | file(s) | use on (and keywords in `note`) |
|---|---|---|---|
| `helicopter` | yes (≥ 1.5) | helicopter_distant_01 / _fly_away / helicopter_military_passby_mid | night footage of the army helicopters (cts01 18.4, Caracas cts08, the capture cts12). Note "pass/close/flyby/overhead" → mid-distance pass; "away/leave" → flying off |
| `gunfire_distant` | no | gunshot_distant_heavy_01/_02; "burst" → rifle_burst_distant_reverb / guns_automatic_big_distant | **sparingly**: at most one per scene, only where Sam says there is shooting (cts01 "gunfight going on", cts12 "hit with some gunfire"). Very low by design (gain 0.025–0.035) |
| `vehicle_fire` | yes | fire_flames_large_01 | burning trucks / cars as roadblocks (cts01 24.2, cts13 1203.5), the gas station; stack `fire_crackle` for crackle |
| `walkie` | opt. | walkie_engage / walkie_static_01; dur > 2 → walkie_static_02 | army/police radios, the officers calling Zuany from the scene, the CIA's tablets/live feed |
| `uav_drone` | yes | prop_plane_small_flyby_quiet; note "hum" → hub_drone_electric_hum | the CIA spy drones ("cameras in the sky", cts07 567.8), drone-feed HUD screens |
| `plane_takeoff` | yes (peak mid-move) | jet_takeoff_distant | prisoners flown to the US (cts06), the Air Force plane to Mexico City (cts13), Maduro flown to New York |
| `boat_engine` | yes (peak mid-move) | speedboat_pass_medium | go-fast drug boats (cts02 92.1, cts08); the strike itself = `explosion_distant` (restrained) |
| `folder_drop` | no | paper_folder_put_down / clip_file_put_down (alternate) | TARGET FILE / dossier / target package landing on the desk |
| `cell_door` | no | prison_door_slam | "an American prison" (cts06 539), "a jail in Brooklyn" (cts08 689.8) |
| `door_kick` | no | door_kick_open | "kick the door in" (cts07 553), raids (cts10) — a short wood hit |
| `convoy` | yes | van_drive_exterior_loop; note "idle" → truck_idle_distance | the convoy of 60+ (cts11 986.9), the night drive back, armored convoys, prisoner transfers |
| `stadium_walla` | ambience | stadium_crowd_walla (≈ VO − 27 LU) | the Guasave ballpark (cts01 0–18, the callback cts13 1212) |
| `night_insects` | ambience | crickets_night (≈ VO − 27 LU, looped) | rural Sinaloa / the Sierra at night, the plain white house |
| `sea` | ambience | ocean_medium_waves_wind (≈ VO − 27 LU) | Caribbean / Pacific boat-strike maps and footage |
| `wind_pines` | ambience | wind_pine_tree (≈ VO − 26 LU, looped); also `wind` + note "pine/forest/sierra/tapalpa" | Tapalpa (El Mencho), the Chihuahua mountains, **the cliff (cts11 1006–1018: the only sound besides the drone)** |

**Existing types on this box** (exact names): moves `whip`, `whoosh_soft`, `whoosh`, `whoosh_big`, `air_swell`, `rewind`, `riser`, `boom_low`;
paper/case file `paper_slide`, `paper_rustle`, `paper_flip`, `page_turn`, `paper_tear`, `rubber_stamp`, `stamp_thud`, `typewriter`,
`highlighter_swipe`, `marker_scratch`, `marker_long`, `pencil_scribble`, `string_pull`, `string_draw`, `cork_pin`, `scanner_sweep`, `card_flip`; map `map_pin`, `pin_pop`, `dot_slide`, `dot_ticks`, `radio_pulse`, `circuit_clunk` (contrast call-out), `crack`;
numbers/UI `counter_ticks`, `odometer_tick`, `letter_ticks`, `tick_soft`, `pop_soft`, `tone_blip`, `chime_soft`, `clock_tick`, `glitch`,
`keyboard`, `app_notify` (the ambassador's post), `app_error`, `message_ping`, `phone_vibrate`, `phone_ring` / `phone_dial` (Sheinbaum's call,
cts06 476), `switch_click`, `lamp_click`, `dial_click`, `domino_tick`, `domino_run`; camera/film `shutter` (note "spy/surveil/cctv" → real
shutters), `focus_hunt`, `camera_flash` (press; dur > 1 → burst), `projector_click`, `film_burn`, `crt_click`, `crt_off` (the 1985 Camarena
TV); objects `handcuffs` (cts13 "hands cuffed"), `gavel` (charges, court), `cash_register`, `coins` (money people, $12 bn), `medal_ring`,
`gate_creak`, `door_knock`, `solder_hiss`; vehicles/war `car_engine`, `car_door`, `plane_pass` (map routes), `drone_buzz` (small quadcopter
only), `explosion_distant` (boat strikes, very restrained), `siren_distant`, `fire_crackle`, `burn_crackle` (map burns), `radio_static`,
`heartbeat` (tension, sparingly), `stadium_crowd` (a cheer swell — not for the frightened ballpark; use `stadium_walla` there);
ambiences `crowd_murmur` (press room, Congress), `crowd_room` (note "restaurant" → crowded-restaurant walla, e.g. the bar raid cts10 956.7; else office room tone), `newsroom` (NYT),
`factory_hum` (note "fab" or "cleanroom" → machine-room electronics hum, e.g. the meth lab; else light factory hum), `city_night` (note "insect" → warm night + insects), `wind`, `projector_loop`,
`crt_hum`, `tube_hum`.

Levels (binding, place_sound): SFX peaks hero −16 / sub hits −19 / rest −22 dB under the VO's local peak; music+SFX 3 s ≥ 14 LU under the VO
(`sfx_limit`); ambiences "felt, not heard" (VO − 26…−27 LU, × AMB_SCALE). Editors never add music.

## 5. Levels

Binding limits (MANUAL §0 / §10.8) are hard-coded in make_cuesheet.py and asserted before writing: `bed_lu_under_vo` 22, `vo_duck` gap 20 /
gap_fast 18 / ceiling 20 / margin 0.7 / 3 passes / max −30 dB, `pause_lift_db` 0, `sfx_limit` gap 14 / margin 1 (as NVIDIA). Per-act aim
−20…−24 LU re VO while he speaks (quieter is the accepted side, NVIDIA landed −23.7…−25.1). The generator also asserts that every layer reads
inside its file.

**Phase 2 (2026-11-22): final trims and whole-length numbers are in `SOUND_REPORT.md`** (acts −23.3…−26.3, whole −25.2, ALL LIMITS MET).
Phase-1 trims (`TRIM`): C2 +3, C3 +4 dB — Perplexed's and Running through the Dark's quiet openings measured −26.3 / −26.9 LU re VO on the first test.
As on NVIDIA each +dB buys only ≈ 0.25–0.5 LU (global normalisation + the duck). Phase 2 must re-run `act_levels.py` on the whole-length build
and trim C4–C21; watch C18–C20 (VO −34…−35 LUFS: the duck follows the quiet voice, the music will read quiet in LUFS but right in LU).

**TEST, 0–180 s, 2026-11-22** (place_sound, the cue sheet + a tiny hand-made marker file exercising the new types —
`work/sound/markers/test_cold.sfx.json`, 20 markers, `--no-hierarchy`; `work/sound/testbed`, WAVs deleted after measuring; build 91 s):
bed −56.4 LUFS (target −54.1 before the duck), peak −38.9 dBFS; duck active 48.0 % of the time, mean −3.45 dB while ducked, max −16.9 dB;
sfx_limit cut 0.0 %; sfx.wav peak −34.3 dBFS; ambience peak −45.2 dBFS.
act_levels (music re VO while he speaks): untrimmed C1 −24.2 · C2 −26.3 · C3 −26.9 → trimmed **C1 −24.5 · C2 −25.3 · C3 −25.3 · window −25.3**.
`tools/audio/vo_music_scan.py --vo project/cartels/media/vo_ct.wav --beds work/sound/testbed --from 0 --to 180` (exit 0;
`work/sound/scan_test_final.txt`, untrimmed `scan_test1_untrimmed.txt` also met all limits):
```
VO -31.2 LUFS-I over 0.0–180.0 s
[0.4 s windows, music] VO speaking 94% · median gap 25.3 LU · p5 19.3 · min 15.8 · windows < 18 LU: 15 (0.9%) in 14 spans
[0.4 s windows, music+sfx] VO speaking 94% · median gap 24.1 LU · p5 18.0 · min 11.6 · windows < 18 LU: 83 (4.9%) in 34 spans
[3.0 s windows, music] VO speaking 100% · median gap 24.1 LU · p5 20.9 · min 19.3 · windows < 18 LU: 0 (0.0%) in 0 spans
[3.0 s windows, music+sfx] VO speaking 100% · median gap 22.9 LU · p5 17.6 · min 15.7 · windows < 18 LU: 127 (7.1%) in 11 spans
[3 s] per-minute min gap (music / music+sfx) while he speaks:
   00:19.7/15.7  01:20.0/16.5  02:19.3/17.8
VERDICT (VO -31.2 LUFS-I):
   PASS  3 s music gap while he speaks — MIN (never closer than 18): 19.3 LU (limit ≥ 18)
   PASS  3 s music gap while he speaks — 5th percentile (at least 20): 20.9 LU (limit ≥ 20)
   PASS  3 s music gap while he speaks — median: 24.1 LU (limit ≥ 20)
   PASS  0.4 s music gap vs local speech level — 1st percentile: 18.2 LU (limit ≥ 15)
   PASS  3 s music+SFX gap while he speaks — MIN: 15.7 LU (limit ≥ 14)
   ALL LIMITS MET
```
`measure_mix.py` on the window (test WAV in /dev/shm, deleted): music while VO speaks −56.2 LUFS (−25.3 LU re VO), SFX under VO median
−27.5 dB re the local VO peak; mix vs VO alone over the same 0–180 s (BS.1770, dual-mono): −28.20 vs −28.19 → **Δ 0.0 LU**. VO md5 unchanged.

## 6. Build / rebuild (one heavy audio job at a time, niced)

```bash
cd /home/user/vox-edit-kit
python3 project/cartels/gen/make_cuesheet.py            # only if the cue tables changed
nice .venv/bin/python tools/audio/place_sound.py --vo project/cartels/media/vo_ct.wav --transcript transcript_ct.json --len 1341.912 \
  --markers 'compositions/cts*.sfx.json' --cues project/cartels/music_cuesheet.json --out assets/audio/cartels
nice .venv/bin/python tools/audio/vo_music_scan.py --vo project/cartels/media/vo_ct.wav --beds assets/audio/cartels   # VERDICT first
nice .venv/bin/python tools/audio/act_levels.py --vo project/cartels/media/vo_ct.wav --beds assets/audio/cartels --cues project/cartels/music_cuesheet.json --len 1341.912
nice .venv/bin/python tools/audio/measure_mix.py --vo project/cartels/media/vo_ct.wav --beds assets/audio/cartels --len 1341.912 --out /dev/shm/testmix_ct.wav \
  && rm -f /dev/shm/testmix_ct.wav
```
Quick test of a window: same place_sound line with `--len 180 --markers 'work/sound/markers/test_cold.sfx.json' --out work/sound/testbed
--no-hierarchy`, scan with `--from 0 --to 180`, then delete the WAVs. **Memory**: a 1342 s build is shorter than NVIDIA's 2402 s (≈ 7.5 GB
peak there) — still run it alone on the box (phase 2). `assets/audio/cartels/*.wav` is gitignored (added 2026-11-22). The Epidemic WAVs are
gitignored: on a fresh machine re-download them first (ids in LOG.md "Cartels (2026-11-22)": 13 tracks ≈ 0.85 GB at 16-bit with only the
used stems, 98 SFX ≈ 0.64 GB at 48 kHz).

## 7. Open questions / phase 2 to-do
1. Whole-length build once the editors' `cts*.sfx.json` exist → scan → act_levels → trims for C4–C21 (aim −22…−25) → measure_mix.
2. Check the editors' markers for types outside §4 (place_sound asserts on unknown types; fix with `marker_edits` retype) and for any
   gunfire/explosion placed close-up or on a person — drop those (BRIEF rule 3).
3. The cliff (C16) is drone-only by design; if Krish wants total silence there, drop the C16 glue and let the scandal track enter at 1017.
4. Sensitive lines with no music push: the ambush deaths 206.5, the boat-strike deaths 666–674 (−3 dB), the witnesses / murders 820–846
   (−2/−3 dB), the cliff 1006–1018 (drone only), the clinic 1220.5 (inside DB Cooper's peak — phase 2: consider a −2 dB `auto` dip there).
5. The VO is −32.1 LUFS-I; the finished mix will read ≈ −32. A louder delivery is a whole-mix decision for the lead, never the VO alone.
