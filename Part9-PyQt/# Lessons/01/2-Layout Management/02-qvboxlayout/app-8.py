"""
QVBOXLAYOUT

Setting spaces between widgets

- By default, the QVBoxLayout sets a default space between widgets. To change the spaces between widgets, you use the setSpacing() method.
- The following example uses the setSpacing() method to set the spaces between QLabel widgets to zero:

"""

#

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("PyQt QVBoxLayout")

        # create a layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        # create buttons
        label_1 = QLabel("")
        label_1.setStyleSheet("QLabel{background-color:red}")

        label_2 = QLabel("")
        label_2.setStyleSheet("QLabel{background-color:green}")

        label_3 = QLabel("")
        label_3.setStyleSheet("QLabel{background-color:blue}")

        layout.addWidget(label_1)
        layout.addWidget(label_2)
        layout.addWidget(label_3)

        layout.setSpacing(0)  # @@

        # show the window
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
