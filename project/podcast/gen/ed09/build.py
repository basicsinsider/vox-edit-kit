#!/usr/bin/env python3
"""ED09: inline map path data into the pd18/pd19/pd20 templates -> compositions/pdNN.html.
Usage: python3 project/podcast/gen/ed09/build.py pd18 [pd19 pd20]"""
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__)); R = os.path.abspath(os.path.join(H, "..", "..", "..", ".."))
us = json.load(open(os.path.join(R, "assets/podcast/pd18/us_paths_3840.json")))
ea = json.load(open(os.path.join(R, "assets/podcast/pd20/east_asia_paths.json")))
rest = {k: [v, us["bbox"][k]] for k, v in us["states"].items() if k != "california"}
SUB = {"/*US_REST*/": json.dumps(rest, separators=(",", ":")), "/*US_ALL*/": json.dumps("".join(us["states"].values())),
       "/*CA*/": json.dumps(us["states"]["california"]), "/*NY*/": json.dumps(us["states"]["new_york"]),
       "/*CHINA*/": json.dumps(ea["china"]), "/*TAIWAN*/": json.dumps(ea["taiwan"])}
for name in sys.argv[1:]:
    s = open(os.path.join(H, name + ".src.html")).read()
    for k, v in SUB.items(): s = s.replace(k, v)
    open(os.path.join(R, "compositions", name + ".html"), "w").write(s)
    print(name, len(s))
