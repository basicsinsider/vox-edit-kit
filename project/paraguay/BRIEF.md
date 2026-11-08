# Brief — "Paraguay" (geopolitical documentary, the crisis now unfolding in Paraguay), Searching Lessons
Owner: Krish. Written by the Paraguay lead session, 2026-11-08, from Krish's own instructions.
Quality bar: the finished **Ivan** documentary (`project/ivan/`, delivered as Ivan v3 in 4K) — "the edit should be the same
quality as the Ivan one". Same process, look and quality; be super creative within the house style. MANUAL.md (all, esp. §0,
§10 incl. §10.5/§10.10, §11/§11.1 and the Ivan changelog) applies; this file adds to / overrides it for this video.

## Inputs (tested reachable from the cloud on 2026-11-08)
- **Script** (Google Doc): https://docs.google.com/document/d/1EFDdzsJWv7kqMxGf6awnqVD0Yae70ePQehKttXPe22U/edit
  Plain text: `curl -sSL "https://docs.google.com/document/d/1EFDdzsJWv7kqMxGf6awnqVD0Yae70ePQehKttXPe22U/export?format=txt"`
  → `project/paraguay/src/script.txt` (~4,800 words; opens "That's a paraguayan congressman getting dragged out by protestors.").
  It contains notes and links (e.g. the X link) that are not narration.
- **Raw face cam**: ONE file, `2026-11-07 17-40-20.mp4`, 7.52 GB, Drive folder
  https://drive.google.com/drive/folders/1KvgHGKgBqWBlUII5GZW07hequawIIJG0 —
  `curl -sSL -o input/raw_facecam.mp4 "https://drive.usercontent.google.com/download?id=1uzGtoshYwVaGAV8lpi6ebeI1mT4I0seJ&export=download&confirm=t"`
  (input/*.mp4 is gitignored — keep it that way).
- **The X post** in the script: https://x.com/xx17965797n/status/2118781730370806217 (Truthseeker, 2026-11-06: "Paraguayans dragging
  politicians out of Congress as anger mounts in Paraguay"). 29.2 s vertical video, 720×1280 with audio. Fetched via
  `curl -sS https://api.fxtwitter.com/xx17965797n/status/2118781730370806217` → `tweet.media.videos[0].url` (video.twimg.com) →
  `input/x_congress.mp4`. Krish: "Make sure to use the footage from the X link in the script in the intro." It is the cold-open
  shot under the first line. Frame the vertical video in house style (phone / social-post frame, or blurred fill) and credit it on screen.

## Krish's rules for this video (binding)
1. **Improvisations.** The raw take may contain improvised lines. Align the edit to what he actually says (ASR of the raw take),
   using the script as a guide, not a strict text. Keep good improvised lines that fit the story; drop off-track ones. On-screen
   text matches his actual words.
2. **Clean the take** — cut errors, ums, ahs, long unneeded pauses, repetitions, false starts and retakes, with an EDL exactly
   like Ivan (`project/ivan/gen/build_edl.py`, `render_vo.py`, MANUAL Ivan notes). Cuts only — never EQ/compress/gain/normalise the
   voice. Clean cuts in silences with a few-ms crossfades. Face-cam picture stays in sync.
3. **Face cam**: no narrator on camera for the first 10 s. Intro (first 1–2 min): he pops in often, but only 1–2 s each time.
   After that ≈ 35 % narrator on camera, ≈ 65 % edit. MANUAL §10.5 face-cam rules + Ivan practice (clean & modern, punch-ins hide
   jump cuts, frame-exact shot edges per FIXES_ROUND1 §4).
4. **Geopolitical documentary: the Paraguay crisis.** It starts from one bank, **Ueno**, which around 60 % of adults used; then
   protests, the president's resignation (rejected), and his arrest. B-roll for that subject: real photos, footage, news,
   documents, maps (Paraguay and the region, in map-kit style), charts. Every visual matches the exact words under it.
   Copyrighted material is OK under fair use — credit it and log it in SOURCES.md.
5. **Same style as Ivan**: animation style, effects, charts, maps, sound design (layered Epidemic bed, restraint pass), fonts
   (Cooper Hewitt, Haskoy, Crimson Pro only). MANUAL §10.10 (grid placement, clean meaningful text, contrast) is binding.
   **A NEW palette** for this story (not Taiwan's, not Ivan's): `lib/palette_paraguay.css`, colours with story meanings, yellow kept
   for the highlighter + one key number. Show Krish a swatch (`references/palette_paraguay.png`); keep working while waiting.
6. **Render order (Krish, 2026-11-08):** the first full render is **720p** so he can watch quickly and approve; only AFTER his
   approval render the 4K master. **Deliver at the Ivan v3 spec (4K)** via the same tools (`tools/render_piece.sh` with `RES=4k`, `tools/deliver_chunked.sh`),
   plus review copies.
7. **Fast rendering**: MANUAL §11/§11.1 and the Ivan 4K notes — helper cloud sessions render one segment each; the lead collects,
   assembles and delivers.

## Owner rules, always
- Never assume anything — test it, even with a tiny check, before relying on it or telling Krish.
- Never kill a running render, for any reason.
- The lead's machine shuts down when the session goes idle: never leave a long job running between turns; stay in a blocking wait,
  heavy work on helper sessions/agents.
- Watch the disk before every big write (the footage alone is 7.5 GB).
- Commit and push to `claude/paraguay-edit` often. Never commit any key. Never log in or create accounts.
- Epidemic Sound: key stored as an environment network secret for www.epidemicsound.com (proxy-injected); `tools/epidemic_mcp.py`
  reads a placeholder from `~/.secrets/epidemic_key` (`epidemic_live_dummy`). Tested 2026-11-08: SearchSoundEffects works.

## Order of work
1. Epidemic key ✅ → 2. tell Krish we started ✅ → 3. download inputs → 4. ASR of the raw take, align to the script, EDL, edited VO
+ word-timed transcript; report the edited length → 5. plan (BEATS, EDIT_NOTES per segment, SEGMENTS, ASSETS_NEEDED, DECISIONS,
SOUND_PLAN — same set as Ivan) → 6. palette swatch → 7. asset gatherers + segment editors (parallel agents) → 8. sound → 9.
snapshot QA of every scene against its words → 10. render with helpers, assemble, deliver → 11. report to Krish at each milestone.
