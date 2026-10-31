"""Assemble compositions/c3s03.html from c3s03.src.html + c3s03.scenes_{a,b,c}.js + map paths + recognition lists.
Run from the project root: python3 project/c3/gen/build_c3s03.py"""
import json, pathlib, re
G = pathlib.Path("project/c3/gen")
src = (G / "c3s03.src.html").read_text()
scenes = "".join((G / f"c3s03.scenes_{k}.js").read_text() for k in "abc")
P = json.load(open("assets/c3/derived/c3s03/paths.json"))
E = json.load(open("assets/c4/derived/c4s01/paths.json"))["eurasia"]
eur = {"d": {k: E["d"][k] for k in ["poland", "czechia", "slovakia", "hungary", "romania", "bulgaria", "albania", "russia", "ukraine", "belarus", "lithuania", "latvia",
        "estonia", "moldova", "georgia", "armenia", "azerbaijan", "kazakhstan", "uzbekistan", "turkmenistan", "kyrgyzstan", "tajikistan", "germany", "china"]}, "gdr_clip": E["gdr_clip"]}
R = json.load(open("assets/c3/data/recognition.json"))["snapshots_roc_recognisers"]
CID = {"United States": "united_states_of_america", "Korea, Republic of": "south_korea", "Holy See (Vatican City)": "vatican", "Dominican Republic": "dominican_rep",
       "Central African Republic": "central_african_rep", "Ivory Coast": "c_te_d_ivoire", "Zaire": "dem_rep_congo", "Congo-Brazzaville": "congo", "Dahomey": "benin",
       "South Vietnam": "vietnam", "Gambia": "gambia"}
def ids(lst):
    out = []
    for n in lst:
        k = CID.get(n, re.sub(r"[^a-z]+", "_", n.lower()).strip("_"))
        if k in P["world"]["d"]: out.append(k)
        else: print("  no path:", n, k)
    return out
rec = {"r1950": ids(R["1950"]["roc"]), "r1969": ids(R["1969"]["roc"])}
out = (src.replace("/*__PATHS__*/null", json.dumps(P, separators=(",", ":")))
          .replace("/*__EURASIA__*/null", json.dumps(eur, separators=(",", ":")))
          .replace("/*__REC__*/null", json.dumps(rec, separators=(",", ":")))
          .replace("    /*__SCENES__*/\n", scenes))
pathlib.Path("compositions/c3s03.html").write_text(out)
print("compositions/c3s03.html", len(out), {k: len(v) for k, v in rec.items()})
