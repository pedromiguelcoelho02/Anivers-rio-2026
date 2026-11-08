"""Serve a raiz do repositório localmente e abre um túnel Cloudflare (trycloudflare.com).

Uso:  .env\\Scripts\\python serve.py [porta]
"""
import functools
import http.server
import sys
import threading
import time
from pathlib import Path

from pycloudflared import try_cloudflare

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
SITE = Path(__file__).parent

handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(SITE))
server = http.server.ThreadingHTTPServer(("127.0.0.1", PORT), handler)
threading.Thread(target=server.serve_forever, daemon=True).start()
print(f"Local:  http://localhost:{PORT}", flush=True)

tunnel = try_cloudflare(port=PORT)
print(f"Público: {tunnel.tunnel}", flush=True)

try:
    while True:
        time.sleep(3600)
except KeyboardInterrupt:
    try_cloudflare.terminate(PORT)
    server.shutdown()
