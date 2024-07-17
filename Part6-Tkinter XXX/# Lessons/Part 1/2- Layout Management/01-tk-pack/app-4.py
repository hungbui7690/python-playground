"""
TKINTER PACK

5) Using the anchor option

- The anchor allows you to anchor the widget to the edge of the allocated space. It accepts one of the following values:


    Sticky	Description
    N	    North or Top Center
    S	    South or Bottom Center
    E	    East or Right Center
    W	    West or Left Center
    NW	    North West or Top Left
    NE	    North East or Top Right
    SE	    South East or Bottom Right
    SW	    South West or Bottom Left
    CENTER	Center

The following picture illustrates the anchor options: pic-8

"""

# For example, the following program shows widgets that use E and W anchors:

import tkinter as tk

root = tk.Tk()
root.title("Pack Demo")
root.geometry("350x200")

# box 1
box1 = tk.Label(root, text="Box 1", bg="green", fg="white")
box1.pack(ipadx=20, ipady=20, anchor=tk.E, expand=True)

# box 2
box2 = tk.Label(root, text="Box 2", bg="red", fg="white")
box2.pack(ipadx=20, ipady=20, anchor=tk.W, expand=True)


root.mainloop()
