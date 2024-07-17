"""
TKINTER CANVAS

\\\\\\\\\\\\\\\\\\\\\

Introduction to the Tkinter canvas widget

- The canvas widget is the most flexible widget in Tkinter. The Canvas widget allows you to build anything from custom widgets to complete user interfaces.
- The canvas widget is a blank area on which you can draw figures, create text, and place images.

- A canvas has a coordinate system like a window. The origin (0,0) is at the top-left corner. The direction of the x-axis is from left to right and the direction of the y-axis is from top to bottom.

"""

# To create a canvas widget, you create a new instance of the Canvas class from the tkinter module. For example, the following creates a canvas on a window:

import tkinter as tk


root = tk.Tk()
root.geometry("800x600")
root.title("Canvas Demo")


# First, create a new Canvas object with the width 600px, height 400px and background white:
canvas = tk.Canvas(root, width=600, height=400, bg="white")

# Second, place the canvas object on the root window using the pack() geometry.
canvas.pack(anchor=tk.CENTER, expand=True)


root.mainloop()
