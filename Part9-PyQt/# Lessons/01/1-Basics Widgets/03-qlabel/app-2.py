"""
QLABEL

Using the PyQt QLabel widget to display an image
- To display an image using the QLabel widget, you do the following steps:

  + First, import QPixmap from PyQt6.QtGui module:

      @@ from PyQt6.QtGui import QPixmap

  + Second, create a new QPixmap widget with a path to an image file:

      @@ pixmap = QPixmap('python-logo.svg')

      > Note that the python-logo.svg file must be in the same directory as the python program

  + Third, create a QLabel widget and call the setPixmap() method to display the image:

      @@ label = QLabel()
      @@ label.setPixmap(pixmap)

"""

# The following program shows how to display an image using a QLabel widget:

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QPixmap


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("PyQt Label Widget")
        self.setGeometry(100, 100, 320, 210)

        label = QLabel()
        pixmap = QPixmap("./playground/python-tutorial.png")
        label.setPixmap(pixmap)

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
