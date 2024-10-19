"""
QHBOXLAYOUT

- PyQt layout defines the way to arrange child widgets on a parent widget. PyQt supports a variety of layout classes, each has a layout strategy that suits a particular situation.
- The steps for using a layout class are as follows:

    First, create a layout object from a layout class.
    Second, assign the layout object to the parent widget’s layout property using the setLayout() method.
    Third, add widgets to the layout using the addWidget() method of the layout object.

- Also, you can add layouts to a layout using the addLayout() method. This allows you to create a more complex layout for arranging widgets.

\\\\\\\\\\\\\\\\\\\\\

Introduction to the PyQt QHBoxLayout

- The QHBoxLayout divides the parent widget into horizontal boxes and places the child widgets sequentially from left to right.

"""


#

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("PyQt QHBoxLayout")

        # (1) create a QHBoxLayout object:
        layout = QHBoxLayout()

        # (2) set the layout for the MainWindow by calling its setLayout() method:
        self.setLayout(layout)

        # (3) create three buttons using QPushButton and add them to the layout using the addWidget() method:
        titles = ["Yes", "No", "Cancel"]
        buttons = [QPushButton(title) for title in titles]
        for button in buttons:
            layout.addWidget(button)

        # show the window
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
