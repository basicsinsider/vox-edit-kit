"""compositions/cts03.html = cts03_template.html + map data (run from repo root)."""
import json
d = json.load(open("project/cartels/gen/cts03_mapdata.json"))
d["sonpaths"] = {k: d["sonpaths"][k] for k in ("st-sonora", "b-us_mexico")}
d.pop("boat_landmask", None)
t = open("project/cartels/gen/cts03_template.html").read()
open("compositions/cts03.html", "w").write(t.replace("/*MAPDATA*/null", json.dumps(d, separators=(",", ":"))))
print("wrote compositions/cts03.html")
