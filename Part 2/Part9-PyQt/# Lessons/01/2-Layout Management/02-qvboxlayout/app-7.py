"""
QVBOXLAYOUT

- To allocate spaces for each QLabel widget proportionally, you use the setStretchFactor() method with the following syntax:

    @@ setStretchFactor(widget, factor)

- The setStretchFactor() method sets a stretch factor for the widget to stretch within the layout. Therefore, you need to setStretchFactor() method after adding the child widgets to the layout.

- The following program uses the setStretchFactor() method to set the stretch factors for the first, second, and third QLabel widgets as 1, 2, and 3:

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

        # @@ Because of the stretch factors, the second QLabel widget takes twice as much space as the first one and the third QLabel widget uses space that is three times bigger than the first one.
        layout.setStretchFactor(label_1, 1)
        layout.setStretchFactor(label_2, 2)
        layout.setStretchFactor(label_3, 3)

        # show the window
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
