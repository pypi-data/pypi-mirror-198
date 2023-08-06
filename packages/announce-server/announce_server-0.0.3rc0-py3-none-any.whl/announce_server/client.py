import argparse
import asyncio
import signal
import sys
import threading
from http.server import HTTPServer, SimpleHTTPRequestHandler

import socketio

from .decorator import register_service
from .get_ip import get_ip_address

http_server_thread = None

def start_client(host_ip="0.0.0.0", host_port=4999):
    @register_service(
        name="test client",
        ip=get_ip_address(),
        port=13373,
        host_ip=host_ip,
        host_port=host_port,
    )
    def server(port=13373):
        def start_server():
            global http_server_thread
            print(f"Serving HTTP on 0.0.0.0 port {port} (http://0.0.0.0:{port}/) ...")
            httpd = HTTPServer(("", port), SimpleHTTPRequestHandler)
            httpd.serve_forever()
        server_thread = threading.Thread(target=start_server)
        server_thread.daemon = True
        server_thread.start()
        server_thread.join()

    def signal_handler(signal, frame):
        print("Cleaning up and shutting down...")

        # If the HTTP server thread is running, shut it down
        if http_server_thread is not None and http_server_thread.is_alive():
            http_server_thread.shutdown()

        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    try:
        server()
        signal.pause()
    except asyncio.exceptions.CancelledError:
        print("CancelledError")
        # signal_handler(signal.SIGINT, None)
        pass
    finally:
        print("Shutting down test client...")
        sys.exit(0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Start announce_server client.")
    parser.add_argument(
        "--host-ip",
        type=str,
        default="0.0.0.0",
        help="Host IP address (default: 0.0.0.0)",
    )
    parser.add_argument(
        "--host-port", type=int, default=4999, help="Host port number (default: 4999)"
    )
    args = parser.parse_args()

    start_client(args.host_ip, args.host_port)
