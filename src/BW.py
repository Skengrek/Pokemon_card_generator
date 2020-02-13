# -*- coding: utf-8 -*-

"""
The main file for the black and white card edition

Coded by Skengrek
"""

import os
import sys

# ! PIL imports
from PIL import Image, ImageQt
from PIL.ImageDraw import Draw
from PIL.Image import alpha_composite

import resources

from .image import add_text, Font, Type
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

        # * Initialise basic image
        # * ##################################################################

        bc_path = os.path.join(resources.path(), 'BW', 'blank.png')
        self.image = Image.open(bc_path)
        self.x_max, self.y_max = self.image.size
        self.initialise_blank()

        # * Set the default text of a card
        # * ##################################################################
        self.text = {
            'name': '',
            'stage': None,
            'type': 'basic',
            'background': 'colorless',
            'health': '',
            'image': None,
            'height': "",
            'weight': "",
            'ability': None,
            'attack': None,
            'weakness': None,
            'resistance': [],
            'retreat': 1,
            'description': '',
            'set_number': '',
            'set_maximum': '',
            'illustrator': '',
            'generation': 'BW'
        }

    def initialise_blank(self):
        """
        Create the base text for the card with the blank card

        Args:
            img_blank (Image.Image): the blank image
        """
        drawing = Draw(self.image)

        # ? Weakness
        x = 36
        y = self.y_max - 86
        font = self.font.weakness
        color = self.type.color
        add_text(drawing, x, y, 'weakness', font, color)

        # ? Resistance
        x = 111
        y = self.y_max - 86
        font = self.font.weakness
        color = self.type.color
        add_text(drawing, x, y, 'resistance', font, color)

        # ? Retreat
        x = 36
        y = self.y_max - 44
        font = self.font.weakness
        color = self.type.color
        add_text(drawing, x, y, 'resistance', font, color)

    def add_background(self):
        # ? background
        size_x = self.x_max - 15
        size_y = self.y_max - 15
        background = Image.open(self.type.path_background)

        img = background.resize((size_x, size_y), Image.LANCZOS)

        background = Image.new("RGBA", self.image.size, (0, 0, 0, 0))
        background.paste(img, (6, 6))

        self.image = alpha_composite(background, self.image)

    def write_text(self):
        """
        Write the text of a card
        """
        pass

    def set_image(self, f_path):
        """
        Returns:
        """
        img = Image.open(f_path)

        size_x = self.x_max - 70
        size_y = 240
        img = img.resize((size_x, size_y), Image.LANCZOS)
        background = Image.new("RGBA", self.image.size, (0, 0, 0, 0))
        background.paste(img, (35, 60))

        self.image = alpha_composite(background, self.image)
        self.add_background()

    def type_modification(self, _type):
        """
        If needed change the color of the text for the card

        Args:
            _type (str): the type of the card

        Returns:
        """
        self.type = Type(_type)

    def show(self):
        if hasattr(self.image, 'show'):
            self.image.show()


# ! Main and tester
# ! ##########################################################################


def main():
    # * Start test
    img = BW('dragon')
    img.set_image(sys.argv[1])

    # * End of tester
    img.show()


if __name__ == "__main__":
    main()
