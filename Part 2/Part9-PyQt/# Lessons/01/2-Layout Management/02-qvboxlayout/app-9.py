"""
QVBOXLAYOUT

Setting content margins

- By default, the QVBoxLayout sets specific left, top, right, and bottom margins for a widget. To change the margins, you use the setContentsMargins() method:

    @@ setContentsMargins(self, left: int, top: int, right: int, bottom: int) -> None

- For example, the following uses the setContentsMargins() method to set the margins for QLabel widgets to zero

\\\\\\\\\\\\\\\\\\\\\\

Summary

- Use PyQt QVBoxLayout to divide the parent widget into vertical boxes and place the child widgets sequentially from top to bottom.
- Use the addStretch() method of the QVBoxLayout object to add a vertical spacer to the layout to align widgets at the top, bottom, or center.
- Use the setStretchFactor() method of the QVBoxLayout object to set a stretch factor for a widget in the layout.
- Use the setSpacing() method of the QVBoxLayout object to set the spaces between child widgets.
- Use the setContentsMargins() method of the QVBoxLayout object to set the left, top, right, and bottom margins of the contents.

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

        # @@ set the contents margins
        layout.setContentsMargins(0, 0, 0, 0)

        # show the window
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
