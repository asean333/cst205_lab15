# Annalise Sean, CST205

# Task 1
# just a screenshot

# Task 2

# The widget that I chose is QGraphicsTransform. This lets you create and control advanced transformations that can be configured independently using specialized properties.
# This is particularly useful for animations, letting you interpolate the property values of each independent transformations.
# https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QGraphicsTransform.html#more

# Task 3
# https://gist.github.com/avner-csumb/1d47ee1c2f45d546f13982de80dade56

import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt
# from __feature__ import snake_case, true_property

my_app = QApplication([])

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        label1 = QLabel('<h1>Annalise Sean</h1>')
        label2 = QLabel('<h2>CST205!</h2>')
        label3 = QLabel('<p>Im small!</p>')

        vbox = QVBoxLayout()
        vbox.addWidget(label1)      
        vbox.addWidget(label2)
        vbox.addWidget(label3)

        # self.palette = Qt.darkMagenta
        self.setLayout(vbox)       
        self.resize(800, 600)
        # self.set_window_title("CST205Lab11 - Annalise Sean")  
        self.setWindowTitle("CST205Lab11 - Annalise Sean")      
        self.show()

my_win = MyWindow()
sys.exit(my_app.exec())


# ///////////////////////////////////////////////////////

'''
class MyWindow(QWidget):
	def __init__(self):
		super().__init__()
		label1 = QLabel('<h1>my text</h1>')
		label2 = QLabel('<h2>more text</h2>')

		vbox = QVBoxLayout()	# creating vertical box object

		vbox.add_widget(label1)
		vbox.add_widget(label2)

		self.palette = Qt.darkMagenta
		self.set_layout(vbox)
		self.resize(800, 600)
		self.show()

# he says only use self in class definition if we need them
# would look like
#class MyWindow(QWidget):
#	def __init__(self):
#		super().__init__()
#		self.label1 = QLabel('<h1>my text</h1>')
#		self.vbox = QVBoxLayout()	# creating vertical box object
#		self.vbox.add_widget(label1)
#		self.set_layout(vbox)
#		self.show()

# create mywindow object
my_win = MyWindow()

//////////

import sys

from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt
from __feature__ import /////
'''
