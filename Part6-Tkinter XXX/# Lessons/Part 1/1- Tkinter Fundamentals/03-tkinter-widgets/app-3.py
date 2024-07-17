"""
3 Ways to Set Options for a Tk Themed Widget

  + At widget creation, using keyword arguments.
  + After widget creation, using a dictionary index.
  + And use the config() method with keyword attributes.

"""

# 2) Using a dictionary index after widget creation
# The following program shows the same label. However, it uses a dictionary index to set the text option for the Label widget:

import tkinter as tk
from tkinter import ttk


root = tk.Tk()

label = ttk.Label(root)


# The following sets the text options for the label:
label["text"] = "Hi, there"


label.pack()

root.mainloop()
