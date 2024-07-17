"""
3 Ways to Set Options for a Tk Themed Widget


"""

# 3) Using the config() method with keyword attributes
# The following program illustrates how to use the config() method to set the text option for the label:

import tkinter as tk
from tkinter import ttk


root = tk.Tk()

label = ttk.Label(root)
label.config(text="Hi, there")
label.pack()

root.mainloop()


# Summary
# Ttk widgets provide you with three ways to set options:
# Use keyword arguments at widget creation.
# Use a dictionary index after widget creation.
# Use the config() method with keyword attributes.
