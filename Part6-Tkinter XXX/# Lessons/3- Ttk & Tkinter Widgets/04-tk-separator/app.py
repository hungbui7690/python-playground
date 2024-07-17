"""
TKINTER SEPARATOR

Introduction to the Tkinter Separator widget

- A separator widget places a thin horizontal or vertical rule between groups of widgets.
- To create a separator widget, you use the ttk.Separator constructor like this:

    sep = ttk.Separator(container,orient='horizontal')

- The orient option can be either 'horizontal' or 'vertical'.

"""


# The following example illustrates how to use a separator widget to separate two labels:

import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.geometry("300x200")
root.resizable(False, False)
root.title("Separator Widget Demo")


ttk.Label(root, text="First Label").pack()
separator = ttk.Separator(root, orient="horizontal")
separator.pack(fill="x")
ttk.Label(root, text="Second Label").pack()


root.mainloop()


# Notice that the size of a separator is 1px. Therefore, you need to set the fill or sticky property to adjust its size.


# Summary
# Use a separator widget to place a thin horizontal or vertical rule between groups of widgets.
# Remember to set the fill or sticky property to adjust the size of the separator.
