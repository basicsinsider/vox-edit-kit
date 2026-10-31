from PIL import Image, ImageDraw, ImageFilter
import math
src = Image.open('/home/user/vox-edit-kit/assets/c2/objects/ck722.jpg').convert('RGB')
W, H = src.size
mask = Image.new('L', (W, H), 0)
d = ImageDraw.Draw(mask)
body = [(1200,1415),(1260,1405),(1320,1410),(1400,1490),(1460,1580),(1470,1650),(1460,1770),(1400,1840),
        (1040,2030),(960,2020),(880,1960),(830,1840),(830,1720),(870,1680)]
d.polygon(body, fill=255)
mask = mask.filter(ImageFilter.MinFilter(9)).filter(ImageFilter.GaussianBlur(2.5))
out = Image.new('RGBA', (W, H), (0,0,0,0))
out.paste(src, (0,0), mask)
# leads: silver wires drawn (the photo's wires sit on a busy box)
dl = ImageDraw.Draw(out)
leads0 = [((1355,1462),(2820,368)), ((1412,1527),(2872,392)), ((1458,1597),(2920,508))]
leads = [(a, (int(a[0]+(b[0]-a[0])*0.5), int(a[1]+(b[1]-a[1])*0.5))) for a,b in leads0]
for (a, b) in leads:
    for w, col in ((13,(70,72,76,255)), (9,(168,170,172,255)), (4,(225,226,228,255))):
        dl.line([a, b], fill=col, width=w)
# re-paste body over the lead roots
out.paste(src, (0,0), mask)
out = out.crop((780, 300, 3000, 2100))
ang = math.degrees(math.atan2(-(420-1720), 2870-1150))  # leads direction (image y down)
out = out.rotate(-(90 - (-ang)) , resample=Image.BICUBIC, expand=True)
bb = out.getbbox(); out = out.crop(bb)
out.thumbnail((1400, 1400))
out.save('/home/user/vox-edit-kit/assets/c2/cutouts/transistor_early.png')
print(out.size)
import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage
im = Image.open('/home/user/vox-edit-kit/_tmp/c2s01/bottle.jpg').convert('RGB')
a = np.asarray(im).astype(float)
# background = connected region from border close to local grey
bg = np.median(np.concatenate([a[:20].reshape(-1,3), a[-20:].reshape(-1,3), a[:, :20].reshape(-1,3)]), axis=0)
rowbg = np.median(np.concatenate([a[:, :40], a[:, -40:]], axis=1), axis=1)[:, None, :]
dist = np.sqrt(((a - rowbg) ** 2).sum(-1))
sat = a.max(-1) - a.min(-1)
cand = (dist < 30) & (sat < 26)
lab, n = ndimage.label(cand)
border = set(np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))) - {0}
bgm = np.isin(lab, list(border))
fg = ~bgm
fg = ndimage.binary_opening(fg, iterations=6)
fg = ndimage.binary_fill_holes(fg)
lab2, n2 = ndimage.label(fg); sizes = ndimage.sum(fg, lab2, range(1, n2 + 1)); fg = lab2 == (np.argmax(sizes) + 1)
m = Image.fromarray((fg * 255).astype(np.uint8)).filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(1.5))
out = im.convert('RGBA'); out.putalpha(m); out = out.crop(out.getbbox())
out.save('/home/user/vox-edit-kit/assets/c2/cutouts/glass_bottle_cut.png'); print(out.size)
from PIL import Image, ImageDraw, ImageFilter
src = Image.open('/home/user/vox-edit-kit/assets/c2/objects/early_triode_vacuum_tubes.jpg').convert('RGB')
m = Image.new('L', src.size, 0)
P = [(228,25),(246,30),(262,90),(300,120),(345,160),(370,240),(378,400),(378,980),(360,1050),(330,1090),(330,1330),(300,1345),(130,1345),(110,1330),(110,1090),(85,1050),(68,980),(66,400),(75,240),(105,160),(160,115),(212,90)]
ImageDraw.Draw(m).polygon(P, fill=255)
m = m.filter(ImageFilter.GaussianBlur(2))
o = src.convert('RGBA'); o.putalpha(m); o = o.crop(o.getbbox())
o.save('/home/user/vox-edit-kit/assets/c2/cutouts/vacuum_tube_tall_cut.png'); print(o.size)
