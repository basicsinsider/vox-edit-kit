# NVIDIA — "Is the chip ban actually working?" — deliveries

## 720p review — 2026-11-17 07:00 UTC
- **https://gofile.io/d/RHNc6bOu** — `NVIDIA_chip_ban_720p_review.mp4`, 965,864,901 bytes, 40:02.000 (57,648 frames @ 24 fps), 1280×720 H.264 CRF 20 + AAC 320k 48 kHz stereo.
- md5 `b036c115fb8b53e2661d21a11b005e24` — local md5 == gofile's md5 (MATCH).
- Picture: 23 segments rendered at 1080p on 23 Sonnet helper sessions (`render/nvs01…nvs23`, ≈ 5 min each), every piece SHA-256-verified, joined
  frame-exact on the 24 fps master grid by `tools/assemble_nvidia_lowdisk.py` (lead-side; the assembly helper hit the account's usage limit).
- Sound (`project/nvidia/SOUND_REPORT.md`): VO untouched at unity — VO alone −29.8 LUFS-I = final mix −29.8 LUFS-I, true peak −4.8 dBFS.
  `vo_music_scan.py` (re-run by the lead): ALL LIMITS MET — music vs voice while he speaks, 3 s windows: min 18.2 LU (limit ≥ 18), 5th pct 20.8 LU
  (≥ 20), median 23.2 LU; 0.4 s 1st pct 18.4 LU; pauses min 30.6 LU; music+SFX min 15.0 LU (≥ 14). Per act (N1–N21): −23.7…−25.1 LU re VO.
- 4K: after Krish approves → `RES=4k PRESET=fast tools/render_piece.sh nv 2402 <seg>` on helpers (MANUAL §11.1, Paraguay 4K notes).
