"""
TKINTER PACK

    2) ipadx & ipady: setting internal paddings

        To create internal paddings for widgets, you use the ipadx and ipady parameters:

            ipadx creates padding left and right, or padding along the x-axis.
            ipady creates padding top and bottom, or padding along the y-axis.

"""

# For example, the following program uses ipadx and ipady parameters to set the internal paddings of each box:

import tkinter as tk

root = tk.Tk()
root.title("Pack Demo")
root.geometry("350x200")

# box 1
box1 = tk.Label(root, text="Box 1", bg="green", fg="white")
box1.pack(ipadx=10, ipady=10)

# box 2
box2 = tk.Label(root, text="Box 2", bg="red", fg="white")
box2.pack(ipadx=10, ipady=10)

root.mainloop()
