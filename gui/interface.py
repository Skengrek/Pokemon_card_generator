# -*- coding: utf-8 -*-

"""

"""

import sys

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
        self.stage_edit = QtWidgets.QLineEdit()

        type_list = ['Basic', 'Dark', 'Electric', 'Fighting', 'Fire', 'Grass',
                     'Metal', 'Psy', 'Water']
        self.type_choice = QtWidgets.QComboBox()
        self.type_choice.addItems(type_list)

        self.hp_label = QtWidgets.QLabel('Health')
        self.hp_edit = QtWidgets.QLineEdit()

        # ?####################################################################
        # ? Layout
        # ?####################################################################

        layout = QtWidgets.QGridLayout()

        layout.addWidget(self.name_label, 1, 0, 1, 2)
        layout.addWidget(self.name_edit, 1, 1, 1, 2)

        layout.addWidget(self.stage_label, 2, 0, 1, 2)
        layout.addWidget(self.stage_edit, 2, 1, 1, 2)

        layout.addWidget(self.type_choice, 3, 0, 1, -1)

        layout.addWidget(self.hp_label, 4, 0)
        layout.addWidget(self.hp_edit, 4, 1)

        self.setLayout(layout)


if __name__ == "__main__":
    # execute only if run as a script
    app = QtWidgets.QApplication(sys.argv)
    main_widget = MainWidget()
    main_widget.show()
    app.exec_()
