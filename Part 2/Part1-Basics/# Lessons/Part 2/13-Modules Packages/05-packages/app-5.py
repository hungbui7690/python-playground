"""
Subpackages
- Packages can contain subpackages. The subpackages allow you to further organize modules.
- The sales package that contains three subpackages: order, delivery, and billing. Each subpackage has the corresponding module.


Initializing a package
- By convention, when you import a package, Python will execute the __init__.py in that package.
- Therefore, you can place the code in the __init__.py file to initialize package-level data.
- Without __init__, it is namespace package, not a regular package.


"""

# 4a. absolute path
from sales.data import get_data
from sales.order.order import create_sales_order


# 1. sales package > __init__.py

# 2.
from sales import TAX_RATE

print(TAX_RATE)  # 0.07


# 3. In addition to initializing package-level data, the __init__.py also allows you to automatically import modules from the package > sales/__init__.py

# 4b. And import the sales package from app.py file, the create_sales_order function will be automatically available as follows:
# Need to comment step 3 to run these
get_data()
create_sales_order()
