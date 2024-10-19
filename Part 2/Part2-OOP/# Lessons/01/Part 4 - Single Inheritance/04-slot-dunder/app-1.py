"""
Python __slots__

"""


# The following defines a Point2D class that has two attributes including x and y coordinates:
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point2D({self.x},{self.y})"


# Each instance of the Point2D class has its own __dict__ attribute that stores the instance attributes. For example:
point = Point2D(0, 0)
print(point.__dict__)  # {'x': 0, 'y': 0}


# By default, Python uses the dictionaries to manage the instance attributes. The dictionary allows you to add more attributes to the instance dynamically at runtime. However, it also has a certain memory overhead. If the Point2D class has many objects, there will be a lot of memory overhead.
# To avoid the memory overhead, Python introduced the slots. If a class only contains fixed (or predetermined) instance attributes, you can use the slots to instruct Python to use a more compact data structure instead of dictionaries.
