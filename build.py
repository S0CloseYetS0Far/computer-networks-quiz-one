"""Build index.html from src/template.html, src/data.js and the figures in src/fig."""
import base64, json, pathlib

root = pathlib.Path(__file__).parent
src = root / "src"
page = (src / "template.html").read_text(encoding="utf8")
images = {
    f.stem: "data:image/jpeg;base64," + base64.b64encode(f.read_bytes()).decode()
    for f in sorted((src / "fig").glob("*.jpg"))
}
page = page.replace("/*__IMG__*/", "const IMG = " + json.dumps(images) + ";")
page = page.replace("/*__DATA__*/", (src / "data.js").read_text(encoding="utf8"))
page = page.replace('<div class="wrap">', '</head>\n<body>\n<div class="wrap">', 1)
html = '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n' + page + "\n</body>\n</html>\n"
(root / "index.html").write_text(html, encoding="utf8")
print("wrote index.html")
