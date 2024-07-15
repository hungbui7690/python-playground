"""
Class Attributes

"""


# To define a class attribute, you place it outside of the __init__() method. For example, the following defines pi as a class attribute:


class Circle:
    pi = 3.14159

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.pi * self.radius**2

    def circumference(self):
        return 2 * self.pi * self.radius


# After that, you can access the class attribute via instances of the class or via the class name:
# object_name.class_attribute
# class_name.class_attribute
# In the area() and circumference() methods, we access the pi class attribute via the self variable.


# Outside the Circle class, you can access the pi class attribute via an instance of the Circle class or directly via the Circle class. For example:
c = Circle(10)
print(c.pi)  # 3.14159
print(Circle.pi)  # 3.14159
