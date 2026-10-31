"""Builds compositions/c1s01.html from a_style.html + b_body.html + c_script.html with the s02 map geometry inlined
(same approach as templates/full-edit/generators/seg01 — no runtime fetch). Usage: python3 project/c1/gen/c1s01/gen_c1s01.py"""
import json, pathlib, re

H = pathlib.Path(__file__).resolve().parent
R = H.parents[3]
ov = json.load(open(R / "assets/maps/us_overlay.json"))
st = ov["states"]
states = " ".join(v["d"] for k, v in st.items() if k not in ("AK", "HI", "PR"))
river = ov["mississippi"]["d"]; rlen = int(ov["mississippi"]["length_px"]) + 10
px = lambda lon, lat: ((lon + 128) * 100, (52 - lat) * 100)
# HQ clusters of the 11 western trillion-dollar companies (identical to the approved s02 / seg01)
clusters = [("bay", px(-122.05, 37.40), 5), ("sea", px(-122.22, 47.64), 2), ("aus", px(-97.74, 30.27), 1),
            ("stb", px(-97.16, 25.99), 1), ("oma", px(-95.94, 41.26), 1), ("boi", px(-116.20, 43.62), 1)]
pins = ""
for cid, (x, y), n in clusters:
    cnt = f'<text x="66" y="40" class="t-display" font-size="120" fill="#f2ede3" stroke="#141312" stroke-width="16" paint-order="stroke">×{n}</text>' if n > 1 else ""
    pins += (f'<g class="c1-mpin" transform="translate({x:.0f} {y:.0f})"><circle class="c1-mhalo" r="90" fill="none" stroke="#f2ede3" stroke-width="7" opacity="0.5"/>'
             f'<circle r="44" fill="#f2ede3" stroke="#141312" stroke-width="10"/>{cnt}</g>\n          ')
ix, iy = ov["places"]["indianapolis"]["x"], ov["places"]["indianapolis"]["y"]
pins += (f'<g id="c1s01-sc011-pin-indy" transform="translate({ix:.0f} {iy:.0f})"><circle r="90" fill="none" stroke="#9fc3e3" stroke-width="8" opacity="0.6"/>'
         f'<circle r="44" fill="#9fc3e3" stroke="#141312" stroke-width="10"/></g>')
rep = {"%%STATES%%": states, "%%WEST%%": ov["regions"]["west_of_mississippi"]["d"], "%%IN%%": st["IN"]["d"],
       "%%RIVER%%": river, "%%RLEN%%": str(rlen), "%%PINS%%": pins, "%%CONUS%%": ov["regions"]["conus_outline"]["d"], "%%CA%%": st["CA"]["d"]}
tpl = (H / "a_style.html").read_text() + (H / "b_body.html").read_text() + (H / "c_script.html").read_text()
for k, v in rep.items():
    tpl = tpl.replace(k, v)
left = re.findall(r"%%[A-Z_]+%%", tpl)
assert not left, left
(R / "compositions/c1s01.html").write_text(tpl)
print("ok", len(tpl))
