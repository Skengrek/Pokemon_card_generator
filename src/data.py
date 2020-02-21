# coding: utf-8

"""
The data structure of a card.
"""

# ! ##########################################################################
# ! Imports
# ! ##########################################################################


import sys

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
        self.flag = []

        self.__name = None
        self.__stage = None,
        self.__type = '',
        self.__background = '',
        self.__evolution = '',
        self.__evolution_image = '',
        self.__health = 240,
        self.__image = '',
        self.__height = "",
        self.__weight = "",
        self.__ability = None,
        self.__attacks = None,
        self.__space = 10,
        self.__weakness = None,
        self.__resistance = [],
        self.__retreat = 1,
        self.__description = '',
        self.__id = 10,
        self.__set_number = 1,
        self.__set_maximum = 10,
        self.__illustrator = '',
        self.__generation = ''

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        assert isinstance(value, str)
        self.__name = value
        self.flag.append('name')

    @property
    def stage(self):
        return self.stage

    @stage.setter
    def stage(self, value):
        assert isinstance(value, str)
        self.__stage = value
        self.flag.append('stage')

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        assert isinstance(value, str)
        self.__type = value
        self.flag.append('type')

    @property
    def background(self):
        return self.__background

    @background.setter
    def background(self, value):
        assert isinstance(value, str)
        self.__background = value
        self.flag.append('background')

    @property
    def evolution(self):
        return self.__evolution

    @evolution.setter
    def evolution(self, value):
        assert isinstance(value, str)
        self.__evolution = value
        self.flag.append('evolution')

    @property
    def evolution_image(self):
        return self.__evolution_image

    @evolution_image.setter
    def evolution_image(self, value):
        assert isinstance(value, str)
        self.__evolution_image = value
        self.flag.append('evolution_image')

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        assert isinstance(value, str)
        self.__health = value
        self.flag.append('health')

    @property
    def image(self):
        return self.__image

    @image.setter
    def image(self, value):
        assert isinstance(value, str)
        self.__image = value
        self.flag.append('image')

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        assert isinstance(value, str)
        self.__height = value
        self.flag.append('height')

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        assert isinstance(value, str)
        self.__weight = value
        self.flag.append('weight')

    @property
    def ability(self):
        return self.__ability

    @ability.setter
    def ability(self, value):
        assert isinstance(value, Ability)
        self.__ability = value
        self.flag.append('ability')

    @property
    def attacks(self):
        return self.__attacks

    @attacks.setter
    def attacks(self, value):
        assert isinstance(value, list)
        for element in value:
            assert isinstance(element, Attack)
        self.__attacks = value
        self.flag.append('attacks')

    @property
    def space(self):
        return self.__space

    @space.setter
    def space(self, value):
        assert isinstance(value, int)
        self.__space = value
        self.flag.append('space')

    @property
    def weakness(self):
        return self.__weakness

    @weakness.setter
    def weakness(self, value):
        assert isinstance(value, str)
        self.__weakness = value
        self.flag.append('weakness')

    @property
    def resistance(self):
        return self.__resistance

    @resistance.setter
    def resistance(self, value):
        assert isinstance(value, list)
        for element in value:
            assert isinstance(element, str)
        self.__resistance = value
        self.flag.append('resistance')

    @property
    def retreat(self):
        return self.__retreat

    @retreat.setter
    def retreat(self, value):
        assert isinstance(value, int)
        self.__retreat = value
        self.flag.append('retreat')

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        assert isinstance(value, str)
        self.__retreat = value
        self.flag.append('retreat')

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        assert isinstance(value, str)
        self.__id = value
        self.flag.append('id')

    @property
    def set_number(self):
        return self.__set_number

    @set_number.setter
    def set_number(self, value):
        assert isinstance(value, int)
        self.__set_number = value
        self.flag.append('set_number')

    @property
    def set_maximum(self):
        return self.__maximum

    @set_maximum.setter
    def set_maximum(self, value):
        assert isinstance(value, int)
        self.__set_maximum = value
        self.flag.append('set_maximum')

    @property
    def illustrator(self):
        return self.__illustrator

    @illustrator.setter
    def illustrator(self, value):
        assert isinstance(value, str)
        self.__illustrator = value
        self.flag.append('illustrator')

    @property
    def generation(self):
        return self.__generation

    @generation.setter
    def generation(self, value):
        assert isinstance(value, str)
        self.__generation = value
        self.flag.append('generation')

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

        if self.type != _dict['type']:
            self.type = _dict['type']

        if self.stage != _dict['stage']:
            self.stage = _dict['stage']

        if self.evolution != _dict['evolution']:
            self.evolution = _dict['evolution']

        if self.image != _dict['image']:
            self.image = _dict['image']

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


# * Ability
# * ##########################################################################


class Ability(object):

    def __init__(self):
        pass


# * Attack
# * ##########################################################################


class Attack(object):

    def __init__(self):
        pass


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
    pass


if __name__ == "__main__":
    main()
