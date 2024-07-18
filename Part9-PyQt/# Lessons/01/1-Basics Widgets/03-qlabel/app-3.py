"""
QLABEL

Using the PyQt QLabel widget to display an animated image
- To create a movie, you can follow these steps:

  + First, import QMovie from PyQt6.QtGui module:

        @@ from PyQt6.QtGui import QMovie

  + Second, create a QMovie object with a path to the GIF file:

        @@ movie = QMovie('python.gif')

  + Third, create a new QLabel widget:

        @@ label = QLabel(self)

  + Fourth, set the movie to the QLabel widget by calling the setMovie() method:

        @@ label.setMovie(movie)

  + Finally, call the start() method of the QMovie object to show the movie:

        @@ movie.start()

"""

# The following program shows how to display a movie using the QLabel & QMovie widgets:

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QMovie


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("PyQt QLabel Widget")
        self.setGeometry(100, 100, 320, 210)

        label = QLabel()
        movie = QMovie("./playground/giphy.webp")
        label.setMovie(movie)
        movie.start()

        # place the widget on the window
        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)

        # show the window
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # create the main window
    window = MainWindow()

    # start the event loop
    sys.exit(app.exec())
