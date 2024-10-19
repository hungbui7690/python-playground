"""
QPUSHBUTTON

Creating a push button with an icon

- To create a button with an icon, you use the following steps:

  + First, import QIcon from PyQt6.QtGui module:

        @@ from PyQt6.QtGui import QIcon

  + Second, create a QPushButton object:

        @@ button = QPushButton('Delete')

  + Third, add the icon of the button by calling the setIcon() method of the QPushButton with the QIcon object:

        @@ button.setIcon(QIcon('trash.png'))
        > - Note that the QIcon object accepts a path to the icon file.

- To make the button nicer, you can set its size by calling setFixedSize() method.
- The size is determined by the QSize object with two arguments width and height. Note that you need to import QSize class from PyQt6.QtCore module.

"""

#

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("PyQt QPushButton Widget")
        self.setGeometry(100, 100, 320, 210)

        button = QPushButton("Delete")
        button.setIcon(QIcon("./playground/trash.png"))

        button.setFixedSize(QSize(100, 30))

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
