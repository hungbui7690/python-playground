"""
QHBOXLAYOUT

Setting content margins

- By default, the QHBoxLayout sets specific left, top, right, and bottom margins for child widgets. To change the margins, you use the setContentsMargins() method: pic-8

    @@ setContentsMargins(self, left: int, top: int, right: int, bottom: int) -> None

\\\\\\\\\\\\\\\\\\

Summary

- Use QHBoxLayout to divide the parent widget into horizontal boxes and place them sequentially from left to right.
- Use the addStretch() method of the QHBoxLayout object to add a horizontal spacer to the layout to align the child widgets left, right, or center.
- Use the setStretchFactor() method of the QHBoxLayout object to set the stretch factor for a child widget.
- Use the setSpacing() method of the QHBoxLayout object to set the spaces between child widgets.
- Use the setContentsMargins() method of the QHBoxLayout object to set the left, top, right, and bottom margins.


"""


# The following example uses the setContentsMargins() to set the left, top, right, and bottom margins for the child widgets:

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("PyQt QHBoxLayout")

        # create a layout
        layout = QHBoxLayout()
        self.setLayout(layout)

        # create buttons and add them to the layout
        titles = ["Yes", "No", "Cancel"]
        buttons = [QPushButton(title) for title in titles]
        for button in buttons:
            layout.addWidget(button)

        layout.setContentsMargins(50, 50, 50, 50)  # @@

        # show the window
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
