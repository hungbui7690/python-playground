"""
Import Modules
- To import every object from a module, you can use the following syntax:

    from module_name import *

- This import statement will import all public identifiers including variables, constants, functions, classes, etc., to the program.
- However, it’s not a good practice because if the imported modules have the same object, the object from the second module will override the first one. The program may not work as you would expect.

"""

# 1. First, create a new file called product.py and define the get_tax()
# Both product and pricing modules have the get_tax() function. However, the get_tax() function from the product module has only one parameter while the get_tax() function from the pricing module has two parameters.

# 2. Second, import all objects from both pricing and product modules and use the get_tax() function:
from pricing import *
from product import *

tax = get_tax(100)
print(tax)

# Since the get_tax() function from the product module overrides the get_tax() function from the pricing module, you get the tax with a value of 10.


"""
    Summary

        A module is a Python source code file with the .py extension. The module name is the Python file name without the extension.
        To use objects from a module, you import them using the import statement.

"""
