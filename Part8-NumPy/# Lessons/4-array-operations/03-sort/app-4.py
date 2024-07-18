"""
SORT

"""

import numpy as np


# The following example sorts the employees by year of services and then salary:
dtype = [("name", "S10"), ("year_of_services", float), ("salary", float)]

employees = [("Alice", 1.5, 12500), ("Bob", 1, 15500), ("Jane", 1, 11000)]

payroll = np.array(employees, dtype=dtype)
print(payroll)
# [ (b'Alice', 1.5, 12500.)
#   (b'Bob',   1. , 15500.)
#   (b'Jane',  1. , 11000.)]

result = np.sort(payroll, order=["year_of_services", "salary"])
print(result)
# [(b'Jane',  1. , 11000.)
#  (b'Bob',   1. , 15500.)
#  (b'Alice', 1.5, 12500.)]
