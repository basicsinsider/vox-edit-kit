"""Build compositions/ivs02.html from project/ivan/gen/ivs02_template.html.
Replaces  @S(x)   -> x - SEG_START (segment-local seconds, 3 decimals)
          @D(a,b) -> b - a + 0.10   (timed clip lasts one frame-ish past its cut)
          /*@PATHS@*/ -> simplified country outlines (assets/ivan/ivs02/derived/ee_paths.json, made by ivs02_paths.py)
Run: python3 project/ivan/gen/build_ivs02.py"""
import re, json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[3]
SEG_START = 144.02
src = (ROOT / "project/ivan/gen/ivs02_template.html").read_text()
src = re.sub(r"@S\(([\d.]+)\)", lambda m: "%.3f" % (float(m.group(1)) - SEG_START), src)
src = re.sub(r"@D\(([\d.]+),([\d.]+)\)", lambda m: "%.3f" % (float(m.group(2)) - float(m.group(1)) + 0.10), src)
paths = json.loads((ROOT / "assets/ivan/ivs02/derived/ee_paths.json").read_text())
src = src.replace("/*@PATHS@*/", "const EE = " + json.dumps({k: paths[k] for k in ("russia", "ukraine", "crimea")}) + ";")
(ROOT / "compositions/ivs02.html").write_text(src)
print("wrote compositions/ivs02.html", len(src))
