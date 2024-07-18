"""
SIGNALS & SLOTS

Introduction to the PyQT signals and slots

- Typically, a Python script runs from the top to the bottom as follows:

    Get inputs.
    Process the inputs to produce outputs.
    Write the outputs to the screen or a file.

- This is called procedure programming.

- When you create a GUI program, you use event-driven programming instead. In the event-driven programming paradigm, a program has the following flow:

    Create widgets like labels, line edits, and buttons.
    Start an event loop that waits for events.
    Respond to events when they occur by executing callables.

- Note that a callable is a function, a method, or an object that implements the __call__() method.

- To connect events with callables of the program, PyQt uses the signals and slots mechanism.

\\\\\\\\\\\\\\\\\\

Signals

  A signal is a special property of an object that is emitted when an event occurs. An event may be a user action, a timeout, or the completion of an asynchronous operation.

\\\\\\\\\\\\\\\\\\

Slots

  A slot is a callable that can receive a signal and respond to it.

  To respond to events, you connect signals to slots. When you connect a signal to a slot, the slot will be executed when the signal is emitted.

  In PyQt, all subclasses of the QObject class can send and receive signals. Almost all classes in PyQt are subclasses of the QObject class.

"""

# The following program displays a window that has a button. When you click the button, the program shows the clicked message in the console:

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # set the window title
        self.setWindowTitle("Qt Signals & Slots")

        # (1) create a button widget and connect its clicked signal
        # to a method
        button = QPushButton("Click me")

        # (2) connect the clicked signal to the on_clicked method (slot):
        # Method 1
        button.clicked.connect(self.button_clicked)

        # Method 2: Also, you can connect a signal to a slot when passing a slot to a signal as a keyword argument. For example:
        # button = QPushButton('Click me', clicked=self.button_clicked)

        # Note that the following code places the button on the window using the vertical box layout. And you’ll learn more about it in the upcoming tutorial.
        layout = QVBoxLayout()
        self.setLayout(layout)
        layout.addWidget(button)

        # show the window
        self.show()

    # (3) define a method on_clicked that prints the clicked message to the terminal:
    # When you click the button, the QPushButton emits the clicked signal that executes the connected slot on_clicked.
    def button_clicked(self):
        print("clicked")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # create the main window and display it
    window = MainWindow()

    # start the event loop
    sys.exit(app.exec())
