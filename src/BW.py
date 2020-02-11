# -*- coding: utf-8 -*-

"""
The main file for the black and white card edition

Coded by Skengrek
"""

import os

# ! PIL imports
from PIL import Image, ImageQt
from PIL.ImageDraw import Draw
from PIL.Image import alpha_composite

import resources

from .image import Font, Type
from .logginginit import get_logger

# * Logger
# * ##########################################################################
logger = get_logger(__name__)


# ! Class
# ! ##########################################################################


class BW(object):
    """
        This class has for main goal to create and manipulate a
        pokemon Bw card
    """

    def __init__(self, _type):
        """

        """

        # * Get the fonts and type for the images
        # * ##################################################################

        self.font = Font()
        logger.debug(self.font)
        self.type = Type(_type)
        logger.debug(self.type)

        # * Initialise basic part
        # * ##################################################################

        self.image = None
        self.text = None

        bc_path = os.path.join(resources.path(), 'BW', 'blank.png')
        blank_card = Image.open(bc_path)

        self.x_max, self.y_max = blank_card.size

        self.initialise_blank(blank_card)

    def initialise_blank(self, img_blank):
        """
        Create the base text for the card with the blank card
        Returns:
        """
        pass

    def type_modification(self, _type):
        """
        If needed change the color of the text for the card

        Args:
            _type (str): the type of the card

        Returns:
        """
        self.type = Type(_type)


# ! Main and tester
# ! ##########################################################################


def main():
    img = BW('dragon')

if __name__ == "__main__":
    main()
