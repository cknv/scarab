"""Tests for the servers module."""
import scarab
from scarab import servers


def test_preview_server():
    """Simple tests for the PreviewServer."""
    server = servers.PreviewServer(8000)
    assert server.pages == {}

    pages = [
        scarab.pages.Page('some/path', b'some bytes'),
    ]

    server.set_pages(pages)

    simplified_pages = {
        '/' + page.path: page.bytes
        for page in pages
    }
    assert server.pages == simplified_pages
