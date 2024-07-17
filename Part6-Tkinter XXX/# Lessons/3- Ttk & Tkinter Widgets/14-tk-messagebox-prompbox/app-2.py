"""
TKINTER ASKYESNO

\\\\\\\\\\\\\\\\\\\\\

Introduction to the Tkinter askyesno() function

- Sometimes, you need to ask for user confirmation. For example, if users click the quit button, you want to ask whether they really want to close the application. Or they just accidentally do so:
Tkinter askyesno

- To show a dialog that asks for user confirmation, you use the askyesno() function.
- The dialog will have a title, a message, and two buttons (yes and no).
- When you click the yes button, the function returns True. However, if you click the no button, it returns False.
- The following shows the syntax of the askyesno() function:

    answer = askyesno(title, message, **options)

- Note that the answer is a Boolean value, either True or False.
- Tkinter also has another function called askquestion(), which is similar to the askyesno() function except that it returns a string with a value of 'yes' or 'no':

    answer = askquestion(title, message, **options)

"""


#

# If you click the yes button, the application will be closed. Otherwise, it’ll stay.

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askyesno

# create the root window
root = tk.Tk()
root.title("Tkinter Yes/No Dialog")
root.geometry("300x150")


# click event handler
def confirm():
    answer = askyesno(
        title="confirmation", message="Are you sure that you want to quit?"
    )
    if answer:
        root.destroy()


ttk.Button(root, text="Ask Yes/No", command=confirm).pack(expand=True)


# start the app
root.mainloop()
