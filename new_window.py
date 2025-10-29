import sys
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QLineEdit, 
                                QHBoxLayout, QVBoxLayout, QDialog, QTextBrowser, QComboBox)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Slot
from __feature__ import snake_case, true_property
app = QApplication([])

my_list = ['sun', 'sky', 'beach']

class MyWindow(QWidget):
  def __init__(self):
    super().__init__()
    self.combo = QComboBox()
    self.combo.add_items(my_list)
    btn = QPushButton('CLICK ME')
    vbox = QVBoxLayout()
    vbox.add_widget(self.combo)
    vbox.add_widget(btn)
    self.set_layout(vbox)
    btn.clicked.connect(self.open_win)

  @Slot() 
  def open_win(self):
    i = self.combo.current_index
    self.new_win = NewWindow(my_list[i])
    self.new_win.show()

class NewWindow(QWidget):
  def __init__(self, nice_things):
    super().__init__()
    my_text = QLabel(nice_things)
    self.layout = QVBoxLayout()
    self.layout.add_widget(my_text)
    self.set_layout(self.layout)


main = MyWindow()
main.show()
sys.exit(app.exec())