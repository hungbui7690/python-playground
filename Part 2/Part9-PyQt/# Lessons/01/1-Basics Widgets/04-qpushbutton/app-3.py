"""
QPUSHBUTTON

Creating a toggle button

- The QPushButton class has the checkable property that allows you to use the button as a toggle button.
- A toggle button has an on/off state. If the button is on, the checked button is true. Otherwise, it is false.
- For a toggle button, the clicked signal sends the status of the button, either on or off.

"""

#

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("PyQt QPushButton Widget")
        self.setGeometry(100, 100, 320, 210)

        button = QPushButton("Toggle Me")
        button.setCheckable(True)
        button.clicked.connect(self.on_toggle)

        # place the button on the window
        layout = QVBoxLayout()
        layout.addWidget(button)
        self.setLayout(layout)

        # show the window
        self.show()

    def on_toggle(self, checked):
        print(checked)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # create the main window
    window = MainWindow()

    # start the event loop
    sys.exit(app.exec())
