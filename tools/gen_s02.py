"""Generates compositions/s02-map.html with the map paths inlined (no runtime fetch)."""
import json, pathlib
R = pathlib.Path(__file__).resolve().parent.parent
d = json.load(open(R / "assets/maps/us_overlay.json"))
reg = d["regions"]
states = " ".join(v["d"] for k, v in d["states"].items() if k not in ("AK", "HI", "PR"))
river = d["mississippi"]["d"]; rlen = d["mississippi"]["length_px"]
def px(lon, lat): return ((lon + 128) * 100, (52 - lat) * 100)
# Approximate HQ clusters of the 12 trillion-dollar companies (best guess; confirm list with user).
clusters = [  # the 12 US companies over $1T on companiesmarketcap.com, fetched 2026-10-29 (see analysis/BEATS.md §6)
  ("bay", px(-122.05, 37.40), 5, "Bay Area"),      # NVIDIA, Apple, Alphabet, Broadcom, Meta
  ("sea", px(-122.22, 47.64), 2, "Seattle"),       # Microsoft, Amazon
  ("aus", px(-97.74, 30.27), 1, "Austin"),         # Tesla
  ("stb", px(-97.16, 25.99), 1, "Starbase"),       # SpaceX
  ("oma", px(-95.94, 41.26), 1, "Omaha"),          # Berkshire Hathaway
  ("boi", px(-116.20, 43.62), 1, "Boise"),         # Micron
]
indy = d["places"]["indianapolis"]
ix, iy = (indy["x"], indy["y"]) if isinstance(indy, dict) else indy
pins = ""
for i, (cid, (x, y), n, name) in enumerate(clusters):
    pins += f'''<g class="s02-pin" id="s02-pin-{cid}" transform="translate({x:.0f} {y:.0f})">
      <circle class="s02-halo" r="90" fill="none" stroke="#f4eee2" stroke-width="7" opacity="0.5"/>
      <circle r="44" fill="#f4eee2" stroke="#141312" stroke-width="10"/>
      {f'<text x="66" y="40" class="s02-count t-display">×{n}</text>' if n > 1 else ''}
    </g>'''
pins += f'''<g class="s02-pin" id="s02-pin-indy" transform="translate({ix:.0f} {iy:.0f})">
      <circle id="s02-indy-halo" class="s02-halo" r="90" fill="none" stroke="#f2cf3b" stroke-width="8" opacity="0.6"/>
      <circle r="44" fill="#f2cf3b" stroke="#141312" stroke-width="10"/>
    </g>'''
tpl = (R / "tools/s02_template.html").read_text()
out = (tpl.replace("%%WEST%%", reg["west_of_mississippi"]["d"] if isinstance(reg["west_of_mississippi"], dict) else reg["west_of_mississippi"])
          .replace("%%EAST%%", reg["east_of_mississippi"]["d"] if isinstance(reg["east_of_mississippi"], dict) else reg["east_of_mississippi"])
          .replace("%%STATES%%", states).replace("%%RIVER%%", river).replace("%%RLEN%%", str(int(rlen) + 10))
          .replace("%%PINS%%", pins).replace("%%IX%%", f"{ix:.0f}").replace("%%IY%%", f"{iy:.0f}"))
(R / "compositions/s02-map.html").write_text(out)
print("ok", len(out), ix, iy)
