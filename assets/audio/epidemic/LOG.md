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

### Candidates auditioned (by metadata + measured key from previews; not downloaded)
Formations (Van Sandano, 100, Ab minor — wrong key for the set), Chrysotile (Farrell Wooten drone, C# minor — clashes with D),
Imber (140, F# minor), Ostinato (Vieveri, 180, A minor — strong alternative for a build), City Phases (John Abbot, 150, A minor —
alt for the boom), Terms of Gravity (Eb major), Building Something Together (Eden Avery, B major), Methodus (C# minor),
Deception Uncovered (C major/minor dark drone), Behind the Curtain (E), The Last Horizon (A major), Silent Sun (Anna Landström,
116, F major — hopeful, alt for act VIII), April (G major), Reclaim (C minor), A Pinpoint of Light (105, D minor — alt pulse),
Still in Blues (G minor drone), Air (A minor drone), Lotus River (D major). Similar-search seeds: Melting Glass, Formations, Chrysotile.
c3/c5 audition (similar to Melting Glass / Estimations / Formations; key from previews): Covert Affairs (E minor), The Mole (F# minor),
Methodus, Fake Photisms / Paradigm Shift / Neon Noir (E minor), Rise of the Velcro (B minor), Sense of Betrayal / Rushes To (C minor),
Allegro Sotto Le Stelle (Ab major) — off-key; No One in Sight, Mindscape (A minor) — spares.

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
