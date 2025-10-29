# Annalise Sean, CST205

import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QComboBox, QLabel
)
from PySide6.QtGui import QPalette, QColor
from __feature__ import snake_case, true_property

app = QApplication([])

# Task 1
def run_task_1():
    class BlueWindow(QWidget):
        def __init__(self):
            super().__init__()
            self.window_title = "Blue Window"
            self.resize(200, 200)
            palette = self.palette
            palette.set_color(QPalette.Window, QColor("blue"))
            self.palette = palette
            self.auto_fill_background = True
            self.move(100, 100)

    class RedWindow(QWidget):
        def __init__(self):
            super().__init__()
            self.window_title = "Red Window"
            self.resize(200, 200)
            palette = self.palette
            palette.set_color(QPalette.Window, QColor("red"))
            self.palette = palette
            self.auto_fill_background = True
            self.move(350, 100)

    win1 = BlueWindow()
    win2 = RedWindow()
    win1.show()
    win2.show()

# Task 2
def run_task_2():
    class NestedWindow(QWidget):
        def __init__(self):
            super().__init__()
            self.window_title = "Nested Layout"

            h_layout = QHBoxLayout()
            h_layout.add_widget(QPushButton("Left"))
            h_layout.add_widget(QPushButton("Right"))

            v_layout = QVBoxLayout()
            v_layout.add_widget(QPushButton("Top"))
            v_layout.add_layout(h_layout)
            v_layout.add_widget(QPushButton("Bottom"))

            self.set_layout(v_layout)

    window = NestedWindow()
    window.show()

# Task 3
def run_task_3():
    class ColorDisplay(QWidget):
        def __init__(self, color_name):
            super().__init__()
            self.window_title = f"Color: {color_name}"
            self.resize(200, 200)
            palette = self.palette
            palette.set_color(QPalette.Window, QColor(color_name))
            self.palette = palette
            self.auto_fill_background = True

    class ColorSelector(QWidget):
        def __init__(self):
            super().__init__()
            self.window_title = "Select a Color"
            self.resize(300, 100)

            self.combo = QComboBox()
            self.combo.add_items(["red", "orange", "yellow", "green", "blue", "purple"])

            self.button = QPushButton("Show Color")
            self.button.clicked.connect(self.show_color)

            self.color_display = QLabel("")

            layout = QVBoxLayout()
            layout.add_widget(self.combo)
            layout.add_widget(self.button)
            layout.add_widget(self.color_display)
            self.set_layout(layout)

        def show_color(self):
            color = self.combo.current_text
            self.color_window = ColorDisplay(color)
            self.color_window.show()
            self.color_display.set_text(f"Color: {color}")

    selector = ColorSelector()
    selector.show()

# Task 4



# ////////////////////////////////////

# task collection; uncomment whatever one you want to run

#run_task_1()
run_task_2()
#run_task_3()
#run_task_4()

sys.exit(app.exec())