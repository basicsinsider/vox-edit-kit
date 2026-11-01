"""Build compositions/ivs06.html from ivs06_template.html: inline the grey-man path and the padded-map borders."""
import json, re
R = "/home/user/vox-edit-kit/"
src = open(R + "project/ivan/gen/ivs06_template.html").read()
gm = re.search(r'\sd="([^"]+)"', open(R + "assets/ivan/motifs/grey_man.svg").read()).group(1)
b = json.load(open(R + "assets/ivan/ivs06/derived/ee_pad_borders.json"))
keep = ["c-russia", "c-ukraine", "c-crimea", "c-poland", "c-belarus", "c-moldova", "c-lithuania", "c-romania", "c-slovakia", "c-hungary"]
src = src.replace("GREYMAN", gm).replace("/*BORDERS*/{}", json.dumps({k: b[k] for k in keep}, separators=(",", ":")))
open(R + "compositions/ivs06.html", "w").write(src)
print("ok", len(src))
