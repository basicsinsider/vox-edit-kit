# Agent briefs used for the approved 10-minute edit

The lead session ran these agents (Agent tool, background, in parallel where marked). Reuse them: replace the
project path, time ranges and topic. Every brief starts with "read MANUAL.md / the relevant docs first".

## 1. Story analyst → `analysis/BEATS.md`
Inputs: `transcript.json` (word timings), the trimmed voiceover. Produce: (1) a corrected transcript split into beats
of ~4–12 s covering the whole duration with no gaps — id, start/end snapped to word starts, exact words, one line
"what the viewer must understand"; (2) ASR corrections for misheard names + narrator slips/repeats the edit must not
emphasise; (3) an entity list (people, places, institutions, companies, objects, documents, dates, numbers) with beat
ids and exact key-word timestamps; (4) 1–3 on-screen key words per beat with their exact start times; (5) any data the
story needs (e.g. a current list of companies) from reliable sources with the source date; (6) story structure — acts,
time ranges, emotional tone (drives music and pacing). NO fact-checking of the narration's claims (owner's rule).

## 2. Director / edit planner → `EDIT_NOTES.md`, `ASSETS_NEEDED.md`, `SEGMENTS.md`
Reads MANUAL, BRIEF/USER_BRIEF, BEATS, references (style images + reels), the samples. Writes a shot-by-shot plan with
no gaps: scene id, start/end on word starts, ground (paper/night), effect numbers #1–#20 and reference layouts R#,
closest sample to copy, exact on-screen text + cue time per line (narration's words exactly), assets needed, camera,
transition, SFX cues with times, music notes. Requirements: every effect at least once, most several times WITH
variations (different TVs, newspapers, maps, 2.5D at the 2–3 moments that most deserve depth); every reference layout
used (except the owner's skips); never the same effect twice in a row; ≤3 scenes in a row on the same ground; text
minimal. Ends with a coverage table and open questions. ASSETS_NEEDED: deduplicated by type, existing vs to-find,
scene ids, subject/era, preferred free sources, licence, min resolution. SEGMENTS: ~6 contiguous segments of ~90–110 s
cut at scene boundaries, continuity rules (shared map look, recurring motifs, owners), and conventions (segNN ids,
`T()` text cues / `S()` structural cues, SFX markers in `compositions/segNN.sfx.json` as {t, type, scene, dur, level, note}).
The lead answers open questions with sensible defaults in `DECISIONS.md` rather than blocking.

## 3. Asset gatherers (run 3 in parallel, split by type) → `assets/**` + SOURCES.md + ✅/🔁/❌ in ASSETS_NEEDED
Common rules: MANUAL §8.1 sourcing playbook; free/PD/CC only; look at every file; log every file; use thumbnails +
throttling on Wikimedia; never log in; substitutes noted honestly; finish in ~40 min.
- **A — photos, logos, people cutouts**: archival photos (§1 of ASSETS_NEEDED), logos via `media-use resolve --type logo`,
  people cutouts via `remove-background` (blur halftone prints first), halftones, circle portraits.
- **B — documents, footage, TV props**: newspaper/document scans (+ headline bounding boxes), typeset recreations when
  missing (no fake signatures/seals), public-domain film clips trimmed to the best 6–20 s (contact sheet first),
  vintage TV/radio photos with the screen made transparent + `*_screen.json` bbox.
- **C — maps, 2.5D layers, textures, icons**: relief/beige/old maps with lon/lat→pixel JSON, 2.5D layer sets (backdrop
  with subject removed + blurred fill, mid, foreground, `layout.json`), extra textures (§3.4), own SVG icons.

## 4. Segment editors (run all in one wave, one per segment) → `compositions/segNN.html`
`EDITOR_BRIEF.md` is the brief. Each works in its own sandbox (`tools/make_sandbox.sh segNN`), reuses the approved
samples for their moments, snapshots every scene, runs `sync_audit`, writes `segNN.sfx.json` + `segNN.NOTES.md`,
and coordinates boundaries (first/last frame) with neighbours through the lead.

## 5. Sound designer (phase 1 at the start, phase 2 after picture lock)
Phase 1 — library: marimba-led score in one key family with stems (marimba / pizz / pad), mood cues + stingers,
synthesized so it's licence-free (`tools/audio/gen_music.py`), plus the SFX palette (`gen_sfx.py`, Kenney CC0
imports); LIBRARY.md + MIX_RULES.md. Phase 2 — placement: music cue sheet following the story acts, thin stems under
dense speech, lift in pauses (detected from the VO level, never processing the VO), every `segNN.sfx.json` marker
mapped to a sound with varied takes, ambience beds; pre-mixed into three 600 s beds + `assets/audio/timeline.json`
(`tools/audio/place_sound.py`); test mix measured (`measure_mix.py`). Music ≈12–16 LU under the voice.

## 6. Lead (you) between phases
Write the defaults, pass boundary notes between editors, promote good helpers into `lib/fx.js` + MANUAL, assemble with
`tools/build_master.py`, render a picture check, review contact sheets of the whole cut, fix, then the final render
with sound. Verify the VO in the final file still measures the same loudness as the raw file.
