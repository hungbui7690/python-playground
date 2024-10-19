"""
TKINTER PACK

6) Using the side option

- The side option specifies the alignment of the widget:

    tkinter.TOP
    tkinter.LEFT
    tkinter.RIGHT
    tkinter.BOTTOM

- They are equivalent to 'left', 'top', 'right', and 'bottom'.

- The side defaults to TOP. In other words, widgets are aligned to the top of their container.

"""

# The following example sets the side for the first widget to tkinter.LEFT :

import tkinter as tk


root = tk.Tk()
root.title("Pack Demo")
root.geometry("350x200")


# box 1
box1 = tk.Label(root, text="Box 1", bg="green", fg="white")
box1.pack(ipadx=20, ipady=20, fill=tk.BOTH, expand=True, side=tk.LEFT)


# box 2
box2 = tk.Label(root, text="Box 2", bg="red", fg="white")
box2.pack(ipadx=20, ipady=20, fill=tk.BOTH, expand=True)


root.mainloop()


"""
In this example, the expand option may not work as you expected. The reason is that widgets have different sides.

To make their space even again, you can:

    Set the side of both widgets to 'left'
    Or set the side of a widget to 'left' and the side of the other widget to 'right'.
"""
