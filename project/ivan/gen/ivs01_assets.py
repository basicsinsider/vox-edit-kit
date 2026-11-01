"""ivs01 derived map assets (run from repo root with .venv/bin/python).
Outputs assets/ivan/ivs01/derived/: ee_night.jpg / ee_atlas.jpg (eastern_europe crop lon 22-48, lat 43-58, x0.5),
ee_ru.png / ee_ua.png (white+alpha country fills in that space), ru_night.jpg (russia kit x0.4) + ru_ru.png,
paths.json (simplified outline paths in each crop's pixel space)."""
import json, re
from PIL import Image, ImageDraw, ImageFilter
Image.MAX_IMAGE_PIXELS = None
K = 'assets/maps/kit/'; O = 'assets/ivan/ivs01/derived/'

def subpaths(d):
    out = []
    for sp in re.split(r'(?=M)', d):
        pts = [tuple(map(float, p)) for p in re.findall(r'(-?[\d.]+),(-?[\d.]+)', sp)]
        if len(pts) < 3: continue
        if any(abs(pts[i][0]-pts[i-1][0]) > 400 for i in range(1, len(pts))): continue
        out.append(pts)
    return out

def get(svgfile, cid):
    s = open(K + svgfile).read()
    m = re.search(r'<path[^>]*id="%s"[^>]*>' % cid, s)
    return subpaths(re.search(r' d="([^"]*)"', m.group(0)).group(1))

def rdp(pts, eps):
    if len(pts) < 3: return pts
    (x1, y1), (x2, y2) = pts[0], pts[-1]
    dx, dy = x2-x1, y2-y1; n = (dx*dx+dy*dy) ** 0.5 or 1e-9
    dm, im = 0, 0
    for i in range(1, len(pts)-1):
        dd = abs(dy*pts[i][0] - dx*pts[i][1] + x2*y1 - y2*x1) / n
        if dd > dm: dm, im = dd, i
    if dm > eps: return rdp(pts[:im+1], eps)[:-1] + rdp(pts[im:], eps)
    return [pts[0], pts[-1]]

def simp(pts, eps):
    h = len(pts)//2
    return rdp(pts[:h+1], eps)[:-1] + rdp(pts[h:], eps)

def crop_space(subs, x0, y0, s, W, H, eps=1.2, minlen=8):
    paths = []
    for pts in subs:
        q = [((x-x0)*s, (y-y0)*s) for x, y in pts]
        if max(p[0] for p in q) < -50 or min(p[0] for p in q) > W+50 or max(p[1] for p in q) < -50 or min(p[1] for p in q) > H+50: continue
        q = simp(q, eps)
        if len(q) < 3: continue
        xs = [p[0] for p in q]; ys = [p[1] for p in q]
        if max(xs)-min(xs) + max(ys)-min(ys) < minlen: continue
        paths.append(q)
    return paths

def d_of(paths):
    return ' '.join('M' + ' L'.join('%.1f %.1f' % p for p in q) + ' Z' for q in paths)

def mask(paths, W, H, blur=1.2):
    m = Image.new('L', (W, H), 0); dr = ImageDraw.Draw(m)
    for q in paths: dr.polygon(q, fill=255)
    m = m.filter(ImageFilter.GaussianBlur(blur))
    im = Image.new('RGBA', (W, H), (255, 255, 255, 0)); im.putalpha(m); return im

out = {}
# --- Eastern Europe crop
kx, ky = 147.768, 240.0
x0, x1, y0, y1 = (22-20)*kx, (48-20)*kx, (62-58)*ky, (62-43)*ky
s = 0.5; W, H = round((x1-x0)*s), round((y1-y0)*s)
for f in ['night', 'atlas']:
    im = Image.open(K + 'eastern_europe_%s.jpg' % f).crop((round(x0), round(y0), round(x1), round(y1))).resize((W, H), Image.LANCZOS)
    im.save(O + 'ee_%s.jpg' % f, quality=88)
ru = crop_space(get("eastern_europe_overlay.svg", "c-russia"), x0, y0, s, W, H, eps=2.5, minlen=30)
ua = crop_space(get("eastern_europe_overlay.svg", "c-ukraine"), x0, y0, s, W, H, eps=2.0, minlen=30)
cr = crop_space(get('eastern_europe_overlay.svg', 'c-crimea'), x0, y0, s, W, H)
mask(ru, W, H).save(O + 'ee_ru.png'); mask(ua, W, H).save(O + 'ee_ua.png')
pl = json.load(open(K + 'eastern_europe.json'))['places']
out['ee'] = {'W': W, 'H': H, 'ru': d_of(ru), 'ua': d_of(ua), 'crimea': d_of(cr),
             'places': {k: [round((v['x']-x0)*s, 1), round((v['y']-y0)*s, 1)] for k, v in pl.items()},
             'formula': 'x = ((lon-20)*147.768 - %.1f)*0.5 ; y = ((62-lat)*240 - %.1f)*0.5' % (x0, y0)}
# --- Russia-wide
s2 = 0.4; R = json.load(open(K + 'russia.json')); W2, H2 = round(R['width']*s2), round(R['height']*s2)
Image.open(K + 'russia_night.jpg').resize((W2, H2), Image.LANCZOS).save(O + 'ru_night.jpg', quality=88)
ru2 = crop_space(get('russia_overlay.svg', 'c-russia'), 0, 0, s2, W2, H2, eps=3.0, minlen=40)
ua2 = crop_space(get('russia_overlay.svg', 'c-ukraine'), 0, 0, s2, W2, H2, eps=3.0, minlen=40)
mask(ru2, W2, H2).save(O + 'ru_ru.png')
out['ru'] = {'W': W2, 'H': H2, 'ru': d_of(ru2), 'ua': d_of(ua2),
             'places': {k: [round(v['x']*s2, 1), round(v['y']*s2, 1)] for k, v in R['places'].items()}}
json.dump(out, open(O + 'paths.json', 'w'))
print(W, H, W2, H2, len(out['ee']['ru']), len(out['ee']['ua']), len(out['ru']['ru']))
