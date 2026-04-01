from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer


HOST = "0.0.0.0"
PORT = 7799


def run_server() -> None:
    server = ThreadingHTTPServer((HOST, PORT), SimpleHTTPRequestHandler)
    print(f"HTTP server is running at http://localhost:{PORT}/")
    print("Press Ctrl+C to stop.")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server...")
    finally:
        server.server_close()


if __name__ == "__main__":
    run_server()