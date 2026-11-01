# "Ivan" sound plan — Searching Lessons, master 0.00–949.00 s (`vo_iv.mp3`)

Sound designer. Sources: MANUAL §7, §10.3, §10.8; SEGMENTS.md §3 (story per segment), §1 (insert slots); worked example
`project/intro/SOUND_PLAN.md`. Tracks / ids / why: `assets/audio/epidemic/LOG.md` ("Ivan" sections). Measured stems, sections, keys:
`assets/audio/epidemic/ANALYSIS.md`. Cue sheet = `project/ivan/music_cuesheet.json`, **generated** by
`project/ivan/gen/make_cuesheet.py` (edit the tables there, re-run, rebuild §6). All music = Epidemic Sound (Krish's subscription),
one key family **D minor / D (modal) / F major**. Tone: tense, intimate, investigative — dark pulses, drones, contemporary-classical
tension; no trailer action.

## 0. Measured facts (ffmpeg ebur128 / numpy, 2026-11-01)

| | value |
|---|---|
| `vo_iv.mp3` (= `vo_ivan_master.wav`) | **−36.8 LUFS-I**, sample peak −12.1 dBFS, LRA 7.3 LU. ~10 dB quieter than the Taiwan VOs (−24…−27). Never processed. |
| Bed target | **VO − 14 LU = −50.8 LUFS** (sum of all layers, `bed_lu_under_vo` 14); per act −12.5…−16 LU re the VO while he speaks (§5) |
| VO activity gate | the old fixed −45 dBFS gate caught only 50 % of in-word 20 ms frames of this quiet VO → place_sound now gates at `min(−45, VO_LUFS − 13.5)` = −50.3 dBFS |
| Speech density | 2.2–3.7 words/s; densest windows 30–50, 270–280, 370, 450, 560, 620–630, 730, 870, 900 s → the cue sheet thins layers there (`auto` dips, drums out) |
| Insert clips (own audio) | insert1 **−15.8 LUFS** (peak −1.0), insert2 **−25.5 LUFS** (peak −4.4), insert3 **−14.5 LUFS** (peak −0.3, LRA 12.7: loud FPV/impact first 5 s ≈ −13 S, then decays to −25) — 21 / 11 / 22 LU louder than the VO |
| Music under the inserts | measured −69.5…−70.0 LUFS (≈ 31 LU under the inserts at the recommended gains): near-silent |
| Room tone / library loops | scaled by `db(VO_LUFS + 25)` (AMB_SCALE) so they stay ≈ 30 LU under this quiet VO (unscaled they sat 20 LU under) |

### Recommended insert gains (the clips are the foreground in their slots; target ≈ the VO's speech loudness)
| slot | master | measured | target | **gain** | why |
|---|---|---|---|---|---|
| 1 protest chants | 108.700 (8 s) | −15.8 LUFS | ≈ −38.5 (VO −1.7) | **−22.5 dB** | crowd chant, constant level; a touch under the voice |
| 2 Moscow resident (Kirillov site) | 407.900 (18 s) | −25.5 LUFS | ≈ −37.5 (VO −0.7) | **−12 dB** | speech: match the narrator |
| 3 SBU FPV drone | 532.917 (11 s) | −14.5 LUFS | ≈ −39 (VO −2) | **−24.5 dB** | loud impact transient (peak → −24.8 dBFS, still under the VO's −12.1) |
`G1=-22.5 G2=-12 G3=-24.5 tools/final_mix_ivan.sh <picture.mp4> <out_dir>` (the script's env gains). Note for the lead: with the VO
untouched at −36.8 LUFS the finished mix is ≈ −36.5 LUFS integrated — very quiet for YouTube (≈ −14); any loudness lift has to be a
decision about the whole mix (MANUAL §0 forbids touching the VO alone).

## 1. Layers (vocabulary)

| layer | file(s) `assets/audio/epidemic/<track>/<track>_<stem>.wav` | LUFS-I | bpm / bar | sections used |
|---|---|---|---|---|
| **DRONE** | `woodwind_reviere_bass` (+ `_instruments` = air) | −14.4 / −23.3 | free | steady 18–201 |
| **COLD / MYSTERY** | `code_of_violence_instruments`, `_bass`, `_drums` | −16.6 / −17.6 / −19.3 | 102 / 2.35 s | quiet 4–41, build 41–44, steady 44–100, peaks 100–107, 118–123 |
| **INVESTIGATION** pulse | `tracker_full` (stems don't carry the melody) | −10.7 | 90 / 2.67 s | steady 0–145 |
| **TENSION** | `estimations_instruments`, `_bass`, `_drums` | −19.1 / −18.0 / −34.7 | 117 / 2.05 s | quiet 0–27, steady 27–120, peaks 120–123, 143–173 |
| **SPIDERWEB** | `close_call_instruments`, `_bass`, `_drums` | −15.4 / −17.6 / −14.6 | 84 / 2.86 s | build 36–41, peak 41–65, quiet 71–97, build 97–104, peak 104–134, drop 134–141 |
| **SUSPENSE** | `make_way_for_hearses_full` | −15.3 | 90 / 2.67 s | steady 34–73, drop 73–79, quiet 79–94, build 94–99, steady 99–116 |
| **REFLECTION** | `letters_never_sent_instruments`, `_bass` | −16.9 / −16.4 | 80 / 3.0 s | peaks 101–113, 128–134, 141–160, dip 164–168, build 168–175, peak 175–183 |
| heartbeat | `sfx/heartbeat_cinematic_54bpm.wav` (cue-sheet layer with `"file"`) | — | 54 | under "explosives in his car" |

Rules kept from the intro: one rhythmic track at a time (tracks change only at act boundaries, the tempo-free DRONE bridges the joins);
stems of one track keep the same offset (sample-aligned); exits on beats are quick (0.12–0.6 s), entries slow (1–3 s); a track returns
only where the story rhymes (Code of Violence = Ivan's mystery, cold open ↔ M7; Tracker = sabotage/investigation, M3 ↔ M9).

## 2. Cue sheet (master seconds; offset = read position in the file at the layer's start)

| # | story (SEGMENTS §3) | in → out | layers | moves on words |
|---|---|---|---|---|
| M1 | Cold open: Ivan's double life, patriot, why, the network, opposition → invasion | 0.00 → 108.5 | DRONE @20; CODE OF VIOLENCE instruments @4 (quiet intro), bass from "But what most of them don't know" 13.84, drums 47.44–81.0 and 97.85–108.5 | its build lands on "the only way…Putin's government" 38.9–40.4; thinned 31–51 (dense); peak + 3 dB on "full-scale invasion…February 2022" 104.25/105.21; out 107.9–108.5 |
| — | **insert 1** protest chants | 108.7 → 116.7 | DRONE only, whole bed −16 dB (duck) | SFX/ambience muted |
| M2 | protesters, new laws, arrests, exodus | 116.73 → 131.8 | DRONE + DRONE-air (sombre) | — |
| M3 | Ivan decides → Mamoń → strange videos → verifying → GUR confirms → Kazakhstan/Tatarstan → satellite aside | 131.78 → 257.0 | TRACKER full @0 (fade-in 2.5 s), −2 dB until 140 | lift on "that part of his story checked out" 212.91; −1.5 dB under the satellite face-cam aside 239–256 |
| M4 | the five-hour assignment → normal day → Foma (Warsaw) → network → 25 years → over their shoulders → Kirillov | 256.26 → 407.6 | ESTIMATIONS instruments @0.1 (offset puts the file's 143 s peak on "killed" 399.16), bass 266.18–296.18 and from "FOMA's network" 327.43, drums from "Well, he wanted officers…" 383.64; DRONE glue 252–300 | −1.5 dB 271–281 (dense); +1.5 dB from 399; out 407.3–407.6 |
| — | **insert 2** Moscow resident at the blast site | 407.9 → 425.9 | DRONE only, ducked −16 dB | SFX/ambience muted |
| M5 | Sarvarov car bomb → Foma's people tracked him → two and two → officers unsettled | 425.96 → 471.0 | ESTIMATIONS instruments + bass @160 (inside the peak), drums 428.2–441; DRONE-air from 459.45 | +1.5 dB on "exploded" 435.77; −2 dB 449–458 (dense) |
| M6 | Operation Spiderweb: far airfields → June 1st drones → flames → SBU, 18 months → four cargo trucks → **insert 3** → Tu-95/Tu-22M3 → 41 / at least 10 → no airfield safe | 474.57 → 595.0 | CLOSE CALL instruments + bass @18.6; drums 496.96–521.2 and 559.39–590.11 | build → peak exactly on "On June 1st" 496.96; quiet section under trucks + insert 3 (ducked); build → peak on the losses 560–590; drop on "wasn't actually safe anymore" |
| M7 | Ivan foresaw it → "Now I want to be clear" → SBU ≠ GUR → Yelabuga → towers → Foma's theory → "one thing he couldn't understand" | 594.35 → 675.4 | CODE OF VIOLENCE instruments @44, bass 597.71–617.36 and 630.96–675.4, drums 636.96–664.56 | −2 dB under the face-cam clarification 617.6–630.5; its 118–123 peak on "one thing…couldn't understand" 668–673; out 675.0–675.4 |
| M8 | how was he never caught → double agent? → Warsaw → handler can't rule it out → silence → back in touch → car inspection → **explosives** → fear | 675.59 → 767.3 (+ tail to 784) | MAKE WAY FOR HEARSES full @13.6; DRONE 735–790; DRONE-air 741–756 (the silence) and 767.38–784; heartbeat 767.38–775 | drop on "stopped answering his messages" 736; quiet on "weeks…months…nothing"; build on "stopped…inspect his car" 756–761; **music cut dead on "explosives" 767.38** + low hit + heartbeat |
| M9 | trains, Freedom of Russia, locomotives, 300–500, tiny fraction, the flip side | 781.2 → 860.0 | TRACKER full @20 | −2.5 dB on "tiny fraction…overthrowing Putin" 827–841; +0.5 lift on "But the flip side" 841.59 |
| M10 | uncomfortable reality → who can you trust (both sides) → will it bring change → "Putin won't live forever" → risk everything | 858.23 → 949.0 | LETTERS NEVER SENT instruments @93.2, bass from 865.66; DRONE 850–949; DRONE-air from 919.13 | its peak on "Russians themselves" 865.66–869; −2 dB 873–905 (dense); its dip under "Putin won't live forever" 928.49; build → peak on the last line 940.2–946.8; fade out 947–949 |

## 3. Stingers (cue sheet `stingers`, synced on the file's loudest point)

| s | word | sound | rel LU re VO |
|---|---|---|---|
| 104.25 | "full-scale **invasion**" | `boom_cinematic_deep` | −24 |
| 399.16 | Kirillov "**killed** by a bomb" | `boom_dark_cinematic_low_hit` | −21 |
| 435.77 | Sarvarov "a bomb **exploded**" | `boom_sub_bass_clean_01` | −25 |
| 496.96 | → "**On June 1st**, small Ukrainian drones" | `riser_reverse_cymbal_short` (ends on the word) | −27 |
| 705.99 | "…for Russian intelligence, **too?**" | `boom_cinematic_deep` | −27 |
| 767.38 | "**explosives** in his car" (music cut) | `boom_dark_cinematic_low_hit` | −21 |

An editor's `boom_low` / `riser` marker within ±0.6 s of a stinger is dropped automatically (no double hits); a realistic
`explosion_distant` there is kept (picture sound under the musical hit).

## 4. SFX vocabulary for the editors (`compositions/ivsNN.sfx.json`, master seconds)

Format as project/c2/SEGMENTS.md §3.4: `{"t": 399.16, "type": "boom_low", "scene": "ivs03-sc012", "level": "soft|normal", "dur": <loops>, "note": "…"}`.
All existing types still work (whoosh_soft/whoosh/whoosh_big/whip, paper_*, marker_*, highlighter_swipe, pin_pop, map_pin, stamp_thud,
shutter, typewriter, counter_ticks, radio_pulse, string_draw, scanner_sweep, focus_hunt, crt_*, projector_*, boom_low, riser, plane_pass…).
**New for Ivan** (Epidemic recordings, `tools/audio/place_sound.py`; common misspellings are aliased, e.g. `static`, `vibrate`, `ping`,
`drone`, `explosion`, `train`, `typing`, `siren`, `knock`, `fire`, `city`):

| type | sound | use on |
|---|---|---|
| `radio_static` (dur) | lost-signal static / glitchy AM tuning | intercepted messages, handler radio, "went silent" |
| `phone_vibrate` (dur > 1 s = call loop) | phone buzz in hand | messages arriving, "stopped answering" |
| `message_ping` | soft text-message tone | typeset message bubbles |
| `drone_buzz` (dur) | small-drone motor whir | FPV/drone graphics (not inside insert 3) |
| `explosion_distant` (low) | real distant explosion (always kept by the restraint pass) | bombers in flames, Yelabuga strike, the car bomb picture |
| `train_pass` (dur; peak mid-move) | electric locomotive pass-by | railway / locomotive scenes |
| `car_engine` (dur), `car_door` ("trunk/inspect" → boot lid) | car start + idle / door or boot close | the checkpoint & car inspection, Sarvarov's car |
| `keyboard` (dur) | typing | case files typed, satellite analysis UI |
| `heartbeat` (dur, low) | cinematic 54 bpm heartbeat | fear moments (the music already has one under "explosives") |
| `glitch` | digital data glitch | CCTV/redaction/digital wipes |
| `fire_crackle` (dur) | real fire crackle | burning aircraft stills |
| `siren_distant` (dur) | distant police siren | arrests / Moscow police |
| `door_knock` | apartment door knock | "arrests", "if he got caught" |
| `city_night` (ambience, dur) | distant night-city traffic tone | Moscow at night, apartment block |
| `wind` + note "winter/snow/moscow/cold" | designed winter wind | snowy Moscow footage |
| `shutter` + note "film/soviet/surveil/spy/cctv" | KMZ Zenit / Canon shutters | surveillance stills, Ivan filming facilities |
| `stamp_thud` + note "passport/visa/document" | real rubber stamp | passport stamps (Kazakhstan, Warsaw) |
Insert scenes get no SFX (any marker inside an insert window is dropped and reported).

## 5. Levels (measured on the music-only test build, 2026-11-01, `tools/audio/act_levels.py`; full mix: §7)

| act | music re VO while he speaks |
|---|---|
| M1 cold open | −16.0 LU |
| M2 protests/arrests (incl. insert 1) | −12.5 |
| M3 investigation | −15.6 |
| M4 assignment → Foma → Kirillov | −14.1 |
| M5 Sarvarov | −14.4 |
| M6 Spiderweb | −13.5 |
| M7 Ivan's mystery | −15.1 |
| M8 suspense | −15.9 |
| M9 trains | −15.8 |
| M10 ending | −14.4 |
| whole | −14.9 (bed −50.7 LUFS, peak −30.9 dBFS) |

## 6. Build / rebuild (one command; ~2–3 min; run heavy audio jobs one at a time)

```bash
cd /home/user/vox-edit-kit
python3 project/ivan/gen/make_cuesheet.py            # only if the cue tables changed
nice .venv/bin/python tools/audio/place_sound.py --vo vo_iv.mp3 --transcript transcript_iv.json --len 949.0 \
  --markers 'compositions/ivs0*.sfx.json' --cues project/ivan/music_cuesheet.json --out assets/audio/ivan
nice .venv/bin/python tools/audio/act_levels.py --vo vo_iv.mp3 --beds assets/audio/ivan --cues project/ivan/music_cuesheet.json --len 949.0
nice .venv/bin/python tools/audio/measure_mix.py --vo vo_iv.mp3 --beds assets/audio/ivan --len 949.0 --out renders/testmix_ivan.wav \
  && rm -f renders/testmix_ivan.wav
```
→ `assets/audio/ivan/{music_bed.wav, sfx.wav, ambience.wav, timeline.json}` (+ music_report.json, sfx_placements.json, sfx_hierarchy.json).
The Epidemic WAVs are gitignored: on a fresh machine re-download them first (commands + ids in `assets/audio/epidemic/LOG.md`, "Ivan").
A segment re-run = edit its `compositions/ivsNN.sfx.json`, run the place_sound line again (it always rebuilds all three beds).

### place_sound.py / epidemic_bed.py changes made for Ivan
- VO gate relative to the measured VO (`min(−45, VO_LUFS − 13.5)`); VO decoded once.
- Cue sheet `ducks` (insert windows): music −16 dB with ramps, no pause lifts within 0.5 s, SFX + ambience muted, markers inside dropped.
- Ambience/room-tone library loops scaled by `db(min(0, VO_LUFS + 25))`.
- New types + aliases (§4); `explosion_distant` / `heartbeat` are sub-heavy (LOWTYPES caps); hierarchy ranks for them.
- Cue-sheet layers may name a `"file"` (e.g. `sfx/heartbeat_cinematic_54bpm.wav`) instead of track/stem.

## 7. Phase 2 (full mix with the editors' markers)
**Final build 2026-11-01** (all seven `compositions/ivs0*.sfx.json`: 355 markers; 2 editor booms duplicating stingers dropped
(399.66, 767.4); restraint pass kept 265, dropped 90 — see `assets/audio/ivan/sfx_hierarchy.json`). `measure_mix.py`: mix −36.8 LUFS-I =
VO alone −36.8 (**Δ 0.0 LU** ✓), true peak −12.1 dBTP; music bed −50.7 LUFS (**−14.9 LU** re the VO while he speaks; per act −12.5…−16.0,
table §5 unchanged); SFX median −20.8 dB re the local VO peak (max −33.4 dBFS); ambience −68.0 LUFS (≈ 32 LU under).
If a segment's timing changes: edit its sfx.json and re-run the §6 commands (≈ 3 min).
