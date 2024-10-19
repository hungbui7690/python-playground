"""
SIGNALS & SLOTS

Using signals that send data

- A signal may carry data that provides the state of the object when the event occurs. For example, the textChanged signal of the QLineEdit has the text entered in the widget.
- If a signal carries data, the connected slot can receive it.

"""

# The following program shows QLineEdit and QLabel widgets. When you type something on the QLineEdit, the QLabel will display it accordingly:

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("Qt Signals & Slots")

        # (1) create a QLabel widget. The QLabel widget has the setText() method that sets its contents.
        label = QLabel()

        # (2) create a new QLineEdit widget:
        line_edit = QLineEdit()

        # (3) connect the textChanged signal to the setText method of the QLabel object:
        line_edit.textChanged.connect(label.setText)

        # place the widgets
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(line_edit)
        self.setLayout(layout)

        # show the window
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())


"""
When you type something on the QLineEdit:

    The textChanged signal sends the text
    The QLabel receives the text and passes it to the setText() method.

\\\\\\\\\\\\\\\\\\\

Summary

    A signal is a special property of an object that is emitted when an event occurs.
    A slot is a callable that can receive a signal and respond to it accordingly.
    PyQt uses signals and slots to wire up events with callables.

"""
