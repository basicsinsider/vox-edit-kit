"""Assemble compositions/c5s03.html from the parts in this folder (edit the parts, re-run)."""
import os
D = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(D, "../../../.."))
p = lambda n: open(os.path.join(D, n)).read()
html = f"""<!doctype html>
<html lang="en">
<head><meta charset="UTF-8" /></head>
<body>
<template>
  <style>
{p('1_style.css')}
  </style>
{p('2_markup.html')}
  <script>
  (function () {{
{p('3_a.js')}
{p('3_b.js')}
{p('3_c.js')}
    FX.mount(tl, DURATION);
    window.__timelines = window.__timelines || {{}}; window.__timelines[SEG] = tl;
  }})();
  </script>
</template>
</body>
</html>
"""
open(os.path.join(ROOT, "compositions/c5s03.html"), "w").write(html); print("wrote compositions/c5s03.html", len(html))
