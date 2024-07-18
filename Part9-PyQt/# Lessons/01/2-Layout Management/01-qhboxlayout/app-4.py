"""
QHBOXLAYOUT

Align center

To align buttons to the center, you add one horizontal spacer at the beginning and the other at the end of the layout: pic-4

"""


# To do that you call addStretch() method before and after adding buttons to the layout:

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("PyQt QHBoxLayout")

        # create a layout
        layout = QHBoxLayout()
        self.setLayout(layout)

        # @@ add a spacer
        layout.addStretch()

        # create buttons and add them to the layout
        titles = ["Yes", "No", "Cancel"]
        buttons = [QPushButton(title) for title in titles]
        for button in buttons:
            layout.addWidget(button)

        # @@ add a spacer
        layout.addStretch()

        # show the window
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
