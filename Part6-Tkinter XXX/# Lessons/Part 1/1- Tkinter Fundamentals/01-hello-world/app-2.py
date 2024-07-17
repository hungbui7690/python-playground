"""
Displaying a label
- Now, it’s time to place a component on the window. In Tkinter, components are called widgets.

- To create a widget that belongs to a container, you use the following syntax:

        widget = WidgetName(container, **options)

- In this syntax:

      The container is the parent window or frame where you want to place the widget.
      The options is one or more keyword arguments that specify the configurations of the widget.

- In the program, the following creates a Label widget placed on the root window:

        message = tk.Label(root, text="Hello, World!")

- And the following statement positions the Label on the main window:

        message.pack()

- Note that you’ll learn more about the pack() method later. If you don’t call the pack() method, the Tkinter still creates the widget. However, the widget is invisible.

\\\\\\\\\\\\\\\\\\\\

Fixing the blur UI on Windows

- If you find the text and UI are blurry on Windows, you can use the ctypes Python library to fix it.

- First import the ctypes module:

        from ctypes import windll

- Second, call the SetProcessDpiAwareness() function:

        windll.shcore.SetProcessDpiAwareness(1)

- If you want the application to run across platforms such as Windows, macOS, and Linux, you can place the above code in a try...finally block:

        try:
            from ctypes import windll

            windll.shcore.SetProcessDpiAwareness(1)
        finally:
            root.mainloop()

\\\\\\\\\\\\\\\\\\

Summary
- Import tkinter module to create a Tkinter desktop application.
- Use Tk class to create the main window and call the mainloop() method to keep the window displays.
- In Tkinter, components are called widgets.

"""

import tkinter as tk


root = tk.Tk()


# place a label on the root window
message = tk.Label(root, text="Hello, World!")
message.pack()


root.mainloop()
