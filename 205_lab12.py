# Annalise Sean, CST205

import sys
from PySide6.QtWidgets import (
	QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QComboBox, QTabWidget
)
from PySide6.QtCore import Qt, Slot
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color

# dictionary
color_data = {
	"Red": {"rgb": (255, 0, 0), "hex": "#FF0000"},
	"Green": {"rgb": (0, 255, 0), "hex": "#00FF00"},
	"Blue": {"rgb": (0, 0, 255), "hex": "#0000FF"},
	"Yellow": {"rgb": (255, 255, 0), "hex": "#FFFF00"},
	"Cyan": {"rgb": (0, 255, 255), "hex": "#00FFFF"},
	"Magenta": {"rgb": (255, 0, 255), "hex": "#FF00FF"},

}

# Task 1
class ButtonWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.label = QLabel("Click a button!")
		self.button1 = QPushButton("Button 1")
		self.button2 = QPushButton("Button 2")

		self.button1.clicked.connect(self.show_message1)
		self.button2.clicked.connect(self.show_message2)

		layout = QVBoxLayout()
		layout.addWidget(self.label)
		layout.addWidget(self.button1)
		layout.addWidget(self.button2)
		self.setLayout(layout)

	@Slot()
	def show_message1(self):
		self.label.setText("Button 1 clicked")

	@Slot()
	def show_message2(self):
		self.label.setText("Button 2 clicked")

# Task 2
class ColorExchange(QWidget):
	def __init__(self):
		super().__init__()
		self.combo = QComboBox()
		self.combo.addItems(color_data.keys())
		self.combo.currentTextChanged.connect(self.update_color_info)

		self.rgb_label = QLabel("RGB: ")
		self.hex_label = QLabel("Hex: ")

		layout = QVBoxLayout()
		layout.addWidget(self.combo)
		layout.addWidget(self.rgb_label)
		layout.addWidget(self.hex_label)
		self.setLayout(layout)

		self.update_color_info(self.combo.currentText())

	def update_color_info(self, color_name):
		rgb = color_data[color_name]["rgb"]
		hex_val = color_data[color_name]["hex"]
		self.rgb_label.setText(f"RGB: {rgb}")
		self.hex_label.setText(f"Hex: {hex_val}")

# Task 3
class ColorExchangeLab(QWidget):
	def __init__(self):
		super().__init__()
		self.combo = QComboBox()
		self.combo.addItems(color_data.keys())
		self.combo.currentTextChanged.connect(self.update_color_info)

		self.rgb_label = QLabel("RGB: ")
		self.hex_label = QLabel("Hex: ")
		self.lab_label = QLabel("CIELAB: ")

		layout = QVBoxLayout()
		layout.addWidget(self.combo)
		layout.addWidget(self.rgb_label)
		layout.addWidget(self.hex_label)
		layout.addWidget(self.lab_label)
		self.setLayout(layout)

		self.update_color_info(self.combo.currentText())

	def update_color_info(self, color_name):
		rgb = color_data[color_name]["rgb"]
		hex_val = color_data[color_name]["hex"]
		self.rgb_label.setText(f"RGB: {rgb}")
		self.hex_label.setText(f"Hex: {hex_val}")

		srgb = sRGBColor(rgb[0]/255.0, rgb[1]/255.0, rgb[2]/255.0)
		lab = convert_color(srgb, LabColor)
		self.lab_label.setText(
			f"CIELAB: L*={lab.lab_l:.2f}, a*={lab.lab_a:.2f}, b*={lab.lab_b:.2f}"
		)

class MainWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("CST205 — Combined GUI")
		self.resize(500, 300)

		tabs = QTabWidget()
		tabs.addTab(ButtonWindow(), "Task 1")
		tabs.addTab(ColorExchange(), "Task 2")
		tabs.addTab(ColorExchangeLab(), "Task 3")

		layout = QVBoxLayout()
		layout.addWidget(tabs)
		self.setLayout(layout)
		self.show()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow()
	sys.exit(app.exec())

# /////////////////////////////

'''# Task 1 

import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QComboBox
from PySide6.QtCore import Qt, Slot

class ButtonWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Task 1")

		self.label = QLabel("Click a button!")
		self.button1 = QPushButton("Button 1")
		self.button2 = QPushButton("Button 2")

		self.button1.clicked.connect(self.show_message1)
		self.button2.clicked.connect(self.show_message2)

		layout = QVBoxLayout()
		layout.addWidget(self.label)
		layout.addWidget(self.button1)
		layout.addWidget(self.button2)
		self.setLayout(layout)

		self.resize(400, 400)
		self.show()

	@Slot()
	def show_message1(self):
		self.label.setText("Button 1 clicked")

	@Slot()
	def show_message2(self):
		self.label.setText("Button 2 clicked")

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = ButtonWindow()
	sys.exit(app.exec())
	
# Task 2

# dictionary
color_data = {
	"Red": {"rgb": (255, 0, 0), "hex": "#FF0000"},
	"Green": {"rgb": (0, 255, 0), "hex": "#00FF00"},
	"Blue": {"rgb": (0, 0, 255), "hex": "#0000FF"},
	"Yellow": {"rgb": (255, 255, 0), "hex": "#FFFF00"},
	"Magenta": {"rgb": (255, 0, 255), "hex": "#FF00FF"},
	"Cyan": {"rgb": (0, 255, 255), "hex": "#00FFFF"},
}

class ColorExchange(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Task 2")

        # combobox
		self.combo = QComboBox()
		self.combo.addItems(color_data.keys())
		self.combo.currentTextChanged.connect(self.update_color_info)

		self.rgb_label = QLabel("RGB: ")
		self.hex_label = QLabel("Hex: ")

		layout = QVBoxLayout()
		layout.addWidget(self.combo)
		layout.addWidget(self.rgb_label)
		layout.addWidget(self.hex_label)
		self.setLayout(layout)

		self.resize(350, 150)
		self.show()

		self.update_color_info(self.combo.currentText())

	def update_color_info(self, color_name):
		rgb = color_data[color_name]["rgb"]
		hex_val = color_data[color_name]["hex"]
		self.rgb_label.setText(f"RGB: {rgb}")
		self.hex_label.setText(f"Hex: {hex_val}")

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = ColorExchange()
	sys.exit(app.exec())
	
# Task 3

import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QComboBox
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color

# Dictionary of colors with RGB and Hex values
color_data = {
	"Red": {"rgb": (255, 0, 0), "hex": "#FF0000"},
	"Green": {"rgb": (0, 255, 0), "hex": "#00FF00"},
	"Blue": {"rgb": (0, 0, 255), "hex": "#0000FF"},
	"Yellow": {"rgb": (255, 255, 0), "hex": "#FFFF00"},
	"Magenta": {"rgb": (255, 0, 255), "hex": "#FF00FF"},
	"Cyan": {"rgb": (0, 255, 255), "hex": "#00FFFF"},
}

class ColorExchangeLab(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Task 3")

		self.combo = QComboBox()
		self.combo.addItems(color_data.keys())
		self.combo.currentTextChanged.connect(self.update_color_info)

		self.rgb_label = QLabel("RGB: ")
		self.hex_label = QLabel("Hex: ")
		self.lab_label = QLabel("CIELAB: ")

		layout = QVBoxLayout()
		layout.addWidget(self.combo)
		layout.addWidget(self.rgb_label)
		layout.addWidget(self.hex_label)
		layout.addWidget(self.lab_label)
		self.setLayout(layout)

		self.resize(400, 200)
		self.show()
		self.update_color_info(self.combo.currentText())

	def update_color_info(self, color_name):
		rgb = color_data[color_name]["rgb"]
		hex_val = color_data[color_name]["hex"]

		self.rgb_label.setText(f"RGB: {rgb}")
		self.hex_label.setText(f"Hex: {hex_val}")

		# convert RGB to CIELAB
		srgb = sRGBColor(rgb[0]/255.0, rgb[1]/255.0, rgb[2]/255.0)
		lab = convert_color(srgb, LabColor)
		self.lab_label.setText(
			f"CIELAB: L*={lab.lab_l:.2f}, a*={lab.lab_a:.2f}, b*={lab.lab_b:.2f}"
		)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = ColorExchangeLab()
	sys.exit(app.exec())
'''


'''
class MyWindow(QWidget):

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
      '''

# ///////////////////////

'''
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

'''

# ///////////////////////

'''
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
'''

# ///////////////////////
'''
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
'''

# Task 1 buttons



# Task 2 color exchange



# Task 3 color exchange 2