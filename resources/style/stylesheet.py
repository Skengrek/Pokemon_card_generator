"""

"""

MISC_BUTTON = """
QPushButton{
    background-color: grey;
    border: 1px black;
}

"""

GENERIC = """
QLabel{
    min-width: 75px;
    max-width: 75px;
}

QLabel#slash{
    min-width: 10px;
    max-width: 10px;
    qproperty-alignment: AlignCenter;
}
""" + """
 QComboBox {
    border: 1px solid darkgrey;
    border-radius: 3px;
    padding: 1px 18px 1px 3px;
    min-width: 6em;
 }
 
 QComboBox:!editable, QComboBox::drop-down:editable {
      background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                  stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,
                                  stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);
 }
 
 QComboBox:!editable:on, QComboBox::drop-down:editable:on {
     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                 stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,
                                 stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);
 }
 
 QComboBox:on { /* shift the text when the popup opens */
     padding-top: 3px;
     padding-left: 4px;
 }
 
 QComboBox::drop-down {
    
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 15px;
    
    border-left-width: 1px;
    border-left-color: darkgray;
    border-left-style: solid; /* just a single line */
    border-top-right-radius: 3px; /* same radius as the QComboBox */
    border-bottom-right-radius: 3px;
 }
 
 QComboBox::down-arrow:on { /* shift the arrow when popup is open */
     top: 1px;
     left: 1px;
 }
 
 QComboBox QAbstractItemView {
    border: 2px solid darkgray;
    selection-background-color: red;
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                 stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,
                                 stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);
}

"""
DEBUG = """
QLabel{
    background-color: yellow;
}

QComboBox{
    background-color: red;
}

QLineEdit{
    background-color: purple;
}

QSlider{
    background-color: pink;
}

"""