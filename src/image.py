"""
    All the function for the manipulation and creation of pokemon card
"""

import os
from .logginginit import get_logger

from PIL import Image
from PIL.ImageFont import truetype

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
        icon_path = os.path.join(icons_path, self.type + '.png')
        self.icon = Image.open(icon_path)
        icon_path_s = os.path.join(icons_path, self.type + '_small.png')
        self.icon_small = Image.open(icon_path_s)

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

    # * repr
    # * ######################################################################

    def __repr__(self):
        _str = '\nType with the following parameters:\n'
        _str += '\tIcons:\n'
        _str += '\t\tinfo:' + str(self.icon.info) + '\n'
        _str += '\t\tsize:' + str(self.icon.size) + '\n'
        _str += '\tIcons_small:\n'
        _str += '\t\tinfo:' + str(self.icon_small.info) + '\n'
        _str += '\t\tsize:' + str(self.icon_small.size) + '\n'
        _str += '\tAvailable background:\n'
        _str += '\t\t' + str(self.available_background) + '\n'
        return str(_str)


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
        logger.info('The color has been created with the following parameter'
                    '{text}, {border}, {ability}'
                    .format(text=self.text, border=self.border,
                            ability=self.ability))


class Font(object):
    """
    This class contains all font used in the images ready to be used by PIL
    """

    def __init__(self):
        """
        Initialise the fonts for the black and white generation card
        """

        font = os.path.join(resources.path(), 'fonts')
        font = os.path.normpath(font)

        # * Font Path
        # * ##################################################################

        # ? gill based font
        g_std = os.path.join(font, 'GillSansStd.otf')
        g_bold = os.path.join(font, 'GillSansStd-Bold.otf')
        g_bold_cond = os.path.join(font, 'GillSansStd-BoldCondensed.otf')

        # ? futura based font
        f_med = os.path.join(font, 'FuturaStd-Medium.otf')
        f_bold = os.path.join(font, 'FuturaStd-Bold.otf')
        f_cond_bold = os.path.join(font, 'FuturaStd-CondensedBold.otf')
        f_bold_cond_obl = os.path.join(font, 'FuturaStd-CondensedBoldObl.otf')

        # ? SanvitoPro based font
        s_bold = os.path.join(font, 'SanvitoPro-Bold.otf')

        # * Font definition for PIL
        # * ##################################################################

        self.name = truetype(g_bold, 23)
        self.hp_str = truetype(g_bold, 11)
        self.hp_nbr = truetype(f_cond_bold, 11)
        self.info = truetype(g_std, 9)
        self.ability_name = truetype(g_bold_cond, 9)
        self.ability_text = truetype(g_std, 16)
        self.damage = truetype(f_bold, 16)
        self.weakness = truetype(g_bold, 15)
        self.illustrator = truetype(f_bold_cond_obl, 11)
        self.copyright = truetype(f_med, 7)
        self.description = truetype(s_bold, 13)
        self.misc_text = truetype(g_bold, 10)

    def __repr__(self):
        # ! Override print function for type
        _str = '\nthis Font is initialised with :\n'
        _str += str(self.__dict__.keys())
        return _str




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