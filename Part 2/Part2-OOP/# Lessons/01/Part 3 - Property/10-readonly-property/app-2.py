"""
Readonly Property


"""

# To make the area() method as a property of the Circle class, you can use the @property decorator as follows:
import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius**2


c = Circle(10)
print(c.area)  # 314.1592653589793


# The area is calculated from the radius attribute. Therefore, it’s often called a calculated or computed property.
