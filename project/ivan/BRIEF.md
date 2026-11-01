# Brief — "Ivan" (geopolitical documentary, Russia–Ukraine war), Searching Lessons
Owner: Krish. Written by the Taiwan-project lead session, 2026-11-01, from Krish's own words (quoted where it matters).
This project uses the SAME kit, look, process and quality bar as the Taiwan edit (`review/intro_720p.mp4`,
`review/c1…c6_720p.mp4`, MANUAL.md all sections incl. §10–§11). Everything below either adds to or overrides that.

## Inputs (tested reachable on 2026-11-01)
- **Script** (Google Doc, public): https://docs.google.com/document/d/1QOJriv_2sj0OsWOmRBkoUFSJW96ZT698JWwZHPXemu8/edit
  Plain text: `curl -sSL "https://docs.google.com/document/d/1QOJriv_2sj0OsWOmRBkoUFSJW96ZT698JWwZHPXemu8/export?format=txt"`
  (~5,700 words; starts "Somewhere inside Russia, a man named Ivan has been living a rather dangerous double life…";
  first line is a "May be title:" note with a YouTube link — a note, not narration).
- **Raw footage** (Drive folder https://drive.google.com/drive/folders/1MyWRBUWSfeQS7UDaUKQ-wUM_GjL8Pl5q): ONE face-cam
  recording `2026-10-31 20-42-52.mp4`, 4.57 GB, file id `1jirvzCa800k6WBoQKLDAKQ8iYLKE0ugx`. Download:
  `curl -sSL -o "input/raw_facecam.mp4" "https://drive.usercontent.google.com/download?id=1jirvzCa800k6WBoQKLDAKQ8iYLKE0ugx&export=download&confirm=t"`
  (tested: HTTP 206/200, video/mp4). Keep it gitignored (input/ media is not committed).
- Krish estimates the finished video at **15–20 minutes**.

## Krish's rules for this video (binding)
1. **Edit the narration from the raw face-cam**: "trim the footage to align with the script + remove any uhms, ahs,
   repetitions, mistakes, etc. when the narrator is narrating." Build the voiceover by CUTTING the raw take (transcribe it
   with the kit's Parakeet/ASR, align to the script, keep the best clean take of every line, drop fillers, false starts,
   repeats and retakes). Cuts only — still never EQ / compress / gain / normalise the voice (MANUAL §0). Make every audio
   cut clean (cut in silences, tiny crossfades of a few ms at the cut points are fine — no audible clicks). Keep the
   picture of the face cam in sync with its audio after every cut (it's one file, so cut both together). Produce an
   edit decision list (EDL) so every cut is traceable, and the final edited VO + transcript with word timings.
2. **Face-cam rules**: no narrator on camera for the first 10 s. In the intro (the first 1–2 min) the narrator pops in on
   camera more times, but only for **1–2 s** each. For the **rest of the video: ~35 % narrator on camera, ~65 % edit**
   (B-roll / graphics). Face cam stays clean and modern (MANUAL §10.5 face-cam rules: text treatments OK, graphics may sit
   behind him via remove-background cut-out). Use the on-camera moments where he talks to the viewer / makes a point;
   vary the framing (punch-ins on cuts hide jump cuts from the trimming).
3. **Genre: geopolitical documentary** about something connected to the Russia–Ukraine war — "not business
   documentary". Pick B-roll (photos, footage, documents, maps, newspapers, paintings/posters, propaganda posters,
   satellite views) for that subject. Real/true images preferred; copyrighted material is OK (fair use: commentary,
   transformed, credited). Every visual matches the exact words under it.
4. **Same** animation style, effects, maps (assets/maps/kit + new Eastern-Europe kit maps in the same style), charts,
   reference layouts (D01–D15, refs 1–12 and variations), sound design (layered Epidemic bed, restraint pass), fonts
   (Cooper Hewitt, Haskoy, Crimson Pro only).
5. **A different colour palette** from the Taiwan one (lib/palette.css is Taiwan's — do not edit it; make
   `lib/palette_ivan.css` and load it for this project only). Give the colours meanings for this story (e.g. Russia /
   Ukraine / the double agent / the West) the way Taiwan's palette did (MANUAL §10.2), keep yellow = highlighter + one key
   number. Make a swatch PNG like `references/palette_taiwan.png` and show it to Krish.
6. **"Be super creative with this."** New layout variations, new map moves, new transitions in the house style.
7. **Rendering must be fast**: follow MANUAL §11 / §11.1 exactly — helper cloud sessions render one segment each
   (`tools/render_piece.sh`), the lead collects (`tools/collect_pieces.sh`), assembles (`tools/assemble_chunk.sh`) and
   delivers (`tools/deliver.sh`). Never kill a render. Stay actively working while anything long runs (the container is
   shut down when the session is idle). Watch the disk before every big write.
8. **Never assume — test** everything, even with a tiny check, before relying on it or reporting it.

## Process (same as Taiwan; scale it to 15–20 min)
1. Download footage + script → ASR transcript of the raw take → script alignment → EDL → edited VO (+ face-cam video
   timeline) → transcript with word timings of the edited VO. Report the edited length to Krish.
2. Plan (analyst/planner): BEATS, EDIT_NOTES (every scene, words → picture), SEGMENTS (split into ~3-min segments for
   parallel editors and helpers), ASSETS_NEEDED, DECISIONS, palette — same formats as `project/intro/` and `project/c1…c6/`.
3. Asset gatherers, segment editors (parallel agents, one per segment), sound designer (Epidemic, layered bed), sync
   audit, lint, snapshot QA of every scene against its words.
4. Render via helpers → assemble → mix (VO at unity) → review copies + full-quality master on `deliveries/ivan`
   → send Krish the review and the pull commands.
5. Keep MANUAL.md + Changelog current with anything new learned.

## Things the lead must get from Krish
- The **Epidemic Sound API key**: it lives only in the Taiwan session's container (never in git). Ask Krish to paste it
  into this session or set it as the environment secret `EPIDEMIC_SOUND_MCP_API_KEY`; then store it at
  `~/.secrets/epidemic_key` (never commit it). Everything else can start without it.
- Approval of the palette swatch (keep working while waiting).
