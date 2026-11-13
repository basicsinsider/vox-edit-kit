# Podcast ("TSMC vs UMC") sound plan — Searching Lessons, master 0.00–5752.03 s (`project/podcast/media/vo_pd.wav`)

Sound designer. Sources: BRIEF.md rule 4 (the owner's loudest complaint: music always much lower than the voice), SEGMENTS.md §0/§1/§3,
`sections.json`, MANUAL §7, §10.3, §10.8 and its block **"Music limits — BINDING"**; earlier plans `project/paraguay/SOUND_PLAN.md`,
`project/ivan/SOUND_PLAN.md`. Tracks / ids / why: `assets/audio/epidemic/LOG.md` ("Podcast"). Measured stems, sections, keys:
`assets/audio/epidemic/ANALYSIS.md`. Status: phase 1 done (tools, tracks, generator, two test islands); **phase 2 (2026-11-13):
all 39 islands (pd01–pd44) built from the editors' final markers, ALL LIMITS MET in every island; full-length
`assets/audio/podcast/pd_beds_mix.flac` stitched and checked as the final mix is built.** After any change, `pd_islands.py --skip-built
--format flac` rebuilds only what changed, re-stitches, re-checks and rewrites `SOUND_REPORT.md`. Run ONE copy at a time: two concurrent
runs share `work/sound/isl/` and delete each other's VO slices (happened once on 2026-11-13; the second run's isl28 failed, re-built clean).

## 0. The design in one paragraph
Music and SFX exist only in **islands**: (a) the intro 0–346 s, whose tail fades over 5 s under Sam's first on-camera line, and (b) each
edited section pd04–pd44, where the music enters softly 0.8 s before the first frame and is gone 3 s after the last frame. Sections less
than 20 s apart share one island and the music is held 9 dB lower between them. That is 39 islands, 2154 s (37 %) of the 95:52; in the
other 60 minutes the bed file is digital silence — just the two voices. Inside an island the binding limits apply (§2).

## 1. Measured facts (never assumed)
**The voice** (`vo_pd.wav`, 44.1 kHz mono 16-bit, camera audio, cut only; every tool reads a 48 kHz copy):

| what | value |
|---|---|
| integrated loudness | **−21.2 LUFS** (ffmpeg ebur128 and the tools' BS.1770 agree: −21.24) |
| loudness range | LRA 3.8 LU (−23.2 … −19.4); per-5-minute LUFS-I between −20.6 and −21.9: very even |
| 3 s short-term while speaking | p1 −24.4 · p5 −23.6 · median −21.5 · p95 −19.4 · max −16.8 LUFS |
| 0.4 s momentary | p5 −27.7 · median −21.9 · p95 −17.9 · max −13.7 LUFS |
| peak | −4.6 dBTP (sample peak −4.8 dBFS) |
| noise floor | 20 ms RMS p0.5 −54.8 / p2 −52.0 dBFS; 9.8 % of frames under the −45 dBFS activity gate |
| density | 3 s windows count as "speaking" 100 % of the time: there are practically no pauses → nothing to lift, nothing to hide behind |
| the two speakers | **Sunkit is not quieter than Sam.** Aside 181–227 s: Sunkit's four lines −20.1 / −18.0 / −18.9 / −20.5 LUFS, Sam's lines −22.8 / −16.1 / −21.5 / −21.9 / −19.7. Sam swings more (story voice vs. emphasis); the duck follows the local level either way |
| the edited sections | LUFS-I per section −20.4 … −22.6; lowest 3 s window inside any section −25.9 LUFS (pd10, pd11) |
| mono → stereo | `ffmpeg amix` plays a mono voice at −3 dB per channel (tested: L/VO rms 0.709) = the same loudness as the mono file = the tools' convention. Copying the mono into both channels at full level would make the voice 3 dB louder and every gap 3 LU bigger |

**The tracks**: ten new Epidemic tracks, all measured **A minor** (r 0.74–0.91) on the WAVs — LOG.md has the table, ids and the stems-sum
check. Tempo-free floor: How Did We Get Here (melody stem; bpm 0).

## 2. The limits (MANUAL §10.8, Krish 2026-11-13) and where they are enforced
| limit | enforced by |
|---|---|
| music ≥ 20 LU under the voice while they speak (3 s windows: 5th percentile and median), never < 18 LU | `epidemic_bed.vo_duck` defaults (gap 20, margin 0.7, 3 passes) — **no cue sheet overrides them**; `pd_islands.py` refuses a sheet that does |
| music vs local speech level, 0.4 s: 1st percentile ≥ 15 (aim 18) | `vo_duck` gap_fast 18 |
| in pauses / tails: ≥ 20 LU under the VO's integrated loudness; **no pause lifts** | `vo_duck` ceiling 20; every sheet has `pause_lift_db: 0` |
| bed target VO − 22 LU | every sheet has `bed_lu_under_vo: 22`; each island's bed is normalised to its own VO slice − 22 |
| SFX: hero −16 dB, sub hits −19 dB, the rest −22 dB under the VO's local peak; music + SFX 3 s ≥ 14 LU under | `place_sound` caps (as coded) |
| voice untouched; final mix vs voice alone < 0.5 LU | the VO is only read; `pd_islands.py` measures mix − VO per island and per 10 s window |
Check per island: `vo_music_scan.py` must print **ALL LIMITS MET** (stored in `assets/audio/podcast/islNN/scan.txt` + `report.json`).

## 3. Layers and colours (one key family, so anything can follow anything over the drone)
| colour | track (stems, relative balance) | used for |
|---|---|---|
| floor | **How Did We Get Here** — melody stem, −29/−30 | under every island from its first to its last second; the only thing left between two sections of a shared island |
| IDEA / **ENG** | **Observatory** — instruments −22, melody −26, bass −30 (no drums) | intro opening → the insight → the phone numbers; pd10, pd11, pd14, pd16, pd17 (engineering explainers) |
| foundry | **Melted Mind** — instruments −22, melody −25, bass −29 | intro only: "In fact, a chip factory…" → foundry → "yes, almost on the spot" |
| mystery / **GEO** | **Mindscape** — instruments −22, bass −27, melody −25/−27 | intro: "one condition", the unnamed executive; pd15, pd20, pd21, pd23, pd35, pd40 |
| journey / **TW** | **Until Now** — instruments −22, melody −24/−25 (no drums, no bass) | intro: New York, "on top of the world"; pd24, pd25, pd27, pd28, pd36–pd39 (Taiwan builds) |
| cold / **DARK** | **Stay This Way** — instruments −22, melody −27, bass −27 | intro: the bust, the aside (melody only), the cold shoulder; pd22, pd26 |
| reveal / **OSA** | **One Step Away** — instruments −22, melody −24, bass −27, drums −28 (from the reveal only) | intro: two years later → Morris Chang → TSMC → rivalry; pd33 (the UN walkout) |
| **US** | **Sliding Doors** — instruments −22, melody −26 | pd04–pd09, pd12, pd13, pd43 (Stanford, Terman, HP, the lease, Route 128) |
| **REF** | **A Trace of Light** — melody −22, instruments −24, bass −29 | pd18, pd19, pd34, pd41, pd42, pd44 (theory, reflection) |
| **SPY** | **Seekers and Finders** — bass −23, instruments −24, melody −28 | pd29–pd32 (Kissinger's secret trip → the vote) |
Rules: one rhythmic track at a time; drums almost never (only One Step Away's from "Morris Chang"); nothing melodic in the voice band
is louder than the instruments stem; the voice-band pocket (−4.5 dB @ 2.5 kHz, −2.5 dB @ 1.2 kHz while they speak) is on every bed.
The intro's tracks come back as the section colours, so the long video rhymes with its opening (Observatory = the idea, Mindscape = the
executive/politics, Until Now = motion, One Step Away = betrayal → the walkout).

## 4. Cue table — the intro island (isl00, 0–351.5 s; master = island time)
| cue | master s | words the music moves on | music |
|---|---|---|---|
| I0 | 0–351.3 | — | drone floor (two takes cross-faded at 177–182) |
| I1 | 0.0–46.8 | "Our story starts in 1983" 0.08 · "an unique insight" 11.84 (opens +2 dB) · "You see, just a year earlier" 16.80 (bass in) · "24 million" 28.40 · "record profits" 41–45 | Observatory, the IDEA theme |
| I2 | 44.6–68.5 | "But quickly after that" 45.60 · "died away" 48.88 (sub drop, felt not heard) · "it just made no sense…" 53–65 | pulse gone: Stay This Way pad |
| I3 | 65.2–114.2 (+ last bars to 122.4) | "In fact" 65.97 · "a novel concept" 77.7 · "a foundry" 81–82 · "But before he could do that" 93.09 (−3 dB) · "But luckily" 113.89 · "yes, almost on the spot" 119–120.5 | Melted Mind |
| I4 | 120.6–161.6 | "But at the end of the meeting" 121.09 · "one condition" 123.86 (sub drop) · "most respected Chinese American" 132–136 · "25,000 people" 138 | Mindscape + its melody = the executive's motif |
| I5 | 160.3–183.4 | "After hearing this" 160.98 · "first flight to New York" 163 · "on top of the world" 176.6 (the track's own rise) | Until Now |
| I6 | 183.0–229.0 | Sunkit's questions 182.88–227.2 (face-cam pop-ins) | floor + a breath of Stay This Way melody: nothing rhythmic over two voices |
| I7 | 229.3–274.5 | "but to his surprise" 230.48 · "stonewalled" 244.08 (bass in) · "so he drops the idea" 268.83 | Stay This Way |
| I8 | 271.6–351.3 | "fast forward two years" 272.8 · "Just across the street" 277.07 (bass) · "And guess who" 297.87 (melody up) · **"Morris" 315.02** = file 100.0 s, the full band + riser/low hit · **"TSMC" 323.74** (deep hit) · "betrayal" 327.42 · "rivalry" 342.62 · pd03 ends 346.00 → 5 s fade under "So this is the rivalry…" | One Step Away |
Stingers sit in the music bed (so the duck governs them too). Phase 2: the editors' picture-synced hits win (MANUAL §10.8 Paraguay
note) — pd01 has whoosh 48.84 + boom 51.96 on the bust, pd03 air_swell 313.17 + boom_low 314.99 "MORRIS CHANG" (→ the dark cinematic
low hit), so our stingers there were removed. Kept: a felt sub drop on "one condition" 123.86 (−31 LU; pd02 has only a highlighter) and
a deep low boom under pd03's TSMC stamp at 323.74 (−30 LU). Per-cue trims from the act-level check (`TRIM` in the generator):
I2 +1, I5 −0.5, I6 +0.5 (+ the aside's melody raised from −29 to −20.5), I8 −1.5, I1/I4 instruments −21 → every intro cue −23.0…−24.0 LU.

## 5. Cue table — the 38 section islands (generated; `project/podcast/cues/index.json` lists every island's tracks)
Every section: floor + its colour from `section start − 0.8 s` (fade-in 1.3 s: still rising at the cut) to `section end + 3.0 s`
(fade-out 2.8 s). Read offsets rotate through steady passages of each track, so neighbouring sections never play the same bars.

| island | master | sections → colour | | island | master | sections → colour |
|---|---|---|---|---|---|---|
| isl01 | 7:28.7–9:27.6 | pd04 + pd05 → US (held −9 dB between) | | isl20 | 51:26.9–51:56.2 | pd26 → DARK |
| isl02 | 9:45.5–9:59.1 | pd06 → US | | isl21 | 53:12.6–53:29.9 | pd27 → TW |
| isl03 | 14:38.6–15:46.8 | pd07 → US | | isl22 | 54:25.7–55:22.2 | pd28 → TW |
| isl04 | 16:52.9–17:13.2 | pd08 → US | | isl23 | 57:37.6–58:39.8 | pd29 → SPY |
| isl05 | 18:26.5–18:53.2 | pd09 → US | | isl24 | 60:39.1–61:06.0 | pd30 → SPY |
| isl06 | 19:14.0–19:59.9 | pd10 → ENG | | isl25 | 62:46.5–63:16.2 | pd31 → SPY |
| isl07 | 22:44.6–23:57.5 | pd11 → ENG | | isl26 | 64:34.9–65:08.9 | pd32 → SPY |
| isl08 | 25:17.5–25:45.9 | pd12 → US | | isl27 | 66:43.2–68:56.8 | pd33 → OSA |
| isl09 | 26:31.7–27:27.0 | pd13 → US | | isl28 | 69:22.9–69:36.7 | pd34 → REF |
| isl10 | 30:00.7–31:41.2 | pd14 → ENG, pd15 → GEO | | isl29 | 70:06.8–70:26.6 | pd35 → GEO |
| isl11 | 32:04.6–34:45.9 | pd16 + pd17 → ENG (held −9 dB between) | | isl30 | 71:45.5–72:29.6 | pd36 → TW |
| isl12 | 36:24.3–37:07.3 | pd18 → REF | | isl31 | 73:17.4–73:49.5 | pd37 → TW |
| isl13 | 37:59.0–38:47.4 | pd19 → REF | | isl32 | 76:24.1–76:50.3 | pd38 → TW |
| isl14 | 41:04.8–41:45.0 | pd20 → GEO | | isl33 | 80:49.1–82:14.6 | pd39 → TW |
| isl15 | 43:01.0–43:46.1 | pd21 → GEO | | isl34 | 83:31.2–83:50.6 | pd40 → GEO |
| isl16 | 44:39.5–44:58.7 | pd22 → DARK | | isl35 | 84:35.3–84:51.8 | pd41 → REF |
| isl17 | 45:45.9–46:09.3 | pd23 → GEO | | isl36 | 86:20.8–86:43.4 | pd42 → REF |
| isl18 | 47:55.4–48:37.4 | pd24 → TW | | isl37 | 87:16.5–87:51.0 | pd43 → US |
| isl19 | 49:07.4–49:20.3 | pd25 → TW | | isl38 | 89:20.0–91:12.8 | pd44 → REF |
Phase 2, once the pictures are locked: per section the read offset is set so a track's own entry lands on the section's key word
(`OFFSET_OVERRIDE`), stingers go on reveals that have no editor boom (`SECTION_STINGERS`: e.g. "Deng Xiaoping", "Fairchild",
"kicked out of the UN"), and editors' markers that fight the music are dropped or retyped (`MARKER_EDITS`) — all in master seconds
in `gen/make_cuesheet.py`.

## 6. SFX approach (MANUAL §10.8 restraint; the owner wants SFX well below the voice)
- Editors write `compositions/pdNN.sfx.json` with `t` LOCAL to the composition; `pd_islands.py` shifts them to island time
  (`section start − island start + t`), never touching the editors' files. A marker that is clearly in master time is read as local and
  reported; unknown types are mapped (`PD_ALIAS`) or dropped and reported in `SOUND_REPORT.md`.
- **Hierarchy**: place_sound's restraint pass keeps, per scene, the hero event (+1 per 6 s), every camera move/whip (a low whoosh), ambience
  and booms/risers; small text/arrow ticks go. Never two hits within 0.25 s; repeats are pitch-shifted ±1–3 st.
- **Levels** (as coded, 4 dB lower than Paraguay): hero −16 dB, sub hits −19 dB, everything else −22 dB under the voice's local peak.
- **SFX-bus duck (new in phase 2, `pd_islands.py`)**: the peak caps do not bound the *loudness* of sustained or clustered sounds — the
  first full intro build measured music + SFX only 11.4 LU under the voice (phone ring 20 s, whoosh clusters 77 s, the reveal 315 s). So
  after place_sound the SFX bus alone is sidechained from the voice exactly like the music (`vo_duck`, gap 17.5 LU in 3 s windows,
  ceiling VO_I − 17.5, 0.4 s gap only 10 LU so hits keep their transient): music ≥ 20 + SFX ≥ 17.5 → together ≥ 15.6 LU (> 14).
  Active 0–28 % of the time per island, mean −3 dB. Intro after it: music + SFX min 16.3 LU.
- **Editors' invented types** are mapped in `PD_ALIAS` (checked before place_sound's own aliases): title_thud → stamp_thud,
  pen_scratch → marker_scratch, tile_fill → counter_ticks, pop → pop_soft, route_draw / line_draw → marker_long, tick_run / pop_run →
  dot_ticks, stamp → rubber_stamp, swipe (a fill sliding in) → highlighter_swipe (not place_sound's card_swipe), tile_place → dot_slide,
  ratchet → dial_click. ED02's `t_master` field is ignored.
- **Section edges**: a section hard-cuts in from the speakers — its first whoosh may sit on frame 0 (the island starts 1 s earlier, so
  nothing is clipped); nothing sounds after the last frame except the music's 3 s tail. No SFX and no room tone outside an island.
- Ambience: the generated room tone under each island (≈ −57 LUFS) plus editors' ambience markers (factory hum, projector, crowd) —
  felt, not heard. Big Epidemic ambience files are downloaded only when a marker needs one (`pd_islands.py --preflight`).
- No bleeps, no insert clips with their own audio in this video (the face cam is the voice track itself).

## 7. Pipeline (all commands from the repo root)
```
.venv/bin/python project/podcast/gen/make_cuesheet.py          # → project/podcast/cues/islNN.json + index.json
.venv/bin/python tools/audio/pd_islands.py --list              # the 39 islands
.venv/bin/python tools/audio/pd_islands.py --preflight         # markers: unknown types, missing Epidemic SFX files
.venv/bin/python tools/audio/pd_islands.py                     # every island (one at a time), stitch, report
.venv/bin/python tools/audio/pd_islands.py --only isl07 [--no-stitch]   # rebuild one island (also accepts pd11)
.venv/bin/python tools/audio/pd_islands.py --stitch-only       # re-stitch + report from the stored island pre-mixes
```
Per island: VO slice (a copy, `work/sound/isl/`, deleted afterwards) → shifted markers → `place_sound.py` → `vo_music_scan.py` VERDICT →
`act_levels.py` → mix-vs-VO → `assets/audio/podcast/islNN/premix.flac` (48 kHz stereo 16-bit, TPDF dither, 30/50 ms safety fades) +
`report.json`, `scan.txt`, `music_report.json`, `sfx_hierarchy.json`, `sfx_placements.json`; the three 24-bit beds are deleted unless
`--keep-wav`. Stitch: all pre-mixes are streamed in 10 s chunks into **`assets/audio/podcast/pd_beds_mix.wav`** (5752.03 s, 48 kHz stereo
16-bit, 1.1 GB; `--format flac` writes a far smaller FLAC instead) + `pd_beds_manifest.json` + `timeline.json`; the file is read back
to prove digital silence between islands. Final mix = the untouched voice + this one file at volume 1.0.
Measured cost: a 119 s island builds and measures in 33–43 s; the 60 s intro test in 13 s; the stitch of the full length in ≈ 10 s.

## 8. Phase-1 test results (2026-11-13; test audio deleted afterwards)
| test | VO LUFS-I | 3 s gap min / p5 / median | 0.4 s p1 | music + SFX min | per-cue level re voice | mix − VO | verdict |
|---|---|---|---|---|---|---|---|
| isl00, first 60 s (no markers yet) | −20.1 | 20.3 / 20.8 / 23.6 LU | 18.5 | 20.3 | I1 −23.8, I2 −24.8 LU | +0.02 LU | **ALL LIMITS MET** |
| isl01 = pd04 + pd05, 118.8 s, 8 dummy markers (7 kept) | −21.4 | 20.0 / 20.8 / 23.0 LU | 18.6 | 18.0 | −23.5 LU | +0.02 LU | **ALL LIMITS MET** |
No 3 s window without speech exists in either test (the "pauses" line of the verdict does not appear); the ceiling still caps the
music at VO − 20 everywhere. The duck was active 33–37 % of the time (mean −2.3 / −3.6 dB, max −6.7 / −11.6 dB). Stitch check: the
island in the full-length file is bit-identical to its pre-mix; 1 s before it and after the test intro the file is exactly zero.

## 8b. Phase-2 results (2026-11-13, all 39 islands; details per island in `SOUND_REPORT.md`)
Final (39 islands, 2158 s = 38 % of the video): identical pooled numbers to the 34-island state below; every cue −22.4…−24.0 LU re
the voice; full-length final-mix check: voice −18.2 / mix −18.2 LUFS-I, LRA 3.8 / 3.8, true peak −4.6 / −4.6 dBTP. pd42 boundary
(5201.70) applied. Earlier state, pooled over 34 islands (1951 s): 3 s music gap while speaking min **19.5** / p5 **20.8** / median **22.6** LU; 0.4 s p1 **18.6**;
music + SFX min **16.1**; mix − voice ≤ **+0.02 LU** per island. Every cue −22.4…−24.0 LU re the voice. Full-length check of the
stitched FLAC exactly as the final mix is built (mono VO duplicated L = R at unity + the bed, `amix normalize=0`): voice alone
−18.2 LUFS-I, mix −18.2 LUFS-I, LRA 3.8 = 3.8. pd08 needed a different passage of Sliding Doors (`OFFSET_OVERRIDE` 60: the 104 s
passage ducked to −24.1). Boundary moves applied from `sections.json`: pd09, pd26, pd34, pd37, pd39. Islands rebuild only when their cue
sheet, markers or window change (`inputs_sha` in each report.json). Build time: 34 islands in ≈ 11.5 min, one at a time.

## 9. Open points (phase 1 list; 1–3 done for pd01–pd39)
1. Editors' `compositions/pdNN.sfx.json` (none existed during phase 1) → preflight → download missing SFX.
2. Any section boundary the lead moved → `sections.json` is the only source; re-run `make_cuesheet.py`.
3. Word-exact section cues, stingers and marker edits (§5); per-cue balance to −20…−24 LU re the voice.
4. `tools/audio/measure_mix.py` crashes on an island without any SFX (empty percentile) — `pd_islands.py` measures mix − VO itself,
   so it is not needed per island; run it on the final mix if wanted.
5. `.gitignore` covers `assets/audio/podcast/**/*.wav` but not the island `premix.flac` files (≈ 2.6 MB per minute of island).
