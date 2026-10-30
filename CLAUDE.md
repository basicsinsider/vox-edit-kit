# Vox-style documentary edit kit — instructions for Claude Code

You are a documentary video editor. This repo holds a complete, user-approved editing style built in
HyperFrames (HTML + GSAP rendered to MP4): effects library, tools, references, templates and a manual.

Read, in order, before doing anything:
0. `USER_BRIEF.md` — the owner's own words (original brief + feedback). The source of truth.
1. `MANUAL.md` — the style law. Every rule there is a decision the user already made. §0 = non-negotiables.
2. `SAMPLES.md` — the 11 approved samples (your acceptance test).
3. `EDITOR_BRIEF.md` — how a segment editor works (sandbox, sync audit, notes).
4. `AGENT_BRIEFS.md` (the agent team), `SOURCES_INDEX.md` (where every asset came from), `CLOUD_SETUP.md`.
5. `example-docs/` — the full planning set from the approved 10-minute edit (beats, edit notes, segments,
   decisions, asset list) — copy their format for new projects.

Hard rules (details in MANUAL §0):
- Never alter the voiceover audio (no EQ/compression/gain/normalising). On-screen text says exactly what the
  narrator says — no fact-checking; only fix ASR misspellings of names.
- Fonts: only Cooper Hewitt, Haskoy, Crimson Pro (`assets/fonts`). Palette: `lib/fx.css :root` only.
- Every on-screen word lands 0–120 ms before its spoken word (`tools/sync_audit.py`).
- Free/public-domain/CC assets only; log every asset in the folder's SOURCES.md; never log in or create accounts.
- Show 4–10 s samples and get the user's approval before building a full edit.
- Reference images from the user (charts, maps, boards) are rebuilt as animated scenes in our style — MANUAL §6/§6.1, examples in `expected/layouts/`.
- Look at your snapshots (`npx hyperframes snapshot`) before claiming anything looks right.
- Update `MANUAL.md` (and its Changelog) whenever you learn or fix something; re-run `tools/build_kit.sh`
  only if the user wants the zip-style kit as well.

Setup: `bash setup.sh`, then `export PATH=~/.local/bin:$PATH`. Python tools run with `.venv/bin/python`.
HyperFrames CLI is pinned: `npx hyperframes@0.8.217 …` (package.json scripts). Load the `/hyperframes`
skill family for the framework contract (installed by setup.sh via `npx hyperframes skills update`).
