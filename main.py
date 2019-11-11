"""
    Pokemon card generator,

    This tool aim to be a generator for pokemon card.

"""


from src.pokemon import Card


def test():
    """Test function"""
    cap1 = {
        'name': 'test',
        'resources': ['fire'],
        'text': 'This is a sample text',
        'damage': 20
    }

    cap2 = {
        'name': 'test',
        'resources': ['fire', 'electric', 'water'],
        'text': 'Capacity 2 try',
        'damage': 100
    }

    ability = {
        'Name': 'Ability 1',
        'text': 'text about the ability'
    }

    pokemon_card_1 = {
        'name': 'Aéromite',
        'stage': 'base',
        'type': 'fire',
        'health': 120,
        'height': 100,
        'weight': 20,
        'ability': ability,
        'attack': [cap1, cap2],
        'weakness': ['water'],
        'resistance': ['fighting', -30],
        'retreat': 2,
        'text': 'sample text here about the pokemon',
        'set_number': 12,
        'set_maximum': 30,
        'copyright': '2019 Skengrek'
    }


def main():
    print("Start")


if __name__ == "__main__":
    main()
