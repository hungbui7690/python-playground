"""
TKINTER WINDOW

\\\\\\\\\\\\\\\\\

Window stacking order

- The window stack order refers to the order of windows placed on the screen from bottom to top. The closer window is on the top of the stack and it overlaps the one lower.

- To ensure that a window is always at the top of the stacking order, you can use the -topmost attribute like this:

    root.attributes('-topmost', 1)

- To move a window up or down of the stack, you can use the lift() and lower() methods:

    root.lift()
    root.lift(another_window)

    root.lower()
    root.lower(another_window)

"""


# The following example places the root window on top of all other windows. In other words, the root window is always on top:

import tkinter as tk


root = tk.Tk()
root.title("Tkinter Window Demo")
root.geometry("300x200+50+50")
root.resizable(0, 0)
root.attributes("-topmost", 1)

root.mainloop()
