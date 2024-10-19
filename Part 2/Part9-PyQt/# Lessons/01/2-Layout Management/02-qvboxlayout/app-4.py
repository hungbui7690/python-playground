"""
QVBOXLAYOUT

Align center

To align the buttons in the center of the parent widget, you add a vertical spacer at the beginning and one at the end of the layout like this: pic-6

"""

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("PyQt QVBoxLayout")

        # create a layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        # @@ add a spacer
        layout.addStretch()

        # create buttons and add them to the layout
        titles = ["Find Next", "Find All", "Close"]
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
