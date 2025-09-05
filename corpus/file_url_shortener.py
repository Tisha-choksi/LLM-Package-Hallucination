from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi

urls = {}

class URLShortenerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/shorten'):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"<form method='POST' action='/shorten'>"
                             b"Long URL: <input type='text' name='long_url'>"
                             b"<input type='submit' value='Shorten'>"
                             b"</form>")
        else:
            self.send_error(404)

    def do_POST(self):
        if self.path == '/shorten':
            form = cgi.FieldStorage(self.rfile, self.headers)
            long_url = form.getvalue('long_url')
            short_url = f"http://short.url/{len(urls)}"
            urls[short_url] = long_url
            self.send_response(200)
            self.end_headers()
            self.wfile.write(f"Short URL: {short_url}".encode())

if __name__ == "__main__":
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, URLShortenerHandler)
    print("Serving on port 8000...")
    httpd.serve_forever()
