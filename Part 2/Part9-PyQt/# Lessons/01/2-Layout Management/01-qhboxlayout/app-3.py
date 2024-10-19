"""
QHBOXLAYOUT

Align right

Similarly, you can add a spacer at the beginning of the layout to push the buttons to the right: pic-3

"""


# To do this, you call the addStretch() method before adding buttons to the layout:

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("PyQt QHBoxLayout")

        # create a layout
        layout = QHBoxLayout()
        self.setLayout(layout)

        # add a spacer
        layout.addStretch()

        # create buttons and add them to the layout
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
