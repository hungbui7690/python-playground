"""
QHBOXLAYOUT

Alignments
- When the parent widget has more space for child widgets, the child widgets will stretch horizontally like this: pic-1
- To keep the child widgets at their default sizes and align them horizontally, you use a horizontal spacer.

\\\\\\\\\\\\\\

Align left

- To align the button to the left of the parent widget, you add a horizontal spacer after the child widgets to the QHBoxLayout. For example: pic-2

In this example, the horizontal spacer with stretch to the end of the layout and left enough space for the buttons.

"""


# To add a horizontal spacer to the end of the layout, you call the addStretch() method after adding all buttons to the layout:

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("PyQt QHBoxLayout")

        # create a layout
        layout = QHBoxLayout()
        self.setLayout(layout)

        # create buttons and add them to the layout
        titles = ["Yes", "No", "Cancel"]
        buttons = [QPushButton(title) for title in titles]
        for button in buttons:
            layout.addWidget(button)

        # add a spacer
        layout.addStretch()

        # show the window
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
