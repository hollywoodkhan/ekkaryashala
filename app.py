from pathlib import Path


ROOT = Path(__file__).resolve().parent


def app(environ, start_response):
    path = environ.get("PATH_INFO", "/") or "/"
    if path == "/":
        file_path = ROOT / "index.html"
        content_type = "text/html; charset=utf-8"
    elif path == "/styles.css":
        file_path = ROOT / "styles.css"
        content_type = "text/css; charset=utf-8"
    elif path == "/script.js":
        file_path = ROOT / "script.js"
        content_type = "application/javascript; charset=utf-8"
    else:
        body = b"Not Found"
        start_response("404 Not Found", [("Content-Type", "text/plain; charset=utf-8")])
        return [body]

    if file_path.exists():
        body = file_path.read_bytes()
        start_response("200 OK", [("Content-Type", content_type), ("Content-Length", str(len(body)))])
        return [body]

    start_response("404 Not Found", [("Content-Type", "text/plain; charset=utf-8")])
    return [b"Not Found"]
