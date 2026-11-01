#!/usr/bin/env python3
"""Writes project/ivan/music_cuesheet.json (the sound designer's cue sheet for "Ivan", master seconds 0–949.0).
Edit the tables here and re-run (python3 project/ivan/gen/make_cuesheet.py), then rebuild the beds (SOUND_PLAN.md §6).
offset = read position inside the Epidemic file at the layer's start, chosen so the track's own builds/peaks
(assets/audio/epidemic/ANALYSIS.md) land on the story beats named in the notes."""
import json, os

def L(cue, track, stem, start, end, offset, rel, fi=1.5, fo=1.5, auto=None, note="", file=None):
    d = dict(cue=cue, track=track, stem=stem, start=start, end=end, offset=round(offset, 3), rel_lu=rel,
             fade_in=fi, fade_out=fo)
    if auto: d["auto"] = auto
    if note: d["note"] = note
    if file: d["file"] = file
    return d

WR = "woodwind_reviere"     # D-minor drone (tempo-free glue)
layers = [
    # ---------------- M1 cold open: Ivan's double life → why → opposition → invasion (Code of Violence, D, 102 bpm)
    L("M1", WR, "bass", 0.0, 30.0, 20.0, -17.5, 3.0, 4.0, note="drone floor under the cold open"),
    L("M1", "code_of_violence", "instruments", 0.0, 108.5, 4.0, -10.5, 2.0, 0.6,
      auto=[[0, 0], [30.0, 0], [31.0, -2], [50.0, -2], [52.0, 0], [96.0, 0], [98.0, 1.5], [104.0, 1.5], [104.6, 3.0], [107.9, 3.0]],
      note="quiet intro (file 4–41) under 'Somewhere inside Russia…'; its 41–44 build lands on 'the only way…Putin' 37–40; "
           "thinned under the dense 30–50 s; the 100–118 peak carries 'full-scale invasion…February 2022' (104.25/105.21)"),
    L("M1", "code_of_violence", "bass", 13.84, 108.5, 17.84, -18, 2.0, 0.6, note="enters on 'But what most of them don't know'"),
    L("M1", "code_of_violence", "drums", 47.44, 81.0, 51.44, -20, 2.0, 1.0, note="pulse from 'Because while Russia has been fighting…'; out for the reflective 'To understand why…'"),
    L("M1", "code_of_violence", "drums", 97.85, 108.5, 101.85, -19.5, 1.5, 0.6, note="back on 'But Putin's government…' into the invasion"),
    # ---------------- insert 1 (108.7–116.7, protest chants) — drone only, ducked (see ducks); M2 protests/laws/arrests/exodus
    L("M2", WR, "bass", 100.0, 141.0, 30.0, -17, 3.0, 3.0, note="the floor through insert 1 (ducked) and the arrests/exodus"),
    L("M2", WR, "instruments", 116.4, 140.0, 40.0, -18, 1.5, 3.0, note="airy, sombre: protesters, new laws, thousands of arrests, leaving"),
    # ---------------- M3 Ivan decides → Mamoń → videos → verification → Kazakhstan/Tatarstan → satellite (Tracker, D minor, 90 bpm)
    L("M3", "tracker", "full", 131.78, 257.0, 0.0, -13, 2.5, 1.5,
      auto=[[131.78, -2], [140.0, -2], [144.0, 0], [212.5, 0], [213.0, 1.5], [215.0, 1.5], [215.6, 0], [238.0, 0], [239.0, -1.5], [256.0, -1.5]],
      note="steady sneaking pulse starts as Ivan 'started looking at things differently' and carries the investigation; "
           "small lift on 'So, that part of his story checked out' 212.91; thinner under the face-cam satellite aside"),
    # ---------------- M4 the 5-hour assignment → Foma's network → 25 years → over their shoulders → Kirillov (Estimations, D minor, 117)
    L("M4", WR, "bass", 252.0, 300.0, 60.0, -19, 3.0, 4.0, note="glue under the Tracker→Estimations join"),
    L("M4", "estimations", "instruments", 256.26, 407.6, 0.1, -14, 2.5, 0.3,
      auto=[[256.26, 1], [270.0, 1], [271.0, -1.5], [281.0, -1.5], [282.0, 0], [395.0, 0], [399.0, 1.5], [407.0, 1.5]],
      note="quiet intro (file 0–27) under 'one rather big problem…five hours'; offset puts the file's 143–173 peak exactly on "
           "'killed by a bomb' 399.16 (Kirillov)"),
    L("M4", "estimations", "bass", 266.18, 296.18, 10.02, -19, 2.0, 1.5, note="tension under the five hours / normal day / family"),
    L("M4", "estimations", "bass", 327.43, 407.6, 71.27, -19, 2.0, 0.3, note="back on 'FOMA's network was quite big'"),
    L("M4", "estimations", "drums", 383.64, 407.6, 127.48, -21, 2.0, 0.3, note="clock-like pulse from 'officers…looking over their shoulders' into Kirillov"),
    # ---------------- insert 2 (407.9–425.9, Moscow resident at the blast site) — drone only, ducked
    L("M5", WR, "bass", 404.0, 442.0, 100.0, -18, 2.0, 3.0, note="floor through insert 2"),
    # ---------------- M5 Sarvarov → Foma's people tracked him → two and two → senior officers unsettled
    L("M5", "estimations", "instruments", 425.96, 471.0, 160.0, -14, 1.0, 2.0,
      auto=[[425.96, 0], [435.0, 0], [435.8, 1.5], [438.0, 1.5], [440.0, 0], [448.0, 0], [449.0, -2], [458.0, -2], [459.0, 0]],
      note="re-enters inside its 143–173 peak: 'December 2025…Fanil Sarvarov…a bomb exploded beneath his car' 435.77; "
           "thinned under the dense 'two and two together'"),
    L("M5", "estimations", "bass", 425.96, 471.0, 160.0, -19, 1.0, 2.0),
    L("M5", "estimations", "drums", 428.2, 441.0, 162.24, -22, 1.0, 1.5, note="'December 2025' → the car bomb"),
    L("M5", WR, "instruments", 459.45, 476.0, 90.0, -20, 2.0, 2.0, note="eerie air: 'even in Moscow…someone watching'"),
    # ---------------- M6 Operation Spiderweb (Close Call, D minor, 84 bpm)
    L("M6", "close_call", "instruments", 474.57, 595.0, 18.6, -14, 1.5, 1.2,
      auto=[[474.57, -1], [496.0, -1], [497.0, 1.0], [520.0, 1.0], [521.5, 0], [559.0, 0], [560.0, -1.5], [572.0, -1.5], [573.0, 0]],
      note="offset puts the file's 36–41 build → 41–65 peak on 'On June 1st, small Ukrainian drones…' 496.96 → flames → "
           "Spider Web; its 71–97 quiet section sits under the cargo trucks + insert 3; 97–104 build → 104–134 peak on "
           "'stopped building…41 aircraft…at least 10 strategic bombers'; 134–141 drop = 'wasn't actually safe anymore'"),
    L("M6", "close_call", "bass", 474.57, 595.0, 18.6, -19, 1.5, 1.2),
    L("M6", "close_call", "drums", 496.96, 521.2, 41.0, -20, 0.4, 0.8, note="drums with the drones (June 1st → remarkable)"),
    L("M6", "close_call", "drums", 559.39, 590.11, 103.42, -20, 1.5, 1.0, note="drums back for the losses (stopped building → 41 → 10)"),
    # ---------------- M7 Ivan foresaw it → not saying he was involved → Yelabuga → Foma's theory → 'one thing he can't understand'
    L("M7", "code_of_violence", "instruments", 594.35, 675.4, 44.0, -15, 1.5, 0.4,
      auto=[[594.35, 0], [617.0, 0], [617.6, -2], [630.5, -2], [631.5, 0]],
      note="the cold-open track returns for Ivan's own mystery (rhymes with M1); its 118–123 peak lands on "
           "'one thing…still couldn't understand' 668–673; thinner under 'Now I want to be clear'"),
    L("M7", "code_of_violence", "bass", 597.71, 617.36, 47.36, -20, 2.0, 1.0),
    L("M7", "code_of_violence", "bass", 630.96, 675.4, 80.61, -20, 2.0, 0.4),
    L("M7", "code_of_violence", "drums", 636.96, 664.56, 86.61, -22, 1.5, 1.5, note="'extraordinary scale' → Yelabuga → towers → theory"),
    # ---------------- M8 how was he never caught? → double agent? → silence → car inspection → explosives (Make Way for Hearses, D, 90)
    L("M8", "make_way_for_hearses", "full", 675.59, 767.3, 13.6, -14, 0.8, 0.12,
      auto=[[675.59, 0], [726.0, 0], [727.0, -2], [735.0, -2], [736.0, 0]],
      note="offset puts its 73–79 drop on 'Ivan suddenly stopped answering his messages' 736–741, the 79–94 quiet on "
           "'weeks…months…still nothing…got back in touch', the 94–99 build on 'stopped…inspect his car'; "
           "cut dead on 'explosives' 767.38 (stinger hit)"),
    L("M8", WR, "bass", 735.0, 790.0, 120.0, -18, 3.0, 4.0, note="floor from the silence to the trains"),
    L("M8", WR, "instruments", 741.0, 756.0, 130.0, -20, 2.0, 2.0, note="the months of silence"),
    L("M8", "sfx", "heartbeat", 767.38, 775.0, 2.0, -23, 0.3, 2.0, file="sfx/heartbeat_cinematic_54bpm.wav",
      note="low heartbeat under 'explosives in his car…without the officers finding anything'"),
    L("M8", WR, "instruments", 767.38, 784.0, 150.0, -20, 1.0, 3.0, note="'the fear of getting caught never really went away'"),
    # ---------------- M9 trains / Freedom of Russia / 300–500 / tiny fraction / the flip side (Tracker reprise)
    L("M9", "tracker", "full", 781.2, 860.0, 20.0, -16, 2.0, 3.0,
      auto=[[781.2, 0], [826.0, 0], [827.0, -2.5], [841.0, -2.5], [841.6, 0.5], [850.0, 0.5], [851.0, 0]],
      note="sabotage pulse returns for the railway saboteurs; thinner on 'tiny fraction…not close to overthrowing Putin'; "
           "lift on 'But the flip side' 841.59"),
    # ---------------- M10 reflective ending (Letters Never Sent, F major / D minor, 80 bpm)
    L("M10", WR, "bass", 850.0, 949.0, 100.0, -20.5, 4.0, 2.0, note="drone floor to the end"),
    L("M10", "letters_never_sent", "instruments", 858.23, 949.0, 93.2, -17.5, 3.0, 2.0,
      auto=[[858.23, 0], [872.0, 0], [873.0, -2], [905.0, -2], [906.0, 0]],
      note="offset puts its 101–113 peak on 'Russians themselves' 865.66–869, its 164–168 dip under 'Putin won't live "
           "forever' 928.49, and the 168–175 build → 175–183 peak on the last line 'willing to risk everything…never get "
           "to see' 940.2–946.8; hold 1.5 s past the last word, fade to the end"),
    L("M10", "letters_never_sent", "bass", 865.66, 949.0, 100.63, -22.5, 2.0, 2.0),
    L("M10", WR, "instruments", 919.13, 949.0, 160.0, -21, 3.0, 2.0, note="air from 'Ivan certainly doesn't know'"),
]

stingers = [
    dict(file="boom_cinematic_deep", t=104.25, sync="loudest", rel_lu=-24, note="'full-scale invasion' (Feb 2022)"),
    dict(file="boom_dark_cinematic_low_hit", t=399.16, sync="loudest", rel_lu=-21, note="Kirillov 'killed by a bomb'"),
    dict(file="boom_sub_bass_clean_01", t=435.77, sync="loudest", rel_lu=-25, note="Sarvarov 'a bomb exploded beneath his car'"),
    dict(file="riser_reverse_cymbal_short", t=496.96, sync="loudest", rel_lu=-27, note="into 'On June 1st, small Ukrainian drones'"),
    dict(file="boom_cinematic_deep", t=705.99, sync="loudest", rel_lu=-27, note="'…working for Russian intelligence, too?'"),
    dict(file="boom_dark_cinematic_low_hit", t=767.38, sync="loudest", rel_lu=-21, note="'explosives in his car' (music cut)"),
]

ducks = [   # insert clips: music near-silent under their own audio; SFX/ambience muted (sfx_db)
    dict(start=108.7, end=116.7, db=-16, ramp=0.5, sfx_db=-60, note="insert 1: protest chants"),
    dict(start=407.9, end=425.9, db=-16, ramp=0.5, sfx_db=-60, note="insert 2: Moscow resident at the Kirillov blast site"),
    dict(start=532.917, end=543.917, db=-16, ramp=0.25, sfx_db=-60, note="insert 3: SBU FPV drone footage (VO 'airfields.' ends 532.64)"),
]

sheet = dict(length=949.0, bed_lu_under_vo=14.0,
             doc="Layered Epidemic bed for 'Ivan' (Searching Lessons). Master seconds of vo_iv.mp3. Generated by "
                 "project/ivan/gen/make_cuesheet.py — edit there. Key family D minor / F major. Acts = SEGMENTS.md §3. "
                 "'ducks' = the three insert clips (place_sound.py: music −16 dB, SFX/ambience muted, no pause lifts).",
             layers=layers, stingers=stingers, ducks=ducks)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "music_cuesheet.json")
json.dump(sheet, open(out, "w"), indent=1)
print("wrote", os.path.normpath(out), len(layers), "layers")
