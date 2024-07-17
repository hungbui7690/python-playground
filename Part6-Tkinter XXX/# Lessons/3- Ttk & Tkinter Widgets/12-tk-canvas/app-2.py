"""
TKINTER CANVAS

\\\\\\\\\\\\\\\\\\\\\

Adding items to a canvas using create_* methods

- A canvas object has a number of add_* methods. These methods allow you to place items on it. The items are:

    Item	    Method
    Line	    create_line()
    Rectangle	create_rectangle()
    Oval	    create_oval()
    Arc	        create_arc()
    Polygon	    create_polygon()
    Text	    create_text(()
    Image	    create_image()

"""

import tkinter as tk


root = tk.Tk()
root.geometry("800x600")
root.title("Canvas Demo")

canvas = tk.Canvas(root, width=600, height=400, bg="white")
canvas.pack(anchor=tk.CENTER, expand=True)

# To create a line, you use the create_line() method. For example, the following creates a red line:
canvas.create_line((50, 50), (100, 100), width=4, fill="red")

root.mainloop()


# In this example, a line consists of two points (50,50) and (100,100). The create_line() method connects the dots between these points.
# The width argument specifies the width of the line. And the fill argument specifies the color of the line.
