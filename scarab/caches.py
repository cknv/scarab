"""Scarab caches."""
import hashlib

from .loaders import file_names


class OutputCache:
    """Cache that helps filter away any files that are the same.

    Builds a cache from the directory it is given.
    Then uses that cache to eliminate items from a sequence, when used.
    """

    def __init__(self, directory):
        """Create a new OutputCache."""
        self.directory = directory
        self.cache = {
            file_name: self._file_checksum(file_name)
            for file_name in file_names(directory)
        }

    @classmethod
    def _file_checksum(cls, file_name):
        """Get the checksum of the contents of a file."""
        with open(file_name, 'br') as fo:
            return cls._calc_checksum(fo.read())

    @staticmethod
    def _calc_checksum(value):
        """Return the checksum of some bytes."""
        return hashlib.md5(value).hexdigest()

    def filter(self, generator):
        """Yield items from a generator if they are not known."""
        for each in generator:
            value = self._calc_checksum(each['bytes'])
            full_destination = self.directory + '/' + each['destination']
            if self.cache.get(full_destination) == value:
                continue

            yield each
            self.cache[full_destination] = value
