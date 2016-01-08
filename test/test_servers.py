"""Tests for the servers module."""
from scarab import servers


def test_preview_server():
    """Simple tests for the PreviewServer."""
    server = servers.PreviewServer(8000)
    assert server._server.pages == {}

    pages = [
        {
            'destination': 'some/path',
            'bytes': b'some bytes',
        },
    ]

    server.set_pages(pages)

    simplified_pages = {
        '/' + page['destination']: page['bytes']
        for page in pages
    }
    assert server._server.pages == simplified_pages
