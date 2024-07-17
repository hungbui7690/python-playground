"""
EVENT BINDING

Introduction to the Tkinter event binding

- Assigning a function to an event of a widget is called event binding. When the event occurs, the assigned function is invoked automatically.

- In the previous tutorial, you learned how to bind a function to an event of a widget via the command option. However, not all Tkinter widgets support the command option.

- Therefore, Tkinter provides you with an alternative way for event binding via the bind() method. The following shows the general syntax of the bind() method:

    widget.bind(event, handler, add=None)

- When an event occurs in the widget, Tkinter will invoke the handler automatically with the event detail.

- If you want to register an additional handler, you can pass the '+' to the add argument. It means that you can have multiple event handlers that respond to the same event.


"""

# The following program illustrates how to bind the return_pressed function to the Return key pressed event of the 'Save' button:

import tkinter as tk
from tkinter import ttk


def return_pressed(event):
    print("Return key pressed.")


root = tk.Tk()

btn = ttk.Button(root, text="Save")


# In this example, the following statement calls the bind() method on the button widget to bind the Return key pressed event:
btn.bind("<Return>", return_pressed)


btn.focus()
btn.pack(expand=True)

root.mainloop()
