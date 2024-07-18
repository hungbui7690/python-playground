"""
QVBOXLAYOUT

Alignments

- The QVBoxLayout stretches each widget type in a specific way. For example, the QVBoxLayout stretches the QPushButton horizontally, not vertically.
- It means that when you increase the width of the parent widget, the widths of all the buttons also increase: pic-2
- However, when you increase the height of the parent widget, the heights of the buttons don’t change. More importantly, the QVBoxLayout allocates evenly the spaces of the parent widget to each button: pic-3
- When the parent widget has more space for the child widgets, you can align the child widgets within the parent widget using vertical spacers.

\\\\\\\\\\\\\\\\\

Align bottom

To push the buttons to the bottom of the parent widget, you add a vertical spacer at the beginning of the layout by using the addStretch() method of the QVBoxLayout object: pic-4

"""

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


# If you increase the height of the window, the vertical spacer will stretch to the end of the QVBoxLayout and leaves enough spaces for the buttons:


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("PyQt QVBoxLayout")

        # create a layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        # @@ add a spacer
        layout.addStretch()

        # create buttons and add them to the layout
        titles = ["Find Next", "Find All", "Close"]
        buttons = [QPushButton(title) for title in titles]
        for button in buttons:
            layout.addWidget(button)

        # show the window
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
