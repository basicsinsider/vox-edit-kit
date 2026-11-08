"""pys01 derived assets: footage trims (h264, 24 fps, no audio), the blurred fill for the X clip,
and simplified map paths (Paraguay + neighbours) in the kit's pixel spaces -> assets/paraguay/pys01/derived/maps.json.
Run from the repo root: .venv/bin/python project/paraguay/gen/pys01_assets.py [footage|maps]"""
import json, re, subprocess, sys, math
SH = "assets/paraguay/shared/footage/"
OUT = "assets/paraguay/pys01/"

TRIMS = [  # name, src, start, dur, vf
    ("x_congress_trim.mp4", SH + "x_congress_src.mp4", 2.6, 7.6, "scale=720:1280"),
    ("pena_resignation_trim.mp4", SH + "x_pena_resignation_msg.mp4", 20.0, 3.4, "scale=1920:1080"),
    ("pena_fiscalia_trim.mp4", SH + "uh_pena_enters_fiscalia.mp4", 14.6, 3.4, "scale=1350:736"),
    ("chaos_streets_trim.mp4", SH + "x_chaos_streets_jungle.mp4", 5.9, 3.8, "scale=854:480"),
    ("pension_sign_trim.mp4", SH + "x_mioriente_protestas.mp4", 40.7, 3.6, "scale=1280:720"),
]

def ff(args):
    print(" ".join(args)); subprocess.run(args, check=True)

def footage():
    for name, src, ss, d, vf in TRIMS:
        ff(["ffmpeg", "-v", "error", "-y", "-ss", str(ss), "-t", str(d), "-i", src, "-an", "-vf", vf + ",fps=24",
            "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p", "-movflags", "+faststart", OUT + "footage/" + name])
    # blurred, darkened full-frame fill of the X clip (cover crop 720x1280 -> 1920x1080)
    ff(["ffmpeg", "-v", "error", "-y", "-ss", "2.6", "-t", "7.6", "-i", SH + "x_congress_src.mp4", "-an", "-vf",
        "scale=1920:-2,crop=1920:1080:0:(ih-1080)/2,boxblur=28:2,eq=brightness=-0.16:saturation=0.75,fps=24",
        "-c:v", "libx264", "-preset", "medium", "-crf", "22", "-pix_fmt", "yuv420p", OUT + "footage/x_congress_fill.mp4"])

def paths(svg, ids, step):
    s = open(svg).read(); out = {}
    for cid in ids:
        d = re.search(r'<path id="%s"[^>]* d="([^"]+)"' % cid, s).group(1)
        res = []
        for sub in re.split(r"(?=M)", d):
            pts = [tuple(map(float, p)) for p in re.findall(r"(-?\d+\.?\d*),(-?\d+\.?\d*)", sub)]
            if len(pts) < 3: continue
            keep = [pts[0]]
            for p in pts[1:]:
                if math.dist(p, keep[-1]) >= step: keep.append(p)
            if len(keep) < 4: continue
            res.append("M" + " L".join("%.0f %.0f" % p for p in keep) + "Z")
        out[cid[2:]] = "".join(res)
    return out

def maps():
    J = {}
    J["py"] = paths("assets/maps/kit/paraguay_overlay.svg", ["c-paraguay", "c-brazil", "c-argentina", "c-bolivia"], 6)
    J["sa"] = paths("assets/maps/kit/south_america_overlay.svg", ["c-paraguay", "c-brazil", "c-argentina", "c-bolivia"], 3)
    for k in ("paraguay", "south_america"):
        J[k + "_places"] = {n: [round(v["x"], 1), round(v["y"], 1)] for n, v in json.load(open("assets/maps/kit/%s.json" % k))["places"].items()}
    json.dump(J, open(OUT + "derived/maps.json", "w"))
    for g in ("py", "sa"):
        print(g, {k: len(v) for k, v in J[g].items()})

if __name__ == "__main__":
    what = sys.argv[1:] or ["footage", "maps"]
    if "footage" in what: footage()
    if "maps" in what: maps()
