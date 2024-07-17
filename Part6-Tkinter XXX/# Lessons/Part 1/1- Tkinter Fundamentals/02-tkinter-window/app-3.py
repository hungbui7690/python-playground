"""
TKINTER WINDOW

\\\\\\\\\\\\\\\\\

Resizing behavior

- By default, you can resize the width and height of a window. To prevent the window from resizing, you can use the resizable() method:

    window.resizable(width,height)

- The resizable() method has two parameters that specify whether the width and height of the window can be resizable.

- When a window is resizable, you can specify the minimum and maximum sizes using the minsize() and maxsize() methods:

    root.minsize(min_width, min_height)
    root.maxsize(min_height, max_height)

"""

import tkinter as tk


root = tk.Tk()
root.title("Tkinter Window Demo")
root.geometry("600x400+50+50")


# The following shows how to make the window with a fixed size:
root.resizable(True, True)


# When a window is resizable, you can specify the minimum and maximum sizes using the minsize() and maxsize() methods:
root.minsize(300, 300)


root.mainloop()
