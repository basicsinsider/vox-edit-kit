"""Inline map paths into the cts09 template → compositions/cts09.html.  python3 project/cartels/gen/build_cts09.py"""
import json, os
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
t = open(f"{R}/project/cartels/gen/cts09_template.html").read()
p = json.load(open(f"{R}/project/cartels/gen/cts09_paths.json"))
t = t.replace("/*@@PATHS*/", "const P = " + json.dumps(p, separators=(",", ":")) + ";")
open(f"{R}/compositions/cts09.html", "w").write(t)
print("ok", len(t))
