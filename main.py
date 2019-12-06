"""
    Pokemon card generator,

    This tool aim to be a generator for pokemon card.

"""


from src.image import from_dict


def test():
    """Test function"""
    cap1 = {
        'name': 'test',
        'resources': ['psy'],
        'text': 'This is a sample text',
        'damage': '20'
    }

    cap2 = {
        'name': 'test 2',
        'resources': ['fire', 'electric', 'water', 'basic'],
        'text': 'Capacity 2 try',
        'damage': '100'
    }

    ability = {
        'name': 'Ability 1',
        'text': 'text about the ability text about the ability text about the ability text about the ability '
    }

    pokemon_card_1 = {
        'name': 'Aéromite',
        'stage': 'stage2',
        'type': 'Fairy',
        'health': '120',
        'image': 'test2.jpg',
        'height': "1'23''",
        'weight': "40",
        'ability': ability,
        'attack': [cap1, cap2],
        'weakness': 'water',
        'resistance': ['fighting', '-30'],
        'retreat': 2,
        'description': 'Sample text here about the pokemon for now it need to be long to test test test test test test test test test test',
        'set_number': '12',
        'set_maximum': '30',
        'illustrator': 'Armand',
        'generation': 'BW'
    }

    from_dict(pokemon_card_1)


def main():
    print("Start")
    test()


if __name__ == "__main__":
    main()
