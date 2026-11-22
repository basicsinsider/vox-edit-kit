# circle-portrait crops for cts03 scene D (fix #11): whole head + a bit of shoulder in a square, face centred.
# Where the source photo is tighter than the square, the margin is a blurred, enlarged copy of the same photo
# (a "blurred fill", background only) and the sharp photo is feathered into it.
import sys
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
R = "/home/user/vox-edit-kit/"
OUT = R + "assets/cartels/cts03/derived/"
N = 480
def make(src, box, side, cy=0.5):
    """sharp crop `box` (inside the photo) placed in a `side`-px square; margins = edge-extended + blurred photo"""
    im = np.asarray(Image.open(src).convert("RGB"))
    l, t, r, b = box
    sharp = im[t:b, l:r]
    h, w = sharp.shape[:2]
    x0 = (side - w) // 2; y0 = int((side - h) * cy)
    pad = ((y0, side - h - y0), (x0, side - w - x0), (0, 0))
    bg = Image.fromarray(np.pad(sharp, pad, mode="edge")).filter(ImageFilter.GaussianBlur(side * 0.03))
    f = max(2, int(min(w, h) * 0.05))
    m = Image.new("L", (side, side), 0)
    ImageDraw.Draw(m).rectangle((x0 + (f if x0 > 0 else -9), y0 + (f if y0 > 0 else -9),
                                 x0 + w - 1 - (f if x0 + w < side else -9), y0 + h - 1 - (f if y0 + h < side else -9)), fill=255)
    m = m.filter(ImageFilter.GaussianBlur(f / 2))
    bg.paste(Image.fromarray(np.pad(sharp, pad, mode="edge")), (0, 0), m)
    return bg.resize((N, N), Image.LANCZOS)
SPEC = {
    # name: (source, sharp crop box, square side in source px, vertical placement)
    "arturo": (R + "assets/cartels/people/arturo_beltranleyva_1.jpg", (12, 0, 136, 124), 124, 1.0),
    "alfredo": (R + "assets/cartels/cts03/photos/src_eluniversal_alfredo_2008.jpg", (670, 0, 1210, 560), 600, 1.0),
    "hector": (R + "assets/cartels/people/hector_beltranleyva_mugshot_3.jpg", (16, 0, 300, 400), 430, 1.0),
    "isidro": (R + "assets/cartels/people/meza_fbi_photo_hires_2.jpg", (0, 0, 1515, 1900), 1960, 0.0),
}
prev = Image.new("RGB", (4 * (N + 20), N + 20), (30, 30, 30))
for i, (k, (src, box, side, cy)) in enumerate(SPEC.items()):
    c = make(src, box, side, cy)
    if len(sys.argv) > 1 and sys.argv[1] == "write":
        c.save(OUT + "circ_" + k + ".jpg", quality=92)
    m = Image.new("L", (N, N), 0); ImageDraw.Draw(m).ellipse((0, 0, N - 1, N - 1), fill=255)
    prev.paste(c, (i * (N + 20) + 10, 10), m)
prev.save("/tmp/claude-0/-home-user-vox-edit-kit/15480379-9930-57a9-90a2-05a2b08ccf1a/scratchpad/circ.jpg")
