# Running this kit in a Claude Code cloud session (claude.ai/code)

Do this once, on the claude.ai account that will run the sessions, **before** the first session.

## 1. Give the session internet access to the archives (most important)
Cloud environments default to **Trusted** network access, which only reaches package registries and GitHub — the
archives this style depends on (Wikimedia Commons, archive.org, Texturelabs, Library of Congress, NASA, USGS,
Instagram for reference reels…) would be blocked.

At claude.ai/code → environment selector (or the caret next to a running session's title → **Edit cloud environment**)
→ open the environment's settings → **Network access**:
- **Full** (recommended) — any domain. Simplest, and needed for new stories that need new sources.
- or **Custom**, tick **Also include default list of common package managers**, and paste the list in
  `cloud/allowed-domains.txt` (one domain per line; `*.` = all subdomains).

## 2. Raise the command time limits (renders take a while)
Same dialog → **Environment variables**, add:
```
BASH_DEFAULT_TIMEOUT_MS=600000
BASH_MAX_TIMEOUT_MS=7200000
```
Without these, any single command is stopped after about 30 minutes (a full 10-minute render on the cloud's
4 vCPUs can take longer). The session should still render long pieces in the background and segment by segment.

## 3. (Optional) Setup script, so every session starts ready
Same dialog → **Setup script** → paste `cloud/setup-script.sh`. It installs ffmpeg/zsh/fonts quickly; the session
still runs `bash setup.sh` itself for the rest (HyperFrames, Parakeet, Agent Reach, .venv, music).

## 4. Resources to expect
Ubuntu 24.04 x86_64, 4 vCPUs, 16 GB RAM, 30 GB disk, Node 22 and Python preinstalled, no ffmpeg until setup.
Sessions pause when idle and can be reopened; background jobs don't survive a reclaimed VM, so the session should
commit and push work often.

## 5. If a site is still blocked
Some sites block cloud/datacenter IPs even with Full access (Instagram often does; Wikimedia may rate-limit).
The session then uses the **fetch relay** (MANUAL §8.2): it lists what it needs in `requests/fetch.json`, pushes its
branch and tells you; on your Mac, in a clone of this repo, run `python3 tools/fetch_relay.py <branch>`; it
downloads everything with the same sources and pushes it back. Then tell the session to pull.
