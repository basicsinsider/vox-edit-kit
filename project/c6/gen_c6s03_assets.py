"""c6s03 derived assets (run with .venv/bin/python). Re-run after dropping a real Fei Hua portrait at
_tmp/c6s03/raw/fei_hua_1971.jpg (or assets/c6/photos/fei_hua_*.jpg) to replace the fallback circle."""
import glob, os
from PIL import Image, ImageOps, ImageFilter
Image.MAX_IMAGE_PIXELS = None
D = 'assets/c6/derived/c6s03/'
# Pacific atlas card for C6S102: lon 112E..115W, lat 52..12N (pacific.json: x=(lon-100)*44, y=(60-lat)*44)
p = Image.open('assets/maps/kit/pacific_atlas.jpg').crop((528, 352, 6380, 2112))
p.resize((3440, round(3440 * 1760 / 5852)), Image.LANCZOS).save(D + 'pacific_atlas_card.jpg', quality=90)
# Fei Hua circle (C6S106/107): real portrait if present, else the neutral silhouette (documented fallback)
src = [f for f in glob.glob('assets/c6/photos/fei_hua_*.jpg') + ['_tmp/c6s03/raw/fei_hua_1971.jpg'] if os.path.exists(f)]
ok = None
for f in src:
    try: ok = Image.open(f).convert('RGB'); break
    except Exception: pass
if ok is not None:
    w, h = ok.size; s = min(w, h)
    c = ok.crop(((w - s) // 2, max(0, int(h * 0.08)), (w - s) // 2 + s, max(0, int(h * 0.08)) + s)).resize((520, 520), Image.LANCZOS)
    ImageOps.grayscale(c).convert('RGB').save(D + 'fei_hua_circle.jpg', quality=92); print('fei: real portrait from', f)
else:
    # typographic name reveal: his name in Chinese (as an image - our fonts have no CJK), ink on paper
    from PIL import ImageDraw, ImageFont
    pap = Image.open('assets/textures/paper_cream_02.jpg').convert('RGB').resize((520, 520))
    c = Image.blend(Image.new('RGB', (520, 520), (228, 220, 203)), pap, 0.45)
    f = ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc', 170)
    d = ImageDraw.Draw(c); d.text((260, 262), '費驊', font=f, fill=(20, 27, 36), anchor='mm')
    c = c.filter(ImageFilter.GaussianBlur(0.6))
    c.save(D + 'fei_hua_circle.jpg', quality=92); print('fei: FALLBACK name card (real portrait missing)')
