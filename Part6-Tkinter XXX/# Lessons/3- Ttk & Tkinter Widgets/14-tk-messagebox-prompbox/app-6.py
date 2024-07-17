"""
TKINTER ASKRETRYCANCEL

\\\\\\\\\\\\\\\\\\\\\

Introduction to the Tkinter askretrycancel() function

- Sometimes, the application performs a task but fails to do so because of an error.
- For example, you may want to connect to a database server. However, the database server is currently not reachable. It may be offline for a short period of time.

- In this case, you can display a confirmation dialog that allow users to reconnect to the database or just keep the application as is.
- To display the Retry/Cancel dialog, you can use the askretrycancel() function:

    answer = askretrycancel(title, message, **options)

- The askretrycancel() function returns True if the Retry button is clicked. If the Cancel button is clicked, it returns False.

"""

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askretrycancel, showinfo

# create the root window
root = tk.Tk()
root.title("Tkinter OK/Retry Dialog")
root.geometry("300x150")


# click event handler
def confirm():
    answer = askretrycancel(
        title="Connection Issue",
        message="The database server is unreachable. Do you want to retry?",
    )
    if answer:
        showinfo(
            title="Information", message="Attempt to connect to the database again."
        )


ttk.Button(root, text="Connect to the Database Server", command=confirm).pack(
    expand=True
)


# start the app
root.mainloop()


# Summary
# Use the askretrycancel() function to display a Retry/Cancel dialog to confirm users to carry an operation again.
# The askretrycancel() function returns True if the Retry button is clicked. If the Cancel button is clicked, it returns False.
