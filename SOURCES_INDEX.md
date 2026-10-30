# Where everything in the approved edit came from

Use the **same sources first**, then add new ones a story needs (MANUAL §8.1). Exact URLs, licences and authors for
every file of the approved 10-minute edit are in `example-docs/sources/*.md` (177 source URLs); the sample assets
carry their own `SOURCES.md` in `assets/**`.

| asset type | sources actually used | notes |
|---|---|---|
| archival photos | **Wikimedia Commons** (the main source — 113 links: Library of Congress / Detroit Publishing, Harris & Ewing, NARA, Smithsonian, Boston Public Library postcards, Bain), Library of Congress (lccn.loc.gov / cdn.loc.gov), White House Historical Association | thumbnails via `tools/commons_thumb.sh` (960/1280/1920/3840) |
| yearbooks, books, documents | **archive.org** texts: Stanford Quad yearbook 1921 (young Terman), Terman *The Measurement of Intelligence* 1916, *Leland Stanford Junior University* founding grant, CSL catalogue | `find_media.py archive-texts` / `files` |
| newspapers | **archive.org** — The New York Times, Nov 7 1928 front page (full-page scan) | headline bboxes recorded in SOURCES |
| archival footage | **archive.org**: California Revealed (`copl_000211` UC Berkeley 1932 graduation), Ford Motor Co./NARA (Hoover 1928), Prelinger ("How To Take A Test", "Radio and Television" 1940), NARA newsreel (Vannevar Bush 1945), GE 1923 film | trimmed 6–20 s, h264, 24 fps |
| maps | NASA Blue Marble / Visible Earth (basemaps), USGS The National Map historical topos (Palo Alto 1899, Boston 1903), Library of Congress via Commons (Rand McNally 1920 railroad map), AWS Terrain Tiles (relief, registry.opendata.aws), us-atlas via jsDelivr + Natural Earth (state/river geometry) | generators in `tools/gen_*.py` |
| textures | **texturelabs.org** (18 textures: grunge, paper, halftone, lensfx) + synthetic grain | §3.4 |
| TV sets / props | Wikimedia Commons CC0 museum photos (Philco Predicta, RCA TRK-12, Bush TV22, Westinghouse 196) | screen made transparent |
| logos | HyperFrames `media-use resolve --type logo` (theSVG / official marks), Commons for the rest | `assets/logos/` |
| sound | 100 % synthesized score + SFX (`tools/audio/`), Kenney.nl CC0 packs | no third-party music |
| data | companiesmarketcap.com (trillion-dollar list, dated) | always date-stamp data |
| reference reels | Instagram via Agent Reach's yt-dlp | studied copies in `references/reels/` |

Blocked or flaky: Library of Congress search/API (blocks all scripts; its image servers tile/cdn.loc.gov work — MANUAL §8.1), Wikimedia originals (429),
Instagram from datacenter IPs. Cloud sessions: see `CLOUD_SETUP.md` (Full network access) and the fetch relay (§8.2).
