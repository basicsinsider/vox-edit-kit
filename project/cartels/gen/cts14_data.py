"""Inline data for compositions/cts14.html: CDC overdose series + Mexico map paths (between @@DATA-BEGIN/@@DATA-END)."""
import csv, json, re, pathlib
R = pathlib.Path(__file__).resolve().parents[3]
rows = list(csv.DictReader(open(R / "assets/cartels/docs/data/cdc_vsrr_us_overdose_12mo.csv")))
od = [int(r["predicted_12mo"]) for r in rows]
assert rows[0]["period_end"] == "2015-01" and rows[-1]["period_end"] == "2026-06" and len(od) == 138
svg = open(R / "assets/maps/kit/mexico_overlay.svg").read()
def d(i):
    m = re.search(r'<path[^>]*id="' + i + r'"[^>]*\bd="([^"]+)"', svg)
    return m.group(1)
paths = {k: d(k) for k in ["hwy-mex15-north", "b-us_mexico", "st-sinaloa", "us-arizona", "us-new_mexico", "us-texas", "us-california"]}
js = "const OD = " + json.dumps(od) + ";\n    const MP = " + json.dumps(paths) + ";"
p = R / "compositions/cts14.html"
s = p.read_text()
s = re.sub(r"// @@DATA-BEGIN.*?// @@DATA-END", lambda m: "// @@DATA-BEGIN (project/cartels/gen/cts14_data.py)\n    " + js + "\n    // @@DATA-END", s, flags=re.S)
p.write_text(s)
print("ok", len(od), max(od), od[-1], {k: len(v) for k, v in paths.items()})
