"""
    All the function for the manipulation and creation of pokemon card
"""
from os import sep

from PIL import Image
from ImageFont import truetype
from ImageDraw import Draw


def from_dict(data_dict):
    """Generate an image from a dictionary"""

    # * Definition of the path for the base image
    gen = data_dict['generation']
    img_type = data_dict['type']
    stage = data_dict['stage']

    base_path = 'resources' + sep + 'img' \
                + sep + gen \
                + sep + img_type \
                + sep + stage + '.png'

    tmp_img = Image.open(base_path)

    # * Add text
    # ?  define fonts

    path_font_folder = 'resources' + sep + 'fonts' + sep

    path_font_name = path_font_folder + 'GillSansStd-Bold.otf'
    font_name = truetype(path_font_name, 25)
    font_hp_str = truetype(path_font_name, 11)

    path_font_hp = path_font_folder + 'FuturaStd-CondensedBold.otf'
    font_hp_nbr = truetype(path_font_hp, 25)

    # ? Define colors
    black = (0, 0, 0)

    tmp_draw = Draw(tmp_img)
    # ? Name
    tmp_draw.text((100, 31), data_dict['name'], font=font_name, fill=black)

    # ? Health point text
    tmp_draw.text((310, 44), 'HP', font=font_hp_str, fill=black)
    # ? Health point numbers
    tmp_draw.text((325, 31), data_dict['health'], font=font_hp_nbr, fill=black)

    # ? Information under visual
    set_nb = data_dict['set_number']
    if len(set_nb) == 2:
        set_nb = 'O' + set_nb
    str_info = 'NO. ' + set_nb 

    # * Show the image
    tmp_img.show()
