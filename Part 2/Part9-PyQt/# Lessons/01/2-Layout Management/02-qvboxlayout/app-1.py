"""
QVBOXLAYOUT
- The QVBoxLayout divides the parent widget into vertical boxes and places the child widgets sequentially from top to bottom.


"""


# This program illustrates how to use the QVBoxLayout class:

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("PyQt QVBoxLayout")

        # (1) create a QVBoxLayout object:
        layout = QVBoxLayout()

        # (2) Next, set the layout for the MainWindow by calling its setLayout() method:
        self.setLayout(layout)

        # (3) Then, define a list of three strings that represent button titles:
        titles = ["Find Next", "Find All", "Close"]

        # (4) After that, create three buttons (QPushButton) from the list titles using a list comprehension:
        buttons = [QPushButton(title) for title in titles]

        # (5) Finally, add the buttons to the layout using a for loop:
        for button in buttons:
            layout.addWidget(button)

        # show the window
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
