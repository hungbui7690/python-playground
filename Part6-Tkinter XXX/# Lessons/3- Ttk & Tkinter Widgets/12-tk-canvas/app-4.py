"""
TKINTER CANVAS

\\\\\\\\\\\\\\\\\\\\\

Creating an oval

"""


# To draw an oval, you use the create_oval() method. For example:

import tkinter as tk

root = tk.Tk()
root.geometry("800x600")
root.title("Canvas Demo - Oval")

canvas = tk.Canvas(root, width=600, height=400, bg="white")
canvas.pack(anchor=tk.CENTER, expand=True)


points = (
    (50, 150),
    (200, 350),
)
canvas.create_oval(*points, fill="purple")

root.mainloop()


"""
Like a rectangle, an oval takes the coordinate of the upper-left and lower-right corners of its bounding box. A bounding box of an oval is the smallest rectangle that contains the oval.

In this example, the upper-left and lower-right corners of the bounding box are (50,150) and (200,350).
"""
