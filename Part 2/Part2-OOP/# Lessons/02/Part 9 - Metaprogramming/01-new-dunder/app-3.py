"""
When using the __new__ method


"""


# The following example defines the SquareNumber class that inherits from the built-in int type:
class SquareNumber(int):
    def __new__(cls, value):
        return super().__new__(cls, value**2)


x = SquareNumber(3)
print(x)  # 9


# In this example, the __new__() method of the SquareNumber class accepts an integer and returns the square number. x is an instance of the SquareNumber class and also an instance of the int built-in type:
print(isinstance(x, int))  # True


# Note that you cannot do this by using the __init__() method because the __init__() method of the built-in int takes no argument. The following code will result in an error:
class SquareNumberX(int):
    def __init__(self, value):
        super().__init__(value**2)


# TypeError: object.__init__() takes exactly one argument (the instance to initialize)
x = SquareNumberX(3)


# In practice, you use the __new__() method when you want to tweak the object at the instantiated time.
