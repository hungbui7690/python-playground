"""
\\\\\\\\\\\\\\\\\\

Python Virtual Environments

"""

import sys
import site


# Python stores all system packages in a specified folder when installing Python. Typically, most system packages locate at subfolders of a path specified in the sys.prefix. To find this path, you can import the sys module and display it as follows:
print(sys.prefix)  # C:\Users\7hanhHung\AppData\Local\Programs\Python\Python311


# When you use pip to install third-party packages, Python stores these packages in a different folder specified by the site.getsitepackges() function:
print(site.getsitepackages())
# ['C:\\...Python\\Python311', 'C:\\...Lib\\site-packages']


"""
    You’ll be fine if you have some projects that use only standard Python libraries. However, it’ll be a problem when you have some projects that use third-party packages.

    Suppose you have two projects that use different versions of a library. Since there is only one location to store the third-party packages, you cannot keep different versions at the same time.

    A workaround is that you can use the pip command to switch between versions by installing/uninstalling the packages. However, it will be time-consuming and not scale very well.

    This is where virtual environments come into play.

"""
