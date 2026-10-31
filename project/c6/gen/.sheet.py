import sys,glob
from PIL import Image,ImageDraw
fs=sorted(glob.glob(sys.argv[1]+"/frame-*.png"))
W,H=600,338;sh=Image.new("RGB",(W*3,(H+20)*((len(fs)+2)//3)),(30,30,30));d=ImageDraw.Draw(sh)
for i,f in enumerate(fs):
    x,y=(i%3)*W,(i//3)*(H+20);sh.paste(Image.open(f).convert("RGB").resize((W,H)),(x,y+20));d.text((x+4,y+4),f.split("-at-")[1],fill="white")
sh.save(sys.argv[1]+"/sheet.jpg",quality=85)
