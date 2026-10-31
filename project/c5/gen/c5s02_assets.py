"""c5s02 derived assets: globe videos (C5S050 sat, C5S063 night), map crops, keyed RCA TV, country paths JSON.
Run: .venv/bin/python project/c5/gen/c5s02_assets.py [globes|maps|tv|paths|all]"""
import sys, json, re, math, subprocess, os
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
Image.MAX_IMAGE_PIXELS = None
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
K = ROOT + "/assets/maps/kit/"
OUT = ROOT + "/assets/c5/derived/c5s02/"
MADE = ROOT + "/assets/c5/made/"
os.makedirs(OUT, exist_ok=True); os.makedirs(MADE, exist_ok=True)

def load_draft(path, size):
    im = Image.open(path); im.draft("RGB", size); im = im.convert("RGB")
    if im.size != size: im = im.resize(size, Image.LANCZOS)
    return np.asarray(im)

def ease_cam(x):  # FX.ease.cam bezier(0.45,0,0.2,1)
    x = min(1, max(0, x)); x1, y1, x2, y2 = 0.45, 0, 0.2, 1
    t = x
    for _ in range(12):
        X = 3*(1-t)**2*t*x1 + 3*(1-t)*t*t*x2 + t**3
        dX = 3*(1-t)**2*x1 + 6*(1-t)*t*(x2-x1) + 3*t*t*(1-x2)
        if abs(X-x) < 1e-6 or dX == 0: break
        t -= (X-x)/dX; t = min(1, max(0, t))
    return 3*(1-t)**2*t*y1 + 3*(1-t)*t*t*y2 + t**3

def project(lon, lat, lon0, lat0, R, cx, cy, alt=0.0):
    l, p, l0, p0 = map(math.radians, (lon, lat, lon0, lat0))
    r = R*(1+alt)
    x = r*math.cos(p)*math.sin(l-l0)
    y = r*(math.cos(p0)*math.sin(p) - math.sin(p0)*math.cos(p)*math.cos(l-l0))
    z = math.sin(p0)*math.sin(p) + math.cos(p0)*math.cos(p)*math.cos(l-l0)
    vis = z > 0 or (x*x+y*y) > R*R
    return cx+x, cy-y, vis

def gc(a, b, n=120):
    (lo1, la1), (lo2, la2) = a, b
    v = lambda lo, la: np.array([math.cos(math.radians(la))*math.cos(math.radians(lo)), math.cos(math.radians(la))*math.sin(math.radians(lo)), math.sin(math.radians(la))])
    A, B = v(lo1, la1), v(lo2, la2); w = math.acos(np.clip(A@B, -1, 1)); pts = []
    for i in range(n+1):
        f = i/n; P = (math.sin((1-f)*w)*A + math.sin(f*w)*B)/math.sin(w)
        pts.append((math.degrees(math.atan2(P[1], P[0])), math.degrees(math.asin(P[2]))))
    return pts

def render_globe(tex, frames_fn, out, W=1920, H=1080, fps=24, bg=(13, 16, 20), night=False):
    th, tw = tex.shape[:2]
    p = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(fps), "-i", "-",
                          "-c:v", "libx264", "-crf", "17", "-preset", "medium", "-pix_fmt", "yuv420p", "-movflags", "+faststart", out], stdin=subprocess.PIPE)
    i = 0
    while True:
        st = frames_fn(i)
        if st is None: break
        lon0, lat0, R, cx, cy, draw = st
        img = np.empty((H, W, 3), np.uint8); img[:] = bg
        yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
        X = (xx-cx)/R; Y = (cy-yy)/R; rr = X*X+Y*Y
        m = rr < 1
        Z = np.sqrt(np.clip(1-rr, 0, 1))
        p0 = math.radians(lat0)
        # inverse orthographic
        lat = np.arcsin(np.clip(Z*math.sin(p0) + Y*math.cos(p0), -1, 1))
        lon = math.radians(lon0) + np.arctan2(X, Z*math.cos(p0) - Y*math.sin(p0))
        u = ((np.degrees(lon)+180) % 360)/360*(tw-1); v = (90-np.degrees(lat))/180*(th-1)
        s = tex[v[m].astype(np.int32), u[m].astype(np.int32)].astype(np.float32)
        shade = (0.35+0.65*Z[m]**0.6)[:, None] if not night else (0.55+0.45*Z[m]**0.5)[:, None]
        img[m] = np.clip(s*shade, 0, 255).astype(np.uint8)
        # atmosphere rim
        d = np.sqrt(rr)
        ring = np.clip(1-np.abs(d-1.0)/0.035, 0, 1)**2*(d > 0.97)
        glow = np.clip((1.12-d)/0.12, 0, 1)**3*(d >= 1)
        col = np.array([150, 185, 215] if not night else [90, 120, 170], np.float32)
        a = (ring*0.55 + glow*0.35)[..., None]
        img[:] = np.clip(img*(1-a) + col*a, 0, 255).astype(np.uint8)
        pim = Image.fromarray(img)
        if draw: draw(pim, lon0, lat0, R, cx, cy, i)
        p.stdin.write(pim.tobytes()); i += 1
    p.stdin.close(); p.wait(); print(out, i, "frames")

def globes():
    # C5S050: Washington -> Pakistan, scene 227.66-231.58; video starts at 227.50 (local c5 s)
    t0 = 227.50; n = int((231.80-t0)*24)+1
    tex = load_draft(K+"world_satdesat_21600.jpg", (5400, 2700))
    WAS, RWP = (-77.04, 38.9), (73.05, 33.6)
    route = gc(WAS, RWP, 160)
    def st50(i):
        if i >= n: return None
        t = t0 + i/24
        k = ease_cam((t-227.75)/2.75)
        lon0 = -80 + (69-(-80))*k + max(0, t-230.5)*0.6
        lat0 = 33 + (28-33)*k
        R = 600 - 40*k; cx, cy = 960, 590
        def draw(im, lon0, lat0, R, cx, cy, i):
            d = ImageDraw.Draw(im, "RGBA")
            f = min(1, max(0, (t-228.35)/2.0)); f = 1-(1-f)**2.2
            m = int(f*len(route))
            pts = []
            for j, (lo, la) in enumerate(route[:m]):
                alt = 0.10*math.sin(math.pi*j/len(route))
                x, y, vis = project(lo, la, lon0, lat0, R, cx, cy, alt)
                pts.append((x, y, vis))
            for a, b in zip(pts, pts[1:]):
                if a[2] and b[2]: d.line([a[:2], b[:2]], fill=(242, 237, 227, 235), width=5)
            # pin + halo on Pakistan after 230.84
            if t >= 230.80:
                x, y, vis = project(*RWP, lon0, lat0, R, cx, cy)
                age = t-230.80; r = 9 + 3*math.exp(-age*6)
                for q in range(2):
                    ph = ((age/1.4)+q*0.5) % 1
                    rr = 14+ph*70; d.ellipse([x-rr, y-rr*0.8, x+rr, y+rr*0.8], outline=(242, 237, 227, int(170*(1-ph))), width=3)
                d.ellipse([x-r, y-r, x+r, y+r], fill=(242, 237, 227, 255), outline=(20, 27, 36, 255), width=3)
            # start dot at Washington
            x, y, vis = project(*WAS, lon0, lat0, R, cx, cy)
            if vis and f > 0: d.ellipse([x-7, y-7, x+7, y+7], fill=(242, 237, 227, 220))
        return lon0, lat0, R, cx, cy, draw
    render_globe(tex, st50, MADE+"c5s02_globe_was_pak.mp4")
    x, y, _ = project(*RWP, 69, 28, 560, 960, 590); print("RWP end px", x, y)
    del tex
    # C5S063: night globe, 284.03-287.63; video from 283.90
    t1 = 283.90; n2 = int((287.85-t1)*24)+1
    tex = load_draft(ROOT+"/_tmp/c5s02/bm.jpg", (6750, 3375))
    tex = np.clip(tex.astype(np.float32)*1.25 + 4, 0, 255).astype(np.uint8)
    BEI = (116.4, 39.9); route2 = gc(RWP, BEI, 120)
    def st63(i):
        if i >= n2: return None
        t = t1 + i/24
        lon0 = 84 + (t-t1)*2.2; lat0 = 24; R = 720; cx, cy = 980, 700
        def draw(im, lon0, lat0, R, cx, cy, i):
            d = ImageDraw.Draw(im, "RGBA")
            f = min(1, max(0, (t-284.30)/2.1)); f = 1-(1-f)**2
            m = int(f*len(route2))
            for j in range(0, m-1, 3):
                alt = 0.05*math.sin(math.pi*j/len(route2))
                x, y, v = project(*route2[j], lon0, lat0, R, cx, cy, alt)
                d.ellipse([x-2.6, y-2.6, x+2.6, y+2.6], fill=(242, 237, 227, 200))
            if m > 1:
                j = m-1; alt = 0.05*math.sin(math.pi*j/len(route2))
                x, y, v = project(*route2[j], lon0, lat0, R, cx, cy, alt)
                d.ellipse([x-6, y-6, x+6, y+6], fill=(242, 237, 227, 240))
        return lon0, lat0, R, cx, cy, draw
    render_globe(tex, st63, MADE+"c5s02_globe_night_route.mp4", bg=(8, 9, 12), night=True)

def crop_save(src, box, out, size=None, q=88):
    im = Image.open(src); im = im.crop(box)
    if size: im = im.resize(size, Image.LANCZOS)
    im.convert("RGB").save(out, quality=q); print(out, im.size)

def maps():
    # world (16384 px, 45.5111 px/deg) and blue marble 21600 (60 px/deg)
    # South Asia -> Taiwan strip (satdesat, 60 px/deg): lon 55-130, lat 45-5 -> 4500x2400, saved at 0.75 = 45 px/deg
    crop_save(K+"world_satdesat_21600.jpg", (int((55+180)*60), int((90-45)*60), int((130+180)*60), int((90-5)*60)), OUT+"sasia_sat.jpg", (3375, 1800))
    # Asia atlas for the tilted D10 route (world_atlas, lon 60-125, lat 50-15)
    s = 45.5111
    crop_save(K+"world_atlas.jpg", (int(240*s), int(40*s), int(305*s), int(75*s)), OUT+"asia_atlas.jpg")
    # beige world (R11) lon -130..160, lat 78..5 at half res (22.76 px/deg)
    crop_save(K+"world_atlas.jpg", (int(50*s), int(12*s), int(340*s), int(85*s)), OUT+"world_beige.jpg", (int(290*s/2), int(73*s/2)))
    # NE Asia detail (full 45.5 px/deg) lon 100..145, lat 60..35
    crop_save(K+"world_atlas.jpg", (int(280*s), int(30*s), int(325*s), int(55*s)), OUT+"neasia_beige.jpg")
    # Pacific atlas half size (22 px/deg)
    crop_save(K+"pacific_atlas.jpg", (0, 0, 6380, 2420), OUT+"pacific_atlas_half.jpg", (3190, 1210))
    # US night ghost
    crop_save(K+"us_night.jpg", (0, 0, 6392, 3524), OUT+"us_night_2400.jpg", (2400, 1323))
    # Peking on far_east_1943 (Peiping ~ 3690,1800)
    crop_save(K+"scans/far_east_1943.jpg", (2490, 1000, 4890, 2500), OUT+"peking_far_east_1943.jpg")

def tv():
    im = Image.open(ROOT+"/_tmp/c5s02/rca_xl100.jpg").convert("RGBA")
    W, H = im.size; cx, cy, a, b, n = 521, 417, 404, 314, 4.2
    yy, xx = np.mgrid[0:H, 0:W]
    v = np.abs((xx-cx)/a)**n + np.abs((yy-cy)/b)**n
    alpha = np.clip((v-1)/0.02, 0, 1)*255
    arr = np.asarray(im).copy(); arr[..., 3] = alpha.astype(np.uint8)
    Image.fromarray(arr).save(ROOT+"/assets/c5/screens/rca_xl100_frame.png")
    json.dump({"image": "rca_xl100_frame.png", "width": W, "height": H, "screen_bbox": [cx-a, cy-b, 2*a, 2*b],
               "screen_shape": {"type": "superellipse", "cx": cx, "cy": cy, "a": a, "b": b, "n": n},
               "source": "https://commons.wikimedia.org/wiki/File:RCA_XL-100_20110627.jpg", "licence": "CC BY-SA 3.0"},
              open(ROOT+"/assets/c5/screens/rca_xl100_frame_screen.json", "w"), indent=1)
    print("tv ok")

USSR = ["russia", "ukraine", "belarus", "kazakhstan", "uzbekistan", "turkmenistan", "kyrgyzstan", "tajikistan", "georgia", "armenia",
        "azerbaijan", "moldova", "lithuania", "latvia", "estonia"]
def paths():
    svg = open(K+"world_overlay.svg").read()
    get = lambda cid: re.search(r'<path id="c-%s"[^>]* d="([^"]+)"' % cid, svg).group(1)
    s = 45.5111
    def conv(d, fx, fy, minstep=2.5):
        out = []
        for sub in d.split("M")[1:]:
            pts = [tuple(map(float, q.split(","))) for q in re.split(r"[LZz]", sub) if "," in q]
            pts = [(fx(x), fy(y)) for x, y in pts]
            keep = [pts[0]]
            for p in pts[1:]:
                if math.hypot(p[0]-keep[-1][0], p[1]-keep[-1][1]) >= minstep: keep.append(p)
            if len(keep) < 4: continue
            if any(abs(a[0]-b[0]) > 400 for a, b in zip(keep, keep[1:])): continue
            out.append("M" + "L".join("%.0f %.0f" % p for p in keep) + "Z")
        return "".join(out)
    J = {}
    # sasia_sat space: 45 px/deg, lon0 55, lat0 45
    fx = lambda x: (x/s-180-55)*45; fy = lambda y: (90-y/s-45)*-45*-1
    fy = lambda y: (45-(90-y/s))*45
    J["sasia"] = {k: conv(get(k), fx, fy) for k in ["india", "pakistan", "china", "taiwan"]}
    # asia_atlas: native world px offset (240*s, 40*s)
    fx = lambda x: x-int(240*s); fy = lambda y: y-int(40*s)
    J["asia"] = {k: conv(get(k), fx, fy, 4) for k in ["pakistan", "china"]}
    # world_beige: offset (50*s, 12*s), half scale
    fx = lambda x: (x-int(50*s))/2; fy = lambda y: (y-int(12*s))/2
    J["world"] = {"ussr": "".join(conv(get(k), fx, fy, 3) for k in USSR), "china": conv(get("china"), fx, fy, 3),
                  "usa": conv(get("united_states_of_america"), fx, fy, 3)}
    fx = lambda x: x-int(280*s); fy = lambda y: y-int(30*s)
    J["neasia"] = {"ussr": conv(get("russia"), fx, fy, 7), "china": conv(get("china"), fx, fy, 3)}
    # us_night_2400: us.json x=(lon+126)*106.533, y=(50-lat)*133 scaled 2400/6392
    us = open(K+"us_overlay.svg").read()
    d = re.search(r'<path id="c-united_states_of_america"[^>]* d="([^"]+)"', us)
    k = 2400/6392
    J["us"] = {"usa": conv(d.group(1), lambda x: x*k, lambda y: y*k, 3) if d else ""}
    json.dump(J, open(OUT+"c5s02_paths.json", "w"))
    print({a: {b: len(c) for b, c in v.items()} for a, v in J.items()})

if __name__ == "__main__":
    w = sys.argv[1] if len(sys.argv) > 1 else "all"
    if w in ("tv", "all"): tv()
    if w in ("paths", "all"): paths()
    if w in ("maps", "all"): maps()
    if w in ("globes", "all"): globes()
