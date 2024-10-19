"""
Comparing boolean values
- Since True and False are singleton objects that always reference the same objects in the memory throughout the program.

"""

# Therefore, you can use either is or == operator to compare boolean values. The results are the same. For example:
a = True
b = True

print(a == b)  # True
print(a is b)  # True


# The same is applied to the False object:
a = False
b = False

print(a == b)  # False
print(a is b)  # False
