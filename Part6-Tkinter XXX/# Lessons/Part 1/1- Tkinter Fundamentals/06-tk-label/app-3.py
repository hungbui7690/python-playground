"""
TKINTER LABEL

Setting a specific font for the Label

- To set a particular font for a label, you pass the font keyword argument to the Label constructor like this:

    font = ('font name', font_size)

- The font keyword argument is a tuple that contains font name and size. For example:

    font=("Helvetica", 14)

"""

# The following example shows a label with the Helvetica font:

import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.geometry("300x200")
root.resizable(False, False)
root.title("Label Widget Demo")

# label with a specific font
label = ttk.Label(root, text="A Label with the Helvetica font", font=("Helvetica", 14))

label.pack(ipadx=10, ipady=10)

root.mainloop()
