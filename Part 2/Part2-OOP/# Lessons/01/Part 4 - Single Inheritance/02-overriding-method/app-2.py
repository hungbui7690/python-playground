"""
Overriding Method
- The overriding method allows a child class to provide a specific implementation of a method that is already provided by one of its parent classes.

"""


class Employee:
    def __init__(self, name, base_pay):
        self.name = name
        self.base_pay = base_pay

    def get_pay(self):
        return self.base_pay


# To include the sales incentive in the pay, you need to redefine the get_pay() method in the SalesEmployee class as follows:
class SalesEmployee(Employee):
    def __init__(self, name, base_pay, sales_incentive):
        self.name = name
        self.base_pay = base_pay
        self.sales_incentive = sales_incentive

    # In this case, we say that the get_pay() method in the SalesEmployee class overrides the get_pay() method in the Employee class.
    def get_pay(self):
        return self.base_pay + self.sales_incentive


# When you call the get_pay() method of the SalesEmployee‘s object, Python will call the get_pay() method in the SalesEmployee class:
john = SalesEmployee("John", 5000, 1500)
print(john.get_pay())  # 6500


# If you create an instance of the Employee class, Python will call the get_pay() method of the Employee class, not the get_pay() method of the SalesEmployee class. For example:
jane = Employee("Jane", 5000)
print(jane.get_pay())  # 5000
