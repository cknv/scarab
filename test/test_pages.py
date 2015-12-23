"""Tests for the page module."""
import hashlib

from scarab import pages


def test_page_class():
    """Test page class test."""
    page = pages.Page(
        '/some/path/some.file',
        b'some bytes',
        other_key='other_value',
    )

    assert page.checksum == hashlib.sha512(b'some bytes').hexdigest()
    assert page['other_key'] == 'other_value'
    assert page.path == '/some/path/some.file'

    page_set = {page}
    assert page in page_set

    page2 = pages.Page('/some/path/some/other.file', b'some bytes')
    assert page2 != page
    assert page2 not in page_set

    page3 = pages.Page('/some/path/some.file', b'some bytes')
    assert page3 != page
    assert page3 not in page_set

    assert page != 'hey! a string?!'
    assert 'hey! another string?!' != page
