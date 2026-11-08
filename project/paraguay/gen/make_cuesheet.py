#!/usr/bin/env python3
"""Writes project/paraguay/music_cuesheet.json (the sound designer's cue sheet for "Paraguay", master seconds 0–1621.87).
Edit the tables here and re-run (python3 project/paraguay/gen/make_cuesheet.py), then rebuild the beds (SOUND_PLAN.md §6).
offset = read position inside the Epidemic file at the layer's start, chosen so the track's own builds/peaks/drops
(assets/audio/epidemic/ANALYSIS.md, profiles quoted in SOUND_PLAN.md §1) land on the story beats named in the notes.
Key family: E minor / G major (+ B minor neighbour). Glue drone: And Then (DEX 1200), bass + instruments only (its drums pulse).
Same format as project/ivan/music_cuesheet.json; adds "bleeps" (place_sound.py places a 1 kHz bleep over each muted word)."""
import json, os

# per-act balance trims (dB on every layer of the act), from the act-level check (SOUND_PLAN §5): aim −12…−17 LU re the VO
TRIM = {"P1": +2.0, "P3": -0.5, "P4": -1.7, "P7": -2.0, "P8": +2.5, "P9": +1.0, "P12": -1.2, "P13": -1.5}


def L(cue, track, stem, start, end, offset, rel, fi=1.5, fo=1.5, auto=None, note="", file=None):
    rel = round(rel + TRIM.get(cue, 0.0), 2)
    d = dict(cue=cue, track=track, stem=stem, start=start, end=end, offset=round(offset, 3), rel_lu=rel,
             fade_in=fi, fade_out=fo)
    if auto: d["auto"] = auto
    if note: d["note"] = note
    if file: d["file"] = file
    return d

LEN = 1621.87
DR = "and_then"       # E-minor drone (tempo-free glue: bass pulse 1.1, instruments 1.6 — measured; its drums stem is NOT used)
XCLIP = "../../paraguay/shared/footage/x_congress_audio.wav"   # relative to assets/audio/epidemic (epidemic_bed joins EPI + file)
XCLIP_MEDIA_START = 3.0   # = the X clip's media start in pys01 sc001 (EDIT_NOTES_pys01: media 3.0–9.45 over 0–6.45); re-check in pys01.html

layers = [
    # ================= P1 cold open (pys01, 0–116.3): the X clip, protests, the president → one bank → 60 % → pensions
    L("P1", "xclip", "crowd", 0.0, 6.6, XCLIP_MEDIA_START, -17, 0.05, 1.6, file=XCLIP,
      note="the X clip's own crowd under 'That's a congressman in Paraguay getting dragged out by protesters' (0.24–4.6); "
           "never over the VO (−17 LU re VO); out with the clip"),
    L("P1", "sfx", "chant", 3.5, 13.0, 10.0, -27, 1.5, 3.0, file="sfx/protest_distant_chanting_walla.wav",
      note="distant chanting carries 'protests are spreading all across the country' (5.76) after the clip, gone by 'the president' 9.1"),
    L("P1", "starfall", "instruments", 0.0, 27.2, 14.2, -13, 1.0, 1.0,
      note="weight from frame 1 (file 14–41 steady); offset puts the file's melody return (33 s) on 'it all started with one bank' 18.80"),
    L("P1", "starfall", "melody", 0.0, 27.2, 14.2, -17.5, 1.0, 1.0),
    L("P1", "starfall", "drums", 4.6, 26.8, 18.8, -20, 1.5, 1.0, note="urgency from 'protests are spreading' → 'one bank. This bank. Ueno'"),
    L("P1", DR, "instruments", 14.0, 40.0, 60.0, -19, 3.0, 4.0, note="glue under the Starfall → DOX join (26.4)"),
    L("P1", "dox", "full", 26.0, 116.4, 113.0, -15, 1.2, 0.4,
      auto=[[26.0, 0], [38.0, 0], [39.0, -2], [50.0, -2], [51.0, 0], [77.0, 0], [78.0, -2], [92.0, -2], [93.0, 0],
            [104.5, 0], [116.4, 0]],   # (the +1.5 lift into "how we got here" removed: Krish 2026-11-08)
      note="the money pulse under the numbers ('how big it was. Around 60%' 26.4/27.68 → Chase 10% → 60% market share); "
           "its 139–155 drop/silence lands on 'Now imagine…all collapsing in one day' 52.0 → 'that's kinda like…Paraguay' 58.8 → 68; "
           "back at 73, its 168–173 build on 'FDIC…97%' 80.7–84.9; lift on 'So now the big question' 105.03 into 'how we got here' 116.3"),
    L("P1", DR, "bass", 48.0, 76.0, 100.0, -18, 3.0, 3.0, note="the floor while DOX drops out ('imagine…one day')"),
    L("P1", DR, "instruments", 52.0, 72.0, 120.0, -18.5, 2.0, 3.0),
    L("P1", DR, "bass", 100.0, 128.0, 150.0, -19, 3.0, 4.0, note="glue into P2"),
    # ================= P2 (pys02, 116.3–213.6): World Cup, the tweet (wry) → a boring success story → 'one bad news'
    L("P2", "in_disguise", "instruments", 116.6, 156.0, 5.0, -16, 1.0, 1.5,
      note="wry, sneaky pizzicato colour (E minor) for 'I don't know about you…World Cup…this tweet…not gonna read it…skin color'; "
           "out on 'But that's not the case' 154.9"),
    L("P2", "in_disguise", "bass", 116.6, 156.0, 5.0, -22, 1.0, 1.5),
    L("P2", "in_disguise", "melody", 127.0, 150.0, 15.4, -20, 1.0, 1.5, note="the tweet bit only (127.26 → 147.3)"),
    L("P2", DR, "instruments", 150.0, 170.0, 160.0, -19, 2.0, 3.0, note="glue under the In Disguise → Andean Valley join"),
    L("P2", "andean_valley", "instruments", 157.5, 206.0, 18.0, -15, 2.0, 0.4,
      note="Latin-American acoustic colour: 'Paraguay is actually a success story, a boring one…especially in South America' 159.3; "
           "investment grade 166.5, Wall Street 184.8, strongest growth 197.4; out on 'one bad news' 205.6"),
    L("P2", "andean_valley", "drums", 162.5, 206.0, 23.0, -21, 2.0, 0.4),
    L("P2", "andean_valley", "bass", 184.5, 206.0, 45.0, -21, 1.0, 0.4, note="its bass enters (file 45) on '$350 million…Wall Street' 184.79"),
    L("P2", DR, "bass", 200.0, 226.0, 180.0, -18, 3.0, 4.0, note="under the turn 'one bad news' → 'background on this bank'"),
    # ================= P3 (pys03, 213.6–332.6): background — the 1950 joke, loan sharking, 2015 heir, the conglomerate
    L("P3", "we_picked_irises", "instruments", 213.8, 333.0, 37.8, -17, 1.5, 2.5,
      auto=[[213.8, 0], [228.0, 0], [229.0, -1.5], [244.0, -1.5], [245.0, 0], [283.0, 0], [284.0, -1.5], [305.0, -1.5], [306.0, 0]],
      note="G-major contemporary-classical (hopeful, a bit cheeky): its 40–45 swell under 'born in 1950. I'm just kidding' 217.9–220; "
           "75 s dip on 'Credit Central…not a bank' 246–252; drums enter (file 88) on 'in 2015, the leadership changes' 263.7; "
           "110–135 peak = 'national conglomerate…diversify'; 145 dip → 'where the problem starts' 331.5"),
    L("P3", "we_picked_irises", "melody", 213.8, 333.0, 37.8, -18.5, 1.5, 2.5),
    L("P3", "we_picked_irises", "bass", 213.8, 333.0, 37.8, -22, 1.5, 2.5),
    L("P3", "we_picked_irises", "drums", 264.0, 333.0, 88.2, -24, 1.0, 2.5, note="(stem −28.9 LUFS file-wide: quiet by nature)"),
    L("P3", DR, "instruments", 324.0, 346.0, 200.0, -19, 3.0, 3.0, note="glue into P4 ('by 2020, around COVID')"),
    # ================= P4 (pys04, 332.6–457.4): COVID → the merger → Ueno, a fintech → the boom → 50 % promos → 'four times bigger'
    L("P4", "i_can_see_the_world", "instruments", 333.4, 448.9, 30.0, -15, 2.0, 0.2,
      auto=[[333.4, 0], [396.5, 0], [398.4, -3], [448.9, -3]],   # its 95–145 peak was the 7:20 complaint (Krish 2026-11-08)
      note="E-minor/G acoustic (charango-like plucks, restless): low under COVID / 2021 merge; drums (file 40) on 'in 2021, he merges' "
           "344.7; its 90 s breath at 393.4 between '50% discount' and the limits joke; 95–145 peak = 'nonetheless…huge hit' 398.1 → "
           "groceries → low income → first accounts; ends dead on 'buying a bank that's four times bigger' 448.75"),
    L("P4", "i_can_see_the_world", "melody", 333.4, 448.9, 30.0, -16.5, 2.0, 0.2, auto=[[333.4, 0], [396.5, 0], [398.4, -3], [448.9, -3]]),
    L("P4", "i_can_see_the_world", "drums", 343.4, 448.9, 40.0, -21, 1.0, 0.2),
    L("P4", "i_can_see_the_world", "bass", 398.4, 448.9, 95.0, -22.5, 0.5, 0.2),
    L("P4", DR, "bass", 440.0, 470.0, 210.0, -18, 2.0, 3.0, note="near-silence for 'how the hell do you buy something four times bigger' 454.4 (face cam joke)"),
    L("P4", DR, "instruments", 447.0, 462.0, 220.0, -19, 1.0, 2.0),
    # ================= P5 (pys05, 457.4–595.6): the secret weapon — political capital (Neon Noir, investigative pulse)
    L("P5", "neon_noir", "instruments", 457.6, 595.8, 14.6, -15, 1.5, 1.2,
      auto=[[457.6, 0], [472.0, 0], [474.0, -3], [509.0, -3], [511.0, 0]],   # its 35–50 peak (instruments +4…+7 LU) pulled down
      note="its 35–50 peak on 'then finance minister…who goes on to become the president…2023' 478.7–482.6; its 80 s accent on "
           "'the next day he becomes part of the central bank' 524.3; melody out (95–145) under the acquisition going wrong; "
           "150 dip = 'bigger and in a worse position' ~593"),
    L("P5", "neon_noir", "drums", 457.6, 595.8, 14.6, -21, 1.5, 1.2),
    L("P5", "neon_noir", "melody", 457.6, 540.0, 14.6, -19.5, 1.5, 2.0),
    L("P5", "neon_noir", "bass", 473.0, 595.8, 30.0, -20, 1.5, 1.2, note="bass from file 30 ('one of those investors')"),
    L("P5", DR, "bass", 585.0, 612.0, 230.0, -18, 2.0, 3.0, note="glue under the Neon Noir → In Disguise join"),
    # ================= P6 (pys06, 595.6–706.2): 'Luckily for Ueno' → government deposits → IPS → the law gets changed (sly)
    L("P6", "in_disguise", "instruments", 596.0, 706.4, 0.0, -17, 1.5, 1.0,
      auto=[[596.0, 0], [632.0, 0], [633.0, -2], [649.0, -2], [650.3, 0.5], [660.0, 0.5], [661.0, 0], [685.0, 0], [686.0, -1.5], [706.4, -1.5]],
      note="the sneaky colour of the tweet returns (rhyme: the narrator's irony) on 'Luckily for Ueno, though' 595.84; thinner under the "
           "pension-law explanation, small lift on 'Well, guess what? That law gets changed' 649.6–650.6 (stinger); thinner again "
           "under 'raising eyebrows…protests…looks sketchy'; the file's own 104–110 drop = the act's end"),
    L("P6", "in_disguise", "bass", 596.0, 706.4, 0.0, -22.5, 1.5, 1.0),
    L("P6", DR, "instruments", 690.0, 722.0, 240.0, -19, 3.0, 4.0, note="glue into P7 ('with the benefit of hindsight')"),
    # ================= P7 (pys07, 706.2–798.0): hindsight → conflict → capital ratio → 0.58 % → 'too good to be true…It was.'
    L("P7", "desert_whispers", "instruments", 706.2, 797.35, 23.9, -14.5, 1.5, 0.12,
      auto=[[706.2, 0], [753.0, 0], [754.0, -1.5], [772.0, -1.5], [773.0, 0], [786.0, 0], [796.0, 1.5], [797.35, 1.5]],
      note="dark nylon-guitar tension; bass (file 35) on 'March 2025' ~717, drums (file 45) on '…sells his stake' 727 → "
           "'conflict of interest' 730.2; offset puts its 110–115 crest on 'too good to be true. And guess what?' and the "
           "music is CUT DEAD on 'It was.' 797.27 (stinger)"),
    L("P7", "desert_whispers", "melody", 706.2, 797.35, 23.9, -16.5, 1.5, 0.12),
    L("P7", "desert_whispers", "bass", 717.3, 797.35, 35.0, -20, 1.5, 0.12),
    L("P7", "desert_whispers", "drums", 727.3, 797.35, 45.0, -20.5, 1.0, 0.12),
    L("P7", DR, "bass", 798.2, 832.0, 250.0, -18, 2.0, 4.0, note="after the cut: the floor for 'this is where we come back to the beginning'"),
    # ================= P8 (pys08, 798.0–940.6): back to the conglomerate → self-dealing 20 % → owe a billion → shell companies
    L("P8", "fake_photisms", "full", 812.0, 932.0, 0.0, -16, 3.0, 3.0,
      auto=[[812.0, 0], [876.0, 0], [877.0, -1.5], [884.0, -1.5], [885.0, 0]],
      note="E-minor mystery (full mix: its stems are ~10 LU under it); 30 s entry of bass/melody on 'this is not illegal…' ~838–842; "
           "a breath under the 'owe a million / owe a billion' joke 878–883; 90–105 return on 'shell companies…created today' 905–916"),
    L("P8", DR, "instruments", 924.0, 952.0, 260.0, -19, 3.0, 3.0, note="glue into P9"),
    # ================= P9 (pys09, 940.6–1042.6): 60 days → creative accounting (joke) → over and over → $300 M → merry-go-round
    L("P9", "dox", "full", 940.6, 1042.5, 37.3, -16, 2.0, 0.3,
      auto=[[940.6, 0], [974.0, 0], [975.5, -3], [991.0, -3], [992.5, 0]],
      note="the money pulse of the cold open returns for the scheme itself (rhyme: the machine); recedes under the accounting-teacher "
           "joke 975–992; its own 139 s drop lands on 'Merry go around' 1041.6–1042.3"),
    L("P9", "sfx", "music_box", 1030.0, 1044.5, 5.0, -31, 2.5, 1.5, file="sfx/music_box_antique_melody.wav",
      note="the carousel hint (very subtle) under '$300 million…merry-go-round'"),
    L("P9", DR, "bass", 1034.0, 1085.0, 270.0, -18, 3.0, 4.0, note="floor while Crossing the Border starts from nothing"),
    # ================= P10–P11 (pys10–11, 1042.6–1294.5): the central bank catches on → the buyer → the report buried → ABC Color
    L("P10", "crossing_the_border", "instruments", 1043.5, 1294.0, 0.0, -14, 2.0, 3.0,
      auto=[[1043.5, 7], [1075.0, 5], [1105.0, 3], [1140.0, 0], [1146.0, -3], [1252.0, -3], [1258.0, 0], [1271.0, 0]],   # peak −3
      note="slow dark build (file 0–105, −32 → −2 LU, lifted by auto) from 'luckily the central bank did catch on' 1043; build "
           "through 'a buyer…owned by the same group' 1125 (stinger); 105–210 peak = '$79 million…$80 million…the report…head of the "
           "central bank (Aug 14/15)…buries it' 1146–1193 → 'two months later' → ABC Color 1233.5 → 'last week' 1258.8; "
           "fades 1253–1283 ('political pressure…own party')"),
    L("P10", "crossing_the_border", "bass", 1118.5, 1294.0, 75.0, -19, 3.0, 3.0),
    L("P10", "crossing_the_border", "drums", 1168.5, 1294.0, 125.0, -20, 2.0, 3.0, note="drums (file 125) from '…someone's paying us $80 million' → the report"),
    L("P11", DR, "bass", 1268.0, 1310.0, 280.0, -18, 3.0, 4.0, note="glue into P12 (IMF)"),
    L("P11", DR, "instruments", 1280.0, 1300.0, 140.0, -19, 2.0, 3.0),
    # ================= P12 (pys12, 1294.5–1456.5): the IMF → the Senate presses → burying looks like corruption → the unique law
    L("P12", "where_it_all_happened", "instruments", 1294.5, 1440.5, 0.0, -15, 1.5, 1.5,
      auto=[[1294.5, 0], [1329.0, 0], [1330.0, -1.5], [1345.0, -1.5], [1346.0, 0], [1354.0, 0], [1357.0, -2.5], [1440.5, -2.5]],   # peak −2.5
      note="E-minor 'crime scene' pulse: thin 20–45 under 'developing country…investors rely on the IMF assessment'; full band back "
           "(file 45) on 'whatever IMF says is very important' 1337–1339; 75–145 peak = 'the Senate…pressure on the central bank' 1369 → "
           "'one bad bank vs every bank' → 'a very unique law' 1417 → 'criminally held liable whenever the thing blows apart' 1437–1440.7 (file 145 = its end)"),
    L("P12", "where_it_all_happened", "bass", 1294.5, 1440.5, 0.0, -20, 1.5, 1.5),
    L("P12", "where_it_all_happened", "melody", 1304.5, 1440.5, 10.0, -18.5, 1.5, 1.5),
    L("P12", "where_it_all_happened", "drums", 1334.5, 1440.5, 40.0, -21, 1.5, 1.5),
    L("P12", DR, "bass", 1432.0, 1470.0, 100.0, -18, 2.0, 4.0, note="floor under 'a personal disincentive' → 'combine all of this'"),
    L("P12", DR, "instruments", 1438.0, 1462.0, 130.0, -19, 2.0, 3.0),
    # ================= P13 (pys13, 1456.5–1621.87): the vote → 'the bank is done' → apps dead → protests → impeachment → arrests → coda
    L("P13", "starfall", "instruments", 1456.6, 1486.7, 53.9, -14, 2.0, 0.1,
      note="the cold-open track returns (rhyme): 'the board does the right thing…votes unanimously' 1460–1469; its 78–84 build lands "
           "the 84 s peak on 'the bank is done' 1486.66 — CUT DEAD there (stinger)"),
    L("P13", "starfall", "melody", 1456.6, 1486.7, 53.9, -18, 2.0, 0.1),
    L("P13", "starfall", "bass", 1482.6, 1486.7, 80.0, -19, 0.4, 0.1),
    L("P13", "starfall", "drums", 1482.6, 1486.7, 80.0, -21, 0.4, 0.1),
    L("P13", "buried_in_the_dirt", "instruments", 1490.5, LEN, 0.0, -15, 2.0, 2.5,
      auto=[[1490.5, 0], [1499.0, 0], [1500.0, -1.5], [1540.0, -1.5], [1541.0, 0], [1570.0, 0], [1573.0, -3], [1597.0, -3], [1600.0, 0]],
      note="E-minor orchestral drama (sentimental) for the people: rises from the silence after the apps stop working; "
           "melody (file 65) on 'the Senate rejects his resignation…impeaches him' 1560; 85–105 peak = the arrests → 'investigation "
           "ongoing' → 'going viral' 1575–1595; the file's own 110 s drop on the bleep 'stupid [bleep]' 1600.6; quiet tail under "
           "'tax the poor…Columbia…more fire' to the end"),
    L("P13", "buried_in_the_dirt", "bass", 1490.5, LEN, 0.0, -21, 2.0, 2.5),
    L("P13", "buried_in_the_dirt", "melody", 1555.5, 1601.0, 65.0, -16.5, 1.5, 0.4, auto=[[1555.5, 0], [1570.0, 0], [1573.0, -3], [1601.0, -3]]),
    L("P13", "buried_in_the_dirt", "drums", 1510.5, 1600.8, 20.0, -21.5, 2.0, 0.3),
    L("P13", "sfx", "chant", 1525.5, 1547.0, 20.0, -28, 2.0, 3.0, file="sfx/protest_distant_drums_chants.wav",
      note="distant street protest (drums, chants) under 'that's why we are seeing protest all over the place' 1528.2"),
    L("P13", DR, "bass", 1596.0, LEN, 120.0, -20, 3.0, 2.5, note="floor to the end"),
]

stingers = [
    dict(file="boom_sub_bass_clean_01", t=27.68, sync="loudest", rel_lu=-28, note="'Around 60% of adults'"),
    dict(file="swell_reverse_timpani_cymbal", t=115.34, sync="loudest", rel_lu=-27, note="swell into 'Let's look at exactly how we got here'"),
    dict(file="boom_sub_bass_clean_01", t=205.59, sync="loudest", rel_lu=-26, note="'there was one bad news'"),
    dict(file="boom_cinematic_deep", t=524.28, sync="loudest", rel_lu=-25, note="'the next day he becomes part of the central bank'"),
    dict(file="boom_dark_cinematic_low_hit", t=650.32, sync="loudest", rel_lu=-27, note="'That law gets changed'"),
    dict(file="boom_dark_cinematic_low_hit", t=797.27, sync="loudest", rel_lu=-22, note="'too good to be true. And guess what? It was.' (music cut)"),
    dict(file="boom_cinematic_deep", t=1125.14, sync="loudest", rel_lu=-24, note="buyer reveal: 'owned by the same group that own the bank'"),
    dict(file="boom_sub_bass_clean_01", t=1193.27, sync="loudest", rel_lu=-25, note="'he basically buries the report'"),
    dict(file="riser_reverse_cymbal_short", t=1233.54, sync="loudest", rel_lu=-28, note="ends on 'ABC Color'"),
    dict(file="boom_dark_cinematic_low_hit", t=1486.66, sync="loudest", rel_lu=-21, note="'the bank is done' (music cut)"),
    dict(file="boom_cinematic_deep", t=1562.36, sync="loudest", rel_lu=-23, note="'the Senate rejects his resignation and then impeaches him'"),
]

# phase 2: the editors' booms on 20.8 ('UENO' logo, hero) and 448.69 ('4×' lands, hero) replace my stingers at 18.80 / 448.75
# (picture-synced; a stinger within 0.6 s would drop them). Edits of editor markers (place_sound applies them by t + type):
marker_edits = [
    dict(t=207.76, type="boom_low", action="drop", note="2.2 s after the 'one bad news' stinger 205.59 — one hit is enough"),
    dict(t=232.42, type="camera_flash", action="drop", note="'flash' = a white flash frame, not a camera: no sound"),
    dict(t=331.8, type="boom_low", action="drop", note="1.4 s before the 2020 boom 333.21 (hero) across the join"),
    dict(t=575.03, type="boom_low", action="retype", to="stamp_thud", note="blocks drop: thuds, the boom kept for the hero 577.27"),
    dict(t=575.83, type="boom_low", action="retype", to="stamp_thud", note="blocks drop: thud"),
    dict(t=590.0, type="boom_low", action="retype", to="stamp_thud", note="big block lands: thud; boom kept for the slam 593.05"),
    dict(t=652.55, type="paper_tear", action="retype", to="crack", note="the 10% cap line cracks (hero: the scene's point)"),
    dict(t=653.56, type="boom_low", action="drop", note="third hit in 3.3 s after the 'law gets changed' stinger + crack"),
    dict(t=690.0, type="crowd_room", action="retype", to="crowd_chant", note="editor 'crowd' = protest ambience (alias was office walla)"),
    dict(t=724.85, type="dot_ticks", action="retype", to="coins", note="money chips pour into the bank: handful of coins (editor's wish)"),
    dict(t=797.25, type="paper_tear", action="retype", to="crack", note="ice crack through 0.58% on 'It was.' (editor's wish)"),
    dict(t=892.95, type="paper_tear", action="retype", to="crack", note="the bank cracks"),
    dict(t=1041.17, type="riser", action="drop", note="fights DOX's own drop at 1041.6 + the music box (lead's note)"),
]

bleeps = [   # Krish: "Can we bleep the shit part?" — the lead mutes these exact VO spans in the final mix (DECISIONS §3)
    dict(t=1104.58, dur=0.32, note="'the loan was a piece of [shit]'"),
    dict(t=1159.43, dur=0.16, note="'its own piece of [shit]'"),
    dict(t=1600.60, dur=0.24, note="'people do stupid [shit]'"),
]

sheet = dict(length=LEN, bed_lu_under_vo=13.0,   # before the VO duck (which takes ≈ 2.5 dB off) → ≈ 15.8 LU under after it

             doc="Layered Epidemic bed for 'Paraguay' (Searching Lessons). Master seconds of vo_py.wav/vo_py.mp3. Generated by "
                 "project/paraguay/gen/make_cuesheet.py — edit there. Key family E minor / G major. Acts = SEGMENTS.md §3 (P1–P13 = "
                 "pys01–pys13). 'bleeps' = place_sound.py adds a 1 kHz bleep (VO − 3 LU) over each muted word. No insert ducks: the "
                 "X clip's own crowd is a layer (P1).",
             layers=layers, stingers=stingers, ducks=[], bleeps=bleeps, marker_edits=marker_edits,
             vo_duck=dict(gap=12.0, attack=0.05, release=0.4, max_cut=-15.0))
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "music_cuesheet.json")
json.dump(sheet, open(out, "w"), indent=1)
print("wrote", os.path.normpath(out), len(layers), "layers,", len(stingers), "stingers,", len(bleeps), "bleeps")
