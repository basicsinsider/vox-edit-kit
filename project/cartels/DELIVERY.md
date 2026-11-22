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
