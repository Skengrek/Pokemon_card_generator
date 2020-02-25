"""
__init__.py for the ressource folder.
"""

import os
from PIL import Image


# * Path
# * ##########################################################################


def path():
    return os.path.dirname(__file__)


# * Get icons
# * ##########################################################################


def get_icons(icon_name):
    """
    returns the PIL Image of the icon
    Args:
        icon_name (str): the name of the icon

    Returns:
        (PIL.Image): the icon PIL image
    """
    _path = os.path.join(path(), 'icons', icon_name.lower() + '.png')

    return Image.open(_path)
