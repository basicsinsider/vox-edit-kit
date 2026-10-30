"""Cut a photo into 2.5D layers (s10-style): sky (keyed + extended), mid (sky removed, near-layer regions
inpainted with a diffusion/blur fill), near layers (feathered polygons) and a blurred backdrop.
Usage: cut_layers.py spec.json   (spec: src, crop [x0,y0,x1,y1], out_w, outdir, sky:{scan_from,thresh} | null,
       near:{name:[[x,y],...] in crop px}, feather)"""
import sys, json, numpy as np
from PIL import Image, ImageDraw, ImageFilter
sp=json.load(open(sys.argv[1])); Image.MAX_IMAGE_PIXELS=None
im=Image.open(sp['src']).convert('RGB').crop(tuple(sp['crop']))
s=sp['out_w']/im.width; im=im.resize((sp['out_w'],round(im.height*s)),Image.LANCZOS)
W,H=im.size; a=np.asarray(im,np.float32); out=sp['outdir']; fe=sp.get('feather',12)
def poly_mask(pts,feather):
    m=Image.new('L',(W,H),0); ImageDraw.Draw(m).polygon([(x*s,y*s) for x,y in pts],fill=255)
    return m.filter(ImageFilter.GaussianBlur(feather))
def fill(img,mask,iters=40):  # diffusion fill inside mask (mask 255 = fill)
    sm=img.resize((W//8,H//8),Image.BILINEAR); mk=mask.resize((W//8,H//8),Image.BILINEAR).point(lambda v:255 if v>20 else 0)
    base=sm.copy()
    for i in range(iters):
        bl=base.filter(ImageFilter.GaussianBlur(4)); base=Image.composite(bl,sm,mk)
    up=base.resize((W,H),Image.BILINEAR).filter(ImageFilter.GaussianBlur(6))
    return Image.composite(up,img,mask)
lum=a.mean(axis=2)
skyline=np.full(W,H,int)
alpha=np.full((H,W),255,np.uint8)
if sp.get('sky'):
    sk=sp['sky']; y0=int(sk['scan_from']*s)
    L=np.asarray(Image.fromarray(lum.astype(np.uint8)).filter(ImageFilter.GaussianBlur(2)),np.float32)
    for x in range(W):
        ref=L[max(y0-40,0):y0,x].mean(); col=L[y0:,x]
        hit=np.where(col<ref*sk['thresh'])[0]; skyline[x]=y0+(hit[0] if len(hit) else H-y0)
    # median-ish smoothing of skyline to kill noise spikes
    k=5; sl=np.array([np.median(skyline[max(0,x-k):x+k+1]) for x in range(W)]).astype(int); skyline=sl
    yy=np.arange(H)[:,None]; alpha=((yy>=skyline[None,:])*255).astype(np.uint8)
    am=Image.fromarray(alpha).filter(ImageFilter.GaussianBlur(1.5))
    # sky plate: fill below skyline with sky colour, blur
    skya=a.copy()
    for x in range(W):
        y=max(skyline[x]-6,1); skya[y:,x]=a[max(y-30,0):y,x].mean(axis=0)
    sky=Image.fromarray(skya.astype(np.uint8)).filter(ImageFilter.GaussianBlur(18))
    sky.save(f'{out}/sky.jpg',quality=90)
else:
    am=Image.fromarray(alpha)
near_union=Image.new('L',(W,H),0)
for name,pts in sp.get('near',{}).items():
    m=poly_mask(pts,fe); near_union=Image.fromarray(np.maximum(np.asarray(near_union),np.asarray(m)))
    rgba=im.copy(); rgba.putalpha(m); bb=m.point(lambda v:255 if v>8 else 0).getbbox()
    rgba.crop(bb).save(f'{out}/{name}.png'); sp.setdefault('placed',{})[name]={"x":bb[0],"y":bb[1],"w":bb[2]-bb[0],"h":bb[3]-bb[1]}
# mid: inpaint where near layers were, apply sky alpha
grow=near_union.filter(ImageFilter.MaxFilter(9)).point(lambda v:255 if v>10 else 0)
mid=fill(im,grow)
if sp.get('mid_poly'):
    mm=poly_mask(sp['mid_poly'],fe); am=Image.fromarray(np.minimum(np.asarray(am),np.asarray(mm)))
    grow=Image.fromarray(np.maximum(np.asarray(grow),np.asarray(mm.filter(ImageFilter.MaxFilter(15)).point(lambda v:255 if v>10 else 0))))
mid.putalpha(am); mid.save(f'{out}/{sp.get("mid_name","mid")}.png')
bd=fill(im,grow).filter(ImageFilter.GaussianBlur(10)); bd.save(f'{out}/backdrop.jpg',quality=88)
lay={"source":sp['src'],"crop_in_source":sp['crop'],"frame":[W,H],"scale_from_crop":s,
     "layers":{"sky.jpg" if sp.get('sky') else None:"far, full frame",f"{sp.get('mid_name','mid')}.png":"full frame, sky alpha 0, near-layer areas inpainted","backdrop.jpg":"full frame, blurred, near areas inpainted"},
     "near_layers_placed_px":sp.get('placed',{}),"notes":sp.get('notes','')}
lay['layers']={k:v for k,v in lay['layers'].items() if k}
json.dump(lay,open(f'{out}/layout.json','w'),indent=1); print(json.dumps(lay['near_layers_placed_px']))
