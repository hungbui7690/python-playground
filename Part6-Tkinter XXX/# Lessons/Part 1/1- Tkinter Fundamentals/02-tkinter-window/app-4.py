"""
TKINTER WINDOW

\\\\\\\\\\\\\\\\\

Transparency

- Tkinter allows you to specify the transparency of a window by setting its alpha channel ranging from 0.0 (fully transparent) to 1.0 (fully opaque):

    window.attributes('-alpha',0.5)

"""

import tkinter as tk

root = tk.Tk()
root.title("Tkinter Window Demo")
root.geometry("600x400+50+50")
root.resizable(False, False)


# The following example illustrates a window with 50% transparent:
root.attributes("-alpha", 0.5)


root.mainloop()
