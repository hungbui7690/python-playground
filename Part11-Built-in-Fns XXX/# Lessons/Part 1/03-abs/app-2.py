"""
ABS

"""


# 2) Using abs() function with a user-defined object
# The following example creates a class Balance that implements the __abs__() method:
class Balance:
    def __init__(self, amount):
        self.amount = amount

    def __abs__(self):
        return abs(self.amount)


balance = Balance(-299)
print(abs(balance))  # 👉 -299


# When we pass the balance object to the abs() function, the abs() function delegates the call to the __abs__() method that returns the absolute value of the amount attribute.
