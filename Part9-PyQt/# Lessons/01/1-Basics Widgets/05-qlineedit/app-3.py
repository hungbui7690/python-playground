"""
QLINEEDIT

3) Using the PyQt QLineEdit with the auto-complete feature

- To create an entry with the auto-complete feature, you follow these steps:

  + First, import the QCompleter from PyQt6.QtWidgets module.

  + Second, create a QCompleter widget with a list of strings used for autocomplete feature:

      @@ completer = QCompleter(word_list)

  + Third, create a QLineEdit and call its setCompleter() method with the completer object:

      @@ line_edit = QLineEdit(self)
      @@ line_edit.setCompleter(completer)

\\\\\\\\\\\\\\\\\\

Summary

  Use the QLineEdit to create a single-line entry widget.
  Use the echoMode property to change the way the text is displayed.
  Use the QLineEdit widget with a QCompleter widget to support the auto-complete feature.

"""


# For example, the following program shows a QLineEdit widget with an auto-complete feature:

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout, QCompleter


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("PyQt QLineEdit Widget")
        self.setGeometry(100, 100, 320, 210)

        data = [
            "Apple",
            "Apricot",
            "Banana",
            "Carambola",
            "Olive",
            "Oranges",
            "Papaya",
            "Peach",
            "Pineapple",
            "Pomegranate",
            "Rambutan",
            "Ramphal",
            "Raspberries",
            "Rose apple",
            "Starfruit",
            "Strawberries",
            "Water apple",
        ]

        complete = map(lambda x: x.lower(), data)

        common_fruits = QCompleter(complete)
        fruit = QLineEdit(self)
        fruit.setCompleter(common_fruits)

        # place the widget on the window
        layout = QVBoxLayout()
        layout.addWidget(fruit)
        self.setLayout(layout)

        # show the window
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
