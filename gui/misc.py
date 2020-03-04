# -*- coding: utf-8 -*-

"""

"""

import sys

from PySide2 import QtCore, QtGui, QtWidgets
from os import path

from resources.style import stylesheet


# !############################################################################
# ! Miscellaneous classes
# !############################################################################

class AddMinusButtons(QtWidgets.QWidget):
    """
    Basic +/- buttons. it sends one sig per button.
    """

    add_sig = QtCore.Signal()
    min_sig = QtCore.Signal()

    def __init__(self, width=None, height=None):
        super(AddMinusButtons, self).__init__()

        self.setStyleSheet(stylesheet.MISC_BUTTON)

        if width is not None:
            self.setFixedWidth(width)
        if height is not None:
            self.setFixedHeight(height)

        self.button_add = QtWidgets.QPushButton('+')
        self.button_min = QtWidgets.QPushButton('-')
        self.button_add.clicked.connect(self.add_slot)
        self.button_min.clicked.connect(self.min_slot)

        if width is not None:
            self.button_add.setFixedWidth((width/2) - 3)
            self.button_min.setFixedWidth((width/2) - 3)

        if height is not None:
            self.button_add.setFixedHeight(height - 1)
            self.button_min.setFixedHeight(height - 1)

        layout = QtWidgets.QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        layout.addWidget(self.button_add)
        layout.addWidget(self.button_min)
        layout.setContentsMargins(1, 1, 1, 1)
        self.setLayout(layout)

    def add_slot(self):
        self.add_sig.emit()

    def min_slot(self):
        self.min_sig.emit()


class LabelEdit(QtWidgets.QFrame):
    """
    Basic Label + Edit zone
    """

    edit_sig = QtCore.Signal(str)

    def __init__(self, *argv):
        super(LabelEdit, self).__init__()
        self.label = []
        self.edit = []

        index = 0

        for element in argv:
            self.label.append(QtWidgets.QLabel(element))
            self.edit.append(QtWidgets.QLineEdit())
            self.edit[index].textChanged.connect(self.edit_sig.emit)
            index += 1

        layout = QtWidgets.QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        for index in range(len(self.label)):
            layout.addWidget(self.label[index])
            layout.addWidget(self.edit[index])

        self.setLayout(layout)


class LabelComboBox(QtWidgets.QWidget):
    """
    Basic label + comboBox zone
    """
    edit_sig = QtCore.Signal(str)

    def __init__(self, name, *argv):
        """
        argv contains list to initialise combobox
        """
        super(LabelComboBox, self).__init__()

        self.label = QtWidgets.QLabel(name)

        self.combo = QtWidgets.QComboBox()
        self.combo = []

        index = 0
        for _list in argv:
            self.combo.append(QtWidgets.QComboBox())
            self.combo[index].addItems(_list)
            self.combo[index].currentTextChanged.connect(self.edit_sig.emit)
            self.combo[index].setCurrentIndex(0)
            index += 1

        layout = QtWidgets.QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        layout.addWidget(self.label, 25)
        for element in self.combo:
            layout.addWidget(element, int(75/len(self.combo)))
        self.setLayout(layout)

    def item_icons(self, folder_path, index_combo):
        """
        Add Icons to the ComboBox if asked
        """
        tmp = self.combo[index_combo]
        for index in range(self.combo[index_combo].count()):
            path_icon = path.join(folder_path, tmp.itemText(index)+'.png')
            icon = QtGui.QIcon(path_icon)
            tmp.setItemIcon(index, icon)
            tmp.setIconSize(QtCore.QSize(17, 17))


# *############################################################################
# * Main function
# *############################################################################


def main():
    # execute only if run as a script
    app = QtWidgets.QApplication(sys.argv)

    app.exec_()


if __name__ == "__main__":
    main()
