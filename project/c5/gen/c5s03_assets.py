"""c5s03 derived assets: Taiwan Strait Esri z10 mosaic (Web Mercator, unresampled) + json pixel formula.
Run: MK_CACHE=/tmp/c5s03/tiles python3 tools/map_tiles.py fetch esri 10 117.3 21.9 122.3 26.6 ; python3 project/c5/gen/c5s03_assets.py strait"""
import sys, os, json, math
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../../tools"))
from PIL import Image
import map_tiles as mt
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
def strait():
    z, lon0, lat0, lon1, lat1 = 10, 117.3, 21.9, 122.3, 26.6
    X0, X1 = int(mt.tx(lon0, z)), int(mt.tx(lon1, z)); Y0, Y1 = int(mt.ty(lat1, z)), int(mt.ty(lat0, z))
    W, H = (X1 - X0 + 1) * 256, (Y1 - Y0 + 1) * 256
    im = Image.new("RGB", (W, H)); miss = 0
    for X in range(X0, X1 + 1):
        for Y in range(Y0, Y1 + 1):
            try: im.paste(Image.open(mt.path("esri", z, X, Y)).convert("RGB"), ((X - X0) * 256, (Y - Y0) * 256))
            except Exception: miss += 1
    out = f"{ROOT}/assets/c5/made/strait_esri_z10.jpg"; im.save(out, quality=90)
    P = {"kinmen": (118.3171, 24.4321), "matsu": (119.95, 26.16), "xiamen": (118.0894, 24.4798), "fuzhou": (119.2965, 26.0745),
         "taipei": (121.5654, 25.033), "kaohsiung": (120.3014, 22.6273), "penghu": (119.5664, 23.5655), "taiwan_centre": (120.95, 23.75)}
    places = {k: {"lon": a, "lat": b, "x": round((mt.tx(a, z) - X0) * 256, 1), "y": round((mt.ty(b, z) - Y0) * 256, 1)} for k, (a, b) in P.items()}
    json.dump({"image": "strait_esri_z10.jpg", "width": W, "height": H, "zoom": z, "tiles": [X0, X1, Y0, Y1], "missing": miss,
               "formula": f"x=((lon+180)/360*2^{z}-{X0})*256 ; y=(mercY(lat)*2^{z}-{Y0})*256", "places": places,
               "credit": "Imagery: Esri, Maxar, Earthstar Geographics"}, open(out.replace(".jpg", ".json"), "w"), indent=1)
    print(W, H, miss, places)

def twmask():
    """Taiwan land mask in the strait mosaic pixel space (white + alpha), from the imagery itself (sea = dark blue)."""
    import numpy as np
    from PIL import ImageFilter
    im = np.asarray(Image.open(f"{ROOT}/assets/c5/made/strait_esri_z10.jpg").convert("RGB")).astype(np.float32)
    r, g, b = im[..., 0], im[..., 1], im[..., 2]
    land = (g > b * 1.02) | ((r + g + b) / 3 > 75)
    H, W = land.shape
    keep = np.zeros_like(land); keep[1100:3950, 2050:3600] = True       # Taiwan main island box only
    from scipy import ndimage
    lk = ndimage.binary_opening(land & keep, iterations=3); lab, n = ndimage.label(lk)
    sizes = ndimage.sum(lk, lab, range(1, n + 1)); lk = lab == (1 + int(np.argmax(sizes)))      # biggest blob = main island
    lk = ndimage.binary_fill_holes(ndimage.binary_closing(lk, iterations=6))
    m = Image.fromarray((lk * 255).astype("uint8")).filter(ImageFilter.GaussianBlur(1.5))
    out = Image.new("RGBA", (W, H), (255, 255, 255, 0)); out.putalpha(m)
    out.save(f"{ROOT}/assets/c5/made/strait_taiwan_mask.png", optimize=True); print("mask ok")

if __name__ == "__main__": globals()[sys.argv[1]]()
