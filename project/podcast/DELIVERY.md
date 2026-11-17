# Podcast "TSMC vs UMC" — deliveries
- 2026-11-13 · **720p review**: https://gofile.io/d/B2ocpaJN — `TSMC_vs_UMC_podcast_720p_review.mp4` · 1280×720 h264 30 fps · AAC 320k ·
  5752.03 s (95:52) · 172,561 frames · 1,257,918,922 B · md5 3d9104f3abbea44937be2efc647597f8 (= gofile)
  · A-roll cut by EDL (98:20 → 95:52, 226 word cuts + pause trims, punch-ins at every join); intro 0–5:46 fully edited (pd01–03);
    41 edited sections after it (pd04–pd44, 26.6 min); 44 pieces rendered on 10 cloud helpers, assembled frame-exact.
  · Sound (39 islands, all ALL LIMITS MET, `SOUND_REPORT.md`): music 3 s gap under the voice min 19.5 / p5 20.8 / median 22.6 LU;
    0.4 s p1 18.6 LU; music+SFX min 16.1 LU; no music between islands. Voice unchanged: review −18.2 LUFS-I = voice alone −18.2
    (also equal on 60 s windows at 0, 2700, 5690 s).
- 2026-11-17 · **Premiere Pro package** (Krish asked, same as Paraguay): https://gofile.io/d/eMChCD0C — one gofile folder, two zips
  that unzip into one `TSMC_vs_UMC_Premiere/` folder: `TSMC_vs_UMC_Premiere_1of2.zip` (XML, README, voice, 39×3 island stems,
  final-mix reference, 240 assets + SOURCES, source) 2,415,776,136 B md5 428b800a69904580aa7efd3f45439a11 (= gofile) ·
  `TSMC_vs_UMC_Premiere_2of2.zip` (Media/Sections pd01–pd44, 1080p30) 3,205,139,221 B md5 bc60e23f2a750372a5369f82d5733376 (= gofile).
  XML by `tools/premiere_xml_podcast.py` (copy + README in `project/podcast/premiere/`): seq 1 final edit 1080p30 (V1 = raw take cut
  by the 229 EDL pieces with the punch-ins as scale, V2 = 44 sections, A1/A2 voice, A3–A8 island music/SFX/ambience), seq 2 dialogue
  edit on the raw take (4K). Krish supplies podcast.mp4 into Media/Raw/. Island stems rebuilt with --keep-wav (premix md5 identical).
