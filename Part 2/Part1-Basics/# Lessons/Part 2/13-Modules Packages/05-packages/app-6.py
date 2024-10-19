"""
Import All Objects
- When you use the statement to import all objects from a package:

    from <package> import *

  - Python will look for the __init__.py file.
  - If the __init__.py file exists, it’ll load all modules specified in a special list called __all__ in the file.


  *** NOTES: __all__ affects the from <module> import * behavior only. Members that are not mentioned in __all__ are still accessible from outside the module and can be imported with from <module> import <member>.

"""


# 1. __init__, you can place the order and delivery modules in the __all__ list like this:

# 2
from sales import *


# 3. From the app.py, you can access functions defined in the order and delivery modules. But you cannot see the billing module because it isn’t in the __all__ list.
data.get_data()
test()
