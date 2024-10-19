"""
TKINTER BUTTON


"""

# 3) Displaying an image button

# To display both text and image on a button, you need to use the compound option. If you don’t, the button will display the text only, not the image.

# The following shows how to display both text and image on a button:

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


# root window
root = tk.Tk()
root.geometry("300x200")
root.resizable(False, False)
root.title("Image Button Demo")


# download button handler
def download_clicked():
    showinfo(title="Information", message="Download button clicked!")


download_icon = tk.PhotoImage(file="./playground/download.png")

download_button = ttk.Button(
    root,
    image=download_icon,
    text="Download",
    compound=tk.LEFT,
    command=download_clicked,
)

download_button.pack(ipadx=5, ipady=5, expand=True)


root.mainloop()


"""
Summary
- Use the ttk.Button() class to create a button.
- Assign a lambda expression or a function to the command option to respond to the button click event.
- Assign the tk.PhotoImage() to the image property to display an image on the button.
- Use the compound option if you want to display both text and image on a button.

"""
