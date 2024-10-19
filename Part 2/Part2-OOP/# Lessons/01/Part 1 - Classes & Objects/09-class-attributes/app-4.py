"""
When to use Python class attributes

- Class attributes are useful in some cases such as storing class constants, tracking data across all instances, and defining default values.


    1) Storing class constants

        - Since a constant doesn’t change from instance to instance of a class, it’s handy to store it as a class attribute.

        - For example, the Circle class has the pi constant that is the same for all instances of the class. Therefore, it’s a good candidate for the class attributes.

"""


# 2) Tracking data across of all instances
# The following adds the circle_list class attribute to the Circle class. When you create a new instance of the Circle class, the constructor adds the instance to the list:


class Circle:
    circle_list = []
    pi = 3.14159

    def __init__(self, radius):
        self.radius = radius
        # add the instance to the circle list
        self.circle_list.append(self)

    def area(self):
        return self.pi * self.radius**2

    def circumference(self):
        return 2 * self.pi * self.radius


c1 = Circle(10)
c2 = Circle(20)

# Get the length
print(len(Circle.circle_list))  # 2


print(Circle.pi)  # 3.14159
print(Circle.circle_list)
# [<__main__.Circle object at 0x000001FE444FF950>, <__main__.Circle object at 0x000001FE444FF990>]
