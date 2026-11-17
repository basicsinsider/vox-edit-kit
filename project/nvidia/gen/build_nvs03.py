"""Build compositions/nvs03.html from project/nvidia/gen/nvs03_template.html (inlines icon paths + country silhouettes)."""
import json, os, re
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
src = open(os.path.join(ROOT, "project/nvidia/gen/nvs03_template.html")).read()
icons = {}
for n in ["person", "chip", "ban", "lock", "check", "cross", "factory"]:
    s = open(os.path.join(ROOT, "assets/nvidia/shared/icons", n + ".svg")).read()
    s = re.sub(r"<!--.*?-->", "", s, flags=re.S)
    icons[n] = re.search(r"<svg[^>]*>(.*)</svg>", s, flags=re.S).group(1).strip().replace("\n", "")
sil = json.load(open(os.path.join(ROOT, "assets/nvidia/nvs03/derived/silhouettes.json")))
src = src.replace("/*__ICONS__*/{}", json.dumps(icons)).replace("/*__SIL__*/{}", json.dumps(sil))
open(os.path.join(ROOT, "compositions/nvs03.html"), "w").write(src)
print("wrote compositions/nvs03.html", len(src))
