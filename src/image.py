"""
    All the function for the manipulation and creation of pokemon card
"""

import os
from .logginginit import get_logger

from src.BW_old import bw

import resources

# * logger
# * ##########################################################################
logger = get_logger(__name__)


# * Functions
# *###########################################################################


def from_dict(data_dict):
    if data_dict['generation'] == 'BW':
        bw(data_dict)
    else:
        print('It is not possible to generate card for this generation')


# * Class
# * ##########################################################################


class Type(object):
    """
    Define a type of a pokemon card
    """

    def __init__(self, _type):
        """
        For a specific type, define icons, available background and color
        needed for the text

        Args:
            _type (str): the name of the type
        """

        self.type = _type

        # ? Colors
        # ? ##################################################################

        icons_path = os.path.join(resources.path(), 'icons')
        self.icon = os.path.join(icons_path, self.type + '.png')
        self.icon_small = os.path.join(icons_path, self.type+'_small.png')

        # ? Background
        # ? ##################################################################

        back_folder = os.path.join(resources.path(), 'background')
        file_list = os.listdir(back_folder)
        list_available_background = []
        for element in file_list:
            if _type.lower() in element:
                list_available_background.append(element[:-4])
        if _type.lower() == 'basic':
            list_available_background.append('colorless')

        self.available_background = list_available_background
        self.background = None
        self.color = None

        # ? Text
        # ? ##################################################################

    def set_color(self):
        """
        Set the color in function of the background of this type
        """

        font_color = (0, 0, 0)
        ability = (194, 54, 0)
        if self.background in ['dark', 'dragon', 'metal']:
            font_color = (255, 255, 255)

        if self.background in ['metal_modern']:
            font_color = (0, 0, 0)
        border_color = font_color
        return Color(font_color, border_color, ability)

    def set_background(self, background):
        """
        Set the background if it is in the list of available on otherwise
        select the first of the list
        Args:
            background (str): the name of the background
        """
        if background in self.available_background:
            self.background = background
        else:
            logger.error("This background does not exist for this type")
            self.background = self.available_background[0]

        self.set_color()


class Color(object):
    """
    Define colors for images
    """

    def __init__(self, text, border, ability):
        """
        Defines the color used by the card.

        Args:
            text (tuple): the color for the text
            border (tuple): the color for the border
            ability (tuple): the color for the ability
        """
        assert isinstance(text, tuple) and len(text) == 3
        assert isinstance(border, tuple) and len(text) == 3
        assert isinstance(ability, tuple) and len(text) == 3
        self.text = text
        self.border = border
        self.ability = ability
        logger.info('The coloe has been created with the following parameter'
                    '{text}, {border}, {ability}'
                    .format(text=self.text, border=self.border,
                            ability=self.ability))


# ! Main and tester
# ! ##########################################################################


def main():

    test = Type('Dragon')
    try:
        col = Color((1, 2), (2, 3), (3, 4))
    except AssertionError:
        print('Assert for wrong tuple with les than 3 value work')

    col = Color((255, 255, 255), (20, 20, 20), (189, 42, 0))
    print('Text color :', col.text)
    print('Text ability :', col.ability)
    print('Text border :', col.border)


if __name__ == "__main__":
    main()