"""
TKINTER WINDOW

\\\\\\\\\\\\\\\\\

Changing the default icon

- Tkinter window displays a default icon. To change this default icon, you follow these steps:

    + Prepare an image in the .ico format. If you have the image in other formats like png or jpg, you can convert it to the .ico format. There are many online tools that allow you to do it quite easily.
    + Place the icon in a folder that can be accessible from the program.
    + Call the iconbitmap() method of the window object.

"""


# The following program illustrates how to change the default icon to a new one:

import tkinter as tk


root = tk.Tk()
root.title("Tkinter Window Demo")
root.geometry("300x200+50+50")
root.resizable(False, False)
root.iconbitmap(".\\playground\\icon.ico")

root.mainloop()


"""
Summary
  Use the title() method to change the title of the window.
  Use the geometry() method to change the size and location of the window.
  Use the resizable() method to specify whether a window can be resizable horizontally or vertically.
  Use the window.attributes('-alpha',0.5) to set the transparency for the window.
  Use the window.attributes('-topmost', 1) to make the window always on top.
  Use lift() and lower() methods to move the window up and down of the window stacking order.
  Use the iconbitmap() method to change the default icon of the window.
"""
