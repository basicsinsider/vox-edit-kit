US vs CARTELS (Searching Lessons) — Premiere Pro package, FINAL 4K (2026-11-23)
==============================================================================
This is the delivered final 4K (gofile US_vs_Cartels_4K_final.mp4: fix round 1 + Krish's 3D renders) as an editable timeline.

WHAT'S HERE
  US_vs_Cartels_Premiere.xml   Final Cut Pro 7 XML — Premiere Pro imports it as a project with 2 sequences (see below)
  Media/Video/Segments/        put the 15 rendered 4K files here: cts00_4k.mp4 … cts14_4k.mp4 (3840x2160, 24 fps).
                               They are separate files in the same gofile folder as this zip (too big to zip together).
  Media/Video/3D/              Krish's 3D renders conformed to 4K/24 fps on the edit's frame grid (R1, R4 — R4 contains R2 and R3)
  Media/Audio/                 VO.wav (the edited voice after the review cuts — cuts only, samples untouched, starts after the 4.5 s
                               cold open), Cold_open_clip_audio.wav, Music_bed.wav, SFX.wav, Ambience.wav (the stems),
                               Final_mix_levelled.m4a (the delivered mix, with the owner-requested levelling ride)
  Media/Raw/                   us vs cartels.wav — the original recording (sequence 2)
  Assets/                      every photo, clip, logo, document, map, texture and font used, with SOURCES.md credits;
                               Assets/3D_renders_original/ = the four 3D renders exactly as downloaded from the Google Doc links
  Source/                      the HyperFrames compositions, edit notes, EDL + EDL_NOTES, fix-round-1 notes and ops, transcripts,
                               sound plan + cue sheets, research

IMPORT INTO PREMIERE PRO
  1. Unzip. Move the 15 files cts00_4k.mp4 … cts14_4k.mp4 into US_vs_Cartels_Premiere/Media/Video/Segments/.
  2. Premiere Pro > File > Import… > choose US_vs_Cartels_Premiere.xml.
  3. The media shows offline the first time (the XML points at /US_vs_Cartels_Premiere/Media/…). In the Link Media dialog click
     "Locate", browse to any one file inside YOUR US_vs_Cartels_Premiere/Media folder, keep "Relink others automatically" ticked,
     OK — every other clip relinks.

SEQUENCE 1 — "US vs Cartels — FINAL (3840x2160)"  24 fps, 21:55.125 (31,563 frames) = the delivered final 4K
  V1  cts00 (the cold-open crowd clip) + the 14 rendered segments, cut into 326 clips: one per scene, plus a cut at every place
      the review round tightened the voice-over (the segments were rendered on the earlier, longer timeline — those frames are
      simply trimmed out here). Sequence markers at every scene start, with the narration line in the comment.
  V2  Krish's 3D renders over V1:  R1 "All of this was happening because the Mexican army had come for one man … not related"
      (0:35.75–0:47.33) · R4 "To answer that, we have to start with the guy from last night … in charge of shooting and killing"
      (1:57.88–3:18.96). Disable V2 to see the original graphics underneath.
  A1/A2 VO · A3/A4 cold-open clip sound · A5/A6 music · A7/A8 SFX · A9/A10 ambience — at 0 dB these sum to the mix BEFORE the
      levelling ride Sam/Sanket asked for. A11/A12 = the delivered levelled mix (muted, reference; solo it to compare).
      The SFX under the 3D renders were removed (they belonged to the replaced graphics); music and ambience run on.

SEQUENCE 2 — "VO edit on the raw take (reference)"  audio only, 60 fps grid
  The voice edit (retakes, false starts, pauses removed + the review-round tightening) as clips on the original recording.
  Cut points are rounded to 1/60 s here; the exact cuts (with 4–12 ms crossfades) are in Media/Audio/VO.wav.

WHAT DOES NOT TRANSFER
  The animated graphics were built in code (HyperFrames: HTML + GSAP) and rendered — they come in as the rendered 4K clips on V1;
  their sources are in Assets/ and the code in Source/. Epidemic Sound music is pre-mixed into Music_bed.wav (tracks listed in
  Source/project/SOUND_PLAN.md and music_cuesheet_v2.json).
