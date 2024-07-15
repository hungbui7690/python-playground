"""
Class Attributes

"""


# Let’s start with a simple Circle class:


class Circle:
    def __init__(self, radius):
        self.pi = 3.14159
        self.radius = radius

    def area(self):
        return self.pi * self.radius**2

    def circumference(self):
        return 2 * self.pi * self.radius


"""
The Circle class has two attributes pi and radius. It also has two methods that calculate the area and circumference of a circle.

Both pi and radius are called instance attributes. In other words, they belong to a specific instance of the Circle class. If you change the attributes of an instance, it won’t affect other instances.

Besides instance attributes, Python also supports class attributes. The class attributes don’t associate with any specific instance of the class. But they’re shared by all instances of the class.

If you’ve been programming in Java or C#, you’ll see that class attributes are similar to the static members, but not the same.
"""
