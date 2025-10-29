import sys
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QDialog, QGroupBox, 
                                  QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit)
from __feature__ import snake_case, true_property

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        label1 = QLabel('QLineEdit: ')
        line_edit = QLineEdit()

        hbox1 = QHBoxLayout()
        hbox1.add_widget(label1)
        hbox1.add_widget(line_edit)

        gbox1 = QGroupBox('Group Box 1')
        gbox1.set_layout(hbox1)

        label2 = QLabel('Here are some buttons:')
        b1 = QPushButton('button 1')
        b2 = QPushButton('button 2')

        hbox2 = QHBoxLayout()
        hbox2.add_widget(label2)

        hbox3 = QHBoxLayout()
        hbox3.add_widget(b1)
        hbox3.add_widget(b2)

        vbox2 = QVBoxLayout()
        vbox2.add_layout(hbox2)
        vbox2.add_layout(hbox3)

        gbox2 = QGroupBox("Group Box 2")
        gbox2.set_layout(vbox2)

        mbox = QVBoxLayout()
        mbox.add_widget(gbox1)
        mbox.add_widget(gbox2)

        self.set_layout(mbox)
        self.window_title = "CST 205 App"

app = QApplication([])
win = MyWindow()
win.show()
sys.exit(app.exec())