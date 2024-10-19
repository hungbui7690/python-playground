"""
TKINTER LABEL

Displaying a regular label

"""

# The following program shows how to display a regular label on the root window:

import tkinter as tk
from tkinter.ttk import Label

root = tk.Tk()
root.geometry("300x200")
root.resizable(False, False)
root.title("Label Widget Demo")


# show a label
label = Label(root, text="This is a label")
label.pack(ipadx=10, ipady=10)


root.mainloop()


"""
How it works.

    First, import Label class from the tkinter.ttk module.
    Second, create the root window and set its properties including size, resizable, and title.
    Third, create a new instance of the Label widget, set its container to the root window, and assign a literal string to its text property.
"""
