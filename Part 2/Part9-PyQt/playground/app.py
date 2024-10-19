"""
QFORMLAYOUT

Introduction to the PyQt QFormLayout

- When creating a data-entry form, you often need to place fields in rows. And on each row, you place a label next to an input widget.
- PyQt provides you with a convenient two-column form that arranges the widgets on a form. The left column has a label and the right column has an input widget.

- To create a form layout, you use QFormLayout class:

  @@ layout = QFormLayout(self)
  @@ self.setLayout(layout) # self is the parent widget

- Adding widgets to the form layout can be done with the addRow() method. For example:

  @@ layout.addRow('Field 1', input_widget1)
  @@ layout.addRow('Field 2', input_widget2)

- The addRow() method takes a string and a widget and automatically creates the QLabel widget for the string.
- If you pass a single widget such as a QLabel, the widget will automatically span both columns. In practice, you can use this feature for creating headings or section labels.

- Besides providing conveniences, QFormLayout adheres to the platform’s look and feel guidelines. For example, when used on macOS labels are right-justified while when used on Windows, labels are left-justified.
- In addition, when displayed on a narrow screen, the layout automatically collapses to a single column with labels above the input widgets.

"""


#

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QFormLayout


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("Sign Up Form")

        layout = QFormLayout()
        self.setLayout(layout)

        layout.addRow("Name:", QLineEdit(self))
        layout.addRow("Email:", QLineEdit(self))
        layout.addRow(
            "Password:", QLineEdit(self, echoMode=QLineEdit.EchoMode.Password)
        )
        layout.addRow(
            "Confirm Password:", QLineEdit(self, echoMode=QLineEdit.EchoMode.Password)
        )
        layout.addRow("Phone:", QLineEdit(self))

        layout.addRow(QPushButton("Sign Up"))

        # show the window
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
