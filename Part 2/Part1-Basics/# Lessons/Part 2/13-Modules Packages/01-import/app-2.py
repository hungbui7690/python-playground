"""
Import Modules

"""

# If you don’t want to use the pricing as the identifier in the main.py, you can rename the module name to another as follows:
import pricing as selling_price


# And then you can use the selling_price as the identifier in the main.py:
net_price = selling_price.get_net_price(price=100, tax_rate=0.01)
