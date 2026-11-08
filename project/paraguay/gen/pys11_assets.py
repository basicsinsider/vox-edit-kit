"""pys11 derived assets: crops of the real ABC Color screenshots (shared/docs) for the newspaper page, cork clippings and phones.
Run: python3 project/paraguay/gen/pys11_assets.py   (from the repo root)"""
from PIL import Image, ImageFilter
D = "assets/paraguay/shared/docs/"
O = "assets/paraguay/pys11/derived/"
def crop(src, box, out, q=90, maxw=None):
    im = Image.open(D + src).convert("RGB").crop(box)
    if maxw and im.width > maxw:
        im = im.resize((maxw, round(im.height * maxw / im.width)), Image.LANCZOS)
    im.save(O + out, quality=q); print(out, im.size)
SEN = "abc_article_2026-09-14_senado_acorrala_bcp.jpg"
# full article column (headline, photo, first body lines) = the newspaper page (page px = full px - (820, 800))
crop(SEN, (820, 800, 2380, 2400), "abc_senado_page.jpg")
# blurred background copy (whole screenshot, dark)
im = Image.open(D + SEN).convert("RGB").resize((1600, 1200), Image.LANCZOS).filter(ImageFilter.GaussianBlur(10)); im.save(O + "abc_senado_bg.jpg", quality=80)
# cork clippings (headline + top of the photo; no date line)
crop("abc_article_2026-07-08_ips_catarata_fondos.jpg", (830, 890, 2370, 1560), "clip_ips_catarata.jpg", maxw=900)
crop("abc_article_2026-07-06_ips_exceso_fondos.jpg", (830, 890, 2370, 1560), "clip_ips_exceso.jpg", maxw=900)
crop("abc_article_2026-11-07_esquema_seis_hechos.jpg", (830, 890, 2370, 1520), "clip_esquema.jpg", maxw=900)
crop("abc_article_2025-12-14_grupo_vazquez_780m.jpg", (980, 890, 2240, 1075), "clip_vazquez_780m.jpg", maxw=760)
crop("abc_article_2025-04-05_pena_vendio_acciones.jpg", (980, 890, 2240, 1160), "clip_pena_acciones.jpg", maxw=760)
# phone screens (masthead + article top)
for s, o in [(SEN, "phone_senado.jpg"), ("abc_article_2026-11-07_esquema_seis_hechos.jpg", "phone_esquema.jpg"),
             ("abc_article_2026-07-08_ips_catarata_fondos.jpg", "phone_ips.jpg"), ("abc_article_2025-12-14_grupo_vazquez_780m.jpg", "phone_vazquez.jpg"),
             ("abc_article_2025-04-05_pena_vendio_acciones.jpg", "phone_acciones.jpg")]:
    crop(s, (933, 181, 2253, 2213), o, maxw=660)
crop("abc_homepage_2026-11-08.jpg", (490, 181, 2710, 1813), "phone_home.jpg", maxw=900)
# phone screens v2: ABC masthead strip (logo + date, from the same screenshot) + the article from its section line down (ads skipped)
for s, o in [(SEN, "phone_senado.jpg"), ("abc_article_2026-11-07_esquema_seis_hechos.jpg", "phone_esquema.jpg"),
             ("abc_article_2026-07-08_ips_catarata_fondos.jpg", "phone_ips.jpg"),
             ("abc_article_2025-04-05_pena_vendio_acciones.jpg", "phone_acciones.jpg")]:
    im = Image.open(D + s).convert("RGB")
    head = im.crop((500, 185, 1730, 335)); art = im.crop((990, 840, 2220, 2213))
    out = Image.new("RGB", (1230, 150 + 30 + art.height), (255, 255, 255))
    out.paste(head, (0, 0)); out.paste(art, (0, 180))
    out = out.resize((615, round(out.height / 2)), Image.LANCZOS); out.save(O + o, quality=90); print(o, out.size)
# blurred homepage for the ABC Color reveal background
im = Image.open(D + "abc_homepage_2026-11-08.jpg").convert("RGB").crop((480, 160, 2720, 1840)).resize((1600, 1200), Image.LANCZOS).filter(ImageFilter.GaussianBlur(9))
im.save(O + "abc_home_bg.jpg", quality=80); print("abc_home_bg.jpg", im.size)
