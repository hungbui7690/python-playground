"""
TKINTER ASKYESNO

\\\\\\\\\\\\\\\\\\\\\



"""


#

# The following is the same program but use the object-oriented programming approach:

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askyesno, askquestion


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Tkinter Yes/No Dialog")
        self.geometry("300x150")

        # Quit button
        quit_button = ttk.Button(self, text="Quit", command=self.confirm)
        quit_button.pack(expand=True)

    def confirm(self):
        answer = askyesno(
            title="Confirmation", message="Are you sure that you want to quit?"
        )
        if answer:
            self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()


# Summary
# Use the Tkinter askyesno() function to show a dialog that asks for user confirmation.
# The askyesno() function returns True if you click the yes button, otherwise, it returns False.
# The askquestion() function returns a string with a value of 'yes' or 'no' instead.
