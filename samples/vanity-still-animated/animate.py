"""Animate the user's vanity-mirror illustration into a 5 s shot (1920x1080, 30 fps).

Every frame is computed from the single still:
  - the Gemini sparkle watermark (bottom right) is inpainted away once;
  - blinks are painted onto the eyes (she and both reflections blink together);
  - small, smoothly masked warps add breathing, a slow head nod, and the reflection's fingers working the earring;
  - a slow camera push-in, plus a few dust motes drifting in the lamplight.

usage: python animate.py src.jpg out.mp4 [--frames-at 0.5,1.45]   (needs numpy + opencv-python-headless + ffmpeg)
"""
import math, subprocess, sys
import numpy as np
import cv2

W, H, FPS, DUR = 1920, 1080, 30, 5.0
SS = 4  # supersampling for painted eyelids

def smoothstep(e0, e1, x):
    t = np.clip((x - e0) / (e1 - e0), 0, 1)
    return t * t * (3 - 2 * t)

def ease(x):
    x = min(1.0, max(0.0, x))
    return x * x * (3 - 2 * x)

def remove_watermark(img):
    # sparkle sits at ~(2638, 1422) on a 2752x1536 image; mask its light pixels and inpaint
    x0, y0, x1, y1 = 2590, 1375, 2690, 1470
    roi = img[y0:y1, x0:x1]
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY).astype(np.int16)
    bg = cv2.medianBlur(gray.astype(np.uint8), 41).astype(np.int16)
    m = ((gray - bg) > 10).astype(np.uint8) * 255          # the semi-transparent sparkle is lighter than its surroundings
    n, lab, stats, _ = cv2.connectedComponentsWithStats(m)
    keep = 1 + int(np.argmax(stats[1:, cv2.CC_STAT_AREA])) if n > 1 else 0
    m = ((lab == keep) * 255).astype(np.uint8)
    m = cv2.dilate(m, np.ones((15, 15), np.uint8))
    mask = np.zeros(img.shape[:2], np.uint8)
    mask[y0:y1, x0:x1] = m
    return cv2.inpaint(img, mask, 9, cv2.INPAINT_TELEA), int((m > 0).sum())

# eyes in source pixels: corners P0, P2 and quadratic controls for the upper / lower lid
EYES = [
    dict(p0=(730, 533), p2=(778, 528), up=(752, 507), lo=(756, 551), lid=(735, 776, 503, 511)),   # reflection, left
    dict(p0=(846, 512), p2=(888, 505), up=(867, 493), lo=(868, 531), lid=(850, 884, 488, 496)),   # reflection, right
    dict(p0=(1622, 472), p2=(1648, 470), up=(1635, 459), lo=(1636, 488), lid=(1624, 1646, 449, 456)),  # her eye (profile)
]

def qpts(p0, c, p2, n=24):
    t = np.linspace(0, 1, n)[:, None]
    p0, c, p2 = map(np.array, (p0, c, p2))
    return (1 - t) ** 2 * p0 + 2 * (1 - t) * t * c + t ** 2 * p2

def paint_blink(img, e, b, lid_col, lash_col):
    if b <= 0.01:
        return
    (x0, y0), (x2, y2) = e["p0"], e["p2"]
    bx0, by0 = min(x0, x2) - 12, min(e["up"][1], y0, y2) - 10
    bx1, by1 = max(x0, x2) + 12, max(e["lo"][1], y0, y2) + 10
    patch = img[by0:by1, bx0:bx1]
    ph, pw = patch.shape[:2]
    big = cv2.resize(patch, (pw * SS, ph * SS), interpolation=cv2.INTER_CUBIC)
    off = np.array([bx0, by0])
    edge_c = (e["up"][0] + (e["lo"][0] - e["up"][0]) * b, e["up"][1] + (e["lo"][1] - e["up"][1]) * b * 0.92)
    upper = qpts(e["p0"], (e["up"][0], e["up"][1] - 3), e["p2"])
    edge = qpts(e["p0"], edge_c, e["p2"])
    poly = np.vstack([upper, edge[::-1]])
    pts = ((poly - off) * SS).astype(np.int32)
    lid = big.copy()
    cv2.fillPoly(lid, [pts], lid_col, lineType=cv2.LINE_AA)
    a = np.zeros(big.shape[:2], np.float32)
    cv2.fillPoly(a, [pts], 1.0, lineType=cv2.LINE_AA)
    a = cv2.GaussianBlur(a, (0, 0), SS * 0.6)[..., None]
    big = (big * (1 - a) + lid * a).astype(np.uint8)
    ep = ((edge - off) * SS).astype(np.int32)
    cv2.polylines(big, [ep], False, lash_col, thickness=int(SS * (2.0 + 1.6 * b)), lineType=cv2.LINE_AA)
    img[by0:by1, bx0:bx1] = cv2.resize(big, (pw, ph), interpolation=cv2.INTER_AREA)

def blink_curve(t, t0):
    if t < t0 or t > t0 + 0.2:
        return 0.0
    return (t - t0) / 0.08 if t < t0 + 0.08 else max(0.0, 1 - (t - t0 - 0.08) / 0.12)

def main():
    src_path, out_path = sys.argv[1], sys.argv[2]
    stills = []
    if "--frames-at" in sys.argv:
        stills = [float(v) for v in sys.argv[sys.argv.index("--frames-at") + 1].split(",")]
    src = cv2.imread(src_path)
    SH, SW = src.shape[:2]
    src, npx = remove_watermark(src)
    print(f"source {SW}x{SH}, watermark pixels inpainted: {npx}")

    cols = []
    for e in EYES:
        x0, x1, y0, y1 = e["lid"]
        cols.append(tuple(int(v) for v in np.median(src[y0:y1, x0:x1].reshape(-1, 3), axis=0)))
    lash = (30, 42, 74)  # BGR warm dark brown, like the drawing's lash lines

    u, v = np.meshgrid(np.arange(W, dtype=np.float32), np.arange(H, dtype=np.float32))

    # dust motes (seeded)
    rng = np.random.default_rng(1108)
    motes = [dict(x=rng.uniform(300, 1700), y=rng.uniform(80, 900), r=rng.uniform(1.0, 2.6),
                  sp=rng.uniform(.4, 1.0), ph=rng.uniform(0, 6.28), a=rng.uniform(.15, .4)) for _ in range(26)]

    def region(x, y, cx, cy, rx, ry, inner=.5):
        r = np.sqrt(((x - cx) / rx) ** 2 + ((y - cy) / ry) ** 2)
        return 1 - smoothstep(inner, 1.0, r)

    def rot_disp(x, y, px, py, ang):
        c, s = math.cos(ang), math.sin(ang)
        dx, dy = x - px, y - py
        return (c * dx - s * dy) - dx, (s * dx + c * dy) - dy

    def frame(t):
        img = src.copy()
        b = max(blink_curve(t, 1.35), blink_curve(t, 3.85))
        for e, col in zip(EYES, cols):
            paint_blink(img, e, b, col, lash)

        # camera: slow push-in toward the space between her and her reflection
        k = ease(t / DUR)
        cw0 = SH * 16 / 9; cw1 = cw0 / 1.075
        cw = cw0 + (cw1 - cw0) * k; ch = cw * 9 / 16
        cx = SW / 2 + (1280 - SW / 2) * k; cy = SH / 2 + (700 - SH / 2) * k
        cx = min(max(cx, cw / 2), SW - cw / 2); cy = min(max(cy, ch / 2), SH - ch / 2)
        x = (cx - cw / 2) + u * (cw / W); y = (cy - ch / 2) + v * (ch / H)

        breath = 0.5 - 0.5 * math.cos(2 * math.pi * t / 3.4)
        nod = ease(t / 4.2) * 0.9 + 0.25 * math.sin(2 * math.pi * t / 2.6)   # degrees, gentle
        fid = math.sin(2 * math.pi * t * 0.9) * smoothstep(0.3, 1.0, t) * (1 - smoothstep(4.4, 5.0, t))
        dx = np.zeros_like(x); dy = np.zeros_like(y)

        # her head and hair: forward nod about the neck
        w = region(x, y, 1760, 400, 340, 400)
        rx_, ry_ = rot_disp(x, y, 1760, 760, math.radians(-nod))
        dx += w * rx_; dy += w * ry_
        # her shoulders / chest: breathing
        w = region(x, y, 1900, 1050, 520, 460, .35)
        dy += w * (-3.2 * breath)
        # her hand on her cheek: a slight press
        w = region(x, y, 1620, 760, 90, 150)
        dy += w * (-1.2 * fid)
        # reflection (centre mirror): nod reads as a small drop of the face; breathing; fingers at the earring
        w = region(x, y, 800, 440, 220, 290)
        dy += w * (1.8 * nod / 0.9 * 0.6); dx += w * (-0.5 * nod)
        w = region(x, y, 820, 930, 270, 230, .35)
        dy += w * (-2.4 * breath)
        w = region(x, y, 950, 630, 85, 135, .45)
        hx, hy = rot_disp(x, y, 975, 800, math.radians(1.6 * fid))
        dx += w * hx; dy += w * hy
        # side mirror (back view): follows the nod and breath
        w = region(x, y, 1350, 470, 150, 220)
        dy += w * (1.4 * nod / 0.9 * 0.6)
        w = region(x, y, 1360, 860, 190, 200, .35)
        dy += w * (-2.0 * breath)

        out = cv2.remap(img, (x - dx).astype(np.float32), (y - dy).astype(np.float32),
                        cv2.INTER_CUBIC, borderMode=cv2.BORDER_REFLECT)

        # dust motes in the warm light
        glow = np.zeros((H, W), np.float32)
        for m in motes:
            my = (m["y"] - t * 18 * m["sp"]) % 900 + 60
            mx = m["x"] + math.sin(t * m["sp"] + m["ph"]) * 14
            cv2.circle(glow, (int(mx * 4), int(my * 4)), int(m["r"] * 4),
                       m["a"] * (.6 + .4 * math.sin(t * 1.6 + m["ph"])), -1, cv2.LINE_AA, 2)
        glow = cv2.GaussianBlur(glow, (0, 0), 1.6)[..., None]
        warm = np.array([180, 225, 255], np.float32)
        out = np.clip(out + glow * warm, 0, 255).astype(np.uint8)
        return out

    if stills:
        for t in stills:
            cv2.imwrite(out_path.replace(".mp4", f"_t{t:.2f}.png"), frame(t))
        return
    ff = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", f"{W}x{H}",
                           "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-crf", "15", "-preset", "slow",
                           "-pix_fmt", "yuv420p", "-movflags", "+faststart", out_path], stdin=subprocess.PIPE)
    n = int(DUR * FPS)
    for i in range(n):
        ff.stdin.write(frame(i / FPS).tobytes())
    ff.stdin.close(); ff.wait()
    print("wrote", out_path, n, "frames")

if __name__ == "__main__":
    main()
