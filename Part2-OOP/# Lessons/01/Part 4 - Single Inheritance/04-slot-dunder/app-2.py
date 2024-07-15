"""
Python __slots__

"""

from pprint import pprint


# For example, if the Point2D class has only two instance attributes, you can specify the attributes in the slots like this:
class Point2D:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point2D({self.x},{self.y})"


# In this example, you assign an iterable (a tuple) that contains the attribute names that you’ll use in the class.
# By doing this, Python will not use the __dict__ for the instances of the class. The following will cause an AttributeError error:
point = Point2D(0, 0)
# print(point.__dict__) # AttributeError: 'Point2D' object has no attribute __dict__


# Instead, you’ll see the __slots__ in the instance of the class. For example:
point = Point2D(0, 0)
print(point.__slots__)  # ('x', 'y')


# Also, you cannot add more attributes to the instance dynamically at runtime. The following will result in an error:
# point.z = 0  # AttributeError: 'Point2D' object has no attribute 'z'


# However, you can add the class attributes to the class:
Point2D.color = "black"
pprint(Point2D.__dict__)
"""
mappingproxy({'__doc__': None,
            '__init__': <function Point2D.__init__ at 0x00000249B20F8FE0>,
            '__module__': '__main__',
            '__repr__': <function Point2D.__repr__ at 0x00000249B24B1940>,
            '__slots__': ('x', 'y'),
            'color': 'black',
            'x': <member 'x' of 'Point2D' objects>,
            'y': <member 'y' of 'Point2D' objects>})


This code works because Python applies the slots to the instances of the class, not the class.

"""
