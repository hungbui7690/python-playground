"""
TKINTER SCROLLBAR

Introduction to the Tkinter scrollbar widget

- A scrollbar allows you to view all parts of another widget whose content is typically larger than the available space.
- Tkinter scrollbar widget is not a part of any other widgets such as Text and Listbox. Instead, a scrollbar is an independent widget.

- To use the scrollbar widget, you need to:

    First, create a scrollbar widget.
    Second, link the scrollbar with a scrollable widget.

- The following shows how to create a scrollbar widget using the ttk.Scrollbar constructor:

    scrollbar = ttk.Scrollbar(
        container,
        orient='vertical',
        command=widget.yview
    )

- In this syntax:

    The container is the window or frame on which the scrollbar locates.
    The orient argument specifies whether the scrollbar needs to scroll horizontally or vertically.
    The command argument allows the scrollbar widget to communicate with the scrollable widget.

- The scrollable widget also needs to communicate back to the scrollbar about the percentage of the entire content area that is currently visible.

- Every scrollable widget has a yscrollcommand and/or xscrollcommand options. And you can assign the scrollbar.set method to it:

    widget['yscrollcommand'] = scrollbar.set

"""


# The Text widgets are one of several types of scrollable widgets. The following program illustrates a simple user interface that consists of Text and Scrollbar widgets:

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.resizable(False, False)
root.title("Scrollbar Widget Example")


# apply the grid layout
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)


# create the text widget
text = tk.Text(root, height=10)
text.grid(row=0, column=0, sticky=tk.EW)


# create a scrollbar widget and set its command to the text widget
scrollbar = ttk.Scrollbar(root, orient="vertical", command=text.yview)
scrollbar.grid(row=0, column=1, sticky=tk.NS)


#  communicate back to the scrollbar
text["yscrollcommand"] = scrollbar.set


# add sample text to the text widget to show the screen
for i in range(1, 50):
    position = f"{i}.0"
    text.insert(position, f"Line {i}\n")


root.mainloop()


# Summary
# Create a scrollbar with ttk.Scrollbar(orient, command)
# The orient can be 'vertical' or 'horizontal'
# The command can be yview or xview property of the scrollable widget that links to the scrollbar.
# Set the yscrollcommand property of the scrollable widget so it links to the scrollbar.
