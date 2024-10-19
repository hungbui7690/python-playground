"""
QLINEEDIT

Introduction to the PyQt QLineEdit widget
- The PyQt QLineEdit allows you to create a single-line text-entry widget. Typically, you’ll use the QLineEdit in a data-entry form.
- In practice, you often use the QLineEdit widget with a QLabel widget.
- To create a QLineEdit widget, you follow these steps.

  + First, import QLineEdit from PyQt6.QtWidgets module:

        @@ from PyQt6.QtWidgets import QLineEdit

  + Second, create a new QLineEdit object that uses:

        No arguments.
        With only a parent widget.
        Or with a default string value as the first argument.

- For example:

    @@ line_edit = QLineEdit('Default Value', self)

- Also, you can use the following additional properties:

    Property						Type								Description
    text								string							The content of the line edit
    readOnly						Boolean							True or False. If True, the line edit cannot be edited
    clearButtonEnabled	Boolean							True to add a clear button
    placeholderText			string							The text that appears when the line edit is empty
    maxLength						integer							Specify the maximum number of characters that can be entered
    echoMode						QLineEdit.EchoMode	Change the way the text displays e.g., password

"""


# 1) Simple PyQt QLineEdit example
# The following program shows how to create a QLineEdit widget:

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("PyQt QLineEdit Widget")
        self.setGeometry(100, 100, 320, 210)

        search_box = QLineEdit(
            self,
            placeholderText="Enter a keyword to search...",
            clearButtonEnabled=True,
        )

        # place the widget on the window
        layout = QVBoxLayout()
        layout.addWidget(search_box)
        self.setLayout(layout)

        # show the window
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
