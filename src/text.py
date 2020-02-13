# coding: utf-8
"""

"""
import os

from PIL import Image
from PIL.ImageDraw import Draw
from PIL.Image import alpha_composite

def add_description_bw(desc, img, font, color, x_max, y_max):
    """The text needs to have a size under 535."""
    if font.getsize(desc)[0] <= 528:
        tmp_draw = Draw(img)
        tmp_text, height = wrap_text(desc, font, 140)
        pos_x, pos_y = x_max - 193, y_max - 89
        for element in tmp_text:
            justified_element = justified_text(element, font, 140)
            tmp_draw.text((pos_x, pos_y), justified_element,
                          font=font, fill=color)
            pos_y += height - 3
            pos_x -= 8

        return img
    else:
        print('Text too long.')
        return img


def add_ability(ability, img, pos, font_text, font_name,
                size_justified, name_color, text_color):
    tmp_pos_y = pos
    # ? Paste this image in a transparent background
    foreground = Image.new("RGBA", img.size, (0, 0, 0, 0))
    tmp_path = os.path.join('resources', 'icons', 'ability.png')
    energy_img = Image.open(tmp_path)
    foreground.paste(energy_img, (30, tmp_pos_y))

    # ? Merge both image
    img = alpha_composite(img, foreground)
    draw = Draw(img)

    ability_name = ability['name']
    draw.text((135, tmp_pos_y + 5), ability_name,
              font=font_name, fill=name_color)

    tmp_pos_y += 30
    tmp_str = ability['text']
    text, height = wrap_text(tmp_str, font_text, size_justified)
    for element in text:
        tmp_el = justified_text(element, font_text, size_justified)
        draw.text((40, tmp_pos_y), tmp_el, font=font_text, fill=text_color)
        tmp_pos_y += height + 5

    return [img, tmp_pos_y]


def add_capacity(capacities, img, pos, x_max, font_text, font_name,
                 font_damage, size_justified, name_color, text_color,
                 space):

    tmp_pos_y = pos

    if capacities is not None:
        for capacity in capacities:
            x_pos = 30
            for energy in capacity['resources']:
                # ? Paste this image in a transparent background
                foreground = Image.new("RGBA", img.size, (0, 0, 0, 0))
                tmp_path = os.path.join('resources', 'icons', energy+'.png')
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

            tmp_pos_y += space
    return [img, tmp_pos_y]


def wrap_text(text, font, size):
    """Wraps text with a special font into a box."""

    height = font.getsize(text)[1]

    word_list = text.split(' ')
    lines = []
    tmp_line = ''
    if len(word_list) == 1:
        for element in text:
            size_text = font.getsize(tmp_line)[0]
            size_word = font.getsize(element)[0]
            if size_text + size_word < size:
                tmp_line += element
            else:
                lines.append(tmp_line)
                tmp_line = '  ' + element
        if tmp_line != '':
            lines.append(tmp_line)

        return [lines, height]
    else:
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

        return [lines, height]


def justified_text(text, font, size):
    """The function to justified a text for a certain size."""

    # ? search all spaces
    indexs = get_spaces_index(text)

    # ? add space to fill the
    tmp_ind = 0
    ind_max = len(indexs)
    space_size = font.getsize(' ')[0]
    diff = size - font.getsize(text)[0]
    if diff < size / 4 and len(indexs) - 1 > 0:
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