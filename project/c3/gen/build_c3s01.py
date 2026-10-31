"""Assemble compositions/c3s01.html from project/c3/gen/c3s01/* (+ derived JSON). Run from the repo root."""
import json, glob
D = "project/c3/gen/c3s01/"
html = "".join(open(D + f).read() for f in ["a_style.html", "b_scenes1.html", "b_scenes2.html", "b_scenes3.html", "b_scenes4.html", "c_script1.js", "c_script2.js", "c_script3.js"])
us = open("assets/c3/derived/c3s01/us_paths.json").read()
tw = open("assets/c3/derived/c3s01/pacific_taiwan.json").read()
html = html.replace("__US__", us).replace("__TW__", tw)
open("compositions/c3s01.html", "w").write(html)
print("wrote compositions/c3s01.html", len(html))
