PARAGUAY (Searching Lessons) — Premiere Pro package
=====================================================

WHAT'S HERE
  Paraguay_Premiere.xml   Final Cut Pro 7 XML — Premiere Pro imports it as a project with 2 sequences (see below)
  Media/Video/            paraguay_facecam_master.mp4 (clean face cam, cut + aligned to the final edit, 1920x1080 30p)
                          + Paraguay_4K_final.mp4  <-- the 4K master (3840x2160 24p) is the second file in the same
                            gofile folder; move it into THIS folder (Media/Video/) before importing
  Media/Audio/            VO_bleeped.wav (your voice, untouched except the 3 bleeped words muted)
                          VO_unbleeped.wav (your edited voice, nothing muted)
                          Music_bed.wav, SFX.wav, Ambience.wav (the stems; bleep tones are in SFX.wav)
                          Final_mix_reference.m4a (the delivered mix = VO_bleeped + Music + SFX + Ambience at 0 dB)
  Media/Raw/              put your original recording "2026-11-07 17-40-20.mp4" here (only needed for sequence 2)
  Assets/                 every photo, footage clip, logo, document, map, texture and font used in the edit,
                          with SOURCES.md files (credits/licences) in each folder
  Source/                 the HyperFrames compositions (HTML/GSAP) the graphics were built from, edit notes per segment,
                          EDL, transcripts, sound plan + music cue sheet (Epidemic Sound track list), research

IMPORT INTO PREMIERE PRO
  1. Unzip. Move Paraguay_4K_final.mp4 into Paraguay_Premiere/Media/Video/.
     (Optional) copy your raw "2026-11-07 17-40-20.mp4" into Paraguay_Premiere/Media/Raw/.
  2. Premiere Pro > File > Import… > choose Paraguay_Premiere.xml.
  3. Premiere will show the media as offline the first time (the XML points at /Paraguay_Premiere/Media/…).
     In the Link Media dialog click "Locate", browse to any one file inside YOUR Paraguay_Premiere/Media folder,
     keep "Relink others automatically" ticked, OK — every other clip relinks.
  4. Open the sequences in the imported bin.

SEQUENCE 1 — "Paraguay — final edit (4K)"  3840x2160, 24 fps, 27:01.8
  V2  the finished 4K edit, cut into 332 clips — one per scene, named "segment scene · words"; a sequence marker at
      every scene start with the narration line in its comment. Cuts are on the same file, so the playback is
      identical to the delivered master. Trim/replace/re-order scenes freely.
  V1  clean face cam aligned to the edit (disabled). Enable it to re-frame or replace shots (scale 200% for 4K).
  A1/A2 VO (bleeped) L/R · A3/A4 Music bed · A5/A6 SFX · A7/A8 Ambience — mix them at 0 dB to get the delivered
      mix (−25.9 LUFS, VO at unity). Rebalance the music per scene if you like; it is already ducked under the voice.

SEQUENCE 2 — "Paraguay — dialogue edit on raw take (104 cuts)"  1920x1080, 60 fps
  Your dialogue edit (retakes, ums, pauses removed) as 104 clips on the original recording, frame-exact. Use it to
  change any cut — the in/out of every clip is the cut point in the raw file.

WHAT DOES NOT TRANSFER (and why)
  The animated graphics (maps, charts, 2.5D, text, transitions) were built in code (HyperFrames: HTML + GSAP) and
  rendered — Premiere can't rebuild them as native layers, so they come in as the rendered 4K clips on V2. Their sources
  (photos, footage, maps, fonts) are all in Assets/ and the code is in Source/ if you want to rebuild a scene by hand.
  Epidemic Sound music is pre-mixed into Music_bed.wav; the individual tracks are listed in Source/project/SOUND_PLAN.md
  and music_cuesheet.json (licensed to your Epidemic subscription — re-download them from Epidemic if you want stems).

Fonts: Cooper Hewitt (OFL), Haskoy, Crimson Pro (OFL) — install from Assets/fonts if you add text in Premiere.
