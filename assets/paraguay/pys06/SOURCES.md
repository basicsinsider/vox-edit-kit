# pys06 assets (segment editor pys06, 2026-11-08)

| file | subject | source / URL | licence | author | date | size |
|---|---|---|---|---|---|---|
| photos/abc_ips_gremio_2024_10.jpg | Corriente Sindical Clasista protest in front of IPS (Hospital Ingavi) against Peña's IPS fund policy / IPS investment in ueno (Peña a ueno Holding shareholder) — used under "people were out there protesting" ("two years ago") | https://www.abc.com.py/politica/2024/10/16/gremio-repudia-que-pena-siga-dilapidando-fondos-jubilatorios-del-ips/ (og:image, resizer width=1920) | © ABC Color, fair use — on-screen credit "Photo: ABC Color, Oct 2024" | ABC Color | 2024-10-16 | 1920×1280 |
| derived/pena_sash_cut.png | Peña with the presidential sash, background removed (2.5D subject layer) | `npx hyperframes@0.8.217 remove-background` of shared/photos/pena_sash_crop.jpg (Commons "Santi Peña and William Lai (cropped)2.jpg") | CC BY 2.0, Office of the President (ROC) — on-screen credit | — | 2023-08-16 | 743×990 RGBA |
| derived/pena_backdrop_blur.jpg | blurred greyscale copy of pena_sash_crop (far 2.5D plate, tinted plum in CSS) | derived (PIL GaussianBlur 14+10, 1920×1080 crop) | as above | — | — | 1920×1080 |
| derived/facecam_595_75.jpg | still of the face cam at master 595.75 s (covers the 3 frames before the EDL join 595.683 → picture change at 595.725) | `ffmpeg -ss 595.75 -i assets/facecam/paraguay_facecam_master.mp4 -frames:v 1` | Krish's own footage | — | — | 1920×1080 |

Shared assets used (logged in shared/*/SOURCES.md): photos/pena_sash_crop.jpg, ips_hospital.jpg (CC BY-SA 3.0, Iamlatin),
pena_portrait_reuters.jpg (© Reuters/Cesar Olmedo), ueno_sign_hq_reuters.jpg (© Reuters); logos/ueno_logo.png.
