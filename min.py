import sys
from PySide6.QtWidgets import (QWidget, QApplication)
from __feature__ import snake_case, true_property

my_app = QApplication([])

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.show()


my_win = MyWindow()
sys.exit(my_app.exec())