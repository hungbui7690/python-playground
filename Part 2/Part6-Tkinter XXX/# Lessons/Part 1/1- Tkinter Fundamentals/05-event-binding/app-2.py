"""
EVENT BINDING


"""

# The following example illustrates how to use the bind() method to register multiple handlers for the same event:
# When you move the focus to the button and press the Return key, Tkinter automatically invokes the return_pressed and log functions.

import tkinter as tk
from tkinter import ttk


def return_pressed(event):
    print("Return key pressed.")


def log(event):
    print(event)


root = tk.Tk()

btn = ttk.Button(root, text="Save")
btn.bind("<Return>", return_pressed)


# The following binds the log() function to the Return key pressed event of the 'Save' button:
btn.bind("<Return>", log, add="+")
# In this statement, the third argument add='+' registered additional handler, which is the log() function.
# If you don’t specify the add='+' argument, the bind() method will replace the existing handler (return_pressed) by the new one (log).


btn.focus()
btn.pack(expand=True)

root.mainloop()
