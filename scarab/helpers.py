"""Helpers."""
import io
import hashlib
import base64


def determine_encoder(extension):
    """PIL helper for getting the correct encoder by file extension."""
    options = {
        'jpg': 'jpeg',
        'jpeg': 'jpeg',
        'png': 'png',
    }

    return options[extension.lower()]


def image_to_bytes(image, encoder):
    """Convert a PIL image to a sequence of bytes."""
    fake_file = io.BytesIO()
    image.save(fake_file, encoder)
    return fake_file.getvalue()


def subresource_integrity(bytes_value, algorithm):
    """Generate the subresource integrity for a given bytes value.

    Options for algorithm are: sha256, sha384, and sha512.

    Arguments:
        bytes_value: ``bytes``
        algorithm: ``str``

    Returns:
        ``str``, the subresource integrity for the bytes.
    """
    algorithms = {
        'sha256': hashlib.sha256,
        'sha384': hashlib.sha384,
        'sha512': hashlib.sha512,
    }

    hash_function = algorithms[algorithm]
    digest = hash_function(bytes_value).digest()
    integrity = base64.b64encode(digest).decode('ascii')
    return '{algorithm}-{integrity}'.format(
        algorithm=algorithm,
        integrity=integrity,
    )
