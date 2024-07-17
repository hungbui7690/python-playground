"""
COMMAND BINDING

Introduction to Tkinter command binding

- To make the application more interactive, the widgets need to respond to the events such as:

    Mouse clicks
    Key presses

- This requires assigning a callback function to a specific event. When the event occurs, the callback will be invoked automatically to handle the event.

- In Tkinter, some widgets allow you to associate a callback function with an event using the command binding.

- It means that you can assign the name of a function to the command option of the widget so that when the event occurs on the widget, the function will be called automatically.

- To use the command binding, you follow these steps:

    First, define a function as a callback.
    Then, assign the name of the function to the command option of the widget.

- For example, the following defines a function called button_clicked():

    def button_clicked():
        print('Button clicked')

- After that, you can associate the function with the command option of a button widget:

    ttk.Button(root, text='Click Me',command=button_clicked)

- Note that you pass the callback without parentheses () within the command option. Otherwise, the callback would be called as soon as the program runs.

"""

# The following is the full program that illustrates how to associate the button_clicked callback function with the Button widget:

import tkinter as tk
from tkinter import ttk

root = tk.Tk()


def button_clicked():
    print("Button clicked")


button = ttk.Button(root, text="Click Me", command=button_clicked)
button.pack()

root.mainloop()
