# coding: utf-8

"""
The data structure of a card.
"""

# ! ##########################################################################
# ! Imports
# ! ##########################################################################


import os
import sys

from PIL import Image
from PIL.ImageFont import truetype

import resources
from .logginginit import get_logger

# * Logger
# * ##########################################################################

logger = get_logger(__name__)


# ! ##########################################################################
# ! Class
# ! ##########################################################################


# * Data
# * ##########################################################################

class Data(object):

    def __init__(self):

        # ? Flag contains the data changed that are not updated in the card
        self.flags = []

        self.__name = None
        self.__stage = None
        self.__type = ''
        self.__background = ''
        self.__evolution = ''
        self.__evolution_image = ''
        self.__health = 240
        self.__image = ''
        self.__height = ""
        self.__weight = ""
        self.__ability = None
        self.__attacks = None
        self.__space = 10
        self.__weakness = None
        self.__resistance = []
        self.__retreat = 1
        self.__description = ''
        self.__id = 10
        self.__set_number = 1
        self.__set_maximum = 10
        self.__illustrator = ''
        self.__generation = ''

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value != self.__name:
            assert isinstance(value, str)
            self.__name = value
            self.flags.append('name')

    @property
    def stage(self):
        return self.__stage

    @stage.setter
    def stage(self, value):
        if value is not None and value != self.__stage:
            assert isinstance(value, str)
            self.__stage = value
            self.flags.append('stage')

    @property
    def card_type(self):
        return self.__type

    @card_type.setter
    def card_type(self, value):
        if value != self.__type:
            assert isinstance(value, str)
            self.__type = value
            self.flags.append('type')

    @property
    def background(self):
        return self.__background

    @background.setter
    def background(self, value):
        if value != self.__background:
            assert isinstance(value, str)
            self.__background = value
            self.flags.append('background')

    @property
    def evolution(self):
        return self.__evolution

    @evolution.setter
    def evolution(self, value):
        if value != self.__evolution:
            assert isinstance(value, str)
            self.__evolution = value
            self.flags.append('evolution')

    @property
    def evolution_image(self):
        return self.__evolution_image

    @evolution_image.setter
    def evolution_image(self, value):
        if value != self.__evolution_image:
            assert isinstance(value, str)
            self.__evolution_image = value
            self.flags.append('evolution_image')

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value != self.__health:
            assert isinstance(value, str)
            self.__health = value
            self.flags.append('health')

    @property
    def image(self):
        return self.__image

    @image.setter
    def image(self, value):
        if value != self.__image:
            assert isinstance(value, str)
            self.__image = value
            self.flags.append('image')

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if value != self.__height:
            assert isinstance(value, str)
            self.__height = value
            self.flags.append('height')

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if value!= self.__weight:
            assert isinstance(value, str)
            self.__weight = value
            self.flags.append('weight')

    @property
    def ability(self):
        return self.__ability

    @ability.setter
    def ability(self, value):
        if value is not None and value != self.__ability:
            assert isinstance(value, Ability)
            self.__ability = value
            self.flags.append('ability')

    @property
    def attacks(self):
        return self.__attacks

    @attacks.setter
    def attacks(self, value):
        if value is not None:
            assert isinstance(value, list)
            for element in value:
                assert isinstance(element, Attack)
            self.__attacks = value
            self.flags.append('attacks')

    @property
    def space(self):
        return self.__space

    @space.setter
    def space(self, value):
        if value != self.__space:
            assert isinstance(value, int)
            self.__space = value
            self.flags.append('space')

    @property
    def weakness(self):
        return self.__weakness

    @weakness.setter
    def weakness(self, value):
        if value is not None and value != self.weakness:
            assert isinstance(value, str)
            self.__weakness = value
            self.flags.append('weakness')

    @property
    def resistance(self):
        return self.__resistance

    @resistance.setter
    def resistance(self, value):
        if value != self.__resistance:
            assert isinstance(value, list)
            for element in value:
                assert isinstance(element, str)
            self.__resistance = value
            self.flags.append('resistance')

    @property
    def retreat(self):
        return self.__retreat

    @retreat.setter
    def retreat(self, value):
        if value != self.__retreat:
            assert isinstance(value, int)
            self.__retreat = value
            self.flags.append('retreat')

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        if value != self.__description:
            assert isinstance(value, str)
            self.__description = value
            self.flags.append('description')

    @property
    def id_card(self):
        return self.__id

    @id_card.setter
    def id_card(self, value):
        if value != self.__id:
            assert isinstance(value, str)
            self.__id = value
            self.flags.append('id')

    @property
    def set_number(self):
        return self.__set_number

    @set_number.setter
    def set_number(self, value):
        if value != self.__set_number:
            assert isinstance(value, str)
            self.__set_number = value
            self.flags.append('set_number')

    @property
    def set_maximum(self):
        return self.__set_maximum

    @set_maximum.setter
    def set_maximum(self, value):
        if value != self.__set_maximum:
            assert isinstance(value, str)
            self.__set_maximum = value
            self.flags.append('set_maximum')

    @property
    def illustrator(self):
        return self.__illustrator

    @illustrator.setter
    def illustrator(self, value):
        if value != self.__illustrator:
            assert isinstance(value, str)
            self.__illustrator = value
            self.flags.append('illustrator')

    @property
    def generation(self):
        return self.__generation

    @generation.setter
    def generation(self, value):
        if value != self.__generation:
            assert isinstance(value, str)
            self.__generation = value
            self.flags.append('generation')

    def update_by_dict(self, _dict):
        """
        Update Text or image if needed
        check for each key if a value is different and update text or image
        Args:
            _dict (dict): a dict with all the parameter of an image in it
        """
        self.name = _dict['name']
        self.health = _dict['health']
        self.card_type = _dict['type']
        self.stage = _dict['stage']
        self.evolution = _dict['evolution']
        self.image = _dict['image']
        self.evolution_image = _dict['evolution_image']
        self.height = _dict['height']
        self.weight = _dict['weight']
        self.ability = _dict['ability']
        self.attacks = _dict['attacks']
        self.space = _dict['space']
        self.weakness = _dict['weakness']
        self.resistance = _dict['resistance']
        self.retreat = _dict['retreat']
        self.description = _dict['description']
        self.id_card = _dict['id']
        self.set_number = _dict['set_number']
        self.set_maximum = _dict['set_maximum']
        self.illustrator = _dict['illustrator']
        self.generation = _dict['generation']
        self.card_type = _dict['type']


# * Ability
# * ##########################################################################

class Ability(object):

    def __init__(self, name, text):

        self.name = name
        self.text = text

# * Attack
# * ##########################################################################


class Attack(object):

    def __init__(self, name, resources, text, damage):

        self.name = name
        self.resources = resources
        self.text = text
        self.damage = damage


class Type(object):
    """
    Define a name of a pokemon card
    """

    def __init__(self, _type):
        """
        For a specific name, define icons, available background and color
        needed for the text

        Args:
            _type (str): the name of the name
        """

        self.name = _type

        # ? Colors
        # ? ##################################################################

        icons_path = os.path.join(resources.path(), 'icons')
        icon_path = os.path.join(icons_path, self.name + '.png')
        self.icon = Image.open(icon_path)
        icon_path_s = os.path.join(icons_path, self.name + '_small.png')
        self.icon_small = Image.open(icon_path_s)

        # ? Background
        # ? ##################################################################

        back_folder = os.path.join(resources.path(), 'background')
        file_list = os.listdir(back_folder)
        list_available_background = []
        for element in file_list:
            if _type.lower() in element:
                list_available_background.append(element[:-4])

        self.available_background = list_available_background
        self.background = self.available_background[0]
        self.color = None
        self.set_background(self.background)

        # ? Text
        # ? ##################################################################

    @property
    def path_background(self):
        return os.path.join(resources.path(), 'background',
                            self.background + '.png')

    def set_color(self):
        """
        Set the color in function of the background of this name
        """

        font_color = (0, 0, 0)
        ability = (194, 54, 0)
        if self.name in ['dark', 'dragon', 'metal']:
            font_color = (255, 255, 255)

        if self.background in ['metal_modern']:
            font_color = (0, 0, 0)
        border_color = None
        self.color = Color(font_color, ability, border_color)

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
            logger.error("This background does not exist for this name")
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

    def __init__(self, text, ability, border=None):
        """
        Defines the color used by the card.

        Args:
            text (tuple): the color for the text
            ability (tuple): the color for the ability
            border (tuple | None): the color for the border
        """
        assert isinstance(text, tuple) and len(text) == 3
        assert isinstance(ability, tuple) and len(text) == 3
        self.text = text
        self.border = border
        self.ability = ability
        logger.info('The color has been created with the following parameter'
                    '{text}, {border}, {ability}'
                    .format(text=self.text, border=self.border,
                            ability=self.ability))

    def __eq__(self, other):
        if isinstance(other, Color):
            if self.text != other.text:
                return False
            elif self.ability != other.ability:
                return False
            elif self.border != other.border:
                return False
            else:
                # ? Color are the same
                return True
        else:
            return False


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
        f_light = os.path.join(font, 'FuturaStd-Light.otf')
        f_med = os.path.join(font, 'FuturaStd-Medium.otf')
        f_heavy = os.path.join(font, 'FuturaStd-Heavy.otf')
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
        self.ability_text = truetype(g_std, 15)
        self.ability_name = truetype(g_bold_cond, 24)
        self.damage = truetype(f_heavy, 19)
        self.weakness_str = truetype(g_bold, 10)
        self.weakness = truetype(g_bold, 15)
        self.illustrator = truetype(f_bold_cond_obl, 11)
        self.copyright = truetype(f_med, 7)
        self.description = truetype(s_bold, 13)
        self.misc_text = truetype(g_bold, 10)
        self.evolve_text = truetype(g_bold, 8)

    def __repr__(self):
        # ! Override print function for name
        _str = '\nthis Font is initialised with :\n'
        _str += str(self.__dict__.keys())
        return _str


# ! ##########################################################################
# ! Main and tester
# ! ##########################################################################


def main():
    # * Start test
    dat = Data()

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
    dat.update_by_dict(data)
    print(dat.flags)


if __name__ == "__main__":
    main()
