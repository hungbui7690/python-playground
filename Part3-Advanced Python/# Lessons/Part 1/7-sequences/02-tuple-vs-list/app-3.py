"""
Tuple vs List


"""


# 3) Copying a tuple is faster than a list

# When you copy a list, Python creates a new list. The following example illustrates copying a list to another:
fruit_list = ["apple", "orange", "banana"]
fruit_list2 = list(fruit_list)
print(id(fruit_list) == id(fruit_list2))  # False


# However, when copying a tuple, Python just reuses an existing tuple. It doesn’t create a new tuple because tuples are immutable.
fruit_tuple = ("apple", "orange", "banana")
fruit_tuple2 = tuple(fruit_tuple)
print(id(fruit_tuple) == id(fruit_tuple2))  # True
# Therefore, copying a tuple always slightly faster than a list.
