"""
How Python class attributes work

- When you access an attribute via an instance of the class, Python searches for the attribute in the instance attribute list.
- If the instance attribute list doesn’t have that attribute, Python continues looking up the attribute in the class attribute list.
- Python returns the value of the attribute as long as it finds the attribute in the instance attribute list or class attribute list.

- However, if you access an attribute, Python directly searches for the attribute in the class attribute list.

"""


# The following example defines a Test class to demonstrate how Python handles instance and class attributes.
class Test:
    x = 10  # CLASS ATTRIBUTE

    def __init__(self):
        self.x = 20  # INSTANCE ATTRIBUTE


test = Test()
print(test.x)  # 20
print(Test.x)  # 10


"""
How it works.

    The Test class has two attributes with the same name (x) one is the instance attribute and the other is a class attribute.

    When we access the x attribute via the instance of the Test class, it returns 20 which is the variable of the instance attribute.

    However, when we access the x attribute via the Test class, it returns 10 which is the value of the x class attribute.
"""
