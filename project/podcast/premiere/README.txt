TSMC vs UMC (Searching Lessons podcast) — Premiere Pro package
================================================================

The package comes as TWO zips in the same gofile folder. Unzip BOTH into the same place: they fill one folder,
TSMC_vs_UMC_Premiere/ (zip 1 = XML, audio, assets, source; zip 2 = the 44 rendered graphic sections).

WHAT'S HERE
  TSMC_vs_UMC_Premiere.xml   Final Cut Pro 7 XML — Premiere Pro imports it as a project with 2 sequences (see below)
  Media/Raw/                 put your original recording podcast.mp4 here (12.58 GB — not included, you already have it)
  Media/Sections/            pd01–pd44.mp4: every edited part, rendered 1920x1080 30 fps (pd01–pd03 = the 5:46 intro,
                             pd04–pd44 = the 41 graphic sections after it)
  Media/Audio/               Voice_edited.wav — your voices, cut by the EDL, otherwise untouched (mono, 44.1 kHz)
                             Islands/islNN_Music.wav, islNN_SFX.wav, islNN_Ambience.wav — the sound, as 39 "islands" (the intro
                               and each graphic section; there is no music anywhere else)
                             Final_mix_reference.m4a — the exact mix of the 720p review
  Assets/                    every photo, clip, map, document, logo, texture and font the graphics use (240 files), with the
                             SOURCES.md credit/licence files of their folders
  Source/                    the HyperFrames compositions (HTML/GSAP) the graphics were built from + each section's NOTES
                             (scenes, words, which inspo-frames asset inspired it), the EDL, transcripts, sections plan,
                             sound plan + SOUND_REPORT (loudness numbers), the Epidemic track log, the palette, the references

IMPORT INTO PREMIERE PRO
  1. Unzip both zips into the same place. Copy your podcast.mp4 into TSMC_vs_UMC_Premiere/Media/Raw/.
  2. Premiere Pro > File > Import… > choose TSMC_vs_UMC_Premiere.xml.
  3. The media shows offline the first time (the XML points at /TSMC_vs_UMC_Premiere/Media/…). In the Link Media dialog
     click "Locate", pick any one file inside YOUR TSMC_vs_UMC_Premiere/Media folder, keep "Relink others automatically"
     ticked, OK. If podcast.mp4 stays offline, locate it once in Media/Raw/.
  4. Open the sequences in the imported bin.

SEQUENCE 1 — "TSMC vs UMC — final edit"  1920x1080, 30 fps, 1:35:52
  V2  the 44 rendered sections at their exact frames (named "pdNN · title"); a marker at each section with the reason it
      exists. Trim, move or delete any of them — the A-roll is underneath everywhere.
  V1  the A-roll: your raw take cut into the 229 kept pieces of the EDL (frame-exact). Every second piece is the punch-in
      used to hide the jump cut (scale 54 % = 108 % of the 4K→1080 fit). In the review the punch-ins were anchored a little
      above centre (heads stay in frame); here they are centred — nudge Position if you want it identical.
  A1/A2  your voice (Voice_edited.wav on both channels, unity) — the same signal as the delivered audio.
  A3/A4 Music · A5/A6 SFX · A7/A8 Ambience — one clip per island, all at 0 dB. Played together with A1/A2 they give the
      review's mix: voice −18.2 LUFS, music at least 19.5 LU under the voice everywhere (see Source/project/podcast/SOUND_REPORT.md).

SEQUENCE 2 — "TSMC vs UMC — dialogue edit on raw take (229 cuts)"  3840x2160, 30 fps
  Just the clean dialogue edit on your original file (V1 + A1/A2), no punch-ins, no graphics — use it to change any cut;
  the in/out of each clip is the cut point in the raw file. (The delivered voice also has 4–12 ms fades at each join, so a
  cut here can sound very slightly different from Voice_edited.wav at the join.)

WHAT DOES NOT TRANSFER (and why)
  The animated graphics were built in code (HyperFrames: HTML + GSAP) and rendered, so they come in as rendered clips on V2,
  not as editable Premiere layers. Their sources are in Assets/ and the code is in Source/ to rebuild any scene by hand.
  The Epidemic Sound music is pre-mixed per island (Music.wav); the tracks used are listed in Source/project/EPIDEMIC_TRACK_LOG.md
  ("Podcast" section) and Source/project/podcast/cues/ — they are licensed to your subscription, re-download for stems.
  These sections are 1080p (the review resolution); the 4K versions get rendered after you approve the edit.

Fonts: Cooper Hewitt (OFL), Haskoy, Crimson Pro (OFL) — install from Assets/fonts if you add text in Premiere.
