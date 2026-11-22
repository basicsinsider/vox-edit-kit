# US vs Cartels — deliveries

## 720p review — 2026-11-22 07:15 UTC
- **https://gofile.io/d/ZRjFouUu** — `US_vs_Cartels_720p.mp4`, 1,068,994,479 bytes, 22:21.917 (32,206 frames @ 24 fps), 1280×720 H.264 + AAC 320k 48 kHz.
- md5 `47591669bd796e672a1720b8fce8f4fb` — local md5 == gofile's md5 (MATCH).
- Picture: 14 segments rendered at 1080p on 14 Sonnet helper sessions (`render/cts01…cts14`, 720p pieces via `SCALE=720`), SHA-256 verified,
  joined frame-exact on the 24 fps grid (`tools/assemble_cartels.py`; checked: every segment start lands on its master frame, offset 0;
  blackdetect: no black frames).
- VO: raw 24:46 → 22:22 by EDL (cuts only, `project/cartels/EDL.json`); never processed.
- Sound (`project/cartels/SOUND_REPORT.md`): VO alone −32.1 LUFS-I = final mix −32.1 LUFS-I (Δ 0.00 LU), VO true peak −4.3 dBTP.
  `vo_music_scan.py`: ALL LIMITS MET — music vs voice while he speaks, 3 s windows: min 19.0 LU (≥ 18), 5th pct 20.9 (≥ 20), median 23.9;
  0.4 s 1st pct 18.3; music+SFX min 15.0 (≥ 14). Acts −23.3…−26.3 LU re VO (whole bed −25.2; the cliff −30.1 on purpose).

## 720p v2 + 4K Premiere Pro package — 2026-11-22 17:40 UTC (Krish: "the premiere pro file needs to be 4k")
- Folder **https://gofile.io/d/7At2HNxJ** (guest folder; token only in gitignored `work/`).
- `US_vs_Cartels_Premiere.zip` 1,562,748,026 bytes, md5 `b928d0f133610e85b718f30ecd7865e7` — local == gofile (MATCH). XML (3840x2160 24p,
  32,206 frames, 180 scene clips + markers on the 14 ctsNN_4k.mp4 files, VO/Music/SFX/Ambience L/R; seq 2 = raw-take EDL, 86 pieces),
  stems (VO.wav = the edited VO, 32-bit float, L = R = original samples, verified bit-identical), raw VO, Assets, Source, README.
  Checked before upload: XML parses; 5 of 19 media paths are in the zip, the other 14 are exactly the 4K segment files.
- `US_vs_Cartels_720p_v2.mp4` 1,068,864,122 bytes, md5 `8519ce52327c3fbe6ae368cce8a70f4d` (MATCH) — replaces the first 720p, whose mix
  had the VO 3 dB low per channel (ffmpeg's default mono→stereo up-mix). v2: VO alone −29.1 LUFS-I = mix −29.1; music limits re-run:
  3 s min 22.0 LU, p5 24.0, median 26.9, 0.4 s p1 21.3, music+SFX min 18.0 — ALL LIMITS MET.
- 4K segments: 14 Sonnet helpers (`render4k/ctsNN`, `project/cartels/HELPER4K_PROMPT.md`) render `RES=4k` and upload ctsNN_4k.mp4 into the
  same folder (md5-checked by each helper).
