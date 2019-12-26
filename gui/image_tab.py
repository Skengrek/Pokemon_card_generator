# -*- coding: utf-8 -*-

"""

"""

import sys

from PySide2 import QtCore, QtGui, QtWidgets


# !# ! Main Widget
# !

class ImageWidget(QtWidgets.QWidget):
    """
    
    """
    add_image_sig = QtCore.Signal(str)

    def __init__(self):
        super(ImageWidget, self).__init__()

        self.main_image_push = QtWidgets.QPushButton('Add main image')
        self.main_image_push.clicked.connect(self.file_explorer)

        self.main_image_label = QtWidgets.QLabel('No image selected')

        layout = QtWidgets.QVBoxLayout()

        layout.addWidget(self.main_image_push)
        layout.addWidget(self.main_image_label)
        layout.addStretch(1)

        self.setLayout(layout)

    def file_explorer(self):

        """

        """
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(self,
                                                             'Open file',
                                                             '/home')
        if file_name:
            # ! if a file is selected
            self.add_image_sig.emit(file_name)
            self.main_image_label.setText(file_name)


if __name__ == "__main__":
    # execute only if run as a script
    app = QtWidgets.QApplication(sys.argv)
    main_widget = ImageWidget()
    main_widget.show()
    app.exec_()