"""
Readonly Property
- To define a readonly property, you need to create a property with only the getter. However, it is not truly read-only because you can always access the underlying attribute and change it.

- The read-only properties are useful in some cases such as for computed properties.

"""

# The following example defines a class called Circle that has a radius attribute and an area() method:
import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2


# And the following creates a new Circle object and returns its area:
c = Circle(10)
print(c.area())  # 314.1592653589793

# This code works perfectly fine.
# But it would be more natural that the area is a property of the Circle object, not a method.
