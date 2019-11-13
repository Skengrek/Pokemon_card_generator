"""
    All the function for the manipulation and creation of pokemon card
"""
from os import sep

from PIL import Image
from ImageFont import truetype
from ImageDraw import Draw

from math import floor


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
    x_max, y_max = tmp_img.size

    # * Add text
    # ?  define fonts

    path_font_folder = 'resources' + sep + 'fonts' + sep

    path_font_name = path_font_folder + 'GillSansStd-Bold.otf'
    font_name = truetype(path_font_name, 25)
    font_hp_str = truetype(path_font_name, 11)

    path_font_hp = path_font_folder + 'FuturaStd-CondensedBold.otf'
    font_hp_nbr = truetype(path_font_hp, 25)

    path_info = path_font_folder + 'GillSansStd.otf'
    font_info = truetype(path_info, 9)

    path_ability_name = path_font_folder + 'GillSansStd-BoldCondensed.otf'
    font_ability_name = truetype(path_ability_name, 24)

    path_ability_text = path_font_folder + 'GillSansStd.otf'
    font_ability_text = truetype(path_ability_text, 16)

    path_dmg = path_font_folder + 'FuturaStd-Bold.otf'
    font_dmg = truetype(path_dmg, 21)

    # ? Define colors
    black = (0, 0, 0)
    red = (194, 54, 0)

    tmp_draw = Draw(tmp_img)
    # ? Name
    tmp_draw.text((100, 31), data_dict['name'], font=font_name, fill=black)

    # ? Health point text
    tmp_draw.text((x_max - 110, 44), 'HP', font=font_hp_str, fill=black)
    # ? Health point numbers
    tmp_draw.text((x_max - 95, 31), data_dict['health'], font=font_hp_nbr,
                  fill=black)

    # ? Information under visual
    set_nb = data_dict['set_number']
    if len(set_nb) == 2:
        set_nb = 'O' + set_nb
    str_info = 'NO. ' + set_nb + ' ' + img_type + ' Pokemon '
    str_info += 'HT ' + data_dict['height'] + ' WT ' + data_dict['weight']

    size_str = font_info.getsize(str_info)[0]
    x_info = floor(x_max / 2 - size_str / 2)
    y_info = floor(y_max / 2)
    tmp_draw.text((x_info, y_info), str_info, font=font_info, fill=black)

    # ? ability and capacity
    abilities = data_dict['ability']
    tmp_y = add_ability_text(abilities, tmp_draw, 330, font_ability_text,
                             font_ability_name, x_max - 80, red, black)

    capacities = data_dict['attack']
    tmp_y = add_capacity_text(capacities, tmp_draw, tmp_y, x_max,
                              font_ability_text, font_ability_name, font_dmg,
                              x_max - 80, black, black)

    # * Show the image
    tmp_img.show()


def add_ability_text(abilities, img, pos, font_text, font_name,
                     size_justified, name_color, text_color):
    tmp_pos_y = pos
    for ability in abilities:

        # TODO need to add ability image

        ability_name = ability['name']
        img.text((135, tmp_pos_y), ability_name,
                 font=font_name, fill=name_color)

        tmp_pos_y += 25
        tmp_str = ability['text']
        text, height = wrap_text(tmp_str, font_text, size_justified)
        for element in text:
            tmp_el = justified_text(element, font_text, size_justified)
            img.text((40, tmp_pos_y), tmp_el, font=font_text, fill=text_color)
            tmp_pos_y += height + 5

    return tmp_pos_y


def add_capacity_text(capacities, img, pos, x_max, font_text, font_name,
                      font_damage, size_justified, name_color, text_color ):

    tmp_pos_y = pos
    for capacity in capacities:

        # TODO need to add capacity energy image

        ability_name = capacity['name']
        img.text((40, tmp_pos_y), ability_name,
                 font=font_name, fill=name_color)

        ability_dmg = capacity['damage']
        tmp_size = font_damage.getsize(ability_dmg)[0]
        img.text((x_max - 40 - tmp_size, tmp_pos_y), ability_dmg,
                 font=font_name, fill=name_color)

        tmp_pos_y += 25
        tmp_str = capacity['text']
        text, height = wrap_text(tmp_str, font_text, size_justified)
        for element in text:
            tmp_el = justified_text(element, font_text, size_justified)
            img.text((40, tmp_pos_y), tmp_el, font=font_text, fill=text_color)
            tmp_pos_y += height + 5

    return tmp_pos_y


def wrap_text(text, font, size):
    """Wraps text with a special font into a box."""
    word_list = text.split(' ')
    lines = []
    tmp_line = ''
    for element in word_list:

        size_text = font.getsize(tmp_line)[0]
        size_word = font.getsize(element)[0]

        if size_text + size_word < size:
            if tmp_line != '':
                tmp_line += ' '
            tmp_line += element
        else:
            lines.append(tmp_line)
            tmp_line = ''
    if tmp_line != '':
        lines.append(tmp_line)
    height = font.getsize(tmp_line)[1]

    return [lines, height]


def justified_text(text, font, size):
    """The function to justified a text for a certain size."""

    # ? search all spaces
    i = 0
    indexs = get_spaces_index(text)

    # ? add space to fill the
    tmp_ind = 0
    ind_max = len(indexs)
    space_size = font.getsize(' ')[0]
    diff = size - font.getsize(text)[0]
    if diff < size / 3:
        while diff > space_size:
            text = text[:indexs[tmp_ind]] + ' ' + text[indexs[tmp_ind]:]
            tmp_ind += 1
            if tmp_ind == ind_max:
                tmp_ind = 0
            diff = size - font.getsize(text)[0]
            indexs = get_spaces_index(text)
    return text


def get_spaces_index(text):
    """
        Get where the spaces are, account the spaces grouped as one
    """
    index_list = []
    i = 0
    last_letter = ''
    for letter in text:
        if letter == ' ' and last_letter != ' ':
            index_list.append(i)
        last_letter = letter
        i += 1
    return index_list
