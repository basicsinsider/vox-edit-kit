"""Assemble compositions/c3s02.html from c3s02.src.html + c3s02.scenes_{a,b,c}.js + the derived map data.
Run from the project root: python3 project/c3/gen/build_c3s02.py   (assets: .venv/bin/python project/c3/gen/c3s02_assets.py)"""
import json, pathlib, re
G = pathlib.Path("project/c3/gen")
src = (G / "c3s02.src.html").read_text()
scenes = "".join((G / f"c3s02.scenes_{k}.js").read_text() for k in "abc")
J = json.load(open("assets/c3/derived/c3s02/c3s02_maps.json"))
def simp(d, step):
    out = []
    for sp in re.findall(r"M[^M]+", d):
        pts = [(float(a), float(b)) for a, b in re.findall(r"(-?\d+\.?\d*) (-?\d+\.?\d*)", sp)]
        q = []
        for x, y in pts:
            if not q or abs(x - q[-1][0]) + abs(y - q[-1][1]) >= step: q.append((x, y))
        if len(q) > 3: out.append("M" + "L".join(f"{x:.0f} {y:.0f}" for x, y in q) + "Z")
    return "".join(out)
J["ea"]["china"] = simp(J["ea"]["china"], 7)
out = src.replace("/*__MAPS__*/null", json.dumps(J, separators=(",", ":"))).replace("    /*__SCENES__*/\n", scenes)
pathlib.Path("compositions/c3s02.html").write_text(out)
print("compositions/c3s02.html", len(out), "china path", len(J["ea"]["china"]))
