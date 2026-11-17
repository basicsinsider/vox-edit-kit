# "NVIDIA" sound plan — Is the chip ban actually working?, master 0.00–2402.00 s (`project/nvidia/media/vo_nv.wav` = `vo_nv.mp3`)

Sound designer, phase 1 (2026-11-17). Sources: MANUAL §0, §7, §10.3, §10.8 (incl. "Music limits — BINDING", the Ivan and Paraguay notes);
SEGMENTS.md §3 (story per segment), §6 (tone: an investigation told even-handedly, a little wry; worlds SERVER HALL / WASHINGTON
PAPERWORK / MAP; motifs THE SCOREBOARD and THE LINE); quality bar `project/paraguay/SOUND_PLAN.md`. Tracks / ids / §10.8 checks:
`assets/audio/epidemic/LOG.md` ("NVIDIA" sections). Measured stems, sections, keys: `assets/audio/epidemic/ANALYSIS.md`. Cue sheet =
`project/nvidia/music_cuesheet.json`, **generated** by `project/nvidia/gen/make_cuesheet.py` (edit the tables there, re-run, rebuild §6).
All music = Epidemic Sound, one key family **C minor / Eb major** (new: Ivan + Taiwan D minor / F, Paraguay E minor / G, the podcast
A minor / C). Tone: investigative tech documentary — cold, pulsing, textural (Melting Glass lineage): electronic pulses for the server hall,
contemporary-classical suspense for Washington, wry floating electro for Sam's asides, hopeful strings only for job two's ✓. No trailer action.

## 0. Measured facts (ffmpeg ebur128 / numpy, 2026-11-17; `work/nv-sound/vo_ebur128_summary.txt`, `vo_stats.txt`)

| | value |
|---|---|
| `vo_nv.wav` (= `vo_nv.mp3`, 48 kHz, 2400.62 s) | **−29.8 LUFS-I**, true peak −4.8 dBTP, LRA 8.8 LU (low −35.4 / high −26.6). Quiet (Ivan-like) → every threshold is relative to it. Never processed. |
| VO 10 s windows | −26.3 … −38.6 LUFS; quietest 500 s (−38.6), 700–880 (−36…−37.5: the anecdotes / big fish), 2330; loudest 1440, 1810, 2040, 2180 (−26.3…−26.8) |
| VO per act (LUFS-I) | A0 0–162 −29.7 · A1 162–362 −30.7 · A2 362–935 **−32.7** · A3 935–1595 −29.3 · A4 1595–2147 −28.2 · A5 2147–2352 −29.6 · A6 2352–2401 −33.2 |
| Activity gate | 20 ms frames: floor −65…−75 dBFS, speech median −39.7; place_sound's gate `min(−45, VO_LUFS − 13.5)` = **−45 dBFS** → 84 % active, **185 pauses ≥ 0.6 s** (median 0.70 s, max 1.82 s at 1571.0) — works at this level, no tool change needed |
| Speech density | 7730 words, **3.22 words/s** (10 s p10 2.6 / p90 3.8); 115 of 240 windows ≥ 3.3 w/s; densest 2060, 2360, 1470 (4.4–4.5 w/s). Few breaths → the cue sheet thins layers by hand (`auto` dips) under the dense explanations |
| Bed target | `bed_lu_under_vo` **22** → −51.8 LUFS before the duck; the duck (gap 20 / gap_fast 18 / ceiling 20) takes ≈ 2 dB → ≈ **VO − 24 LU** while he speaks |
| Insert clips with their own audio | none planned (all footage muted) → no `ducks`; bleeps none (no swearing in the script) |
| Room tone / library loops | AMB_SCALE = db(min(0, VO + 25)) = **−4.8 dB** (the Ivan scaling) |

## 1. Layers (vocabulary) — `assets/audio/epidemic/<track>/<track>_<stem>.wav`, all C minor (r 0.64–0.87)

| layer | track (stems used) | LUFS-I full / stems | bpm | sections (s, ANALYSIS) | role |
|---|---|---|---|---|---|
| **DRONE** | `flute` bass (instruments = faint air, 14 LU under) — pulse 1.1 / 1.4, Σ stems = full (−78 dB) | −15.6 / bass −15.7 | free | rises 0–40, steady to 247 | glue under every join; alone for the verdicts and the iPhone memory |
| **COLD PULSE** | `seventy_seven_cycles` instruments, melody, bass | −13.4 / −19.3, −19.5, −14.7 | 170 | steady 0–54, peak 54–67, 83–99, drop 99–107, quiet 107–118 | cold open (HK mall → Shenzhen → servers); "the ban works" (60 → 80 %, DeepSeek dark) |
| **THE QUESTION** | `unsolved_issues` instruments, melody, bass | −14.4 / −19.5, −16.1, −18.5 | 100 | build 126–129, peak 129–133, drop 133–140, peak 154–161, drop 165–171 | "Was the chip ban a mistake?" ↔ "So why do they still have this ban?" ↔ "I don't think it's working" |
| **PAPERWORK** | `cinema_neon` full (stems 10–17 LU under it) | −10.1 | 97 | quiet 0–8, steady, drop 167–173 | what the ban is; three ways to measure; volume → yield |
| **INVESTIGATION** | `the_investigator` instruments, bass, melody (Σ clean −20.6 dB) | −14.2 / −20.1, −16.2, −19.3 | 113 | quiet 44–54, build 54–57, steady 57–110, peak 133–146, drop 153–157 | "is it fair?"; the factors nobody says aloud → the chart |
| **DUAL USE** | `subconscious` full | −16.1 | 100 | peak ≈ 211, steady 81–177 | uranium → bomb → Taiwan; the US government's unseen test |
| **AMERICAN LAW** | `gnomon` instruments, melody, bass (drums not used) | −14.2 / −26.8, −24.0, −24.2 | 120 | quiet 0–12, steady 12–73, drop 73–88, build 88–95, peak 95–119 | scoreboard → design IP → "every chip on the planet"; Huawei → Lutnick → the port |
| **CAT AND MOUSE** | `shifting_angles` instruments, bass, drums (drums only under the peak) | −15.2 / −20.9, −18.9, −17.3 | 84 | quiet 61–69, build 69–72, drop 110, build 128–131, peak 149–184, drop 184–190 | THE LINE (job one); distillation's cat and mouse |
| **WRY** | `hidden_room` instruments, bass | −16.9 / −19.2, −21.3 | 80 | quiet 0–20, steady 20–123, drop 123–128 | PlayStation → Marketplace → $2,000; iPhone 1 vs iPhone 18 |
| **CAPER** | `operation` instruments, melody, bass, drums (drums only under the camera peak) | −13.2 / −16.4, −19.2, −21.4, −14.3 | 110 | steady 24–83, peak 83–112, drop 112–116 | the big fish: co-founder → hair dryer → warehouse camera |
| **SERVER HALL** | `pinnacle` full (stems 6–18 LU under, Σ ≠ full) | −15.9 | 110 | steady 20–72, quiet 72–90, build 90–96, peak 96–121 | training → the rack → Memphis → 7 % |
| **THE TURN** | `breath_by_breath` instruments, melody, bass | −11.9 / −18.7, −14.0, −15.3 | 68 | steady 41–114, **peak 114–162** | labs share attacks → gap widening → ✓ "one to one" |
| **JOB THREE** | `the_northern_cliff` instruments, melody, bass | −12.4 / −17.5, −14.5, −16.3 | 120 | quiet 22–57, build 57–60, drop 85–89, build 120–128, peak 128–168 | Jensen's argument → keyboard → 95 % → 0 % → Huawei |
| **LEVEL FOUR** | `across` instruments, bass, melody (nearly tempo-free: full 2.8, bass 1.2) | −14.4 / −16.4, −20.3, −17.4 | free-ish | quiet 9–48, build 48–52, build 134–143, peak 143–154, build 175–180, quiet tail 253–285 | Malaysia → flying with the data → the debate → "?" → outro |

Rules kept from Ivan/Paraguay: one rhythmic track at a time (tracks change only at act boundaries, the tempo-free DRONE bridges every join);
stems of one track keep the same offset; exits on beats quick (0.4–1 s), entries slow (2–4 s); a track returns only where the story rhymes
(77 Cycles = chips getting in ↔ how few they are; Unsolved Issues = THE QUESTION, three times; The Investigator = fairness ↔ suspicion;
Shifting Angles = the two cat-and-mouse games; Gnomon = American law ↔ the Commerce Secretary; Hidden Room = PlayStation ↔ iPhone 1;
Cinema Neon = the explainer colour).

## 2. Act map and cue sheet (master seconds; offset = read position in the file at the layer's start; full notes in make_cuesheet.py)

| act (brief) | cue | story (SEGMENTS §3) | in → out | layers | moves on words |
|---|---|---|---|---|---|
| **A0 cold open + intro 0–162** | N1 | nvs01: the question → CEO news → HK mall → Shenzhen → servers → caveat → Megaspeed | 0 → 115.5 | COLD PULSE instr + melody @0, bass @38.7 from 38.7; DRONE 100–124 | pulse from frame 1 under "Is the chip ban actually working?" 0.16; melody −3 dB under the sensitive CEO lines 11–25, up on "a shopping mall in Hong Kong" 40.6; bass on "Take a look at this video" 38.7; file peak 54–67 = ferry → Shenzhen → "a room full of NVIDIA GPUs"; −2 dB from "there is a caveat" 82.4; drop on "Singapore, Malaysia" 101.8 |
| | N2 | nvs02: 60 % / 17 % → catching up → **"Was the chip ban a mistake?"** | 112 → 163 | THE QUESTION instr @95.5, melody 127–158, bass 135–160; DRONE 152–176 | its build + peak land on "raises an important question" 142.0 → "mistake?" 147.72 (stinger); drop on "why do we still have it?" 148.3 |
| **A1 what the ban is 162–362** | N3 | nvs02: a US law → machines → October 7th 2022 → Biden/Trump → back and forth | 162.6 → 229.6 | PAPERWORK full @0 (TRIM +7, see §5); DRONE 222–246 | quiet entry under "basically a US law" 167.9; −2 dB under the dense extended / rolled back 205–229 |
| | N4 | nvs03: is it fair? free trade → Google/Facebook/YouTube banned → IP theft → WTO | 231 → 314.5 | INVESTIGATION instr @44, bass @57 from 244, melody @79 from 266 (TRIM +1); DRONE 306–330 | build on "the fair part" 243.4; steady under the ban list 271 → IP theft 296 → WTO 303; fades on "let's go even deeper" 314.5 |
| | N5 | nvs03: uranium → bomb → enriched uranium → AI → Taiwan → "the main question" | 316 → 352.5 | DUAL USE full @195; DRONE 345–378 alone 352.5–363 | its 211 s peak under "a nuclear bomb" 325 → Taiwan 343.9–351; drone only for "is that ban working or not" 358.9 |
| **A2 scoreboard + job one 362–935** | N6 | nvs04: define working → THE SCOREBOARD → design IP → "every chip on the planet is under American law" | 363 → 472.6 | AMERICAN LAW instr @0, melody @12 from 375, bass @88 from 451; DRONE 466–492 | steady under the scoreboard 386 → "made in Taiwan" 417.6; drop/quiet = design 422–441; build → peak = "every chip on the planet" 462.7–469.2; cut on "job number one" 472.75 |
| | N7 | nvs05–06: THE LINE → two chips → devastating → a chip on the line → the line moves → "the very next day" | 473.5 → 603.5 | CAT AND MOUSE instr + bass @61 (473.5–529) then @123 (536–603.5), drums @149 562–597.5; DRONE 520–548 | build on "a chip ban for a reason" 483.7; drop = "devastating…a quarter" 518.5; build = "a brand new chip" 542.5; peak = "moves the line" 565.5 → the quote; drop on "the very next day" 598.8 |
| | N8 | nvs06–07: the PC aside → PlayStation → individuals → Marketplace → $2,000 → iPhone memory | 600 → 790 | WRY instr @0 600–731, bass @47 647–728; DRONE 722–790 alone for the iPhone memory | quiet under "you guys can't see it" 604; steady under PlayStation 615–631 → Marketplace 662.6 → "Imagine this video bombs" 669.5; drop = "That's how people look at it" 727.7. VO quietest here (−36…−38) — the duck follows it |
| | N9 | nvs08: the big fish → $1.5 billion → fake company → hair dryer → the warehouse camera | 776 → 866 | CAPER instr + bass @24.5, melody 800–866, drums @82.5 834–864 | steady under the arrest 782.9 → $1.5 billion 792.8; −1.5 dB under the auditors / hair dryer 808–826; peak = "The warehouse camera was recording" 834.7 → "So he was caught" 838.7; drop = the verdict 864.8 |
| | N10 | nvs09: VERDICT job one **✗** → "a joke"? → why keep it → keep the LEAD | 860 → 950 | DRONE 860–902 alone (near-silence for the verdict); THE QUESTION instr @100 890–936, melody 905–934; DRONE 928–950 | stinger "it's not working" 889.0; the question theme returns on "So why do they still have this ban?" 905.5 → peak on "keep the lead" 922.0 |
| **A3 job two 935–1595** | N11 | nvs10: training → cluster → the rack (refrigerator, 3,000 lb, 100 homes) → Memphis → 7 % | 936.5 → 1047 | SERVER HALL full @16; DRONE 1040–1056 | quiet = "thousands of racks" 994.5 → "so hard to smuggle" 1003.7; peak = Memphis 1016.2 → "more computing power" 1023.6 → 7 %; drop = "the ban is working" 1046.1 |
| | N12 | nvs11: 60 % → 80 % → China 1 % → cut 80 % → ByteDance → DeepSeek dark → leaked call → irony | 1047.5 → 1174.6 | COLD PULSE instr @0, bass 1050–1146, melody 1100–1146; DRONE 1166–1186 | peak = "DeepSeek went dark" 1105.6; 83–99 peak = "not enough chips" 1134–1139; quiet under the electricity irony 1139.8–1168 |
| | N13 | nvs12–13: three ways to measure → tests → the government's unseen test → caveats → "much larger?" | 1176 → 1357 | PAPERWORK full @57 1176–1261; DUAL USE full @81 1259–1357; DRONE 1250–1270, 1349–1364 | −2 dB under "building models to succeed in these tests" 1232–1259 and the unseen-questions explanation 1278–1300 |
| | N14 | nvs14–16: factors nobody says → the chart → distillation → fake accounts → labs share attacks → gap widening → **✓ "one to one"** | 1357 → 1596 | INVESTIGATION instr + bass @57, melody 1405–1453; CAT AND MOUSE instr + bass @131 1454–1512; THE TURN instr @46 1511–1596, melody 1540+, bass 1560+; DRONE 1446–1462, 1588–1606 | peak = "Take a look at this chart" 1428.6 → "suspicious" 1442.3; drop = "distillation" 1451.7; peak = "cat and mouse game" 1473.7 → fake accounts 1484.2; Breath by Breath's 114 s peak = "it is working" 1576.6–1582.5 → "one to one" 1590.5 (stinger); out on "job three" 1595.2 |
| **A4 job three 1595–2147** | N15 | nvs16–17: Jensen's argument → a competitor → hooked on American chips → keyboard → biased → 95 % → 0 % → Huawei | 1596 → 1748 | JOB THREE instr @22, melody 1631–1748 (−3 dB 1663–1693), bass @122 1696+; DRONE 1740–1756 | build = "built on American chips" 1631; drop = "biased" 1661.7; build = "keeping China hooked" 1698.3; peak = 95 % 1704 → 0 % 1711.3 → "the answer is Huawei" 1742.2 |
| | N16 | nvs17–18: Huawei scales → the Commerce Secretary → Lutnick's quote → China blocks → 600,000 at a port | 1745 → 1857 | AMERICAN LAW instr + melody @12 (melody −4 dB under the quote), bass @88 1821+; DRONE 1850–1866 | drop/quiet = the Lutnick quote 1801.5–1820.3; peak = "China itself is kind of blocking" 1835.9 → "600,000 chips…on a port" 1844.9; drop = "Why is the CCP doing this?" 1853.5 |
| | N17 | nvs18–20: volume → yield → Texas Instruments → 10 / 30 / 99.x % → TSMC | 1856 → 2027 | PAPERWORK full @0 (−2 dB 1942–1968); DRONE 2016–2034 | steady under volume 1873.8 → yield 1882.3 → Texas → 99.3 % 1919.9 → TSMC 1926.8 |
| | N18 | nvs20: 60 % again → iPhone 1 vs iPhone 18 → 10 % → the CCP's plan | 2027 → 2104 | WRY instr @20, bass @53 2060+; DRONE 2096–2156 | "Imagine you have an iPhone 1" 2026.7 → "10%" 2066.8 → "Not as scary" 2074 |
| | N19 | nvs21: more questions → SCOREBOARD job three **✗** → "let's talk about level four" | 2105 → 2151 | THE QUESTION instr @120 (third time) | its 154–161 peak = "I don't think it's working" 2139.62 (stinger); drop = "level four" 2147.0 |
| **A5 level four 2147–2351** | N20 | nvs21–23: the loophole → Malaysia → renting → "perfectly legal" → flying with the data → the debate | 2150 → 2352 | LEVEL FOUR instr @18, bass @48 2180+, melody @134 2266+ (−1.5 dB 2207–2236, 2314–2340) | build on "data centers in Malaysia" 2182.7; build = "The funniest part" 2268.2, peak = "flying to Malaysia with…the information" 2280.6; build = the debate 2307.3 |
| **A6 outro 2351–2402** | N21 | nvs23: SCOREBOARD row four **"?"** → comments → "My name is Sam" → fade to night | 2351 → 2402 | LEVEL FOUR instr @219 (its quiet tail, −3 → −6 dB from 2390); DRONE 2344–2402 | "I don't know how to rank this part" 2354.19 (stinger); fades with the picture to 2402.0 (no hold past the master) |

## 3. Stingers (cue sheet `stingers`, synced on the file's loudest point; word times checked in `transcript_nv.json`)

| s | word | sound | rel LU re VO |
|---|---|---|---|
| 147.72 | TITLE QUESTION "Was the chip ban a **mistake?**" (146.36–148.28) | `swell_reverse_timpani_cymbal` (peaks on the word) | −30 |
| 889.00 | SCOREBOARD job one ✗: "…it's not **working.**" | `boom_dark_cinematic_low_hit` | −28 |
| 1590.50 | SCOREBOARD job two ✓: "So the score is **one to one.**" (after "it is working" 1576.6–1582.5) | `boom_sub_bass_clean_01` (felt, not heard) | −31 |
| 2139.62 | SCOREBOARD job three ✗: "I don't think it's **working**" | `boom_dark_cinematic_low_hit` | −28 |
| 2354.19 | SCOREBOARD row four "?": "I don't know how to **rank** this part" (from "Now, I'll be very honest" 2351.55) | `riser_reverse_cymbal_short` | −31 |

Stingers are 3–7 dB quieter than Paraguay's (binding limits; the duck runs after them). An editor's `boom_low` / `riser` within ±0.6 s of a
stinger is dropped automatically; in phase 2 prefer the editor's picture-synced boom when they are < 2.5 s apart (MANUAL §10.8).

## 4. SFX / ambience palette for the editors (`compositions/nvsNN.sfx.json`, master seconds; format as Paraguay §4)

Existing types cover most of the edit (the 12 wave-1 files use paper_slide, whoosh_soft/whoosh/whoosh_big/whip, pop_soft, marker_scratch,
pin_pop, counter_ticks, stamp_thud, map_pin, dot_ticks, pencil_scribble, highlighter_swipe, crt_*, factory_hum, keyboard, glitch …).
**24 new Epidemic SFX** (ids in LOG.md "SFX added for NVIDIA"; all 48 kHz/16-bit) give the NVIDIA worlds their own sound. Proposed marker
types — **wired into place_sound in phase 2** (until then place_sound asserts on unknown types, so editors keep to existing types or write
the proposed name only after phase 2 lands):

| proposed type | file(s) | use on |
|---|---|---|
| `server_room` (ambience, dur; note "big/hall" → data_server_room_hum_01) | server_room_medium_roomtone, data_server_room_hum_01 | SERVER HALL scenes: racks, clusters, Memphis, Malaysian data centers (≈ VO − 26 LU) |
| `fans_spin` (dur) | computer_fans_power_up_down | the PC aside 604; a rack powering up |
| `power_down` | electric_motor_shutdown_01 | "DeepSeek went dark" 1105.6, features switched off, "switch the data centers off" |
| `electric_hum` (ambience, dur) | electrical_hum_lights | 100 homes / 800,000 homes, "China has the electricity" |
| `liquid_cool` (dur) | water_pipes_flowing_03 | liquid cooling / plumbing of the rack 985 |
| `data_process` (dur) / `ui_beep` | data_processing_digital_buttons, data_processing_loading_21 / ui_beep_computer_short | training, test scores, fake accounts, distillation, logins |
| `flipdot` (scoreboard row flip) | relay_flipdot_metal_01, relay_flipdot_plastic_02 (alternate) | THE SCOREBOARD rows (nvs04, 09, 16, 21, 23) |
| `marker_line` (dur) | marker_on_paper_stroke, marker_on_paper_writing_01 | THE LINE being drawn / moved (nvs05–06) |
| `marker_tick` / `marker_cross` / `marker_scrub` | marker_notebook_tick / marker_on_paper_writing_01 / marker_scrub_out_01 | scoreboard ✓ / ✗ / "?" (the stingers carry the weight; keep these soft) |
| `lens_zoom` / `cctv_servo` | camera_lens_motor_zoom / servo_camera_turn_on_off | the warehouse camera 834.7 (security-monitor screen) |
| `barcode_scan` | barcode_checkout_scanner | swapped barcodes / auditors 808–826 |
| `hair_dryer` (dur) | hair_dryer_running | the hair-dryer trick (very low, ≤ 2 s) |
| `port` (ambience, dur) + `ship_horn` | harbor_container_terminal_01 + ship_horn_distant_big | "600,000 chips are sitting on a port" 1844.9 |
| `ferry_horn` | ferry_horn_medium | "a short ferry ride…Shenzhen" 54.96 |
| `market_walla` (ambience, dur) | street_market_walla_01 | the HK mall / Huaqiangbei 40–65 |
| `airport` (ambience, dur) | airport_departure_lounge | individuals carrying chips 647; employees flying to Malaysia 2280 |

Already in the library for the rest: whooshes, booms, riser/swell, paper slides, marker circle/drag, highlighter, rubber stamp, jets
(routes on the maps), typewriter, keyboard, glitch, office/factory ambiences, crowd murmur (Senate/press). Editors never add music; one hero
per scene + camera moves (the §10.8 restraint pass drops the rest). SFX caps are the binding −16 / −19 / −22 dB under the VO's local peak.

## 5. Levels

Binding limits (MANUAL §0 / §10.8) are hard-coded in make_cuesheet.py and asserted before writing: `bed_lu_under_vo` 22, `vo_duck`
gap 20 / gap_fast 18 / ceiling 20 / margin 0.7 / 3 passes / max −30 dB, `pause_lift_db` 0. Per-act aim −20…−24 LU re VO while he speaks.

Trims (`TRIM`): N2 +1, N3 +7, N4 +1 dB — Cinema Neon's quiet opening measured −27.5 LU re VO on the first test (N1 −23.6, N2 −24.1,
N4 −24.0). Each +dB on a quiet act buys only ≈ 0.5 LU: the bed is normalised to VO − 22 over the build window and the duck then caps every
3 s window at ≥ 20 LU under, so the acts converge on ≈ −24. Phase 2 must re-run `act_levels.py` on the whole-length build (the
normalisation then runs over 2402 s) and trim N5–N21 the same way (aim −22…−24).

**TEST, 0–300 s, 2026-11-17** (place_sound, music only, no markers; `work/nv-sound/testbed`, WAVs deleted after measuring; build 50 s):
bed −53.9 LUFS (target −51.8 before the duck), peak −36.3 dBFS; duck active 48.8 % of the time, mean −3.4 dB while ducked, max −15.4 dB.
act_levels (music re VO while he speaks): **N1 −24.1 · N2 −24.2 · N3 −23.9 · N4 −23.8 · whole window −24.0**.
`tools/audio/vo_music_scan.py --vo project/nvidia/media/vo_nv.wav --beds work/nv-sound/testbed --from 0 --to 300` (exit 0):
```
[0.4 s windows, music] VO speaking 97% · median gap 24.3 LU · p5 19.1 · min 16.7 · windows < 18 LU: 18 (0.6%) in 17 spans
[3.0 s windows, music] VO speaking 100% · median gap 23.0 LU · p5 20.8 · min 19.2 · windows < 18 LU: 0 (0.0%) in 0 spans
[3 s] per-minute min gap (music / music+sfx) while he speaks:
   00:19.8/19.8  01:19.7/19.7  02:19.8/19.8  03:19.7/19.7  04:19.2/19.2
VERDICT (VO -30.2 LUFS-I):
   PASS  3 s music gap while he speaks — MIN (never closer than 18): 19.2 LU (limit ≥ 18)
   PASS  3 s music gap while he speaks — 5th percentile (at least 20): 20.8 LU (limit ≥ 20)
   PASS  3 s music gap while he speaks — median: 23.0 LU (limit ≥ 20)
   PASS  0.4 s music gap vs local speech level — 1st percentile: 18.2 LU (limit ≥ 15)
   PASS  3 s music+SFX gap while he speaks — MIN: 19.2 LU (limit ≥ 14)
   ALL LIMITS MET
```
(Full output `work/nv-sound/scan_test_final.txt`; the untrimmed first pass `scan_test1.txt` also met all limits.) Tools: no threshold broke
at −29.8 LUFS (gate −45 dBFS catches 84 % active frames, 185 pauses; vo_duck / scan are relative to the measured VO) → no tool changes.

## 6. Build / rebuild (one heavy audio job at a time, niced)

```bash
cd /home/user/vox-edit-kit
python3 project/nvidia/gen/make_cuesheet.py            # only if the cue tables changed
nice .venv/bin/python tools/audio/place_sound.py --vo project/nvidia/media/vo_nv.wav --transcript transcript_nv.json --len 2402.0 \
  --markers 'compositions/nvs*.sfx.json' --cues project/nvidia/music_cuesheet.json --out assets/audio/nvidia
nice .venv/bin/python tools/audio/vo_music_scan.py --vo project/nvidia/media/vo_nv.wav --beds assets/audio/nvidia   # VERDICT first
nice .venv/bin/python tools/audio/act_levels.py --vo project/nvidia/media/vo_nv.wav --beds assets/audio/nvidia --cues project/nvidia/music_cuesheet.json --len 2402.0
nice .venv/bin/python tools/audio/measure_mix.py --vo project/nvidia/media/vo_nv.wav --beds assets/audio/nvidia --len 2402.0 --out renders/testmix_nv.wav \
  && rm -f renders/testmix_nv.wav
```
Quick test of a window: same place_sound line with `--len 300 --markers 'compositions/none_*.sfx.json' --out work/nv-sound/testbed`, scan
with `--from 0 --to 300`, then delete the WAVs. **Memory**: a whole-length build peaks at ≈ 7.5–10 GB (2402 s is the longest bed so far) —
run it alone on the box (phase 2, not now). The Epidemic WAVs are gitignored: on a fresh machine re-download them first (ids in LOG.md
"NVIDIA": 14 tracks ≈ 1.86 GB + 29 SFX ≈ 152 MB).

## 7. Open questions / phase 2 to-do
1. Wire the §4 proposed types into `place_sound.py` (GAIN / AMBTYPES / RANK / aliases) before the editors' final markers are built.
2. Wave-1 markers use two unknown types: `drop` (1×) and `stamp` (1×, aliased → rubber_stamp). `drop` must be aliased or fixed with a
   `marker_edits` retype, or place_sound's assert stops the build.
3. Whole-length act_levels trims for N5–N21 (§5); watch A2 (VO −32.7 LUFS, the quietest act) and the outro (−33.2).
4. The VO is −29.8 LUFS-I; the finished mix will read ≈ −29.7. A louder delivery is a whole-mix decision for the lead, never the VO alone.
5. Sensitive CEO lines (11–25, 2355–2362, 2385): the melody is held −3 dB under 11–25 and no stinger sits on them.
