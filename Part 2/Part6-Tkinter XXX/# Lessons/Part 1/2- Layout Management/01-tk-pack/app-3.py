"""
TKINTER PACK

3) Using the fill option

- The fill option accepts one of three string constants defined in the tkinter module.

    tkinter.X – fill available space along the x-axis
    tkinter.Y – fill available space along the y-axis
    tkinter.BOTH – fill available space long both axises

- These string constants are equivalent to 'x', 'y', and 'both'.

- Note that if you import the tkinter module as tk, you need to reference the constants X, Y, and BOTH using the tk prefix e.g., tk.X, tk.Y, and tk.BOTH.

- The following example uses the fill parameter to set the fill option for the first label:

    box1.pack(ipadx=20, ipady=20, fill=tk.X)

… you’ll see that the widget fills all available space across the x-axis: pic-2

- However, if you change to fill=tk.Y as follows:

    box1.pack(ipadx=20,ipady=20,fill=tk.Y)

… you’ll see that the first widget doesn’t fill all spaces vertically: pic-3

- This is because the pack allocates space to each widget as highlighted in the following picture: pic-4

- When you use the fill option, the area each widget can fill is constrained by their allocated areas.

\\\\\\\\\\\\\\\\\\\\\\\\\

4) Using the expand option

- The expand option allocates more available space to a widget. If you add the expand option to the first widget:

    box1.pack(ipadx=20,ipady=20,expand=True)

…you’ll get the following output: pic-5

- In this example, the first widget takes all available space in the window except for the space allocated to the second widget.

- Since the first widget doesn’t have the fill option, it floats in the middle of the allocated area.

- If you set fill option of the first widget to tk.BOTH:

    box1.pack(ipadx=20, ipady=20, fill=tk.BOTH, expand=True)

…you’ll see that the first widget fills up all of its allocated space: pic-6




"""

# If you add the expand option to both widgets, the pack manager will allocate the space to them evenly. For example:

import tkinter as tk

root = tk.Tk()
root.title("Pack Demo")
root.geometry("350x200")

# box 1
box1 = tk.Label(root, text="Box 1", bg="green", fg="white")
box1.pack(ipadx=20, ipady=20, fill=tk.BOTH, expand=True)

# box 2
box2 = tk.Label(root, text="Box 2", bg="red", fg="white")
box2.pack(ipadx=20, ipady=20, expand=True)

root.mainloop()


# Notice that the second widget doesn’t use all allocated space because it doesn’t have the fill option.

# When you set the expand to True for all widgets, the pack geometry manager will allocate spaces to them evenly. However, this is only true when all the widgets share the same side.
