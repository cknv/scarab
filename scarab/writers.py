"""Writers module."""
import os


def bytes_writer(pages, output_directory):
    """Write items to directory."""
    for page in pages:
        prefixed_path = os.path.join(
            output_directory,
            page.path,
        )

        ensure_directory(prefixed_path)
        print(prefixed_path)
        with open(prefixed_path, 'bw+') as fo:
            fo.write(page.bytes)


def ensure_directory(path):
    """Ensure that a directort exists, to make writing easier."""
    destination_folder = os.path.dirname(path)
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
