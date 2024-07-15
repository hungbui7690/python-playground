"""
Importing packages


"""

# 2. To make the code more concise, you can use the following statement to import a function from a module:
#   from <module> import <function>

from sales.order import create_sales_order
from sales.delivery import create_delivery
from sales.billing import create_billing


create_sales_order()
create_delivery()
create_billing()
