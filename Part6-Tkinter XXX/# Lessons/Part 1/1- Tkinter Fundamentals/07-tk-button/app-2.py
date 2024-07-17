"""
TKINTER BUTTON


"""

# 2) Tkinter image button example

# The following program shows how to display an image button. To practice this example, you need to download the following image first:

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


# root window
root = tk.Tk()
root.geometry("300x200")
root.resizable(False, False)
root.title("Image Button Demo")


# download button
def download_clicked():
    showinfo(title="Information", message="Download button clicked!")


# (1) create a new instance of the tk.PhotoImage class that references the image file './assets/download.png'.
download_icon = tk.PhotoImage(file="./playground/download.png")

# (2) create the ttk.Button whose image option is assigned to the image.
# (3) assign a function to the command option. When you click the button, it’ll call the download_clicked function that displays a message box.
download_button = ttk.Button(root, image=download_icon, command=download_clicked)

download_button.pack(ipadx=5, ipady=5, expand=True)


root.mainloop()
