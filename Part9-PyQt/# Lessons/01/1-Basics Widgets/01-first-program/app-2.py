"""
Supporting command line argument & return code

- A PyQt program may accept one or more command line arguments. To enable this, you need to pass the argv from the sys module to the QApplication like this:

    app = QApplication(sys.argv)

- The app.exec() returns 0 for success or other value for failure.
- If a PyQt program is executed from a Shell i.e., the command prompt on Windows or the Terminal on macOS and Linux, it should return a code indicating the program’s success or failure.
- To do this, you call the sys.exit() function and pass the result of the app.exec() to it as follows:

    sys.exit(app.exec())

- By doing this the Shell can receive the return code from the PyQt application.


"""

# The following shows the revised Hello World program:

import sys
from PyQt6.QtWidgets import QApplication, QWidget


# create the QApplication with arguments
app = QApplication(sys.argv)


# create the main window
window = QWidget(windowTitle="Hello World")
window.show()


# start the event loop
sys.exit(app.exec())
