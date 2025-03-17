from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class CustomServer(BaseHTTPRequestHandler):
    def _send_response(self, status, data):
        """Helper function to send HTTP responses"""
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def do_GET(self):
        """Handles GET requests"""
        response = {"message": "This is a GET request", "path": self.path}
        self._send_response(200, response)

    def do_POST(self):
        """Handles POST requests"""
        content_length = int(self.headers['Content-Length']) if self.headers.get('Content-Length') else 0
        post_data = self.rfile.read(content_length) if content_length > 0 else b'{}'
        
        try:
            post_json = json.loads(post_data.decode())
        except json.JSONDecodeError:
            post_json = {"error": "Invalid JSON"}

        response = {"message": "This is a POST request", "data": post_json}
        self._send_response(201, response)

    def do_PUT(self):
        """Handles PUT requests"""
        response = {"message": "This is a PUT request", "path": self.path}
        self._send_response(200, response)

    def do_DELETE(self):
        """Handles DELETE requests"""
        response = {"message": "This is a DELETE request", "path": self.path}
        self._send_response(200, response)

if __name__ == '__main__':
    server_address = ('0.0.0.0', 5000)  # Runs on localhost:5000
    httpd = HTTPServer(server_address, CustomServer)
    print("Server running on port 5000...")
    httpd.serve_forever()
