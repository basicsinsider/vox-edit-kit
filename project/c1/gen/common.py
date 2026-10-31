"""Shared data for the c1 planning docs (beats, ASR fixes). Run gen_beats.py / gen_edit.py from the repo root."""
import json
W = json.load(open("transcript_c1.json"))
END = 602.86
STARTS = {round(w["start"], 2) for w in W}
# ASR/name fixes shown in the corrected transcript (time of token -> corrected token)
FIX = {
    71.81: "**drug**", 133.72: "**Labs,**", 148.12: "**Terman,**", 152.04: "**Terman,**", 163.55: "**Herbert**",
    170.35: "1980, *(slip)*", 236.88: "**trustee(s),**", 260.48: "**Terman**", 265.20: "**east**", 285.19: "**Terman.**",
    286.47: "1900s.", 300.39: "**Lewis**", 314.63: "**Terman**", 333.11: "**Hoover**", 466.70: "**last** *(ASR “NAS”)*",
    522.97: "**Terman**", 522.41: "**II.**",
}
def words(a, b, fix=True):
    out = []
    for w in W:
        if a - 1e-6 <= w["start"] < b - 1e-6:
            out.append(FIX.get(round(w["start"], 2), w["text"]) if fix else w["text"])
    return " ".join(out)
def check_t(t):
    if round(t, 2) not in STARTS:
        raise SystemExit(f"not a word start: {t}")
