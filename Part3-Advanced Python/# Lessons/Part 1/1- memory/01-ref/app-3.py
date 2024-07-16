"""
Counting references

- To get the number of references of an object, you use the from_address() method of the ctypes module.

    ctypes.c_long.from_address(address).value

- To use this method, you need to pass the memory address of the object that you want to count the references. Also, the address needs to be an integer number.

"""

# The following defines a function called ref_count() that uses the from_address() method:
import ctypes


def ref_count(address):
    return ctypes.c_long.from_address(address).value


# Now, you can use a shorter ref_count() function instead of using the long syntax like above.
# This example defines a list of three integers:
numbers = [1, 2, 3]


# To get the memory address of the numbers list, you use the id() function as follows:
numbers_id = id(numbers)


# The following shows the number of references of the list referenced by the numbers variable:
print(ref_count(numbers_id))  # 1


# It returns one because only the numbers variable references the list.
# This assigns the numbers variable to a new variable:
ranks = numbers


# The number of references of the list should be two now because it is referenced by both numbers and ranks variables:
print(ref_count(numbers_id))  # 2


# If you assign ranks variable None, the reference count of the list will reduce to one:
ranks = None
print(ref_count(numbers_id))  # 1


# And if you assign the numbers variable None, the number of references of the list will be zero:
numbers = None
print(ref_count(numbers_id))  # 0


# Summary
# Python variables are references to objects located in the memory
# Use the id() function to get the memory address of the object referenced by a variable.
