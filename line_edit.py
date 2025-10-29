import sys
from PySide6.QtWidgets import (QApplication, QLabel, QWidget, 
                                QPushButton, QLineEdit, QVBoxLayout)
from PySide6.QtCore import Slot
from __feature__ import snake_case, true_property

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        vbox = QVBoxLayout()
        self.my_le = QLineEdit("What's your favorite song?")
        self.my_le.minimum_width = 250
        self.my_le.select_all()
        my_btn = QPushButton("Submit")
        self.my_lbl = QLabel('')
        my_btn.clicked.connect(self.on_submit)
        self.my_le.returnPressed.connect(self.on_submit)
        vbox.add_widget(self.my_le)
        vbox.add_widget(my_btn)
        vbox.add_widget(self.my_lbl)
        self.set_layout(vbox)

    @Slot()
    def on_submit(self):
        your_song = self.my_le.text
        self.my_lbl.text = f'Your favorite song is {your_song}'


app = QApplication([])
my_win = MyWindow()
my_win.show()
sys.exit(app.exec())