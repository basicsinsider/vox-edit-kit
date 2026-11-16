"""NVIDIA project (2026-11-16) map regions, run through tools/map_kit.py unchanged (entries added at runtime).
Usage: MK_CACHE=work/nv-maps/tiles MK_VEC=work/nv-maps/vec .venv/bin/python work/nv-maps/nv_maps.py <region> [steps] | aerial <name>...
The REGIONS / PLACES / AERIALS dicts below are meant to be merged into tools/map_kit.py by the lead."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tools"))
import map_kit as mk

REGIONS = {
  # SE Asia: smuggling routes Singapore/Malaysia -> China, engineers flying to Malaysia
  "southeast_asia": dict(lon0=95, lon1=125, lat0=-6.5, lat1=31.5, ppd=185, k=0.9781, zt=8, ze=8, zf=9),
  # whole China + neighbours (Tokyo/Osaka at the right edge)
  "china": dict(lon0=72, lon1=142, lat0=16, lat1=55, ppd=112, k=0.8141, zt=7, ze=7, zf=14),
  # Pearl River Delta close-up: Hong Kong, Shenzhen, the border, Shekou, Macau edge
  "pearl_river_delta": dict(lon0=113.4, lon1=114.6, lat0=22.0, lat1=22.9, ppd=5600, k=0.9242, zt=13, ze=13, zf=1.6),
}
PLACES = {
  "singapore": (103.8198, 1.3521), "kuala_lumpur": (101.6869, 3.1390), "johor_bahru": (103.7414, 1.4927),
  "cyberjaya": (101.6500, 2.9213), "penang": (100.3327, 5.4164), "batam": (104.0305, 1.1301), "kulai": (103.6059, 1.6569),
  "bangkok": (100.5018, 13.7563), "jakarta": (106.8456, -6.2088), "ho_chi_minh_city": (106.6297, 10.8231),
  "phnom_penh": (104.9282, 11.5564), "vientiane": (102.6331, 17.9757), "yangon": (96.1951, 16.8661), "naypyidaw": (96.1297, 19.7633),
  "kuching": (110.3592, 1.5535), "bandar_seri_begawan": (114.9398, 4.9031), "da_nang": (108.2022, 16.0544), "cebu": (123.8854, 10.3157),
  "hangzhou": (120.1551, 30.2741), "chengdu": (104.0665, 30.5723), "chongqing": (106.5516, 29.5630), "wuhan": (114.3055, 30.5928),
  "xian": (108.9398, 34.3416), "tianjin": (117.3616, 39.3434), "hefei": (117.2272, 31.8206), "kunming": (102.8329, 24.8801),
  "nanning": (108.3665, 22.8170), "haikou": (110.1999, 20.0440), "macau": (113.5439, 22.1987), "dongguan": (113.7518, 23.0205),
  "zhuhai": (113.5767, 22.2707), "ulaanbaatar": (106.9057, 47.8864), "new_delhi": (77.2090, 28.6139), "dhaka": (90.4125, 23.8103),
  "kathmandu": (85.3240, 27.7172), "harbin": (126.5350, 45.8038), "shenyang": (123.4315, 41.8057), "qingdao": (120.3826, 36.0671),
  "urumqi": (87.6168, 43.8256), "lhasa": (91.1172, 29.6500), "hsinchu": (120.9675, 24.8138),
  # Pearl River Delta close-up (OpenStreetMap / Nominatim positions, checked by eye on the Esri imagery)
  "hong_kong_central": (114.1583, 22.2818), "victoria_harbour": (114.1700, 22.2930), "mong_kok": (114.1698, 22.3204),
  "sham_shui_po": (114.1623, 22.3307), "golden_computer_arcade": (114.1620, 22.3320),
  "shenzhen_futian": (114.0550, 22.5464), "huaqiangbei": (114.0815, 22.5448), "seg_plaza": (114.0823, 22.5440),
  "huaqiang_electronics_world": (114.0810, 22.5442), "shekou_port": (113.9088, 22.4719),
  "hk_macau_ferry_terminal": (114.1524, 22.2887), "lo_wu_control_point": (114.1139, 22.5297),
  "futian_checkpoint": (114.0641, 22.5184), "shenzhen_bay_port": (113.9460, 22.5040), "hk_airport": (113.9185, 22.3080),
}
PLACES.update({
  # xAI Memphis: Colossus 1 = former Electrolux plant, 3231 Paul R Lowry Rd (building centre located by eye on Esri z16; the
  # Nominatim address point sits on the road at the gate); Colossus 2 = Tulane Rd, Whitehaven ("MACROHARD" painted on the roof)
  "xai_colossus_1": (-90.1566, 35.0601), "colossus_1_address_3231_paul_r_lowry_rd": (-90.1522, 35.0601),
  "xai_colossus_2_macrohard": (-90.0350, 34.9981),
  # Johor: Sedenak Tech Park (Kulai) - twin white data halls visible in Esri's Feb 2021 imagery (located by eye)
  "sedenak_tech_park_data_halls": (103.4174, 1.6972), "sedenak_tech_park": (103.4120, 1.7020),
  "nusajaya_tech_park": (103.5951, 1.4308),  # Iskandar Puteri (OSM industrial area centre); Esri 2025 imagery
})
AERIALS = {
  "shenzhen_huaqiangbei_z17": (17, 114.0680, 22.5320, 114.1000, 22.5560, ["huaqiangbei", "seg_plaza", "huaqiang_electronics_world", "shenzhen_futian"]),
  "memphis_xai_colossus_z16": (16, -90.1850, 35.0400, -90.1250, 35.0800, ["xai_colossus_1", "colossus_1_address_3231_paul_r_lowry_rd"]),
  "memphis_xai_colossus2_z16": (16, -90.0650, 34.9800, -90.0050, 35.0200, ["xai_colossus_2_macrohard"]),
  "johor_data_centers_z16": (16, 103.3850, 1.6800, 103.4400, 1.7250, ["sedenak_tech_park_data_halls", "sedenak_tech_park"]),
  "johor_nusajaya_tech_park_z16": (16, 103.5780, 1.4140, 103.6120, 1.4420, ["nusajaya_tech_park"]),
}
mk.REGIONS.update(REGIONS); mk.PLACES.update(PLACES); mk.AERIALS.update(AERIALS)
REGIONS["pearl_river_delta"].update(vec_mask=True, gray_mask=13)

# Pearl River Delta: the DEM coast (> 0.5 m) misses reclaimed land (HK airport, Shenzhen Bay, Macau) and floods the delta's fish
# ponds; Natural Earth is far too coarse. Overpass was unreachable, so the land/water mask comes from Esri's
# Canvas/World_Light_Gray_Base tiles (same server as the imagery; water is one flat grey-violet ~ (208,206,212)).
import map_tiles as mt
import numpy as np
from PIL import Image, ImageFilter
mt.URL["gray"] = "https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer/tile/{z}/{y}/{x}"
mt.EXT["gray"] = "jpg"
_lwm = mk.land_water_mask
def gray_land(R, W, H):
    from scipy import ndimage as nd
    M, X0, Y0 = mk.load_mosaic("gray", R["gray_mask"], R)
    A = mk.resample(M, X0, Y0, R["gray_mask"], R, W, H); del M
    lum = A @ np.array([0.299, 0.587, 0.114], np.float32); del A
    water = nd.median_filter(lum < 218, 5)
    land = nd.binary_opening(~water, np.ones((5, 5), bool))  # drops bridges / causeway lines drawn over the sea
    lab, n = nd.label(~land); sz = nd.sum(np.ones_like(lab), lab, range(1, n + 1))
    small = np.zeros(n + 1, bool); small[1:] = sz < 400  # ponds / specks -> land
    land = land | small[lab]
    lab, n = nd.label(land); sz = nd.sum(np.ones_like(lab), lab, range(1, n + 1))
    tiny = np.zeros(n + 1, bool); tiny[1:] = sz < 60  # rocks / boats -> sea
    land = land & ~tiny[lab]
    return Image.fromarray((land * 255).astype(np.uint8))
def land_water_mask(R, W, H):
    return gray_land(R, W, H) if R.get("gray_mask") else _lwm(R, W, H)
mk.land_water_mask = land_water_mask


def mask_paths(m, tol=0.8):
    """Binary mask -> SVG path d (closed contours, use fill-rule evenodd)."""
    from skimage import measure
    pm = np.pad(m.astype(np.float32), 1)
    out = []
    for c in measure.find_contours(pm, 0.5):
        c = measure.approximate_polygon(c, tol)
        if len(c) < 4: continue
        out.append("M" + "L".join(f"{x - 1:.1f},{y - 1:.1f}" for y, x in c) + "Z")
    return "".join(out)
def osm_mask(R, W, H, key):
    from PIL import ImageDraw
    im = Image.new("L", (W, H), 0); d = ImageDraw.Draw(im)
    for poly in mk.osm_geo(key):
        for i, r in enumerate(poly): d.polygon(mk.ring_px(R, r), fill=255 if i == 0 else 0)
    return np.asarray(im) > 127
def prd_overlay(name="pearl_river_delta"):
    """Replace the coarse Natural Earth land / HK / Macau / China paths with ones traced from the landmask (Esri grey-base
    coast) cut by the OpenStreetMap Hong Kong (R913110) and Macau (R1867188) boundaries; add the HK-Shenzhen border line."""
    import re
    R = REGIONS[name]; W, H = mk.geom(R); svgp = f"{mk.OUT}/{name}_overlay.svg"; svg = open(svgp).read()
    land = np.asarray(Image.open(f"{mk.OUT}/{name}_landmask.png")) > 127
    hk = osm_mask(R, W, H, "R913110") & land; mo = osm_mask(R, W, H, "R1867188") & land; cn = land & ~hk & ~mo
    def rep(svg, pid, nm, m):
        new = f'<path id="{pid}" data-name="{nm}" fill-rule="evenodd" d="{mask_paths(m)}"/>'
        svg2, n = re.subn(rf'<path id="{pid}"[^>]*/>', lambda _: new, svg)
        return svg2 if n else svg.replace('<g id="countries">', '<g id="countries">' + new + "\n")
    svg = rep(svg, "c-hong_kong", "Hong Kong", hk); svg = rep(svg, "c-macao", "Macao", mo); svg = rep(svg, "c-china", "China", cn)
    svg = re.sub(r'<g id="land">.*?</g>', lambda _: f'<g id="land"><path id="land-x" fill-rule="evenodd" d="{mask_paths(land)}"/></g>', svg, flags=re.S)
    # HK - mainland boundary (Shenzhen Bay -> Shenzhen River -> Sha Tau Kok -> Mirs Bay), from the OSM HK outer ring
    ring = max((p[0] for p in mk.osm_geo("R913110")), key=len)
    runs, cur = [], []
    for lo, la in ring:
        if la > 22.485 and 113.93 < lo < 114.245: cur.append(mk.proj(R, lo, la))
        elif cur: runs.append(cur); cur = []
    if cur: runs.append(cur)
    d = "".join(mk.pathd(r, False) for r in runs if len(r) > 1)
    sw = max(1.0, W / 3000)
    svg = svg.replace("</style>", f"#borders path{{fill:none;stroke:#f2ede3;stroke-width:{sw * 1.2:.1f};stroke-dasharray:{sw * 6:.0f} {sw * 4:.0f}}}</style>")
    svg = svg.replace('<g id="lakes">', f'<g id="borders"><path id="b-hk_mainland_border" data-name="Hong Kong - Shenzhen boundary (OSM)" d="{d}"/></g>\n<g id="lakes">')
    open(svgp, "w").write(svg); print("  prd overlay: land/hk/macao/china traced from landmask + border", flush=True)

if __name__ == "__main__":
    a = sys.argv[1]
    if a in REGIONS:
        R = REGIONS[a]; steps = (sys.argv[2] if len(sys.argv) > 2 else "relief,sat,overlay").split(",")
        print(a, mk.geom(R), flush=True)
        if "relief" in steps: mk.do_relief(a, R)
        if "sat" in steps: mk.do_sat(a, R)
        if "overlay" in steps:
            mk.do_overlay(a, R)
            if a == "pearl_river_delta": prd_overlay(a)
    elif a == "aerial":
        for n in sys.argv[2:]: mk.do_aerial(n)
