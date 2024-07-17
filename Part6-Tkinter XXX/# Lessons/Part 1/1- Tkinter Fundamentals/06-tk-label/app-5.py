"""
TKINTER LABEL

Displaying an image

- To use a Label widget to display an image, you follow these steps:

      First, create a PhotoImage widget by passing the path to the photo to the PhotoImage constructor:

          photo = tk.PhotoImage(file='./assets/python.png')

      Second, assign the PhotoImage object to the image option of the Label widget:

          Label(..., image=photo)

"""

# The following program shows how to display both text and image on a label:

import tkinter as tk
from tkinter import ttk

# create the root window
root = tk.Tk()
root.geometry("600x600")
root.resizable(False, False)
root.title("Label Widget Image")

# display an image label
photo = tk.PhotoImage(file=".\\playground\\Python.svg.png")
image_label = ttk.Label(root, text="Python", image=photo, compound="top")
image_label.pack()

root.mainloop()


# Summary
# Use the Label widget to display a text or an image or both.
