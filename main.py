"""
    Pokemon card generator,

    This tool aim to be a generator for pokemon card.

"""


from src.image import from_dict

from gui import interface


def test():
    """Test function"""
    cap1 = {
        'name': 'test',
        'resources': [],
        'text': 'This is a sample text',
        'damage': '20'
    }

    cap2 = {
        'name': 'test 2',
        'resources': ['fire', 'electric', 'water', 'c'],
        'text': 'Capacity 2 try',
        'damage': '100'
    }

    ability = {
        'name': 'Ability 1',
        'text': 'text about the ability text about the ability text about the ability text about the ability '
    }

    pokemon_card_1 = {
        'name': '',
        'stage': None,
        'type': 'colorless',
        'background': 'colorless',
        'health': '',
        'image': None,
        'height': "",
        'weight': "",
        'ability': None,
        'attack': None,
        'weakness': None,
        'resistance': [],
        'retreat': 1,
        'description': '',
        'set_number': '',
        'set_maximum': '',
        'illustrator': '',
        'generation': 'BW'
    }

    from_dict(pokemon_card_1)


def main():
    interface.main()


if __name__ == "__main__":
    main()
