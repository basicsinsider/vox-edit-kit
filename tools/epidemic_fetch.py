"""Download Epidemic Sound tracks (full mix + stems, WAV) through the MCP server into assets/audio/epidemic/<slug>/.
Usage: python3 tools/epidemic_fetch.py <kosmosId> <name> [FULL BASS DRUMS INSTRUMENTS ...]
Files are gitignored (licensed to Krish's subscription; re-download any time). Log each track in assets/audio/epidemic/LOG.md.
Robust against proxy resets: curl with retries + resume (-C -); a file is only accepted when its size matches the WAV
header (RIFF size + 8). Already-complete files are skipped, so re-running the same command finishes a broken download.
Run downloads one at a time (memory/bandwidth)."""
import json, pathlib, struct, subprocess, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import epidemic_mcp as m


def wav_complete(f):
    try:
        with open(f, "rb") as fh:
            h = fh.read(12)
        return h[:4] == b"RIFF" and h[8:12] == b"WAVE" and f.stat().st_size >= struct.unpack("<I", h[4:8])[0] + 8
    except (OSError, struct.error):
        return False


def fetch(kid, name, stems):
    out = pathlib.Path(__file__).resolve().parent.parent / "assets/audio/epidemic" / name
    out.mkdir(parents=True, exist_ok=True)
    started = False
    for st in stems:
        f = out / f"{name}_{st.lower()}.wav"
        if wav_complete(f):
            print(st, "-> already complete:", f.name); continue
        if not started:
            m.session(); started = True
        r = m.rpc("tools/call", {"name": "DownloadRecording", "arguments": {"id": kid, "options": {"fileType": "WAV", "stemType": st}}}, rid=3)
        txt = r["result"]["content"][0]["text"]
        if r["result"].get("isError") or "assetUrl" not in txt:
            print(st, "-> not available:", txt[:160]); continue
        url = json.loads(txt)["data"]["recordingDownload"]["assetUrl"]
        for attempt in range(8):
            subprocess.run(["curl", "-sS", "-L", "--retry", "5", "--retry-all-errors", "-C", "-", "-o", str(f), url])
            if wav_complete(f):
                break
            if f.exists() and f.stat().st_size > 0 and attempt == 3:
                f.unlink()                     # restart from scratch once if resume keeps failing
        print(st, "->", f, f.stat().st_size // 1024 if f.exists() else 0, "KB", "OK" if wav_complete(f) else "INCOMPLETE")


if __name__ == "__main__":
    fetch(sys.argv[1], sys.argv[2], sys.argv[3:] or ["FULL", "BASS", "DRUMS", "INSTRUMENTS"])
