"""
Tkinter
- Tkinter is pronounced as tea-kay-inter. Tkinter is the Python interface to Tk, which is the GUI toolkit for Tcl/Tk.

- Tcl (pronounced as tickle) is a scripting language often used in testing, prototyping, and GUI development. Tk is an open-source, cross-platform widget toolkit used by many different programming languages to build GUI programs.

- Python implements the Tkinter as a module. Tkinter is a wrapper of C extensions that use Tcl/Tk libraries.

- Tkinter allows you to develop desktop applications. It’s a very good tool for GUI programming in Python.

- Tkinter is a good choice because of the following reasons:

      Easy to learn.
      Use very little code to make a functional desktop application.
      Layered design.
      Portable across all operating systems including Windows, macOS, and Linux.
      Pre-installed with the standard Python library.

- This tutorial assumes that you already have Python 3.x installed on your computer. If it’s not the case, you need to install Python first.

\\\\\\\\\\\\\\\\\\\\\\

Troubleshooting

- The tkinter module is a built-in Python module. But sometimes, it is not the case. For example, on Ubuntu, you may get the following error:

        ImportError: No module named Tkinter

- In this case, you need to install tkinter module using the following command line:

        sudo apt-get install python3-tk


\\\\\\\\\\\\\\\\\\\\\\

Tkinter Hello, World!
- Creating a window
- The following program shows how to display a window on the screen.

"""

# First, import the tkinter module as tk to the program:
import tkinter as tk


# Second, create an instance of the tk.Tk class that will create the application window:
# By convention, the main window in Tkinter is called root. But you can use any other name like main.
root = tk.Tk()


# Third, call the mainloop() method of the main window object:
root.mainloop()


# The mainloop() keeps the window visible on the screen. If you don’t call the mainloop() method, the window will display and disappear immediately. It will be so fast that you may not see its appearance.
# Also, the mainloop() method keeps the window displaying and running until you close it.
# Typically, you place the call to the mainloop() method as the last statement in a Tkinter program, after creating the widgets.
