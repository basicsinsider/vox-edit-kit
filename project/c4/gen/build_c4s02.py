"""Builds compositions/c4s02.html from c4s02_template.html + the derived map data (inlined as const D)."""
import json, pathlib
R = pathlib.Path(__file__).resolve().parents[3]
s = json.load(open(R / "assets/c4/derived/c4s02/c4s02_small.json"))
D = {"japan": s["ea_japan"], "cia": {"places": s["cia"]["places"]}, "cia_tw": s["cia_tw"], "iso": {"cells": s["iso"]["cells"]},
     "pac": s["pac"], "world_deg": s["world_deg"]}
def rnd(o):
    if isinstance(o, float): return round(o, 1)
    if isinstance(o, list): return [rnd(x) for x in o]
    if isinstance(o, dict): return {k: rnd(v) for k, v in o.items()}
    return o
t = (R / "project/c4/gen/c4s02_template.html").read_text()
t = t.replace("/*DATA*/null", json.dumps(rnd(D), separators=(",", ":")))
(R / "compositions/c4s02.html").write_text(t)
print("wrote compositions/c4s02.html", len(t))
