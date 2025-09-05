from wsgiref.simple_server import make_server

products = {"1": "Widget", "2": "Gadget"}

def app(environ, start_response):
    path = environ.get('PATH_INFO', '').lstrip('/')
    if path == "products":
        response_body = "<h1>Products</h1><ul>"
        for id, name in products.items():
            response_body += f"<li>{name} (ID: {id})</li>"
        response_body += "</ul>"
        status = '200 OK'
    else:
        response_body = "<h1>404 Not Found</h1>"
        status = '404 Not Found'

    headers = [('Content-Type', 'text/html')]
    start_response(status, headers)
    return [response_body.encode()]

if __name__ == "__main__":
    httpd = make_server('', 8000, app)
    print("Serving on port 8000...")
    httpd.serve_forever()
