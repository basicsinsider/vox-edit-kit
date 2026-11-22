# FIX 1 — intro sound wishes (Agent A → sound designer), 2026-11-22
Sanket #7: "intro packaging doesn't seem good, music isn't good either, intro seems slow." Sam #1: start on the clip AND its sound.
Times: **cts00 = pre-roll** (its own seconds 0–4.5 = v2 0–4.5); everything else = **v1 master seconds** (v2 = 4.5 + map(v1), Agent V's
`fix1_ops.json`). Music limits of MANUAL §0 stay binding (≥ 20 LU under the VO while he speaks, never closer than 18 LU).

## 1. Cold open (cts00, pre-roll 0–4.5 s = 108 frames) — NO music
- Only the clip's own sound: `assets/cartels/footage/cold_open_audio.wav` (48 kHz stereo, exactly 4.5 s, untouched: −13.1 LUFS-I, peak −0.8).
  Treat it as an **insert** (its audio is the foreground; no SFX/ambience on top). Balance it so it hits hard but sits ~at the VO's level
  (Paraguay put its X-clip crowd −17 LU under the VO as a bed; here it is the foreground, so nearer the VO — your call by ear).
- Moments in it: crowd yelling from frame 0 · a cluster of sharp shots ≈ 1.2–2.0 s (fans jump the seats) · loudest yell ≈ 3.4–3.6 s ·
  phone swing 4.25–4.5 s. A soft `whoosh` on the phone push at 4.10 → hard cut.
- **The handover**: the crowd should not stop dead at 4.5 — tail it 0.3–0.6 s under the VO's first words (or cross into the
  `stadium_walla` at cts01 0.0), then the music enters (below).

## 2. Where the music builds and drops (cts01 + cts02)
| v1 time | moment | wish |
|---|---|---|
| 0.0–0.6 | VO starts "That's a baseball game…" over the broadcast monitor | music IN here, low pulse (dark, tense, percussive — not the old bed). Crowd tail under it. |
| 14.8–30.3 | gunfight → helicopters → burning trucks | build 1: pulse + low drones, rising intensity (still under the VO limits) |
| 32.0–36.18 | "had come for **one man**" (target brackets snap 35.30) | pull the music DOWN to almost nothing (air swell) → **hit on 36.18 "El Chapo Isidro"** (boom + music back in, stronger) |
| 36.18–44.2 | EL CHAPO / ISIDRO slams 36.50, 37.14 (stamp thuds) | groove locks in |
| 44.2–57.86 | target file, FBI poster insert 51.46–53.70, WANTED 56.74 | steady, ticking; small accent on WANTED |
| 57.86–61.7 | "the Mexican army **had him**" (CAPTURED 60.41) | accent on CAPTURED, then thin out |
| 61.7–68.17 | "…with help from **the United States**" (steel underline 66.81) | a suspended chord / riser that lands on 66.87 "United States" — the hook of the cold open |
| 68.17–75.6 | "if this was a one-time thing… **this has happened before**" (punch 71.93, whip 73.85) | new section: investigative, rhythmic, a notch faster |
| 75.6–108.75 | pattern montage: El Mencho (KILLED 80.41, Tapalpa 80.90–82.62), CIA lab, 70+ boats, Maduro | **build 2** — layers added at each case: 80.41, 85.38, 92.03, 98.33; keep the cuts on the beat if you can |
| 108.75–112.6 | board, threads to the US seal, "What is going on?" ("?" 111.53) | keep building, tension high |
| 112.6–113.25 | **trailer strobe** (2-frame flashes) "Is this a war…" | riser ending exactly on 113.29 |
| 113.29 | **TITLE "US vs CARTELS"** — US slap 113.29, vs + CARTELS 113.85 | the BIG HIT of the intro (boom + full music) |
| 116.01 | "is this actually **working?**" — title punch + flash | second hit, then |
| 116.55–117.05 | push-through into black | **DROP**: music cuts out (or a reverse-cymbal suck) on the black bar 117.05 |
| 117.05–117.5 | "To answer that…" tarmac photo out of black | near-silence, then a NEW, calmer storytelling bed (Act 1 starts) by ~118 |

Avoid the old intro bed (Sanket: "music isn't good"). Prefer a modern documentary trailer palette: low synth pulse + taiko/percussive hits
+ a riser into the title; no marimba until Act 1 if it feels too light here.
