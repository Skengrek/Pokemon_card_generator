# -*- coding: utf-8 -*-

"""

"""

import sys
from os import listdir, sep, path, getcwd

from PySide2 import QtCore, QtGui, QtWidgets
from src.BW import bw
from gui import misc
from resources.style import stylesheet
from gui import image_tab, ability_tab

type_list = ['Basic', 'Dark', 'Dragon', 'Electric', 'Fighting', 'Fire',
             'Grass', 'Metal', 'Psy', 'Water']


# !############################################################################
# ! Main Widget
# !############################################################################


class MainWidget(QtWidgets.QWidget):
    """
    
    """

    def __init__(self):
        super(MainWidget, self).__init__()

        self.edit_zone = EditWidget()
        self.img_zone = ImageWidget()

        self.add_image_zone = image_tab.ImageWidget()
        self.add_image_zone.add_image_sig.connect(self.edit_zone.received_img)

        self.setStyleSheet(stylesheet.DEBUG)

        self.edit_zone.changed_dict_sig.connect(self.img_zone.create_img)
        self.edit_zone.change_background('Basic')

        self.attack_edit = AttackWidget()
        self.attack_edit.send_attack_sig. \
            connect(self.edit_zone.received_attack)
        self.attack_edit.send_slider_sig. \
            connect(self.edit_zone.received_slider)

        self.ability_zone = ability_tab.AbilityWidget()
        self.ability_zone.ability_sig. \
            connect(self.edit_zone.received_ability)
        # ? ##################################################################
        # ? Tab Widget
        # ?###################################################################

        tabs = QtWidgets.QTabWidget()
        tabs.addTab(self.edit_zone, 'Edit text')
        tabs.addTab(self.ability_zone, 'Edit ability')
        tabs.addTab(self.attack_edit, 'Edit attacks')
        tabs.addTab(self.add_image_zone, 'Edit images')

        # ? ##################################################################
        # ? Layout
        # ?###################################################################
        layout = QtWidgets.QHBoxLayout()

        layout.addWidget(tabs)
        layout.addWidget(self.img_zone)

        layout.setSpacing(0)
        self.setLayout(layout)


# !############################################################################
# ! Widgets editing the card
# !############################################################################


class EditWidget(QtWidgets.QWidget):
    changed_dict_sig = QtCore.Signal(dict)

    def __init__(self):
        super(EditWidget, self).__init__()

        self.attacks = None
        self.ability = None
        self.img = None
        self.slider_value = 0

        self.setMinimumWidth(200)
        # ?####################################################################
        # ? Add Label and Edit widgets
        # ?####################################################################

        # TODO add basic option seletcted for QComboBox

        self.name_label = QtWidgets.QLabel('Name')
        self.name_edit = QtWidgets.QLineEdit()
        self.name_edit.textChanged.connect(self.generate_dict)

        self.stage_label = QtWidgets.QLabel('Stage')
        self.stage_edit = QtWidgets.QComboBox()
        # TODO add other stage
        self.stage_edit.addItems(['Basic', 'Stage1', 'Stage2'])
        self.stage_edit.setCurrentIndex(0)
        self.stage_edit.currentTextChanged.connect(self.generate_dict)

        self.type_choice = QtWidgets.QComboBox()
        self.type_choice.addItems(type_list)
        self.type_choice.currentTextChanged.connect(self.change_background)
        self.type_choice.setCurrentIndex(0)

        self.background_choice = QtWidgets.QComboBox()
        self.background_choice.currentTextChanged.connect(self.generate_dict)

        # self.change_background('Basic')

        self.hp_label = QtWidgets.QLabel('Health')
        self.hp_edit = QtWidgets.QLineEdit()
        self.hp_edit.textChanged.connect(self.generate_dict)

        self.size_label = QtWidgets.QLabel('Size')
        self.size_edit = QtWidgets.QLineEdit()
        self.size_edit.textChanged.connect(self.generate_dict)

        self.weight_label = QtWidgets.QLabel('Weight')
        self.weight_edit = QtWidgets.QLineEdit()
        self.weight_edit.textChanged.connect(self.generate_dict)

        self.weak_label = QtWidgets.QLabel('Weakness')
        self.weak_choice = QtWidgets.QComboBox()
        self.weak_choice.addItems(type_list)
        self.weak_choice.currentTextChanged.connect(self.generate_dict)

        self.resist_label = QtWidgets.QLabel('Resistance')
        self.resist_choice = QtWidgets.QComboBox()
        self.resist_choice.addItems(type_list)
        self.resist_choice.currentTextChanged.connect(self.generate_dict)
        self.resist_value = QtWidgets.QComboBox()
        self.resist_value.addItems(['-10', '-20', '-30'])
        self.resist_value.currentTextChanged.connect(self.generate_dict)

        self.retreat_label = QtWidgets.QLabel('Retreat')
        self.retreat_value = QtWidgets.QComboBox()
        self.retreat_value.addItems(['0', '1', '2', '3', '4'])
        self.retreat_value.currentTextChanged.connect(self.generate_dict)

        self.desc_label = QtWidgets.QLabel('Description')
        self.desc_edit = QtWidgets.QLineEdit()
        self.desc_edit.textChanged.connect(self.generate_dict)

        self.setNb_label = QtWidgets.QLabel('Set numbers')
        self.this_number = QtWidgets.QLineEdit()
        self.this_number.textChanged.connect(self.generate_dict)
        self.div_label = QtWidgets.QLabel('/')
        self.max_edit = QtWidgets.QLineEdit()
        self.max_edit.textChanged.connect(self.generate_dict)

        self.illustrator_label = QtWidgets.QLabel('Illustrator')
        self.illustrator_edit = QtWidgets.QLineEdit()
        self.illustrator_edit.textChanged.connect(self.generate_dict)

        self.gen_label = QtWidgets.QLabel('Generation')
        self.gen_value = QtWidgets.QComboBox()
        self.gen_value.addItems(['Black & White'])
        self.gen_value.currentTextChanged.connect(self.generate_dict)

        self.copyright_label = QtWidgets.QLabel('copyright')
        self.copyright_edit = QtWidgets.QLineEdit()
        self.copyright_edit.textChanged.connect(self.generate_dict)

        # ?####################################################################
        # ? Layout
        # ?####################################################################

        layout = QtWidgets.QGridLayout()

        layout.addWidget(self.gen_label, 0, 0, 1, 1)
        layout.addWidget(self.gen_value, 0, 1, 1, -1)

        layout.addWidget(self.name_label, 1, 0, 1, 1)
        layout.addWidget(self.name_edit, 1, 1, 1, -1)

        layout.addWidget(self.stage_label, 2, 0, 1, 1)
        layout.addWidget(self.stage_edit, 2, 1, 1, -1)

        layout.addWidget(self.type_choice, 3, 0, 1, 1)
        layout.addWidget(self.background_choice, 3, 1, 1, -1)

        layout.addWidget(self.hp_label, 4, 0, 1, 1)
        layout.addWidget(self.hp_edit, 4, 1, 1, -1)

        layout.addWidget(self.size_label, 5, 0, 1, 1)
        layout.addWidget(self.size_edit, 5, 1, 1, -1)

        layout.addWidget(self.weight_label, 6, 0, 1, 1)
        layout.addWidget(self.weight_edit, 6, 1, 1, -1)

        layout.addWidget(self.weak_label, 9, 0, 1, 1)
        layout.addWidget(self.weak_choice, 9, 1, 1, -1)

        layout.addWidget(self.resist_label, 10, 0, 1, 1)
        layout.addWidget(self.resist_choice, 10, 1, 1, 1)
        layout.addWidget(self.resist_value, 10, 2, 1, -1)

        layout.addWidget(self.retreat_label, 11, 0, 1, 1)
        layout.addWidget(self.retreat_value, 11, 1, 1, -1)

        layout.addWidget(self.desc_label, 12, 0, 1, 1)
        layout.addWidget(self.desc_edit, 12, 1, 1, -1)

        layout.addWidget(self.illustrator_label, 17, 0, 1, 1)
        layout.addWidget(self.illustrator_edit, 17, 1, 1, -1)

        layout.addWidget(self.setNb_label, 18, 0, 1, 1)
        layout.addWidget(self.this_number, 18, 1, 1, 1)
        layout.addWidget(self.div_label, 18, 2, 1, 1)
        layout.addWidget(self.max_edit, 18, 3, 1, 1)

        layout.addWidget(self.copyright_label, 19, 0, 1, 1)
        layout.addWidget(self.copyright_edit, 19, 1, 1, -1)

        self.setLayout(layout)

    def change_background(self, e):
        """Get all the background available for a specific type"""
        _type = e
        self.background_choice.clear()

        if _type is not None:
            file_list = listdir('resources' + sep + 'background' + sep)
            list_available_background = []
            for element in file_list:
                if _type.lower() in element:
                    list_available_background.append(element[:-4])
            if _type.lower() == 'basic':
                list_available_background.append('colorless')

            self.background_choice.addItems(list_available_background)
            self.update()
            self.generate_dict()

    def generate_dict(self):
        _dict = {
            'name': self.name_edit.text(),
            'stage': self.stage_edit.currentText().lower(),
            'type': self.type_choice.currentText().lower(),
            'background': self.background_choice.currentText(),
            'health': self.hp_edit.text(),
            'image': self.img,
            'height': self.size_edit.text().lower(),
            'weight': self.weight_edit.text().lower(),
            'ability': self.ability,
            'attack': self.attacks,
            'space': self.slider_value,
            'weakness': self.weak_choice.currentText().lower(),
            'resistance': [self.resist_choice.currentText().lower(),
                           self.resist_value.currentText().lower()],
            'retreat': int(self.retreat_value.currentText().lower()),
            'description': self.desc_edit.text(),
            'set_number': self.this_number.text(),
            'set_maximum': self.max_edit.text(),
            'illustrator': self.illustrator_edit.text(),
            'generation': self.gen_value.currentText(),
            'copyright': self.copyright_edit.text(),
        }

        self.changed_dict_sig.emit(_dict)

    def received_attack(self, _list):
        self.attacks = _list
        self.generate_dict()

    def received_ability(self, _dict):
        self.ability = _dict
        self.generate_dict()

    def received_slider(self, slider_value_received):
        self.slider_value = slider_value_received
        self.generate_dict()

    def received_img(self, file_path):
        self.img = file_path
        self.generate_dict()


class AttackWidget(QtWidgets.QWidget):
    """

    """

    # TODO Add a "stretch" (slider) to separate attacks
    send_attack_sig = QtCore.Signal(list)
    send_slider_sig = QtCore.Signal(int)

    def __init__(self):
        super(AttackWidget, self).__init__()

        self.attack = [AttackCreationWidget(self),
                       AttackCreationWidget(self)]

        self.nb_attack = 0

        self.slider = QtWidgets.QSlider(QtCore.Qt.Orientation(1))
        self.slider.hide()
        self.slider.sliderMoved.connect(self.slider_mod)

        self.buttons = misc.AddMinusButtons(100, 25)
        self.buttons.add_sig.connect(self.add_attack)
        self.buttons.min_sig.connect(self.rm_attack)

        layout = QtWidgets.QVBoxLayout()

        layout.addWidget(self.attack[0])
        layout.addWidget(self.slider)
        layout.addWidget(self.attack[1])
        layout.addWidget(self.buttons)

        layout.addStretch(1)

        self.setLayout(layout)
        self.update()

    def add_attack(self):
        if self.nb_attack < 2:

            self.attack[self.nb_attack].show()
            self.nb_attack += 1

            if self.nb_attack == 2:
                self.slider.show()

    def rm_attack(self):
        if self.nb_attack > 0:
            self.slider.hide()
            self.nb_attack -= 1
            self.attack[self.nb_attack].hide()

    def send_attack(self):
        _list = []
        for element in self.attack:
            if not element.isHidden():
                _list.append(element.get_attack())
        self.send_attack_sig.emit(_list)

    def slider_mod(self, e):
        self.send_slider_sig.emit(e)


class AttackCreationWidget(QtWidgets.QWidget):

    def __init__(self, parent):
        super(AttackCreationWidget, self).__init__()

        self.parent = parent

        size_column = 75

        self.name_label = QtWidgets.QLabel('Name')
        self.name_edit = QtWidgets.QLineEdit()
        self.name_edit.textChanged.connect(parent.send_attack)

        self.text_label = QtWidgets.QLabel('Text')
        self.text_edit = QtWidgets.QLineEdit()
        self.text_edit.textChanged.connect(parent.send_attack)

        self.damage_label = QtWidgets.QLabel('Damages')
        self.damage_edit = QtWidgets.QLineEdit()
        self.damage_edit.textChanged.connect(parent.send_attack)

        self.energies_label = QtWidgets.QLabel('Energies')

        self.energies = [QtWidgets.QComboBox(),
                         QtWidgets.QComboBox(),
                         QtWidgets.QComboBox(),
                         QtWidgets.QComboBox(),
                         ]

        self.energies[0].addItems(type_list)
        self.energies[1].addItems(type_list)
        self.energies[2].addItems(type_list)
        self.energies[3].addItems(type_list)

        self.energies[0].hide()
        self.energies[1].hide()
        self.energies[2].hide()
        self.energies[3].hide()

        self.energies[0].currentTextChanged.connect(self.parent.send_attack)
        self.energies[1].currentTextChanged.connect(self.parent.send_attack)
        self.energies[2].currentTextChanged.connect(self.parent.send_attack)
        self.energies[3].currentTextChanged.connect(self.parent.send_attack)

        self.nb_energies = 0

        self.buttons_energy = misc.AddMinusButtons(size_column, 25)
        self.buttons_energy.add_sig.connect(self.add_energy)
        self.buttons_energy.min_sig.connect(self.rm_energy)

        layout = QtWidgets.QGridLayout()

        layout.addWidget(self.name_label, 0, 0, 1, 1)
        layout.addWidget(self.name_edit, 0, 1, 1, 3)

        layout.addWidget(self.text_label, 1, 0, 1, 1)
        layout.addWidget(self.text_edit, 1, 1, 1, 3)

        layout.addWidget(self.damage_label, 2, 0, 1, 1)
        layout.addWidget(self.damage_edit, 2, 1, 1, 3)

        layout.addWidget(self.energies_label, 3, 0, 1, 1)
        layout.addWidget(self.buttons_energy, 3, 1)
        layout.addWidget(self.energies[0], 4, 0, 1, 1)
        layout.addWidget(self.energies[1], 4, 1, 1, 1)
        layout.addWidget(self.energies[2], 4, 2, 1, 1)
        layout.addWidget(self.energies[3], 4, 3, 1, 1)

        layout.setColumnStretch(0, 0)
        layout.setColumnStretch(1, 0)
        layout.setColumnStretch(2, 0)
        layout.setColumnStretch(3, 0)

        layout.setColumnMinimumWidth(0, size_column)
        layout.setColumnMinimumWidth(1, size_column)
        layout.setColumnMinimumWidth(2, size_column)
        layout.setColumnMinimumWidth(3, size_column)

        self.setLayout(layout)
        self.hide()

    def add_energy(self):
        if self.nb_energies <= 3:
            self.energies[self.nb_energies].show()
            self.nb_energies += 1
            self.parent.send_attack()

    def rm_energy(self):
        if self.nb_energies > 0:
            self.nb_energies -= 1
            self.energies[self.nb_energies].hide()
            self.parent.send_attack()

    def get_attack(self):
        _dict = {
            'name': self.name_edit.text(),
            'text': self.text_edit.text(),
            'damage': self.damage_edit.text(),
        }
        energies_saved = []
        for element in self.energies:
            if not element.isHidden():
                energies_saved.append(element.currentText())

        _dict['resources'] = energies_saved
        return _dict


# !############################################################################
# ! Image Widget
# !############################################################################


class ImageWidget(QtWidgets.QLabel):

    def __init__(self):
        super(ImageWidget, self).__init__()

        self.img_viewer = ImageViewer()
        self.save_button = QtWidgets.QPushButton('Save')
        self.save_button.clicked.connect(self.img_viewer.save_file)

        layout = QtWidgets.QVBoxLayout()

        layout.addWidget(self.img_viewer)
        layout.addWidget(self.save_button)

        self.setLayout(layout)
        self.show()

    def create_img(self, _dict):
        self.img_viewer.create_img(_dict)


class ImageViewer(QtWidgets.QLabel):

    def __init__(self):
        super(ImageViewer, self).__init__()
        self.img = None
        self.setMinimumSize(420, 590)

    def create_img(self, _dict):
        if _dict['generation'] == 'Black & White':
            _dict['generation'] = 'BW'
            tmp_img = bw(_dict)
            self.img = QtGui.QPixmap.fromImage(tmp_img)
            self.setPixmap(self.img)
            # TODO update size with image size !

        self.update()

    def save_file(self):
        if self.img is not None:
            filename = \
                QtWidgets.QFileDialog.getSaveFileName(self, "Save file",
                                                      "", ".png")

            self.img.save(''.join(filename), "PNG", 100)


def main():
    # execute only if run as a script
    app = QtWidgets.QApplication(sys.argv)
    main_widget = MainWidget()
    main_widget.show()
    app.exec_()


if __name__ == "__main__":
    main()
