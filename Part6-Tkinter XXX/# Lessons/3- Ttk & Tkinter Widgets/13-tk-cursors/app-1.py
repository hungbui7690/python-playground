"""
TKINTER CURSORS

\\\\\\\\\\\\\\\\\\\\\

Changing the cursor for the root window

- The root window has only two cursors:

    Normal cursor
    Busy cursor

- The Normal cursor has the value of "" while the busy cursor has the value of "watch".

"""


# The following program shows how to change the cursor of the root window from normal to busy:

import tkinter as tk

root = tk.Tk()


root.geometry("300x300")

# change the cursor to busy using the cursor parameter.
root.config(cursor="watch")

root.mainloop()
