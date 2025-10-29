import sys
from PySide6.QtWidgets import (QApplication, QLabel, QWidget, 
                                QPushButton, QLineEdit, QVBoxLayout, QComboBox)
from PySide6.QtCore import Slot
from __feature__ import snake_case, true_property

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.my_list = ["Pick a value", "vanilla", "chocolate", "raspberry", "coconut"]

        self.my_combo_box = QComboBox()
        self.my_combo_box.add_items(self.my_list)
        self.my_label = QLabel("")

        vbox = QVBoxLayout()
        vbox.add_widget(self.my_combo_box)
        vbox.add_widget(self.my_label)

        self.set_layout(vbox)
        self.my_combo_box.currentIndexChanged.connect(self.update_ui)

    @Slot()
    def update_ui(self):
        my_text = self.my_combo_box.current_text
        my_index = self.my_combo_box.current_index
        self.my_label.text = f'You chose {self.my_list[my_index]}.'


app = QApplication([])
my_win = MyWindow()
my_win.show()
sys.exit(app.exec())