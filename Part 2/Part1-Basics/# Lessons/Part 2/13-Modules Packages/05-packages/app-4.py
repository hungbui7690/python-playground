"""
Importing packages


"""

# 3. It’s possible to rename the object when importing it:

from sales.order import create_sales_order as create_order
from sales.delivery import create_delivery as start_delivery
from sales.billing import create_billing as issue_billing


create_order()
start_delivery()
issue_billing()
