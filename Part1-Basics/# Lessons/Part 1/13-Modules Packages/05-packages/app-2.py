"""
Importing packages
- To import a package, you use the import statement like this:

    import package.module

- And to access an object from a module that belongs to a package, you use the dot notation:

    package.module.function


"""

# 1. The following shows how to use functions in the order, delivery, and billing modules from the sales package:
import sales.order
import sales.delivery
import sales.billing

sales.order.create_sales_order()
sales.delivery.create_delivery()
sales.billing.create_billing()
