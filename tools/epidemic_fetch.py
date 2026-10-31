"""Download Epidemic Sound tracks (full mix + stems, WAV) through the MCP server into assets/audio/epidemic/<slug>/.
Usage: python3 tools/epidemic_fetch.py <kosmosId> <name> [FULL BASS DRUMS INSTRUMENTS ...]
Files are gitignored (licensed to Krish's subscription; re-download any time). Log each track in assets/audio/epidemic/LOG.md."""
import json, pathlib, subprocess, sys, urllib.request
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import epidemic_mcp as m

kid, name, stems = sys.argv[1], sys.argv[2], sys.argv[3:] or ["FULL", "BASS", "DRUMS", "INSTRUMENTS"]
out = pathlib.Path(__file__).resolve().parent.parent / "assets/audio/epidemic" / name
out.mkdir(parents=True, exist_ok=True)
m.session()
for st in stems:
    r = m.rpc("tools/call", {"name": "DownloadRecording", "arguments": {"id": kid, "options": {"fileType": "WAV", "stemType": st}}}, rid=3)
    txt = r["result"]["content"][0]["text"]
    if r["result"].get("isError") or "assetUrl" not in txt:
        print(st, "-> not available:", txt[:160]); continue
    url = json.loads(txt)["data"]["recordingDownload"]["assetUrl"]
    f = out / f"{name}_{st.lower()}.wav"
    urllib.request.urlretrieve(url, f)
    print(st, "->", f, f.stat().st_size // 1024, "KB")
