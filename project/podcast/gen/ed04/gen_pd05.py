"""Builds compositions/pd05.html from pd05_template.html with the US map geometry inlined (no runtime fetch).
Geometry: assets/maps/us_overlay.json (s02 pixel space x=(lon+128)*100, y=(52-lat)*100), drawn inside a
<g transform="translate(-213.066 -266) scale(1.06533 1.33)"> so it lands in the kit `us` pixel space (6392x3524).
Usage: python3 project/podcast/gen/ed04/gen_pd05.py"""
import json, pathlib, re
H = pathlib.Path(__file__).resolve().parent
R = H.parents[3]
ov = json.load(open(R / "assets/maps/us_overlay.json"))
st = ov["states"]
rep = {
    "%%STATES%%": " ".join(v["d"] for k, v in st.items() if k not in ("AK", "HI", "PR")),
    "%%WEST%%": ov["regions"]["west_of_mississippi"]["d"],
    "%%RIVER%%": ov["mississippi"]["d"],
    "%%NY%%": st["NY"]["d"], "%%NJ%%": st["NJ"]["d"], "%%MA%%": st["MA"]["d"],
}
tpl = (H / "pd05_template.html").read_text()
for k, v in rep.items():
    tpl = tpl.replace(k, v)
left = re.findall(r"%%[A-Z_]+%%", tpl)
assert not left, left
(R / "compositions/pd05.html").write_text(tpl)
print("ok", len(tpl))
