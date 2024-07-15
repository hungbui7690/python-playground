"""
Python __len__
- If a custom class doesn’t have the __bool__ method, Python will look for the __len__() method. If the __len__ is zero, the object is False. Otherwise, it’s True.

- If a class doesn’t implement the __bool__ and __len__ methods, the objects of the class will evaluate to True.

"""


# The following defines a Payroll class that doesn’t implement __bool__ but the __len__ method:


class Payroll:
    def __init__(self, length):
        self.length = length

    def __len__(self):
        print("len was called...")
        return self.length


# Since the Payroll class doesn’t override the __bool__ method, Python looks for the __len__ method when evaluating the Payroll’s objects to a boolean value.

if __name__ == "__main__":
    # In the following example payroll’s __len__ returns 0, which is False:
    payroll = Payroll(0)
    print(bool(payroll))  # False

    # However, the following example __len__ returns 10 which is True:
    payroll.length = 10
    print(bool(payroll))  # True


"""
Summary

    All objects of custom classes return True by default.
    Implement the __bool__ method to override the default. The __bool__ method must return either True or False.
    If a class doesn’t implement the __bool__ method, Python will use the result of the __len__ method. If the class doesn’t implement both methods, the objects will be True by default.
"""
