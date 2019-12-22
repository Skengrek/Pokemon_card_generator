# -*- coding: utf-8 -*-

"""

"""

import sys

from PySide2 import QtCore, QtGui, QtWidgets


# !# ! Main Widget
# !

class ImageTab(QtWidgets.QWidget):
    """
    
    """

    def __init__(self):
        super(ImageTab, self).__init__()


if __name__ == "__main__":
    # execute only if run as a script
    app = QtWidgets.QApplication(sys.argv)
    main_widget = ImageTab()
    main_widget.show()
    app.exec_()