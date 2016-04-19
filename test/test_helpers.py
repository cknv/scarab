"""Tests for the helpers."""
import pytest

from scarab import helpers


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
        'sha512-ZcJWxjm9bdSDvjQYMcGaOZaVSQG7Kgf3lZPz469WklWb2xJNCZwrks7X5Zt+0C07f0LVB0DZmb69kZg9soQnYg==',  # pylint: disable=line-too-long
    ),
])
def test_subresource_integrity(algorithm, sri):
    """Test specific SRI algorithms."""
    value = b'some content'

    assert helpers.subresource_integrity(value, algorithm) == sri
