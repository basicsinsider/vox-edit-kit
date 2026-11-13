"""ED12 build: inlines the map json into the templates -> compositions/pdNN.html.
Usage (repo root): python3 project/podcast/gen/ed12/build.py pd29 pd30   (edit the *.template.html here, not the built file)"""
import sys, pathlib
H = pathlib.Path(__file__).resolve().parent; R = H.parents[3]
DATA = {"pd29": "assets/podcast/pd29/pd29_map.json", "pd30": "assets/podcast/pd30/pd30_africa.json"}
for c in sys.argv[1:]:
    s = (H / f"{c}.template.html").read_text()
    if c in DATA: s = s.replace("/*MAPJSON*/null", (R / DATA[c]).read_text())
    (R / "compositions" / f"{c}.html").write_text(s)
    print("built", c, len(s))
