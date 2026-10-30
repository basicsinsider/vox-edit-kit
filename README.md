# vox-edit-kit

A reusable Vox-style documentary editing system for Claude Code + [HyperFrames](https://hyperframes.heygen.com).
Give it a raw voiceover; it plans, sources, builds, sound-designs and renders a documentary edit in a fixed,
approved style (archival photos with film treatment, animated maps, paper-style charts, newspapers with
highlighters, vintage TVs, 2.5D parallax, Vox markups, marimba sound bed).

- `CLAUDE.md` — start here (agent instructions) · `MANUAL.md` — the full style manual · `SAMPLES.md` — acceptance test
- `setup.sh` — installs everything (Linux or macOS)
- `lib/` effects library (fx.js / fx.css) · `tools/` build, render, audit, image and sound tools
- `compositions/` the 11 approved samples · `templates/full-edit/` the six segments of the approved 10-minute edit
- `USER_BRIEF.md` the owner's brief + feedback verbatim · `AGENT_BRIEFS.md` the agent team · `SOURCES_INDEX.md` + `example-docs/sources/` every source used · `CLOUD_SETUP.md` cloud environment settings · `tools/fetch_relay.py` fetch blocked media from a Mac
- `references/` the user's style images + studied tutorial reels · `expected/` approved sample previews + `layouts/` stills of every reference layout
- `assets/` fonts, textures (Texturelabs), maps, archival media used by the samples, icons, logos, SFX
- `vo10.mp3` + `transcript.json` — the test voiceover (first 10 minutes of the "Taiwan" episode)

Quick check after setup:
```bash
export PATH=~/.local/bin:$PATH
python3 tools/build_index.py && npx hyperframes@0.8.217 lint
tools/render_samples.sh s01 s03        # -> renders/samples/*.mp4, compare with expected/
```

Licences: fonts are the owner's copies (Cooper Hewitt and Crimson Pro are OFL; Haskoy per its foundry).
Texturelabs textures are free to use in videos but may not be redistributed publicly — **keep this repo private.**
Archival media: see each `assets/**/SOURCES.md` (public domain unless noted; CC BY items need on-screen credit).
