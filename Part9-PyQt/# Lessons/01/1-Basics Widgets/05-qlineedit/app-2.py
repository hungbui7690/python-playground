"""
QLINEEDIT

- To make the QLineEdit widget a password entry, you set the echoMode to QLineEdit.EchoMode.Password:

    password = QLineEdit(self, echoMode=QLineEdit.EchoMode.Password)

"""


# 2) Using the PyQt QLineEdit to create a password entry
# The following program creates a new QLineEdit widget as a password entry:

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("PyQt QLineEdit Widget")
        self.setGeometry(100, 100, 320, 210)

        password = QLineEdit(self, echoMode=QLineEdit.EchoMode.Password)

        # place the widget on the window
        layout = QVBoxLayout()
        layout.addWidget(password)
        self.setLayout(layout)

        # show the window
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
