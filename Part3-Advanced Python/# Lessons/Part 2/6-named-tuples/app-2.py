"""
NamedTuple

"""


# To make the code more clear, you might want to use a class. For example:
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# And you can create a new instance of the Point2D:
a = Point2D(100, 200)


# Also, you can access x-coordinate and y-coordinate attributes:
print(a.x)  # 100
print(a.y)  # 200
