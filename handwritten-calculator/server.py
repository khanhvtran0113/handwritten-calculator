from http.server import BaseHTTPRequestHandler, HTTPServer
import json

from main import handleBase64Image


class RequestHandler(BaseHTTPRequestHandler):
    def _send_response(self, status_code, message):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', 'http://localhost:3000')  # Local FE
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
        self.wfile.write(json.dumps(message).encode('utf-8'))

    def do_OPTIONS(self):
        self._send_response(200, {'status': 'success', 'message': 'CORS preflight request handled'})

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        payload = self.rfile.read(content_length).decode('utf-8')

        try:
            # Parse received data
            data = json.loads(payload)
            image_string = data["image_string"]
            base = data["base"]
        except json.JSONDecodeError:
            response_message = {'status': 'error', 'message': 'Invalid JSON payload'}
            self._send_response(200, response_message)
            return

        answer, symbols = handleBase64Image(image_string, base)
        response_message = {'status': 'success', "answer": answer, "equation": symbols}
        self._send_response(200, response_message)


def run():
    port = 8000
    server_address = ('', port)
    httpd = HTTPServer(server_address, RequestHandler)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()


if __name__ == '__main__':
    run()