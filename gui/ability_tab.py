# -*- coding : Utf-8 -*-

"""

"""

from __future__ import with_statement, division, print_function

import sys

from PySide2 import QtCore, QtGui, QtWidgets


class AbilityWidget(QtWidgets.QWidget):
    """

    """
    ability_sig = QtCore.Signal(dict)

    def __init__(self):
        super(AbilityWidget, self).__init__()

        size_column = 75

        self.name_label = QtWidgets.QLabel('Name')
        self.name_edit = QtWidgets.QLineEdit()
        self.name_edit.textChanged.connect(self.send_ability)

        self.text_label = QtWidgets.QLabel('Text')
        self.text_edit = QtWidgets.QLineEdit()
        self.text_edit.textChanged.connect(self.send_ability)

        layout = QtWidgets.QGridLayout()

        layout.addWidget(self.name_label, 0, 0, 1, 1)
        layout.addWidget(self.name_edit, 0, 1, 1, -1)

        layout.addWidget(self.text_label, 1, 0, 1, 1)
        layout.addWidget(self.text_edit, 1, 1, 1, -1)

        layout.setRowMinimumHeight(0, 50)
        layout.setRowMinimumHeight(1, 50)

        self.setLayout(layout)

    def send_ability(self):
        _dict = {
            'name': self.name_edit.text(),
            'text': self.text_edit.text(),
        }
        self.ability_sig.emit(_dict)


# Main function

def main():

    app = QtWidgets.QApplication(sys.argv)
    app.exec_()




if __name__ == '__main__':
    main()
