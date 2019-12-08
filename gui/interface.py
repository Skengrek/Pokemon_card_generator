# -*- coding: utf-8 -*-

"""

"""

import sys
from os import listdir, sep, getcwd

from PySide2 import QtCore, QtGui, QtWidgets

# !############################################################################
# ! Main Widget
# !############################################################################


class MainWidget(QtWidgets.QWidget):
    """
    
    """

    def __init__(self):
        super(MainWidget, self).__init__()

        self.edit_zone = EditWidget()

        # ? ###################################################################
        # ? Layout
        # ?####################################################################
        layout = QtWidgets.QHBoxLayout()

        layout.addWidget(self.edit_zone)

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

    def __init__(self):
        super(EditWidget, self).__init__()

        # ?####################################################################
        # ? Add Label and Edit widgets
        # ?####################################################################
        self.name_label = QtWidgets.QLabel('Name')
        self.name_edit = QtWidgets.QLineEdit()

        self.stage_label = QtWidgets.QLabel('Stage')
        self.stage_edit = QtWidgets.QComboBox()
        # TODO add other stage
        self.stage_edit.addItems(['Basic'])

        type_list = ['Basic', 'Dark', 'Dragon', 'Electric', 'Fighting', 'Fire',
                     'Grass', 'Metal', 'Psy', 'Water']

        self.type_choice = QtWidgets.QComboBox()
        self.type_choice.addItems(type_list)
        self.type_choice.currentTextChanged.connect(self.change_background)

        self.background_choice = QtWidgets.QComboBox()
        self.change_background('Basic')

        self.hp_label = QtWidgets.QLabel('Health')
        self.hp_edit = QtWidgets.QLineEdit()

        self.size_label = QtWidgets.QLabel('Size')
        self.size_edit = QtWidgets.QLineEdit()

        self.weight_label = QtWidgets.QLabel('Weight')
        self.weight_edit = QtWidgets.QLineEdit()

        self.weak_label = QtWidgets.QLabel('Weakness')
        self.weak_choice = QtWidgets.QComboBox()
        self.weak_choice.addItems(type_list)

        self.resist_label = QtWidgets.QLabel('Resistance')
        self.resist_choice = QtWidgets.QComboBox()
        self.resist_choice.addItems(type_list)
        self.resist_value = QtWidgets.QComboBox()
        self.resist_value.addItems(['-10', '-20', '-30'])

        self.retreat_label = QtWidgets.QLabel('Retreat')
        self.retreat_value = QtWidgets.QComboBox()
        self.retreat_value.addItems(['0', '1', '2', '3', '4'])

        self.desc_label = QtWidgets.QLabel('Description')
        self.desc_edit = QtWidgets.QLineEdit()

        self.setNb_label = QtWidgets.QLabel('Set numbers')
        self.this_edit = QtWidgets.QLineEdit()
        self.div_label = QtWidgets.QLabel('/')
        self.max_edit = QtWidgets.QLineEdit()

        self.illustrator_label = QtWidgets.QLabel('Illustrator')
        self.illustrator_edit = QtWidgets.QLineEdit()

        self.gen_label = QtWidgets.QLabel('Retreat')
        self.gen_value = QtWidgets.QComboBox()
        self.gen_value.addItems(['Black & White'])

        # ?####################################################################
        # ? Layout
        # ?####################################################################

        layout = QtWidgets.QGridLayout()

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

        layout.addWidget(self.setNb_label, 17, 0, 1, 1)
        layout.addWidget(self.this_edit, 17, 1, 1, 1)
        layout.addWidget(self.div_label, 17, 2, 1, 1)
        layout.addWidget(self.max_edit, 17, 3, 1, -1)

        layout.addWidget(self.illustrator_label, 18, 0, 1, 1)
        layout.addWidget(self.illustrator_edit, 18, 1, 1, -1)

        layout.addWidget(self.gen_label, 19, 0, 1, 1)
        layout.addWidget(self.gen_value, 19, 1, 1, -1)

        self.setLayout(layout)

    def change_background(self, e):
        """Get all the background available for a specific type"""
        _type = e
        self.background_choice.clear()

        if _type is not None:
            file_list = listdir('..'+sep+'resources'+sep+'background'+sep)
            list_available_background = []
            for element in file_list:
                if _type.lower() in element:
                    list_available_background.append(element[:-4])
            if _type.lower() == 'basic':
                list_available_background.append('colorless')

            self.background_choice.addItems(list_available_background)
            self.update()


if __name__ == "__main__":
    # execute only if run as a script
    app = QtWidgets.QApplication(sys.argv)
    main_widget = MainWidget()
    main_widget.show()
    app.exec_()
