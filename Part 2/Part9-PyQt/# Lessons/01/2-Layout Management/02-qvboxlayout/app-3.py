"""
QVBOXLAYOUT

Align top

Similarly, you can add a vertical spacer as the last item of the layout to push the buttons to the top by calling the addStretch() method after adding the buttons to the layout: pic-5

"""

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("PyQt QVBoxLayout")

        # create a layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        # create buttons and add them to the layout
        titles = ["Find Next", "Find All", "Close"]
        buttons = [QPushButton(title) for title in titles]
        for button in buttons:
            layout.addWidget(button)

        # add a spacer
        layout.addStretch()

        # show the window
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
