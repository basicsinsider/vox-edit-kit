#!/bin/zsh
# Download a Wikimedia Commons file at a standard thumbnail width (full-size originals are rate-limited).
# Usage: tools/commons_thumb.sh "File name.jpg" out.jpg [width]
n="$1"; o="$2"; w="${3:-1920}"
UA="TaiwanEdit/1.0 (personal documentary edit)"
tp=$(python3 -c "import hashlib,sys,urllib.parse;n=sys.argv[1].replace(' ','_');m=hashlib.md5(n.encode()).hexdigest();print(urllib.parse.quote(m[0]+'/'+m[:2]+'/'+n)+'/'+sys.argv[2]+'px-'+urllib.parse.quote(n))" "$n" "$w")
for attempt in 1 2 3 4; do
  curl -s -L -A "$UA" -o "$o" "https://upload.wikimedia.org/wikipedia/commons/thumb/$tp"
  if file -b "$o" | grep -qE "JPEG|PNG"; then echo "$o: $(file -b $o | cut -c1-70)"; exit 0; fi
  sleep $((attempt * 6))
done
echo "$o: FAILED"; exit 1
