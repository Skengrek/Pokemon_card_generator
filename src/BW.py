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

# ! Class
# ! ###########################################################################


class BW(object):
    """
        This class has for main goal to create and manipulate a
        pokemon Bw card
    """

    def __init__(self):
        """

        """

        # * Get the fonts for the images
        # * ###################################################################
        self.font = Font()


class Font(object):
    """
    This class contains all font used in the images ready to be used by PIL
    """

    def __init__(self):
        
        f_dir = os.path.dirname(__file__)
        font = os.path.join(f_dir, '..', 'resources', 'fonts')
        font = os.path.normpath(font)

        # * Font Path
        # * ###################################################################

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
        # * ###################################################################

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
# ! ###########################################################################


def main():
    img = BW()


if __name__ == "__main__":
    main()
