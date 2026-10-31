"""Inline the map paths into the c5s02 template → compositions/c5s02.html."""
import os
R = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
R = os.path.dirname(R)
src = open(R + "/project/c5/gen/c5s02_template.html").read()
paths = open(R + "/assets/c5/derived/c5s02/c5s02_paths.json").read()
assert "/*PATHS*/null" in src
open(R + "/compositions/c5s02.html", "w").write(src.replace("/*PATHS*/null", paths))
print("wrote compositions/c5s02.html")
