"""
TKINTER PROGRESSBAR

\\\\\\\\\\\\\\\\\\\\\

Introduction to the Tkinter Progressbar widget

- A Progressbar widget allows you to give feedback to the user about the progress of a long-running task. To create a Progressbar widget, you use the ttk.Progressbar class:

    ttk.Progressbar(container, **options)

- The following shows the typical parameters to create a Progressbar widget:

    ttk.Progressbar(container, orient, length, mode)

- In this syntax:

    The container is the parent component of the progressbar.
    The orient can be either 'horizontal' or 'vertical'.
    The length represents the width of a horizontal progress bar or the height of a vertical progressbar.
    The mode can be either 'determinate' or 'indeterminate'.

\\\\\\\\\\\\\\\\\\\\\

The indeterminate mode

- In the indeterminate mode, the progressbar shows an indicator that bounces back and forth between the ends of the widget.
- Typically, you use the indeterminate mode when you don’t know how to accurately measure the time that the long-running task takes to complete.

\\\\\\\\\\\\\\\\\\\\\

The determinate mode

- In the determinate mode, the progressbar shows an indicator from the beginning to the end of the widget.
- If you know how to measure relative progress, you can use the determinate mode.

\\\\\\\\\\\\\\\\\\\\\

The important methods of a progressbar

- The Progressbar has the following important methods:

    start([interval]) – start moving the indicator every interval millisecond. The interval defaults to 50ms.
    step([delta]) – increase the indicator value by delta. The delta defaults to 1 millisecond.
    stop() – stop moving the indicator of the progressbar.

"""

# The following program illustrates how to create a progressbar in the indeterminate mode. If you click the start button, the progressbar starts moving the indicator. When you click the stop button, the progressbar stops moving the progress indicator:

import tkinter as tk
from tkinter import ttk


# root window
root = tk.Tk()
root.geometry("300x120")
root.title("Progressbar Demo")

root.grid()

# (1) create a horizontal progressbar whose length is 280 pixels and mode is 'indeterminate':
pb = ttk.Progressbar(root, orient="horizontal", mode="indeterminate", length=280)
# place the progressbar
pb.grid(column=0, row=0, columnspan=2, padx=10, pady=20)


# (2) pass the Progressbar.start method to the command of the start button:
start_button = ttk.Button(root, text="Start", command=pb.start)
start_button.grid(column=0, row=1, padx=10, pady=10, sticky=tk.E)


# (3) pass the Progressbar.stop method to the command of the stop button:
stop_button = ttk.Button(root, text="Stop", command=pb.stop)
stop_button.grid(column=1, row=1, padx=10, pady=10, sticky=tk.W)


root.mainloop()
