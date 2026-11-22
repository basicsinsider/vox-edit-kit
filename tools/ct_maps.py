"""US vs Cartels project (2026-11-22) map regions — built through tools/map_kit.py (unchanged; entries added at runtime,
the pattern of NVIDIA's nv_maps.py) plus Cartels-only extras:
  * a 3rd relief style "relief" (pale-grey 3D-relief land on a dark slate sea, strong hillshade — for the "3D relief, one region
    highlighted" look, inspo ast_d02865717c824c47) + `<region>_height.png` (8-bit heightmap, 0..4000 m to 0..255, sea 0)
  * Mexican states `#st-<state>` + US states `#us-<state>` (NE admin-1 / us-atlas on the wide maps; OpenStreetMap clipped to the
    landmask on the close-ups), highways `#hwy-mex15` (+ `#hwy-mex15-north`, `#hwy-mex45`) from the OSM route relations,
    the US–Mexico border line `#b-us_mexico`, municipalities `#mun-*` and regions `#rg-*`.
Usage:  .venv/bin/python tools/ct_maps.py <region> [relief,sat,overlay]   regions: north_america mexico sinaloa chihuahua
        .venv/bin/python tools/ct_maps.py aerial <name>...                (see AERIALS)
Env:    MK_CACHE (tiles, default work/mapC/tiles), MK_VEC (NE/world-atlas vectors, work/mapC/vec), MK_OSM (OSM JSONs, work/mapC/osm).
Data fetched with tools/map_tiles.py + Nominatim lookups / OSM API relation/<id>/full.json (see assets/maps/kit/README.md)."""
import sys, os, json, math, re, heapq
from collections import defaultdict
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("MK_CACHE", f"{ROOT}/work/mapC/tiles")
os.environ.setdefault("MK_VEC", f"{ROOT}/work/mapC/vec")
os.environ.setdefault("MK_OSM", f"{ROOT}/work/mapC/osm")
sys.path.insert(0, os.path.join(ROOT, "tools"))
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
import map_kit as mk

REGIONS = {
  # US + Mexico + Central America + Caribbean + Venezuela/Colombia coast: boats, Caracas to New York, routes north
  "north_america": dict(lon0=-125, lon1=-58, lat0=5, lat1=50, ppd=120, k=0.8870, zt=8, ze=8, zf=10),
  # all Mexico + US border states (state borders, Mex 15, Sierra Madre Occidental)
  "mexico": dict(lon0=-118, lon1=-86, lat0=14, lat1=36, ppd=200, k=0.9063, zt=9, ze=8, zf=6, pre_blur=True),
  # northern Sinaloa + southern Sonora close-up (Culiacan to Guasave to Los Mochis to Navojoa), coast, Mex 15, foothills
  "sinaloa": dict(lon0=-110.0, lon1=-106.8, lat0=24.5, lat1=27.4, ppd=1400, k=0.8988, zt=12, ze=12, zf=1.8, gray_mask=12),
  # Chihuahua state: Sierra Tarahumara, Chihuahua city, Juarez/El Paso, the Texas/New Mexico line
  "chihuahua": dict(lon0=-109.3, lon1=-103.0, lat0=25.4, lat1=32.4, ppd=700, k=0.8746, zt=11, ze=11, zf=2.6, pre_blur=True, gray_mask=11),
}
# lon, lat — towns from Nominatim (OSM place nodes, 2026-11-22); sites from OSM objects / Wikipedia (noted)
PLACES = {
  "guasave": (-108.46747, 25.57380), "culiacan": (-107.39339, 24.79790), "los_mochis": (-108.99019, 25.79281),
  "ahome": (-109.17860, 25.91880), "guamuchil": (-108.07554, 25.45755), "navolato": (-107.69797, 24.76330),
  "topolobampo": (-109.05431, 25.60136), "el_fuerte": (-108.61726, 26.41555), "mazatlan": (-106.42084, 23.20358),
  "navojoa": (-109.44382, 27.07219), "ciudad_obregon": (-109.93378, 27.48466), "hermosillo": (-110.96922, 29.09482),
  "guaymas": (-110.89941, 27.92164), "nogales_sonora": (-110.94505, 31.32851), "tubutama": (-111.46312, 30.88436),
  "chihuahua_city": (-106.07675, 28.63687), "ciudad_juarez": (-106.48321, 31.73897), "guachochi": (-107.07473, 26.81932),
  "creel": (-107.63435, 27.75302), "parral": (-105.66741, 26.92872), "cuauhtemoc_chih": (-106.86653, 28.40096),
  "mexico_city": (-99.13321, 19.43262), "guadalajara": (-103.33840, 20.67204), "tapalpa": (-103.75760, 19.94490),
  "monterrey": (-100.31526, 25.68020), "tijuana": (-117.03712, 32.53648), "puerto_vallarta": (-105.22031, 20.64072),
  "morelia": (-101.19238, 19.70271), "el_paso": (-106.48705, 31.76010), "tucson": (-110.97485, 32.22288),
  "nogales_arizona": (-110.93608, 31.34021), "phoenix": (-112.07414, 33.44844), "san_diego": (-117.16383, 32.71571),
  "las_cruces": (-106.77981, 32.31404), "albuquerque": (-106.65099, 35.08410), "san_antonio": (-98.49514, 29.42460),
  "doral": (-80.35533, 25.81954), "havana": (-82.35896, 23.13530), "caracas": (-66.91460, 10.50609), "bogota": (-74.08363, 4.65338),
  "panama_city": (-79.53418, 8.97145), "guatemala_city": (-90.51328, 14.64161), "san_salvador": (-89.19116, 13.69763),
  "tegucigalpa": (-87.20471, 14.10581), "managua": (-86.25000, 12.11000), "san_jose_cr": (-84.07967, 9.93274),
  "santo_domingo": (-69.89184, 18.47139), "port_au_prince": (-72.33880, 18.54250), "kingston": (-76.79281, 17.97121),
  "san_juan_pr": (-66.10570, 18.46550), "port_of_spain": (-61.51802, 10.65727), "maracaibo": (-71.64436, 10.64981),
  "cartagena": (-75.54417, 10.42656), "barranquilla": (-74.82318, 11.01019),
  # sites
  "kuroda_park": (-108.47593, 25.58140),            # stadium, Guasave (Wikipedia coords = OSM way 119684549 "Estadio Carranza Limon", renamed 2021)
  "davis_monthan_afb": (-110.88329, 32.16614),      # airfield (OSM aerodrome R19869181); JIATF-CC HQ (building not located)
  "davis_monthan_afb_area": (-110.81496, 32.15736), # centre of the whole base area incl. the AMARG "boneyard" (OSM landuse R14056461)
  "palacio_nacional": (-99.13127, 19.43255), "zocalo": (-99.13321, 19.43262),
}
mk.PLACES.update(PLACES)
for _n in ("new_york", "washington_dc", "miami", "houston", "los_angeles", "chicago", "dallas", "austin", "atlanta"):
    assert _n in mk.PLACES
CREDIT_OSM = "OpenStreetMap contributors (ODbL)"

# ---------------------------------------------------------------- helpers
def osm_polys(key):
    return mk.osm_geo(key)
def poly_mask(R, W, H, polys):
    im = Image.new("L", (W, H), 0); d = ImageDraw.Draw(im)
    for poly in polys:
        for i, r in enumerate(poly):
            pts = mk.ring_px(R, r, 0)  # sh=0: map_kit's ring_px would shift rings west of lon0 by +360 (Pacific hack)
            if len(pts) > 2: d.polygon(pts, fill=255 if i == 0 else 0)
    return np.asarray(im) > 127
def mask_paths(m, tol=0.8, min_len=4):
    """binary mask to SVG path d (closed contours; use fill-rule evenodd)."""
    from skimage import measure
    pm = np.pad(m.astype(np.float32), 1)
    out = []
    for c in measure.find_contours(pm, 0.5):
        c = measure.approximate_polygon(c, tol)
        if len(c) < min_len: continue
        out.append("M" + "L".join(f"{x - 1:.1f},{y - 1:.1f}" for y, x in c) + "Z")
    return "".join(out)
def rdp(pts, eps):
    """Ramer-Douglas-Peucker for an OPEN polyline (iterative)."""
    if len(pts) < 3: return pts
    P = np.asarray(pts, np.float64); keep = np.zeros(len(P), bool); keep[0] = keep[-1] = True
    st = [(0, len(P) - 1)]
    while st:
        a, b = st.pop()
        if b <= a + 1: continue
        A, B = P[a], P[b]; seg = P[a + 1:b]
        d = B - A; L = np.hypot(*d)
        dist = np.abs(d[0] * (seg[:, 1] - A[1]) - d[1] * (seg[:, 0] - A[0])) / L if L > 0 else np.hypot(*(seg - A).T)
        i = int(np.argmax(dist))
        if dist[i] > eps: keep[a + 1 + i] = True; st += [(a, a + 1 + i), (a + 1 + i, b)]
    return [tuple(p) for p in P[keep]]
def line_d(R, W, H, lonlat, eps=0.6, margin=40):
    """lon/lat polyline to 'M..L..' runs inside the view (+margin)."""
    px = [((lo - R["lon0"]) * R["ppd"] * R["k"], (R["lat1"] - la) * R["ppd"]) for lo, la in lonlat]  # no +360 wrap
    runs, cur = [], []
    for x, y in px:
        if -margin <= x <= W + margin and -margin <= y <= H + margin: cur.append((x, y))
        elif cur: runs.append(cur); cur = []
    if cur: runs.append(cur)
    return "".join("M" + "L".join(f"{x:.1f},{y:.1f}" for x, y in rdp(r, eps)) for r in runs if len(r) > 1)

# ---------------------------------------------------------------- OSM route relation to one continuous line
def route_line(fn, start, end):
    """Shortest path through the ways of an OSM route relation (relation/<id>/full.json) from the node nearest `start` to the
    node nearest `end` (lon, lat). Gives ONE continuous south->north line even where the relation has two carriageways."""
    d = json.load(open(f"{mk.OSM}/{fn}"))
    xp = f"{mk.OSM}/{fn.replace('_full', '_extra')}"  # ways added by crawl() where the relation has gaps
    if os.path.exists(xp): d["elements"] += json.load(open(xp))["elements"]
    nodes = {e["id"]: (e["lon"], e["lat"]) for e in d["elements"] if e["type"] == "node"}
    adj = defaultdict(list)
    def dist(a, b):
        (x1, y1), (x2, y2) = nodes[a], nodes[b]
        return math.hypot((x2 - x1) * math.cos(math.radians((y1 + y2) / 2)), y2 - y1)
    for w in (e for e in d["elements"] if e["type"] == "way"):
        ns = [n for n in w["nodes"] if n in nodes]
        for a, b in zip(ns, ns[1:]):
            g = dist(a, b); adj[a].append((b, g)); adj[b].append((a, g))
    bridges = set()
    ids = list(adj)
    # bridge gaps in the relation (endpoints of different pieces < ~20 km apart; mostly city sections near Mexico City /
    # Morelia / Guadalajara) with a penalised straight edge — the Sinaloa/Sonora part is complete (crawl)
    ends = [n for n in ids if len(adj[n]) == 1]
    E = np.array([nodes[n] for n in ends])
    for i, n in enumerate(ends):
        dd = np.hypot((E[:, 0] - E[i, 0]) * math.cos(math.radians(E[i, 1])), E[:, 1] - E[i, 1])
        for j in np.where((dd < 0.18) & (dd > 0))[0]:
            adj[n].append((ends[j], dd[j] * 3)); adj[ends[j]].append((n, dd[j] * 3)); bridges |= {(n, ends[j]), (ends[j], n)}
    # pieces that touch without sharing a node (dual carriageways, junction nodes): join every connected piece to its nearest
    # other piece (< 20 km) with a penalised edge
    from scipy.sparse import coo_matrix
    from scipy.sparse.csgraph import connected_components
    from scipy.spatial import cKDTree
    ix = {n: i for i, n in enumerate(ids)}; rr = [ix[a] for a in adj for b, _ in adj[a]]; cc = [ix[b] for a in adj for b, _ in adj[a]]
    ncomp, lab = connected_components(coo_matrix((np.ones(len(rr)), (rr, cc)), shape=(len(ids), len(ids))), directed=False)
    P = np.array([nodes[n] for n in ids]) * np.array([math.cos(math.radians(25)), 1])
    for k in range(ncomp):
        inside = lab == k
        if inside.all(): break
        tree = cKDTree(P[~inside]); dd, jj = tree.query(P[inside]); i = int(np.argmin(dd))
        if dd[i] < 0.18:
            a = ids[np.where(inside)[0][i]]; b = ids[np.where(~inside)[0][jj[i]]]
            adj[a].append((b, dd[i] * 3)); adj[b].append((a, dd[i] * 3)); bridges |= {(a, b), (b, a)}
    def near(p):
        A = np.array([nodes[n] for n in ids]); return ids[int(np.argmin(np.hypot(A[:, 0] - p[0], A[:, 1] - p[1])))]
    s, t = near(start), near(end)
    D = {s: 0.0}; prev = {}; pq = [(0.0, s)]
    while pq:
        g, u = heapq.heappop(pq)
        if u == t: break
        if g > D.get(u, 1e18): continue
        for v, w in adj[u]:
            if g + w < D.get(v, 1e18): D[v] = g + w; prev[v] = u; heapq.heappush(pq, (g + w, v))
    if t not in D: raise RuntimeError(f"{fn}: no path")
    out = [t]
    while out[-1] != s: out.append(prev[out[-1]])
    seq = out[::-1]; real = {(a, b) for a in adj for b, _ in adj[a]}
    gaps = [(nodes[a], nodes[b], dist(a, b) * 111.32) for a, b in zip(seq, seq[1:]) if (a, b) in bridges and dist(a, b) > 0.002]
    for ga, gb, km in gaps: print(f"    straight bridge {km:.1f} km at {ga[0]:.3f},{ga[1]:.3f} to {gb[0]:.3f},{gb[1]:.3f}", flush=True)
    line = [nodes[n] for n in reversed(out)]
    km = sum(dist(a, b) for a, b in zip(list(reversed(out)), list(reversed(out))[1:])) * 111.32
    return line, km
HIGHWAYS = {  # id: (osm full json, start lon/lat, end lon/lat, data-name)
  "hwy-mex15": ("mex15_full.json", (-99.20, 19.40), (-110.945, 31.32), "Mexico Federal Highway 15 (Mexico City to Guadalajara to Mazatlan to Culiacan to Guasave to Los Mochis to Navojoa to Hermosillo to Nogales), OSM relation 14946429"),
  "hwy-mex15-north": ("mex15_full.json", (-107.39, 24.80), (-110.945, 31.32), "Mex 15, Culiacan to Nogales section (Sinaloa to Sonora to Arizona border), OSM relation 14946429"),
  "hwy-mex45": ("mex45_full.json", (-106.077, 28.637), (-106.44, 31.74), "Mexico Federal Highway 45, Chihuahua city to Ciudad Juarez (to El Paso), OSM relation 4066714"),
}
_HW = {}
def highway(hid):
    if hid not in _HW:
        fn, a, b, _ = HIGHWAYS[hid]; _HW[hid] = route_line(fn, a, b)
        print(f"  {hid}: {len(_HW[hid][0])} nodes, {_HW[hid][1]:.0f} km", flush=True)
    return _HW[hid][0]

# ---------------------------------------------------------------- land mask from Esri's light-grey canvas (NVIDIA PRD method)
import map_tiles as mt
mt.URL["gray"] = "https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer/tile/{z}/{y}/{x}"
mt.EXT["gray"] = "jpg"
def gray_land(R, W, H):
    """Coast from Esri Canvas/World_Light_Gray_Base (water = flat grey-blue, darker than land): the DEM coast (> 0.5 m) breaks up
    in the mangrove/lagoon coast of Sinaloa. Lagoons and bays stay water; specks < 400 px of water -> land, < 60 px of land -> sea."""
    from scipy import ndimage as nd
    M, X0, Y0 = mk.load_mosaic("gray", R["gray_mask"], R)
    A = mk.resample(M, X0, Y0, R["gray_mask"], R, W, H); del M
    lum = A @ np.array([0.299, 0.587, 0.114], np.float32); del A
    water = nd.median_filter(lum < R.get("gray_thr", 220), 5)
    land = nd.binary_opening(~water, np.ones((5, 5), bool))  # drops white road lines drawn over water
    lab, n = nd.label(~land); sz = nd.sum(np.ones_like(lab), lab, range(1, n + 1))
    small = np.zeros(n + 1, bool); small[1:] = sz < 400; land = land | small[lab]
    lab, n = nd.label(land); sz = nd.sum(np.ones_like(lab), lab, range(1, n + 1))
    tiny = np.zeros(n + 1, bool); tiny[1:] = sz < 60; land = land & ~tiny[lab]
    return Image.fromarray((land * 255).astype(np.uint8))

# ---------------------------------------------------------------- relief (atlas / night / relief + heightmap)
RELIEF_LAND = [(-100, "#b9b4ac"), (0, "#bdb8b0"), (300, "#c6c1b9"), (1000, "#d2cec7"), (2000, "#dfdcd6"), (3000, "#e9e7e2"), (4500, "#f4f2ee")]
RELIEF_SEA = [(-9000, "#10171d"), (-4000, "#141c23"), (-1500, "#18222a"), (-200, "#1d2831"), (50, "#223039")]
_style = mk.style
def style(E, land, halo, s, kind):
    if kind != "relief": return _style(E, land, halo, s, kind)
    L = mk.ramp(E, RELIEF_LAND); S = mk.ramp(np.minimum(E, 0), RELIEF_SEA)
    S = S + (np.array(mk.hexs("#2a3a45"), np.float32) - S) * (0.6 * halo)[..., None]
    ls = 1 + (s - 1) * 1.05; ss = 1 + (s - 1) * 0.05
    L = L * np.clip(ls, 0.28, 1.5)[..., None]; S = S * np.clip(ss, 0.7, 1.2)[..., None]
    m = land[..., None]
    return np.clip(L * m + S * (1 - m), 0, 255).astype(np.uint8)

def do_relief(name, R):
    """mk.do_relief + 'relief' style + heightmap; optional pre_blur = Gaussian anti-alias of the DEM mosaic when it is finer
    than the output grid (stops hillshade aliasing)."""
    from scipy import ndimage as nd
    W, H = mk.geom(R); lats = mk.lat_rows(R, H)
    M, X0, Y0 = mk.load_mosaic("terr", R["zt"], R)
    if R.get("pre_blur"):
        native = 256 * 2 ** R["zt"] / 360  # px per deg lon of the mosaic
        ratio = native / (R["ppd"] * R["k"])
        if ratio > 1.2: M = nd.gaussian_filter(M, 0.45 * ratio).astype(np.float32); print(f"  pre-blur sigma {0.45 * ratio:.2f}", flush=True)
    E = mk.resample(M, X0, Y0, R["zt"], R, W, H); del M
    if R.get("gray_mask"):
        lm = gray_land(R, W, H)
    elif R["ppd"] <= 400:
        lm = mk.land_water_mask(R, W, H)
    else:
        lm = Image.fromarray(((E > 0.5) * 255).astype(np.uint8)).filter(ImageFilter.MedianFilter(3))
    lmb = lm.filter(ImageFilter.GaussianBlur(0.7))
    land = np.asarray(lmb, np.float32) / 255
    halo = np.asarray(lm.filter(ImageFilter.GaussianBlur(max(2.0, W / 900))), np.float32) / 255 * (1 - land)
    halo = np.clip(halo * 2.2, 0, 1)
    if R["ppd"] > 400: E = np.where(land > 0.5, E, -150).astype(np.float32)
    E = np.where(land > 0.5, np.maximum(E, 1), np.minimum(E, -1)).astype(np.float32)
    hm = np.clip(E / 4000 * 255, 0, 255).astype(np.uint8)
    Image.fromarray(hm).save(f"{mk.OUT}/{name}_height.png", optimize=True)
    kinds = ("atlas", "night", "relief")
    outs = {k: np.zeros((H, W, 3), np.uint8) for k in kinds}
    for a in range(0, H, 1024):
        a0, b1 = max(0, a - 2), min(H, a + 1026)
        s = mk.hillshade(E[a0:b1], lats[a0:b1], R, R["zf"])
        sl = slice(a - a0, a - a0 + min(1024, H - a))
        for k in outs: outs[k][a:a + 1024] = style(E[a0:b1][sl], land[a0:b1][sl], halo[a0:b1][sl], s[sl], k)
    for k, v in outs.items(): mk.save(v, f"{name}_{k}")
    lm.save(f"{mk.OUT}/{name}_landmask.png", optimize=True)

# ---------------------------------------------------------------- overlay extras
NE_ADMIN1 = "ne_10m_admin_1.geojson"
MX_STATES_OSM = {"sinaloa": ["sinaloa", "sonora", "chihuahua", "durango", "baja_california_sur", "nayarit"],
                 "chihuahua": ["chihuahua", "sonora", "sinaloa", "durango", "coahuila"]}
US_STATES_OSM = {"sinaloa": [], "chihuahua": ["texas", "new_mexico", "arizona"]}
MUNIS = {"sinaloa": ["ahome", "el_fuerte", "choix", "guasave", "sinaloa", "salvador_alvarado", "angostura", "culiacan", "navojoa"],
         "chihuahua": ["morelos_chih", "guachochi"]}
NORTH_SINALOA = ["ahome", "el_fuerte", "choix", "guasave", "sinaloa"]  # the 5 municipalities of "la zona norte" of Sinaloa

def us_mexico_border_ne():
    """Shared arcs of Mexico and the USA in world-atlas countries-10m (Natural Earth) to lon/lat polylines."""
    t = json.load(open(f"{mk.VEC}/world-atlas_2_countries-10m.json")); sc, tr = t["transform"]["scale"], t["transform"]["translate"]
    def arcset(g):
        polys = [g["arcs"]] if g["type"] == "Polygon" else g["arcs"]
        return {i if i >= 0 else ~i for p in polys for r in p for i in r}
    geos = {g["properties"]["name"]: g for g in t["objects"]["countries"]["geometries"]}
    shared = arcset(geos["Mexico"]) & arcset(geos["United States of America"])
    out = []
    for i in sorted(shared):
        x = y = 0; pts = []
        for dx, dy in t["arcs"][i]: x += dx; y += dy; pts.append((x * sc[0] + tr[0], y * sc[1] + tr[1]))
        out.append(pts)
    return out
def us_mexico_border_osm():
    """OSM Mexico outer-ring vertices that lie on the OSM USA boundary (< 300 m), on land only (lat < 32.8 and lon > -117.13)."""
    from scipy.spatial import cKDTree
    us = np.array([p for poly in osm_polys("c_usa") for r in poly for p in r])
    tree = cKDTree(us)
    runs = []
    for poly in osm_polys("c_mexico"):
        r = np.array(poly[0]); dd, _ = tree.query(r)
        on = (dd < 0.003) & (r[:, 0] > -117.13) & (r[:, 0] < -97.15)
        cur = []
        for p, o in zip(r, on):
            if o: cur.append(tuple(p))
            elif cur: runs.append(cur); cur = []
        if cur: runs.append(cur)
    return [r for r in runs if len(r) > 1]

def region_sierra(name, R, W, H, kind):
    """Approximate mountain regions from the heightmap: rugged (local relief) AND high ground, inside a corridor."""
    from scipy import ndimage as nd
    hm = np.asarray(Image.open(f"{mk.OUT}/{name}_height.png"), np.float32) * 4000 / 255
    km_px = 111.32 / R["ppd"]
    win = max(3, int(round(12 / km_px)))  # ~12 km window
    mx = nd.maximum_filter(hm, win); mn = nd.minimum_filter(hm, win)
    rug = nd.uniform_filter(mx - mn, win)
    lons = mk.lon_cols(R, W)[None, :]; lats = mk.lat_rows(R, H)[:, None]
    if kind == "smo":  # Sierra Madre Occidental: SE-running belt from the Sonora/Chihuahua line to Nayarit/Jalisco
        # corridor around the axis (-108.6,30.5) to (-104.6,22.0), +-1.6 deg across
        ax0, ay0, ax1, ay1 = -108.6, 30.5, -104.4, 21.6
        dx, dy = ax1 - ax0, ay1 - ay0; L = math.hypot(dx, dy)
        across = ((lons - ax0) * dy - (lats - ay0) * dx) / L; along = ((lons - ax0) * dx + (lats - ay0) * dy) / L
        corr = (np.abs(across) < 1.7) & (along > -0.3) & (along < L + 0.3)
        m = corr & (hm > 1000) & (rug > 450)
    else:  # Sierra Tarahumara: rugged high ground of SW Chihuahua
        chih = poly_mask(R, W, H, osm_polys("s_chihuahua"))
        m = chih & (lons < -106.45) & (lats < 29.2) & (hm > 1300) & (rug > 650)
    m = nd.binary_closing(m, iterations=max(2, int(4 / km_px)))
    m = nd.binary_opening(m, iterations=max(1, int(2 / km_px)))
    lab, n = nd.label(m)
    if n:
        sz = nd.sum(m, lab, range(1, n + 1)); m = lab == (1 + int(np.argmax(sz)))
    m = nd.binary_fill_holes(m)
    m = nd.gaussian_filter(m.astype(np.float32), max(1.5, 3 / km_px)) > 0.5
    return m

def do_overlay(name, R):
    mk.do_overlay(name, R)
    W, H = mk.geom(R); svgp = f"{mk.OUT}/{name}_overlay.svg"; svg = open(svgp).read()
    sw = max(1.0, W / 3000); close = R["ppd"] > 400
    groups = {}
    land = np.asarray(Image.open(f"{mk.OUT}/{name}_landmask.png")) > 127
    # --- states
    if not close:
        mx = [("Ciudad de México" if nm == "Distrito Federal" else nm, p) for nm, p in
              mk.geo_polys(f"{mk.VEC}/{NE_ADMIN1}", lambda p: p.get("adm0_a3") == "MEX") if nm]  # NE still says Distrito Federal
        def psvg(items, prefix):
            parts = []
            for nm, polys in items:
                ds = [mk.pathd(pts) for poly in polys for r in poly for pts in [mk.ring_px(R, r, 0)] if len(pts) > 2 and mk.in_view(pts, W, H)]
                ds = [d for d in ds if d]
                if ds: parts.append(f'<path id="{prefix}-{mk.slug(nm)}" data-name="{nm}" d="{"".join(ds)}"/>')
            return parts
        groups["mx_states"] = psvg(mx, "st")
        groups["us_states"] = psvg(mk.topo_decode(f"{mk.VEC}/us-atlas_3_states-10m.json", "states"), "us")
        border = us_mexico_border_ne(); bsrc = "Natural Earth 10m (world-atlas shared arcs)"
    else:
        parts = []
        for st in MX_STATES_OSM[name]:
            m = poly_mask(R, W, H, osm_polys("s_" + st)) & land
            if m.any(): parts.append(f'<path id="st-{st}" data-name="{st.replace("_", " ").title()} (OSM, clipped to the landmask)" fill-rule="evenodd" d="{mask_paths(m)}"/>')
        groups["mx_states"] = parts
        parts = []
        for st in US_STATES_OSM[name]:
            m = poly_mask(R, W, H, osm_polys("s_" + st)) & land
            if m.any(): parts.append(f'<path id="us-{st}" data-name="{st.replace("_", " ").title()} (OSM)" fill-rule="evenodd" d="{mask_paths(m)}"/>')
        groups["us_states"] = parts
        # countries + land traced from OSM / landmask (NE 10m is ~1-3 km off at this scale; OSM country polygons reach 12 nm out to sea)
        cm = {"c-mexico": poly_mask(R, W, H, osm_polys("c_mexico")) & land, "c-united_states_of_america": poly_mask(R, W, H, osm_polys("c_usa")) & land}
        for pid, m in cm.items():
            new = f'<path id="{pid}" data-name="{pid[2:]} (OSM, clipped to the landmask)" fill-rule="evenodd" d="{mask_paths(m) if m.any() else ""}"/>'
            svg, n = re.subn(rf'<path id="{pid}"[^>]*/>', lambda _: new, svg)
            if not n and m.any(): svg = svg.replace('<g id="countries">', '<g id="countries">' + new + "\n")
        svg = re.sub(r'<g id="land">.*?</g>', lambda _: f'<g id="land"><path id="land-x" fill-rule="evenodd" d="{mask_paths(land)}"/></g>', svg, flags=re.S)
        border = us_mexico_border_osm(); bsrc = "OpenStreetMap (Mexico/USA boundary relations)"
        # municipalities + regions
        parts = []
        for mu in MUNIS[name]:
            m = poly_mask(R, W, H, osm_polys("m_" + mu)) & land
            if m.any(): parts.append(f'<path id="mun-{mu}" data-name="Municipio {mu} (OSM)" fill-rule="evenodd" d="{mask_paths(m)}"/>')
        groups["municipalities"] = parts
    bd = "".join(line_d(R, W, H, l, eps=0.5, margin=5) for l in border)
    groups["borders"] = [f'<path id="b-us_mexico" data-name="US-Mexico border ({bsrc})" d="{bd}"/>'] if bd else []
    # --- regions
    rg = []
    if name == "sinaloa":
        m = np.zeros((H, W), bool)
        for mu in NORTH_SINALOA: m |= poly_mask(R, W, H, osm_polys("m_" + mu))
        m &= land
        rg.append(f'<path id="rg-northern_sinaloa" data-name="Northern Sinaloa: Ahome, El Fuerte, Choix, Guasave, Sinaloa municipalities (OSM)" fill-rule="evenodd" d="{mask_paths(m)}"/>')
    if name in ("mexico", "chihuahua"):
        kind = "smo" if name == "mexico" else "tarahumara"
        m = region_sierra(name, R, W, H, kind) & land
        nm = "Sierra Madre Occidental (approx.: rugged ground above 1000 m, from the DEM)" if kind == "smo" else "Sierra Tarahumara (approx.: rugged ground above 1300 m in SW Chihuahua, from the DEM)"
        rg.append(f'<path id="rg-{"sierra_madre_occidental" if kind == "smo" else "sierra_tarahumara"}" data-name="{nm}" fill-rule="evenodd" d="{mask_paths(m, tol=1.2)}"/>')
    groups["regions"] = rg
    # --- highways
    hw = []
    for hid in HIGHWAYS:
        if name == "north_america" and hid != "hwy-mex15": continue
        d = line_d(R, W, H, highway(hid), eps=0.5 if close else 0.4)
        if d: hw.append(f'<path id="{hid}" data-name="{HIGHWAYS[hid][3]}" d="{d}"/>')
    groups["highways"] = hw
    css = (f"#mx_states path{{fill:none;stroke:#f2ede3;stroke-width:{sw * .6:.1f};stroke-opacity:.45}}"
           f"#us_states path{{fill:none;stroke:#f2ede3;stroke-width:{sw * .6:.1f};stroke-opacity:.4}}"
           f"#municipalities path{{fill:none;stroke:#f2ede3;stroke-width:{sw * .4:.1f};stroke-opacity:.3}}"
           f"#regions path{{fill:none;stroke:#ec6424;stroke-width:{sw:.1f};stroke-opacity:.0}}"
           f"#borders path{{fill:none;stroke:#f2ede3;stroke-width:{sw * 1.2:.1f};stroke-dasharray:{sw * 6:.0f} {sw * 4:.0f}}}"
           f"#highways path{{fill:none;stroke:#f4cf3d;stroke-width:{sw * 1.1:.1f};stroke-linecap:round;stroke-linejoin:round}}")
    svg = svg.replace("</style>", css + "</style>")
    svg = re.sub(r'<g id="us_states">.*?</g>\n?', "", svg, flags=re.S)
    ins = "".join(f'<g id="{k}">' + "\n".join(v) + "</g>\n" for k, v in groups.items() if v)
    svg = svg.replace('<g id="lakes">', ins + '<g id="lakes">')
    open(svgp, "w").write(svg)
    # json extras
    jp = f"{mk.OUT}/{name}.json"; meta = json.load(open(jp))
    meta["svg_hint"] = (f'<svg viewBox="0 0 {W} {H}"> - {name}_overlay.svg shares this pixel space. Groups: land, countries (#c-mexico, '
                        f'#c-united_states_of_america, ...), mx_states (#st-<state>), us_states (#us-<state>), municipalities (#mun-*), borders '
                        f'(#b-us_mexico), regions (#rg-*), highways (#hwy-*), lakes, rivers (#river-*), cities (#p-<place> = places keys)')
    meta["ids"] = {k: re.findall(r'id="([^"]+)"', "".join(v)) for k, v in groups.items() if v}
    meta["images"] = sorted(f for f in os.listdir(mk.OUT) if f.startswith(name + "_") and f.endswith((".jpg", ".png")))
    meta["height_png"] = f"{name}_height.png: 8-bit heightmap, value = elevation_m / 4000 * 255 (sea = 0), same pixel space"
    meta["credit"]["relief_style"] = mk.CREDIT_RELIEF
    meta["credit"]["overlay"] = ("Natural Earth (PD) + " if not close else "") + CREDIT_OSM + " (highways, municipalities" + (", states, countries" if close else "") + ")"
    json.dump(meta, open(jp, "w"), indent=1)
    print("  overlay extras:", {k: len(v) for k, v in groups.items()}, flush=True)

# ---------------------------------------------------------------- aerials
AERIALS = {
  "guasave_kuroda_park_z18": (18, -108.4830, 25.5760, -108.4690, 25.5870, ["kuroda_park", "guasave"]),
  "guasave_z16": (16, -108.5050, 25.5450, -108.4350, 25.6000, ["guasave", "kuroda_park"]),
  "tucson_davis_monthan_z16": (16, -110.9100, 32.1150, -110.7870, 32.1990, ["davis_monthan_afb", "davis_monthan_afb_area", "tucson"]),
  "tapalpa_z16": (16, -103.8100, 19.9050, -103.7150, 19.9750, ["tapalpa"]),
  "cdmx_palacio_nacional_z18": (18, -99.1375, 19.4290, -99.1265, 19.4365, ["palacio_nacional", "zocalo"]),
}
OUTLINES = {  # aerial to {outline id: OSM json key}
  "guasave_kuroda_park_z18": {"kuroda_park": "w_kuroda_park"},
  "guasave_z16": {"kuroda_park": "w_kuroda_park"},
  "tucson_davis_monthan_z16": {"davis_monthan_afb_area": "dm_afb"},
  "cdmx_palacio_nacional_z18": {"palacio_nacional": "palacio"},
}
mk.AERIALS.update(AERIALS)
def do_aerial(n):
    mk.do_aerial(n)
    jp = f"{mk.OUT}/aerial_{n}.json"; meta = json.load(open(jp)); z = meta["zoom"]; tb = meta["tile_bounds"]
    meta["places"] = {k: v for k, v in meta["places"].items() if k in AERIALS[n][5]}  # drop map_kit's Stanford EXTRA pins
    outl = {}
    for k, key in OUTLINES.get(n, {}).items():
        if not os.path.exists(f"{mk.OSM}/{key}.json"): continue
        rings = []
        for poly in osm_polys(key):
            rings.append([[round((mk.tx(lo, z) - tb["x0"]) * 256, 1), round((mk.ty(la, z) - tb["y0"]) * 256, 1)] for lo, la in poly[0]])
        outl[k] = rings
    if outl: meta["outlines_px"] = outl; meta["outlines_note"] = "OSM outlines (ODbL) in this image's pixels: list of rings [[x,y],...]"
    json.dump(meta, open(jp, "w"), indent=1)

# ---------------------------------------------------------------- fill gaps of an OSM route relation by walking the OSM API
def crawl(rel_fn, out_fn, a, b, refpat=None, max_steps=600):
    """Walk ways tagged ref~refpat (trunk/primary/motorway) from the relation node nearest a to the one nearest b, choosing at
    each node the way whose far end gets closest to b. Uses api.openstreetmap.org (node/<id>/ways, way/<id>/full); appends the
    ways (with their nodes) to <out_fn> in the same 'elements' format as relation/<id>/full.json."""
    refpat = refpat or (r"\b45D?\b" if "45" in rel_fn else r"\b15D?\b")
    import time, urllib.request
    UA = {"User-Agent": "vox-edit-kit-mapper/1.0"}
    def api(p):
        for i in range(4):
            try: return json.loads(urllib.request.urlopen(urllib.request.Request("https://api.openstreetmap.org/api/0.6/" + p, headers=UA), timeout=60).read())
            except Exception as e: print("  retry", p, e, flush=True); time.sleep(2 + 3 * i)
    d = json.load(open(f"{mk.OSM}/{rel_fn}"))
    nodes = {e["id"]: (e["lon"], e["lat"]) for e in d["elements"] if e["type"] == "node"}
    ids = list(nodes); A = np.array([nodes[n] for n in ids])
    def nearest(p, ids=ids, A=A): return ids[int(np.argmin(np.hypot(A[:, 0] - p[0], A[:, 1] - p[1])))]
    G = b  # walk until within ~400 m of this point
    def dist(p): return math.hypot((p[0] - G[0]) * math.cos(math.radians(G[1])), p[1] - G[1])
    outp = f"{mk.OSM}/{out_fn}"
    ex = json.load(open(outp)) if os.path.exists(outp) else {"elements": []}
    nodes.update({e["id"]: (e["lon"], e["lat"]) for e in ex["elements"] if e["type"] == "node"})  # resume from crawled nodes too
    ids2 = list(nodes); A2 = np.array([nodes[n] for n in ids2]); cur = nearest(a, ids2, A2)
    seen_w = {e["id"] for e in ex["elements"] if e["type"] == "way"}; seen_w_local = set()
    for step in range(max_steps):
        cp = nodes[cur]
        if dist(cp) < 0.004: print(f"  reached goal after {step} steps", flush=True); break
        ws = api(f"node/{cur}/ways.json")["elements"]
        best = None
        okref = [w for w in ws if re.search(refpat, w.get("tags", {}).get("ref", ""))]
        for w in (okref if any(x["id"] not in seen_w_local for x in okref) else ws):  # no ref-15 way here (city streets): any trunk/primary
            t = w.get("tags", {})
            if w["id"] in seen_w_local or not t.get("highway", "").startswith(("trunk", "primary", "motorway")): continue
            full = api(f"way/{w['id']}/full.json")["elements"]
            nn = {e["id"]: (e["lon"], e["lat"]) for e in full if e["type"] == "node"}
            wn = w["nodes"]; i = wn.index(cur)
            for seg in (wn[i:], wn[:i + 1][::-1]):
                if len(seg) < 2: continue
                # stop early on the segment if it passes the goal
                dd = [dist(nn[n]) for n in seg]
                near_goal = [k for k, v in enumerate(dd) if v < 0.004 and k > 0]
                j = near_goal[0] if near_goal else len(seg) - 1  # always walk a way to its end (ways bend), stop at the goal
                cand = (dd[j], seg[:j + 1], w, full)
                if best is None or cand[0] < best[0]: best = cand
        if best is None: print(f"  stuck at node {cur} {cp}", flush=True); break
        _, seg, w, full = best; seen_w_local.add(w["id"])
        if w["id"] not in seen_w:
            ex["elements"] += [e for e in full if e["type"] == "node"] + [e for e in full if e["type"] == "way"]; seen_w.add(w["id"])
        nodes.update({e["id"]: (e["lon"], e["lat"]) for e in full if e["type"] == "node"})
        cur = seg[-1]
        if step % 10 == 0: print(f"  step {step}: way {w['id']} ref={w['tags'].get('ref')} now {dist(nodes[cur]):.3f} deg from goal", flush=True)
        time.sleep(0.5)
    json.dump(ex, open(outp, "w"))

if __name__ == "__main__":
    a = sys.argv[1]
    if a in REGIONS:
        R = REGIONS[a]; steps = (sys.argv[2] if len(sys.argv) > 2 else "relief,sat,overlay").split(",")
        mk.REGIONS[a] = R; print(a, mk.geom(R), flush=True)
        if "relief" in steps: do_relief(a, R)
        if "sat" in steps: mk.do_sat(a, R)
        if "overlay" in steps: do_overlay(a, R)
    elif a == "aerial":
        for n in sys.argv[2:] or AERIALS: do_aerial(n)
    elif a == "crawl":  # crawl <rel_fn> <out_fn> lonA latA lonB latB
        crawl(sys.argv[2], sys.argv[3], tuple(map(float, sys.argv[4:6])), tuple(map(float, sys.argv[6:8])))
    elif a == "hw":
        for h in HIGHWAYS: highway(h)

