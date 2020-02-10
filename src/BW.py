# -*- coding: utf-8 -*-

"""
The main file for the black and white card edition

Coded by Skengrek
"""

import os

# ! PIL imports
from PIL import Image, ImageQt
from PIL.ImageFont import truetype
from PIL.ImageDraw import Draw
from PIL.Image import alpha_composite

from .. import resources
from .image import Type
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
        self.type = Type(_type)

        # * Initialise basic part
        # * ##################################################################

        self.image = None
        self.text = None

        bc_path = os.path.join(resources.path(), 'BW', 'blank.png')
        self.blank_card = Image.open(bc_path)

        self.x_max, self.y_max = self.blank_card.size

    def initialise_blank(self):
        """
        Create the base text for the card
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


# ! Main and tester
# ! ##########################################################################


def main():
    img = BW('dragon')


if __name__ == "__main__":
    main()
