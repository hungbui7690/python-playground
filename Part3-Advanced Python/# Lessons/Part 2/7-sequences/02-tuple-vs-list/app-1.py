"""
Tuple vs List


"""

# 1) A tuple is immutable while a list is mutable

# The following example defines a list and modifies the first element:
fruits = ["apple", "orange", "banana"]
fruits[0] = "strawberry"
print(fruits)  # ['strawberry', 'orange', 'banana']


# As you can see clearly from the output, you can mutable a list. However, you cannot mutable a tuple. The following will result in an error:
fruits = ("apple", "orange", "banana")
# fruits[0] = "strawberry" # TypeError: 'tuple' object does not support item assignment


# Python doesn’t you to change the element of a tuple. But you can reference a new tuple. For example:
fruits = ("apple", "orange", "banana")
fruits = ("strawberry", "orange", "banana")
print(fruits)
# In this example, Python creates a new tuple and bounds the fruits variable to the newly created tuple.


# If you examine the memory addresses of the tuple objects, you’ll see that the fruits variable references a different memory address after the assignment:
fruits = ("apple", "orange", "banana")
print(hex(id(fruits)))  # 0x1b95041f000

fruits = ("strawberry", "orange", "banana")
print(hex(id(fruits)))  # 0x1b95041ee80
