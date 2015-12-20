"""Helpers."""
import io


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
    b = io.BytesIO()
    image.save(b, encoder)
    return b
