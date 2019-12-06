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
        self.grid = QtWidgets.QGridLayout()

        self.grid.addWidget(self.edit_zone, 1, 0)

        self.setLayout(self.grid)


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
        self.name_edit = QtWidgets.QLineEdit()




if __name__ == "__main__":
    # execute only if run as a script
    app = QtWidgets.QApplication(sys.argv)
    main_widget = MainWidget()
    main_widget.show()
    app.exec_()