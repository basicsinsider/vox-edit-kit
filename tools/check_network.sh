#!/usr/bin/env bash
# Checks that this machine can reach every source the style depends on (CLOUD_SETUP.md, SOURCES_INDEX.md).
# Usage: bash tools/check_network.sh
ok=0; bad=0
check() {  # name url
  code=$(curl -s -o /dev/null -m 20 -A "VoxEditKit/1.0" -w "%{http_code}" -L "$2")
  if [[ "$code" =~ ^(200|301|302|403|405)$ && "$code" != "403" ]]; then echo "OK    $1"; ok=$((ok+1));
  else echo "FAIL  $1  (HTTP $code)  $2"; bad=$((bad+1)); fi
}
check "Wikimedia Commons API"   "https://commons.wikimedia.org/w/api.php?action=query&meta=siteinfo&format=json"
check "Wikimedia uploads"       "https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Massachusetts_Institute_of_Technology_campus_aerial_War_Department_1925.jpg/960px-Massachusetts_Institute_of_Technology_campus_aerial_War_Department_1925.jpg"
check "archive.org search"      "https://archive.org/advancedsearch.php?q=prelinger&rows=1&output=json"
check "archive.org downloads"   "https://archive.org/download/copl_000211/__ia_thumb.jpg"
check "Texturelabs"             "https://texturelabs.org/textures/grunge_353/"
check "Library of Congress image server (tile.loc.gov)" "https://tile.loc.gov/storage-services/service/pnp/det/4a20000/4a26000/4a26300/4a26364v.jpg"
check "Library of Congress image CDN (cdn.loc.gov)" "https://cdn.loc.gov/service/pnp/det/4a20000/4a26000/4a26300/4a26364v.jpg"
check "NASA Visible Earth"      "https://visibleearth.nasa.gov/"
check "USGS National Map"       "https://tnmaccess.nationalmap.gov/api/v1/products?prodFormats=GeoTIFF&max=1"
check "AWS terrain tiles"       "https://s3.amazonaws.com/elevation-tiles-prod/terrarium/0/0/0.png"
check "jsDelivr (gsap, us-atlas)" "https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"
check "Instagram"               "https://www.instagram.com/"
check "YouTube"                 "https://www.youtube.com/"
check "npm registry"            "https://registry.npmjs.org/hyperframes"
check "HyperFrames registry"    "https://raw.githubusercontent.com/heygen-com/hyperframes/main/registry/registry.json"
echo "NOTE  www.loc.gov search/JSON API refuses ALL scripted requests (even from a home Mac) - by design, not a network problem."
echo "      Find LOC photos via Wikimedia Commons search, then download full-res from tile.loc.gov (MANUAL 8.1)."
echo; echo "$ok reachable, $bad blocked."
[ $bad -gt 0 ] && echo "Blocked sources: set the cloud environment's Network access to Full (CLOUD_SETUP.md); anything still blocked -> fetch relay (MANUAL §8.2)."
exit 0
