from http.server import HTTPServer, SimpleHTTPRequestHandler
from router.routers import URLResolver
from template_engine import base_templates

from settings import HOST_NAME, PORT


class CustomRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        view = URLResolver.get_controller(self.path)

        if view:
            self.send_response(200, "OK")
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(view(), "utf-8"))
        else:
            html_404 = base_templates.get_404_template()
            self.send_response(404)
            self.end_headers()
            self.wfile.write(html_404)


server = HTTPServer((HOST_NAME, PORT), CustomRequestHandler)
