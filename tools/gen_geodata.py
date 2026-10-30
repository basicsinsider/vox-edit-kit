"""Write <map>.json (bounds, projection math, SVG paths of states, places) + optional state alpha mask PNG
for an equirectangular map: x = (lon - lon0) * ppd, y = (lat1 - lat) * ppd.
Usage: gen_geodata.py name lon0 lat0 lon1 lat1 ppd out.json [--mask ABBR out_mask.png] [--image file] [--note text]"""
import sys, json
from PIL import Image, ImageDraw
a=sys.argv; name=a[1]; lon0,lat0,lon1,lat1,ppd=map(float,a[2:7]); out=a[7]
ROOT=__file__.rsplit('/tools/',1)[0]
W=int(round((lon1-lon0)*ppd)); H=int(round((lat1-lat0)*ppd))
P=lambda lon,lat:((lon-lon0)*ppd,(lat1-lat)*ppd)
PLACES={"palo_alto":(-122.143,37.4419),"stanford_main_quad":(-122.1697,37.4275),"hp_garage_367_addison":(-122.1550,37.4430),
 "san_francisco":(-122.4194,37.7749),"los_angeles":(-118.2437,34.0522),"sacramento":(-121.4944,38.5816),"san_jose":(-121.8863,37.3382),
 "indianapolis":(-86.1581,39.7684),"eli_lilly_hq_indianapolis":(-86.145,39.758),"bloomington_in":(-86.5264,39.1653),"chicago":(-87.6298,41.8781),
 "boston":(-71.0589,42.3601),"mit_great_dome":(-71.0921,42.3596),"harvard_yard":(-71.1167,42.3744),"new_york_city":(-74.006,40.7128),
 "schenectady_ge":(-73.9396,42.8142),"st_louis":(-90.1994,38.627),"omaha":(-95.9345,41.2565),"salt_lake_city":(-111.891,40.7608),
 "denver":(-104.9903,39.7392),"reno":(-119.8138,39.5296),"cleveland":(-81.6944,41.4993)}
gj=json.load(open(ROOT+'/assets/maps/us_states.geojson'))
def rings(g): return g['coordinates'] if g['type']=='MultiPolygon' else [g['coordinates']]
def pathd(g):
    s=[]
    for poly in rings(g):
        for r in poly:
            pts=[P(x,y) for x,y in r]
            s.append('M'+' L'.join(f'{x:.1f},{y:.1f}' for x,y in pts)+'Z')
    return ''.join(s)
states={}
for f in gj['features']:
    pr=f['properties']; g=f['geometry']
    xs=[c[0] for p in rings(g) for r in p for c in r]; ys=[c[1] for p in rings(g) for r in p for c in r]
    if max(xs)<lon0 or min(xs)>lon1 or max(ys)<lat0 or min(ys)>lat1: continue
    x0,y1_=P(min(xs),min(ys)); x1,y0=P(max(xs),max(ys))
    states[pr.get('abbr') or pr['name']]={"name":pr['name'],"d":pathd(g),"bbox":[round(x0,1),round(y0,1),round(x1,1),round(y1_,1)]}
pl={k:{"lon":v[0],"lat":v[1],"x":round(P(*v)[0],1),"y":round(P(*v)[1],1)} for k,v in PLACES.items() if lon0<=v[0]<=lon1 and lat0<=v[1]<=lat1}
doc={"name":name,"width":W,"height":H,"bounds":{"lon_min":lon0,"lon_max":lon1,"lat_min":lat0,"lat_max":lat1},"px_per_degree":ppd,
 "projection":"equirectangular (plate carree), WGS84 lon/lat linear",
 "formula":f"x = (lon - ({lon0})) * {ppd:g} ; y = ({lat1} - lat) * {ppd:g}",
 "svg_hint":f'<svg viewBox="0 0 {W} {H}"> paths below; scale with the image using the same transform',
 "states":states,"places":pl}
if '--image' in a: doc["image"]=a[a.index('--image')+1]
if '--note' in a: doc["note"]=a[a.index('--note')+1]
if '--mask' in a:
    i=a.index('--mask'); ab=a[i+1]; mo=a[i+2]
    m=Image.new('L',(W,H),0); d=ImageDraw.Draw(m)
    for f in gj['features']:
        if f['properties'].get('abbr')==ab:
            for poly in rings(f['geometry']):
                d.polygon([P(x,y) for x,y in poly[0]],fill=255)
                for h in poly[1:]: d.polygon([P(x,y) for x,y in h],fill=0)
    m.save(mo); doc["mask"]=mo.split('/taiwan-edit/')[-1] if '/taiwan-edit/' in mo else mo
json.dump(doc,open(out,'w'),separators=(',',':'))
print(out,W,H,len(states),'states',len(pl),'places')
