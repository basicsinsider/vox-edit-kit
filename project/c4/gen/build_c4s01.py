"""Assemble compositions/c4s01.html from c4s01.src.html + scenes_{a,b,c}.js + the simplified map paths.
Run from the project root: python3 project/c4/gen/build_c4s01.py"""
import json, pathlib
G = pathlib.Path("project/c4/gen")
src = (G / "c4s01.src.html").read_text()
scenes = "".join((G / f"c4s01.scenes_{k}.js").read_text() for k in "abc")
P = json.load(open("assets/c4/derived/c4s01/paths.json"))
keep = {"eurasia": ["poland", "czechia", "slovakia", "hungary", "romania", "bulgaria", "albania", "russia", "ukraine", "belarus", "lithuania", "latvia", "estonia",
                    "moldova", "georgia", "armenia", "azerbaijan", "kazakhstan", "uzbekistan", "turkmenistan", "kyrgyzstan", "tajikistan", "germany", "china", "taiwan"],
        "africa": None}
maps = {}
for r, ids in keep.items():
    d = P[r]["d"]
    maps[r] = {"d": {k: d[k] for k in (ids or d)}}
maps["eurasia"]["gdr_clip"] = P["eurasia"]["gdr_clip"]
out = src.replace("/*__PATHS__*/null", json.dumps(maps, separators=(",", ":"))).replace("    /*__SCENES__*/\n", scenes)
pathlib.Path("compositions/c4s01.html").write_text(out)
print("compositions/c4s01.html", len(out))
