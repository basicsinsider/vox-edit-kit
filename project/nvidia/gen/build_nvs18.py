"""Builds compositions/nvs18.html from project/nvidia/gen/nvs18_template.html (inlines the China map outline from
assets/nvidia/nvs18/derived/china_crop.json, made by nvs18_assets.py). Run: python3 project/nvidia/gen/build_nvs18.py"""
import json
START = 1822.167
S = lambda s: "%.3f" % (s - START)
j = json.load(open("assets/nvidia/nvs18/derived/china_crop.json"))
src = open("project/nvidia/gen/nvs18_template.html").read()
rep = {"%%CHINA%%": j["china"], "%%HK%%": j["hong_kong"], "%%MAPJ%%": json.dumps({"places": j["places"]}),
       "%%V2S%%": S(1826.05), "%%V9AS%%": S(1861.43), "%%V9BS%%": S(1866.16)}
for k, v in rep.items():
    assert k in src, k
    src = src.replace(k, v)
open("compositions/nvs18.html", "w").write(src)
print("wrote compositions/nvs18.html", len(src))
