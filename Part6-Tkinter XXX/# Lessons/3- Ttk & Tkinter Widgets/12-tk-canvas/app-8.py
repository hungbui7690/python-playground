"""
TKINTER CANVAS

\\\\\\\\\\\\\\\\\\\\\

Create an image

"""


# To place an image on a canvas, you use the create_image() method. For example:

import tkinter as tk

root = tk.Tk()
root.geometry("800x600")
root.title("Canvas Demo - Image")

canvas = tk.Canvas(root, width=600, height=400, bg="white")
canvas.pack(anchor=tk.CENTER, expand=True)

python_image = tk.PhotoImage(file="./playground/location.png")
canvas.create_image((100, 100), image=python_image)


root.mainloop()


# Note that if you pass directly the PhotoImage to the create_image() method, the image won’t display because it is automatically garbage collected.
# The following code won’t work:
# canvas.create_image(
#     (100, 100),
#     image=tk.PhotoImage(file='python.gif')
# )
