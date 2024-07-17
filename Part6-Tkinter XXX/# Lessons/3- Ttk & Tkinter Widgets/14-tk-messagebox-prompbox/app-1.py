"""
TKINTER MESSAGEBOX

\\\\\\\\\\\\\\\\\\\\\

Introduction to tkinter.messagebox module

- When developing a Tkinter application, you often want to notify users about the events that occurred.
- For example, when users click the save button, you want to notify them that the record has been saved successfully.
- If an error occurred, for example, the database server is not reachable, you can notify users of the error.

- When the update has been completed but the record already exists, you may want to show a warning.
- To cover all of these scenarios, you can use various functions from the tkinter.messagebox module:

    showinfo() – notify that an operation completed successfully.
    showerror() – notify that an operation hasn’t completed due to an error.
    showwarrning() – notify that an operation completed but something didn’t behave as expected.

- All of these functions accept two arguments:

    showinfo(title, message)
    showerror(title, message)
    showwarrning(title, message)

    + The title is displayed on the title bar of the dialog.
    + The message is shown on the dialog.


- To span the message multiple lines, you can add the new line character '\n'.

\\\\\\\\\\\\\\\\\\\\\\\\

Tkinter messagebox examples

- The following program consists of three buttons. When you click a button, the corresponding message box will display. 
- pic

"""


#

# (1) import the tkinter, tkinter.ttk, and tkinter.messagebox modules:
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo


# (2) create the root window and initialize its properties:
root = tk.Tk()
root.title("Tkinter MessageBox")
root.resizable(False, False)
root.geometry("300x150")


options = {"fill": "both", "padx": 10, "pady": 10, "ipadx": 5}


# (3) create three buttons and assign a lambda expression to the command option of each button. Each lambda expression shows a corresponding message box.
ttk.Button(
    root,
    text="Show an error message",
    command=lambda: showerror(title="Error", message="This is an error message."),
).pack(**options)

ttk.Button(
    root,
    text="Show an information message",
    command=lambda: showinfo(
        title="Information", message="This is an information message."
    ),
).pack(**options)


ttk.Button(
    root,
    text="Show an warning message",
    command=lambda: showwarning(title="Warning", message="This is a warning message."),
).pack(**options)


# run the app
root.mainloop()
