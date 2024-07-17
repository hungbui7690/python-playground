"""
TKINTER ASKOKCANCEL

\\\\\\\\\\\\\\\\\\\\\


"""


# The following program does the same as the program above but use the object-oriented programming approach:

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askokcancel, showinfo, WARNING


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Tkinter Ok/Cancel Dialog")
        self.geometry("300x150")

        delete_button = ttk.Button(self, text="Delete All", command=self.confirm)

        delete_button.pack(expand=True)

    def confirm(self):
        answer = askokcancel(
            title="Confirmation",
            message="Deleting will delete all the data.",
            icon=WARNING,
        )

        if answer:
            showinfo(
                title="Deletion Status", message="The data is deleted successfully"
            )


if __name__ == "__main__":
    app = App()
    app.mainloop()


# Summary
# Use the Tkinter askokcancel() function to display a confirmation dialog with two buttons OK and Cancel.
# The askokcancel() function returns True if you click the OK button and False if you click the Cancel button.
