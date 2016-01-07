"""Scarab servers."""
from http import server


class PreviewServer:

    """A server for previewing pages locally."""

    def __init__(self, port):
        """Create a new PreviewServer."""
        server_address = ('localhost', port)
        self._server = server.HTTPServer(server_address, _PreviewHandler)
        self._server.pages = {}

    def set_pages(self, pages):
        """Set the servers pages."""
        self._server.pages = {
            '/' + page['destination']: page['bytes']
            for page in pages
        }

    def serve_forever(self):
        """Serve forever, just like the inner server."""
        self._server.serve_forever()

    def shutdown(self):
        """Do a clean shutdown of the inner server."""
        self._server.shutdown()


class _PreviewHandler(server.BaseHTTPRequestHandler):

    """Handler for the PreviewServer."""

    def load_page(self, path):
        """Load a page, or raise KeyError."""
        if path.endswith('/'):
            path = path + 'index.html'

        return self.server.pages[path]

    def do_GET(self):
        """Handle GET requests."""
        try:
            content = self.load_page(self.path)
        except KeyError:
            self.send_response(404)
            self.end_headers()
        else:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(content)
