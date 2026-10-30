"""Fills map paths into seg03_template.tpl -> compositions/seg03.html (lives in tools/seg03)."""
import json, pathlib, re
H = pathlib.Path(__file__).resolve().parent
ROOT = H.parent.parent
d = json.load(open(ROOT / "assets/maps/us_overlay.json"))
def r(s):  # round coordinates to 0 decimals to keep the file small
    return re.sub(r"(\d+)\.\d+", lambda m: m.group(1), s)
src = (H / "seg03_template.tpl").read_text()
src = src.replace("{{WEST}}", r(d["regions"]["west_of_mississippi"]["d"]))
src = src.replace("{{EAST}}", r(d["regions"]["east_of_mississippi"]["d"]))
src = src.replace("{{STATES}}", r("".join(v["d"] for v in d["states"].values())))
src = src.replace("{{RIVER}}", r(d["mississippi"]["d"]))
(ROOT / "compositions/seg03.html").write_text(src)
print(len(src))
