# assets/cartels/cts05 — sources (cts05 segment editor, 2026-11-22)
All looked at before use. Commons files fetched as 1920 px thumbnails (`tools/commons_thumb.sh`).

| file | subject | URL | licence | author | date | size |
|---|---|---|---|---|---|---|
| photos/trump_day1_eo_signing.jpg | President Trump signing executive orders on Day One (Capital One Arena, Washington) — pixel-identical to `assets/cartels/people/trump_eo_day1_1.jpg` | https://commons.wikimedia.org/wiki/File:Trump_Day_1_Executive_Order_Signing.jpg (orig. https://x.com/VP/status/1882163616646132011/photo/1) | PD-USGov | @VP (Office of the Vice President) | 2025-01-20 | 1920×1281 |
| photos/sheinbaum_2025_eneas.jpg | Claudia Sheinbaum at her morning press conference | https://commons.wikimedia.org/wiki/File:Claudia_Sheinbaum_(2025)_(cropped).jpg (Flickr 54720468437) | CC BY 4.0 — on-screen credit "Photo: Eneas / CC BY 4.0" | Eneas | 2025-08-14 | 1920×2563 |
| photos/white_house_south.jpg | South Lawn and south facade of the White House | https://commons.wikimedia.org/wiki/File:WhSouthLawn.JPEG | PD-USGov-Military | PHC C.M. Fitzpatrick, U.S. DoD | 1987-07-01 | 1920×1536 |
| photos/liberation_day_chart.jpg | Trump holding the "Reciprocal Tariffs" chart, "Make America Wealthy Again" event ("Liberation Day"), Rose Garden | https://commons.wikimedia.org/wiki/File:Trump_showing_a_chart_with_reciprocal_tariffs.jpg (Flickr whitehouse 54427036491) | PD-USGov-POTUS | Official White House Photo by Daniel Torok | 2025-04-02 | 1920×1280 |
| photos/laredo_trade_crossing.jpg | CBP checks trucks inbound from Mexico at the World Trade Crossing International Bridge, Laredo, Texas (Rio Grande behind) | https://commons.wikimedia.org/wiki/File:World_Trade_Crossing_International_Bridge_in_Laredo,_Texas_(35598331400).jpg | PD-USGov-DHS-CBP | U.S. Customs and Border Protection | 2017-04-12 | 1920×1280 |
| photos/fentanyl_rainbow_m30.jpg | counterfeit "rainbow" fentanyl M30 pills (DEA, "DEA" label burned in by the DEA) | https://commons.wikimedia.org/wiki/File:Rainbow_Fentanyl_M30.jpg (Flickr 52389397833) | PD-USGov-DEA | Drug Enforcement Administration | 2022-08-11 | 1920×1541 |
| photos/flag_usa.png | Flag of the United States | https://commons.wikimedia.org/wiki/File:Flag_of_the_United_States.svg | PD | — | — | 1920×1011 |
| photos/flag_mexico.png | Flag of Mexico | https://commons.wikimedia.org/wiki/File:Flag_of_Mexico.svg | PD | — | — | 1920×1098 |

Derived (made by `project/cartels/gen/cts05_assets.py` + `npx hyperframes@0.8.217 remove-background`):
| file | from | what |
|---|---|---|
| derived/trump_cut.png | trump_day1_eo_signing.jpg crop (880,380)–(1800,1281) | person cut-out (matting) |
| derived/trump_duo.png | trump_cut.png | VP Vance's hands + matting ghost removed by polygon; steel duotone + 45° halftone |
| derived/sheinbaum_cut.png | sheinbaum_2025_eneas.jpg (1200 px) | person cut-out |
| derived/sheinbaum_duo.png | sheinbaum_cut.png | olive duotone + 45° halftone |
| derived/nbc_header.jpg | `assets/cartels/news/n_armed_nbc.jpg` (2240×1760 capture of 04:51) | frozen copy of the NBC News header (headline + deck), unedited |
| derived/nbc_body_alqaeda.jpg | `assets/cartels/news/n_armed_nbc_k2.jpg` crop (140,250)–(1300,730) | NBC body: the notice quote + "…same legal category as terrorist groups like Al Qaeda or the Islamic State." — real text, unedited |

Shared assets used (logged by their gatherers): `assets/cartels/docs/d01_eo14157_p1.jpg` (Federal Register, EO 14157),
`assets/cartels/news/n_armed_nbc.jpg` + `n_armed_nbc_k2.jpg` (NBC News, Oct 2025; URL in n_armed_nbc.json).
