"""
VanCheck local development server.

Run:
    python python.py

Then open http://127.0.0.1:8000 in your browser.

This server only serves the local prototype files. Inspection data and photos are
stored by the browser in localStorage; this Python server does not receive them.
"""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import os

HOST = "127.0.0.1"
PORT = 8000
APP_DIR = Path(__file__).resolve().parent


class VanCheckHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(APP_DIR), **kwargs)

    def end_headers(self):
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Referrer-Policy", "same-origin")
        super().end_headers()


def main():
    os.chdir(APP_DIR)
    server = ThreadingHTTPServer((HOST, PORT), VanCheckHandler)
    print(f"VanCheck is running at http://{HOST}:{PORT}")
    print("Press Ctrl+C to stop the server.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\\nStopping VanCheck...")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
