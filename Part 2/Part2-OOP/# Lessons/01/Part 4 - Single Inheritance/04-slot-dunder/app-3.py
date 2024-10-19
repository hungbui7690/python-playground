"""
Python __slots__ and single inheritance

"""


# The base class uses the slots but the subclass doesn’t
# The following defines the Point2D as the base class and Point3D as a subclass that inherits from the Point2D class:
class Point2D:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point2D({self.x},{self.y})"


class Point3D(Point2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z


if __name__ == "__main__":
    point = Point3D(10, 20, 30)
    print(point.__dict__)  # {'z': 30}


# The Point3D class doesn’t have slots so its instance has the __dict__ attribute. In this case, the subclass Point3D uses slots from its base class (if available) and uses an instance dictionary.


# If you want the Point3D class to use slots, you can define additional attributes like this:
class Point3Dx(Point2D):
    __slots__ = ("z",)

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z


# Note that you don’t specify the attributes that are already specified in the __slots__ of the base class.
# Now, the Point3D class will use slots for all attributes including x, y, and z.
