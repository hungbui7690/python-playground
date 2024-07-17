"""
TKINTER ASKOKCANCEL

\\\\\\\\\\\\\\\\\\\\\

Introduction to the Tkinter askokcancel() function

- The askokcancel() function shows a confirmation dialog that has two buttons: OK and Cancel.

    answer = askokcancel(title, message, **options)

- If you click the OK button, the function returns True. However, if you click the Cancel button, the function returns False.

"""

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askokcancel, showinfo, WARNING

# create the root window
root = tk.Tk()
root.title("Tkinter Ok/Cancel Dialog")
root.geometry("300x150")

# click event handler


def confirm():
    answer = askokcancel(
        title="Confirmation", message="Deleting will delete all the data.", icon=WARNING
    )

    if answer:
        showinfo(title="Deletion Status", message="The data is deleted successfully")


ttk.Button(root, text="Delete All", command=confirm).pack(expand=True)


# start the app
root.mainloop()
