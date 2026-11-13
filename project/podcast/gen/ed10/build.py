#!/usr/bin/env python3
"""Inline map path data into the ED10 compositions.  python3 project/podcast/gen/ed10/build.py [pd21 pd22 ...]
Source: project/podcast/gen/ed10/pdNN.src.html  ->  compositions/pdNN.html
Placeholders:  /*EA:china,taiwan*/  -> {"china":"M…",…} (east_asia, 3199 px space)   /*WORLD:a,b*/ -> world (6144 px space)
               /*WORLDALL*/ -> all world paths   /*ROC1969*/ -> list of world keys recognising the ROC in 1969."""
import json, re, sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "../../../.."))
M = json.load(open(os.path.join(HERE, "maps.json")))
ALIAS = {"united_states": "united_states_of_america", "korea_republic_of": "south_korea", "dahomey": "benin", "ivory_coast": "c_te_d_ivoire",
         "zaire": "dem_rep_congo", "south_vietnam": "vietnam", "central_african_republic": "central_african_rep", "dominican_republic": "dominican_rep"}
def key(n): 
    k = re.sub(r"[^a-z]+", "_", n.lower()).strip("_"); return ALIAS.get(k, k)
def roc1969():
    ks = [key(n) for n in M["world"]["roc1969"]["roc"]]
    return [k for k in ks if k in M["world"]["d"]]
def sub(s):
    s = re.sub(r"/\*EA:([a-z_,]+)\*/", lambda m: json.dumps({k: M["ea"]["d"][k] for k in m.group(1).split(",")}), s)
    s = re.sub(r"/\*WORLD:([a-z_,]+)\*/", lambda m: json.dumps({k: M["world"]["d"][k] for k in m.group(1).split(",")}), s)
    s = s.replace("/*WORLDALL*/", json.dumps(M["world"]["d"]))
    s = s.replace("/*ROC1969*/", json.dumps(roc1969()))
    return s
for n in sys.argv[1:] or ["pd21", "pd22", "pd23", "pd24"]:
    src = os.path.join(HERE, n + ".src.html")
    if not os.path.exists(src): continue
    out = sub(open(src).read())
    open(os.path.join(ROOT, "compositions", n + ".html"), "w").write(out)
    print(n, len(out))
