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

    @property
    def checksum(self):
        """Return the checksum of the resource."""
        return hashlib.sha512(self.bytes).hexdigest()

    def __hash__(self):
        """Return the python hash of the page."""
        return hash(self.path)

    def __eq__(self, other):
        """Check for equality."""
        return self.path
