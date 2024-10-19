"""
Tuple vs List

  2) The storage efficiency of a tuple is greater than a list

  - A list is mutable. It means that you can add more elements to it. Because of this, Python needs to allocate more memory than needed to the list. This is called over-allocating. The over-allocation improves performance when a list is expanded.

  - Meanwhile, a tuple is immutable therefore its element count is fixed. So Python just needs to allocate enough memory to store the initial elements.

  - As a result, the storage efficiency of a tuple is greater than a list.

  - To get the size of an object, you use the getsizeof function from the sys module.

"""

from sys import getsizeof


# The following shows the sizes of a list and a tuple that stores the same elements:
fruits = ["apple", "orange", "banana"]
print(f"The size of the list is {getsizeof(fruits)} bytes.")
# The size of the list is 88 bytes.

fruits = ("strawberry", "orange", "banana")
print(f"The size of the tuple is {getsizeof(fruits)} bytes.")
# The size of the tuple is 64 bytes.
