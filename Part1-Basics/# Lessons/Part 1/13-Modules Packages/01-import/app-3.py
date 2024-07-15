"""
Import Modules
- If you want to reference objects in a module without prefixing the module name, you can explicitly import them using the following syntax:

    from module_name import fn1, fn2

"""

from pricing import get_net_price

net_price = get_net_price(price=100, tax_rate=0.01)
print(net_price)
