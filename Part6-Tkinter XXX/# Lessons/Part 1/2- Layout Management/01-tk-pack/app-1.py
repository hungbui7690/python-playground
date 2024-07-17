"""
TKINTER PACK

Introduction to the Tkinter pack geometry manager

- So far, you have learned how to use the pack() method to add widgets to a window.

- Tkinter uses the geometry manager to arrange widgets on a window. The pack() method is one of three geometry managers in Tkinter. The other geometry managers are grid() and place().

- The pack arranges widgets around the edges of their container. The container can be the root window or a frame.

** The pack geometry manager has many configurations. The following are the most commonly used options: fill, expand, side, anchor, ipadx, ipady, padx, and pady.

"""

# 1) Pack with default options

# The following shows how to use the pack geometry manager to arrange two Label widgets on the root window:

import tkinter as tk


root = tk.Tk()
root.title("Pack Demo")
root.geometry("350x200")


# box 1
box1 = tk.Label(root, text="Box 1", bg="green", fg="white")
box1.pack()

# box 2
box2 = tk.Label(root, text="Box 2", bg="red", fg="white")
box2.pack()


root.mainloop()


"""
In this example, we have two boxes: green and red. The pack() places the boxes on top of each other because it uses the default options.

Before diving into other options, you need to understand the x and y coordinates of the window: pic

The top left corner of the window is the origin with the coordinate (0,0). The x-coordinate increments from left to right and the y-coordinate increments from top to bottom.
"""
