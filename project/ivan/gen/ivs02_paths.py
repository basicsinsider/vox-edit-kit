"""ivs02: simplified country outlines (eastern_europe kit pixel space) -> assets/ivan/ivs02/derived/ee_paths.json"""
import re, json, math
S = open("assets/maps/kit/eastern_europe_overlay.svg").read()
def get(cid):
    m = re.search(r'<path[^>]*id="%s"[^>]*d="([^"]+)"' % cid, S) or re.search(r'<path[^>]*d="([^"]+)"[^>]*id="%s"' % cid, S)
    return m.group(1)
def simplify(d, minstep=9, pad=150):
    out = []
    for sub in d.split("M")[1:]:
        pts = [tuple(map(float, p.split(","))) for p in re.findall(r"-?[\d.]+,-?[\d.]+", sub)]
        if len(pts) < 3: continue
        xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
        if max(xs) < -pad or min(xs) > 6206 + pad or max(ys) < -pad or min(ys) > 4800 + pad: continue
        pts = [(min(max(x, -40), 6246), min(max(y, -40), 4840)) for x, y in pts]
        keep = [pts[0]]; jump = False
        for p in pts[1:]:
            if math.hypot(p[0] - keep[-1][0], p[1] - keep[-1][1]) > 400: jump = True
            if math.hypot(p[0] - keep[-1][0], p[1] - keep[-1][1]) >= minstep: keep.append(p)
        if len(keep) < 3: continue
        out.append("M" + "L".join("%.0f,%.0f" % p for p in keep) + "Z")
    return "".join(out)
res = {c: simplify(get("c-" + c)) for c in ["russia", "ukraine", "crimea", "belarus", "poland", "kazakhstan"]}
json.dump(res, open("assets/ivan/ivs02/derived/ee_paths.json", "w"))
print({k: len(v) for k, v in res.items()})
