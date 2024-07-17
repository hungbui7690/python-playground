"""
TKINTER LABEL

Displaying an image

- To use a Label widget to display an image, you follow these steps:

      First, create a PhotoImage widget by passing the path to the photo to the PhotoImage constructor:

          photo = tk.PhotoImage(file='./assets/python.png')

      Second, assign the PhotoImage object to the image option of the Label widget:

          Label(..., image=photo)

"""

# The following example shows how to use a Label widget to display an image:

import tkinter as tk
from tkinter import ttk

# create the root window
root = tk.Tk()
root.geometry("600x600")
root.resizable(False, False)
root.title("Label Widget Image")

# display an image label
photo = tk.PhotoImage(file=".\\playground\\dog.png")
image_label = ttk.Label(root, image=photo, padding=5)
image_label.pack()

root.mainloop()


"""
Note that the image file is located at the /playground/ folder.

To display both text and image, you’ll use the text attribute and compound option.

The compound option specifies the position of the image relative to the text. Its valid values are:

    Compound	Effect
    'top'	    Display the image above the text.
    'bottom'	Display the image below the text.
    'left'	  Display the image to the left of the text.
    'right'	  Display the image to the right of the text.
    'none'	  Display the image if there’s one, otherwise display the text. The compound option defaults to 'none'.
    'text'	  Display the text, not the image
    'image'	  Display the image, not the text.

"""
