#!/usr/bin/env python3
"""ED13: inline world-map paths into pd33.  python3 project/podcast/gen/ed13/build.py
Source: project/podcast/gen/ed13/pd33.src.html -> compositions/pd33.html
Placeholder /*WORLDSUB*/ -> {key: path} for every country named in the source's KEYS list (world 6144 px space, ED10 maps.json)."""
import json, re, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "../../../.."))
M = json.load(open(os.path.join(HERE, "../ed10/maps.json")))
D = M["world"]["d"]
for n in ["pd33"]:
    src = open(os.path.join(HERE, n + ".src.html")).read()
    keys = sorted(set(re.findall(r'"([a-z_]+)"', re.search(r"/\*KEYS\*/(.*?)/\*ENDKEYS\*/", src, re.S).group(1))))
    missing = [k for k in keys if k not in D]
    if missing: raise SystemExit("missing map keys: %s" % missing)
    out = src.replace("/*WORLDSUB*/", json.dumps({k: D[k] for k in keys}))
    open(os.path.join(ROOT, "compositions", n + ".html"), "w").write(out)
    print(n, len(out), len(keys), "countries")
