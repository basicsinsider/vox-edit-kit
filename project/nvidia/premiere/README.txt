NVIDIA — "Is the chip ban actually working?" (Searching Lessons) — Premiere Pro package, 4K
=============================================================================================

THE GOFILE FOLDER HOLDS
  NVIDIA_Premiere.zip              this package (XML, audio stems, assets, source)
  nvidia_facecam_master_4k.mp4     clean face cam, native 4K (3840x2160 30p), cut + aligned to the edit
  nvs01_4k.mp4 … nvs23_4k.mp4      the 23 rendered 4K segments of the edit (3840x2160 24p, no audio)
  00_READ_ME_FIRST.txt

WHAT'S HERE (after unzipping)
  NVIDIA_Premiere.xml     Final Cut Pro 7 XML — Premiere Pro imports it as a project with 2 sequences (see below)
  Media/Video/            put nvidia_facecam_master_4k.mp4 here
  Media/Video/Segments/   put nvs01_4k.mp4 … nvs23_4k.mp4 here
  Media/Audio/            VO.wav (your edited voice, untouched — cuts only, no EQ/compression/gain; digital silence
                            after the last word up to 40:02.0)
                          Music_bed.wav, SFX.wav, Ambience.wav (the stems)
                          Final_mix_reference.m4a (the delivered mix = VO + Music + SFX + Ambience at 0 dB)
  Media/Raw/              (optional, only for sequence 2) your original "part 1.mp4", "part 2.wav", "part 3.mp4"
  Assets/                 every photo, footage clip, logo, document, map, texture and font used in the edit,
                          with SOURCES.md files (credits/licences) in each folder
  Source/                 the HyperFrames compositions (HTML/GSAP) the graphics were built from, edit notes per segment,
                          EDL, transcript, palette, sound plan + music cue sheet (Epidemic Sound track list), research

IMPORT INTO PREMIERE PRO
  1. Unzip. Move nvidia_facecam_master_4k.mp4 into NVIDIA_Premiere/Media/Video/ and the 23 nvsNN_4k.mp4 files into
     NVIDIA_Premiere/Media/Video/Segments/. (Optional) copy your raw takes into NVIDIA_Premiere/Media/Raw/.
  2. Premiere Pro > File > Import… > choose NVIDIA_Premiere.xml.
  3. Premiere shows the media as offline the first time (the XML points at /NVIDIA_Premiere/Media/…).
     In the Link Media dialog click "Locate", browse to any one file inside YOUR NVIDIA_Premiere/Media folder,
     keep "Relink others automatically" ticked, OK — every other clip relinks. (If a few stay offline, locate one
     of them once more — e.g. one file in Segments/.)
  4. Open the sequences in the imported bin.

SEQUENCE 1 — "NVIDIA — final edit (4K)"  3840x2160, 24 fps, 40:02.0 (57,648 frames)
  V2  the finished 4K edit: the 23 segment files cut into 331 clips — one per scene, named "segment scene · words";
      a sequence marker at every scene start with the narration line in its comment. The clips play the segments
      back to back exactly as delivered. Trim/replace/re-order scenes freely.
  V1  clean 4K face cam aligned to the edit (disabled; black during part 2, which was audio-only). Enable it to
      re-frame or replace face-cam shots — it is native 4K, scale 100%.
  A1/A2 VO L/R · A3/A4 Music bed · A5/A6 SFX · A7/A8 Ambience — at 0 dB they sum to the delivered mix
      (−29.8 LUFS integrated, VO at unity, music ≥ 20 LU under the voice). Rebalance per scene if you like.

SEQUENCE 2 — "NVIDIA — dialogue edit on raw takes (129 cuts)"  3840x2160, 60 fps, 40:00.6
  Your dialogue edit (retakes, ums, pauses removed) as 129 clips on the original files part 1 → part 2 → part 3,
  frame-exact. Part 2 is audio only (no picture on V1 there). Use it to change any cut — the in/out of every clip is
  the cut point in the raw file.

WHAT DOES NOT TRANSFER (and why)
  The animated graphics (maps, charts, 2.5D, text, transitions) were built in code (HyperFrames: HTML + GSAP) and
  rendered — Premiere can't rebuild them as native layers, so they come in as the rendered 4K clips on V2. Their sources
  (photos, footage, maps, fonts) are all in Assets/ and the code is in Source/ if you want to rebuild a scene by hand.
  Epidemic Sound music is pre-mixed into Music_bed.wav; the tracks are listed in Source/project/SOUND_PLAN.md and
  music_cuesheet.json (licensed to your Epidemic subscription — re-download them from Epidemic if you want stems).

Fonts: Cooper Hewitt (OFL), Haskoy, Crimson Pro (OFL) — install from Assets/fonts if you add text in Premiere.
