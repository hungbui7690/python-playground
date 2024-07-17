"""
TKINTER LABELFRAME

\\\\\\\\\\\\\\\\\\\\\

Introduction to the Tkinter LabelFrame

- Tkinter LabelFrame widget is a container that contains other related widgets. For example, you can group Radiobutton widgets and place the group on a LabelFrame.

- To create a LabelFrame widget, you use the ttk.LabelFrame:

    lf = ttk.LabelFrame(container, **option)

- In this syntax, you specify the parent component (container) of the LabelFrame and one or more options. A notable option is text which specifies a label for the LabelFrame.

"""

#

import tkinter as tk
from tkinter import ttk


# root window
root = tk.Tk()


# configure the root window
root.geometry("300x200")
root.resizable(False, False)
root.title("LabelFrame Demo")


# (1) create a LabelFrame widget and use the grid geometry manager to manage its layout:
lf = ttk.LabelFrame(root, text="Alignment")
lf.grid(column=0, row=0, padx=20, pady=20)

alignment_var = tk.StringVar()
alignments = ("Left", "Center", "Right")


# (2) create the three radio button widgets based on the alignments list and place them on the label frame widget:
grid_column = 0
for alignment in alignments:
    # create a radio button
    radio = ttk.Radiobutton(lf, text=alignment, value=alignment, variable=alignment_var)
    radio.grid(column=grid_column, row=0, ipadx=10, ipady=10)
    # grid column
    grid_column += 1


root.mainloop()
