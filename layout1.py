import sys
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout)
from __feature__ import snake_case, true_property

app = QApplication([])

class LayoutOne(QWidget):
    def __init__(self):
        super().__init__()
        label1 = QLabel('Label 1')
        label2 = QLabel('Label 2')
        vbox = QVBoxLayout()
        vbox.add_widget(label1)
        vbox.add_widget(label2)
        self.set_layout(vbox)
        self.resize(800, 600)
        self.show()

my_win = LayoutOne()
sys.exit(app.exec())