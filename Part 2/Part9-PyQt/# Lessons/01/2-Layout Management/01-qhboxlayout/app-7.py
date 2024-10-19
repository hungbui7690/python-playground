"""
QHBOXLAYOUT

Setting spaces between widgets

- By default, the QHBoxLayout sets a default space between the child widgets. To change the spaces between them, you use the setSpacing() method of the QHBoxLayout object.

- The following example uses the setSpacing() method to set the spaces between buttons to 50px: pic-7

"""


#

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

        layout.setSpacing(50)  # @@

        # show the window
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
