"""Fetch relay: downloads, on a normal computer, the media a cloud session couldn't reach (MANUAL §8.2).

Cloud side (the session): add entries to requests/fetch.json, commit and push its branch, tell the user the branch.
  [{"kind": "commons",     "src": "File name on Commons.jpg",            "out": "assets/archival/x/name.jpg", "width": 1920},
   {"kind": "url",         "src": "https://archive.org/download/id/f.mp4", "out": "assets/archival/footage/_raw/f.mp4"},
   {"kind": "instagram",   "src": "https://www.instagram.com/reel/ID/",    "out": "references/reels/raw/name.mp4"},
   {"kind": "youtube",     "src": "https://www.youtube.com/watch?v=ID",    "out": "assets/archival/footage/_raw/name.mp4"},
   {"kind": "texturelabs", "src": "https://texturelabs.org/textures/grunge_353/", "out": "assets/textures/_raw/grunge_353.jpg"}]
  Optional per entry: "note" (why it's needed). Files over 95 MB are split into out.part-aa… (rejoin with cat).

User side (on their Mac, in a clone of the repo):
  python3 tools/fetch_relay.py <branch>     # checks out the branch, downloads everything, commits, pushes
Texturelabs entries open the page in the browser: click the site's Download button; the script waits for the
file to appear in ~/Downloads and moves it into place.
"""
import json, os, pathlib, shutil, subprocess, sys, time, urllib.parse, urllib.request, hashlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
REQ = ROOT / "requests/fetch.json"
UA = "VoxEditKit/1.0 (documentary research; personal use)"
YTDLP = shutil.which("yt-dlp") or os.path.expanduser("~/.local/share/uv/tools/agent-reach/bin/yt-dlp")
LIMIT = 95 * 1024 * 1024


def sh(*a, **k):
    print("$", " ".join(map(str, a)))
    return subprocess.run(a, check=True, cwd=ROOT, **k)


def curl(url, out):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    for i in range(4):
        try:
            with urllib.request.urlopen(req, timeout=120) as r, open(out, "wb") as f:
                shutil.copyfileobj(r, f)
            return
        except Exception as e:
            if i == 3:
                raise
            print("  retry:", e); time.sleep(6 * (i + 1))


def commons(name, out, width):
    n = name.removeprefix("File:").replace(" ", "_")
    m = hashlib.md5(n.encode()).hexdigest()
    q = urllib.parse.quote
    curl(f"https://upload.wikimedia.org/wikipedia/commons/thumb/{m[0]}/{m[:2]}/{q(n)}/{width}px-{q(n)}", out)


def texturelabs(page, out):
    dl = pathlib.Path.home() / "Downloads"
    before = set(dl.iterdir())
    subprocess.run(["open", page])
    print(f"  -> click the Download button on {page} (waiting for a new file in ~/Downloads)…")
    while True:
        time.sleep(2)
        new = [p for p in set(dl.iterdir()) - before if not p.name.endswith((".crdownload", ".download", ".part"))]
        if new:
            shutil.move(str(new[0]), out); return


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    branch = sys.argv[1]
    sh("git", "fetch", "origin", branch)
    sh("git", "checkout", branch)
    sh("git", "pull", "--ff-only", "origin", branch)
    items = json.loads(REQ.read_text())
    done = 0
    for it in items:
        if it.get("done"):
            continue
        out = ROOT / it["out"]
        out.parent.mkdir(parents=True, exist_ok=True)
        print(f"[{it['kind']}] {it['src']} -> {it['out']}")
        try:
            k = it["kind"]
            if k == "commons":
                commons(it["src"], out, it.get("width", 1920))
            elif k == "url":
                curl(it["src"], out)
            elif k in ("instagram", "youtube"):
                subprocess.run([YTDLP, "-q", "--no-warnings", "-f", "mp4/best", "-o", str(out), it["src"]], check=True)
            elif k == "texturelabs":
                texturelabs(it["src"], out)
            else:
                raise ValueError("unknown kind " + k)
            if out.stat().st_size > LIMIT:  # GitHub's per-file limit is 100 MB
                subprocess.run(["split", "-b", "90m", str(out), str(out) + ".part-"], check=True)
                out.unlink()
                it["split"] = True
            it["done"] = True
            done += 1
        except Exception as e:
            it["error"] = str(e)
            print("  FAILED:", e)
    REQ.write_text(json.dumps(items, indent=1))
    sh("git", "add", "-A")
    sh("git", "commit", "-m", f"fetch relay: {done} file(s) downloaded locally")
    sh("git", "push", "origin", branch)
    print(f"\n{done} fetched. Tell the cloud session: 'pulled — git pull origin {branch}'.")


main()
