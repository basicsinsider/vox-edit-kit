"""Inline assets/intro/derived/intro03/data.json into compositions/intro03.html between /*DATA-BEGIN*/ and /*DATA-END*/."""
import pathlib, re
R = pathlib.Path(__file__).resolve().parents[3]
f = R / "compositions/intro03.html"
src = f.read_text()
data = (R / "assets/intro/derived/intro03/data.json").read_text()
src = re.sub(r"/\*DATA-BEGIN\*/.*?/\*DATA-END\*/", lambda m: "/*DATA-BEGIN*/" + data + "/*DATA-END*/", src, flags=re.S)
f.write_text(src); print("spliced", len(data))
