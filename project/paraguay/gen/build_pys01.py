"""Build compositions/pys01.html from pys01_template.html + derived map paths (assets/paraguay/pys01/derived/maps.json)."""
import json, pathlib
R = pathlib.Path(__file__).resolve().parents[3]
J = json.load(open(R / "assets/paraguay/pys01/derived/maps.json"))
M = {"py": J["py"]["paraguay"], "sa": J["sa"]["paraguay"], "pyp": J["paraguay_places"], "sap": J["south_america_places"]}
src = (R / "project/paraguay/gen/pys01_template.html").read_text()
out = src.replace("/*@MAP@*/{}", json.dumps(M, separators=(",", ":")))
(R / "compositions/pys01.html").write_text(out)
print("compositions/pys01.html", len(out))
