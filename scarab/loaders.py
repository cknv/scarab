"""Home of the loaders."""
import os

from PIL import Image


def file_names(directory):
    """Yield the names of the files in a given directory."""
    for subdir, __, names in os.walk(directory):
        for file_name in names:
            yield os.path.join(subdir, file_name)


def image_loader(directory):
    """Load the files in a given directory as images."""
    for each in file_names(directory):
        yield {
            'path': each,
            'image': Image.open(each),
        }


def plaintext_loader(directory):
    """Load the files in a given directory as plaintext files."""
    for each in file_names(directory):
        with open(each) as fo:
            yield {
                'path': each,
                'raw': fo.read(),
            }
