"""
Python __slots__ and single inheritance

"""


# The base class doesn’t use __slots__ and the subclass doesn’t
# The following example defines a base class that doesn’t use the __slots__ and the subclass does:
class Shape:
    pass


class Point2D(Shape):
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y


if __name__ == "__main__":
    # use both slots and dict to store instance attributes
    point = Point2D(10, 10)
    print(point.__slots__)  # ('x', 'y')
    print(point.__dict__)  # {}

    # can add the attribute at runtime
    point.color = "black"
    print(point.__dict__)  # {'color': 'black'}


# In this case, the instances of the Point2D class uses both __slots__ and dictionary to store the instance attributes.


# Summary
# Python uses dictionaries to store instance attributes of instances of a class. This allows you to dynamically add more attributes to instances at runtime but also create a memory overhead.
# Define __slots__ in the class if it has predetermined instances attributes to instruct Python not to use dictionaries to store instance attributes. The __slots__ optimizes the memory if the class has many objects.
