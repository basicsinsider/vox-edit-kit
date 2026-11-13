# Brief — "podcast" (working name until the topic is known), Searching Lessons
Owner: Krish. Written by the lead session, 2026-11-13, from the kickoff brief. Branch: `claude/podcast-aroll-edit`.
Quality bar and process: the Paraguay, Ivan and Taiwan videos (`project/paraguay/`, `project/ivan/`, MANUAL.md all of it).

## STATUS (2026-11-13)
Footage: the first Drive file was incomplete (zeros after 3.23 GB); Krish re-uploaded — id **1CI45TQU4BGLyQFiQ4mgI_jflW9ZbM_br**,
12,578,749,203 B, HEVC 3840×2160 30 fps + AAC 44.1 kHz dual-mono, 98:20. It is a two-person podcast (Sam + Sunkit), already switched
(split / single shots) and already tight (21 pauses > 0.9 s). Topic: how Silicon Valley was made (Terman, HP, Shockley, Fairchild,
Kilby, Moore) and how Taiwan set out to copy it (UN 1971, Chiang, the cabinet of engineers, Pan Wen-yuan), framed by the Tsao/UMC vs
Chang/TSMC cold open. **The file ends mid-conversation** (Boston / Innovator's Dilemma; the TSMC-vs-UMC story itself is never reached)
— flagged to Krish; the video ends on the last complete line.
EDL: `project/podcast/EDL.json` (226 word-level cuts from 5 analysts + lead, cut points in the quietest spot hugging the kept word,
30 fps grid, pauses > 0.9 s → 0.5 s) → master **5752.03 s = 95:52**. Plan: `SEGMENTS.md`, `sections.json` (pd01–03 intro 0–346 s;
pd04–pd44 = 41 edited sections, 1597 s). Palette `lib/palette_podcast.css`. Krish asked (before going to bed) to continue without
check-ins until the 720p gofile link.

## Credentials (never commit or print a key)
- Epidemic Sound: proxy-injected for www.epidemicsound.com; `tools/epidemic_mcp.py` reads the placeholder `~/.secrets/epidemic_key`
  (`epidemic_live_dummy`). Tested 2026-11-13: authenticated; `epidemic_fetch.py` downloaded a full WAV.
- inspo-frames (Krish's reference library, MCP over HTTPS): proxy-injected for inspo-frames.vercel.app (send any `Authorization: Bearer
  dummy`). POST https://inspo-frames.vercel.app/api/mcp, headers `Content-Type: application/json`, `Accept: application/json,
  text/event-stream`, body `{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"search","arguments":{"query":…,"limit":50,
  "filters":{"kind":"asset"}}}}`. Tools: list_boards, get_board, search, similar, frame. Tested 2026-11-13. All 57 assets are saved
  in the repo, so the key is no longer needed for this video.

## Inputs
- A-roll: one file `podcast.mp4` → `input/aroll.mp4` (gitignored). Work from proxies and audio extracts; delete intermediates.
  `curl -sSL -C - -o input/aroll.mp4 "https://drive.usercontent.google.com/download?id=<ID>&export=download&confirm=t"` (the
  connection reset once at 6.9 GB; `-C -` resumed it). Disk allowance is ~18 GB free at session start: check `df -h` first.
- Script: none. The A-roll is the narration: transcribe (Parakeet) and build the story from what is said. Ask Krish if a script is needed.

## Krish's rules for this video (binding)
1. **First 5 minutes: business as usual**, exactly like Paraguay/Ivan/Taiwan — full documentary edit (B-roll, maps, charts, call-outs,
   sound design) and the face-cam rules: no speaker on camera for the first 10 s, then short 1–2 s on-camera pop-ins during the intro.
2. **After 5 minutes: edited sections ONLY where truly necessary** to explain the story or improve the viewing experience (maps,
   charts, key names/numbers, documents, events); elsewhere the A-roll carries the video. Not reducing for its own sake.
   The A-roll is cleanly cut: ums, ahs, errors, false starts, retakes, long dead pauses removed via an EDL exactly as in
   `project/ivan/gen/build_edl.py` and the Paraguay notes (`project/paraguay/gen/`). Cuts only — never EQ/compress/gain/normalise the
   voice. Hide jump cuts with punch-ins.
3. **References: inspo-frames ASSETS only** (`filters.kind = "asset"`; not films, not youtube frames, not boards). 57 assets (maps,
   charts, typography, motion graphics, photos) — saved in `references/inspo-assets/` (assets.json, INDEX.md, img/, sheet_1–3.jpg).
   Do NOT use them all: only what fits this story; every visual matches the exact words under it; facts and names correct.
   Rebuild chosen references in our style (MANUAL §6/§6.1). The plan notes which asset id inspired each scene.
4. **Background music ALWAYS much lower than the voice.** ≥ 20 LU under the voice while he speaks, never closer than 18 LU at any
   moment (3 s short-term windows); restrained in pauses and between sections; voice loudness unchanged in the final mix; SFX well
   below the voice. Measure with `tools/audio/measure_mix.py`, `act_levels.py` and `vo_music_scan.py`; report the numbers with the
   720p review. Limits are written into MANUAL §0 / §10.8 "Music limits" + Changelog (done 2026-11-13).
5. **New palette** for this story, distinct from Taiwan's, Ivan's and Paraguay's (`lib/palette_<name>.css`); same fonts (Cooper Hewitt,
   Haskoy, Crimson Pro only), same animation style, effects, maps and sound-design approach. Show Krish a swatch; keep working.
6. **Delivery**: 720p review on gofile.io first; after approval the 4K final, also gofile.io (guest upload to
   `upload-eu-par.gofile.io/uploadfile`, md5 check, as Paraguay); remind Krish to download soon.

## Owner rules, always
Never assume — test. Never kill a running render. The lead's machine shuts down when idle: no long job between turns, heavy work on
helper sessions/agents. Rendering fast per MANUAL §11/§11.1 (one helper per segment; lead collects, assembles, delivers). Watch the
disk before every big write. Commit and push often. Never log in or create accounts.

## Order of work
1 credentials ✅ · 2 tell Krish we started ✅ · 3 download + transcribe ⛔ (file broken at source) · 4 topic/structure/length → report ·
5 EDL + clean A-roll cut · 6 plan (first 5 min in full; later only necessary edited sections, with a reason each) · 7 palette swatch ·
8 choose inspo-frames asset references · 9 gatherers + segment editors in parallel · 10 sound with the new limits · 11 QA snapshots of
every scene against its words · 12 render with helpers → 720p on gofile · 13 after approval: 4K on gofile.
