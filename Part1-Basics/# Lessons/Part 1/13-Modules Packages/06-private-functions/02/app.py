"""
Private Functions
- The __all__ specifies a list of functions (also variables, and other objects) that are available to the other modules. In other words, you can make a function private by not listing it in the __all__ variable.


"""

# 1. mail.py:
# Uses the __all__ variable in the mail module to make the send() function public and attach_file() function private

# 2.
from mail import *

send("test@example.com", "Hello")
