# cts00 — COLD OPEN PRE-ROLL (fix round 1, Sam #1) — P = 4.5 s = 108 frames @ 24 fps, before the VO
Composition id `cts00`, `data-vo-start="0"`, `data-duration="4.5"`. It plays BEFORE cts01 (v2 = 4.5 + map(v1)); no VO, no text cues.

## Built
| id | local | picture | effect |
|---|---|---|---|
| sc001 | 0.000–4.500 | the real Kuroda Park fan video (Luis Cárdenas, video 1) — fans at the rail duck, jump the seats, crouch — in a phone frame (rounded, bone hairline) on a blurred, darkened fill of the same clip; slow push + drift; CT.dateTag GUASAVE, SINALOA · 20 NOV 2026 at 0.35; CT.credit "Video: Luis Cárdenas (X)" | hard open on the panic; at 4.10 the phone pushes hard (1.07 → 1.32, blur 6 px) while the phone camera itself swings away (source 4.25–4.6) → hard cut on action into cts01's broadcast monitor, which starts mid-push (scale 1.12) |

- Video: `assets/cartels/cts00/cold_open_fans.mp4` (source 0.0–5.5, 24 fps, no audio). Sound: `assets/cartels/footage/cold_open_audio.wav`
  (same in-point 0.0, exactly 216000 samples @ 48 kHz = 4.5 s, natural level −13.1 LUFS-I / peak −0.8, no gain or fades). The
  `<audio class="temp-vo">` in the file is preview only (build_master strips temp-vo tags; the sound designer places the WAV).
- Why this clip/window: the most gripping real sound of all fetched originals (LC fan video 1 = the first-hand 576×768 original; K911's
  repost of the same video is 352×624 and louder-normalised; the LMP broadcast audio is commentary at −28 dB; AJE has its own music).
  0.0–4.5 holds the whole panic: yelling from frame 0, a cluster of shots ≈1.2–2.0 s, the loudest yell ≈3.5 s; at 4.25 the camera swings.
- Checks: lint 0 errors (1 warning: fill + sharp copy of the same video); sync_audit 0 cues (no text); headless timeline dump
  `tl.duration() = 4.500`, seek 0→4.5 no errors; snapshots 0.02/0.6/1.6/2.6/3.6/4.2/4.45 looked at + the cut into cts01 0.0/0.042.
- sfx: `cts00.sfx.json` — t = cts00-local seconds (= v2). Entries flagged `"in_clip": true` are REFERENCE markers of what is already in the
  clip audio (treat 0–4.5 as an insert window so place_sound drops them); real SFX = tick_soft 0.35 (date tag), whoosh 4.10 (push/cut).
