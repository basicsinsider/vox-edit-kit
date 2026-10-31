"""Download Epidemic Sound sound effects (WAV) through the MCP server into assets/audio/epidemic/sfx/<name>.wav.
Usage: python3 tools/epidemic_sfx_fetch.py <soundEffectId> <name> [<id> <name> ...]
Find ids with: python3 tools/epidemic_mcp.py call SearchSoundEffects '{"query":{"term":"camera focus"},"first":6}'
Gitignored (licensed to Krish's subscription). Log each file in assets/audio/epidemic/LOG.md (SFX table)."""
import json, pathlib, subprocess, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import epidemic_mcp as m
from epidemic_fetch import wav_complete

out = pathlib.Path(__file__).resolve().parent.parent / "assets/audio/epidemic/sfx"
out.mkdir(parents=True, exist_ok=True)
args = sys.argv[1:]
m.session()
for sid, name in zip(args[::2], args[1::2]):
    f = out / f"{name}.wav"
    if wav_complete(f):
        print(name, "-> already complete"); continue
    r = m.rpc("tools/call", {"name": "DownloadSoundEffect", "arguments": {"id": sid, "options": {"fileType": "WAV"}}}, rid=3)
    txt = r["result"]["content"][0]["text"]
    if r["result"].get("isError") or "assetUrl" not in txt:
        print(name, "-> not available:", txt[:160]); continue
    url = json.loads(txt)["data"]["soundEffectDownload"]["assetUrl"]
    for _ in range(6):
        subprocess.run(["curl", "-sS", "-L", "--retry", "5", "--retry-all-errors", "-C", "-", "-o", str(f), url])
        if wav_complete(f):
            break
    print(name, "->", f.name, f.stat().st_size // 1024 if f.exists() else 0, "KB", "OK" if wav_complete(f) else "INCOMPLETE")
