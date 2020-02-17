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

        self.illustration = None

        # * Set the default text of a card
        # * ##################################################################
        self.data = {
            'name': '',
            'stage': None,
            'evolution': '',
            'type': 'basic',
            'background': 'colorless',
            'health': '',
            'image': None,
            'image_stage': None,
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

    def set_background(self):
        # ? background
        size_x = self.x_max - 15
        size_y = self.y_max - 15
        background = Image.open(self.type.path_background)

        img = background.resize((size_x, size_y), Image.LANCZOS)

        background = Image.new("RGBA", self.image.size, (0, 0, 0, 0))
        background.paste(img, (6, 6))

        self.image = alpha_composite(background, self.image)

    def update(self, _dict):
        """
        Update Text or image if needed
        check for each key if a value is different and update text or image
        Args:
            _dict (dict): a dict with all the parameter of an image in it
        """
        changed_values_keys = \
            [key for key, value in _dict.items() if value != self.data[key]]
        print(changed_values_keys)
        self.data = _dict

        if 'image' in changed_values_keys:
            logger.info('Changing image with {}'.format(_dict['image']))
            changed_values_keys.pop(changed_values_keys.index('image'))
            self.set_illustration(_dict['image'])

        if 'type' in changed_values_keys:
            logger.info('Changing type to {}'.format(_dict['type']))
            changed_values_keys.pop(changed_values_keys.index('type'))
            old_type = self.type
            self.type = _dict['type']
            if self.type.color != old_type.color:
                self.write_text()

        if 'background' in changed_values_keys:
            logger.info(
                'Changing background to {}'.format(_dict['background']))
            changed_values_keys.pop(changed_values_keys.index('background'))

        text_set = {'name', 'health', 'height', 'weight', 'description',
                    'set_number', 'set_maximum', 'illustrator'}
        if text_set & set(changed_values_keys):
            logger.info('Write text')
            self.write_text()

        ability_set = {'ability', 'attack'}
        if ability_set & set(changed_values_keys):
            logger.info('Write ability and attacks')

        # ? Where the energy are copy / paste
        energy_set = {'type', 'weakness', 'resistance'}
        if energy_set & set(changed_values_keys):
            logger.ingo('Add energy and type to the image')

    def write_text(self):
        """
        Write the text of a card
        """
        # * Basic for drawing text :
        draw = Draw(self.image)
        color = self.type.color

        # ? Write name
        font = self.font.name
        add_text(draw, 108, 30, self.data['name'], font, color)

        # ? Health point
        tmp_size = self.font.hp_nbr.getsize(self.data['health'])[0] + 55
        font = self.font.name
        add_text(draw, self.x_max - tmp_size, 31, self.data['health'], font,
                 color)

        tmp_size += self.font.hp_str.getsize('HP ')[0]
        font = self.font.hp_str
        add_text(draw, self.x_max - tmp_size, 38, 'HP ', font, color)

    def set_illustration(self, f_path):
        """
        Set the illustration and add it to the image
        """
        img = Image.open(f_path)

        self.illustration = f_path

        size_x = self.x_max - 70
        size_y = 240
        img = img.resize((size_x, size_y), Image.LANCZOS)
        background = Image.new("RGBA", self.image.size, (0, 0, 0, 0))
        background.paste(img, (35, 60))

        self.image = alpha_composite(background, self.image)
        self.set_background()

    def type_modification(self, _type):
        """
        If needed change the color of the text for the card

        Args:
            _type (str): the type of the card

        Returns:
        """
        self.type = Type(_type)

        # ? Change background

    def show(self):
        # ? always add the background last
        self.set_background()
        if hasattr(self.image, 'show'):
            self.image.show()


# ! Main and tester
# ! ##########################################################################


def main():
    # * Start test
    img = BW('dragon')
    img.set_illustration(sys.argv[1])

    # * test update data
    data = {
        'name': 'AA',
        'stage': None,
        'type': 'basic',
        'background': 'colorless',
        'health': '240',
        'image': None,
        'height': "1m20",
        'weight': "40kg",
        'ability': None,
        'attack': None,
        'weakness': None,
        'resistance': [],
        'retreat': 1,
        'description': '',
        'set_number': '1',
        'set_maximum': '10',
        'illustrator': 'Test',
        'generation': 'BW'
    }
    img.update(data)

    # * End of tester
    img.show()


if __name__ == "__main__":
    main()
