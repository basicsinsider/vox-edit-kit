"""Fetch AWS Terrain Tiles (terrarium PNG) covering a lon/lat bbox at zoom z.
Usage: fetch_terrain.py z lon0 lat0 lon1 lat1 cache_dir
Data: https://registry.opendata.aws/terrain-tiles/ (SRTM, GMTED2010, ETOPO1, USGS NED — public domain sources)."""
import sys, math, os, subprocess
from concurrent.futures import ThreadPoolExecutor
z=int(sys.argv[1]); lon0,lat0,lon1,lat1=map(float,sys.argv[2:6]); cache=sys.argv[6]
def tx(lon): return int((lon+180)/360*2**z)
def ty(lat):
    r=math.radians(lat); return int((1-math.log(math.tan(r)+1/math.cos(r))/math.pi)/2*2**z)
jobs=[]
for x in range(tx(lon0),tx(lon1)+1):
    for y in range(ty(lat1),ty(lat0)+1):
        p=f"{cache}/{z}_{x}_{y}.png"
        if not os.path.exists(p): jobs.append((x,y,p))
def get(j):
    x,y,p=j
    for _ in range(3):
        r=subprocess.run(["curl","-sf","-o",p,f"https://s3.amazonaws.com/elevation-tiles-prod/terrarium/{z}/{x}/{y}.png"])
        if r.returncode==0: return
print(len(jobs),"tiles to fetch")
with ThreadPoolExecutor(16) as ex: list(ex.map(get,jobs))
print("done")
