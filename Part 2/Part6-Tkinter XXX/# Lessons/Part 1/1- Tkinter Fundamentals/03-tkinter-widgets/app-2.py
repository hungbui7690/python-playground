"""
3 Ways to Set Options for a Tk Themed Widget
- When working with themed widgets, you often need to set their attributes e.g., text and image.

- Tkinter allows you to set the options of a widget using one of the following ways:

    At widget creation, using keyword arguments.
    After widget creation, using a dictionary index.
    And use the config() method with keyword attributes.

"""

# 1) Using keyword arguments when creating the widget
# The following illustrates how to use the keyword arguments to set the text option for a label:

import tkinter as tk
from tkinter import ttk


root = tk.Tk()
ttk.Label(root, text="Hi, there").pack()

root.mainloop()
