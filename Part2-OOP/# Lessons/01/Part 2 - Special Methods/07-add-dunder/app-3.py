"""
Special methods for operator overloading

- The following shows the operators with their corresponding special methods:

    Operator	Special Methods
    +	        __add__(self, other)
    –	        __sub__(self, other)
    *	        __mul__(self, other)
    /	        __truediv__(self, other)
    //	        __floordiv__(self, other)
    %	        __mod__(self, other)
    **	        __pow__(self, other)
    >>	        __rshift__(self, other) : bit shift
    <<	        __lshift__(self, other)
    &	        __and__(self, other)
    |	        __or__(self, other)
    ^	        __xor__(self, other)

"""


# For example, you can implement the __sub__() method in the Point2D to support subtraction (-) of two points:
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

    def __add__(self, point):
        if not isinstance(point, Point2D):
            raise ValueError("The other must be an instance of the Point2D")

        return Point2D(self.x + point.x, self.y + point.y)

    def __sub__(self, other):
        if not isinstance(other, Point2D):
            raise ValueError("The other must be an instance of the Point2D")

        return Point2D(self.x - other.x, self.y - other.y)


if __name__ == "__main__":
    a = Point2D(10, 20)
    b = Point2D(15, 25)
    c = b - a
    print(c)  # (5,5)
