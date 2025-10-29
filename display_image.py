import sys
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from __feature__ import snake_case, true_property

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        label = QLabel()
        my_pixmap = QPixmap('walk.jpg')
        my_pixmap = my_pixmap.scaled(500, 500, Qt.KeepAspectRatio)
        label.pixmap = my_pixmap
        self.layout = QVBoxLayout()
        self.layout.add_widget(label)
        self.set_layout(self.layout)
   
app = QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec())