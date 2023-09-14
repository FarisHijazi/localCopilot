from http.server import BaseHTTPRequestHandler, HTTPServer


class RequestHandler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        if (
            self.path
            == "/openai/deployments/asdf/chat/completions?api-version=2023-03-15-preview"
        ):
            self.send_response(200)
            self.send_header("Allow", "OPTIONS, GET, POST")
            self.end_headers()
            self.wfile.write(b"Intercepted the desired request!")
        else:
            self.send_response(404)
            self.end_headers()


def run(server_class=HTTPServer, handler_class=RequestHandler, port=5000):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting httpd on port {port}...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
