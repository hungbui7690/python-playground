"""
Import Modules
- It’s possible to rename an imported name to another by using the following import statement:

    from <module_name> import <name> as <new_name>

"""

from pricing import get_net_price as calculate_net_price

net_price = calculate_net_price(price=100, tax_rate=0.1, discount=0.05)
