"""Tests for the page module."""
import hashlib

import pytest

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


def test_page_extra_values():
    """Test the dict like behaviour of a page."""
    page = pages.Page('path', b'bytes')

    assert 'key' not in page
    page['key'] = 'value'
    assert 'key' in page
    assert page['key'] == 'value'
    assert len(page) == 1


def test_subresource_integrity_default():
    """Test the default SRI algorithm works."""
    page = pages.Page(
        '/some/path',
        b'some content',
    )

    assert page.subresource_integrity() == 'sha512-ZcJWxjm9bdSDvjQYMcGaOZaVSQG7Kgf3lZPz469WklWb2xJNCZwrks7X5Zt+0C07f0LVB0DZmb69kZg9soQnYg=='


@pytest.mark.parametrize('algorithm, sri', [
    (
        'sha256',
        'sha256-KQ9JPET11j0Gs3TQpavSkvrji5LKsvrl7+/hsOk0f1Y=',
    ),
    (
        'sha384',
        'sha384-ZrNwfq7T9/TG8ITkunqqlfBBLD2f2RR1/EVLk+2LfNnTPMGCHlF7UtM4+NjWkIy5',
    ),
    (
        'sha512',
        'sha512-ZcJWxjm9bdSDvjQYMcGaOZaVSQG7Kgf3lZPz469WklWb2xJNCZwrks7X5Zt+0C07f0LVB0DZmb69kZg9soQnYg==',
    ),
])
def test_subresource_integrity(algorithm, sri):
    """Test specific SRI algorithms."""
    page = pages.Page(
        '/some/path',
        b'some content',
    )

    assert page.subresource_integrity(algorithm) == sri
