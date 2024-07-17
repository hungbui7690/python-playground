"""
TKINTER TREEVIEW

\\\\\\\\\\\\\\\\\\\\\

Adding an item to the Treeview widget

- To add an item (or a row) to a Treeview widget, you use the insert() method of the Treeview widget object. The following example adds an item at the end of the item list:

    tree.insert('', tk.END, values=contact)

- To add an item at the beginning of the list, you use zero (0) instead of tk.END constant:

    tree.insert('', 0, values=contact)

"""

# The following program illustrates how to add items to the Treeview:

import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Treeview demo")
        self.geometry("620x200")

        self.tree = self.create_tree_widget()

    def create_tree_widget(self):
        columns = ("first_name", "last_name", "email")
        tree = ttk.Treeview(self, columns=columns, show="headings")

        # define headings
        tree.heading("first_name", text="First Name")
        tree.heading("last_name", text="Last Name")
        tree.heading("email", text="Email")

        tree.grid(row=0, column=0, sticky=tk.NSEW)

        # adding an item
        tree.insert("", tk.END, values=("John", "Doe", "john.doe@email.com"))

        # insert a the end
        tree.insert("", tk.END, values=("Jane", "Miller", "jane.miller@email.com"))

        # insert at the beginning
        tree.insert("", 0, values=("Alice", "Garcia", "alice.garcia@email.com"))

        return tree


if __name__ == "__main__":
    app = App()
    app.mainloop()
