# Mix rules: Silicon Valley origin doc (taiwan-edit)

These rules cover the edit's sound. The narrator comes first, the music is felt more than heard, and the SFX stay small, short and precisely timed.
The file inventory is in `LIBRARY.md`. Library files are stored hot (music at −18 LUFS, SFX at −6 dBFS peak),
and all levels are set in the composition.

---

## 0. Measured facts the levels are based on

| | Measured |
|---|---|
| `vo10.mp3` (narration, stereo 48 kHz) | **−27.2 LUFS-I**, true peak **−3.3 dBTP**, LRA 6 LU (ffmpeg ebur128) |
| Music cues `music/*/…_FULL.wav` | −18.0 LUFS-I (momentum −18.0, peak-limited at −1 dBFS) |
| SFX one-shots `sfx/*.wav` | peak −6.0 dBFS each |
| Composition frame rate | 24 fps (1 frame = 41.7 ms) |

> **Important:** the brief's absolute bed target of −28 to −32 LUFS assumes a VO near the usual −14 to −16 LUFS.
> This VO is quieter, at **−27.2 LUFS**. A bed at −30 LUFS would sit almost level with the voice. The relationship is what matters, so
> this document keeps the brief's relationship and **places the bed 12–16 LU below the VO**, which works out to **≈ −40 to −43 LUFS** here.
> If the whole master is raised later (see §7), every number moves together.

---

## 1. Voiceover: untouched

- One `<audio id="vo" src="vo10.mp3" data-volume="1" data-audio-group="voiceover">`, with **no `data-fx-chain`**, **no automation** and **no carve on it**.
- The `voiceover` group must contain **only** voice clips. Never put music, stingers or SFX in it, because the carve listens to that group.
- Nothing else in the mix may push the true peak above −1 dBTP. The VO peaks at −3.3 dBTP, so the stacked elements have only ~2 dB of headroom.

## 2. Music bed

| Situation | Bed loudness (target) | `data-volume` on a −18 LUFS cue | dB |
|---|---|---|---|
| Under continuous narration (default) | VO −14 LU ≈ **−41 LUFS** | **0.07** | −23 |
| Under very dense or important lines | VO −16 LU ≈ −43 LUFS, or drop stems (below) | 0.056 | −25 |
| Speech gaps ≥ 1.5 s (breaths between paragraphs) | **+3 dB** over the default | 0.10 | −20 |
| Music-only moments (title cards, montage ≥ 3 s, no VO) | VO −8 to −10 LU ≈ −36 LUFS | 0.13–0.16 | −17 |
| Stingers (`stinger_*`) on a reveal | ~2 dB over the bed at that moment, ideally in a VO gap | 0.08–0.10 | |

Formula: `data-volume = 10^((target_LUFS − file_LUFS)/20)`. File LUFS values are listed in LIBRARY.md.

**Thinning instead of ducking.** Each cue has stems (`_stem_marimba`, `_stem_pizz`, `_stem_pad`) that are sample-aligned and sum exactly to `_FULL`:

- Dense narration: use **pad + marimba** only, without pizz. For the densest passages use **pad only**, or marimba at −3 dB.
- Gaps and transitions: bring the full mix back by fading the missing stems in over 0.5–1 s.
- Place stems as separate `<audio>` clips with identical `data-start` / `data-media-start`, and put them in an `<hf-audio-group id="music">` bus so a single fader and a single carve-friendly chain control them all.

**Ducking with automation** (a volume lane in `data-automation`; `t` is clip-local seconds):

- Rise into a gap: start ~0.2 s after the last word ends and ramp up over **0.6–0.8 s** to +3 dB (×1.41).
- Return under speech: start ~**0.3 s before** the next word and ramp down over **0.25–0.35 s**. The bed should already be down when the first syllable arrives.
- Ignore gaps shorter than 1.5 s, because pumping on every breath sounds mechanical.
- Find the gaps in `transcript.json` (word timestamps). Treat any gap between words ≥ 1.5 s as a candidate.

**Spectral carve (required with music under VO).** Every music file already has a static voice pocket
(−2 dB @ 1.3 kHz, −4.5 dB @ 2.8 kHz, +4 dB shelf above 6 kHz). The music's 1–4 kHz energy measures −17 to −24 dB
relative to its total, against −7 dB for the narrator. On top of that, use the HyperFrames dynamic carve on the bed:

```bash
node ~/.claude/skills/hyperframes-audio/scripts/carve.mjs --comp index.html --bed music-bed --voice vo --strength 0.5 --dry-run
```

- Start at **strength 0.5** rather than the 0.8 default, because the static pocket is already baked in and we don't want the bed hollowed.
- Read the reported "level floor". If the carve adds more than ~6 dB of extra ducking on top of the 0.07 static level, lower the strength or raise `data-volume`.
- Run it without `--dry-run`, then run `npx hyperframes check`.
- Use `sources: ["voiceover"]`, which is the group, never a list of clip ids.

**Fades and transitions.** Fade the music in over 1.5–3 s and out over 2–4 s, and crossfade cues over **2 s** on overlapping tracks.
All cues share one key family (D major / B minor / G major), so any crossfade works. For a cleaner transition, crossfade on a downbeat.
Bar lengths are 2.5 s for curious, 2.143 s for historic, 2.609 s for tension, 2.222 s for momentum and 3.0 s for resolve.
Stinger hits land at 1.30 s (`stinger_reveal`) and 0.90 s (`stinger_tension`). Set `data-start = reveal_time − hit`.

**One continuous bed is easiest.** HyperFrames has no loop attribute. Either place copies of a seamless loop back-to-back
(each copy's `data-start` = previous start + loop length), or render one bed from a cue sheet:

```bash
.venv/bin/python tools/audio/build_bed.py sheet.json assets/audio/music/bed_full.wav
```

`build_bed.py` tiles the loops, applies 2 s equal-power crossfades, overlays stingers and handles per-stem trims. Its docstring documents the format.

## 3. SFX levels

The rule of thumb: an SFX peak sits **20–30 dB below the VO's peaks**. The VO peaks around −3 to −6 dBFS, so SFX peaks land around −26 to −33 dBFS.
All SFX files peak at −6 dBFS, so the gain is `data-volume = 10^((target_peak + 6)/20)`.

| Family | Target peak rel. VO | `data-volume` | Notes |
|---|---|---|---|
| UI pops/ticks, typewriter keys, ticker ticks (frequent, sit in the voice band) | −28 to −30 dB | **0.045–0.056** | Rotate the variants. Typewriter: cycle `typewriter_key_01…06` in a non-repeating order. |
| Paper slide/rustle, page flip, marker, highlighter, tape | −24 to −28 dB | **0.056–0.09** | |
| Photo drop, pin drop/pop, sticker, wood knock | −24 to −26 dB | **0.07–0.09** | |
| Whooshes | −22 to −26 dB | **0.07–0.11** | Use `_RtoL` for leftward motion. |
| Camera shutter transitions | −22 dB | **0.11** | |
| Risers | −22 to −24 dB | **0.08–0.11** | They must END on the cut. Set `data-start = cut − duration`. |
| Low impacts / booms (`impact_low_*`, `impact_thud_short`) | −16 to −20 dB | **0.14–0.2** | Mostly sub-bass, so they don't mask speech. Place them on reveals, ideally in a gap. Check that the true peak stays ≤ −1 dBTP. |
| Oscillator tones / radio tuning (one-off story beats) | VO −12 LU, in a gap or very low under VO | **0.02–0.03** | A pure 200 Hz–2 kHz tone is perceptually loud and sits in the voice band. Keep it ≤ 0.02 under words. |
| Fire burn reveal | crackle peaks ~ −26 dB | **0.06–0.1** | |

**Ambience beds (loops).** Set these by loudness, not by peak. Most should be barely audible (felt, not heard):

| Bed | File LUFS | Target | `data-volume` |
|---|---|---|---|
| `room_tone_loop_30s` | −17.6 | −58 LUFS | 0.01 |
| `vinyl_crackle_loop_30s` (archival sections only) | −33.5 | −52 LUFS | 0.12 |
| `wind_air_loop_30s` (clouds over maps) | −19.5 | −50 LUFS | 0.03 |
| `projector_loop_8s` (under archival footage) | −23.0 | −46 LUFS | 0.07 |
| `crt_hum_loop_6s` (vintage-TV framed clips) | −14.4 | −55 LUFS | 0.009 |
| `fire_crackle_loop_8s` | −34.6 | −48 LUFS | 0.2 |
| `radio_static_loop_6s` | −14.0 | −45 LUFS (brief) | 0.028 |

**Density.** Use no more than ~2 SFX at once, plus one bed. On a line the viewer must understand, skip SFX or keep them under 0.05.
Silence is a tool: drop all SFX for the most important sentence of each section.

## 4. Placing SFX on visual events (24 fps)

- **Land on the frame.** The transient sits on the exact frame of contact (photo hits the table, pin lands, number settles).
  LIBRARY.md lists each file's **onset / loudest** time. For clicks, drops and impacts, set `data-start = event_time − onset`. For whooshes and the fire reveal, use `event_time − loudest`.
- If you can't place it exactly, make the sound **0–1 frame late, never early**. Viewers accept sound slightly after the picture, but sound before the picture reads as an error.
- **Whooshes** peak at ~55–65% of their length. Centre them on the fastest part of the motion, not on its start.
- **Marker, highlighter and typewriter:**
  - Start `marker_circle`, `marker_underline` and `highlighter_swipe` on the first frame of the stroke animation. Trim with `data-duration` to the stroke length plus 50 ms and add a 40–60 ms volume fade-out at the end.
  - Use `marker_arrow` for an arrow drawn as shaft + head. Its strokes start at 0.00, 0.58 and 0.76 s, so match the animation to those times or split the file.
  - Letter-by-letter text: one `typewriter_key_0N` per **visible letter step**. For more than ~12 letters/s, use `typewriter_burst_12keys` or play every second letter. End the line with `typewriter_ding` (optional) or `typewriter_return`.
  - Rolling numbers: use `ticker_roll_decel_2s` when the count decelerates, or `ticker_roll_fast_1s` plus a final `ticker_tick_0N` on the landing frame.
- **Shutter transitions:** put the `camera_shutter_mech` transient on the cut frame.
- **Archival:** play `projector_start` into `projector_loop_8s` with a 0.3 s crossfade on the frame the archival footage starts. Fade out over 0.3–0.5 s when it ends.
- **CRT:** put `crt_power_on` on the frame the vintage TV lights up, then optionally `crt_hum_loop_6s` underneath and `crt_power_off` on exit.
- **Fades:** don't fade one-shots that start on a transient. Their natural attack is what syncs them. When you trim a sound mid-tail, add a 30–80 ms fade-out. Give loops and beds ≥ 0.5 s fades in and out.
- **Stereo:** the VO is centre. Pan movement-matched SFX with the L→R or R→L whoosh versions. Keep other one-shots near centre (they are mono content).

## 5. EQ carve guidance

- **Music under VO:** a static dip of −2 dB @ 1.3 kHz and −4.5 dB @ 2.8 kHz is already in the files, followed by the dynamic carve at strength ~0.5.
  If the voice still feels masked, add a `peaking` node at 2.5 kHz, −3 dB, q 0.8 to the `music` bus. Don't cut more than ~8 dB total in the 1–4 kHz band, because the bed starts to sound hollow.
- **SFX bus:** use a `highpass` at 100 Hz on everything except the impacts, which go to their own group or have no chain. Frequent voice-band SFX (typewriter, marker, ticks) can take a `peaking` 2.5 kHz −2 dB on the bus.
- **Never EQ the VO** (brief: VO untouched).
- **Low end:** only the pizz cello, the pad and the impacts live below 120 Hz. If the low end gets muddy under a boom, dip the bed by −3 dB around the hit, from 0.1 s before to 1 s after.

## 6. How HyperFrames handles audio (from `hyperframes-audio` + `hyperframes-core`)

- Every `<audio>` **must have an `id`**, otherwise the mixer skips it and the render is silent (lint: `media_missing_id`).
  Timing comes from `data-start` (seconds, scene-local inside sub-compositions), `data-duration` and optionally `data-media-start` (the trim offset into the file).
  Use `data-volume` (0–1, linear) for the static level and `data-track-index` for Studio lanes only. **Never add `crossorigin`.**
  Don't call `play()` / `pause()`; HyperFrames owns playback.
- **Volume automation:** `data-automation='{"version":1,"lanes":[{"target":"volume","points":[{"t":0,"v":0},{"t":2,"v":1}]}]}'`.
  `t` is clip-local seconds, while a lane on an `<hf-audio-group>` runs on **composition time**. Write the JSON in a double-quoted attribute with `&quot;`.
  A lane on a track overrides any GSAP `volume` tween, so don't do both.
- **Effects:** `data-fx-chain` (highpass, lowpass, peaking, shelves, compressor, limiter, gate, saturate, delay, reverb, chorus, phaser, bitcrush) runs the same Web Audio graph in preview and render.
  The compressor, limiter, gate and bitcrush **can't be automated**. To vary them, automate a `gain` node in front of them.
- **Buses:** `<hf-audio-group id="music" data-volume="…" data-fx-chain="…">` with members carrying `data-audio-group="music"`.
  Suggested groups:
  - `voiceover`: VO only, no chain.
  - `music`: bed clips, stems and stingers.
  - `sfx`: one-shots.
  - `amb`: ambience loops.
- **Carve:** `data-fx-carve` goes on the **bed clip** (not on a bus) and points at the `voiceover` **group**. Generate it with `carve.mjs` (see §2) and don't hand-edit `fromCarve` nodes.
- **Verify:** run `npx hyperframes check`, render, and then measure the render:
  `ffmpeg -i renders/out.mp4 -af ebur128=peak=true -f null -`. The integrated loudness should be within ~1 LU of the VO alone (−27 LUFS) and the true peak ≤ −1 dBTP.
  To check the bed relationship, render once with the VO muted and confirm the bed reads ~−41 LUFS under speech sections.
- Full details: `~/.claude/skills/hyperframes-audio/SKILL.md` and its `references/attributes.md`, `fx-registry.md` and `presets.md`.

Minimal pattern:

```html
<audio id="vo" src="vo10.mp3" data-start="0" data-duration="600" data-volume="1" data-audio-group="voiceover" data-track-index="1"></audio>

<hf-audio-group id="music" data-label="Music" data-volume="1"></hf-audio-group>
<audio id="music-bed" src="assets/audio/music/bed_full.wav" data-start="0" data-duration="600"
       data-volume="0.07" data-audio-group="music" data-track-index="2"
       data-automation="{&quot;version&quot;:1,&quot;lanes&quot;:[{&quot;target&quot;:&quot;volume&quot;,&quot;points&quot;:[{&quot;t&quot;:0,&quot;v&quot;:0},{&quot;t&quot;:2,&quot;v&quot;:1}]}]}"></audio>

<hf-audio-group id="sfx" data-label="SFX" data-volume="1"
  data-fx-chain="{&quot;version&quot;:1,&quot;nodes&quot;:[{&quot;type&quot;:&quot;highpass&quot;,&quot;id&quot;:&quot;n1&quot;,&quot;label&quot;:&quot;SFX low cut&quot;,&quot;params&quot;:{&quot;frequency&quot;:100,&quot;q&quot;:0.707}}]}"></hf-audio-group>
<audio id="sfx-pin-01" src="assets/audio/sfx/map_pin_drop.wav" data-start="41.958" data-duration="0.36" data-volume="0.08" data-audio-group="sfx" data-track-index="5"></audio>
```

## 7. Master / delivery (decision for the user)

With the VO at −27.2 LUFS and untouched, the finished mix will be about **−26 to −27 LUFS-I**.
YouTube and most platforms turn loud content down but **don't turn quiet content up**, so the video will play noticeably quieter than other channels.
The options:

1. **(Default, per brief)** Leave it. The VO stays bit-identical.
2. Apply one clean gain to the entire master, up to **+2 dB** before the VO's −3.3 dBTP peak reaches −1 dBTP. That's a small improvement, and the relationships are unchanged.
3. Normalize the final master to −14 to −16 LUFS with a true-peak limiter at −1 dBTP. This makes it competitive, but it is processing that the VO goes through (limiting its peaks). Do this only if the user approves.

---

## 8. As built for the 600 s edit (Phase 2): `tools/audio/place_sound.py`

The master plays three pre-mixed beds at **volume 1.0**. Their levels are final; `assets/audio/timeline.json` lists them for `tools/build_master.py`.
Pre-mixing is mandatory: 504 separate `<audio>` tags would overload the renderer. To change anything, edit the inputs and re-run the script (about 2–3 minutes).

The inputs are:
- `compositions/seg0*.sfx.json`
- `assets/audio/bed/music_cuesheet.json`, which is generated by `music_cuesheet()` in the script
- the `GAIN` table in the script

### 8.1 Music: act map (cue sheet)

| Time (s) | Cue / stems | Story beat |
|---|---|---|
| 0–4.32 | curious, pad only (the loop's last-bar A chord resolving to D) | cold open |
| 4.32–62.49 | curious, marimba enters on the downbeat at 4.32; pizz drops out in dense windows | Act I. `stinger_reveal` (−6 dB) hits at 35.36 (West burn) |
| 62.49–63.21 | curious, pad only | "completely flipped" |
| 63.21–~99 | historic 3/4 | Act II sepia |
| 93.53–122.98 | tension creeps in over 8 s | brain drain, archival montage |
| 122.98–214.67 | curious | Hoover storytelling. Comic violin-pizz "plink-plonk" at 143.94 ("fails"); `stinger_soft_rise` (−4 dB) at 157.22 ("Hoover gets in") |
| 214.67–249 | historic, strings forward (pad +3 dB) | Founding Grant / money |
| 249–286.84 | curious, marimba+pad building to full | GSB. `stinger_soft_rise` cadence at 286.84 ("a good start"), then a 0.7 s breath |
| 287.56–346.07 | curious, marimba + light pizz (−6 dB) | Terman motif |
| 346.07–474.95 | momentum from bar 5 (cello enters at 355) | Act V: "already had a Silicon Valley" builds to the 16th-note section |
| 474.95–491.48 | warm_resolve, pad (+ marimba −9 dB) | "mind palace": pulls back |
| 491.48–504.92 | tension, pad + sparse marimba | heartbreak dip |
| 504.66 | `stinger_reveal` (−3 dB), hit at 505.96 | "1938" turn |
| 505.96–600 | momentum from bar 1, building | the plan. Cliffhanger fade over 598.87–600, no cadence |

### 8.2 Music processing

- **Thinning:** in 10 s windows with ≥ 3.3 words/s (from `transcript.json`), the pizz stem drops out (marimba + pad remain), with a 1 s linear crossfade. Those windows also get −1 dB.
- **Pause detection:** `transcript.json` contains **no word gaps ≥ 1.5 s**; Whisper merges the pauses into the words. So pauses come from the **VO's own level**: 20 ms frames below −45 dBFS for ≥ 0.6 s, giving 49 pauses. The VO is only read, never processed.
- **Lift in pauses:**
  - pauses ≥ 1.2 s: +3 dB
  - pauses 0.6–1.2 s: +1.5 dB
  - ramp up from 0.15 s after the pause starts (≤ 0.6 s), and back down from 0.3 s before the next word
- **Dynamic carve:** an extra −3 dB @ 2.5 kHz (q 0.8) and −2 dB @ 1 kHz (q 1), crossfaded in by a speech envelope (50 ms attack / 300 ms release). This is on top of the static voice pocket baked into the cues.
- **Final level:** normalized to −41.0 LUFS-I.

Because the bed is pre-carved, do **not** also run `carve.mjs` on `bed-music` in the composition.

### 8.3 SFX

- **Generated per event:** most sounds are generated per event with a unique seed, using the library generators in `gen_sfx.py`. No two pops, slides, whooshes or marker strokes are identical.
- **Fixed takes:** some sounds use fixed files in round-robin:
  - shutters ×3
  - Kenney page flips ×3, ticks, pops, lamp clicks
  - the CRT switch / off
  - the chime
- **Sync point:** `start = t − sync_offset`, where the offset is:
  - the transient onset for hits, drops, clicks, pops, stamps, pins and shutters;
  - for whooshes, the loudest point is placed at the "peaks at X" time when the note gives one, otherwise ~0.12–0.35 s after `t`;
  - for strokes, rolls, swells and fires (anything with a `dur`), the sound starts at `t` and is fitted to `dur`.
- **Level:** the §3 table × −3 dB (`SFX_TRIM_DB`; this VO is quiet, with speech peaks ~ −16 dBFS). "very quiet / very soft / very low" notes get another −6 dB.
- **Hard cap per event:** the peak stays ≥ 20 dB under the VO's local peak (14 dB for the sub-heavy boom/stamp). In VO pauses the cap is −30 dBFS (−24 for boom/stamp).
- **Bus:** a 100 Hz high-pass on everything except the boom/stamp, and −2 dB @ 2.5 kHz on the whole bus.

### 8.4 Ambience

| Element | Where | `data-volume` equivalent |
|---|---|---|
| `projector_loop` markers | per marker | 0.06 (0.03 if "very low") |
| `crt_hum` markers | per marker | 0.009 |
| `wind` markers | per marker | 0.05 for gusts < 3 s, 0.035 for longer |
| Room tone | everywhere | 0.008 (0.011 on PAPER scenes) |
| Vinyl crackle | scenes whose notes mention sepia / weave | 0.10 |
| Cloud wind | the two cloud scenes (SC007, SC042) | 0.03 |

### 8.5 Measured test mix (`tools/audio/measure_mix.py`)

| | Measured |
|---|---|
| VO alone | −27.2 LUFS-I, −3.3 dBTP |
| VO + three beds | **−27.2 LUFS-I, −3.3 dBTP** (the beds add < 0.1 LU) |
| Music while the VO speaks | −41.3 LUFS (**−14.4 LU re VO**) |
| Music in VO pause bodies | −36.9 LUFS (+4.4 dB: the 3 dB lift plus the carve releasing) |
| SFX peaks (0.5 s windows) | median −36 dBFS, p90 −32, max −23.6 |
| SFX during speech | median **−20.6 dB under the local VO peak**, −32.7 dB under the VO's max peak |
| Ambience under speech | −53.7 LUFS |
