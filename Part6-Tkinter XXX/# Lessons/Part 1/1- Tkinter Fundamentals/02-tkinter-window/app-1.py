"""
Tkinter Window
- The root window has a title that defaults to tk. It also has three system buttons including Minimize, Maximize, and Close.

\\\\\\\\\\\\\\\\

Changing the window title

- To change the window’s title, you use the title() method like this:

    window.title(new_title)

- To get the current title of a window, you use the title() method with no argument:

    title = window.title()

\\\\\\\\\\\\\\\\\\

Changing window size and location

- In Tkinter, the position and size of a window on the screen is determined by geometry.

- The following shows the geometry specification: pic

    widthxheight±x±y

- In this specification:

    The width is the window’s width in pixels.
    The height is the window’s height in pixels.
    The x is the window’s horizontal position. For example, +50 means the left edge of the window should be 50 pixels from the left edge of the screen. And -50 means the right edge of the window should be 50 pixels from the right edge of the screen.
    The y is the window’s vertical position. For example, +50 means the top edge of the window should be 50 pixels below the top of the screen. And -50 means the bottom edge of the window should be 50 pixels above the bottom of the screen.

- To change the size and position of a window, you use the geometry() method:

    window.geometry(new_geometry)

"""

import tkinter as tk


root = tk.Tk()
root.title("Tkinter Window Demo")


# The following example changes the size of the window to 600x400 and the position of the window to 50 pixels from the top and left of the screen:
root.geometry("600x400+50+50")


root.mainloop()
