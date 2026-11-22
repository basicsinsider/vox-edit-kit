"""Build compositions/cts11.html from cts11_template.html + derived/paths.json (inlines the map outlines)."""
import json
t = open("project/cartels/gen/cts11_template.html").read()
paths = json.load(open("assets/cartels/cts11/derived/paths.json"))
t = t.replace("/*PATHS*/", "const PATHS = " + json.dumps(paths, separators=(",", ":")) + ";")
open("compositions/cts11.html", "w").write(t)
print("compositions/cts11.html", len(t))
