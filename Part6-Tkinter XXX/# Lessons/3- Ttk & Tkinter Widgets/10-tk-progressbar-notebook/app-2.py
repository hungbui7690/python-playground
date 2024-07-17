"""
TKINTER PROGRESSBAR

\\\\\\\\\\\\\\\\\\\\\

"""

#  The following program shows how to use a progressbar in the determinate mode:

from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showinfo


# root window
root = tk.Tk()
root.geometry("300x120")
root.title("Progressbar Demo")


def update_progress_label():
    return f"Current Progress: {pb['value']}%"


# (2) bind the progress() function to the click event of the progress button. Once the button is clicked, the value of the Progressbar is increased by 20% and the progress label is updated. Also, the program shows a message box indicating that the progress is completed if the value reaches 100:
def progress():
    if pb["value"] < 100:
        pb["value"] += 20
        value_label["text"] = update_progress_label()
    else:
        showinfo(message="The progress completed!")


# (3) bind the stop() function to the click event of the stop button. Also, the stop() function wil updates the progress label.
def stop():
    pb.stop()
    value_label["text"] = update_progress_label()


# (1) create a progressbar in the determinate mode:
pb = ttk.Progressbar(root, orient="horizontal", mode="determinate", length=280)


# place the progressbar
pb.grid(column=0, row=0, columnspan=2, padx=10, pady=20)

value_label = ttk.Label(root, text=update_progress_label())
value_label.grid(column=0, row=1, columnspan=2)

start_button = ttk.Button(root, text="Progress", command=progress)
start_button.grid(column=0, row=2, padx=10, pady=10, sticky=tk.E)

stop_button = ttk.Button(root, text="Stop", command=stop)
stop_button.grid(column=1, row=2, padx=10, pady=10, sticky=tk.W)


root.mainloop()


# Summary
# Use the ttk.Progressbar(container, orient, length, mode) to create a progressbar.
# Use the indeterminate mode when the program cannot accurately know the relative progress to display.
# Use the determinate mode if you know how to measure the progress accurately.
# Use the start(), step(), and stop() methods to control the current value of the progressbar.
