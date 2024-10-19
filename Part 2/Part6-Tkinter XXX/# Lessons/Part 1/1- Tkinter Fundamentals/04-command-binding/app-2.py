"""
COMMAND BINDING

Tkinter button command arguments

- If you want to pass arguments to a callback function, you can use a lambda expression.

- First, define a function that accepts arguments:

    def callback_function(args):
        # do something

- Then, define a lambda expression and assign it to the command option. Inside the lambda expression, invoke the callback function:

    ttk.Button(
        root,
        text='Button',
        command=lambda: callback(args))

"""

# The following program illustrates how to pass an argument to the callback function associated with the button command:

import tkinter as tk
from tkinter import ttk

root = tk.Tk()


def select(option):
    print(option)


ttk.Button(root, text="Rock", command=lambda: select("Rock")).pack()
ttk.Button(root, text="Paper", command=lambda: select("Paper")).pack()
ttk.Button(root, text="Scissors", command=lambda: select("Scissors")).pack()

root.mainloop()


# When you click a button, the lambda expression bound to the command of that button will execute. It’ll call the select() function and pass a string argument to it.


"""
Limitations of command binding

- First, the command option isn’t available in all widgets. It’s limited to the Button and some other widgets.

- Second, the command button binds to the left-click and the backspace. It doesn’t bind to the Return key.

- To check this you can move focus to a button in the program above and press the backspace and return keys. This is not really user-friendly. Unfortunately, you cannot change the binding of the command function easily.

- To overcome these limitations, Tkinter provides an alternative way for associating a function with an event, which is called event binding.

\\\\\\\\\\\\\\\\\

Summary

- Assign a function name to the command option of a widget is called command binding in Tkinter.
- The assigned function will be invoked automatically when the corresponding event occurs on the widget.
- Only few widgets support the command option.


"""
