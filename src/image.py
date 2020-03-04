"""
    All the function for the manipulation and creation of pokemon card
"""

import os
from .logginginit import get_logger

from src.BW import BW
from .data import Type, Color

import resources

# * logger
# * ##########################################################################
logger = get_logger(__name__)


# * Functions
# *###########################################################################


def from_dict(data_dict):
    if data_dict['generation'] == 'BW':
        BW(data_dict)
    else:
        print('It is not possible to generate card for this generation')


# ! Main and tester
# ! ##########################################################################


def main():
    # ? test name definition
    test = Type('Dragon')
    try:
        col = Color((1, 2), (2, 3), (3, 4))
    except AssertionError:
        print('Assert for wrong tuple with les than 3 value work')

    col = Color((255, 255, 255), (20, 20, 20), (189, 42, 0))
    print('Text color :', col.text)
    print('Text ability :', col.ability)
    print('Text border :', col.border)

    # ? Test Color __eq__
    # ! TODO test color __eq__


if __name__ == "__main__":
    main()
