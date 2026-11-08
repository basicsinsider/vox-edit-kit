"""Build the map kit (assets/maps/kit): graded relief + satellite bases, regional crops, vector overlays.
Usage:  .venv/bin/python tools/map_kit.py <region> [steps]      steps: relief,sat,overlay (default all)
        regions: world, east_asia, pacific, us, bay_area, northeast, taiwan, eastern_europe, russia, south_america, paraguay   (see REGIONS)
Data:   AWS Terrain Tiles (terrarium; SRTM/GMTED/ETOPO1, public domain) for relief,
        Esri World Imagery tiles for satellite (credit "Esri, Maxar, Earthstar Geographics"),
        NASA Blue Marble NG topo-bathy (public domain) for the world satellite base,
        Natural Earth 10m vectors (public domain; world-atlas / us-atlas topojson + NE geojson via jsDelivr).
Fetch tiles first with tools/map_tiles.py (one heavy job at a time; regions are processed in row strips)."""
import sys, os, json, math, re
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from map_tiles import tx, ty, path as tpath
Image.MAX_IMAGE_PIXELS = None
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = f"{ROOT}/assets/maps/kit"
VEC = os.environ.get("MK_VEC", "/tmp/mk/vec")
OSM = os.environ.get("MK_OSM", "/tmp/mk/osm")  # Nominatim lookup JSONs (osm_ids=R…, polygon_geojson=1), see README
BM = "/tmp/mk/dl/bm_topobathy_200408.jpg"

# ppd = px per degree of latitude; k = x squash (cos of centre latitude) so close-ups keep true shapes.
# x = (lon - lon0) * ppd * k ;  y = (lat1 - lat) * ppd     (lon < lon0 -> lon + 360 for the Pacific)
REGIONS = {
  "world":     dict(lon0=-180, lon1=180, lat0=-90, lat1=90, ppd=16384/360, k=1.0, zt=6, ze=None, zf=22),
  "east_asia": dict(lon0=100, lon1=150, lat0=15, lat1=48, ppd=150, k=0.853, zt=8, ze=8, zf=9),
  "pacific":   dict(lon0=100, lon1=245, lat0=5, lat1=60, ppd=44, k=1.0, zt=6, ze=6, zf=20),
  "us":        dict(lon0=-126, lon1=-66, lat0=23.5, lat1=50, ppd=133, k=0.801, zt=8, ze=8, zf=10),
  "bay_area":  dict(lon0=-123.0, lon1=-121.55, lat0=36.95, lat1=38.25, ppd=5200, k=0.792, zt=13, ze=13, zf=1.6),
  "northeast": dict(lon0=-75.2, lon1=-69.8, lat0=40.4, lat1=43.0, ppd=1588, k=0.746, zt=11, ze=11, zf=3.0),
  "taiwan":    dict(lon0=119.3, lon1=122.2, lat0=21.8, lat1=25.4, ppd=1222, k=0.916, zt=11, ze=11, zf=1.6),
  # Ivan project (2026-11-01): Poland -> Ukraine/Belarus -> western Russia -> Tatarstan/Kazakhstan NW edge; whole Russia
  "eastern_europe": dict(lon0=20, lon1=62, lat0=42, lat1=62, ppd=240, k=0.6157, zt=8, ze=8, zf=7, flat_water=[(46, 36, 55.5, 47.5)]),
  "russia":    dict(lon0=20, lon1=190, lat0=40, lat1=78, ppd=75, k=0.515, zt=6, ze=None, zf=15, flat_water=[(46, 36, 55.5, 47.5)]),
  # Paraguay project (2026-11-08): whole South America with margin; Paraguay close-up (landlocked: vector land/lake mask
  # + NE rivers burnt in as water, hillshade from the un-flattened DEM so reservoirs don't get cliff rims, no sat water swap)
  "south_america": dict(lon0=-95, lon1=-25, lat0=-58, lat1=15, ppd=84, k=0.9336, zt=7, ze=8, zf=12, river_rank=4),
  "paraguay":  dict(lon0=-63.5, lon1=-53.5, lat0=-28, lat1=-19, ppd=560, k=0.9171, zt=10, ze=10, zf=5, vec_mask=True,
                    burn_rivers={"Paraguay": 3, "Paraná": 5}, sat_water=False, river_rank=9,
                    # NE 1:10M rivers/borders are 2-13 km off the imagery at this scale -> OpenStreetMap geometry (Nominatim
                    # lookup polygon_geojson, threshold 0.0002-0.0003 deg; ODbL) for these countries, rivers and reservoirs
                    osm={"countries": {"Paraguay": "c_paraguay", "Brazil": "c_brazil", "Argentina": "c_argentina", "Bolivia": "c_bolivia"},
                         "rivers": {"Paraguay": "r_paraguay", "Paraná": "r_parana", "Pilcomayo": "r_pilcomayo"},
                         "water": ["r_yacyreta", "r_itaipu"]}),
}

PLACES = {  # lon, lat
  "taipei": (121.5654, 25.0330), "hsinchu_city": (120.9675, 24.8138), "hsinchu_science_park": (121.0150, 24.7736),
  "tsmc_hq_fab12a": (121.01275, 24.77292), "umc_lihsin6_hq": (121.01503, 24.77222), "umc_lihsin3_campus": (121.02047, 24.77035),
  "taichung": (120.6736, 24.1477), "tainan": (120.2270, 22.9999), "kaohsiung": (120.3014, 22.6273),
  "keelung": (121.7419, 25.1276), "kinmen": (118.3171, 24.4321), "matsu": (119.9500, 26.1600), "penghu": (119.5664, 23.5655),
  "beijing": (116.4074, 39.9042), "shanghai": (121.4737, 31.2304), "nanjing": (118.7969, 32.0603),
  "xiamen": (118.0894, 24.4798), "fuzhou": (119.2965, 26.0745), "guangzhou": (113.2644, 23.1291),
  "hong_kong": (114.1694, 22.3193), "shenzhen": (114.0579, 22.5431),
  "tokyo": (139.6917, 35.6895), "osaka": (135.5023, 34.6937), "kyoto": (135.7681, 35.0116), "okinawa_naha": (127.6809, 26.2124),
  "seoul": (126.9780, 37.5665), "pyongyang": (125.7625, 39.0392), "busan": (129.0756, 35.1796),
  "manila": (120.9842, 14.5995), "hanoi": (105.8342, 21.0278), "moscow": (37.6173, 55.7558), "vladivostok": (131.8869, 43.1198),
  "guam": (144.7937, 13.4443), "honolulu": (-157.8583, 21.3069), "anchorage": (-149.9003, 61.2181),
  "san_francisco": (-122.4194, 37.7749), "palo_alto": (-122.1430, 37.4419), "stanford_university": (-122.1697, 37.4275),
  "hp_garage": (-122.1550, 37.4430), "mountain_view": (-122.0838, 37.3861), "san_jose": (-121.8863, 37.3382),
  "santa_clara": (-121.9552, 37.3541), "sunnyvale": (-122.0363, 37.3688), "cupertino": (-122.0322, 37.3230),
  "oakland": (-122.2711, 37.8044), "berkeley": (-122.2730, 37.8715),
  "shockley_lab_mountain_view": (-122.0790, 37.4049),
  "los_angeles": (-118.2437, 34.0522), "seattle": (-122.3321, 47.6062), "portland": (-122.6765, 45.5152),
  "phoenix": (-112.0740, 33.4484), "denver": (-104.9903, 39.7392), "dallas": (-96.7970, 32.7767), "austin": (-97.7431, 30.2672),
  "houston": (-95.3698, 29.7604), "chicago": (-87.6298, 41.8781), "detroit": (-83.0458, 42.3314), "atlanta": (-84.3880, 33.7490),
  "miami": (-80.1918, 25.7617), "washington_dc": (-77.0369, 38.9072), "new_york": (-74.0060, 40.7128),
  "boston": (-71.0589, 42.3601), "mit_cambridge": (-71.0942, 42.3601), "harvard": (-71.1167, 42.3770),
  "route_128_waltham": (-71.2356, 42.3765), "bell_labs_murray_hill": (-74.4018, 40.6840),
  "princeton": (-74.6672, 40.3573), "philadelphia": (-75.1652, 39.9526), "providence": (-71.4128, 41.8240),
  "new_haven_yale": (-72.9223, 41.3163), "ibm_armonk": (-73.7149, 41.1265), "albany": (-73.7562, 42.6526),
  "hartford": (-72.6851, 41.7658),
  # Ivan project (eastern_europe / russia)
  "kyiv": (30.5234, 50.4501), "warsaw": (21.0122, 52.2297), "minsk": (27.5615, 53.9045), "st_petersburg": (30.3351, 59.9343),
  "kazan": (49.1221, 55.7887), "yelabuga": (52.0547, 55.7564), "alabuga_drone_factory": (52.0200, 55.8350), "alabuga_nw_new_halls": (51.9747, 55.8504),
  "ryazan": (39.7413, 54.6269), "ivanovo": (40.9737, 57.0004), "engels": (46.1236, 51.4986), "saratov": (46.0086, 51.5331),
  "kharkiv": (36.2304, 49.9935), "odesa": (30.7233, 46.4825), "lviv": (24.0297, 49.8397), "belgorod": (36.5983, 50.5997),
  "kursk": (36.1873, 51.7304), "rostov_on_don": (39.7015, 47.2357), "volgograd": (44.5133, 48.7080), "nizhny_novgorod": (44.0020, 56.3269),
  "samara": (50.1008, 53.1959), "voronezh": (39.2003, 51.6720), "sevastopol": (33.5254, 44.6166), "vilnius": (25.2797, 54.6872),
  "riga": (24.1052, 56.9496), "tallinn": (24.7536, 59.4370), "helsinki": (24.9384, 60.1699), "uralsk_oral": (51.3667, 51.2333),
  "aktobe": (57.2070, 50.2839), "ufa": (55.9721, 54.7388), "perm": (56.2502, 58.0105), "yekaterinburg": (60.6122, 56.8389),
  "dyagilevo_airbase": (39.5700, 54.6420), "ivanovo_severny_airbase": (40.9810, 57.0600), "engels_airbase": (46.2100, 51.4800),
  "olenya_airbase": (33.4640, 68.1510), "belaya_airbase": (103.5750, 52.9150), "murmansk": (33.0827, 68.9585),
  "irkutsk": (104.2964, 52.2870), "novosibirsk": (82.9346, 55.0084), "astana": (71.4491, 51.1694), "almaty": (76.8512, 43.2220),
  "kirillov_blast_site": (37.7893, 55.7176), "sarvarov_blast_site": (37.7386, 55.6077), "kazan_aircraft_plant": (49.1300, 55.8600),
  # Paraguay project (south_america / paraguay)
  "asuncion": (-57.6340, -25.2830), "brasilia": (-47.8825, -15.7942), "buenos_aires": (-58.3816, -34.6037), "la_paz": (-68.1193, -16.4897),
  "sucre": (-65.2627, -19.0196), "santa_cruz_de_la_sierra": (-63.1812, -17.7833), "montevideo": (-56.1645, -34.9011),
  "santiago": (-70.6693, -33.4489), "lima": (-77.0428, -12.0464), "quito": (-78.4678, -0.1807), "bogota": (-74.0721, 4.7110),
  "caracas": (-66.9036, 10.4806), "georgetown": (-58.1551, 6.8013), "paramaribo": (-55.2038, 5.8520), "cayenne": (-52.3350, 4.9224),
  "panama_city": (-79.5199, 8.9824), "sao_paulo": (-46.6333, -23.5505), "rio_de_janeiro": (-43.1729, -22.9068),
  "cordoba": (-64.1888, -31.4201), "porto_alegre": (-51.2177, -30.0346), "curitiba": (-49.2733, -25.4284),
  "ciudad_del_este": (-54.6111, -25.5097), "encarnacion": (-55.8661, -27.3306), "concepcion": (-57.4314, -23.4064),
  "san_lorenzo": (-57.5097, -25.3397), "luque": (-57.4872, -25.2700), "pedro_juan_caballero": (-55.7356, -22.5472),
  "filadelfia": (-60.0328, -22.3528), "pilar": (-58.3008, -26.8569), "villarrica": (-56.4350, -25.7500),
  "coronel_oviedo": (-56.4447, -25.4500), "foz_do_iguacu": (-54.5882, -25.5163), "posadas": (-55.8961, -27.3671),
  "clorinda": (-57.7186, -25.2847), "formosa_ar": (-58.1781, -26.1775), "itaipu_dam": (-54.5888, -25.4080),
  # Asunción landmarks (OSM/Nominatim positions, checked by eye on the Esri aerials 2026-11-08)
  "palacio_legislativo": (-57.63537, -25.27923), "palacio_de_lopez": (-57.63717, -25.27734), "plaza_de_armas": (-57.63459, -25.27989),
  "plaza_de_los_heroes": (-57.63502, -25.28243), "plaza_de_la_democracia": (-57.63475, -25.28338),
  "banco_central_del_paraguay": (-57.57549, -25.27794), "ueno_hq_santa_teresa_3088": (-57.55454, -25.28974),
  "torres_del_paseo_la_galeria": (-57.56340, -25.28434), "mburuvicha_roga": (-57.60166, -25.29303),
}
CREDIT_RELIEF = "Relief: AWS Terrain Tiles (SRTM/GMTED/ETOPO1, public domain); vectors: Natural Earth (public domain)"
CREDIT_ESRI = "Imagery: Esri, Maxar, Earthstar Geographics"
CREDIT_BM = "NASA Blue Marble Next Generation (public domain)"

def hexs(h): return [int(h[i:i + 2], 16) for i in (1, 3, 5)]
def ramp(v, stops):
    xs = [s[0] for s in stops]; cs = np.array([hexs(s[1]) for s in stops], np.float32)
    return np.stack([np.interp(v, xs, cs[:, c]) for c in range(3)], -1).astype(np.float32)

def geom(R):
    W = int(round((R["lon1"] - R["lon0"]) * R["ppd"] * R["k"])); H = int(round((R["lat1"] - R["lat0"]) * R["ppd"]))
    return W, H
def lon_cols(R, W): return R["lon0"] + (np.arange(W) + 0.5) / (R["ppd"] * R["k"])
def lat_rows(R, H): return R["lat1"] - (np.arange(H) + 0.5) / R["ppd"]
def proj(R, lon, lat):
    if lon < R["lon0"] - 1e-9: lon += 360
    return (lon - R["lon0"]) * R["ppd"] * R["k"], (R["lat1"] - lat) * R["ppd"]

def load_mosaic(src, z, R):
    n = 2 ** z; latN = min(R["lat1"], 85.05); latS = max(R["lat0"], -85.05)
    X0, X1 = int(tx(R["lon0"], z)), int(min(tx(R["lon1"], z), tx(R["lon0"], z) + n - 1e-9)) + 1
    Y0, Y1 = int(ty(latN, z)), min(n - 1, int(ty(latS, z)))
    w, h = (X1 - X0 + 1) * 256, (Y1 - Y0 + 1) * 256
    M = np.zeros((h, w), np.float32) if src == "terr" else np.zeros((h, w, 3), np.uint8)
    miss = 0
    for X in range(X0, X1 + 1):
        for Y in range(Y0, Y1 + 1):
            p = tpath(src, z, X % n, Y)
            try: im = Image.open(p).convert("RGB")
            except Exception: miss += 1; continue
            a = np.asarray(im)
            sl = (slice((Y - Y0) * 256, (Y - Y0 + 1) * 256), slice((X - X0) * 256, (X - X0 + 1) * 256))
            if src == "terr": M[sl] = a[..., 0].astype(np.float32) * 256 + a[..., 1] + a[..., 2] / 256.0 - 32768
            else: M[sl] = a
    print(f"  mosaic {src} z{z}: {w}x{h}, missing {miss}", flush=True)
    return M, X0, Y0

def resample(M, X0, Y0, z, R, W, H, rows=None):
    """Separable bilinear Web-Mercator mosaic -> equirect grid (rows: optional slice of output rows)."""
    lats = lat_rows(R, H); lons = lon_cols(R, W)
    if rows is not None: lats = lats[rows]
    sy = (np.array([ty(min(max(l, -85.05), 85.05), z) for l in lats]) - Y0) * 256 - 0.5
    sx = (tx(lons, z) - X0) * 256 - 0.5
    sy = np.clip(sy, 0, M.shape[0] - 1.001); sx = np.clip(sx, 0, M.shape[1] - 1.001)
    y0 = sy.astype(int); fy = (sy - y0).astype(np.float32); x0 = sx.astype(int); fx = (sx - x0).astype(np.float32)
    out = []
    for a in range(0, len(y0), 512):
        b = slice(a, a + 512); f = fy[b].reshape((-1, 1) + (1,) * (M.ndim - 2))
        A = M[y0[b]].astype(np.float32) * (1 - f) + M[y0[b] + 1].astype(np.float32) * f
        g = fx.reshape((1, -1) + (1,) * (M.ndim - 2))
        out.append(A[:, x0] * (1 - g) + A[:, x0 + 1] * g)
    return np.concatenate(out, 0)

# ---------- vectors ----------
def topo_decode(path, obj):
    t = json.load(open(path)); sc, tr = t["transform"]["scale"], t["transform"]["translate"]
    arcs = []
    for a in t["arcs"]:
        x = y = 0; pts = []
        for dx, dy in a: x += dx; y += dy; pts.append((x * sc[0] + tr[0], y * sc[1] + tr[1]))
        arcs.append(pts)
    def ring(ix):
        pts = []
        for i in ix:
            p = arcs[i] if i >= 0 else arcs[~i][::-1]
            pts.extend(p if not pts else p[1:])
        return pts
    out = []
    for g in t["objects"][obj]["geometries"]:
        polys = [g["arcs"]] if g["type"] == "Polygon" else g["arcs"] if g["type"] == "MultiPolygon" else []
        out.append((g.get("properties", {}).get("name", str(g.get("id"))), [[ring(r) for r in p] for p in polys]))
    return out
def geo_polys(path, keep=lambda p: True):
    out = []
    for f in json.load(open(path))["features"]:
        if not keep(f["properties"]): continue
        g = f["geometry"]; polys = [g["coordinates"]] if g["type"] == "Polygon" else g["coordinates"] if g["type"] == "MultiPolygon" else []
        out.append((f["properties"].get("name") or "", polys))
    return out
def geo_lines(path, keep=lambda p: True):
    out = []
    for f in json.load(open(path))["features"]:
        if not keep(f["properties"]): continue
        g = f["geometry"]; ls = [g["coordinates"]] if g["type"] == "LineString" else g["coordinates"] if g["type"] == "MultiLineString" else []
        out.append((f["properties"].get("name") or "", ls))
    return out
def ring_px(R, ring, sh=None):
    if sh is None:
        mlon = sum(p[0] for p in ring) / len(ring); sh = 360 if mlon < R["lon0"] - 1 else 0
    return [((p[0] + sh - R["lon0"]) * R["ppd"] * R["k"], (R["lat1"] - p[1]) * R["ppd"]) for p in ring]
def unwrap(ring):
    out = []; off = 0; prev = None
    for lo, la in ring:
        if prev is not None and abs(lo + off - prev) > 180: off += 360 if prev > lo + off else -360
        out.append((lo + off, la)); prev = lo + off
    return out
def ring_variants(R, ring):
    """Rings that jump across the antimeridian are unwrapped, then drawn at -360/0/+360 (in_view keeps the visible ones)."""
    r = unwrap(ring)
    return [ring_px(R, r, sh) for sh in (-360, 0, 360)]
def in_view(pts, W, H, m=50):
    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
    return max(xs) > -m and min(xs) < W + m and max(ys) > -m and min(ys) < H + m
def mask_from(R, W, H, polys_list, ss=1):
    im = Image.new("L", (W * ss, H * ss), 0); d = ImageDraw.Draw(im)
    for val, polys in polys_list:
        for poly in polys:
            for i, r in enumerate(poly):
                if len(r) < 3: continue
                pts = ring_px(R, r)
                if not in_view(pts, W, H): continue
                d.polygon([(x * ss, y * ss) for x, y in pts], fill=(val if i == 0 else 255 - val))
    if ss > 1: im = im.resize((W, H), Image.LANCZOS)
    return im
def land_water_mask(R, W, H):
    land = topo_decode(f"{VEC}/world-atlas_2_land-10m.json", "land")
    lakes = geo_polys(f"{VEC}/ne_10m_lakes.geojson", lambda p: p["scalerank"] <= (9 if R["ppd"] > 100 else 4))
    im = Image.new("L", (W, H), 0); d = ImageDraw.Draw(im)
    for _, polys in land:
        for poly in polys:
            for i, r in enumerate(poly):
                for pts in ring_variants(R, r):
                    if len(pts) > 2 and in_view(pts, W, H): d.polygon(pts, fill=255 if i == 0 else 0)
    for _, polys in lakes:
        for poly in polys:
            for i, r in enumerate(poly):
                for pts in ring_variants(R, r):
                    if len(pts) > 2 and in_view(pts, W, H): d.polygon(pts, fill=0 if i == 0 else 255)
    return im

# ---------- styling ----------
ATLAS_LAND = [(-100, "#c3c49d"), (0, "#c3c49d"), (150, "#cdc79f"), (400, "#d8cba2"), (800, "#dcc69b"), (1300, "#d1b38a"),
              (2000, "#c19f7c"), (3000, "#ae8f76"), (4300, "#c4b6a6"), (5500, "#e6e0d6")]
ATLAS_SEA = [(-9000, "#5f7d86"), (-5000, "#6b8990"), (-3000, "#789599"), (-1000, "#87a3a4"), (-200, "#9cb6b2"), (-30, "#adc4bd"), (50, "#b6cbc3")]
NIGHT_LAND = [(-100, "#33373d"), (0, "#34383e"), (500, "#393d43"), (1500, "#42464c"), (3000, "#4b4f55"), (5000, "#5a5e64")]
NIGHT_SEA = [(-9000, "#0b0e12"), (-4000, "#0e1217"), (-1000, "#11161c"), (-200, "#141a21"), (50, "#171e26")]

def hillshade(E, lats, R, zf):
    gy, gx = np.gradient(E)
    dx = (111320 * np.cos(np.radians(lats)) / (R["ppd"] * R["k"]))[:, None].astype(np.float32)
    dy = np.float32(111320 / R["ppd"])
    p = gx / dx * zf; q = -gy / dy * zf  # dz/dEast ; dz/dNorth (rows run south)
    norm = np.sqrt(p * p + q * q + 1)
    s = np.zeros_like(E)
    for az, alt, w in ((315, 45, 0.6), (270, 50, 0.2), (355, 55, 0.2)):
        a, h = math.radians(az), math.radians(alt)
        L = (math.sin(a) * math.cos(h), math.cos(a) * math.cos(h), math.sin(h))
        s += w * np.clip((-p * L[0] - q * L[1] + L[2]) / norm, 0, None) / math.sin(h)
    return s  # flat = 1
def style(E, land, halo, s, kind):
    if kind == "atlas":
        L = ramp(E, ATLAS_LAND); S = ramp(np.minimum(E, 0), ATLAS_SEA)
        S = S + (np.array(hexs("#c5d4cb"), np.float32) - S) * (0.55 * halo)[..., None]
        ls = 1 + (s - 1) * 0.85; ss = 1 + (s - 1) * 0.07
    else:
        L = ramp(E, NIGHT_LAND); S = ramp(np.minimum(E, 0), NIGHT_SEA)
        S = S + (np.array(hexs("#1e2731"), np.float32) - S) * (0.7 * halo)[..., None]
        ls = 1 + (s - 1) * 0.8; ss = 1 + (s - 1) * 0.06
    L = L * np.clip(ls, 0.35, 1.45)[..., None]; S = S * np.clip(ss, 0.6, 1.25)[..., None]
    m = land[..., None]
    return np.clip(L * m + S * (1 - m), 0, 255).astype(np.uint8)

def save(arr_or_im, name, q=90):
    im = arr_or_im if isinstance(arr_or_im, Image.Image) else Image.fromarray(arr_or_im)
    p = f"{OUT}/{name}.jpg"; im.save(p, quality=q, optimize=True, progressive=True)
    print("  wrote", p, im.size, f"{os.path.getsize(p) / 1e6:.1f} MB", flush=True)

def do_relief(name, R):
    W, H = geom(R); lats = lat_rows(R, H)
    M, X0, Y0 = load_mosaic("terr", R["zt"], R)
    E = resample(M, X0, Y0, R["zt"], R, W, H); del M
    pol = np.abs(lats) > 84.0  # terrarium stops at 85.05: fill the caps with a smoothed copy of the 84 deg row
    if pol.any():
        for side in (pol & (lats > 0), pol & (lats < 0)):
            if not side.any(): continue
            ref = np.argmin(np.abs(lats - (84.0 if lats[side][0] > 0 else -84.0)))
            row = np.convolve(np.pad(E[ref], 200, mode="wrap"), np.ones(401, np.float32) / 401, "same")[200:-200]
            E[side] = row
    if R["ppd"] <= 400 or R.get("vec_mask"):
        lm = land_water_mask(R, W, H)
        if R.get("burn_rivers"):
            d = ImageDraw.Draw(lm)
            for poly in [p for k in R.get("osm", {}).get("water", []) for p in osm_geo(k)]:
                for i, r in enumerate(poly):
                    d.polygon(ring_px(R, r), fill=0 if i == 0 else 255)
            for nm, ls in osm_swap(river_fix(geo_lines(f"{VEC}/ne_10m_rivers_lake_centerlines.geojson")), R, "rivers"):
                if nm not in R["burn_rivers"]: continue
                for l in ls:
                    pts = ring_px(R, l)
                    if len(pts) > 1 and in_view(pts, W, H): d.line(pts, fill=0, width=R["burn_rivers"][nm], joint="curve")
    else:  # close-ups: coast from the elevation itself (sharper than 1:10M vectors), lakes from NE
        lm = Image.fromarray(((E > 0.5) * 255).astype(np.uint8)).filter(ImageFilter.MedianFilter(3))
    lmb = lm.filter(ImageFilter.GaussianBlur(0.7))
    land = np.asarray(lmb, np.float32) / 255
    halo_r = max(2.0, W / 900)
    halo = np.asarray(lm.filter(ImageFilter.GaussianBlur(halo_r)), np.float32) / 255 * (1 - land)
    halo = np.clip(halo * 2.2, 0, 1)
    Eh = E.copy() if R.get("vec_mask") else None  # hillshade source (water keeps its real surface -> no cliff rims)
    if R["ppd"] > 400:  # close-ups: flat sea (ETOPO bathymetry shows tile seams at this scale)
        E = np.where(land > 0.5, E, -150).astype(np.float32)  # flat water + coastal halo
    for lo_a, la_a, lo_b, la_b in R.get("flat_water", []):  # inland seas whose bathymetry shows tile seams (Caspian)
        cs = (lon_cols(R, W) >= lo_a) & (lon_cols(R, W) <= lo_b); rs = (lats >= la_a) & (lats <= la_b)
        box = np.ix_(rs, cs); E[box] = np.where(land[box] > 0.5, E[box], -60)
    E = np.where(land > 0.5, np.maximum(E, 1), np.minimum(E, -1)).astype(np.float32)
    outs = {k: np.zeros((H, W, 3), np.uint8) for k in ("atlas", "night")}
    for a in range(0, H, 1024):
        a0, b1 = max(0, a - 2), min(H, a + 1026)
        s = hillshade((E if Eh is None else Eh)[a0:b1], lats[a0:b1], R, R["zf"])
        sl = slice(a - a0, a - a0 + min(1024, H - a))
        for k in outs:
            outs[k][a:a + 1024] = style(E[a0:b1][sl], land[a0:b1][sl], halo[a0:b1][sl], s[sl], k)
    for k, v in outs.items(): save(v, f"{name}_{k}")
    lm.save(f"{OUT}/{name}_landmask.png", optimize=True)
    del E, outs

def grade_desat(a):
    a = a.astype(np.float32); lum = a @ np.array([0.299, 0.587, 0.114], np.float32)
    a = lum[..., None] + (a - lum[..., None]) * 0.28
    a = 255 * (a / 255) ** 1.12 * 0.92
    a = a + (np.array([-3, 0, 6], np.float32) * (1 - lum[..., None] / 255))  # cool shadows, s02-like
    return np.clip(a, 0, 255).astype(np.uint8)
def grade_nat(a):
    a = a.astype(np.float32); lum = a @ np.array([0.299, 0.587, 0.114], np.float32)
    a = lum[..., None] + (a - lum[..., None]) * 0.88
    return np.clip(a * 1.02, 0, 255).astype(np.uint8)

def do_sat(name, R):
    W, H = geom(R)
    if R["ze"] is None:  # world: NASA Blue Marble topo-bathy 21600
        im = Image.open(BM); a = np.asarray(im)
        Wb, Hb = im.size; out = np.zeros((Hb, Wb, 3), np.uint8)
        for r in range(0, Hb, 1200): out[r:r + 1200] = grade_desat(a[r:r + 1200])
        del a; save(out, f"{name}_satdesat_21600", q=88); return
    M, X0, Y0 = load_mosaic("esri", R["ze"], R)
    A = resample(M, X0, Y0, R["ze"], R, W, H); del M
    A = np.clip(A + 0.5, 0, 255).astype(np.uint8)
    mp = f"{OUT}/{name}_landmask.png"
    if R["ppd"] > 400 and R.get("sat_water", True) and os.path.exists(mp):  # close-ups: Esri's water is a patchwork of sources -> one calm water tone
        land = np.asarray(Image.open(mp).filter(ImageFilter.GaussianBlur(1.5)), np.float32)[..., None] / 255
        water = np.median(A[land[..., 0] < 0.05].reshape(-1, 3), axis=0) if (land < 0.05).any() else np.array([20, 40, 60])
        A = np.clip(A * land + water.astype(np.float32) * 0.8 * (1 - land), 0, 255).astype(np.uint8)
    save(grade_nat(A), f"{name}_sat"); save(grade_desat(A), f"{name}_satdesat")

def slug(s):
    import unicodedata  # strip accents first (Paraná -> parana, not "paran")
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "_", s.lower()).strip("_")
def pathd(pts, closed=True):
    out = []; last = None
    for x, y in pts:
        if last and abs(x - last[0]) < 0.8 and abs(y - last[1]) < 0.8: continue
        out.append(f"{x:.1f},{y:.1f}"); last = (x, y)
    return ("M" + "L".join(out) + ("Z" if closed else "")) if len(out) > 1 else ""
def crimea_fix(items):
    """world-atlas (Natural Earth de-facto) puts Crimea inside Russia. For the Ivan project Crimea is drawn as part of
    #c-ukraine (internationally recognised border) and ALSO as its own #c-crimea path so a scene can hatch/label it as occupied."""
    out = []; crimea = []
    def in_crimea(poly):
        r = poly[0]; lo = sum(p[0] for p in r) / len(r); la = sum(p[1] for p in r) / len(r)
        return 32.3 < lo < 36.8 and 44.2 < la < 46.3
    for nm, polys in items:
        if nm == "Russia":
            crimea += [p for p in polys if in_crimea(p)]; polys = [p for p in polys if not in_crimea(p)]
        out.append((nm, polys))
    if crimea:
        out = [(nm, polys + crimea) if nm == "Ukraine" else (nm, polys) for nm, polys in out] + [("Crimea", crimea)]
    return out
def osm_geo(key):
    g = json.load(open(f"{OSM}/{key}.json"))[0]["geojson"]; c = g["coordinates"]
    return {"Polygon": [c], "MultiPolygon": c, "LineString": [c], "MultiLineString": c}[g["type"]]
def osm_swap(items, R, kind):
    """Replace Natural Earth features by OSM ones where the region asks for it (R['osm'][kind] = {name: json key})."""
    m = R.get("osm", {}).get(kind, {})
    if not m: return items
    out = [(nm, g) for nm, g in items if nm not in m]
    return out + [(nm, osm_geo(k)) for nm, k in m.items()]
def river_fix(items):
    """Natural Earth 10m names the Paraguay river 'Paraná' (the scalerank-2 trunk from Mato Grosso, -14.3, down to the
    confluence at Corrientes, -27.3): the line that starts at (-55.08, -14.32) is renamed 'Paraguay' (#river-paraguay)."""
    out = []
    for nm, ls in items:
        if nm == "Paraná":
            par = [l for l in ls if abs(l[0][0] + 55.0753) < 0.01 and abs(l[0][1] + 14.3194) < 0.01]
            rest = [l for l in ls if l not in par]
            if par: out.append(("Paraguay", par))
            if rest: out.append((nm, rest))
        else: out.append((nm, ls))
    return out
def guiana_fix(items):
    """world-atlas puts French Guiana inside #c-france: give it its own #c-french_guiana (France keeps its other parts)."""
    out = []; fg = []
    for nm, polys in items:
        if nm == "France":
            def sa(p): return sum(q[0] for q in p[0]) / len(p[0]) < -40 and sum(q[1] for q in p[0]) / len(p[0]) < 10
            fg += [p for p in polys if sa(p)]; polys = [p for p in polys if not sa(p)]
        out.append((nm, polys))
    return out + ([("French Guiana", fg)] if fg else [])
def do_overlay(name, R):
    W, H = geom(R); g = {}
    def polys_svg(items, prefix):
        parts = []
        for nm, polys in items:
            ds = []
            for poly in polys:
                for r in poly:
                    for pts in ring_variants(R, r):
                        if len(pts) > 2 and in_view(pts, W, H): ds.append(pathd(pts))
            if ds: parts.append(f'<path id="{prefix}-{slug(nm)}" data-name="{nm}" d="{"".join(ds)}"/>')
        return parts
    g["countries"] = polys_svg(osm_swap(guiana_fix(crimea_fix(topo_decode(f"{VEC}/world-atlas_2_countries-10m.json", "countries"))), R, "countries"), "c")
    g["land"] = polys_svg(topo_decode(f"{VEC}/world-atlas_2_land-10m.json", "land"), "land")
    if name in ("us", "bay_area", "northeast", "pacific", "world"):
        g["us_states"] = polys_svg(topo_decode(f"{VEC}/us-atlas_3_states-10m.json", "states"), "st")
    g["lakes"] = polys_svg(geo_polys(f"{VEC}/ne_10m_lakes.geojson", lambda p: p["scalerank"] <= (9 if R["ppd"] > 100 else 3)), "lake")
    riv = []
    rr = R.get("river_rank", 6 if R["ppd"] > 100 else 3)
    for nm, ls in osm_swap(river_fix(geo_lines(f"{VEC}/ne_10m_rivers_lake_centerlines.geojson", lambda p: p["scalerank"] <= rr)), R, "rivers"):
        ds = [pathd(pts, False) for l in ls if len(l) > 1 for pts in ring_variants(R, l) if in_view(pts, W, H)]
        ds = [d for d in ds if d]
        if ds: riv.append(f'<path id="river-{slug(nm) or "x"}" data-name="{nm}" d="{"".join(ds)}"/>')
    g["rivers"] = riv
    places = {}
    for k, (lo, la) in PLACES.items():
        x, y = proj(R, lo, la)
        if -1 <= x <= W + 1 and -1 <= y <= H + 1: places[k] = {"lon": lo, "lat": la, "x": round(x, 1), "y": round(y, 1)}
    g["cities"] = [f'<circle id="p-{k}" cx="{v["x"]}" cy="{v["y"]}" r="{max(3, W / 1200):.1f}"/>' for k, v in places.items()]
    sw = max(1.0, W / 3000)
    style_css = (f"#countries path{{fill:none;stroke:#f2ede3;stroke-width:{sw:.1f};stroke-opacity:.55}}"
                 f"#us_states path{{fill:none;stroke:#f2ede3;stroke-width:{sw * .6:.1f};stroke-opacity:.4}}"
                 f"#land path{{fill:none;stroke:#f2ede3;stroke-width:{sw:.1f}}}#lakes path{{fill:none;stroke:#9fc3e3;stroke-width:{sw * .6:.1f}}}"
                 f"#rivers path{{fill:none;stroke:#9fc3e3;stroke-width:{sw * .7:.1f};stroke-opacity:.6}}#cities circle{{fill:#f2ede3}}")
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">',
           f"<style>{style_css}</style>"]
    for k in ("land", "countries", "us_states", "lakes", "rivers", "cities"):
        if k in g: svg.append(f'<g id="{k}">' + "\n".join(g[k]) + "</g>")
    svg.append("</svg>")
    open(f"{OUT}/{name}_overlay.svg", "w").write("\n".join(svg))
    lon_note = " ; for lon < %g use lon + 360 (Pacific-centred, crosses the antimeridian)" % R["lon0"] if R["lon1"] > 180 else ""
    meta = {"name": name, "width": W, "height": H,
            "projection": "equirectangular (plate carree), WGS84" + (f", x squashed by k=cos({math.degrees(math.acos(R['k'])):.1f}deg) to keep true shapes at this latitude" if R["k"] != 1 else ""),
            "bounds": {"lon_min": R["lon0"], "lon_max": R["lon1"] if R["lon1"] <= 180 else R["lon1"] - 360, "lat_min": R["lat0"], "lat_max": R["lat1"]},
            "px_per_degree_lat": round(R["ppd"], 4), "px_per_degree_lon": round(R["ppd"] * R["k"], 4),
            "formula": f"x = (lon - ({R['lon0']})) * {R['ppd'] * R['k']:.4f} ; y = ({R['lat1']} - lat) * {R['ppd']:.4f}{lon_note}",
            "svg_hint": f'<svg viewBox="0 0 {W} {H}"> - {name}_overlay.svg shares this pixel space (groups: land, countries, us_states, lakes, rivers, cities; paths id c-<country>, st-<state>, p-<place>)',
            "images": sorted(f for f in os.listdir(OUT) if f.startswith(name + "_") and f.endswith((".jpg", ".png"))),
            "credit": {"relief": CREDIT_RELIEF, "sat": CREDIT_ESRI if R["ze"] else (CREDIT_BM if name == "world" else "none (no sat base for this region)")},
            "places": places}
    if name == "world":
        meta["note_satdesat_21600"] = "world_satdesat_21600.jpg is 21600x10800: multiply x,y above by 21600/16384 = 1.318359"
    json.dump(meta, open(f"{OUT}/{name}.json", "w"), indent=1)
    print("  wrote overlay + json", name, flush=True)

if __name__ == "__main__" and sys.argv[1] in REGIONS:
    name = sys.argv[1]; steps = (sys.argv[2] if len(sys.argv) > 2 else "relief,sat,overlay").split(",")
    os.makedirs(OUT, exist_ok=True); R = REGIONS[name]; print(name, geom(R), flush=True)
    if "relief" in steps: do_relief(name, R)
    if "sat" in steps: do_sat(name, R)
    if "overlay" in steps: do_overlay(name, R)

# ---------- Esri aerial close-ups (kept in Web Mercator, no resampling = full sharpness) ----------
AERIALS = {  # name: (z, lon0, lat0, lon1, lat1, places)
  "hsinchu_park_z18": (18, 121.0035, 24.7638, 121.0277, 24.7802, ["hsinchu_science_park", "tsmc_hq_fab12a", "umc_lihsin6_hq", "umc_lihsin3_campus"]),
  "hsinchu_park_z17": (17, 120.990, 24.755, 121.040, 24.790, ["hsinchu_science_park", "tsmc_hq_fab12a", "umc_lihsin6_hq", "umc_lihsin3_campus"]),
  "stanford_z17": (17, -122.1880, 37.4135, -122.1440, 37.4440, ["stanford_university", "hp_garage", "palo_alto"]),
  "palo_alto_hp_garage_z18": (18, -122.1640, 37.4370, -122.1460, 37.4490, ["hp_garage", "palo_alto"]),
  "mit_z17": (17, -71.1150, 42.3460, -71.0730, 42.3740, ["mit_cambridge"]),
  # Ivan project (2026-11-01)
  "moscow_kirillov_blast_z17": (17, 37.7733, 55.7096, 37.8053, 55.7256, ["kirillov_blast_site"]),
  "moscow_sarvarov_blast_z17": (17, 37.7226, 55.5997, 37.7546, 55.6157, ["sarvarov_blast_site"]),
  "olenya_airbase_z16": (16, 33.4160, 68.1323, 33.5039, 68.1716, ["olenya_airbase"]),
  "belaya_airbase_z16": (16, 103.5341, 52.8894, 103.6148, 52.9412, ["belaya_airbase"]),
  "dyagilevo_airbase_z16": (16, 39.5367, 54.6337, 39.6002, 54.6595, ["dyagilevo_airbase"]),
  "ivanovo_severny_airbase_z16": (16, 40.9515, 57.0443, 41.0099, 57.0695, ["ivanovo_severny_airbase"]),
  "alabuga_sez_z16": (16, 51.9622, 55.8119, 52.0714, 55.8577, ["alabuga_drone_factory", "alabuga_nw_new_halls"]),
  "kazan_aircraft_plant_z16": (16, 49.0979, 55.8495, 49.1683, 55.8803, ["kazan_aircraft_plant"]),
  # Paraguay project (2026-11-08)
  "asuncion_city_z15": (15, -57.6700, -25.3500, -57.5200, -25.2450, ["asuncion", "palacio_legislativo", "palacio_de_lopez", "plaza_de_armas",
      "plaza_de_los_heroes", "plaza_de_la_democracia", "banco_central_del_paraguay", "ueno_hq_santa_teresa_3088", "torres_del_paseo_la_galeria",
      "mburuvicha_roga"]),
  "asuncion_congress_z18": (18, -57.6440, -25.2865, -57.6270, -25.2725, ["palacio_legislativo", "palacio_de_lopez", "plaza_de_armas",
      "plaza_de_los_heroes", "plaza_de_la_democracia"]),
  "asuncion_banco_central_z18": (18, -57.5830, -25.2835, -57.5680, -25.2725, ["banco_central_del_paraguay"]),
  "asuncion_ueno_hq_z18": (18, -57.5690, -25.2945, -57.5490, -25.2800, ["ueno_hq_santa_teresa_3088", "torres_del_paseo_la_galeria"]),
  "asuncion_mburuvicha_roga_z18": (18, -57.6090, -25.2985, -57.5945, -25.2875, ["mburuvicha_roga"]),
}
EXTRA = {"stanford_main_quad": (-122.1697, 37.4275), "hoover_tower": (-122.1665, 37.4275), "stanford_research_park": (-122.1480, 37.4110)}
def do_aerial(name):
    z, lon0, lat0, lon1, lat1, keys = AERIALS[name]
    X0, X1 = int(tx(lon0, z)), int(tx(lon1, z)); Y0, Y1 = int(ty(lat1, z)), int(ty(lat0, z))
    W, H = (X1 - X0 + 1) * 256, (Y1 - Y0 + 1) * 256
    im = Image.new("RGB", (W, H)); miss = 0
    for X in range(X0, X1 + 1):
        for Y in range(Y0, Y1 + 1):
            try: im.paste(Image.open(tpath("esri", z, X, Y)).convert("RGB"), ((X - X0) * 256, (Y - Y0) * 256))
            except Exception: miss += 1
    print(name, W, H, "missing", miss)
    save(im, f"aerial_{name}", q=92)
    places = {}
    for k in keys + [k for k in EXTRA]:
        lo, la = PLACES.get(k) or EXTRA[k]
        x, y = (tx(lo, z) - X0) * 256, (ty(la, z) - Y0) * 256
        if 0 <= x <= W and 0 <= y <= H: places[k] = {"lon": lo, "lat": la, "x": round(x, 1), "y": round(y, 1)}
    meta = {"name": f"aerial_{name}", "image": f"aerial_{name}.jpg", "width": W, "height": H, "zoom": z,
            "projection": "Web Mercator (EPSG:3857) - NOT equirectangular",
            "tile_bounds": {"x0": X0, "x1": X1, "y0": Y0, "y1": Y1},
            "formula": f"x = ((lon+180)/360*2^{z} - {X0}) * 256 ; y = ((1 - ln(tan(lat)+sec(lat))/pi)/2*2^{z} - {Y0}) * 256   (lat in radians)",
            "metres_per_px": round(156543.034 * math.cos(math.radians((lat0 + lat1) / 2)) / 2 ** z, 3),
            "source": "Esri World Imagery tiles (server.arcgisonline.com World_Imagery/MapServer), stitched unmodified",
            "credit": CREDIT_ESRI + " (on screen)", "rights": "(c) Esri and its data providers - used under fair use per MANUAL 10.9; credit on screen",
            "places": places}
    json.dump(meta, open(f"{OUT}/aerial_{name}.json", "w"), indent=1)
if __name__ == "__main__" and sys.argv[1] == "aerial":
    for n in (sys.argv[2:] or AERIALS): do_aerial(n)

# ---------- crops of the world bases (no rebuild; same plate carrée as world.json) ----------
CROPS = {  # name: (lon0, lon1, lat0, lat1, places)  — Paraguay project: "Paraguay vs the US", IMF Washington -> Asunción
  "americas": (-130, -20, -58, 55, ["washington_dc", "new_york", "miami", "asuncion", "brasilia", "buenos_aires", "la_paz", "lima",
                                     "bogota", "caracas", "santiago", "sao_paulo", "panama_city", "los_angeles", "houston", "chicago"]),
}
def do_crop(name):
    lon0, lon1, lat0, lat1, keys = CROPS[name]; meta = {"name": name, "projection": "equirectangular (plate carree), crop of the world bases", "variants": {}}
    for src, out, ppd in (("world_night.jpg", f"{name}_night", 16384 / 360), ("world_satdesat_21600.jpg", f"{name}_satdesat", 21600 / 360)):
        x0, x1, y0, y1 = [int(round(v)) for v in ((lon0 + 180) * ppd, (lon1 + 180) * ppd, (90 - lat1) * ppd, (90 - lat0) * ppd)]
        im = Image.open(f"{OUT}/{src}").crop((x0, y0, x1, y1)); save(im, out, q=90)
        meta["variants"][out + ".jpg"] = {"width": im.width, "height": im.height, "source": src, "crop_px": [x0, y0, x1, y1],
            "formula": f"x = (lon + 180) * {ppd:.4f} - {x0} ; y = (90 - lat) * {ppd:.4f} - {y0}",
            "places": {k: {"lon": PLACES[k][0], "lat": PLACES[k][1], "x": round((PLACES[k][0] + 180) * ppd - x0, 1),
                           "y": round((90 - PLACES[k][1]) * ppd - y0, 1)} for k in keys}}
    meta["credit"] = {"night": CREDIT_RELIEF, "satdesat": CREDIT_BM}
    json.dump(meta, open(f"{OUT}/{name}.json", "w"), indent=1); print("  wrote", name + ".json")
if __name__ == "__main__" and sys.argv[1] == "crop":
    for n in (sys.argv[2:] or CROPS): do_crop(n)
