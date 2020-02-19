# -*- coding: utf-8 -*-

from os import sep, path

from PIL import Image, ImageQt
from PIL.ImageFont import truetype
from PIL.ImageDraw import Draw
from PIL.Image import alpha_composite

from .text import add_ability, add_capacity, add_description_bw

from math import floor


def bw(data_dict):
    """
    Test test
    Args:
        data_dict:

    Returns:

    """
    """Generate an image from a dictionary"""

    # * Definition of the path for the base image
    gen = data_dict['generation']
    img_type = data_dict['type']

    base_path = path.join('resources', gen.lower(), 'blank.png')

    tmp_img = Image.open(base_path)
    x_max, y_max = tmp_img.size

    # * Add text
    # ?  define fonts

    path_font_folder = 'resources' + sep + 'fonts' + sep

    path_font_name = path_font_folder + 'GillSansStd-Bold.otf'
    font_name = truetype(path_font_name, 23)
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

    path_illu = path_font_folder + 'FuturaStd-CondensedBoldObl.otf'
    font_illu = truetype(path_illu, 11)

    path_copy = path_font_folder + 'FuturaStd-Medium.otf'
    font_copy = truetype(path_copy, 7)

    path_desc = path_font_folder + 'SanvitoPro-Bold.otf'
    font_desc = truetype(path_desc, 13)

    path_weak_text = path_font_folder + 'GillSansStd-Bold.otf'
    font_weak_text = truetype(path_weak_text, 10)

    # ? Define colors
    font_color = (0, 0, 0)
    red = (194, 54, 0)

    if data_dict['type'] in ['dark', 'dragon', 'metal']:
        font_color = (255, 255, 255)

    if data_dict['background'] in ['metal_modern']:
        font_color = (0, 0, 0)

    # ? stage
    stage = data_dict['stage']
    if stage == 'basic':
        pos_stage = (8, 12)
    elif stage == 'stage1':
        pos_stage = (10, 10)
    else:
        pos_stage = (10, 8)

    # ? Paste this image in a transparent background
    foreground_stage = Image.new("RGBA", tmp_img.size, (0, 0, 0, 0))
    tmp_path = path.join('resources', 'BW', stage + '.png')
    stage_img = Image.open(tmp_path)
    foreground_stage.paste(stage_img, pos_stage)

    # ? Merge both image
    tmp_img = alpha_composite(tmp_img, foreground_stage)

    tmp_draw = Draw(tmp_img)

    # ? Name
    tmp_draw.text((108, 30), data_dict['name'], font=font_name,
                  fill=font_color)

    # ? Health point numbers
    tmp_size = font_hp_nbr.getsize(data_dict['health'])[0] + 55
    tmp_draw.text((x_max - tmp_size, 31), data_dict['health'],
                  font=font_hp_nbr, fill=font_color)

    # ? Health point text
    tmp_size += font_hp_str.getsize('HP ')[0]
    tmp_draw.text((x_max - tmp_size, 44), 'HP', font=font_hp_str,
                  fill=font_color)

    # ? Information under visual
    set_nb = data_dict['set_number']
    if len(set_nb) == 2:
        set_nb = 'O' + set_nb
    str_info = 'NO. ' + set_nb + ' ' + img_type + ' Pokemon '
    str_info += 'HT ' + data_dict['height'] + ' WT ' + data_dict['weight']

    size_str = font_info.getsize(str_info)[0]
    x_info = floor(x_max / 2 - size_str / 2)
    y_info = floor(y_max / 2) + 1
    tmp_draw.text((x_info, y_info), str_info, font=font_info, fill=(0, 0, 0))

    # ? ability and capacity
    abilities = data_dict['ability']
    pos = 330
    if abilities is not None:
        tmp_img, pos = add_ability(abilities, tmp_img, pos,
                                   font_ability_text, font_ability_name,
                                   x_max - 80, red, font_color)

    capacities = data_dict['attack']
    if capacities is not None:
        tmp_img, pos = add_capacity(capacities, tmp_img, pos, x_max,
                                    font_ability_text, font_ability_name,
                                    font_dmg, x_max-80, font_color, font_color,
                                    data_dict['space'])

    # ? Weakness and resistance

    weakness = data_dict['weakness']
    if weakness is not None:
        # ? Paste this image in a transparent background
        foreground = Image.new("RGBA", tmp_img.size, (0, 0, 0, 0))
        tmp_path = 'resources' + sep + 'icons' + sep + weakness + '_small.png'
        weakness_img = Image.open(tmp_path)
        foreground.paste(weakness_img, (35, y_max - 78))

        # ? Merge both image
        tmp_img = alpha_composite(tmp_img, foreground)
        tmp_draw = Draw(tmp_img)

        tmp_draw.text((57, y_max - 75), 'x2', font=font_weakness,
                      fill=font_color)
    tmp_draw.text((36, y_max - 86), 'weakness',
                  font=font_weak_text, fill=font_color)

    resistance = data_dict['resistance']

    if resistance:
        if resistance[0] is not None and resistance[1] is not None:
            # ? Paste this image in a transparent background
            foreground = Image.new("RGBA", tmp_img.size, (0, 0, 0, 0))
            tmp_path = 'resources' + sep + 'icons' + sep + resistance[
                0] + '_small.png'
            weakness_img = Image.open(tmp_path)
            foreground.paste(weakness_img, (110, y_max - 78))

            # ? Merge both image
            tmp_img = alpha_composite(tmp_img, foreground)
            tmp_draw = Draw(tmp_img)

            tmp_draw.text((130, y_max - 75), resistance[1], font=font_weakness,
                          fill=font_color)
    tmp_draw.text((111, y_max - 86), 'resistance', font=font_weak_text,
                  fill=font_color)
    tmp_draw.text((37, y_max - 44), 'retreat', font=font_weak_text,
                  fill=font_color)

    tmp_draw.text((23, y_max - 27), data_dict['copyright'], font=font_copy,
                  fill=font_color)

    tmp_illustrator = 'illus. ' + data_dict['illustrator']
    tmp_set_numb = data_dict['set_number'] + '/' + data_dict['set_maximum']
    tmp_txt = tmp_illustrator + '    ' + tmp_set_numb
    tmp_size = font_illu.getsize(tmp_txt)[0]

    tmp_draw.text((floor((4 * x_max / 6) - tmp_size / 2), y_max - 33),
                  tmp_txt, font=font_illu, fill=font_color)

    # ? Add Image to the card
    if data_dict['image'] is not None:
        path_image = data_dict['image']
        img = Image.open(path_image)

        # ? Define the illustration
        size_x = x_max - 70
        size_y = 240
        img = img.resize((size_x, size_y), Image.LANCZOS)  # LANCZOS is for quality

        # ? Paste this image in a transparant background
        background = Image.new("RGBA", tmp_img.size, (0, 0, 0, 0))
        background.paste(img, (35, 60))

        # ? Merge both image
        tmp_img = alpha_composite(background, tmp_img)

    # ? add description text
    desc = data_dict['description']
    tmp_img = add_description_bw(desc, tmp_img, font_desc, font_color,
                                 x_max, y_max)

    # ? Add Background to the card
    if data_dict['background'] != '':
        path_photo_folder = 'resources' + sep + 'background' + sep
        path_image = path_photo_folder + data_dict['background'] + '.png'
        img = Image.open(path_image)

        # ? Define the illustration
        size_x = x_max - 15
        size_y = y_max - 15
        # LANCZOS is for quality
        img = img.resize((size_x, size_y), Image.LANCZOS)

        # ? Paste this image in a transparant background
        background = Image.new("RGBA", tmp_img.size, (0, 0, 0, 0))
        background.paste(img, (6, 6))

        # ? Merge both image
        tmp_img = alpha_composite(background, tmp_img)

    # ? Type Logo
    _type = data_dict['type']

    # ? Paste this image in a transparent background
    foreground = Image.new("RGBA", tmp_img.size, (0, 0, 0, 0))
    tmp_path = 'resources' + sep + 'icons' + sep + _type + '.png'
    weakness_img = Image.open(tmp_path)
    weakness_img = weakness_img.resize((30, 30), Image.LANCZOS)
    foreground.paste(weakness_img, (x_max - 51, 22))

    # ? Merge both image
    tmp_img = alpha_composite(tmp_img, foreground)

    tmp_img = add_retreat_energy(tmp_img, data_dict['retreat'], y_max)

    return_img = ImageQt.ImageQt(tmp_img)
    return return_img


def add_retreat_energy(img, number, y_max):
    """Add X energy to the retreat"""
    x_pos = 85
    for i in range(number):
        # ? Paste this image in a transparent background
        foreground = Image.new("RGBA", img.size, (0, 0, 0, 0))
        tmp_path = 'resources' + sep + 'icons' + sep + 'basic_small.png'
        weakness_img = Image.open(tmp_path)
        foreground.paste(weakness_img, (x_pos, y_max - 48))
        # ? Merge both image
        img = alpha_composite(img, foreground)

        # ? Increment size to shift new energy
        x_pos += 17

    return img
