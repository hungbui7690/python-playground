"""
Tkinter Window


"""

import tkinter as tk


# Sometimes, you may want to center the window on the screen. The following program illustrates how to do it:
root = tk.Tk()
root.title("Tkinter Window - Center")

window_width = 300
window_height = 200


# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


# find the center point
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)


# set the position of the window to the center of the screen
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")


root.mainloop()


"""
How it works.

    First, get the screen width and height using the winfo_screenwidth() and winfo_screenheight() methods.
    Second, calculate the center coordinate based on the screen and window width and height.
    Finally, set the geometry for the root window using the geometry() method.

If you want to get the current geometry of a window, you can use the geometry() method without providing any argument:

    window.geometry()
"""
