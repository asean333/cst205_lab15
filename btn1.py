import sys
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QPushButton)
from PySide6.QtCore import Slot  
from __feature__ import snake_case, true_property

app = QApplication([])

class ButtonOne(QWidget):
    def __init__(self):
        super().__init__()
        vbox = QVBoxLayout()
        my_btn = QPushButton('button 1')
        self.my_lbl = QLabel('button not yet clicked')
        my_btn.clicked.connect(self.on_click)

        vbox.add_widget(self.my_lbl)
        vbox.add_widget(my_btn)

        self.set_layout(vbox)
        self.resize(400, 400)
        self.show()

    @Slot()
    def on_click(self):
        self.my_lbl.text = 'button has been clicked!'

btn_win = ButtonOne()
sys.exit(app.exec())