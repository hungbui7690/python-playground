"""
QPUSHBUTTON

Introduction to the PyQt QPushButton widget
- The PyQt QPushButton class allows you to create a button widget, which can be a push button or a toggle button.
- To create a push button, you follow these steps:

  + First, import QPushButton from PyQt6.QtWidgets module:

        @@ from PyQt6.QtWidgets import QPushButton

  + Second, call the QPushButton() with a text that appears on the button:

        @@ button = QPushButton('Click Me')

  + Third, connect the clicked signal to a callable:

        @@ button.clicked.connect(self.on_clicked)

- The on_clicked is a method that executes when the button is clicked.

"""

# The following shows the complete program that displays a button on a window:

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("PyQt QPushButton Widget")
        self.setGeometry(100, 100, 320, 210)

        button = QPushButton("Click Me")

        # place the widget on the window
        layout = QVBoxLayout()
        layout.addWidget(button)
        self.setLayout(layout)

        # show the window
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # create the main window
    window = MainWindow()

    # start the event loop
    sys.exit(app.exec())
