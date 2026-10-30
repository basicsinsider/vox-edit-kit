"""Beige muted US map (ref R11) in the us_basemap pixel space (6400x3200, x=(lon+128)*100, y=(52-lat)*100).
Writes assets/maps/us_beige.svg (vector, states as <path id="st-XX">) and us_beige_3840.png (paper texture inside states).
Usage: gen_us_beige.py NE_DIR   (Natural Earth ne_50m_admin_0_countries + ne_50m_lakes geojson)"""
import sys, json, numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageChops
NE=sys.argv[1]; ROOT=__file__.rsplit('/tools/',1)[0]
W,H=6400,3200; P=lambda lon,lat:((lon+128)*100,(52-lat)*100)
WATER='#98adba'; LAND2='#c3cdd2'; LAND2_LINE='#93a4af'; BEIGE='#e6d6b2'; INK='#18222f'
def rings(g): return g['coordinates'] if g['type']=='MultiPolygon' else [g['coordinates']]
def inb(poly): xs=[c[0] for c in poly[0]]; ys=[c[1] for c in poly[0]]; return not(max(xs)<-130 or min(xs)>-62 or max(ys)<18 or min(ys)>54)
def d_of(g):
    out=[]
    for poly in rings(g):
        if not inb(poly): continue
        for r in poly: out.append('M'+' L'.join('%.1f,%.1f'%P(x,y) for x,y in r)+'Z')
    return ''.join(out)
countries=json.load(open(NE+'/ne_50m_admin_0_countries.geojson'))
lakes=json.load(open(NE+'/ne_50m_lakes.geojson'))
states=json.load(open(ROOT+'/assets/maps/us_states.geojson'))
others=[f for f in countries['features'] if f['properties'].get('ADM0_A3')!='USA']
usa=[f for f in countries['features'] if f['properties'].get('ADM0_A3')=='USA']
conus=[f for f in states['features'] if f['properties'].get('conus')]
bigl=[f for f in lakes['features'] if f['properties'].get('scalerank',9)<=1]
svg=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">',
 '<!-- R11 beige US map. Pixel space = assets/maps/us_overlay.json (x=(lon+128)*100, y=(52-lat)*100). Boundaries: us-atlas (US Census, PD) + Natural Earth (PD). -->',
 f'<rect id="water" width="{W}" height="{H}" fill="{WATER}"/>','<g id="neighbours" fill="%s" stroke="%s" stroke-width="3">'%(LAND2,LAND2_LINE)]
for f in others+usa:
    d=d_of(f['geometry'])
    if d: svg.append(f'<path id="c-{f["properties"]["ADM0_A3"]}" d="{d}"/>')
svg.append('</g>')
svg.append(f'<g id="states" fill="{BEIGE}" stroke="{INK}" stroke-opacity="0.55" stroke-width="3" stroke-linejoin="round">')
for f in conus:
    svg.append(f'<path id="st-{f["properties"]["abbr"]}" data-name="{f["properties"]["name"]}" d="{d_of(f["geometry"])}"/>')
svg.append('</g>')
svg.append(f'<g id="lakes" fill="{WATER}" stroke="{LAND2_LINE}" stroke-width="2">')
for f in bigl:
    d=d_of(f['geometry'])
    if d: svg.append(f'<path d="{d}"/>')
svg.append('</g></svg>')
open(ROOT+'/assets/maps/us_beige.svg','w').write('\n'.join(svg))
# raster preview / plate at 3840x1920 (scale 0.6)
S=0.6; w,h=int(W*S),int(H*S)
def draw(feats,img,fill,outline=None,width=1,only_inb=True):
    d=ImageDraw.Draw(img)
    for f in feats:
        for poly in rings(f['geometry']):
            if only_inb and not inb(poly): continue
            pts=[(P(x,y)[0]*S,P(x,y)[1]*S) for x,y in poly[0]]
            d.polygon(pts,fill=fill)
            for hole in poly[1:]: d.polygon([(P(x,y)[0]*S,P(x,y)[1]*S) for x,y in hole],fill=0 if img.mode=='L' else WATER)
            if outline: d.line(pts+[pts[0]],fill=outline,width=width,joint='curve')
base=Image.new('RGB',(w,h),WATER)
draw(others+usa,base,LAND2,LAND2_LINE,2)
mask=Image.new('L',(w,h),0); draw(conus,mask,255)
lm=Image.new('L',(w,h),0); draw(bigl,lm,255)
mask=ImageChops.subtract(mask,lm)
paper=Image.open(ROOT+'/assets/textures/paper_cream_01_hires.jpg').convert('RGB').resize((w,h))
pa=np.asarray(paper,np.float32)/255; pa=pa/pa.mean(axis=(0,1))  # normalise to keep the beige hue
beige=np.array([0xe6,0xd6,0xb2],np.float32)/255
land=np.clip(beige[None,None,:]*(0.55+0.45*pa),0,1)
# watercolour edge: darken slightly near the coast/edges
edge=np.asarray(mask.filter(ImageFilter.GaussianBlur(14)),np.float32)/255
land=land*(0.88+0.12*edge[...,None])
landimg=Image.fromarray((land*255).astype(np.uint8))
base.paste(landimg,(0,0),mask)
ImageDraw.Draw(base)
d=ImageDraw.Draw(base)
for f in conus:
    for poly in rings(f['geometry']):
        pts=[(P(x,y)[0]*S,P(x,y)[1]*S) for x,y in poly[0]]
        d.line(pts+[pts[0]],fill=(0x18,0x22,0x2f),width=2,joint='curve')
lake_draw=Image.new('RGB',(w,h),WATER); base.paste(lake_draw,(0,0),lm)
base.save(ROOT+'/assets/maps/us_beige_3840.png')
print('ok',w,h)
