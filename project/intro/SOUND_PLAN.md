# Intro sound plan — "Taiwan: the chip rivalry", INTRO 0.00–275.06 s (VO seconds)

Sound designer, phase 1 (library + cue sheet). Sources: MANUAL §7, §7.1, §10.3; BEATS.md §6 (acts); Krish's rules (BRIEF.md
rule 8). Tracks, ids, stems and why: `assets/audio/epidemic/LOG.md`. Measured stems/sections/keys:
`assets/audio/epidemic/ANALYSIS.md` (+ `.json`). All music = Epidemic Sound (Krish's subscription), all in one key family
(**D minor / F major**, with G minor for the host joke). Anchor/vibe: *Melting Glass* (Eden Avery).

## 0. Measured facts

| | value |
|---|---|
| `vo_intro.mp3` | **−24.1 LUFS-I**, true peak −2.5 dBTP, LRA 4.4 LU (ffmpeg ebur128). Louder than the old `vo10.mp3` (−27.2), so the old −41 LUFS bed target is too low here. |
| Bed target under speech | **VO −14 LU ≈ −38 LUFS** (sum of all music layers) |
| Under dense/important lines (numbers, names, the joke) | VO −16 LU ≈ −40 LUFS, or thin layers (preferred) |
| Lifts | +2…3 dB only where the VO breathes. This VO barely pauses (longest internal gap 0.72 s at 193.57–194.29), so the lifts are on **beats** (swells on words) not on gaps. Music-only: none inside the intro (after 275.06 → chunk 1). |
| SFX | peaks ≥ 12 dB under the VO's peaks; "soft" ≈ −18 dB re VO, "normal" ≈ −12 dB. Ambiences (room/factory/restaurant) ≈ −50 LUFS — felt, not heard. |
| VO | never processed. All ducking/carving happens on the bed (place_sound reads the VO level only). |

Layer gains below are `gain_dB = layer_target_LUFS − stem_LUFS-I` (stem loudness from ANALYSIS.json); after summing,
normalise each act window to the bed target above (stems differ ±3 LU between sections, see each track's profile).

## 1. The layers (vocabulary)

| layer | source (stem) | stem LUFS-I | target alone | gain dB |
|---|---|---|---|---|
| **DRONE** | `woodwind_reviere_bass` (D-minor dark floor, tempo-free) | −14.4 | −44 | −29.6 |
| DRONE-air | `woodwind_reviere_instruments` (airy upper drone) | −23.3 | −45 | −21.7 |
| **PAD** | `interstice_of_sound_instruments` (F maj / D min, floating) | −21.1 | −43 | −21.9 |
| **COLD-OPEN** | `melting_glass_instruments` | −13.5 | −41 | −27.5 |
| **PULSE** (boom) | `lightbulb_moment_instruments` + `_drums` (−45) + `_bass` (−44) | −10.5 / −15.7 / −18.5 | −41 | −30.5 / −29.3 / −25.5 |
| **MYSTERY / TENSION** | `estimations_instruments` + `_bass` (+ `_drums` in the reveal) | −19.1 / −18.0 / −34.7 | −42 / −43 / −46 | −22.9 / −25.0 / −11.3 |
| **TRAVEL** | `anytime_soon_instruments` + `_drums` + `_bass` | −14.1 / −14.8 / −16.1 | −41 / −45 / −44 | −26.9 / −30.2 / −27.9 |
| **MELODY** (sentimental) | `melting_glass_melody_derived` (+ `_bass`) | −16.6 / −19.0 | −42 / −44 | −25.4 / −25.0 |
| **LIGHT** (host joke) | `pardon_my_french_instruments` + `_bass` (+ `_melody_derived` in gaps) | −21.4 / −20.0 / −15.8 | −43 / −45 / −45 | −21.6 / −25.0 / −29.2 |
| spare | `misguided_path_*` (A minor dark build) | | | |

Bar lengths (for bar-aligned entries/exits): Melting Glass 1.791 s (134 bpm), Lightbulb Moment 1.333 s (180), Anytime Soon
1.412 s (170), Estimations 2.051 s (117), Pardon My French 2.069 s (116). Drone/pad are free-time (enter anywhere).
`offset` = where to read inside the file at the segment's start (`media_start`), chosen so the track's own builds/peaks
(ANALYSIS.md sections) land on the story beats.

## 2. Cue sheet (VO seconds)

| # | act / beat | in → out | layers (file offset at "in") | moves on words |
|---|---|---|---|---|
| M1 | 0 Cold open — 1983 factory floor, insight | 0.00 → 16.5 | COLD-OPEN `melting_glass_instruments` @0.0 (its quiet intro) fade-in 1.5 s; DRONE @20.0 fade-in 3 s | +2.5 dB swell 13.8→14.8 into "the world" (14.80); crossfade to M2 15.0→16.5 |
| M2 | I The boom — exports 4M→24M, 6×, record profits | 15.52 → 37.44 | PULSE `lightbulb_moment` instruments @75.0 (offset = VO+59.5), drums enter 20.9 ("4" 20.96), bass enters 23.1 ("24" 23.12); DRONE continues −3 dB | the track's own build 83–90 → peak 90 lands on 23.5–30.5 = the numbers + "6×" (25.52); peak through "record" (32.64) |
| — | II The bust — "the phone boom died" | 37.44 | PULSE all stems out with a 0.25 s fade starting 37.40 (rhythm pulled on "died") | `boom_sub_bass_clean_01` at 37.44, very low (−22 dB re VO); 37.44–40.4 DRONE alone, +2 dB (the empty beat) |
| M3 | III The idea: a foundry | 40.40 → 69.09 | PAD `interstice_of_sound_instruments` @20.0 fade-in 2 s; MELODY `melting_glass_melody_derived` + COLD-OPEN instruments @35.0 enter on "profitable" 48.96 (offset = VO−13.96, bar-aligned) | +2 dB lift 61.0→61.6 on "foundry"; `melting_glass_bass` enters on "idea." 68.45 (confident) |
| M4 | IV Board, young company, uphill, excited | 69.09 → 93.97 | Melting Glass continues (same offset): instruments + bass; MELODY **out** 69.09–85.09 (dense board lines), back on "Luckily" 85.09; PAD −3 dB | the track's own peak (file 102 s) arrives at VO 88 = "almost told him yes"; **stop**: all Melting Glass out in 0.15 s at 93.90 → "one condition." 93.97 + `boom_cinematic_deep` (soft) at 93.97 |
| M5 | IV The mystery executive → go get his approval | 94.61 → 120.26 | MYSTERY `estimations` instruments + bass @7.0 (offset = VO−87.61; its quiet intro 7–27 → steady from VO 114.6); DRONE + DRONE-air | darker texture under the executive description (94.61–110.45); tension rises as he's sent to share the plan (110–120) |
| M6 | V New York — flight, meeting, dinner, top of the world | 120.26 → 135.54 | TRAVEL `anytime_soon` instruments+bass @116.8 (offset = VO−3.46), drums enter 125.3 ("The meeting goes really well"); DRONE **out** 118.5–120.3 (bright, F major) | the track's build 121–128 → peak 128 lands on 124.5–131.5; brightest on "top of the world" 134.18; **cut everything** 135.50 (0.08 s) on "shock" 135.54 |
| M7 | VI The cold shoulder — stonewalled, drop it | 135.54 → 157.22 | 135.54–136.5 near-silence (room tone only); DRONE + DRONE-air back 136.3 (fade 1.5 s), uneasy; PAD enters 149.38 ("In Taiwan, especially 1984") fade 2 s | sad resolve on "dropping" 156.02: PAD +2 dB, DRONE fades out 155.5–157.2 |
| M8 | VII The betrayal reveal — across the street, bar for bar | 157.22 → 170.98 | TENSION `estimations` instruments+bass @109.0 (offset = VO−48.22), drums enter 160.3 ("ground"); DRONE −2 dB | the track's peak (file 120 s) lands exactly on "bar for bar" 168.18; **out** in 0.2 s at 170.90 |
| M9 | VII "Guess who…" → Morris Chang → TSMC | 170.98 → 185.01 | near-silence: DRONE alone at −46 (face cam, direct address); `riser_reverse_cymbal_short` ends at 180.69; TENSION `estimations` bass+instruments @143.0 (peak section) re-enter at 180.69 | **hit** `boom_dark_cinematic_low_hit` on "Morris" 180.69; second, softer hit `boom_cinematic_deep` on "TSMC." 183.89 |
| M10 | VIII Rivalry → superpower → greatest business story → Hsinchu → Silicon Valley | 185.01 → 246.18 | MELODY act: `melting_glass` instruments + bass @92.7 (offset = VO−92.29), MELODY `_melody_derived` enters 194.29; PAD under at −46 for glue; DRONE out 185–187 | big lift on "superpower" 194.29 (the track's own 102–140 s peak starts here); thin under the personal lines 196.61–214.37 (melody out, bass −3 dB); rebuild: bass back 214.37, melody back on "Shin Shu Park" 227.09; land on "big reasons" 244.26; fade out 245.5–247.5 |
| M11 | IX Host intro + "face built for radio" joke | 246.18 → 270.02 | LIGHT `pardon_my_french` instruments + bass @19.3 (offset = VO−226.86) fade-in 1.5 s; its melody_derived only in the short breaths (≥ 0.4 s) at −45 | title sting on "Searching Lessons" 250.74: `chime_soft` (library) soft, or a 1-bar MELODY lift; **no hits on the punchlines** (254.74 "radio", 260.5/266.74 "sweat"); fade out 269.3–270.4 |
| M12 | X "Enjoy the historic images… here's the story" | 270.02 → 275.06 (→ chunk 1) | PULSE `lightbulb_moment` instruments + drums @86.24 (offset = VO−183.78), fade-in 1 s; `swell_reverse_timpani_cymbal` peak on "here's" ≈ 273.78 | the track's build 83–90 → peak 90 lands on 273.78; continues into chunk 1 (hand the offset to the chunk-1 plan) |

Rules applied: never more than one *rhythmic* track at a time (the tempi differ); tracks change only at act boundaries,
with the tempo-free DRONE/PAD bridging the joins; stems of one track are kept sample-aligned (same offset) when they
enter/leave; exits on beats are quick (0.08–0.25 s), entries slow (1–3 s); one track used for more than one act only
where the story rhymes (Melting Glass = insight → legacy; Lightbulb Moment = boom → launch; Estimations = mystery → reveal).

## 3. Stingers / hits

| VO s | word | sound | level |
|---|---|---|---|
| 14.80 | "the world." | music swell only (+2.5 dB) | — |
| 37.44 | "died," | `epidemic/sfx/boom_sub_bass_clean_01.wav` | very soft (sub only) |
| 93.97 | "condition." | `epidemic/sfx/boom_cinematic_deep.wav` + music stop | soft |
| 135.54 | "shock," | music cut (no sound) | — |
| 179.1→180.69 | → "Morris" | `epidemic/sfx/riser_reverse_cymbal_short.wav` (ends on the hit) | soft |
| 180.69 | "Morris" | `epidemic/sfx/boom_dark_cinematic_low_hit.wav` | normal (the biggest hit of the intro) |
| 183.89 | "TSMC." | `epidemic/sfx/boom_cinematic_deep.wav` | soft |
| 250.74 | "Lessons." | `sfx/chime_soft.wav` (library) | soft |
| 273.78 | "here's the story" | `epidemic/sfx/swell_reverse_timpani_cymbal.wav` (peak on the word) | normal |

## 4. SFX vocabulary for the editors (`compositions/introNN.sfx.json`)

Marker format = example-docs/SEGMENTS.md §3.4: `{"t": <VO s of the object event>, "type": "...", "scene": "...",
"level": "soft|normal", "dur": <loops only>, "note": "..."}`, sorted by `t`, absolute VO seconds. Editors add **no music**.
Existing types keep their library mapping (LIBRARY.md); new and re-mapped types for this intro:

| type | files (takes rotate; `epidemic/sfx/` = Epidemic, `sfx/` = free library) | use on |
|---|---|---|
| `whip` (new) | `epidemic/sfx/whoosh_swoosh_light.wav`, `whoosh_swoosh_wide.wav`, `whoosh_soft.wav`; free: `sfx/whoosh_short_0p4s*.wav` | every `FX.whip` transition (t = the whip's middle frame) |
| `whoosh_soft`, `whoosh`, `whoosh_big` | `epidemic/sfx/whoosh_soft.wav` / free `sfx/whoosh_*` | moves, zooms |
| `paper_slide` | `epidemic/sfx/paper_slide_wood_table.wav`, `_04.wav`; free `sfx/paper_slide_0*.wav` | cards, photos, documents sliding in |
| `marker_scratch`, `marker_long` | `epidemic/sfx/marker_drag.wav`, `marker_circle.wav`; free `sfx/marker_*.wav` | underline/arrow/circle draws |
| `highlighter_swipe` | single strokes cut from `epidemic/sfx/highlighter_drag_text.wav`; free `sfx/highlighter_swipe*.wav` | `.hl` swipes |
| `pin_pop`, `map_pin`, `pop_soft` | free `sfx/map_pin_*`, `kenney_ui_drop_pop_*` | pins on maps, isotype dots |
| `stamp_thud` | `epidemic/sfx/rubber_stamp_document_01.wav`; free `sfx/stamp_thud_0*.wav` | D07 collage stamps, the hovering "YES" (91 s) |
| `boom_low` | see §3 (only the listed beats) | reveals |
| `riser` (new) | `epidemic/sfx/riser_reverse_cymbal_short.wav` (t = END of the riser) | before a reveal |
| `phone_ring` (new) | `epidemic/sfx/phone_ring_04.wav` (80s electronic), `phone_bell_ring_old_01.wav` | telephone exports beat (15.5–28 s), one ring max |
| `phone_dial` (new) | key presses cut from `epidemic/sfx/phone_pushbutton_dial_pickup.wav`, `phone_handset_grab_buttons.wav` | 1980s push-button phone close-ups |
| `plane_pass` (new, needs `dur`) | `epidemic/sfx/jet_pass_overhead_01.wav`, `jet_pass_long_distant.wav` | "very next flight to New York" 122.82, "flies back home" ≈131.7 (route lines on maps) |
| `crowd_room` (new, loop, `dur`) | `epidemic/sfx/restaurant_crowded_distant_01.wav` (dinner), `office_aircon_people_quiet.wav` (board/office) | dinner 126.98–131.70; boardroom scenes |
| `factory_hum` (new, loop, `dur`) | `epidemic/sfx/factory_hum_light_activity_01.wav`, `factory_machine_room_electronics_hum.wav`, `roomtone_aircon_unit_a.wav` (cleanroom) | 1983 factory floor 0–10 s; fab/cleanroom B-roll; "across the street" fab 157–162 |
| `teletype` (new) | `epidemic/sfx/telegraph_antique.wav`; free `sfx/typewriter_*` | D08 telegram layouts, typed captions |
| `focus_hunt` (new) | `epidemic/sfx/camera_focus_nikon_d3100.wav`, `lens_autofocus_f4_01.wav`, `lens_autofocus_f4_03.wav` | DSLR focus hunt after fast zooms (MANUAL §10) |
| `projector_loop`, `crt_click`, `crt_hum`, `shutter`, `tick_soft`, `counter_ticks` … | free library (unchanged) | as before |

Draft markers the plan already implies (editors confirm/shift to their frames):
```json
[
  {"t": 0.00,   "type": "factory_hum", "scene": "I001", "dur": 10.2, "level": "soft", "note": "1983 factory floor bed, fade out under the insight"},
  {"t": 20.96,  "type": "phone_ring",  "scene": "I004", "level": "soft", "note": "one 80s ring under the 4M → 24M exports (optional)"},
  {"t": 37.44,  "type": "boom_low",    "scene": "I009", "level": "soft", "note": "the phone boom died (sub only)"},
  {"t": 93.97,  "type": "boom_low",    "scene": "I020", "level": "soft", "note": "one condition"},
  {"t": 122.82, "type": "plane_pass",  "scene": "I026", "dur": 6.0, "level": "soft", "note": "very next flight to New York"},
  {"t": 126.98, "type": "crowd_room",  "scene": "I027", "dur": 4.7, "level": "soft", "note": "dinner together"},
  {"t": 180.69, "type": "boom_low",    "scene": "I039", "level": "normal", "note": "Morris Chang reveal (riser ends here)"},
  {"t": 183.89, "type": "boom_low",    "scene": "I039", "level": "soft", "note": "TSMC"}
]
```

## 5. `tools/audio/place_sound.py` changes (DONE 2026-10-31 — cue sheet = `project/intro/music_cuesheet.json`)

1. **Parameterise the project**: `--vo vo_intro.mp3 --words transcript_intro.json --len 275.06 --markers 'compositions/intro*.sfx.json'
   --out assets/audio/bed/intro/` instead of the hard-coded `vo10.mp3`, `transcript.json`, `LEN = 600`, `seg0*`. Also: its
   `FFMPEG = ~/.local/bin/ffmpeg` doesn't exist on this machine — fall back to `shutil.which("ffmpeg")`.
2. **Targets from measurement**: read `VO_LUFS` from the VO (ebur128) instead of the constant −27.2; `MUSIC_TARGET = VO − 14`.
3. **Epidemic cue sheet instead of `music_cuesheet()`**: load `project/intro/music_cuesheet.json` (the §2 table as data, one
   entry per *layer*: `{"track": "melting_glass", "stem": "instruments", "start": 48.96, "end": 93.90, "offset": 35.0,
   "gain_db": -27.5, "fade_in": 1.5, "fade_out": 0.15, "auto": [[61.0, 0], [61.6, 2], ...]}`). Every layer is an *overlay*
   (summed), not a crossfaded segment as in the old `build_bed.py`.
4. **`build_bed.py` loader**: resolve `assets/audio/epidemic/<track>/<track>_<stem>.wav`; read only the needed window with
   `soundfile.read(start=, stop=)` (Interstice of Sound is 11 min — loading whole files as float64 would blow memory);
   default `gain_db` from `ANALYSIS.json` (`target − stem LUFS-I`).
5. **Keep** what already works: thinning under dense speech (now: drop the MELODY/drums layers instead of "pizz"),
   dynamic carve (−3 dB @ 2.5 kHz, −2 dB @ 1 kHz while the voice speaks), per-act normalisation to the bed target,
   −1 dBTP ceiling, varied SFX takes per marker, the three pre-mixed beds + `timeline.json`.
6. **SFX map**: add the new types of §4 to the type→file table; Epidemic files are long recordings → cut by onset
   (`onset()`/`trimfit()` already exist) and pick a random region per take for the long ones (highlighter, phone dial).
7. **Stingers** (§3) as their own list in the cue sheet (`overlay` one-shots placed so the file's loudest point = the word).

## 6. Notes / open points
- `melting_glass` has **no drums stem** on Epidemic (DRUMS → NOT_FOUND). `anytime_soon` stems don't sum to its master
  (melody can't be derived) — use its stems as delivered.
- Derived melody stems (`*_melody_derived.wav`) are numerically clean where noted, but listen before relying on them.
- If a layer feels too busy under a dense line, drop it rather than lowering the whole bed (Krish: music always far under).
- Reference playlist tracks not used here (Formations, Chrysotile, Imber, Ostinato, City Phases…) are in the wrong key for this
  set or too busy; Ostinato / City Phases (A minor) are good for chunk 1.
