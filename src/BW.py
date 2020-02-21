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

from .image import Font, Type, Color
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

        # * Get the fonts and name for the images
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
        self.initialise_generic_text()



        # * Set the default text of a card
        # * ##################################################################
        self.name = ''
        self.stage = None
        self.evolution = ''
        self.evolution_image = None

        self.health = ''
        self.illustration = None

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

    def initialise_generic_text(self):
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
            self.name = _dict['name']

        if self.health != _dict['health']:
            self.health = _dict['health']

        # if self.type.name != _dict['type']:
        #     self.update_type(_dict['type'])

        if self.stage != _dict['stage']:
            self.stage = _dict['name']

        if self.evolution != _dict['evolution']:
            self.evolution = _dict['evolution']

        if self.illustration != _dict['image']:
            self.illustration = _dict['image']
            self.set_illustration(_dict['image'])

        if self.evolution_image != _dict['evolution_image']:
            self.evolution_image = _dict['evolution_image']

        if self.height != _dict['height']:
            self.height = _dict['height']

        if self.weight != _dict['weight']:
            self.weight = _dict['weight']

        if self.ability != _dict['ability']:
            self.ability = _dict['ability']

        if self.attacks != _dict['attacks']:
            self.attacks = _dict['attacks']

        if self.space != _dict['space']:
            self.space = _dict['space']

        if self.weakness != _dict['weakness']:
            self.weakness = _dict['weakness']

        if self.resistance != _dict['resistance']:
            self.resistance = _dict['resistance']

        if self.retreat != _dict['retreat']:
            self.retreat = _dict['retreat']

        if self.description != _dict['description']:
            self.description = _dict['description']

        if self.id != _dict['id']:
            self.id = _dict['id']

        if self.set_number != _dict['set_number']:
            self.set_number = _dict['set_number']

        if self.set_maximum != _dict['set_maximum']:
            self.set_maximum = _dict['set_maximum']

        if self.illustrator != _dict['illustrator']:
            self.illustrator = _dict['illustrator']

        if self.generation != _dict['generation']:
            self.generation = _dict['generation']

        self.write_text()

    def write_text(self):
        """
        Write the text of a card
        """
        # * Basic for drawing text :
        draw = Draw(self.image)
        color = self.type.color

        # ? Write name
        font = self.font.name
        add_text(draw, 108, 30, self.name, font, color)

        # ? Health point
        tmp_size = self.font.hp_nbr.getsize(self.health)[0] + 80
        font = self.font.name
        add_text(draw, self.x_max - tmp_size, 31, self.health, font,
                 color)

        tmp_size += self.font.hp_str.getsize('HP ')[0]
        font = self.font.hp_str
        add_text(draw, self.x_max - tmp_size, 38, 'HP ', font, color)

        # ? Information under visual
        font = self.font.info
        _id = self.id
        if len(_id) == 1:
            _id = '00' + _id
        elif len(_id) == 1:
            _id = '0' + _id
        str_info = 'NO. ' + _id + ' ' + self.type.name + ' Pokemon '
        str_info += 'HT ' + self.height + ' WT ' + self.weight

        size_str = font.getsize(str_info)[0]
        x_info = floor(self.x_max / 2 - size_str / 2)
        y_info = floor(self.y_max / 2) + 1
        color_info = Color((0, 0, 0), (0, 0, 0),)
        add_text(draw, x_info, y_info, str_info, font, color_info)

        # ? Write ability and capacity
        self.write_ability_capacity()

        # ? Write resistance numbers
        resist = self.resistance
        font = self.font.weakness
        if resist:
            if resist[0] is not None and resist[1] is not None:
                add_text(draw, 135, self.y_max - 75, resist[1], font, color)

        # ? Illustration info
        font = self.font.illustrator
        tmp_set_numb = self.set_number + '/' + self.set_maximum
        x = self.x_max - 70
        y = self.y_max - 33
        add_text(draw, x, y, tmp_set_numb, font, color)
        tmp_illustrator = 'illus. ' + self.illustrator

        _txt = tmp_illustrator
        tmp_size = font.getsize(tmp_illustrator)[0]
        x = self.x_max - 70 - tmp_size - 50
        y = self.y_max - 33
        add_text(draw, x, y, tmp_illustrator, font, color)

        # ? Description
        add_description_bw(self.description, draw, self.font.description,
                           self.type.color, self.x_max, self.y_max)

    def write_ability_capacity(self):
        """
        """

        pos = 330

        if self.ability is not None:
            font_title = self.font.ability_name
            font_text = self.font.ability_text

            tmp_img, pos = \
                add_ability(self.ability, self.image, pos,
                            font_text, font_title, self.x_max - 80,
                            self.type.color)

        if self.attacks is not None:
            add_capacity(self.attacks, self.image, pos,
                         self.x_max, self.font, self.x_max - 80,
                         self.type.color, self.space)

    def set_illustration(self, f_path):
        """
        Set the illustration and add it to the image
        """
        img = Image.open(f_path)

        self.illustration = f_path

        size_x = self.x_max - 73
        size_y = 230
        img = img.resize((size_x, size_y), Image.LANCZOS)
        foreground = Image.new("RGBA", self.image.size, (0, 0, 0, 0))
        foreground.paste(img, (37, 61))

        self.image = alpha_composite(self.image, foreground)
        self.set_background()

    def update_type(self, _type):
        """
        If needed change the color of the text for the card

        Args:
            _type (str): the name of the card
        """
        bc_path = os.path.join(resources.path(), 'BW', 'blank.png')
        self.image = Image.open(bc_path)

        self.type = Type(_type)

        # ? Change background
        self.set_illustration(self.illustration)

        # ? initialise empty card
        self.initialise_generic_text()

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
        'evolution': '',
        'evolution_image': '',
        'health': '240',
        'image': sys.argv[2],
        'height': "1m20",
        'weight': "40kg",
        'ability': None,
        'attacks': None,
        'space': 10,
        'weakness': None,
        'resistance': ['fire', '-20'],
        'retreat': 1,
        'description': 'LALALALALALALLALA test mon pote',
        'id': '10',
        'set_number': '1',
        'set_maximum': '10',
        'illustrator': 'Test',
        'generation': 'BW'
    }
    img.update_by_dict(data)

    # * End of tester
    img.show()


if __name__ == "__main__":
    main()
