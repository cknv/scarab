"""Tests for the page module."""
import hashlib

from scarab import pages


def test_single_page():
    """Test the Page class simple behaviour."""
    bytes_value = b'some bytes'
    page_path = '/some/path/some.file'

    page = pages.Page(
        page_path,
        bytes_value,
        other_key='other_value',
    )

    assert page.path == page_path
    assert page.bytes == bytes_value

    hexdigest = hashlib.sha512(bytes_value).hexdigest()
    assert page.checksum == hexdigest
    assert repr(page) == '<Page {} {}>'.format(
        page_path,
        hexdigest,
    )
    assert page['other_key'] == 'other_value'
    assert page != 'hey! a string?!'
    assert 'hey! another string?!' != page
