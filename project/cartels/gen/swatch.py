"""Palette swatch for the Cartels video -> references/palette_cartels.png (lib/palette_cartels.css)."""
from PIL import Image, ImageDraw, ImageFont
F = 'assets/fonts/'
hk = lambda s: ImageFont.truetype(F + 'Haskoy-ExtraBold.otf', s)
ch = lambda s: ImageFont.truetype(F + 'CooperHewitt-Bold.otf', s)
cp = lambda s: ImageFont.truetype(F + 'CrimsonPro-Italic-VariableFont_wght.ttf', s)
W, H = 1920, 1080
im = Image.new('RGB', (W, H), '#100e0c'); d = ImageDraw.Draw(im)
d.text((96, 72), 'US vs CARTELS', font=hk(96), fill='#f3ede1')
d.text((100, 184), 'PALETTE  ·  SEARCHING LESSONS  ·  2026-11-22', font=ch(26), fill='#c8c1b6')
rows = [('EMBER', '#ec6424', ['#8a3311', '#ec6424', '#f7b48c'], 'The cartels — territory, bosses, roadblocks, drug routes north'),
        ('STEEL', '#6f93b4', ['#2f4a63', '#6f93b4', '#bcd1e4'], 'The United States — White House, CIA, FBI, DEA, drones, boat strikes'),
        ('OLIVE', '#9a9a4e', ['#50512a', '#9a9a4e', '#d3d39c'], "Mexico's state — Sheinbaum, army, navy, National Guard, special forces"),
        ('YELLOW', '#f4cf3d', ['#b5911a', '#f4cf3d', '#f9e591'], 'Only the highlighter + the one key number of a scene')]
y = 270
for name, main, sh, mean in rows:
    for i, c in enumerate(sh):
        d.rectangle([96 + i * 150, y, 96 + i * 150 + 140, y + 130], fill=c)
    d.text((580, y + 6), name, font=hk(56), fill=main)
    d.text((582, y + 78), mean, font=cp(36), fill='#f3ede1')
    y += 158
# grounds
d.rectangle([96, 912, 476, 1008], fill='#e9e0cd'); d.text((120, 930), 'SAND PAPER', font=ch(26), fill='#1d1a16'); d.text((120, 966), 'files · charts · maps', font=cp(28), fill='#57504a')
d.rectangle([500, 912, 880, 1008], fill='#221e1a', outline='#3b3631'); d.text((524, 930), 'CHARCOAL NIGHT', font=ch(26), fill='#f3ede1'); d.text((524, 966), 'footage · cinematic', font=cp(28), fill='#c8c1b6')
d.text((920, 920), 'America finds  ·  Mexico arrests', font=hk(40), fill='#bcd1e4')
d.text((920, 972), 'ember + steel = US vs the cartels  ·  steel + olive = the deal', font=cp(30), fill='#c8c1b6')
im.save('references/palette_cartels.png'); print('ok')
