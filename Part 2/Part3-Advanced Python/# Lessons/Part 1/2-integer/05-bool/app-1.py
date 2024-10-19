"""
Python bool
- To represent boolean values including True and False, Python uses the built-in bool class.

- The bool class is the subclass of the int class. It means that the bool class inherits all properties and methods of the int class. In addition, the bool class has specific behaviors related to boolean operations.

"""

# If you use the issubclass() function for the bool and int classes, it’ll return True as follows:
is_child_class = issubclass(bool, int)
print(is_child_class)  # True


# In fact, True and False are singleton objects of the bool class.
isinstance(True, bool)  # True
isinstance(False, bool)  # True


# Since both True and False are also int objects, you can convert them to integers:
true_value = int(True)
print(true_value)  # 1

false_value = int(False)
print(false_value)  # 0

# As you can see, Python interprets True as 1 and False as 0.
# Please note that True and 1 are not the same object. Likewise, False and 0 are not the same.
