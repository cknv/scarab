"""Writers module."""
import os


def bytes_writer(items, output_directory):
    """Write items to directory."""
    for item in items:
        full_destination = os.path.join(
            output_directory,
            item['destination'],
        )

        ensure_directory(full_destination)
        print(full_destination)
        with open(full_destination, 'bw+') as fo:
            fo.write(item['bytes'])


def ensure_directory(path):
    """Ensure that a directort exists, to make writing easier."""
    destination_folder = os.path.dirname(path)
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
