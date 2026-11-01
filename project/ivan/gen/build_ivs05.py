"""Inline the ivs05 map paths into the template -> compositions/ivs05.html (run from repo root)."""
import json
m = json.load(open("assets/ivan/ivs05/derived/ivs05_map_paths.json"))
data = {"wide": {k: m["wide"][k] for k in ("russia", "ukraine")},
        "ee": {"russia": m["ee"]["russia"], "ukraine": m["ee"]["ukraine"], "kx": round(m["ee"]["kx"], 4), "ky": round(m["ee"]["ky"], 4)}}
src = open("project/ivan/gen/ivs05_template.html").read()
assert "/*MAPDATA*/null" in src
open("compositions/ivs05.html", "w").write(src.replace("/*MAPDATA*/null", json.dumps(data, separators=(",", ":"))))
print("compositions/ivs05.html written")
