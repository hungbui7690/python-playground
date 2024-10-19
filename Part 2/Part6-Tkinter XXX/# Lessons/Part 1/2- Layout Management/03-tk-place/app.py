"""
TKINTER PLACE

\\\\\\\\\\\\\\\\\\\\

Introduction to Tkinter place geometry manager

- The Tkinter place geometry manager allows you to precisely position widgets within its container using the (x, y) coordinate system.
- To access the place geometry manager, you use the place() method on all the standard widgets like this:

    widget.place(**options)

\\\\\\\\\\\\\\\\\\\\

Absolute and relative positions

- The place geometry manager provides you with both absolute and relative positioning options.

    Absolute positioning is specified by the x and y options.
    Relative positions is specified by the relx and rely options.

\\\\\\\\\\\\\\\\\\\\

Specifying width and height

- To set the absolute width and height of the widget in pixels, you use the width and height options.
- The place geometry manager also provides you with relative width and height using the relwidth and relheight options.
- The relwidth and relheight has a value of a floating-point number between 0.0 and 1.0. This value represents a fraction of the width and height of the container.

\\\\\\\\\\\\\\\\\\\\

anchor

- To specify the exact position of the widget, you use the anchor option.
- The value of anchor can be N, E, S, W, NW, SE,or SW.
- The anchor defaults to NW which is the upper left corner of the parent container.

\\\\\\\\\\\\\\\\\\\\

When to use the place geometry manager

- In practice, you’ll rarely use the place geometry manager. The reason is that if you make a minor change to the position of a widget, you need to change the position of other widgets, which is very cumbersome.
- The place manager is only useful when you want to build applications that allow end-users to decide where to place the widgets on a container.

"""


# The following program illustrates how to use the place geometry manager:

import tkinter as tk

root = tk.Tk()
root.title("Tkinter place Geometry Manager")

# label 1
label1 = tk.Label(root, text="Absolute placement", bg="red", fg="white")
label1.place(x=20, y=10)

# label 2
label2 = tk.Label(root, text="Relative placement", bg="blue", fg="white")
label2.place(relx=0.8, rely=0.2, relwidth=0.5, anchor="ne")

root.mainloop()


# TRY TO RESIZE THE APP

"""
\\\\\\\\\\\\\\\\\

How it works.

First, this program places two labels on the root window using both absolute and relative positions.

Second, if you change the size of the window, you’ll see that the first label with the absolute position doesn’t change its coordinate. However, the second label with relative position changes its coordinate to accommodate the new size of the window.

\\\\\\\\\\\\\\\\\\

Summary

    Use Tkinter place geometry manager to precisely position widgets within its container using the (x, y) coordinate system.
"""
