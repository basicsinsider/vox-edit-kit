# assets/intro/cutouts — SOURCES (gatherer A, 2026-10-31)
Made with `npx hyperframes@0.8.217 remove-background` (one at a time), from files in ../photos (see ../photos/SOURCES.md for licence/author; the cutout inherits it).

| file | subject | made from | prep | licence (inherited) | size |
|---|---|---|---|---|---|
| tsao_cutout.png | Robert Tsao, modern, head+shoulders, black polo | ../photos/tsao_advisor_cc0.jpg (曹興誠顧問.jpg) | none | Attribution — 總統府 | 1280x1805 |
| tsao_vase_cutout.png | Robert Tsao, white shirt/gold tie, leaning on table, with vase | ../photos/tsao_portrait_cc0.jpg (Robert Tsao (2).jpg) | none | Attribution — NYCU 秘書處 | 1280x1921 (upscaled from 853x1280) |
| chang_1951_cutout.png | Morris Chang, 1951 MIT yearbook | ../photos/chang_1951_mit.jpg | Gaussian blur 1.6 px (halftone) | Public domain | 1280x1703 (upscaled from 962x1280) |
| chang_2017_cutout.png | Morris Chang, modern bust, suit + tie (2017) | ../photos/chang_award.jpg crop x900–1560 y0–760, cutout trimmed to 600x560 | crop; bottom edge is flat (trophy hand removed) — mask the bottom in a card | CC BY 2.0 — Office of the President, Taiwan | 600x560 |

Rejected: cutout from chang_2018.jpg (microphone left a hole across his chin/tie).
| phone_pushbutton_cutout.png | brown push-button desk telephone (hand polygon mask; remove-background failed on the object) | ../photos/phone_pushbutton_brown_cc0.jpg | polygon mask, 2 px feather | CC0 — Alf van Beem | 1172x1059 |
| phone_pushbutton_halftone.png | same, 45° halftone (tools/halftone.py --cell 9 --transparent-paper) × the cutout alpha — D01 base object | phone_pushbutton_cutout.png | halftone | CC0 | 1172x1059 |
| fab_walker_cutout.png | the cardigan-wearing manager walking the factory floor (IS004 freeze) | ../made/fab_walk_freeze_2p9.jpg (footage still) | remove-background + polygon trim | as the footage | 1440x1080 |

## intro02 editor (2026-10-31)
| file | from | how |
|---|---|---|
| chang_2018_crop.jpg | photos/chang_2018.jpg (CC BY 2.0, Office of the President ROC) crop 240,40 → 1200×1080 | head & shoulders, the IS043 reveal plate |
| chang_2018_cutout.png | the crop above | `hyperframes remove-background` (mic hole — only used to make the matte below) |
| silhouette_exec.png / silhouette_exec_night.png | matte of the cut-out, holes filled (scipy binary_fill_holes), filled #141b24 (paper) / #2a2e33 (night) | N38 grey executive silhouette — same pixel space as chang_2018_crop.jpg so the burn reveal lines up |
| tsao_rally_figure.png | photos/tsao_rally_2023.jpg crop 600,560 → 690×1390, remove-background, white-shirt bystander keyed out, cut at the waist (900 px) | IS033 stonewall cut-out |

Not added by gatherer A (another agent made these; owner must log): chang_2018_crop.jpg, chang_2018_cutout.png, phone_pushbutton_cutout.png, phone_pushbutton_halftone.png, silhouette_exec.png, silhouette_exec_night.png, tsao_rally_figure.png, tsao_rally_head.jpg.
