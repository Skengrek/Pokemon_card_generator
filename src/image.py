"""
    All the function for the manipulation and creation of pokemon card
"""
from src.BW_old import bw


def from_dict(data_dict):
    if data_dict['generation'] == 'BW':
        bw(data_dict)
    else:
        print('It is not possible to generate card for this generation')
