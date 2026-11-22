US vs CARTELS (Searching Lessons) — Premiere Pro package (4K)
==============================================================

WHAT'S HERE
  US_vs_Cartels_Premiere.xml   Final Cut Pro 7 XML — Premiere Pro imports it as a project with 2 sequences (see below)
  Media/Video/Segments/        put the 14 rendered 4K segments here: cts01_4k.mp4 … cts14_4k.mp4 (3840x2160, 24 fps).
                               They are separate files in the same gofile folder as this zip (too big to zip together).
  Media/Audio/                 VO.wav (your edited voice — cuts only, samples untouched, stereo, padded with silence to the
                               picture length), Music_bed.wav, SFX.wav, Ambience.wav (the stems),
                               Final_mix_reference.m4a (the delivered mix = VO + Music + SFX + Ambience at 0 dB)
  Media/Raw/                   us vs cartels.wav — your original recording (sequence 2)
  Assets/                      every photo, footage clip, logo, document, map, texture and font used in the edit, with
                               SOURCES.md files (credits/licences) in each folder
  Source/                      the HyperFrames compositions (HTML/GSAP) the graphics were built from, edit notes per segment,
                               EDL + EDL_NOTES (what was removed from the VO), transcripts, sound plan + music cue sheet, research

IMPORT INTO PREMIERE PRO
  1. Unzip. Move the 14 files cts01_4k.mp4 … cts14_4k.mp4 into US_vs_Cartels_Premiere/Media/Video/Segments/.
  2. Premiere Pro > File > Import… > choose US_vs_Cartels_Premiere.xml.
  3. Premiere shows the media as offline the first time (the XML points at /US_vs_Cartels_Premiere/Media/…).
     In the Link Media dialog click "Locate", browse to any one file inside YOUR US_vs_Cartels_Premiere/Media folder,
     keep "Relink others automatically" ticked, OK — every other clip relinks.
  4. Open the sequences in the imported bin.

SEQUENCE 1 — "US vs Cartels — final edit (3840x2160)"  24 fps, 22:21.917 (32,206 frames)
  V1  the finished edit as the 14 rendered 4K segments, cut into 180 clips — one per scene, named "segment scene · words";
      a sequence marker at every scene start with the narration line in its comment. Trim/replace/re-order scenes freely.
  A1/A2 VO L/R · A3/A4 Music bed · A5/A6 SFX · A7/A8 Ambience — at 0 dB they give the delivered mix (−32.1 LUFS, VO at
      unity). The music is already ducked ≥ 20 LU under the voice; rebalance per scene if you like.
  No face-cam track (this video has none).

SEQUENCE 2 — "US vs Cartels — VO edit on the raw take (86 pieces, reference)"  audio only, 60 fps grid
  The voice edit (retakes, false starts, long pauses removed — see Source/project/EDL_NOTES.md) as 86 clips on your
  original recording. Cut points are rounded to 1/60 s here; the exact cuts are in Media/Audio/VO.wav.

WHAT DOES NOT TRANSFER (and why)
  The animated graphics (maps, charts, 2.5D, text, transitions) were built in code (HyperFrames: HTML + GSAP) and rendered —
  Premiere can't rebuild them as native layers, so they come in as the rendered 4K clips on V1. Their sources (photos,
  footage, maps, fonts) are all in Assets/ and the code is in Source/ if you want to rebuild a scene by hand.
  Epidemic Sound music is pre-mixed into Music_bed.wav; the individual tracks are listed in Source/project/SOUND_PLAN.md and
  music_cuesheet.json (licensed to your Epidemic subscription — re-download them from Epidemic if you want stems).

Fonts: Cooper Hewitt (OFL), Haskoy, Crimson Pro (OFL) — install from Assets/fonts if you add text in Premiere.
