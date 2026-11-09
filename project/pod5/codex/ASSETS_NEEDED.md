# Taiwan podcast — assets used and gaps

The files below were inspected in the edited frames. Existing folder `SOURCES.md` files record the source URL, author and rights; the sound IDs are in `assets/audio/epidemic/LOG.md`. On-screen credits appear for the credited photos, maps, film and poster. A `✅` means present and used; `🔁` means an illustrative stand-in; `❌` means a source specifically matching the period/event was not located locally.

| Status | Asset | Use / limitation | Source log |
|---|---|---|---|
| ✅ | `input/BB_podcast_v2_first5min.mp4` | Original camera cuts and continuous mono voice; MD5 verified; ignored by Git | User supplied |
| ✅ | `assets/intro/photos/tsao_portrait_cc0.jpg`, `tsao_advisor_cc0.jpg` | Tsao identification; these are modern portraits, not 1983 images | `assets/intro/photos/SOURCES.md` |
| ✅ | `assets/intro/made/tsao_layers/{backdrop.jpg,tsao.png,vase.png}` | Layered portrait treatment derived from the first Tsao image | `assets/intro/made/SOURCES.md` |
| 🔁 | `assets/intro/photos/umc_fab8ab.jpg` | UMC building used as a company/factory identification image; photograph is from 2021, credited with date | `assets/intro/photos/SOURCES.md` |
| 🔁 | `fab_floor_manager_walks_rows.mp4`, `fab_hk_workers_microscope_rows_a.mp4`, `wafer_closeup_purple.mp4`, `wafer_die_pattern_macro.mp4` | Illustrative Prelinger semiconductor footage, filmed at a different plant; not presented as the actual UMC factory | `assets/intro/footage/SOURCES.md` |
| 🔁 | `jet_707_takeoff_hongkong.mp4` | Illustrative flight footage, not Tsao's actual flight | `assets/intro/footage/SOURCES.md` |
| ✅ | `phone_pushbutton_cutout.png`, `phone_pushbutton_halftone.png`, `phone_pushbutton_brown_cc0.jpg` | Period telephone diagram and export chart | `assets/intro/cutouts/SOURCES.md`, `assets/intro/photos/SOURCES.md` |
| ✅ | `wafer_12in.jpg`, `fab_walk_freeze_2p9.jpg`, `ibm_5154_monitor_frame_withbg.jpg` | Chip, comparison and product imagery | `assets/intro/photos/SOURCES.md`, `assets/intro/made/SOURCES.md`, `assets/intro/screens/SOURCES.md` |
| ✅ | `pacific_night.jpg`, `east_asia_night.jpg`, `taiwan_relief_grey.jpg`, `taiwan_celadon_wash.png` | Geography and Taiwan motif | `assets/maps/kit/SOURCES.md`, `assets/intro/maps/SOURCES.md`, `assets/intro/made/SOURCES.md` |
| ✅ | `silhouette_exec.png`, `silhouette_exec_night.png` | Anonymous adviser; no recognizable identity or company revealed | `assets/intro/cutouts/SOURCES.md` |
| ✅ | `twa_new_york_1958_klein.jpg` | New York travel-poster imagery; printed title cropped and separately timed | `assets/intro/paintings/SOURCES.md` |
| ✅ | `stone_wall_texture_cc0.jpg` | Visual metaphor for being stonewalled | `assets/intro/photos/SOURCES.md` |
| ✅ | `paper_cream_01.jpg`, `paper_graph_01_hires.jpg`, `paper_stained_01_hires.jpg`, `paper_lined_01_hires.jpg`, K+E grid card | House paper grounds and card textures | `assets/textures/SOURCES.md`, `assets/intro/papers/SOURCES.md` |
| ✅ | Cooper Hewitt, Haskoy, Crimson Pro in `assets/fonts/` | House typography | `assets/fonts/SOURCES.md` if present; kit font files |
| ✅ | Melting Glass, Woodwind Reviere, Lightbulb Moment, Interstice of Sound stems; Epidemic stamp and paper sounds; kit generated/local effects | Layered music and SFX; licensed WAVs ignored by Git | `assets/audio/epidemic/LOG.md`, `project/pod5/codex/music_cuesheet.json`, `compositions/pod5*.sfx.json` |
| ❌ | Confirmed 1983 Tsao portrait and actual UMC fab-floor footage | Modern credited portraits and explicitly illustrative archival footage used instead | — |
| ❌ | A listening review by an editor | Automated loudness and visual checks completed; final mix still requires a human listening pass | — |

No source or final master video over 95 MB is included in the branch. The 720p review is under that limit. Rebuild sound with `tools/build_pod5_audio.sh` after restoring the ignored source and licensed WAVs, then rebuild wrappers with `project/pod5/codex/build_pod5.py`.
