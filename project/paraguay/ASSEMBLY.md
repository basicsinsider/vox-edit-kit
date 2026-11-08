# Assembly notes (lead)
- Segment boundaries are not on the 24 fps master grid (e.g. 213.60 = frame 5126.4). Pieces are rendered from their own 0, so
  concatenating rounded pieces drifts the picture up to −1.4 frames (pys09/pys10) against the VO. At assembly: read each piece's
  real frame count (ffprobe -count_packets), compute where its first frame lands vs round(SEG_START*24), and add/drop one frame at
  that boundary (tpad=start=1 clone / trim) so every piece starts on the nearest master frame (|error| ≤ 0.5 frame). Then run the
  face-cam lip-sync correlation on the assembled picture (MANUAL 2026-11-08) — target same lag as the raw (+2 by that method).
- Bleeps: tools/final_mix_paraguay.sh mutes 1104.58+0.32, 1159.43+0.16, 1600.60+0.24 (sound designer's bleep tones in sfx.wav).
- First full render = 1080p pieces → review/py_720p.mp4 (Krish approves) → only then RES=4k pieces (MANUAL §11.1, Ivan v3).
