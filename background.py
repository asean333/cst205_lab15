# sys module needed for optional command line arguments
import sys

# Qt Widgets Module provides a set of UI elements to create classic desktop-style user interfaces
# QApplication is a class in the Qt Widgets module and manages the GUI application's control flow and main settings
# QWidget is a class in the Qt Widgets module and is the base class of all user interface objects
# QLabel is a class in the Qt Widgets module that provides a text or image display
from PySide6.QtWidgets import QApplication, QWidget, QLabel


# All other Qt modules rely on this Qt Core
# Qt namespace, used here for GlobalColor enum
# see http://bit.ly/3l6enCh
from PySide6.QtCore import Qt

from __feature__ import snake_case, true_property



# calls the constructor of the C++ class QApplication
# uses sys.argv to initialize the QT application
# for this application it will pass ['background.py']
my_qt_app = QApplication([])

class ColorWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.window_title = 'Background'
        self.palette = Qt.darkMagenta

my_window = ColorWindow()
my_window.show()

# my_qt_app.exec_() runs the main loop
# putting it in sys.exit() allows for a graceful exit
sys.exit(my_qt_app.exec())