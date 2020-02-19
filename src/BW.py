# -*- coding: utf-8 -*-

"""
The main file for the black and white card edition

Coded by Skengrek
"""

import os
import sys

from math import floor

# ! PIL imports
from PIL import Image, ImageQt
from PIL.ImageDraw import Draw
from PIL.Image import alpha_composite

import resources

from .image import Font, Type
from .logginginit import get_logger
from .text import add_ability, add_capacity, add_description_bw, add_text

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
        self.name = ''
        self.stage = None
        self.evolution = ''
        self.image_stage = None

        self.health = ''
        self.image = None

        self.height = ''
        self.weight = ''

        self.ability = None
        self.attacks = None

        self.space = 0

        self.weakness = None

        self.resistance = []
        self.retreat = 1

        self.description = ''

        self.id = ''
        self.set_number = ''
        self.set_maximum = ''

        self.illustrator = ''
        self.generation = 'BW'

    def initialise_blank(self):
        """
        Create the base text for the card with the blank card

        Args:
            img_blank (Image.Image): the blank image
        """
        draw = Draw(self.image)

        # ? Weakness
        x = 40
        y = self.y_max - 86
        font = self.font.weakness_str
        color = self.type.color
        add_text(draw, x, y, 'weakness', font, color)
        font = self.font.weakness
        add_text(draw, 67, self.y_max - 75, 'x2', font, color)

        # ? Resistance
        x = 111
        y = self.y_max - 86
        font = self.font.weakness_str
        color = self.type.color
        add_text(draw, x, y, 'resistance', font, color)

        # ? Retreat
        x = 36
        y = self.y_max - 44
        font = self.font.weakness
        color = self.type.color
        add_text(draw, x, y, 'resistance', font, color)

    def set_background(self):
        # ? background
        size_x = self.x_max - 15
        size_y = self.y_max - 15
        background = Image.open(self.type.path_background)

        img = background.resize((size_x, size_y), Image.LANCZOS)

        background = Image.new("RGBA", self.image.size, (0, 0, 0, 0))
        background.paste(img, (6, 6))

        self.image = alpha_composite(background, self.image)

    def update_by_dict(self, _dict):
        """
        Update Text or image if needed
        check for each key if a value is different and update text or image
        Args:
            _dict (dict): a dict with all the parameter of an image in it
        """
        if self.name != _dict['name']:
            self.name = ''
        self.stage = None
        self.evolution = ''
        self.image_stage = None

        self.health = ''
        self.image = None

        self.height = ''
        self.weight = ''

        self.ability = None
        self.attacks = None

        self.space = 0

        self.weakness = None

        self.resistance = []
        self.retreat = 1

        self.description = ''

        self.id = ''
        self.set_number = ''
        self.set_maximum = ''

        self.illustrator = ''
        self.generation = 'BW'


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

        # ? Information under visual
        font = self.font.info
        _id = self.data['id']
        if len(_id) == 1:
            _id = '00' + _id
        elif len(_id) == 1:
            _id = '0' + _id
        str_info = 'NO. ' + _id + ' ' + self.type.type + ' Pokemon '
        str_info += 'HT ' + self.data['height'] + ' WT ' + self.data['weight']

        size_str = font.getsize(str_info)[0]
        x_info = floor(self.x_max / 2 - size_str / 2)
        y_info = floor(self.y_max / 2) + 1
        add_text(draw, x_info, y_info, str_info, font, color)

        # ? Write ability and capacity
        self.write_ability_capacity()

        # ? Write resistance numbers
        resist = self.data['resistance']
        font = self.font.weakness
        if resist:
            if resist[0] is not None and resist[1] is not None:
                add_text(draw, 135, self.y_max - 75, resist[1], font, color)

        # ? Illustration info
        font = self.font.illustrator
        tmp_set_numb = self.data['set_number'] + '/' + self.data[
            'set_maximum']
        x = self.x_max - 70
        y = self.y_max - 33
        add_text(draw, x, y, tmp_set_numb, font, color)
        tmp_illustrator = 'illus. ' + self.data['illustrator']

        _txt = tmp_illustrator
        tmp_size = font.getsize(tmp_illustrator)[0]
        x = self.x_max - 70 - tmp_size - 50
        y = self.y_max - 33
        add_text(draw, x, y, tmp_illustrator, font, color)

    def write_ability_capacity(self):
        """
        """

        pos = 330

        if self.data['ability'] is not None:
            font_title = self.font.ability_name
            font_text = self.font.ability_text

            tmp_img, pos = \
                add_ability(self.data['ability'], self.image, pos,
                            font_text, font_title, self.x_max - 80,
                            self.type.color)

        if self.data['attacks'] is not None:
            tmp_img, pos = \
                add_capacity(self.data['attacks'], self.image, pos,
                             self.x_max, self.font, self.x_max - 80,
                             self.type.color, self.data['space'])

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
        'attacks': None,
        'space': 10,
        'weakness': None,
        'resistance': ['fire', '-20'],
        'retreat': 1,
        'description': '',
        'id': '10',
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
