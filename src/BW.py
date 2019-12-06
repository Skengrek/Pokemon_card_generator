# -*- coding: utf-8 -*-

from os import sep

from PIL import Image
from PIL.ImageFont import truetype
from PIL.ImageDraw import Draw
from PIL.Image import alpha_composite

from math import floor


def bw(data_dict):
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

    path_weakness = path_font_folder + 'GillSansStd-Bold.otf'
    font_weakness = truetype(path_weakness, 15)

    path_copy = path_font_folder + 'FuturaStd-CondensedBoldObl.otf'
    font_copy = truetype(path_copy, 11)

    path_desc = path_font_folder + 'SanvitoPro-LtCapt.otf'
    font_desc = truetype(path_desc, 14)

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
    pos= 330
    if abilities is not None:
        tmp_img, pos = add_ability(abilities, tmp_img, pos,
                                     font_ability_text, font_ability_name,
                                     x_max - 80, red, black)

    capacities = data_dict['attack']
    tmp_img, pos = add_capacity(capacities, tmp_img, pos, x_max,
                                  font_ability_text, font_ability_name,
                                  font_dmg, x_max - 80, black, black)

    # ? Weakness and resistance
    weakness = data_dict['weakness']

    # ? Paste this image in a transparent background
    foreground = Image.new("RGBA", tmp_img.size, (0, 0, 0, 0))
    tmp_path = 'resources' + sep + 'misc' + sep + weakness + '_small.png'
    weakness_img = Image.open(tmp_path)
    foreground.paste(weakness_img, (35, y_max - 78))

    # ? Merge both image
    tmp_img = alpha_composite(tmp_img, foreground)
    tmp_draw = Draw(tmp_img)

    tmp_draw.text((57, y_max - 75), 'x2', font=font_weakness, fill=black)

    resistance = data_dict['resistance']
    if len(resistance) == 2:
        # ? Paste this image in a transparent background
        foreground = Image.new("RGBA", tmp_img.size, (0, 0, 0, 0))
        tmp_path = 'resources' + sep + 'misc' + sep + resistance[0] + '_small.png'
        weakness_img = Image.open(tmp_path)
        foreground.paste(weakness_img, (110, y_max - 78))

        # ? Merge both image
        tmp_img = alpha_composite(tmp_img, foreground)
        tmp_draw = Draw(tmp_img)

        tmp_draw.text((130, y_max - 75), resistance[1], font=font_weakness,
                      fill=black)

    tmp_illustrator = 'illus. ' + data_dict['illustrator']
    tmp_size = font_copy.getsize(tmp_illustrator)[0]
    tmp_draw.text((floor((3.5 * x_max / 6) - tmp_size / 2), y_max - 33),
                  tmp_illustrator, font=font_copy, fill=black)

    # ? Add Image to the card
    path_photo_folder = 'resources' + sep + 'photo' + sep
    path_image = path_photo_folder + data_dict['image']
    img = Image.open(path_image)

    # ? Define the illustration
    size_x = x_max - 39 - 38 + 1
    size_y = 290 - 64 + 1
    img = img.resize((size_x, size_y), Image.LANCZOS)  # LANCZOS is for quality

    # ? Paste this image in a transparant background
    background = Image.new("RGBA", tmp_img.size, (0, 0, 0, 0))
    background.paste(img, (38, 64))

    # ? Merge both image
    tmp_img = alpha_composite(background, tmp_img)

    # ? add description text
    desc = data_dict['description']
    tmp_img = add_description(desc, tmp_img, font_desc, black, x_max, y_max)

    # * Show the image
    tmp_img.show()


def add_description(desc, img, font, color, x_max, y_max):
    """The text needs to have a size under 535."""
    if font.getsize(desc)[0] <= 535:
        tmp_draw = Draw(img)
        tmp_text, height = wrap_text(desc, font, 140)
        pos_x, pos_y = x_max - 193, y_max - 89
        for element in tmp_text:
            justified_element = justified_text(element, font, 140)
            tmp_draw.text((pos_x, pos_y), justified_element,
                          font=font, fill=color)
            pos_y += height - 3
            pos_x -= 10

        return img
    else:
        print('Text too long. More than 131 char')
        return img


def add_ability(ability, img, pos, font_text, font_name,
                size_justified, name_color, text_color):
    tmp_pos_y = pos

    # ? Paste this image in a transparent background
    foreground = Image.new("RGBA", img.size, (0, 0, 0, 0))
    tmp_path = 'resources' + sep + 'misc' + sep + 'ability.png'
    energy_img = Image.open(tmp_path)
    foreground.paste(energy_img, (30, tmp_pos_y))

    # ? Merge both image
    img = alpha_composite(img, foreground)
    draw = Draw(img)

    ability_name = ability['name']
    draw.text((135, tmp_pos_y), ability_name,
              font=font_name, fill=name_color)

    tmp_pos_y += 25
    tmp_str = ability['text']
    text, height = wrap_text(tmp_str, font_text, size_justified)
    for element in text:
        tmp_el = justified_text(element, font_text, size_justified)
        draw.text((40, tmp_pos_y), tmp_el, font=font_text, fill=text_color)
        tmp_pos_y += height + 5

    return [img, tmp_pos_y]


def add_capacity(capacities, img, pos, x_max, font_text, font_name,
                 font_damage, size_justified, name_color, text_color):
    tmp_pos_y = pos
    for capacity in capacities:
        x_pos = 30
        for energy in capacity['resources']:
            # ? Paste this image in a transparent background
            foreground = Image.new("RGBA", img.size, (0, 0, 0, 0))
            tmp_path = 'resources' + sep + 'misc' + sep + energy + '.png'
            energy_img = Image.open(tmp_path)
            foreground.paste(energy_img, (x_pos, tmp_pos_y))
            x_pos += 25

            # ? Merge both image
            img = alpha_composite(img, foreground)
        draw = Draw(img)

        ability_name = capacity['name']
        draw.text((135, tmp_pos_y), ability_name,
                  font=font_name, fill=name_color)

        ability_dmg = capacity['damage']
        tmp_size = font_damage.getsize(ability_dmg)[0]
        draw.text((x_max - 40 - tmp_size, tmp_pos_y), ability_dmg,
                  font=font_name, fill=name_color)

        tmp_pos_y += 25
        tmp_str = capacity['text']
        text, height = wrap_text(tmp_str, font_text, size_justified)
        for element in text:
            tmp_el = justified_text(element, font_text, size_justified)
            draw.text((40, tmp_pos_y), tmp_el, font=font_text, fill=text_color)
            tmp_pos_y += height + 5

    return [img, tmp_pos_y]


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
            tmp_line = element
    if tmp_line != '':
        lines.append(tmp_line)
    height = font.getsize(text)[1]
    print(font.getsize(text))

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
    if diff < size / 4:
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
