#!/usr/bin/env python3
"""Cue sheets for the podcast's sound ISLANDS (project/podcast/SOUND_PLAN.md) → project/podcast/cues/islNN.json (+ cues/index.json).

  .venv/bin/python project/podcast/gen/make_cuesheet.py   # (needs the venv: imports pd_islands) then: .venv/bin/python tools/audio/pd_islands.py …

Everything here is written in MASTER seconds (vo_pd / transcript_pd.json) and converted to island-local seconds on output
(islands come from tools/audio/pd_islands.build_islands(): the intro 0–346 s + tail, and every edited section, sections < 20 s
apart sharing an island). Key family A minor / C major — ten fresh Epidemic tracks (assets/audio/epidemic/LOG.md "Podcast").
offset = read position inside the Epidemic file at the layer's start (profiles: assets/audio/epidemic/ANALYSIS.md).

BINDING (MANUAL §10.8 "Music limits", Krish 2026-11-13): bed_lu_under_vo 22, pause_lift_db 0, no vo_duck override (the defaults
gap 20 / gap_fast 18 / ceiling 20 apply). `rel_lu` only balances the layers against each other — place_sound normalises every
island's bed to VO − 22 LU and then ducks it under the voice.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "tools", "audio"))
from pd_islands import build_islands, PRE, POST          # noqa: E402

OUT = os.path.join(HERE, "..", "cues")
DUR = {"observatory": 192, "melted_mind": 125, "mindscape": 186, "until_now": 168, "one_step_away": 181, "sliding_doors": 166,
       "a_trace_of_light": 188, "seekers_and_finders": 141, "how_did_we_get_here": 346, "stay_this_way": 223}
DR = "how_did_we_get_here"     # tempo-free A-minor drone (melody + instruments stems; its bass stem pulses a little — not used)
ENTER = 0.8                    # music enters this long before a section's first frame …
FADE_IN = 1.3                  # … softly: still rising at the cut
TAIL = 3.0                     # and is gone this long after the last frame
FADE_OUT = 2.8


# per-cue balance trims (dB on every layer of the cue), from the act-level check (aim −20…−24 LU re the voice; SOUND_PLAN §8)
TRIM = {"I8": -1.5, "I5": -0.5, "I2": +1.0, "I6": +0.5}


def L(cue, track, stem, start, end, offset, rel, fi=1.5, fo=1.5, auto=None, note=""):
    rel = round(rel + TRIM.get(cue, 0.0), 2)
    d = dict(cue=cue, track=track, stem=stem, start=round(start, 3), end=round(end, 3), offset=round(offset, 3), rel_lu=rel,
             fade_in=fi, fade_out=fo)
    if auto:
        d["auto"] = auto
    if note:
        d["note"] = note
    return d


# ============================================================ the intro island (pd01–pd03, 0–346 s + a 5 s tail)
# One arc: the IDEA theme (Observatory) → bust → the foundry idea (Melted Mind) → the board / the unnamed executive (Mindscape)
# → New York (Until Now) → the aside (floor only) → the cold shoulder (Stay This Way) → the reveal and the rivalry (One Step Away).
END = 351.3
intro_layers = [
    # --- floor: the drone under every join (two takes of the file, cross-faded)
    L("I0", DR, "melody", 0.0, 182.0, 92.0, -30, 0.6, 5.0, note="tempo-free A-minor floor from frame 1; every track enters and leaves over it"),
    L("I0", DR, "melody", 177.0, END, 150.0, -30, 5.0, 5.0),
    # --- I1 0–45.6: "Our story starts in 1983 with Robert Tsao" → the insight 11.84 → 4 million → 24 million 28.40 → record profits 43
    L("I1", "observatory", "instruments", 0.0, 46.8, 0.0, -21, 0.5, 1.6,
      auto=[[0.0, -2], [11.0, -2], [12.6, 0], [46.8, 0]],
      note="the IDEA theme: curious electronic pulses, low under the first two sentences, opens on 'an unique insight' 11.84 / "
           "'An insight that's gonna change the future' 12.64; carries 'You see, just a year earlier' 16.80 and the numbers "
           "(4 million 23.9 → 24 million 28.40 → 6X 29.84 → record profits 41–45); out on 'But quickly after that' 45.60"),
    L("I1", "observatory", "melody", 0.0, 46.8, 0.0, -26, 0.5, 1.6, note="its melody is only active 0–15 and 40–50: the opening and 'record profits'"),
    L("I1", "observatory", "bass", 16.4, 46.8, 16.4, -29, 1.5, 1.2, note="weight from 'You see' — the boom"),
    # --- I2 45.6–66: the phone boom dies, UMC's sales die → "it made no sense to create chips for just one product"
    L("I2", "stay_this_way", "instruments", 44.6, 68.5, 74.0, -18.0, 2.0, 3.0,
      note="the bust: the pulse is gone, a dark floating pad under 'died away' 48.88 / 'UMC's sales also died away' → the lesson 53–65"),
    # --- I3 65.97–113.5: "In fact, a chip factory would be more successful if it made chips for basically any product" → the foundry
    L("I3", "melted_mind", "instruments", 65.2, 114.2, 19.5, -22, 1.5, 1.5,
      auto=[[65.2, 0], [92.5, 0], [94.0, -3], [112.8, -3], [113.8, 0], [114.2, 0]],
      note="hopeful pulses: enters on 'In fact' 65.97; 'a novel concept' 77.7 / 'a pure play chip factory or a foundry' 80–82 / "
           "'Tsao could see the future' 83.5 (its melody, file 30+); thinner under 'he had to ask permission from his board' 93.09–113"),
    L("I3", "melted_mind", "melody", 72.5, 94.5, 26.8, -25, 2.0, 2.0, note="'Now, right now that sounds obvious… back in 1983 this was a novel concept'"),
    L("I3", "melted_mind", "bass", 65.2, 94.0, 19.5, -29, 1.5, 2.0),
    # --- I4 113.89–160.6: the board says yes → "one condition" 123.86 → the unnamed executive
    L("I4", "mindscape", "instruments", 120.6, 161.6, 0.0, -21, 2.5, 1.8,
      note="the mystery colour (dark electronic pulses): creeps in under 'But at the end of the meeting' 121.09, there on 'one "
           "condition' 123.86; 'the most respected Chinese American in the chip business' 132–136, '25,000 people' 138"),
    L("I4", "mindscape", "melody", 123.6, 158.0, 3.0, -25, 1.0, 2.5, note="the executive's motif (file 0–35) — it returns at the reveal as One Step Away's melody register"),
    L("I4", "melted_mind", "instruments", 113.6, 122.4, 68.0, -24, 0.6, 1.6, note="'But luckily… they tell him yes, almost on the spot' — the idea theme's last bars, cut by 'But'"),
    # --- I5 160.98–182.6: "Robert gets on the first flight to New York" → dinner → "on top of the world" 176.6
    L("I5", "until_now", "instruments", 160.3, 183.4, 61.0, -22, 1.2, 1.4,
      note="travelling pulse (adventure, smooth): enters on 'After hearing this' 160.98; its own rise (file 70–80) lands on "
           "'he flies back feeling on top of the world' 175.3–177.2; out as Sunkit's first question starts 182.88"),
    L("I5", "until_now", "melody", 160.3, 183.4, 61.0, -24, 1.2, 1.4),
    # --- I6 182.88–227.2: the aside (Sunkit's questions, face-cam pop-ins): floor only, nothing rhythmic over the two voices
    L("I6", "stay_this_way", "melody", 183.0, 229.0, 44.0, -20.5, 3.0, 3.0, note="a breath of air over the drone while they talk (tempo-free)"),
    # --- I7 227.52–272.4: "but to his surprise" 230.48 → stonewalled 244.08 → "so he drops the idea" 268.83
    L("I7", "stay_this_way", "instruments", 229.3, 274.5, 96.0, -22, 2.0, 3.5,
      note="the cold shoulder: dark floating pad from 'but to his surprise' 230.48; 'he's getting stonewalled' 244.08; "
           "'drop this whole thing' 257; 'so he drops the idea' 268.83"),
    L("I7", "stay_this_way", "bass", 243.0, 274.0, 109.7, -27, 1.5, 3.0, note="low weight from 'stonewalled'"),
    # --- I8 272.43–346 (+tail): two years later → across the street → "guess who" 297.87 → Morris Chang 315.02 → TSMC 323.74 → rivalry
    L("I8", "one_step_away", "instruments", 271.6, END, 56.6, -22, 2.5, 5.0,
      note="the build: offset puts the file's 100 s entry of the full band on 'Morris' 315.02 (file 100.0) and its 108–135 crest on "
           "'The company is TSMC' 323.74 → 'a betrayal' 327.42 → 'two decades… this war' 330–335 → 'a rivalry' 342.62; the tail "
           "fades over 5 s under 'So this is the rivalry…' (file 131–136, just before its own drop)"),
    L("I8", "one_step_away", "melody", 271.6, END, 56.6, -24, 2.5, 5.0,
      auto=[[271.6, -2], [296.5, -2], [298.0, 0], [END, 0]], note="up on 'And guess who the founder… is?' 297.87"),
    L("I8", "one_step_away", "bass", 276.6, END, 61.6, -27, 1.0, 5.0, note="bass from 'Just across the street' 277.07"),
    L("I8", "one_step_away", "drums", 314.2, END, 99.2, -28, 0.4, 5.0, note="its percussion only from the reveal (file 100)"),
]
intro_stingers = [   # phase 2: the editors' picture-synced hits win where they exist (pd01 whoosh 48.84 + boom 51.96 on the bust;
                     # pd03 air_swell 313.17 + boom_low 314.99 "MORRIS CHANG" → boom_dark_cinematic_low_hit) — no stinger of ours there
    dict(file="boom_sub_bass_clean_01", t=123.86, sync="loudest", rel_lu=-31, note="'one condition' (pd02 has only a highlighter there)"),
    dict(file="boom_cinematic_deep", t=323.74, sync="loudest", rel_lu=-30, note="'TSMC' — low weight under pd03's stamp_thud 323.72"),
]

# ============================================================ section colours (reusable; A minor family)
# (track, stem, rel_lu) per colour; WIN = read offsets that start on steady, active material — rotated so that no two neighbouring
# sections use the same passage. The first stem is the lead of the colour.
COL = {
    "US":  dict(track="sliding_doors", stems=[("instruments", -22), ("melody", -26)], win=[12, 100, 40, 104, 22],
                why="warm contemporary-classical (dreamy, hopeful): Stanford, Terman, Hewlett & Packard, the land lease"),
    "ENG": dict(track="observatory", stems=[("instruments", -22), ("melody", -26), ("bass", -30)], win=[2, 82, 30, 108],
                why="the IDEA theme of the intro: curious electronic pulses for the engineering explainers"),
    "GEO": dict(track="mindscape", stems=[("instruments", -22), ("bass", -27), ("melody", -27)], win=[12, 98, 42, 128],
                why="dark electronic pulses (the executive's colour in the intro): geopolitics, the UN, the two Chinas"),
    "SPY": dict(track="seekers_and_finders", stems=[("bass", -23), ("instruments", -24), ("melody", -28)], win=[38, 86, 4],
                why="pulsing suspense bass: Kissinger's secret trip, the vote count"),
    "TW":  dict(track="until_now", stems=[("instruments", -22), ("melody", -25)], win=[12, 62, 36, 84],
                why="the New-York travelling pulse of the intro, now for Taiwan building itself"),
    "REF": dict(track="a_trace_of_light", stems=[("melody", -22), ("instruments", -24), ("bass", -29)], win=[26, 108, 4, 124],
                why="neoclassical, peaceful: theory and reflection (non-competes, the Field Code, copycats, Christensen)"),
    "OSA": dict(track="one_step_away", stems=[("instruments", -22), ("melody", -24), ("bass", -27)], win=[8, 40],
                why="the reveal track of the intro returns for the walkout: a slow orchestral-hybrid build"),
    "DARK": dict(track="stay_this_way", stems=[("instruments", -22), ("melody", -27)], win=[74, 96, 120, 40],
                 why="the cold-shoulder pad of the intro: defeat, exile, a sombre name card"),
}
SECTION_COLOUR = {
    "pd04": "US", "pd05": "US", "pd06": "US", "pd07": "US", "pd08": "US", "pd09": "US", "pd10": "ENG", "pd11": "ENG", "pd12": "US",
    "pd13": "US", "pd14": "ENG", "pd15": "GEO", "pd16": "ENG", "pd17": "ENG", "pd18": "REF", "pd19": "REF", "pd20": "GEO",
    "pd21": "GEO", "pd22": "DARK", "pd23": "GEO", "pd24": "TW", "pd25": "TW", "pd26": "DARK", "pd27": "TW", "pd28": "TW",
    "pd29": "SPY", "pd30": "SPY", "pd31": "SPY", "pd32": "SPY", "pd33": "OSA", "pd34": "REF", "pd35": "GEO", "pd36": "TW",
    "pd37": "TW", "pd38": "TW", "pd39": "TW", "pd40": "GEO", "pd41": "REF", "pd42": "REF", "pd43": "US", "pd44": "REF",
}
# hand-placed extras per section, MASTER seconds (filled in phase 2 once the pictures are locked): stingers on the words,
# marker_edits against the editors' sfx.json (t = master time of the marker = section start + its local t).
SECTION_STINGERS = {}      # "pd35": [dict(file="boom_cinematic_deep", t=4219.9, rel_lu=-29, note="'Deng Xiaoping'")]
MARKER_EDITS = {}          # "pd16": [dict(t=1931.2, type="boom_low", action="drop", note="…")]
OFFSET_OVERRIDE = {"pd08": 60}   # pd08: 104 measured −24.1 LU re VO (busier passage, more duck) → 60       # "pd33": 8   (read offset of the colour track at the section's music entry)

_rot = {}


def pick_offset(col, need, sec_id):
    c = COL[col]
    k = _rot.get(col, 0)
    if sec_id in OFFSET_OVERRIDE:          # an override still uses up its rotation slot, so the other sections keep their passages
        _rot[col] = k + 1
        return OFFSET_OVERRIDE[sec_id]
    n = len(c["win"])
    for j in range(n):
        o = c["win"][(k + j) % n]
        if o + need <= DUR[c["track"]] - 6:
            _rot[col] = k + j + 1
            return o
    _rot[col] = k + 1
    return max(0, min(c["win"][0], DUR[c["track"]] - 6 - need))


def section_island(isl, drone_pos):
    layers, secs = [], isl["sections"]
    a, b = secs[0]["start"] - ENTER, secs[-1]["end"] + TAIL
    # floor: the drone through the whole island (held between the sections of a shared island)
    off = 92 + (drone_pos % 5) * 38
    if off + (b - a) > DUR[DR] - 12:
        off = 92
    layers.append(L(secs[0]["id"], DR, "melody", a, b, off, -29, FADE_IN, FADE_OUT, note="A-minor drone floor (tempo-free)"))
    # colour runs: neighbouring sections of the same colour share one continuous layer, dipped between them
    runs = []
    for s in secs:
        col = SECTION_COLOUR.get(s["id"], "REF")
        if runs and runs[-1][0] == col:
            runs[-1][1].append(s)
        else:
            runs.append([col, [s]])
    for col, ss in runs:
        ra, rb = ss[0]["start"] - ENTER, ss[-1]["end"] + TAIL
        c = COL[col]
        off = pick_offset(col, rb - ra, ss[0]["id"])
        auto = None
        if len(ss) > 1:                                   # hold very low between the sections (voices on camera)
            auto = [[ra, 0]]
            for s0, s1 in zip(ss, ss[1:]):
                auto += [[s0["end"] + 0.3, 0], [s0["end"] + 2.5, -9], [s1["start"] - 2.0, -9], [s1["start"] - 0.2, 0]]
            auto.append([rb, 0])
        for k, (stem, rel) in enumerate(c["stems"]):
            layers.append(L(ss[0]["id"], c["track"], stem, ra, rb, off, rel, FADE_IN, FADE_OUT, auto=auto,
                            note=(f"{'+'.join(s['id'] for s in ss)} [{col}] {c['why']} — " + "; ".join(s["title"] for s in ss)) if k == 0 else ""))
    st = [x for s in secs for x in SECTION_STINGERS.get(s["id"], [])]
    me = [x for s in secs for x in MARKER_EDITS.get(s["id"], [])]
    return layers, st, me


def localise(isl, layers, stingers, edits):
    t0 = isl["start"]
    out = []
    for ly in layers:
        d = dict(ly)
        d["start"], d["end"] = round(max(0.0, ly["start"] - t0), 3), round(min(isl["len"], ly["end"] - t0), 3)
        if ly["start"] < t0:                               # clipped at the island start: keep the read position in sync
            d["offset"] = round(ly["offset"] + (t0 - ly["start"]), 3)
        if "auto" in ly:
            d["auto"] = [[round(p[0] - t0, 3), p[1]] for p in ly["auto"]]
        d["master_start"] = ly["start"]
        out.append(d)
    return out, [dict(s, t=round(s["t"] - t0, 3), master_t=s["t"], sync=s.get("sync", "loudest")) for s in stingers], \
        [dict(e, t=round(e["t"] - t0, 3), master_t=e["t"]) for e in edits]


def main():
    islands, total = build_islands()
    os.makedirs(OUT, exist_ok=True)
    index = []
    for k, isl in enumerate(islands):
        if isl["kind"] == "intro":
            layers, st, me = intro_layers, intro_stingers, [x for s in isl["sections"] for x in MARKER_EDITS.get(s["id"], [])]
        else:
            layers, st, me = section_island(isl, k)
        for ly in layers:                                  # the file must be long enough for the layer
            tr = ly["track"]
            assert ly["offset"] + (ly["end"] - ly["start"]) <= DUR[tr] + 0.5, (isl["id"], tr, ly["stem"], ly["offset"], ly["end"] - ly["start"])
        lay, sti, edi = localise(isl, layers, st, me)
        sheet = dict(island=isl["id"], master_start=isl["start"], master_end=isl["end"], length=isl["len"],
                     sections=[s["id"] for s in isl["sections"]],
                     doc="Layered Epidemic bed for one sound island of the podcast (island-local seconds; master = master_start + t). "
                         "Generated by project/podcast/gen/make_cuesheet.py — edit there. Key family A minor / C major. "
                         "Limits: MANUAL §10.8 'Music limits' (bed VO − 22 LU, VO duck defaults, no pause lifts).",
                     bed_lu_under_vo=22.0, pause_lift_db=0.0,
                     layers=lay, stingers=sti, ducks=[], bleeps=[], marker_edits=edi)
        json.dump(sheet, open(os.path.join(OUT, f"{isl['id']}.json"), "w"), indent=1)
        index.append(dict(id=isl["id"], start=isl["start"], end=isl["end"], sections=sheet["sections"],
                          colours=["intro suite"] if isl["kind"] == "intro" else [SECTION_COLOUR.get(s, "REF") for s in sheet["sections"]],
                          tracks=sorted({f"{ly['track']}/{ly['stem']}" for ly in lay}), layers=len(lay), stingers=len(sti)))
    json.dump(index, open(os.path.join(OUT, "index.json"), "w"), indent=1)
    print(f"wrote {len(islands)} cue sheets to project/podcast/cues/ ({sum(i['layers'] for i in index)} layers, "
          f"{sum(i['stingers'] for i in index)} stingers)")


if __name__ == "__main__":
    main()
