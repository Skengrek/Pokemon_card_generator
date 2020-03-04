# -*- coding : Utf-8 -*-

"""

"""
import sys

from PySide2 import QtCore, QtGui, QtWidgets

from gui import misc

from src.data import Ability, Attack


class AbilityWidget(QtWidgets.QWidget):
    """

    """
    ability_sig = QtCore.Signal(Ability)

    def __init__(self):
        super(AbilityWidget, self).__init__()

        self.name = misc.LabelEdit('Name')
        self.name.edit_sig.connect(self.send_ability)

        self.text = misc.LabelEdit('Text')
        self.text.edit_sig.connect(self.send_ability)

        layout = QtWidgets.QVBoxLayout()

        layout.addWidget(self.name)
        layout.addWidget(self.text)
        layout.addStretch(1)

        self.setLayout(layout)

    def send_ability(self, _):

        _dict = {
            'name': self.name.edit[0].text(),
            'text': self.text.edit[0].text(),
        }
        self.ability_sig.emit(Ability(self.name.edit[0].text(),
                                      self.text.edit[0].text()))


# Main function

def main():

    app = QtWidgets.QApplication(sys.argv)
    app.exec_()

if __name__ == '__main__':
    main()
