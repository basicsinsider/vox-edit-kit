"""Grey shaded-relief basemap (ref R12 look) in an equirectangular pixel space.
Usage: gen_relief.py z lon0 lat0 lon1 lat1 px_per_deg tile_cache out.jpg [--exag E] [--land-mask out_mask.png]
x = (lon - lon0) * ppd ; y = (lat1 - lat) * ppd   (lat1 = north edge)
Elevation: AWS Terrain Tiles (terrarium). Water (elev <= 0 and flat) -> navy-grey."""
import sys, math, numpy as np
from PIL import Image, ImageFilter
a=sys.argv; z=int(a[1]); lon0,lat0,lon1,lat1,ppd=map(float,a[2:7]); cache=a[7]; out=a[8]
exag=float(a[a.index('--exag')+1]) if '--exag' in a else 1.0
W=int(round((lon1-lon0)*ppd)); H=int(round((lat1-lat0)*ppd))
N=2**z*256
def mx(lon): return (lon+180)/360*N
def my(lat):
    r=np.radians(lat); return (1-np.log(np.tan(r)+1/np.cos(r))/np.pi)/2*N
lons=lon0+(np.arange(W)+0.5)/ppd; lats=lat1-(np.arange(H)+0.5)/ppd
X=mx(lons); Y=my(lats)
tx0,tx1=int(X.min()//256),int(X.max()//256); ty0,ty1=int(Y.min()//256),int(Y.max()//256)
mos=np.zeros(((ty1-ty0+1)*256,(tx1-tx0+1)*256),np.float32)
for tx in range(tx0,tx1+1):
    for ty in range(ty0,ty1+1):
        try: t=np.asarray(Image.open(f"{cache}/{z}_{tx}_{ty}.png").convert('RGB'),np.float32)
        except Exception: continue
        mos[(ty-ty0)*256:(ty-ty0+1)*256,(tx-tx0)*256:(tx-tx0+1)*256]=t[...,0]*256+t[...,1]+t[...,2]/256-32768
# bilinear sample
xi=X-tx0*256-0.5; yi=Y-ty0*256-0.5
x0=np.clip(np.floor(xi).astype(int),0,mos.shape[1]-2); y0=np.clip(np.floor(yi).astype(int),0,mos.shape[0]-2)
fx=(xi-x0)[None,:]; fy=(yi-y0)[:,None]
Y0=y0[:,None]; X0=x0[None,:]
E=(mos[Y0,X0]*(1-fx)*(1-fy)+mos[Y0,X0+1]*fx*(1-fy)+mos[Y0+1,X0]*(1-fx)*fy+mos[Y0+1,X0+1]*fx*fy)
# hillshade (metres per pixel)
latc=np.radians(lats)[:,None]
dx=111320*np.cos(latc)/ppd; dy=111320/ppd
gy,gx=np.gradient(E*exag)
gx=gx/dx; gy=gy/dy
az=math.radians(315); alt=math.radians(42)
slope=np.arctan(np.hypot(gx,gy)); aspect=np.arctan2(-gx,gy)
hs=np.sin(alt)*np.cos(slope)+np.cos(alt)*np.sin(slope)*np.cos(az-aspect+math.pi)
hs=np.clip(hs,0,1)
# combine: light grey land, slight hypsometric darkening with altitude
land=E>0.5
if '--lakes' in a:
    import json
    from PIL import ImageDraw
    lm=Image.new('L',(W,H),0); d=ImageDraw.Draw(lm)
    gj=json.load(open(a[a.index('--lakes')+1]))
    def ring(r): return [((x-lon0)*ppd,(lat1-y)*ppd) for x,y in r]
    for f in gj['features']:
        g_=f['geometry']; polys=g_['coordinates'] if g_['type']=='MultiPolygon' else [g_['coordinates']]
        for P in polys:
            bx=[c[0] for c in P[0]]; by=[c[1] for c in P[0]]
            if max(bx)<lon0 or min(bx)>lon1 or max(by)<lat0 or min(by)>lat1: continue
            d.polygon(ring(P[0]),fill=255)
            for hole in P[1:]: d.polygon(ring(hole),fill=0)
    land=land&(np.asarray(lm)<128)
flat=np.sin(alt)
g=0.84+1.0*(hs-flat)
# second, softer light from the north for form
hs2=np.clip(np.cos(slope)*0.7+np.sin(slope)*np.cos(math.radians(0)-aspect+math.pi)*0.3,0,1)
g=g+0.25*(hs2-0.7)
g=g-0.05*np.clip(E/3000,0,1)
g=np.clip(g,0.25,1.0)
paper=np.array([0xe4,0xe2,0xdc],np.float32)/255  # cool light grey land
water=np.array([0x2e,0x3e,0x4a],np.float32)/255   # dark navy-grey (R12 water)
wm=Image.fromarray((land*255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.2))
wm=np.asarray(wm,np.float32)[...,None]/255
rgb=(paper[None,None,:]*g[...,None])*wm+water[None,None,:]*(1-wm)
# subtle bathymetry shading in water
rgb=np.clip(rgb,0,1)
Image.fromarray((rgb*255).astype(np.uint8)).save(out,quality=90)
if '--land-mask' in a:
    Image.fromarray((land*255).astype(np.uint8)).save(a[a.index('--land-mask')+1])
print(out,W,H)
