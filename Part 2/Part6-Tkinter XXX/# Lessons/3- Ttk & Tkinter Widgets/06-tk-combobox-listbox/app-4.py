"""
TKINTER LISTBOX

\\\\\\\\\\\\\\\\\\\\\

Adding a scrollbar to the Listbox


"""

# The following program illustrates how to add a scrollbar to a Listbox:

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# create the root window
root = tk.Tk()

root.title("Listbox")


# create a list box
langs = ("Java", "C#", "C", "C++", "Python", "Go", "JavaScript", "PHP", "Swift")

var = tk.Variable(value=langs)

listbox = tk.Listbox(root, listvariable=var, height=6, selectmode=tk.EXTENDED)

listbox.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)

# link a scrollbar to a list
scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=listbox.yview)

listbox["yscrollcommand"] = scrollbar.set

scrollbar.pack(side=tk.LEFT, expand=True, fill=tk.Y)


def items_selected(event):
    # get selected indices
    selected_indices = listbox.curselection()
    # get selected items
    selected_langs = ",".join([listbox.get(i) for i in selected_indices])
    msg = f"You selected: {selected_langs}"

    showinfo(title="Information", message=msg)


listbox.bind("<<ListboxSelect>>", items_selected)

root.mainloop()


# Summary
# Use the tk.Listbox(container, height, listvariable) to create a Listbox widget; a listvariable should be a tk.StringVar(value=items).
# Bind a callback function to the '<<ListboxSelect>>' event to execute the function when one or more list items are selected.
