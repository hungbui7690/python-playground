"""
super().__init__()

- The __init__() method of the SalesEmployee class has some parts that are the same as the ones in the __init__() method of the Employee class.

- To avoid duplication, you can call the __init__() method of Employee class from the __init__() method of the SalesEmployee class.

- To reference the Employee class in the SalesEmployee class, you use the super(). The super() returns a reference of the parent class from a child class.

"""


class Employee:
    def __init__(self, name, base_pay, bonus):
        self.name = name
        self.base_pay = base_pay
        self.bonus = bonus

    def get_pay(self):
        return self.base_pay + self.bonus


# The following redefines the SalesEmployee class that uses the super() to call the __init__() method of the Employee class:
class SalesEmployee(Employee):
    def __init__(self, name, base_pay, bonus, sales_incentive):
        super().__init__(name, base_pay, bonus)
        self.sales_incentive = sales_incentive

    def get_pay(self):
        return self.base_pay + self.bonus + self.sales_incentive


# When you create an instance of the SalesEmployee class, Python will execute the __init__() method in the SalesEmployee class. In turn, this __init__() method calls the __init__() method of the Employee class to initialize the name, base_pay, and bonus.
