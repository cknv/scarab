"""Writers module."""
import os


def bytes_writer(pages, output_directory):
    """Write items to directory."""
    for page in pages:
        destination_path = prepend_dir(output_directory, page.path)

        ensure_directory(destination_path)
        print(destination_path)
        with open(destination_path, 'bw+') as fo:
            fo.write(page.bytes)


def ensure_directory(path):
    """Ensure that a directort exists, to make writing easier."""
    destination_folder = os.path.dirname(path)
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)


def prepend_dir(directory, path):
    """Prepend a directory onto a path."""
    return os.path.join(
        directory,
        path,
    )
