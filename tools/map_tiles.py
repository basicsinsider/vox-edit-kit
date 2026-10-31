"""Fetch + mosaic XYZ tiles (AWS terrarium elevation or Esri World Imagery) for the map kit.
Library + CLI:  map_tiles.py fetch terr|esri z lon0 lat0 lon1 lat1
Tiles cached in /tmp/mk/tiles/<src>/z_x_y.(png|jpg).  Used by tools/map_kit.py."""
import sys, math, os, subprocess
from concurrent.futures import ThreadPoolExecutor
CACHE = os.environ.get("MK_CACHE", "/tmp/mk/tiles")
URL = {"terr": "https://s3.amazonaws.com/elevation-tiles-prod/terrarium/{z}/{x}/{y}.png",
       "esri": "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}"}
EXT = {"terr": "png", "esri": "jpg"}
def tx(lon, z): return (lon + 180) / 360 * 2 ** z
def ty(lat, z):
    r = math.radians(lat); return (1 - math.log(math.tan(r) + 1 / math.cos(r)) / math.pi) / 2 * 2 ** z
def path(src, z, x, y): return f"{CACHE}/{src}/{z}_{x}_{y}.{EXT[src]}"
def tiles(z, lon0, lat0, lon1, lat1):
    n = 2 ** z
    xs = range(int(tx(lon0, z)), int(tx(lon1, z)) + 1)
    ys = range(max(0, int(ty(lat1, z))), min(n - 1, int(ty(lat0, z))) + 1)
    return [(x % n, y) for x in xs for y in ys]
def fetch(src, z, lon0, lat0, lon1, lat1, workers=24):
    os.makedirs(f"{CACHE}/{src}", exist_ok=True)
    todo = [(x, y) for x, y in tiles(z, lon0, lat0, lon1, lat1) if not os.path.exists(path(src, z, x, y))]
    def get(t):
        x, y = t; p = path(src, z, x, y)
        for _ in range(4):
            if subprocess.run(["curl", "-sf", "-m", "60", "-o", p + ".part", URL[src].format(z=z, x=x, y=y)]).returncode == 0:
                os.replace(p + ".part", p); return
    print(f"{src} z{z}: {len(todo)} tiles to fetch", flush=True)
    with ThreadPoolExecutor(workers) as ex: list(ex.map(get, todo))
if __name__ == "__main__":
    if sys.argv[1] == "fetch":
        fetch(sys.argv[2], int(sys.argv[3]), *map(float, sys.argv[4:8])); print("done")
