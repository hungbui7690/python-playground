"""
Overriding Method
- The overriding method allows a child class to provide a specific implementation of a method that is already provided by one of its parent classes.

"""


# First, define the Employee class:
class Employee:
    def __init__(self, name, base_pay):
        self.name = name
        self.base_pay = base_pay

    def get_pay(self):
        return self.base_pay


# The Employee class has two instance variables name and base_pay. It also has the get_pay() method that returns the base_pay.
# Second, define the SalesEmployee that inherits from the Employee class:
class SalesEmployee(Employee):
    def __init__(self, name, base_pay, sales_incentive):
        self.name = name
        self.base_pay = base_pay
        self.sales_incentive = sales_incentive


# The SalesEmployee class has three instance attributes: name, base_pay, and sales_incentive.
# Third, create a new instance of the SalesEmployee class and display the pay:
john = SalesEmployee("John", 5000, 1500)
print(john.get_pay())  # 5000


# The get_pay() method returns only the base_pay, not the sum of the base_pay and sales_incentive.
# When you call the get_pay() from the instance of the SalesEmployee class, Python executes the get_pay() method of the Employee class, which returns the base_pay.
