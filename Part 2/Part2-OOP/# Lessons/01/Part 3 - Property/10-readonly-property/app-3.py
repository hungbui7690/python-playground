"""
Cache calculated properties

- Suppose you create a new circle object and access the area property many times. Each time, the area needs to be recalculated, which is not efficient.

- To make it more performant, you need to recalculate the area of the circle only when the radius changes. If the radius doesn’t change, you can reuse the previously calculated area.

- To do it, you can use the caching technique:

    - First, calculate the area and save it in a cache.
    - Second, if the radius changes, reset the area. Otherwise, return the area directly from the cache without recalculation.


"""

# The following defines the new Circle class with cached area property:
import math


class Circle:
    def __init__(self, radius):
        self._radius = radius

        # First, set the _area to None in the __init__ method. The _area attribute is the cache that stores the calculated area.
        self._area = None

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius must be positive")

        # Second, if the radius changes (in the setter), reset the _area to None.
        if value != self._radius:
            self._radius = value
            self._area = None

    # Third, define the area computed property. The area property returns _area if it is not None. Otherwise, calculate the area, save it into the _area, and return it.
    @property
    def area(self):
        if self._area is None:
            self._area = math.pi * self.radius**2

        return self._area


# Summary
# Define only the getter to make a property readonly
# Do use computed property to make the property of a class more natural
# Use caching computed properties to improve the performance.
