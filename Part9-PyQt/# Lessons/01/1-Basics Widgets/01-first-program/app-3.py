"""
Creating a Qt program template

"""

# The following illustrates the PyQt Hello World in an object-oriented way

import sys
from PyQt6.QtWidgets import QApplication, QWidget


# First, define the MainWindow class that inherits from the QWidget:
class MainWindow(QWidget):
    # In the __init__() method, we set the widow title and call the show() method to display the window.
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # set the window title
        self.setWindowTitle("Hello World")

        # show the window
        self.show()


# Next, add the if __name__ == ‘__main__’ block to include the code if the program is executed directly. If the script is imported as a module, the code in this block will not be executed.
if __name__ == "__main__":
    # Then, create a QApplication object:
    app = QApplication(sys.argv)

    # After that, create a new instance of the MainWindow:
    window = MainWindow()

    # Finally, start the event loop:
    sys.exit(app.exec())


# Summary
# Each PyQt application has one and only one QApplication object. The QApplication object holds an event loop.
# An event loop manages all events of the PyQt application. It checks the event queue continuously and forwards the events to their handlers.
# Call the app.exec() to start the event loop.
# Use QMainWindow to create the main window for the PyQt application and call the show() method to display the window on the screen.
