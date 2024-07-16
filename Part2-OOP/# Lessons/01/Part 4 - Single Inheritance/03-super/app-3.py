"""
Delegating to other methods in the parent class

- The get_pay() method of the SalesEmployee class has some logic that is already defined in the get_pay() method of the Employee class.

- Therefore, you can reuse this logic in the get_pay() method of the SalesEmployee class.

@@ return super().get_pay()

"""


class Employee:
    def __init__(self, name, base_pay, bonus):
        self.name = name
        self.base_pay = base_pay
        self.bonus = bonus

    def get_pay(self):
        return self.base_pay + self.bonus


# To do that, you can call the get_pay() method of the Employee class in the get_pay() method of SalesEmployee class as follows:
class SalesEmployee(Employee):
    def __init__(self, name, base_pay, bonus, sales_incentive):
        super().__init__(name, base_pay, bonus)
        self.sales_incentive = sales_incentive

    def get_pay(self):
        return super().get_pay() + self.sales_incentive


"""
The following calls the get_pay() method of the Employee class from the get_pay() method in the SalesEmployee class:

    super().get_pay()

When you call the get_pay() method from an instance of the SalesEmployee class, it calls the get_pay() method from the parent class (Employee) and return the sum of the result of the super().get_pay() method with the sales_incentive.

"""


# Summary
# Use super() to call the methods of a parent class from a child class.
