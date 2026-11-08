#!/usr/bin/env python3
"""
SQUAD LEGENDS 3D — 1-CLICK LOCAL WI-FI HOTSPOT GAME & MULTIPLAYER SERVER
Run on Laptop or Android (Termux):
    python3 start_hotspot_server.py
Then any friend on the same Mobile Wi-Fi Hotspot opens:
    http://<YOUR_HOTSPOT_IP>:8080
and both players are automatically connected for 60FPS Local Hotspot Multiplayer!
"""
import json, socket, time
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs

ROOM_PACKETS = {}

class HotspotHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_POST(self):
        if self.path.startswith('/mp_sync'):
            length = int(self.headers.get('Content-Length', 0))
            raw = self.rfile.read(length).decode('utf-8', errors='ignore')
            try:
                pkt = json.loads(raw)
                room = pkt.get('room', 'SQ-101')
                pkt['_ts'] = time.time()
                ROOM_PACKETS.setdefault(room, []).append(pkt)
                ROOM_PACKETS[room] = [p for p in ROOM_PACKETS[room] if time.time() - p['_ts'] < 1.5][-40:]
            except Exception:
                pass
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'{"ok":true}')
            return
        super().do_POST()

    def do_GET(self):
        if self.path == '/' or self.path == '/index.html':
            self.path = '/app/src/main/assets/index.html'
            return super().do_GET()
        if self.path.startswith('/mp_poll'):
            qs = parse_qs(urlparse(self.path).query)
            room = qs.get('room', ['SQ-101'])[0]
            now = time.time()
            pkts = [p for p in ROOM_PACKETS.get(room, []) if now - p['_ts'] < 0.35]
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(pkts).encode('utf-8'))
            return
        return super().do_GET()

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = '192.168.43.1'
    finally:
        s.close()
    print("==========================================================")
    print("  SQUAD LEGENDS 3D — LOCAL HOTSPOT MULTIPLAYER SERVER")
    print(f"  Open on Host & Friend Phones: http://{ip}:8080")
    print("==========================================================")
    ThreadingHTTPServer(('0.0.0.0', 8080), HotspotHandler).serve_forever()
