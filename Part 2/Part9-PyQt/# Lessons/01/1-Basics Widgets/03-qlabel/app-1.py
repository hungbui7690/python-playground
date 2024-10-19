"""
QLABEL

Introduction to the PyQt QLabel Widget

- The QLabel class allows you to create a label widget that displays text, an image, or an animated image (GIF).

- To create a label widget, you follow these steps:

  + First, import the QLabel widget from PyQt6.QtWidgets module:

      @@ from PyQt6.QtWidgets import QLabel

  + Second, create a new instance of the QLabel class:

      @@ label = QLabel('This is QLabel widget')

- In this syntax, you pass a string that you want to display to the QLabel.
- Also, you can use the setText() method to set a text to the QLabel widget after creating the QLabel widget:

      @@ label = QLabel()
      @@ label.setText('This is QLabel widget')

- To get the text of the QLabel() widget, you call the text() method:

      @@ label.text()

- To clear the text of a QLabel widget, you use the clear() method:

      @@ label.clear()

"""

# The following program shows a window that displays a QLabel widget:

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QFont


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("PyQt Label Widget")
        self.setGeometry(100, 100, 320, 210)

        # create a QLabel widget
        label = QLabel("This is a QLabel widget")

        # place the widget on the window
        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)

        # show the window
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # create the main window
    window = MainWindow()

    # start the event loop
    sys.exit(app.exec())
