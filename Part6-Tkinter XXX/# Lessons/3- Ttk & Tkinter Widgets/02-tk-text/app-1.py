"""
TKINTER TEXT

Introduction to Tkinter Text widget

- The Text widget allows you to display and edit multi-line textarea with various styles. Besides the plain text, the Text widget supports embedded images and links.

- To create a text widget, you use the following syntax:

    text = tk.Text(master, conf={}, **kw)

- In this syntax:

    The master is the parent component of the Text widget.
    The cnf is a dictionary that specifies the widget’s configuration.
    The kw is one or more keyword arguments used to configure the Text widget.

** Note that the Text widget is only available in the Tkinter module, not the Tkinter.ttk module.

"""


# The following example creates a Text widget with eight rows and places it on the root window:

from tkinter import Tk, Text

root = Tk()
root.resizable(False, False)
root.title("Text Widget Example")

text = Text(root, height=8)
text.pack()


root.mainloop()


# In this example, the height argument specifies the number of rows of the Text widget.
