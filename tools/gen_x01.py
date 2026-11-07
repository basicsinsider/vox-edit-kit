"""Builds compositions/x01-spb-drones.html from tools/x01_template.html + assets/maps/russia/russia_spb.json
(inlines the map paths so the composition has no runtime fetches). Usage: python3 tools/gen_x01.py"""
import json, pathlib
R = pathlib.Path(__file__).resolve().parent.parent
g = json.load(open(R / "assets/maps/russia/russia_spb.json"))
s = (R / "tools/x01_template.html").read_text()
small = {k: v for k, v in g.items() if k not in ("russia_d", "urban_d", "neva_d")}
small["urban_d"] = g["urban_d"]
s = (s.replace("__RUSSIA_D__", g["russia_d"]).replace("__URBAN_D__", g["urban_d"]).replace("__NEVA_D__", g["neva_d"])
      .replace("__SPB_WX__", str(g["spb_wide"][0])).replace("__SPB_WY__", str(g["spb_wide"][1]))
      .replace("__GEO_JSON__", json.dumps(small)))
(R / "compositions/x01-spb-drones.html").write_text(s)
print("wrote compositions/x01-spb-drones.html", len(s))
