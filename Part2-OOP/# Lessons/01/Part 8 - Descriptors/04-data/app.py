"""
Data descriptor

- When a class has a data descriptor, Python will look for an instance’s attribute in the data descriptor first. If Python doesn’t find the attribute, it’ll look for the attribute in the instance dictionary (__dict__).

"""


# First, define a Coordinate descriptor class:
class Coordinate:
    def __get__(self, instance, owner):
        print("The __get__ was called")

    def __set__(self, instance, value):
        print("The __set__ was called")


# Second, define a Point class that uses the Coordinate descriptor:
class Point:
    x = Coordinate()
    y = Coordinate()


# Third, create a new instance of the Point class and assign a value to the x attribute of the p instance:
p = Point()
p.x = 10

# Python called the __set__ method of the x descriptor.
# The __set__ was called


# Finally, access the x attribute of the p instance:
p.x


# Python called the __get__ method of the x descriptor.
# The __get__ was called


# Summary
# Data descriptors are objects of a class that implements __set__ method (and/or __delete__ method)
# Non-data descriptors are objects of a class that have the __get__ method only.
# When accessing object’s attributes, data descriptors override the instance’s attributes and instance’s attributes override non-data descriptors.
