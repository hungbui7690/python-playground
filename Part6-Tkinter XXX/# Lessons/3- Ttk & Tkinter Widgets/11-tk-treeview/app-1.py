"""
TKINTER TREEVIEW

\\\\\\\\\\\\\\\\\\\\\

Introduction to the Tkinter Treeview widget

- A Treeview widget allows you to display data in both tabular and hierarchical structures. To create a Treeview widget, you use the ttk.Treeview class:

    tree = ttk.Treeview(container, **options)

- A Treeview widget holds a list of items. Each item has one or more columns.
- The first column may contain text and an icon that indicates whether it can be expansible or not. The remaining columns contain values of each row.
- The first row of the Treeview consists of headings that identify each column by a name.

\\\\\\\\\\\\\\\\\\\\

    ~~ tree = ttk.Treeview(root, columns=columns, show='headings')

- In this code, we passed the columns to the columns option. The show='heading' hides the first column (column #0) of the Treeview.
- The show option accepts one of the following values:

    'tree' – shows the column #0.
    'heading' – shows the header row.
    'tree headings' – shows both column #0 and the header row. This is the default value.
    '' – doesn’t show the column #0 or the header row.

"""

# The following program shows how to use the Treeview widget to display tabular data:

# (1) import tkinter module, ttk submodule, and the showinfo from tkinter.messagebox:
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


# (2) create the root window, set its title and size:
root = tk.Tk()
root.title("Treeview demo")
root.geometry("620x200")


# (3) define identifiers for columns:
columns = ("first_name", "last_name", "email")


# (4) create a Tkinter’s Treeview widget:
tree = ttk.Treeview(root, columns=columns, show="headings")


# (5) specify the headings for the columns:
tree.heading("first_name", text="First Name")
tree.heading("last_name", text="Last Name")
tree.heading("email", text="Email")


# (6) generate a list of tuples for displaying on the Treeview:
contacts = []
for n in range(1, 100):
    contacts.append((f"first {n}", f"last {n}", f"email{n}@example.com"))


# (7) create new items, one by one, by using the insert() method of the Treeview widget:
for contact in contacts:
    tree.insert("", tk.END, values=contact)


# (8) define a function to handle the <> event. When you select one or more items, the program will show a message box:
def item_selected(event):
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = item["values"]
        # show a message
        showinfo(title="Information", message=",".join(record))


tree.bind("<<TreeviewSelect>>", item_selected)


# (9) place the Treeview widget on the root window:
tree.grid(row=0, column=0, sticky="nsew")


# (10) add a vertical scrollbar to the Treeview widget:
scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky="ns")


root.mainloop()
