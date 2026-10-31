"""Builds compositions/c6s02.html from c6s02_template.html + c6s02_scenes.js + assets/c6/derived/c6s02/paths.json.
Run: python3 project/c6/gen/build_c6s02.py   (re-run c6s02_assets.py first if the derived assets change)."""
import json, os
R = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
g = lambda *a: os.path.join(R, *a)
t = open(g("project/c6/gen/c6s02_template.html")).read()
sc = open(g("project/c6/gen/c6s02_scenes.js")).read()
pd = json.dumps(json.load(open(g("assets/c6/derived/c6s02/paths.json"))), separators=(",", ":"))
assert "/*__PATHS__*/null" in t and "/*__SCENES__*/" in t
out = t.replace("/*__PATHS__*/null", pd).replace("/*__SCENES__*/", sc)
open(g("compositions/c6s02.html"), "w").write(out)
print("wrote compositions/c6s02.html", len(out))
