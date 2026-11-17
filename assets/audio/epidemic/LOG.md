# Epidemic Sound downloads — log (MANUAL §10.3)

Licensed to Krish's Epidemic Sound subscription. **Gitignored** (`assets/audio/epidemic/`): re-download any time with the
commands below. Never use the public low-quality preview MP3s in an edit. Measured loudness / sections / keys:
`ANALYSIS.md` (+ `ANALYSIS.json`), produced by `.venv/bin/python tools/audio/epidemic_analyze.py`.

- Music: `python3 tools/epidemic_fetch.py <kosmosId> <name> FULL BASS DRUMS INSTRUMENTS` (resumable, checks WAV size).
- SFX: `python3 tools/epidemic_sfx_fetch.py <id> <name> [...]` → `sfx/<name>.wav`.
- `<name>_melody_derived.wav` = full − (bass + drums + instruments) (`tools/audio/epidemic_melody.py`; the API has no
  MELODY download). Check by ear before using it as a layer.
- Key = estimated from the audio (Krumhansl chroma on the full mix); Epidemic's API exposes no key. bpm = Epidemic metadata.

## Music (intro set, 2026-10-31) — key family D minor / F major (+ G minor, A minor neighbours)

| folder | title — artist | kosmosId | public URL | stems downloaded | bpm | key (est.) | role in the intro / why |
|---|---|---|---|---|---|---|---|
| `melting_glass/` | Melting Glass — Eden Avery | 332b6167-8f9c-4cf4-a6d9-38dee1eccc82 | https://www.epidemicsound.com/track/2fqOXWpHab/ | full, bass, instruments, melody_derived (no DRUMS stem exists) | 134 | D minor | Krish's anchor. Cold-open texture + the sentimental/"greatest story" layer of act VIII (its 102–140 s peak = "superpower") |
| `woodwind_reviere/` | Woodwind Reviere — Daniella Ljungsberg (ambient, dark drone, floating) | 6882422a-a047-4e82-9c00-4e84b5a5538e | — | full, bass, drums, instruments | — (drone) | D minor | the DRONE layer: tempo-free D-minor floor under acts 0–VII, so any track can enter/leave over it |
| `interstice_of_sound/` | Interstice of Sound — DEX 1200 (ambient drone, floating, peaceful) | ffb8a5b6-bc76-497e-8306-07e2239e6e7a | — | full, bass, instruments | 39 (free) | F major / D minor | PAD layer for hope/discovery (the foundry idea), "sad resolve" after he drops it; 11 min long, lots of steady material |
| `lightbulb_moment/` | Lightbulb Moment — Eden Avery | 7aaacf11-31e8-4493-ad4d-b42ba5a5d977 | — | full, bass, drums, instruments, melody_derived | 180 | D minor | PULSE layer: the phone boom (its 83–90 build + 90–110 peak land on the numbers / "record profits") and the final "here's the story" launch. Same composer as the anchor |
| `anytime_soon/` | Anytime Soon — Hampus Naeselius | b0a48cac-8e6b-41a2-8ed1-d21650e84050 | — | full, bass, drums, instruments (melody can't be derived: stems don't sum to the master) | 170 | F major | travelling OSTINATO for New York → "on top of the world" (its 121–128 build → 128 s peak); hopeful/restless, contemporary-classical/orchestral hybrid |
| `estimations/` | Estimations — Christoffer Moe Ditlevsen | a720e76d-783d-4d9d-a858-b9ed527d3ad3 | — | full, bass, drums, instruments, melody_derived | 117 | D minor | TENSION layer: the mysterious executive (quiet 7–27 s intro), and the rising ostinato of the betrayal reveal (pulses/suspense) |
| `pardon_my_french/` | Pardon My French — Eva Hummingbird | 4d2fcafe-48e2-49e6-9562-a21b735b3fcc | https://www.epidemicsound.com/track/u065zBNJSt/ | full, bass, instruments, melody_derived | 116 | G minor | LIGHT texture for the host intro + "face built for radio" joke (eccentric/elegant contemporary classical, from Krish's playlist) |
| `misguided_path/` | Misguided Path — Bonnie Grace | 5c3964a0-0ec3-312a-9446-48ac7b7505e8 | https://www.epidemicsound.com/track/yIboE3Njz0/ | full, bass, drums, instruments | 92 | A minor | ALTERNATE dark build (from Krish's playlist) — spare for the stonewall/reveal if Estimations feels too busy; also good for chunk 1 |

### Added for chunk c4 (2026-10-31) — cue sheet `project/c4/music_cuesheet.json`

| folder | title — artist | kosmosId | public URL | stems downloaded | bpm | key (est.) | role / why |
|---|---|---|---|---|---|---|---|
| `silent_sun/` | Silent Sun — Anna Landström | 6e8a6f3f-0ea6-400a-bf1e-59a016166c09 | — | full, bass, instruments (melody can't be derived: stems don't sum to the master) | 116 | F major | warm/hopeful melodic layer: Japanese-rule "positives", relief on "luckily", land reform |
| `ostinato/` | Ostinato — Vieveri (Krish's playlist) | e4a14fb1-33bf-3246-9e09-f7d9384f74dd | https://www.epidemicsound.com/track/ClT3alC0ax/ | full, instruments, melody_derived (no bass/drums stems exist) | 180 | A minor | the building ostinato of the UN vote war and the export-zone groove |
| `still_in_blues/` | Still in Blues — (Epidemic, dark drone/suspense) | 5217f8cb-0660-4a3d-867c-bfa3f3d57ce6 | — | full, bass, drums, instruments (stems are far quieter than the full mix — use `full` as the layer) | – (drone) | G minor | cold drone for war damage and the White Terror |

### Added for chunk c2 (2026-10-31) — cue sheet `project/c2/music_cuesheet.json`

| folder | title — artist | kosmosId | public URL | stems downloaded | bpm | key (est.) | role / why |
|---|---|---|---|---|---|---|---|
| `a_pinpoint_of_light/` | A Pinpoint of Light — (Epidemic) | 7be83545-80e3-3b2a-a478-842cdf857781 | — | full, bass, drums, instruments, melody_derived | 105 | D minor | steady pulse of Act I (steeples) and the Silicon Valley lift that ends c2 (bookends) |
| `april/` | April — Jakob Ahlbom | fa190df2-467b-4180-bfea-ecc28647704d | — | full, bass, instruments, melody_derived | 128 | G major | light, hopeful texture under the transistor explanation; Nobel lift; shimmer under the IC "print" idea |
| `city_phases/` | City Phases — John Abbot (Krish's playlist) | a5194258-5cee-4686-b89a-dfa7c323a12a | https://www.epidemicsound.com/track/530JEZzEY7/ | full, bass, instruments, melody_derived (melody is most of the track) | 150 | A minor | "transistor everywhere" build → radios → world |

### Added for chunk c1 (2026-10-31) — cue sheet `project/c1/music_cuesheet.json`

| folder | title — artist | kosmosId | public URL | stems downloaded | bpm | key (est.) | role / why |
|---|---|---|---|---|---|---|---|
| `journeyman_road/` | Journeyman Road — Farrell Wooten (Krish's playlist; acoustic, happy/hopeful) | 6f157326-4849-3772-b7ee-3d96ffac101e | https://www.epidemicsound.com/track/xMW4hwbFgy/ | full, bass, drums, instruments (use `full`: its melody isn't a separate stem) | 108 | B major (est.; light acoustic, sits fine as a short stand-alone act) | playful/delightful layer of Act VII: Disney, the coin flip, the HP garage |
| `formations/` | Formations — Van Sandano (Krish's playlist; contemporary classical, dark pulses) | 62bcc9c2-0834-3299-a065-d3a584cf0067 | https://www.epidemicsound.com/track/WVNmADGk4F/ | full, bass, drums, instruments | 100 | Ab minor (outside the family: used alone, entered on a cut 'the war' and left on a cut 'Dean') | WWII secret radar lab (Act VIII) |

### Added for chunk c3 (2026-10-31) — cue sheet `project/c3/music_cuesheet.json` (political / Cold-War colour)

| folder | title — artist | kosmosId | public URL | stems downloaded | bpm | key (est.) | role / why |
|---|---|---|---|---|---|---|---|
| `thoughts_revoked/` | Thoughts Revoked — Kikoru (drama, pulses, restless; similar to Melting Glass) | 227e6423-291b-3dd6-977a-1c6d78d3b1c3 | — | full, bass, drums, instruments (derived melody ≈ the whole full mix → deleted; use instruments/full) | 122 | D minor | investigative pulse of the California-law act, the steady 'recognition' act and the decolonization/UN act that carries into c4 |
| `shadowfall/` | Shadowfall — Henry Miles (cinematic, dark, epic, orchestral hybrid) | 20dff97e-cb47-48ce-97da-4b82af835462 | — | full, bass, drums, instruments, melody_derived | 83 | A minor | archival grandeur for WWII → Security Council (its 126–135 build lands on the word) and the ominous 'hidden fragility' (its drums enter as a clock-like pulse) |
| `to_whom_it_may_concern/` | To Whom It May Concern — Jon Björk (dark, sad, tragedy) | d87c821d-00ba-3650-8ff8-e37892a2892b | — | full, bass, instruments (stems don't sum to the master: no melody) | 90 | D minor | the existential crisis (UN kicks out the ROC), the wistful flight to Taiwan |

### Added for chunk c5 (2026-10-31) — cue sheet `project/c5/music_cuesheet.json`

| folder | title — artist | kosmosId | public URL | stems downloaded | bpm | key (est.) | role / why |
|---|---|---|---|---|---|---|---|
| `finding_life_again/` | Finding Life Again — Kikoru (contemporary classical, hopeful, restless; similar to Melting Glass) | 76336c03-b048-394c-9f4f-5f80bf7be2b7 | — | full, bass, drums, instruments (stems don't sum to the master: no melody) | 147 | C major (relative of the A-minor set) | Taiwan's rise: export economy, the conference, swell on 'Fred Terman', the brave carrier swell |
| `the_unveiling/` | The Unveiling — Christoffer Moe Ditlevsen (mysterious, sneaking; same composer as Estimations) | 605b5158-5031-3a52-b442-98d766ae92fc | — | full, bass, drums, instruments (no melody: stems don't sum) | 100 | A minor | Kissinger's secret trip (quiet stalk → peak on the announcement), the Cold-War-triangle pulse, the UN-vote build into c6 |
| `prison_cell/` | Prison Cell — Jon Björk (ambient, dark drone, sad) | 4ea71784-9324-3347-9d44-f58f89e4b187 | — | full, bass, instruments (stems louder than the master; no melody) | 92 | A minor | Cultural Revolution drone, the low pulse under Nixon/Kissinger, the 'shock', 'worst dreams', the unresolved ending |

### Added for chunk c6 (2026-10-31) — cue sheet `project/c6/music_cuesheet.json` (political / turning-point colour)

| folder | title — artist | kosmosId | public URL | stems downloaded | bpm | key (est.) | role / why |
|---|---|---|---|---|---|---|---|
| `captivating/` | Captivating — Joseph Alesci (drama, elegant, main title, peaceful) | f0983d53-2b0c-3eb3-bd2b-e54166733057 | — | full, bass, drums, instruments (derived melody −1.9 dB re full: unreliable, deleted) | 91 | A minor | the turning point ('statement' → 'Keep on fighting'), the engineers' cabinet, the breakfast build into c7 |
| `reflection_of_the_sun/` | Reflection of the Sun — Anna Landström (contemporary classical, dreamy) | 91275fd8-6226-4873-a678-2b1686def992 | — | full, bass, instruments, melody_derived (no DRUMS stem exists) | 88 | F major | airy wonder from 'technological breakthrough'; its 93–118 s peak = the swell on 'moon' |

### "Ivan" (Searching Lessons, 2026-11-01) — cue sheet `project/ivan/music_cuesheet.json`, plan `project/ivan/SOUND_PLAN.md`
Key family **D minor / D (modal) / F major**. Geopolitical espionage: dark pulses, drones, contemporary-classical tension, one
reflective ending. Re-downloaded `woodwind_reviere` and `estimations` (IDs above). Stems don't sum to the full mix for Code of Violence,
Close Call, Letters Never Sent (derived melody ≈ 0 dB or above re full → deleted): their delivered stems are used as layers. Tracker and
Make Way for Hearses: stems are 10–20 LU quieter than the full mix (the melody isn't a stem) → the `full` file is the layer.
Fulls of code_of_violence / estimations / close_call / letters_never_sent / woodwind_reviere and tracker_instruments deleted after analysis (disk).

| folder | title — artist | kosmosId | stems downloaded | bpm | key (est.) | role in Ivan / why |
|---|---|---|---|---|---|---|
| `code_of_violence/` | Code of Violence — Dian Shuai (dark, dark ambient, mysterious) | 8b36c332-a349-4289-b02f-b96a294c4b6b | full, bass, drums, instruments | 102 | D major (alt D minor; dark modal) | M1 cold open → invasion (its 100–118 peak on "full-scale invasion…February 2022"); M7 Ivan's own mystery (Spiderweb foreknowledge, Yelabuga) |
| `tracker/` | Tracker — Christoffer Moe Ditlevsen (electronic, sneaking, suspense) | 3d59ec8e-9ad0-3446-87b4-b2f57773c457 | full, bass, drums (instruments −32 LUFS, deleted) | 90 | D minor | M3 the investigation (Ivan decides → Mamoń → videos → verification → Kazakhstan/Tatarstan); M9 railway saboteurs |
| `estimations/` | Estimations — Christoffer Moe Ditlevsen | a720e76d-783d-4d9d-a858-b9ed527d3ad3 | bass, drums, instruments | 117 | D minor | M4/M5 the five-hour assignment → Foma's network → Kirillov (its 143 s peak on "killed by a bomb") → Sarvarov |
| `close_call/` | Close Call — Helmut Schenker (epic, orchestral, restless) | 4669ca1d-a25d-4489-bdea-e572e99220e0 | full, bass, drums, instruments | 84 | D minor | M6 Operation Spiderweb (41–65 peak on "June 1st…drones", quiet under the trucks + insert 3, 104–134 peak on the losses) |
| `make_way_for_hearses/` | Make Way for Hearses — Christian Andersen (dark, suspense) | 883bf493-6079-3e38-a6ee-a027e39b493e | full, bass, drums, instruments | 90 | D major (alt D minor) | M8 "how was he never caught?" → double agent → months of silence → the car inspection; cut dead on "explosives" |
| `letters_never_sent/` | Letters Never Sent — Anna Dager, Anna Landström, Hanna Ekström (contemporary classical, dark, sad) | 39323798-4969-4700-b943-457da8d5619d | full, bass, instruments | 80 | F major (alt D minor) | M10 reflective ending (peak on "Russians themselves", dip under "Putin won't live forever", swell on the last line) |
| `woodwind_reviere/` | Woodwind Reviere — Daniella Ljungsberg (dark drone) | 6882422a-a047-4e82-9c00-4e84b5a5538e | full, bass, instruments | – | D minor | DRONE glue under every join, the floor under the three inserts, the months of silence |

Auditioned for Ivan (previews; key measured): The Connection (Lennon Hutton, D, dark suspense — spare), Out There (Out To The World, D minor,
sub-heavy drone pulse — spare), Returning Home (D minor), Quotidian (Arr. Gabel) (CMD, D minor, sad — spare ending), Disturbing Evidence
(A/D minor), We Are on Our Own (F, drone/sneaking); off-key or too trailer-like: Ignition Protocol, Launch Sequence, Epic Triumph,
Rattlesnake Canyon Chase, Pulse Runner, Formula, The Mole, Covert Affairs, Ghosting, Collusion, Escalation.

### Candidates auditioned (by metadata + measured key from previews; not downloaded)
Formations (Van Sandano, 100, Ab minor — wrong key for the set), Chrysotile (Farrell Wooten drone, C# minor — clashes with D),
Imber (140, F# minor), Ostinato (Vieveri, 180, A minor — strong alternative for a build), City Phases (John Abbot, 150, A minor —
alt for the boom), Terms of Gravity (Eb major), Building Something Together (Eden Avery, B major), Methodus (C# minor),
Deception Uncovered (C major/minor dark drone), Behind the Curtain (E), The Last Horizon (A major), Silent Sun (Anna Landström,
116, F major — hopeful, alt for act VIII), April (G major), Reclaim (C minor), A Pinpoint of Light (105, D minor — alt pulse),
Still in Blues (G minor drone), Air (A minor drone), Lotus River (D major). Similar-search seeds: Melting Glass, Formations, Chrysotile.
c3/c5 audition (similar to Melting Glass / Estimations / Formations; key from previews): Covert Affairs (E minor), The Mole (F# minor),
Methodus, Fake Photisms / Paradigm Shift / Neon Noir (E minor), Rise of the Velcro (B minor), Sense of Betrayal / Rushes To (C minor),
Allegro Sotto Le Stelle (Ab major) — off-key; c6 audition: Longing (B minor), Shadow Play / Kingdom / Nimb / Cry for Help (C minor), Solution in Sight (A major), Kyoto Waltz (E major) — off-key; No One in Sight, Mindscape (A minor) — spares.

## SFX (Epidemic Sound) — `sfx/`

| file | Epidemic id | Epidemic title | len | use |
|---|---|---|---|---|
| phone_pushbutton_dial_pickup.wav | 1b607180-b7fe-4c15-9008-be7c688b9030 | Communications, Telephone, Telephone Button Dial, Pick Up | 55.7 s | 1980s push-button phone (cut single key presses / pick-up) |
| phone_handset_grab_buttons.wav | 1232ab55-9b1d-4743-847e-247fb0390bb1 | Communications, Telephone, Device, Grab, Handle, Press, Butt… | 18.5 s | handset grab + button presses |
| phone_ring_04.wav | d95e0410-d87f-45a4-9721-8aa547f23369 | Communications, Telephone, Telephone Ringing 04 | 11.3 s | electronic ring (80s office phone) |
| phone_bell_ring_old_01.wav | d105ea78-ea46-456c-9d80-45d55aa48eed | Communications, Telephone, Old, Bell Ring 01 | 17.9 s | bell ring (older desk phone) |
| jet_pass_overhead_01.wav | 61f179de-16fb-48bc-99ce-0786879be795 | Aircraft, Jet, Plane, Pass Overhead 01 | 32.3 s | flight to New York / flight home |
| jet_pass_long_distant.wav | 43b5611b-602a-4b4c-8182-27689a1b50ff | Aircraft, Jet, Airplane, Pass, Long, Distant | 66.6 s | softer, distant airplane under map routes |
| restaurant_crowded_distant_01.wav | 45f16e05-3ef8-4808-b9b3-a42edcb3201c | Ambience, Restaurant & Bar, Restaurant, Crowded, Distant 01 | 180 s | the New York dinner (room tone) |
| office_aircon_people_quiet.wav | 14fc1646-3b68-4eb0-b7f8-a0170efd57a9 | Ambience, Office, Office, Air Conditioning, People Talking Q… | 160 s | boardroom / office room tone |
| factory_hum_light_activity_01.wav | c4958898-3ae4-494c-bd79-52dc999cc0e0 | Ambience, Industrial, Factory Hum, Light Activity 01 | 120 s | 1983 factory floor |
| factory_machine_room_electronics_hum.wav | 656520ef-f29a-4b19-8635-4f508f559038 | Ambience, Industrial, Factory, Machine Room, Electronics, Hu… | 95.7 s | cleanroom / fab hum |
| roomtone_aircon_unit_a.wav | 4d6a61fc-2f7b-4c87-8151-5e269703c5de | Ambience, Room Tone, Interior, Air Condition, Unit A | 121 s | neutral room tone (cleanroom air handling) |
| telegraph_antique.wav | e5979560-d9d5-4c38-b625-d7270706dc20 | Communications, Telemetry, Antique Telegraph | 26.5 s | telegram / teletype layouts (D08) |
| camera_focus_nikon_d3100.wav | 10d3e849-2d88-4ca2-8589-9087259a99ad | Communications, Camera, Digital Camera, Nikon D3100, Focus | 1.3 s | DSLR focus hunt |
| lens_autofocus_f4_01.wav / _03.wav | 0a960941-eb3d-42b6-95c1-4c21a1fd1db1 / ab83f8a5-02b6-4a57-824a-a69ce1190585 | Communications, Camera, Lens, Auto Focus, Nikon F4 01 / 03 | 0.5 / 0.8 s | short focus chirps (alternate takes) |
| boom_dark_cinematic_low_hit.wav | d106e784-e06e-4673-ae48-a36e145a715d | Designed, Boom, Impact, Dark, Cinematic, Low HIt | 4.3 s | reveal hit ("Morris Chang") |
| boom_cinematic_deep.wav | 2f0a40ab-f23a-4927-a911-1d70459d52e7 | Designed, Boom, Cinematic, Deep, Boom, Impact | 2.8 s | second hit ("TSMC"), "one condition" |
| boom_sub_bass_clean_01.wav | 95c4ca16-841c-4030-ac26-5893e8a5ba76 | Designed, Boom, Cinematic Booms, Clean Impact, Sub Bass 01 | 11.2 s | sub drop for "the phone boom died" (very low level) |
| whoosh_soft.wav | f040a2a4-0570-4a43-bcdb-d0afee3ccdc5 | Swooshes, Whoosh, Softs | 2.5 s | whip transitions (soft) |
| whoosh_swoosh_light.wav | c52cf22f-9ad0-4e26-b841-f5951a4f7526 | Swooshes, Whoosh, Designed, Swoosh, Light | 1.5 s | whip transitions |
| whoosh_swoosh_wide.wav | 72d49db7-34bc-4f3c-b73d-00db66e7ce08 | Swooshes, Whoosh, Designed, Swoosh, Wide | 1.2 s | bigger whip / act changes |
| paper_slide_wood_table.wav / _04.wav | 6a2298cb-c05a-44c7-9bc2-8759eba61d89 / 4b1eeb52-0176-4c79-b2e3-4d78d8127903 | Paper, Friction, Sheet, Laminated, Slide On Wooden Table (04) | 0.8 / 1.4 s | card / photo slides |
| marker_circle.wav | a836c16e-6b5d-4d44-8eda-12f135d8dfe8 | Objects, Writing, Marker Writing, Circle | 2.5 s | marker circle on a board/map |
| marker_drag.wav | ed2c29c8-3e6c-471f-b7f6-d8c3db16f743 | Objects, Writing, Marker Writing Sound, Drag | 1.1 s | marker underline / arrow |
| highlighter_drag_text.wav | f26907ce-119c-4de5-b8c1-4c8171f800e2 | Objects, Writing, Text, Highlight Drag, Marker Highlighter | 26.5 s | many highlighter swipes (cut single strokes) |
| riser_reverse_cymbal_short.wav | 566b642a-4341-4ad7-961a-d25000cf8341 | Designed, Riser, Cymbal, Reverse, Crescendo, Suspense, Clima… | 1.6 s | lead-in to the reveal hit |
| swell_reverse_timpani_cymbal.wav | 04845f9f-e404-4209-b190-54d21070eec5 | Musical, Stinger, Trailer Swell, Reverse, Timpani and Cymbal | 8.3 s | "here's the story" launch swell |
| rubber_stamp_document_01.wav | d530c5b9-3047-42fe-a06a-7c479d637b60 | Office Supplies, Rubber Stamp, Document 01 | 0.2 s | stamps (D07 collage, "YES" hovering) |
- 2026-10-31 — Disk: stems (bass/drums/instruments/melody WAVs) deleted locally after all c1–c6 beds were built; re-fetch with tools/epidemic_fetch.py (IDs above) to rebuild a bed.

### SFX added for "Ivan" (2026-11-01) — `sfx/` (the intro set above was re-downloaded too: whooshes, booms, riser, swell, paper slides,
focus, jets, telegraph, phone ring/dial, office/factory ambiences, rubber stamp)

| file | Epidemic id | Epidemic title | use (place_sound type) |
|---|---|---|---|
| radio_static_lost_signal_01.wav | 357c719f-fbeb-42b4-80d5-356a35d82aec | Communications, Static, Radio, Lost Signal 01 | `radio_static` |
| radio_am_tuning_glitchy_01.wav | 3c3a05b7-bbc9-46f2-9d87-7aa0b1ec32f0 | Communications, Radio, Am Tuning, Long, Noise, Glitchy 01 | `radio_static` (alt take) |
| phone_vibrate_hand_01/_02.wav | 29ee2675-96c4-4139-a679-f11fb9a3a9d0 / 797ad432-ff97-473c-be53-8313acb8379c | Cellphone, Vibrate, Held In Hand 01/02 | `phone_vibrate` |
| phone_vibrate_call_loop.wav | aa31ac72-0232-44ee-963b-7673b387daaa | Cellphone, Call, Vibrate, Loopable | `phone_vibrate` with dur > 1 s |
| message_text_ping_01/_02.wav | a6dae59d-6111-42cb-887d-9bad152480e1 / 96e6bbfb-71dc-42ff-b506-1ff2ab96da2d | UI, Alert, Notification, Message, Text (02) | `message_ping` |
| drone_rc_motor_medium.wav / drone_rc_fly_around.wav | 3c23824f-ee7c-4583-92e1-e12e10cbd9d1 / abb25339-aaa4-47fb-af4a-5417be3f62ea | RC drone motor whir (medium / fly around) | `drone_buzz` (dur) |
| explosion_distant_01/_03.wav, boom_distant_explosion_03.wav | 36a2288d-4f49-49f4-aa10-7d26a1222104 / 5ff5dfec-b285-4126-96d3-fcf2be4926fe / 4e3da17e-0ca6-471f-a05f-a0fcef395e66 | Explosions, Real, Distant | `explosion_distant` |
| train_locomotive_pass_night/_dawn.wav | 4e703ce2-121f-4ae7-875b-f8af6e32ed40 / 01d1cb24-2fe1-463e-a2ee-6cf97813616c | Trains, Electric, Locomotive, Pass By | `train_pass` (dur) |
| car_start_idle_rover.wav / car_w108_start_idle_stop.wav | 734791ef-ef29-44e7-9e8a-c8f08366754f / c922c4dd-bd24-4623-bfa5-b8003e32f277 | Car start + idle | `car_engine` (dur) |
| car_door_close_hard.wav / car_trunk_close.wav | 05b1bd38-299d-451d-a394-909e672cf764 / b9d78f6f-a41e-4db1-962f-9839002b08f8 | Car door close / boot close | `car_door` ("trunk/inspect" → boot) |
| keyboard_typing_apple.wav / keyboard_typing_17s.wav | c7ac1cb5-8e80-4fdc-bcab-23626f61340a / 5dd650b3-0f30-4872-9b85-ca51efc7bd4d | Keyboard typing | `keyboard` (dur) |
| heartbeat_cinematic_54bpm.wav / heartbeat_evil_fat_bass.wav | c805d6d8-b28b-4982-b407-c6233190e4de / 44f4869f-f2d2-4666-b2f5-4c639c60ae91 | Human, Heartbeat, Cinematic 54 BPM / Evil Heartbeat Fat Bass | `heartbeat` (dur); cue-sheet layer under "explosives in his car" |
| shutter_zenit_01/_02.wav, shutter_canon_5d.wav | 075b129e-49ec-4155-b840-1f167fefa6c8 / 723aa2bf-f067-4951-b62b-a95200b2d666 / cad01d18-bc44-4deb-b361-689f382d2e6c | KMZ Zenit 12XP shutter / Canon 5D shutter | `shutter` with note "film/soviet/surveil/spy/cctv" |
| city_night_distant_traffic_01.wav | 40d588ac-a758-4626-896a-5fefcabd8ed5 | Ambience, City, Distant Traffic Tone, Night 01 | `city_night` (ambience, dur) |
| wind_winter_08.wav | 5d44ec97-d14d-4e70-9579-86d9ce47ad5d | Wind, Designed, Storm, Winter 08 | `wind` with note "winter/snow/moscow/cold" |
| glitch_data_06/_12.wav | ce8c2f91-5e6c-483e-a5de-58b3d3ae18b3 / 5424863f-2378-4f80-8344-52566f83b335 | UI, Glitch, Data Processing | `glitch` |
| fire_burning_crackles.wav | 7c4ae63a-5be3-4b2b-b2fc-08bfd5e3da98 | Fire, Burning, Crackles | `fire_crackle`, `burn_crackle` ≥ 2 s |
| police_siren_distant.wav | 3ee522b6-0203-4fcb-9596-72f34b22b21a | Vehicles, Siren, Police Siren, Distant | `siren_distant` (dur) |
| door_knock_apartment.wav | 3b5d39a2-3bc2-4076-b78b-a9cb10aa46bf | Doors, Knock, Apartment Door | `door_knock` |

### "Paraguay" (Searching Lessons, 2026-11-08) — cue sheet `project/paraguay/music_cuesheet.json`, plan `project/paraguay/SOUND_PLAN.md`
Key family **E minor / G major** (new: Ivan was D minor, the Taiwan chunks D/F/G/A minor). Urgent investigative financial-crisis tone with
a wry narrator; Latin-American colour from acoustic/nylon guitars and plucked strings (no tasteful Paraguayan-harp track exists in the
catalogue: "harp"/"paraguayan harp"/"harp south america" searches return children's/celtic/cumbia material). Found with SearchRecordings +
SearchSimilarToRecording (seeds: Melting Glass, Neon Noir, Fake Photisms, Desert Whispers, Crossing the Border, Andean Valley, And Then,
In Disguise, Starfall, Formations); key measured from the LQ previews, confirmed on the WAVs (`ANALYSIS.md`).
**New (tested 2026-11-08): `DownloadRecording` now delivers a real `MELODY` stem** (`python3 tools/epidemic_fetch.py <id> <name> FULL MELODY
BASS DRUMS INSTRUMENTS`) — no need to derive it. Tracks without a DRUMS/MELODY stem answer NOT_FOUND (DOX, Fake Photisms).
Stems-sum check (full − Σ stems over 60 s): clean for We Picked Irises (−23 dB), I Can See the World (−23), Desert Whispers (−11); NOT
summing (−3…+6 dB: stems mastered separately) for And Then, Starfall, In Disguise, Neon Noir, Where It All Happened, Crossing the Border,
Buried in the Dirt (stems used as layers anyway, like Ivan); Fake Photisms and DOX: stems far under the full mix → `full` is the layer.
Pulse strength (onset autocorrelation, 1 = none): And Then bass 1.1 / instruments 1.6 → tempo-free glue (its drums stem 5.7 is not used).

| folder | title — artist | kosmosId | stems downloaded | bpm | key (meas.) | role in Paraguay / why |
|---|---|---|---|---|---|---|
| `and_then/` | And Then — DEX 1200 (ambient, dark drone, suspense) | 56e2fef0-f63b-45e7-97c4-db880304c35a | full, melody, bass, drums, instruments | 73 (free) | E minor | DRONE glue under every join (bass + instruments only) |
| `starfall/` | Starfall — Roots and Recognition (cinematic, dark, main title, sad) | 5879ab51-10c8-4345-bb75-352bc2d6c380 | full, melody, bass, drums, instruments | 82 | E minor | weight: cold open (X clip → "it all started with one bank") and its return for the board vote → "the bank is done" (84 s peak, cut) |
| `dox/` | DOX — Lennon Hutton (ambient, dark, pulses, restless) | 07e2e4ec-0727-4b5a-a76a-c360d6afb20e | full, bass, instruments (no drums/melody exist) | 74 | E minor | the money pulse: 60 % / Chase / market share / FDIC in the cold open; returns for the merry-go-round scheme (its 139 s drop on "Merry go around") |
| `in_disguise/` | In Disguise — The Fly Guy Five (quirky, sneaky, eccentric) | 20470259-69bc-444e-bc8e-01066aed76ca | full, melody, bass, drums, instruments | 84 | E minor | the wry colour: World Cup + the tweet; returns (instruments + bass only) for "Luckily for Ueno…that law gets changed" |
| `andean_valley/` | Andean Valley — Madison York (acoustic, eccentric, South America) | da44a4a7-0a79-3df4-a8dc-d988b886e7a8 | full, melody, bass, drums, instruments | 95 | E minor | Latin colour for "a success story, a boring one…especially in South America" → investment grade → Wall Street bonds |
| `we_picked_irises/` | We Picked Irises — Jay Taylor (contemporary classical, hopeful, adventure) | eb6d9817-79bf-4a3d-bbda-502ca4450ec5 | full, melody, bass, drums, instruments | 125 | G major (relative) | background: the 1950 joke, the money-lending company, the 2015 heir building a conglomerate (drums on "2015") |
| `i_can_see_the_world/` | I Can See The World From Here — Mythical Score Society (acoustic, restless; found by "charango") | fb49f858-5443-388a-b468-6743a598604e | full, melody, bass, drums, instruments | 142 | E minor (alt G) | the Ueno fintech boom: merger → app → 50 % promos → first bank accounts; ends on "four times bigger" |
| `neon_noir/` | Neon Noir — Lennon Hutton (cinematic, pulses, restless, suspense) | c4470b69-5cac-4373-ad4f-5704a41bd1ff | full, melody, bass, drums, instruments | 85 | E minor | investigative pulse: political capital — finance minister → president, CEO → central bank "the next day" |
| `desert_whispers/` | Desert Whispers — Tellsonic (acoustic, cinematic, dark, mysterious) | 6905cdbd-6f5e-4b54-840a-225684dbad18 | full, melody, bass, drums, instruments | 110 | E minor | dark nylon-guitar tension: hindsight → conflict of interest → 12 % / 15 % / 0.58 % → cut dead on "It was." |
| `fake_photisms/` | Fake Photisms — Martin Klem (ambient, mysterious, suspense) | dd42a193-a22a-344b-8525-7510bfd9a262 | full, melody, bass, instruments (no drums) | 111 | E minor | self-dealing → "owe a billion" → shell companies "created today" (full mix) |
| `where_it_all_happened/` | Where It All Happened — Dian Shuai (cinematic, crime scene, dark) | cb482655-8724-41cf-b82c-32188f35bcb8 | full, melody, bass, drums, instruments | 118 | E minor | the IMF act: full band back on "whatever IMF says is very important", peak through the Senate pressure → "criminally liable…blows apart" |
| `crossing_the_border/` | Crossing the Border — Hampus Naeselius (ambient, dark, suspense) | b8cee8b1-ca97-4507-97c3-a8b3be5ede97 | full, melody, bass, drums, instruments | 80 | E minor | the slow dark build from "the central bank did catch on" → buyer → $79/$80 M → report buried → ABC Color → "last week" |
| `buried_in_the_dirt/` | Buried in the Dirt — Christoffer Moe Ditlevsen (drama, orchestral, sentimental) | 0909f59e-2fa3-4979-b867-d707677d3e75 | full, melody, bass, drums, instruments | 90 | E minor (r = 0.96) | the people + the ending: apps dead → protests → impeachment → arrests → the daughter coda (its 110 s drop on the bleep) |

Auditioned for Paraguay (previews, key measured): Lighthouse Drawings (Broad Sky, E minor drone — spare glue), Loose Sails (Pulsed, E minor),
Fractured Paintings (Trevor Kowalski, E minor, busy orchestral build — too trailer-like), Paradigm Shift (E minor, vocal presence), The Frozen
Tears (E minor, 60 bpm sentimental — spare ending), The Detective (CMD, E minor, 50 bpm crime scene — spare), Tension 2 (E minor orchestral
pulses — spare), Behind the Curtain (E major/minor drone pulses), It May Be June / At the Ballet (G major comedy — too cartoonish), Tea with
Turtles (E minor harp, children's — too cute), Mystery Unfold (E major), My Brother (Yi Nantiro, South America, C minor — off key).
Fulls kept (needed for Fake Photisms / DOX layers and for re-analysis); all WAVs gitignored — re-download with the ids above.

### SFX added for "Paraguay" (2026-11-08) — `sfx/` (the whole intro + Ivan SFX set above was re-downloaded too; ids in the tables above)
Many Epidemic SFX arrive as 96 kHz / 24-bit WAV (ambiences 50–130 MB each); `epidemic_bed.read_window` resamples to 48 kHz on read.

| file | Epidemic id | Epidemic title | use (place_sound type) |
|---|---|---|---|
| protest_distant_chanting_walla.wav | 273dd863-cc20-4411-8f93-554d548b54d5 | Ambience, Protest, Environmental Protest, Walla, Distant Chanting | `crowd_chant` (default); cold-open cue-sheet layer |
| protest_chanting_02.wav | ebc072c0-77ab-475d-9b6a-2148430740eb | Ambience, Protest, Environmental Protest, Chanting 02 | `crowd_chant` + note "close/near/loud" |
| protest_distant_drums_chants.wav | e0f65fdc-3d49-4b2c-9474-f3c80cac5501 | Ambience, Protest, Peaceful, Distant, Scattered Voices, Shouts, Drums, Chants, Traffic | `crowd_chant` + note "drum/street/march"; P13 cue-sheet layer |
| censor_tone_various.wav | 5a4c848a-a7e6-4a73-ba47-e6976cb998e0 | Beeps, General, Censor Tone, Plop, Various Lengths | spare (the bleeps are generated at the exact word length) |
| notification_tone_02.wav / notification_app_general_01.wav | b671d57a-4e9e-4b0b-bef3-b8753b5b4f2b / 71e405a7-fc54-41a6-8080-02a6a1196ae5 | UI, Alert, Mobile Phone, Notification Tone 02 / Notification, Mobile, App, General 01 | `app_notify` |
| app_error_04.wav / app_error_01.wav | 10cc1fb8-b9e7-4dd9-8646-6c91ebf5683b / 0592f7ba-df26-4876-8f18-d0b2940c1cf2 | UI, Alert, Mobile, App, Error 04 / 01 | `app_error` (the app that won't load) |
| cash_register_kaching.wav | 6caad476-d3e4-44ad-afa1-1e9187c46bd0 | Cash Register, Kaching, Money | `cash_register` (bell on t) |
| coins_drop_01.wav / coins_handful_drop_wood.wav | 8e7e3f28-f5cc-4f6c-9342-7e762b5b98a6 / 528e259c-0839-4835-8fc8-f829cbbe1c0b | Objects, Coin, Money, Coins, Drop 01 / Handful, Drop Onto Wood | `coins` (note "handful/pile/many/pour" → handful) |
| card_swipe_03.wav / card_swipe_04.wav | 7866c8b9-51ae-4f70-8944-a1e514802576 / eadeffe2-a88f-4c80-805c-b95a09b97258 | Credit Card, Swipe In Machine 03 / 04 | `card_swipe` |
| atm_cash_buttons_beep.wav | 0849ca76-ec23-48bb-bd12-da7b68f25490 | Machines, Appliance, ATM, Money, Cash, Press, Button, … Beep, Open, Close | `atm` (dur; random excerpt) |
| stamp_hand_press_short.wav | edfbe8a5-c4b4-4af0-879f-cddd7bea480c | Objects, Office, Stamp Hand, Press, Mark, Short | `rubber_stamp` (alternates with rubber_stamp_document_01) |
| music_box_wind_up.wav / music_box_antique_melody.wav | a7eba5d8-f447-471f-9c23-3a31b91593fc / c06a90e2-dfc0-4f26-acb5-48b7b71ab1bb | Toys, Mechanical, Wind Up Music Box / Clocks, Chime, Antique Music Box, Melody | `music_box` (dur > 4.5 s → melody); merry-go-round cue-sheet layer |
| gavel_single_01.wav / gavel_x2.wav | 58112fd3-2705-43ec-8938-721abd7023ae / 115c882d-964a-427f-8475-c07cfb4f8464 | Wood, Impact, Gavel Hit, Courtroom, Single 01 / x2 | `gavel` (note "twice/x2/double" → x2) |
| press_paparazzi_flashes_medium.wav / camera_flash_modern_01.wav | f69fe12e-73a4-4df3-98f6-f6f38cfc2639 / b1cd56e3-e25e-4318-98d4-45d50e05750f | Press Conference, Paparazzi, Only Cameras, Medium Busy / Camera, Flash, Modern, Design 01 | `camera_flash` (dur > 1 s → burst) |
| crowd_walla_indoor_large_02.wav | 5da8d8bf-618c-4b2b-80ab-61bcd8627ab1 | Indoor, Large Crowds, Walla 02 | `crowd_murmur` (ambience: Senate, press room) |
| city_night_rooftop_insects.wav | e5bb207a-3a01-43cb-b4dd-213da670f9f2 | Ambience, Urban, City, Rooftop Terrace, Night, Traffic, Insects Chirp In Distance | `city_night` + note "asuncion/paraguay/tropic/insect" |
| office_small_group_keyboard.wav | 4a021a7c-c853-4b78-a560-ae148371ef21 | Ambience, Office, Small Group, Walla, Keyboard Typing 02 | `newsroom` (ambience: ABC Color newsroom, central-bank office) |
| typewriter_hermes_03.wav / typewriter_hermes_01.wav | 0a427b93-1857-4cef-a41f-b4e91a255c2e / 696833a1-6679-4c18-9c6c-96429c06fbf4 | Communications, Typewriter, Old, Hermes, Typing 03 / 01 | `typewriter` (Epidemic mode: real Hermes excerpt of dur) |
| handcuffs_click_slow.wav | b672bfea-dfea-44e1-bf94-04eb0e6252c1 | Equipment, Tactical, Handcuffs, Slow Adjustment, Click, Police Officer | `handcuffs` |
| stadium_cheer_goal_01.wav | c76a6846-f54f-4229-bde1-85a1bd55d2f4 | Crowds, Sport, Stadium, Cheering, Whistles, Clapping, Excited, Reaction, Goal 01 | `stadium_crowd` (World Cup; swells on t) |
| ice_crack_medium_long_01.wav / ice_crack_medium.wav | c9092b1a-10a5-43af-9de9-a3f5fe9de4c5 / f222b3dc-7399-4322-8e49-98cd59570350 | Ice, Break, Ice Crack Medium Long 01 / Ice Crack Medium | `crack` (level normal → the long one) — phase 2 |
| gavel_single_02.wav | 59936633-8ea8-47dd-926b-d782a026fdf7 | Wood, Impact, Gavel Hit, Courtroom, Single 02 | `gavel` (single takes alternate in order of use) — phase 2 |

### "Podcast" — TSMC vs UMC (Searching Lessons, 2026-11-13) — cue sheets `project/podcast/cues/islNN.json` (generator `project/podcast/gen/make_cuesheet.py`), plan `project/podcast/SOUND_PLAN.md`
Key family **A minor / C major** (new: Taiwan chunks + Ivan were D minor / F, Paraguay E minor / G). Curious, intelligent tech/business
history: contemporary-classical pulses + light electronics, warm for the Stanford/HP origin stories, dark pulses for geopolitics.
Found with SearchRecordings (11 terms) + SearchSimilarToRecording (seeds: Melting Glass, Observatory, Mindscape, Sliding Doors, Until Now,
Stay This Way, One Step Away, Pretend to Wake Up): 328 candidates, key measured from the LQ previews (43 in A minor / C major), then
confirmed on the WAVs (`ANALYSIS.md`: all ten measure A minor, r = 0.74–0.91). Music lives only in "islands" (the intro + each edited
section), bed at VO − 22 LU under the binding limits of MANUAL §10.8.
Fetch: `python3 tools/epidemic_fetch.py <id> <name> FULL MELODY BASS DRUMS INSTRUMENTS` (tracks without DRUMS answer NOT_FOUND).
**The WAVs were converted to 16-bit after analysis** (disk: 1.7 GB for the set; a re-download is 24-bit — levels are identical).
Stems-sum check (full − Σ stems over 60 s; ≤ −10 dB = clean): How Did We Get Here −12.2, A Trace of Light −14.7, Stay This Way −7.2,
Seekers and Finders −4.3, Sliding Doors −2.4, Mindscape −1.1, Observatory +0.5, One Step Away +0.6, Until Now +2.1, Melted Mind +2.6
(stems mastered separately — used as layers anyway, as in Ivan/Paraguay; the bed is normalised after summing).

| folder | title — artist | kosmosId | stems downloaded | bpm | key (meas.) | role in the podcast / why |
|---|---|---|---|---|---|---|
| `how_did_we_get_here/` | How Did We Get Here — Hanna Lindgren (ambient, drone, floating, peaceful) | f2a59c58-76bb-4cf4-82a2-1d0dfbcac42a | full, melody, bass, instruments (no drums exist) | 0 (free) | A minor (0.91) | the tempo-free DRONE floor of every island (melody stem; 346 s long) |
| `observatory/` | Observatory — Out To The World (electronic, pulses, dreamy, hopeful) | 0c47304b-4e50-43b2-8230-2397e7991316 | full, melody, bass, drums, instruments | 128 | A minor (0.86) | the IDEA theme: intro opening → "an unique insight" → 4 M → 24 M; returns as colour ENG (engineering explainers: oscillator, transistor, wiring problem, the integrated circuit, Moore's Law) |
| `melted_mind/` | Melted Mind — Max Anson (ambient, hopeful, pulses, suspense) | 6e4f8193-4f20-329f-9409-ca557df0e18f | full, melody, bass, drums, instruments | 134 | A minor (0.79) | intro: "In fact, a chip factory would be more successful if…" → the foundry idea → the board says yes |
| `mindscape/` | Mindscape — Lennon Hutton (dark, electronic, pulses, suspense) | 4cb08b97-fa28-4f38-9b9c-3e71a2d98b5f | full, melody, bass, instruments (no drums exist) | 108 | A minor (0.77) | intro: "one condition" → the unnamed executive; colour GEO (two Chinas, the UN chapter opener, recognition blocs, Deng, the "Taiwanese shield", the Traitorous Eight) |
| `until_now/` | Until Now — August Wilhelmsson (adventure, ambient, dreamy, pulses, smooth) | 4385955c-8325-3d69-872f-f38e3f8de5e5 | full, melody, bass, drums, instruments | 154 | A minor (0.74) | intro: the flight to New York → "on top of the world"; colour TW (Taiwan builds: Japanese rule, aid, export zones, the cabinet of engineers, Ten Major Projects, Pan Wen-yuan, the value chain) |
| `stay_this_way/` | Stay This Way — Hanna Lindgren (ambient, dark, floating) | 94afc29d-2a9e-4d0d-9820-cf1b06ad0048 | full, melody, bass, instruments (no drums exist) | 0 (free) | A minor (0.83) | intro: the phone bust, the aside's air, the cold shoulder / stonewalled; colour DARK (the ROC flees to Taiwan, Chiang's one-party state) |
| `one_step_away/` | One Step Away — Dian Shuai (build, dark, drama, orchestral hybrid, suspense) | 2dfb0d5d-7d3c-43cb-8216-e76cec2f9b6b | full, melody, bass, drums, instruments | 102 | A minor (0.88) | intro: two years later → "guess who" → its full band (file 100 s) on "Morris Chang" → "TSMC" → betrayal → rivalry; colour OSA (the UN walkout, pd33) |
| `sliding_doors/` | Sliding Doors — Helmut Schenker (contemporary classical, dreamy, hopeful) | 9d171c14-46c0-4b9c-ae82-d796af632443 | full, melody, bass, drums, instruments | 112 | A minor (0.79) | colour US (warm origin stories: Terman, the trillion-dollar map, Hoover, Bush/Raytheon, Hewlett & Packard, Shockley's move, the Stanford lease, Route 128) |
| `a_trace_of_light/` | A Trace of Light — Jakob Ahlbom (ambient, dreamy, neoclassical, peaceful) | 6f30a607-b32c-4302-a5cc-828f6bf623a7 | full, melody, bass, drums, instruments | 75 | A minor (0.90) | colour REF (theory / reflection: non-competes, the Field Code, Chiang Ching-kuo, the institute model, the Silicon copycats, Christensen) |
| `seekers_and_finders/` | Seekers and Finders — Experia (pulses, suspense) | cc31edf0-290e-3049-8a33-dfa501eb8007 | full, melody, bass, drums, instruments | 118 | A minor (0.81) | colour SPY (Kissinger's secret trip, Africa's new votes, July → October, the "important question") — its pulsing bass leads |

Auditioned, not downloaded (previews, key measured): Night Shuttle / Pretend to Wake Up / Waiting for the Call / Drowned Night (Max Anson,
A minor — spare pulses), Cryptic Secrecy + First on the Scene (Dream Cave, A minor crime-scene — spare tension), Victims & Crimes (Skrya),
Nemesis (Alec Slayne), Vital (Christoffer Moe Ditlevsen, A minor, 274 s epic build — too big), Impossible Theory (Rachel Sandy — trailer),
Big Announcement (Out To The World — epic), Water Circles (Luba Hilman, A minor 0.94 drone, 325 s — spare floor), Off-White (Farrell Wooten,
drone), Three Days in Venice / Boxes of Memories (Franz Gordon, strings — too sentimental), Bright White (Frank Jonsson, C major),
The Long Ride (Sam Will — too happy), Launch Sequence (Helmut Schenker — action). `silent_sun/` (full only) is the lead's limit-test file.

SFX for the podcast — `sfx/` re-downloaded 2026-11-13 (ids in the SFX table above): whoosh_soft, whoosh_swoosh_light, whoosh_swoosh_wide,
boom_dark_cinematic_low_hit, boom_cinematic_deep, boom_sub_bass_clean_01, riser_reverse_cymbal_short, swell_reverse_timpani_cymbal,
paper_slide_wood_table (+_04), marker_circle, marker_drag, highlighter_drag_text, rubber_stamp_document_01, stamp_hand_press_short.
Everything else is fetched only if an editor's marker needs it (`tools/audio/pd_islands.py --preflight` lists the missing files).
SFX re-downloaded for the podcast markers, phase 2 (ids in the tables above): coins_drop_01, jet_pass_long_distant, jet_pass_overhead_01,
phone_ring_04, typewriter_hermes_01, typewriter_hermes_03, factory_machine_room_electronics_hum, crowd_walla_indoor_large_02.

### "NVIDIA" (Is the chip ban actually working?, 2026-11-17) — cue sheet `project/nvidia/music_cuesheet.json`, plan `project/nvidia/SOUND_PLAN.md`
Key family **C minor / Eb major** (new: Ivan + the Taiwan chunks D minor / F, Paraguay E minor / G, the podcast A minor / C). Investigative-tech
documentary: cold, pulsing, textural (Melting Glass lineage) — electronic pulses for the server hall, contemporary-classical suspense for the
Washington paperwork, hopeful strings only for job two's ✓. Found with SearchRecordings ("pulsing synth documentary", "string ostinato suspense", "hacker", "processor", "investigation", …) +
SearchSimilarToRecording (seeds Melting Glass, Neon Noir, Mindscape, DOX, Observatory, then 77 Cycles, Unsolved Issues, …); key measured from the LQ previews (`work/nv-sound/keys*.log`), confirmed on the WAVs (`ANALYSIS.md`,
every track C minor, r 0.64–0.87). Fetched one at a time (`work/nv-sound/scripts/fetch_all.sh`: fetch → analyze → §10.8 checks → 48 kHz/16-bit).
§10.8 checks (60 s stems-sum residual, full − Σ stems; pulse = onset-autocorrelation peak/median, ≈ 1–2 tempo-free):
Flute −78 dB (clean; bass 1.1 / instruments 1.4 → the **tempo-free drone**); The Investigator −20.6 (clean); Hidden Room −6.9, Breath by
Breath −8.3, The Northern Cliff −5.2 (borderline); 77 Cycles +1.9, Unsolved Issues −2.9, Cinema Neon −0.0, Shifting Angles +1.5, Operation
−2.2, Gnomon +1.2, Subconscious +1.2, Pinnacle −3.1, Across −2.9 (stems mastered separately → used as layers, like Paraguay). Cinema Neon,
Subconscious, Pinnacle: stems 6–17 LU under the full → `full` is the layer. Across is nearly tempo-free (full 2.8, bass 1.2, melody 1.3).
Disk: stems the cue sheet doesn't use were deleted locally after the checks (cinema_neon bass/drums/instruments, subconscious bass/drums/
melody, gnomon/breath_by_breath/the_northern_cliff/across/seventy_seven_cycles drums) — re-fetch with the ids below. 14 tracks ≈ 1.86 GB.

| folder | title — artist | kosmosId | stems on disk | bpm | key (meas.) | role in NVIDIA |
|---|---|---|---|---|---|---|
| `flute/` | Flute — Daniella Ljungsberg (dark, drone, experimental) | a3494aff-6231-433d-82f9-2388a5b92f17 | full, bass, instruments (no melody/drums exist) | free | C minor (0.81) | DRONE glue under every join; alone for the verdicts / the iPhone memory |
| `seventy_seven_cycles/` | 77 Cycles — Lennon Hutton (cinematic, dark, electronic, pulses) | b303cb62-f4ad-4bd6-8f45-e63df25ae6bd | full, melody, bass, instruments | 170 | C minor (0.77) | the cold-open pulse (HK mall → Shenzhen → servers); returns for "the ban works" (60 % → 80 %, DeepSeek dark) |
| `unsolved_issues/` | Unsolved Issues — Magnus Ludvigsson (contemporary classical, dark, mystery) | d9e25a21-d72a-4fa7-9e40-7747fd064dbb | full, melody, bass, drums, instruments | 100 | C minor (0.83) | THE QUESTION theme: "Was the chip ban a mistake?" ↔ "So why do they still have this ban?" ↔ "I don't think it's working" |
| `cinema_neon/` | Cinema Neon — Trevor Kowalski (contemporary classical, dreamy, mysterious) | 6f1c8f8d-c476-3841-9526-f69510c86577 | full, melody | 97 | C minor (0.78) | Washington-paperwork / explainer colour: what the ban is; three ways to measure; volume → yield |
| `the_investigator/` | The Investigator — Dream Cave (classical crossover, mysterious, suspense) | 5fbbf6b4-3024-4495-9085-ce3a2a3d2275 | full, melody, bass, drums, instruments | 113 | C minor (0.80) | investigation colour: "is it fair?"; returns for the factors nobody says aloud → "Take a look at this chart" |
| `subconscious/` | Subconscious — Nihoni (dark, dreamy, mystery, strange) | a8ad74c7-9aa8-31b2-b330-4fa023fb049a | full, instruments | 100 | C minor (0.64) | dual-use weight: uranium → bomb → Taiwan; the US government's unseen test |
| `gnomon/` | Gnomon — Marten Moses (ambient, drone, mysterious, suspense) | fdb68343-e830-352c-a0df-5af07ad240f1 | full, melody, bass, instruments | 120 | C minor (0.86) | the "American law" pulse: scoreboard → design IP → "every chip on the planet"; returns for Huawei → Lutnick → the port |
| `shifting_angles/` | Shifting Angles — Experia (contemporary classical, dark, restless, suspense) | a26eba24-b2b8-4896-92e5-a4e8880d3da2 | full, bass, drums, instruments (no melody exists) | 84 | C minor (0.67) | cat and mouse: THE LINE (job one); returns for distillation's cat-and-mouse |
| `hidden_room/` | Hidden Room — Anthony Earls (ambient, electro, floating, mysterious) | 9e374078-6220-32f9-816a-ae29417eb720 | full, bass, drums, instruments (no melody exists) | 80 | C minor (0.79) | wry asides: PlayStation rule → Facebook Marketplace → $2,000; returns for iPhone 1 vs iPhone 18 |
| `operation/` | Operation — Wendel Scherer (adventure, dark, restless, suspense) | e96002a2-65ad-33ab-bff8-0854a9a9dbbc | full, melody, bass, drums, instruments | 110 | C minor (0.77) | the caper: the big fish — co-founder arrested, hair dryer, the warehouse camera |
| `pinnacle/` | Pinnacle — Marten Moses (ambient, drone, restless, sentimental) | 5653b460-0719-333f-bd2c-b8e9ed0f8b44 | full, melody, bass, drums, instruments | 110 | C minor (0.73) | the server hall: training → the rack → Memphis 800,000 homes → 7 % |
| `breath_by_breath/` | Breath by Breath — Helmut Schenker (contemporary classical, hopeful, build) | 56550990-4021-4a44-85db-227b4e5ed838 | full, melody, bass, instruments | 68 | C minor (0.87) | the turn: labs share attacks → gap widening → SCOREBOARD ✓ "one to one" (its 114 s peak) |
| `the_northern_cliff/` | The Northern Cliff — Erasmus Talbot (contemporary classical, hopeful, suspense) | 139b05c5-ecc1-4845-b93c-67b7b56c2221 | full, melody, bass, instruments | 120 | C minor (0.75) | job three: Jensen's argument → keyboard analogy → 95 % → 0 % → Huawei |
| `across/` | Across — Harbours & Oceans (ambient, floating, suspense) | 8b6e804b-73fa-47ff-ac50-565a5f2420d8 | full, melody, bass, instruments | free-ish | C minor (0.79) | level four: Malaysia → flying with the data → the debate → "?" → outro |

All WAVs gitignored — re-download with the ids above (`python3 tools/epidemic_fetch.py <id> <name> FULL MELODY BASS DRUMS INSTRUMENTS`).

### SFX added for "NVIDIA" (2026-11-17) — `sfx/` (24 new, 48 kHz/16-bit; also re-downloaded from the tables above: boom_dark_cinematic_low_hit,
boom_cinematic_deep, boom_sub_bass_clean_01, riser_reverse_cymbal_short, swell_reverse_timpani_cymbal — the cue-sheet stingers)

| file | Epidemic id | Epidemic title | len | use |
|---|---|---|---|---|
| server_room_medium_roomtone.wav | 367d1212-26f5-4072-b0ec-2f73f1453819 | Ambience, Room Tone, Medium Sized Server Room | 114 s | SERVER HALL ambience (racks, clusters, data centers) |
| data_server_room_hum_01.wav | a8dae759-70c5-4b72-9f43-3cb9e2b654cb | Ambience, Hitech, Data Server Room, Machine Hum 01 | 60.5 s | bigger hall: Memphis, Malaysia data centers |
| computer_fans_power_up_down.wav | 188078f6-9b33-4b57-9c4e-5fc7b34758eb | Computers, Hard Drive, Desktop, Fans, Power Up, Down, Run, Buttons | 65.3 s | the PC aside; a server powering on |
| electric_motor_shutdown_01.wav | 650a4b4e-0207-4b37-bda3-2f29f4a34d61 | Machines, Appliance, Electric Motor, Shut Down 01 | 3.9 s | "DeepSeek went dark", features switched off, "switch the data centers off" |
| electrical_hum_lights.wav | db72319a-e0ff-4582-a0fb-e4b6c5fc4cb5 | Electricity, Buzz & Hum, Lights, Electrical Hum | 31.9 s | electricity: 100 homes / 800,000 homes, "China has the electricity" |
| water_pipes_flowing_03.wav | 70ce9b3f-4363-4fc3-9ca4-8f44790266b1 | Water, Plumbing, Flowing Through Pipes Basement 03 | 77 s | liquid cooling / plumbing of the rack |
| data_processing_digital_buttons.wav | ad74696d-7c5c-467d-9b6a-d0517ecbcc06 | User Interface, Data, Processing, Digital Buttons | 27.2 s | data/UI texture (training, model tests, fake accounts) |
| data_processing_loading_21.wav | 5c039935-27cc-4376-acc4-998d79911ca4 | User Interface, Data, Computer, Futuristic, Data Processing, Loading 21 | 6.7 s | loading / distillation / "feed the internet to chips" |
| ui_beep_computer_short.wav | d7890ee7-5d23-4af6-9de5-3ff571f38536 | User Interface, Beep, Computer, Digital Beep, Short | 4.5 s | single UI beeps (test scores, login) |
| relay_flipdot_metal_01.wav / relay_flipdot_plastic_02.wav | 40aa9201-fa32-411e-85c1-9287705b739c / f3c2426d-3b02-4132-8d88-e43326f8fc64 | Mechanical, Relay, Metal / Plastic Clicking Mechanism, Flip Dot Display, Counting Board Flipping, Loop 01 / 02 | 6.6 / 6.7 s | THE SCOREBOARD rows flipping; counters |
| marker_on_paper_writing_01.wav / marker_on_paper_stroke.wav | 9b7efd76-5da5-4416-82e4-08ca70778e56 / 5ce91f47-7c92-4a35-b723-22212be8c934 | Objects, Writing, Marker On Paper, Writing 01 / Stroke | 6.8 / 33.7 s | THE LINE being drawn; scoreboard ✗ strokes |
| marker_notebook_tick.wav | 3bcd22f5-b580-4d38-a4bb-172ba7c66a7d | Objects, Writing, Marker On Notebook, Tick | 9.8 s | scoreboard ✓ (job two) |
| marker_scrub_out_01.wav | fb230349-8330-4507-bcb0-5761f2c0dfb8 | Objects, Writing, Marker Pen, Scribble Scrub Out On Cardboard Sheet 01 | 7.1 s | scoreboard "?" scribble; crossing a chip off the list |
| camera_lens_motor_zoom.wav | fbcf9bca-1219-4a94-8a2d-c8ad96cdbdc1 | Communications, Camera, Digital, Lens, Motor, Zoom In, Out | 7.8 s | the warehouse camera zooming in |
| servo_camera_turn_on_off.wav | 6f3e3eb9-c993-424d-9045-1a912476bbd1 | Motors, Servo, Turn, On, Off Digital Camera | 5.9 s | security camera turning (CCTV monitor) |
| barcode_checkout_scanner.wav | d0fe3002-b789-4122-a367-b3841ba88b76 | Beeps, General, Checkout Counter, Scanner, Scanning Labels | 5.0 s | swapped barcodes / auditors scanning servers |
| hair_dryer_running.wav | c9b0f44f-0bc0-4f48-ab3d-7d45695b68fd | Machines, Appliance, Hair Dryer, Running | 16.3 s | the hair-dryer trick (labels peeled) |
| harbor_container_terminal_01.wav | f074cd30-657c-4326-a6e9-4b28fb75d613 | Ambience, Urban, Harbor, Industrial Container Terminal 01 | 150 s | "600,000 chips are sitting on a port" |
| ship_horn_distant_big.wav | 463af07a-e0b5-41be-9019-008d70e379e2 | Boats, Horn, Distant, Big Transatlantic Ship | 34.7 s | the port (one blast, far away) |
| ferry_horn_medium.wav | 67be070b-563c-4380-95be-55a0302300c0 | Boats, Horn, Ship, Ferry, Medium Close | 13.4 s | "a short ferry ride…Shenzhen" |
| street_market_walla_01.wav | 314c15a9-cc17-4110-99ce-7dae248d62a7 | Ambience, Market, Crowd, Street Market, Walla 01 | 82.9 s | the HK mall / Huaqiangbei electronics market |
| airport_departure_lounge.wav | e6e78298-d6e0-4450-8865-c0f5fba59e5c | Ambience, Transportation, Airport, Gatwick, Departure Lounge | 22.9 s | individuals carrying chips; employees flying to Malaysia |

SFX re-downloaded for the NVIDIA phase-2 build (2026-11-17; ids in the tables above — place_sound's Epidemic mode needs them for the
editors' existing marker types): paper_slide_wood_table (+_04), coins_drop_01, rubber_stamp_document_01, stamp_hand_press_short,
card_swipe_04, whoosh_soft, whoosh_swoosh_light, whoosh_swoosh_wide, glitch_data_06/_12, message_text_ping_01/_02,
ice_crack_medium_long_01, keyboard_typing_apple, keyboard_typing_17s, lens_autofocus_f4_01/_03, camera_focus_nikon_d3100,
heartbeat_cinematic_54bpm, jet_pass_overhead_01, cash_register_kaching, factory_machine_room_electronics_hum,
factory_hum_light_activity_01, crowd_walla_indoor_large_02 (25 files ≈ 250 MB, `tools/epidemic_sfx_fetch.py`).
