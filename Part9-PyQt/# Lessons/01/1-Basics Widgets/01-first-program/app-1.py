"""
Installing PyQt package

- PyQt is a Python binding for the Qt cross-platform application toolkit. Because PyQt is a third-party package, you need to install it before use.
- PyQt6 is the latest version of PyQt at the time of writing this tutorial. To install PyQt6 using PyPI on Windows, you use the following pip command:

  ~~ pip install PyQt6

- If you use macOS or Linux, you need to use the pip3 command:

  pip3 install PyQt6

\\\\\\\\\\\\\\\\\\\\\\

Creating the first PyQt program
- The following program displays a window with the title Hello World on the screen:


"""

# First, import the QApplication and QMainWidget classes from the PyQt6.Widgets:
from PyQt6.QtWidgets import QApplication, QWidget


# Second, create a QApplication object:
# Each PyQt application needs one and only one QApplication object.
app = QApplication([])


# Third, create a new instance of the QWidget with the title 'Hello World' and call the show() method to display the window:
window = QWidget(windowTitle="Hello World")
window.show()


# Finally, call the exec() method of the QMainApplication instance to start the event loop:
app.exec()


"""
Event loop

- Every PyQt application needs one instance of QApplication class. The QApplication object holds the event loop of the application.
- The event loop is responsible for managing all events of the application including user interactions with the GUI.
- When you interact with the Qt application e.g., by pressing a key or pushing a button, PyQt generates an event and places it on an event queue.
- The event loop continuously checks the event queue. If the event loop finds an event, it’ll forward the event to a specific event handler.
- The event handler processes the event and passes the control back to the event loop for processing the next events.
- The following picture illustrates how the event loop works: pic

** Note that each PyQt application has one and only one event loop.

"""
