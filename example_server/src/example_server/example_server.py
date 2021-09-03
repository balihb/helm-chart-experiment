import http.server
import os
import socketserver

import jsonpickle

json_data = jsonpickle.encode({
  "my_key1": "my_data1",
  "my_key2": "my_data2",
  "my_key3": {
    "my_sub_key1": "my_sub_data1",
    "my_sub_key2": "my_sub_data2"
  }
}, indent=4)


class ExampleHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)

        self.send_header("Content-Type", "application/json")

        self.end_headers()

        self.wfile.write(bytes(json_data, "utf-8"))

        return


def main():
    handler = ExampleHttpRequestHandler

    port = int(os.getenv('EXAMPLE_HTTP_SERVER_PORT', 8080))
    example_http_server = socketserver.TCPServer(('', port), handler)

    example_http_server.serve_forever()
