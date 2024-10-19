"""
TKINTER SIZEGRIP

\\\\\\\\\\\\\\\\\\\\\

Introduction to the Tkinter Sizegrip widget

- The Sizegrip widget typically locates in the bottom right corner of the window. It allows you to resize the enter application window

- To create a Sizegrip widget, you use the following syntax:

    ttk.Sizegrip(parent, **option)

- To make sure the Sizegrip widget works properly, you need to make the root window resizable.
- If you use the grid geometry manager, you need to configure column and row sizes.

"""

#

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Sizegrip Demo")
root.geometry("300x200")


# (1) make sure the root window resizable:
root.resizable(True, True)

# (2) configure the grid layout:
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# (3) create a Sizegrip widget:
sg = ttk.Sizegrip(root)
sg.grid(row=1, sticky=tk.SE)


root.mainloop()
