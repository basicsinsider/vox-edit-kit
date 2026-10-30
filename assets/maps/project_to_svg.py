#!/usr/bin/env python3
"""Project us_states.geojson + mississippi.geojson into the pixel space of us_basemap.jpg.

Projection: plate carree (equirectangular, EPSG:4326 lon/lat treated linearly).
  Image: 6400 x 3200 px, bounds lon -128..-64 (W..E), lat 20..52 (S..N), 100 px per degree.
  x = (lon - LON_MIN) * PPD          y = (LAT_MAX - lat) * PPD
  (pixel (0,0) = top-left corner of the top-left pixel = lon -128, lat 52)

Outputs (next to this script):
  us_overlay.json  - width/height/bounds, per-state SVG path "d", Mississippi path, west/east region paths,
                     pixel coords of key places
  us_overlay.svg   - same paths in one SVG (viewBox 0 0 6400 3200) for quick inspection
  us_overlay_preview.jpg (with --preview) - basemap with overlay drawn, downsized, for sanity checking

Requires: shapely (>=2), and Pillow for --preview.
  uv venv /tmp/mapvenv && uv pip install --python /tmp/mapvenv/bin/python shapely pillow
  /tmp/mapvenv/bin/python project_to_svg.py [--preview]
"""
import json, os, sys
from shapely.geometry import shape, Polygon, MultiPolygon, LineString, mapping
from shapely.ops import unary_union
from shapely.validation import make_valid

HERE = os.path.dirname(os.path.abspath(__file__))
LON_MIN, LON_MAX, LAT_MIN, LAT_MAX = -128.0, -64.0, 20.0, 52.0
PPD = 100.0
W, H = int((LON_MAX - LON_MIN) * PPD), int((LAT_MAX - LAT_MIN) * PPD)

def polys_only(g):
    """make_valid can return a GeometryCollection with stray lines; keep polygonal parts."""
    g = make_valid(g)
    if isinstance(g, (Polygon, MultiPolygon)):
        return g
    ps = []
    for p in getattr(g, "geoms", []):
        if isinstance(p, Polygon): ps.append(p)
        elif isinstance(p, MultiPolygon): ps.extend(p.geoms)
    return MultiPolygon(ps)

def px(lon, lat):
    return ((lon - LON_MIN) * PPD, (LAT_MAX - lat) * PPD)

def fmt(v):
    s = f"{v:.1f}"
    return s[:-2] if s.endswith(".0") else s

def ring_d(coords):
    pts = [px(*c[:2]) for c in coords]
    if len(pts) > 1 and pts[0] == pts[-1]:
        pts = pts[:-1]
    out, last = [], None
    for x, y in pts:
        p = (fmt(x), fmt(y))
        if p != last:
            out.append(f"{p[0]} {p[1]}"); last = p
    return "M" + "L".join(out) + "Z"

def poly_d(geom):
    if geom.is_empty:
        return ""
    polys = [geom] if isinstance(geom, Polygon) else [g for g in getattr(geom, "geoms", []) if isinstance(g, Polygon)]
    parts = []
    for p in polys:
        parts.append(ring_d(p.exterior.coords))
        parts += [ring_d(i.coords) for i in p.interiors]
    return "".join(parts)

def line_d(coords):
    pts = [px(*c[:2]) for c in coords]
    return "M" + "L".join(f"{fmt(x)} {fmt(y)}" for x, y in pts)

def bbox_px(geom):
    a, b, c, d = geom.bounds
    x0, y1 = px(a, b); x1, y0 = px(c, d)
    return [round(x0, 1), round(y0, 1), round(x1, 1), round(y1, 1)]

def main():
    states = json.load(open(os.path.join(HERE, "us_states.geojson")))["features"]
    river = json.load(open(os.path.join(HERE, "mississippi.geojson")))["features"][0]["geometry"]["coordinates"]

    conus = {}
    for f in states:
        p = f["properties"]
        if not p.get("conus"):
            continue
        conus[p["abbr"]] = (p["name"], polys_only(shape(f["geometry"])))

    out_states = {}
    for ab, (name, g) in sorted(conus.items()):
        c = g.representative_point()
        out_states[ab] = {"name": name, "d": poly_d(g), "bbox": bbox_px(g),
                          "label": [round(v, 1) for v in px(c.x, c.y)]}

    # --- West/East split exactly along the river ---------------------------------------
    # Divider = straight north from Lake Itasca to lat 50 (past the Canadian border) + the river
    # + straight south from the river mouth to lat 20. Everything left of it = "west".
    divider = [(river[0][0], 50.5)] + [tuple(c) for c in river] + [(river[-1][0], 19.0)]
    west_half = polys_only(Polygon(divider + [(-140, 19.0), (-140, 50.5)]))
    us = polys_only(unary_union([g for _, g in conus.values()]))
    west_split = polys_only(us.intersection(west_half))
    east_split = polys_only(us.difference(west_half))

    # --- West/East by whole-state grouping ----------------------------------------------
    WEST_RIVER_STATES = {"MN", "IA", "MO", "AR", "LA"}
    EAST_RIVER_STATES = {"WI", "IL", "KY", "TN", "MS"}
    west_states, east_states = [], []
    for ab, (_, g) in conus.items():
        if ab in WEST_RIVER_STATES: west_states.append(ab)
        elif ab in EAST_RIVER_STATES: east_states.append(ab)
        else:
            (west_states if g.intersection(west_half).area > g.area / 2 else east_states).append(ab)
    west_group = polys_only(unary_union([conus[a][1] for a in west_states]))
    east_group = polys_only(unary_union([conus[a][1] for a in east_states]))

    rpx = [px(*c) for c in river]
    rlen = sum(((rpx[i+1][0]-rpx[i][0])**2 + (rpx[i+1][1]-rpx[i][1])**2) ** 0.5 for i in range(len(rpx)-1))

    places_ll = {
        "indianapolis": (-86.1581, 39.7684),
        "eli_lilly_hq_indianapolis": (-86.1450, 39.7580),
        "palo_alto": (-122.1430, 37.4419),
        "new_york_city": (-74.0060, 40.7128),
        "boston": (-71.0589, 42.3601),
        "mississippi_mouth_southwest_pass": tuple(river[-1]),
        "mississippi_head_of_passes": (-89.2530, 29.1530),
        "mississippi_source_lake_itasca": tuple(river[0]),
        "new_orleans": (-90.0715, 29.9511),
        "st_louis": (-90.1994, 38.6270),
    }
    places = {k: {"lon": v[0], "lat": v[1], "x": round(px(*v)[0], 1), "y": round(px(*v)[1], 1)}
              for k, v in places_ll.items()}

    data = {
        "image": "us_basemap.jpg", "width": W, "height": H,
        "projection": "equirectangular (plate carree), WGS84 lon/lat linear",
        "bounds": {"lon_min": LON_MIN, "lon_max": LON_MAX, "lat_min": LAT_MIN, "lat_max": LAT_MAX},
        "px_per_degree": PPD,
        "formula": "x = (lon + 128) * 100 ; y = (52 - lat) * 100",
        "states": out_states,
        "mississippi": {"d": line_d(river), "length_px": round(rlen, 1), "bbox": bbox_px(LineString(river))},
        "regions": {
            "west_of_mississippi": {"d": poly_d(west_split), "method": "CONUS clipped exactly along river (+ meridian north of Itasca)"},
            "east_of_mississippi": {"d": poly_d(east_split), "method": "CONUS clipped exactly along river (+ meridian north of Itasca)"},
            "west_by_state": {"d": poly_d(west_group), "states": sorted(west_states)},
            "east_by_state": {"d": poly_d(east_group), "states": sorted(east_states)},
            "conus_outline": {"d": poly_d(us)},
        },
        "places": places,
    }
    with open(os.path.join(HERE, "us_overlay.json"), "w") as fh:
        json.dump(data, fh, separators=(",", ":"))

    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">',
           f'<path id="west" d="{data["regions"]["west_of_mississippi"]["d"]}" fill="#ff8a3d" fill-opacity=".35"/>',
           f'<path id="east" d="{data["regions"]["east_of_mississippi"]["d"]}" fill="#3d8aff" fill-opacity=".35"/>']
    for ab, s in out_states.items():
        svg.append(f'<path id="{ab}" d="{s["d"]}" fill="none" stroke="#fff" stroke-width="3"/>')
    svg.append(f'<path id="mississippi" d="{data["mississippi"]["d"]}" fill="none" stroke="#00e5ff" stroke-width="8" stroke-linejoin="round"/>')
    for k, p in places.items():
        svg.append(f'<circle id="{k}" cx="{p["x"]}" cy="{p["y"]}" r="18" fill="#ff2050"/>')
    svg.append("</svg>")
    open(os.path.join(HERE, "us_overlay.svg"), "w").write("\n".join(svg))

    if "--preview" in sys.argv:
        from PIL import Image, ImageDraw
        Image.MAX_IMAGE_PIXELS = None
        s = 0.25
        img = Image.open(os.path.join(HERE, "us_basemap.jpg")).convert("RGB").resize((int(W*s), int(H*s)))
        ov = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(ov)
        def fillgeom(g, col):
            for p in ([g] if isinstance(g, Polygon) else g.geoms):
                if isinstance(p, Polygon):
                    d.polygon([(px(*c)[0]*s, px(*c)[1]*s) for c in p.exterior.coords], fill=col)
        fillgeom(west_split, (255, 140, 60, 70)); fillgeom(east_split, (60, 140, 255, 70))
        for _, g in conus.values():
            for p in ([g] if isinstance(g, Polygon) else g.geoms):
                d.line([(px(*c)[0]*s, px(*c)[1]*s) for c in p.exterior.coords], fill=(255, 255, 255, 200), width=1)
        d.line([(x*s, y*s) for x, y in rpx], fill=(0, 230, 255, 255), width=3)
        for k, p in places.items():
            d.ellipse([p["x"]*s-5, p["y"]*s-5, p["x"]*s+5, p["y"]*s+5], fill=(255, 30, 80, 255))
        Image.alpha_composite(img.convert("RGBA"), ov).convert("RGB").save(os.path.join(HERE, "us_overlay_preview.jpg"), quality=88)
    print(f"wrote us_overlay.json ({len(out_states)} states, river {len(river)} pts, {rlen:.0f}px)")

if __name__ == "__main__":
    main()
