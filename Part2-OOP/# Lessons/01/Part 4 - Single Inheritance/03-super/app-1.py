"""
super

"""


# First, define an Employee class:
class Employee:
    def __init__(self, name, base_pay, bonus):
        self.name = name
        self.base_pay = base_pay
        self.bonus = bonus

    def get_pay(self):
        return self.base_pay + self.bonus


# The Employee class has three instance variables name, base_pay, and bonus. It also has the get_pay() method that returns the total of base_pay and bonus.


# Second, define the SalesEmployee class that inherits from the Employee class:
class SalesEmployee(Employee):
    def __init__(self, name, base_pay, bonus, sales_incentive):
        self.name = name
        self.base_pay = base_pay
        self.bonus = bonus
        self.sales_incentive = sales_incentive

    def get_pay(self):
        return self.base_pay + self.bonus + self.sales_incentive


# The SalesEmployee class has four instance variables name, base_pay, bonus, and sales_incentive. It has the get_pay() method that overrides the get_pay() method in the Employee class.
