"""Classes to represent pages for scarab."""
import hashlib


class Page:

    """A simple page, representing a page to be written."""

    def __init__(self, path, bytes_value, **kwargs):
        """Create a new page."""
        self.path = path
        self.bytes = bytes_value
        self._other_values = kwargs

    def __getitem__(self, key):
        """Return items from the kwargs given."""
        return self._other_values[key]

    def __repr__(self):
        """Return the representation."""
        return '<Page {} {}>'.format(
            self.path,
            self.checksum,
        )

    @property
    def checksum(self):
        """Return the checksum of the resource."""
        return hashlib.sha512(self.bytes).hexdigest()

    def __eq__(self, other):
        """Check for equality."""
        if not isinstance(other, type(self)):
            return NotImplemented

        page_eq = self.path == other.path
        bytes_eq = self.bytes == other.bytes
        other_values_eq = self._other_values == other._other_values

        return page_eq and bytes_eq and other_values_eq
