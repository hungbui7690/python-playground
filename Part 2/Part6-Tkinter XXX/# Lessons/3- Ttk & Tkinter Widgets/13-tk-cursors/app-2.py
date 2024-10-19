"""
TKINTER CURSORS

\\\\\\\\\\\\\\\\\\\\\

Changing the cursor for the root window

- The root window has only two cursors:

    Normal cursor
    Busy cursor

- The Normal cursor has the value of "" while the busy cursor has the value of "watch".

"""


# If you want to change the cursor for an area of the root window, you can use the <Motion> event and track the x (and/or y) coordinate of the cursor. For example:

import tkinter as tk

root = tk.Tk()
root.geometry("300x300")


def change_cursor(event):
    if event.x in range(100, 300):
        root.config(cursor="watch")
    else:
        root.config(cursor="")


root.bind("<Motion>", change_cursor)
root.mainloop()


# In this example, the cursor changes to busy when the mouse is starting on the x-coordinates from 100 to 300.
