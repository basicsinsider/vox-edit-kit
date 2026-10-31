"""Minimal client for the Epidemic Sound MCP server (MANUAL §10.3) — used when the session can't load .mcp.json.
Key: env EPIDEMIC_SOUND_MCP_API_KEY, else ~/.secrets/epidemic_key (never commit it).
Usage: python3 tools/epidemic_mcp.py list
       python3 tools/epidemic_mcp.py call <ToolName> '<json args>'"""
import json, os, pathlib, sys, urllib.request

URL = "https://www.epidemicsound.com/a/mcp-service/mcp"
KEY = os.environ.get("EPIDEMIC_SOUND_MCP_API_KEY") or pathlib.Path("~/.secrets/epidemic_key").expanduser().read_text().strip()
_sid = None


def rpc(method, params=None, rid=1):
    global _sid
    body = {"jsonrpc": "2.0", "method": method, "params": params or {}}
    if rid is not None:
        body["id"] = rid
    h = {"Authorization": f"Bearer {KEY}", "Content-Type": "application/json", "Accept": "application/json, text/event-stream"}
    if _sid:
        h["mcp-session-id"] = _sid
    req = urllib.request.Request(URL, json.dumps(body).encode(), h)
    with urllib.request.urlopen(req, timeout=180) as r:
        _sid = r.headers.get("mcp-session-id") or _sid
        txt = r.read().decode()
    out = None
    for line in txt.splitlines():
        if line.startswith("data:") and line[5:].strip():
            out = json.loads(line[5:])
    if out is None and txt.strip().startswith("{"):
        out = json.loads(txt)
    return out


def session():
    rpc("initialize", {"protocolVersion": "2025-06-18", "capabilities": {}, "clientInfo": {"name": "vox-edit-kit", "version": "1"}})
    try:
        rpc("notifications/initialized", rid=None)
    except Exception:
        pass


if __name__ == "__main__":
    session()
    if sys.argv[1] == "list":
        for t in rpc("tools/list", rid=2)["result"]["tools"]:
            print(f"- {t['name']}: {t.get('description','')[:300]}\n  args: {json.dumps(t.get('inputSchema',{}).get('properties',{}))[:600]}")
    else:
        r = rpc("tools/call", {"name": sys.argv[2], "arguments": json.loads(sys.argv[3] if len(sys.argv) > 3 else "{}")}, rid=3)
        print(json.dumps(r, indent=1)[:20000])
