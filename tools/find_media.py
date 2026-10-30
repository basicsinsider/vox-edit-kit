"""Search free archival sources and print candidates (title, licence, size, URL) — MANUAL §8.1.

Usage:
  python3 tools/find_media.py commons "Herbert Hoover 1928"        # Wikimedia Commons images (licence + size)
  python3 tools/find_media.py archive "Prelinger factory 1930s"   # archive.org films (mediatype movies)
  python3 tools/find_media.py archive-texts "New York Times 1928"  # archive.org scans (newspapers, books, yearbooks)
  python3 tools/find_media.py files <archive_identifier>          # list an archive.org item's downloadable files
Options: --limit N (default 12)
Download Commons images with tools/commons_thumb.sh (full-size originals are rate-limited).
Download archive.org files from https://archive.org/download/<identifier>/<file>.
"""
import json, sys, time, urllib.parse, urllib.request

UA = {"User-Agent": "VoxEditKit/1.0 (documentary research; personal use)"}
args = [a for a in sys.argv[1:] if not a.startswith("--")]
limit = int(sys.argv[sys.argv.index("--limit") + 1]) if "--limit" in sys.argv else 12
if "--limit" in sys.argv:
    args = [a for a in args if a != str(limit)]
if len(args) < 2:
    sys.exit(__doc__)
mode, query = args[0], " ".join(args[1:])


def get(url, tries=4):
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=40) as r:
                return json.loads(r.read())
        except Exception as e:  # 429 / transient: back off politely
            if i == tries - 1:
                sys.exit(f"request failed: {e}")
            time.sleep(6 * (i + 1))


if mode == "commons":
    q = urllib.parse.urlencode({"action": "query", "generator": "search", "gsrnamespace": 6, "gsrsearch": query,
                                "gsrlimit": limit, "prop": "imageinfo", "iiprop": "size|extmetadata|url", "format": "json"})
    d = get("https://commons.wikimedia.org/w/api.php?" + q)
    for p in d.get("query", {}).get("pages", {}).values():
        i = p["imageinfo"][0]; m = i["extmetadata"]
        print(f'{p["title"][5:]}\n   {i["width"]}x{i["height"]} | {m.get("LicenseShortName", {}).get("value", "?")} | '
              f'{(m.get("DateTimeOriginal", {}).get("value") or "")[:25]} | {i["descriptionurl"]}')
elif mode in ("archive", "archive-texts"):
    mt = "movies" if mode == "archive" else "texts"
    q = urllib.parse.urlencode({"q": f"({query}) AND mediatype:{mt}", "fl[]": ["identifier", "title", "year", "licenseurl", "rights"],
                                "rows": limit, "output": "json"}, doseq=True)
    for doc in get("https://archive.org/advancedsearch.php?" + q)["response"]["docs"]:
        lic = doc.get("licenseurl") or (doc.get("rights") or "check item page")
        print(f'{doc.get("title")} ({doc.get("year", "?")})\n   {lic} | https://archive.org/details/{doc["identifier"]}')
elif mode == "files":
    d = get(f"https://archive.org/metadata/{query}")
    m = d.get("metadata", {})
    print(m.get("title"), "|", m.get("licenseurl") or m.get("rights") or "see collection rights")
    for f in d.get("files", []):
        if "thumbs/" not in f["name"] and not f["name"].startswith("__ia") and f["name"].lower().endswith((".mp4", ".mpeg", ".mov", ".avi", ".ogv", ".jpg", ".jp2", ".pdf", ".tif")):
            print(f'   {f["name"]}  {int(f.get("size", 0)) // 1_000_000} MB  {f.get("format", "")}')
else:
    sys.exit(__doc__)
