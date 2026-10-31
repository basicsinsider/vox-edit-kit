"""Build compositions/c6s01.html from project/c6/gen/c6s01.markup.html + c6s01.script.js (+ inlined map paths).
Run from the repo root: .venv/bin/python project/c6/gen/c6s01_assets.py && python3 project/c6/gen/build_c6s01.py"""
import json, pathlib
G = pathlib.Path("project/c6/gen")
m = (G / "c6s01.markup.html").read_text()
s = (G / "c6s01.script.js").read_text()
paths = json.load(open("assets/c6/derived/c6s01/paths.json"))
s = s.replace("/*@PATHS@*/null", json.dumps(paths, separators=(",", ":")))
out = m.replace("/*@SCRIPT@*/", s)
pathlib.Path("compositions/c6s01.html").write_text(out)
print("compositions/c6s01.html", len(out))
