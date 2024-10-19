"""
TKINTER CANVAS

\\\\\\\\\\\\\\\\\\\\\

Binding an event to the item

- All the create_* method returns a string value that identifies the item in the context of the Canvas object. And you can use this value to bind an event to the item.

"""


# To bind an event to an item, you use the tag_bind() method of the Canvas object. For example:

import tkinter as tk

root = tk.Tk()
root.geometry("800x600")
root.title("Canvas Demo - Binding Event")

canvas = tk.Canvas(root, width=600, height=400, bg="white")
canvas.pack(anchor=tk.CENTER, expand=True)


python_image = tk.PhotoImage(file="./playground/location.png")


image_item = canvas.create_image((100, 100), image=python_image)
canvas.tag_bind(image_item, "<Button-1>", lambda e: canvas.delete(image_item))

root.mainloop()


# In this example, we bind the left-mouse click to the image item. If you click the image, the lambda will execute that removes the image from the canvas.


# Summary
# A canvas is a blank area where you can draw items such as lines, rectangles, ovals, arcs, texts, and images.
# Use Canvas() to create a new canvas object.
# Use tag_bind() method to bind an event to an item on a canvas.
