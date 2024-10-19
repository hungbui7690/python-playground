"""
Introduction to Python modules

- A module is a piece of software that has a specific functionality. A Python module is a file that contains Python code.

- For example, when building a shopping cart application, you can have one module for calculating prices and another module for managing items in the cart. Each module is a separate Python source code file.

- A module has a name specified by the filename without the .py extension. For example, if you have a file called pricing.py, the module name is pricing.

"""


# 1. create pricing.py
# The pricing module has two functions that calculate the net price and tax from the selling price, tax rate, and discount.

# 2. import module objects
# To use objects defined in a module, you need to import the module using the following import statement:
# For example, to use the pricing module in the app.py file, you use the following statement:
import pricing


# 3. When you import a module, Python executes all the code from the corresponding file. In this example, Python executes the code from the pricing.py file. Also, Python adds the module name to the current module.
# This module name allows you to access functions, variables, etc. from the imported module in the current module. For example, you can call a function defined in the imported module using the following syntax:
#   module_name.function_name()
# The following shows how to use the get_net_price() function defined in the pricing module in the main.py file:
net_price = pricing.get_net_price(price=100, tax_rate=0.01)
print(net_price)  # 101.0
