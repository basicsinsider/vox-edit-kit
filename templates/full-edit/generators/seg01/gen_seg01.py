"""Generates compositions/seg01.html from tools/seg01/seg01_template.html with the map geometry inlined
(same approach as tools/gen_s02.py — no runtime fetch). Usage: python3 tools/seg01/gen_seg01.py"""
import json, pathlib, re

R = pathlib.Path(__file__).resolve().parent.parent.parent
ov = json.load(open(R / "assets/maps/us_overlay.json"))
ind = json.load(open(R / "assets/maps/indiana_relief_grey.json"))
st = ov["states"]
states = " ".join(v["d"] for k, v in st.items() if k not in ("AK", "HI", "PR"))
river = ov["mississippi"]["d"]; rlen = ov["mississippi"]["length_px"]
reg = ov["regions"]


def px(lon, lat):
    return ((lon + 128) * 100, (52 - lat) * 100)


# HQ clusters of the 12 trillion-dollar companies (identical to tools/gen_s02.py — approved sample)
clusters = [
    ("bay", px(-122.05, 37.40), 5), ("sea", px(-122.22, 47.64), 2), ("aus", px(-97.74, 30.27), 1),
    ("stb", px(-97.16, 25.99), 1), ("oma", px(-95.94, 41.26), 1), ("boi", px(-116.20, 43.62), 1),
]
pins = ""
for cid, (x, y), n in clusters:
    pins += f'''<g class="s1-pin" transform="translate({x:.0f} {y:.0f})">
      <circle class="s1-halo" r="90" fill="none" stroke="#f4eee2" stroke-width="7" opacity="0.5"/>
      <circle r="44" fill="#f4eee2" stroke="#141312" stroke-width="10"/>
      {f'<text x="66" y="40" class="s1-count t-display">×{n}</text>' if n > 1 else ''}
    </g>'''
ix, iy = ov["places"]["indianapolis"]["x"], ov["places"]["indianapolis"]["y"]
pins += f'''<g class="s1-pin" id="seg01-sc007-pin-indy" transform="translate({ix:.0f} {iy:.0f})">
      <circle id="seg01-sc007-indy-halo" class="s1-halo" r="90" fill="none" stroke="#f2d33b" stroke-width="8" opacity="0.6"/>
      <circle r="44" fill="#f2d33b" stroke="#141312" stroke-width="10"/>
    </g>'''

# SC017 route: Palo Alto -> New York, a gentle arc (quadratic) in overlay space
pa = ov["places"]["palo_alto"]; ny = ov["places"]["new_york_city"]
route = f"M{pa['x']:.0f} {pa['y']:.0f} Q{(pa['x'] + ny['x']) / 2:.0f} {min(pa['y'], ny['y']) - 900:.0f} {ny['x']:.0f} {ny['y']:.0f}"
labels = {k: st[k]["label"] for k in ("CA", "NY", "NJ", "MA")}

tpl = (R / "tools/seg01/seg01_template.html").read_text()
rep = {
    "%%STATES%%": states, "%%WEST%%": reg["west_of_mississippi"]["d"], "%%EAST%%": reg["east_of_mississippi"]["d"],
    "%%RIVER%%": river, "%%RLEN%%": str(int(rlen) + 10), "%%PINS%%": pins,
    "%%IN_LOCAL%%": ind["states"]["IN"]["d"] if isinstance(ind["states"]["IN"], dict) else ind["states"]["IN"],
    "%%CA%%": st["CA"]["d"], "%%NY%%": st["NY"]["d"], "%%NJ%%": st["NJ"]["d"], "%%MA%%": st["MA"]["d"],
    "%%ROUTE%%": route, "%%LABELS%%": json.dumps(labels), "%%IX%%": f"{ix:.1f}", "%%IY%%": f"{iy:.1f}",
}
for k, v in rep.items():
    tpl = tpl.replace(k, v)
left = re.findall(r"%%[A-Z_]+%%", tpl)
assert not left, left
(R / "compositions/seg01.html").write_text(tpl)
print("ok", len(tpl))
