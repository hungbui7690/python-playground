"""
TKINTER BUTTON

Introduction to Tkinter button widget

- Button widgets represent a clickable item in the applications. Typically, you use a text or an image to display the action that will be performed when clicked.
- Buttons can display text in a single font. However, the text can span multiple lines. On top of that, you can make one of the characters underline to mark a keyboard shortcut.
- To invoke a function or a method of a class automatically when the button is clicked, you assign its command option to the function or method. This is called the command binding in Tkinter.

- To create a button, you use the ttk.Button constructor as follows:

    button = ttk.Button(container, **option)

- A button has many options. However, the typical ones are like this:

    button = ttk.Button(container, text, command)

- In this syntax:

    The container is the parent component on which you place the button.
    The text is the label of the button.
    The command specifies a callback function that will be called automatically when the button clicked.

\\\\\\\\\\\\\\\\\\\\

Command callback

- The command option associates the button’s action with a function or a method of a class. When you click or press the button, it’ll automatically invoke a callback function.

- To assign a callback to the command option, you can use a lambda expression:

    def callback():
        # do something

    ttk.Button(
        root, 
        text="Demo Button", 
        command=callback
    )

- If the function contains one expression, you use a lambba expression:

    ttk.Button(
    root, 
    text="Demo Button", 
    command=lambda_expression
    )

\\\\\\\\\\\\\\\\\\

Button states

- The default state of a button is normal. In the normal state, the button will respond to the mouse events and keyboard presses by invoking the callback function assigned to its command option.
- The button can also have the disabled state. In the disabled state, a button is greyed out and doesn’t respond to the mouse events and keyboard presses.
- To control the state of a button, you use the state() method:

    # set the disabled flag
    button.state(['disabled'])

    # remove the disabled flag
    button.state(['!disabled'])

"""

# 1) Simple Tkinter button example

# The following program shows how to display an Exit button. When you click it, the program is terminated.

import tkinter as tk
from tkinter import ttk

# root window
root = tk.Tk()
root.geometry("300x200")
root.resizable(False, False)
root.title("Button Demo")

# exit button: The command of the button is assigned to a lambda expression that closes the root window.
exit_button = ttk.Button(root, text="Exit", command=lambda: root.quit())

exit_button.pack(ipadx=5, ipady=5, expand=True)

root.mainloop()
