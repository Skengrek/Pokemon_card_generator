# -*- coding: utf-8 -*-

"""

"""

import sys
from os import listdir, sep, path

from PySide2 import QtCore, QtGui, QtWidgets
from src.BW import bw

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

        self.edit_zone.changed_dict_sig.connect(self.img_zone.create_img)

        self.edit_zone.change_background('Basic')

        # ? ###################################################################
        # ? Layout
        # ?####################################################################
        layout = QtWidgets.QHBoxLayout()

        layout.addWidget(self.edit_zone)
        layout.addWidget(self.img_zone)

        self.setLayout(layout)


# !############################################################################
# ! ToolBar
# !############################################################################


class ToolBar(QtWidgets.QToolBar):
    """

    """

    def __init__(self):
        super(ToolBar, self).__init__()


# !############################################################################
# ! Edit Widget
# !############################################################################


class EditWidget(QtWidgets.QWidget):

    changed_dict_sig = QtCore.Signal(dict)

    def __init__(self):
        super(EditWidget, self).__init__()

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
        self.stage_edit.addItems(['Basic'])
        self.stage_edit.setCurrentIndex(0)

        type_list = ['Basic', 'Dark', 'Dragon', 'Electric', 'Fighting', 'Fire',
                     'Grass', 'Metal', 'Psy', 'Water']

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
        self.weak_choice.addItems(type_list[1:])
        self.weak_choice.currentTextChanged.connect(self.generate_dict)

        self.resist_label = QtWidgets.QLabel('Resistance')
        self.resist_choice = QtWidgets.QComboBox()
        self.resist_choice.addItems(type_list[1:])
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

        # ?####################################################################
        # ? Set values
        # ?####################################################################

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
        layout.addWidget(self.max_edit, 18, 3, 1, -1)

        self.setLayout(layout)

    def change_background(self, e):
        """Get all the background available for a specific type"""
        _type = e
        self.background_choice.clear()

        if _type is not None:
            file_list = listdir('resources'+sep+'background'+sep)
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
            'name': self.name_edit.text().lower(),
            'stage': self.stage_edit.currentText().lower(),
            'type': self.type_choice.currentText().lower(),
            'background': self.background_choice.currentText().lower(),
            'health': self.hp_edit.text(),
            'image': None,
            'height': self.size_edit.text().lower(),
            'weight': self.weight_edit.text().lower(),
            'ability': None,
            'attack': None,
            'weakness': self.weak_choice.currentText().lower(),
            'resistance': [self.resist_choice.currentText().lower(),
                           self.resist_value.currentText().lower()],
            'retreat': int(self.retreat_value.currentText().lower()),
            'description': self.desc_edit.text(),
            'set_number': self.this_number.text(),
            'set_maximum': self.max_edit.text(),
            'illustrator': self.illustrator_edit.text(),
            'generation': self.gen_value.currentText(),
        }

        self.changed_dict_sig.emit(_dict)


# !############################################################################
# ! Image Widget
# !############################################################################


class ImageWidget(QtWidgets.QLabel):

    def __init__(self):
        super(ImageWidget, self).__init__()

    def create_img(self, _dict):
        if _dict['generation'] == 'Black & White':
            _dict['generation'] = 'BW'
            tmp_img = bw(_dict)
            self.img = QtGui.QPixmap.fromImage(tmp_img)
            self.setPixmap(self.img)
        self.update()


def main():
    # execute only if run as a script
    app = QtWidgets.QApplication(sys.argv)
    main_widget = MainWidget()
    main_widget.show()
    app.exec_()


if __name__ == "__main__":
    main()
