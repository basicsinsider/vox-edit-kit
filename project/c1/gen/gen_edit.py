import sys, re; sys.path.insert(0, "project/c1/gen")
from common import *; from beats_data import B; from scenes_data import S; from assets_data import A
bstarts = [b[0] for b in B]
def beats_of(s, e):
    ids = [f"C1B{i+1:03d}" for i, bs in enumerate(bstarts) if bs < e - 1e-6 and (bstarts[i+1] if i+1 < len(bstarts) else END) > s + 1e-6]
    return ids[0] if len(ids) == 1 else f"{ids[0]}–{ids[-1][4:]}"
GN = {"N": "NIGHT", "P": "PAPER", "G": "GRID"}
issues = []; scenes = []
for i, sc in enumerate(S):
    s = sc[0]; e = S[i+1][0] if i+1 < len(S) else END
    check_t(s)
    cues = [float(x) for x in re.findall(r"@(\d+\.\d\d)", sc[8])]
    for c in cues:
        check_t(c)
        if not (s - 0.01 <= c < e): issues.append(f"SC{i+1:03d} cue {c} outside {s}–{e}")
    for a in sc[7]:
        if a not in A: issues.append(f"SC{i+1:03d} unknown asset {a}")
    hold = e - max(cues) if cues else None
    scenes.append(dict(n=i+1, id=f"C1S{i+1:03d}", s=s, e=e, g=sc[1], tag=sc[2], why=sc[3], fx=sc[4], ref=sc[5], vis=sc[6], assets=sc[7], text=sc[8], cam=sc[9], out=sc[10], sfx=sc[11], hold=hold))
# transition fix-up: never the same type twice in a row (rotate alternatives)
ALT = ["HC", "W←", "PS", "FW", "W↓", "PT", "W→"]; k = 0
for a, b in zip(scenes, scenes[1:]):
    tya = "W" if a["out"].startswith("W") else a["out"]; tyb = "W" if b["out"].startswith("W") else b["out"]
    if tya == tyb and b["out"] != "end":
        nxt = scenes[scenes.index(b)+1]["out"] if scenes.index(b)+1 < len(scenes) else ""
        for j in range(len(ALT)):
            c = ALT[(k + j) % len(ALT)]; tc = "W" if c.startswith("W") else c
            tn = "W" if nxt.startswith("W") else nxt
            if tc != tya and tc != tn: break
        k += 1; b["out"] = c; b["fix"] = True
        if c.startswith("W") or c == "FW": b["sfx"] += f" · {b['e']-0.06:.2f} whoosh (transition)"
        elif c == "PS": b["sfx"] += f" · {b['e']-0.08:.2f} paper_slide (transition)"
# checks
run = 1
for a, b in zip(scenes, scenes[1:]):
    run = run + 1 if a["g"] == b["g"] else 1
    if run > 3: issues.append(f"ground run >3 at {b['id']}")
light = 0
for sc in scenes:
    light = light + 1 if sc["g"] in "PG" else 0
    if light > 3: issues.append(f"PAPER/GRID run >3 at {sc['id']}")
ty = lambda o: "W" if o.startswith("W") else o
for a, b in zip(scenes, scenes[1:]):
    if ty(a["out"]) == ty(b["out"]) and a["out"] not in ("end",): issues.append(f"same transition twice {a['id']}→{b['id']} ({a['out']})")
for sc in scenes:
    if sc["e"] - sc["s"] < 2.0: issues.append(f"short scene {sc['id']} {sc['e']-sc['s']:.2f}")
print("\n".join(issues) or "checks ok", len(scenes))
json_out = __import__("json"); json_out.dump([{k: v for k, v in sc.items()} for sc in scenes], open("project/c1/gen/scenes.json", "w"), indent=0)
