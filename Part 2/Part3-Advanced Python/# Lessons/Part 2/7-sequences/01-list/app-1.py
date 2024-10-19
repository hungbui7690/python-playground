"""
\\\\\\\\\\\\\\\\\\\\\\\\

Introduction to Python sequences
- A sequence is a positionally ordered collection of items. And you can refer to any item in the sequence by using its index number e.g., s[0] and s[1].
- In Python, the sequence index starts at 0, not 1. So the first element is s[0] and the second element is s[1]. If the sequence s has n items, the last item is s[n-1].

- Python has the following built-in sequence types: lists, bytearrays, strings, tuples, range, and bytes. Python classifies sequence types as mutable and immutable.
- The mutable sequence types are lists and bytearrays while the immutable sequence types are strings, tuples, range, and bytes.

- A sequence can be homogeneous or heterogeneous. In a homogeneous sequence, all elements have the same type. For example, strings are homogeneous sequences where each element is of the same type.
- Lists, however, are heterogeneous sequences where you can store elements of different types including integer, strings, objects, etc.

- In general, homogeneous sequence types are more efficient than heterogeneous in terms of storage and operations.

\\\\\\\\\\\\\\\\\\\\\\\\

Sequence type vs iterable type

- An iterable is a collection of objects where you can get each element one by one. Therefore, any sequence is iterable. For example, a list is iterable.
- However, an iterable may not be a sequence type. For example, a set is iterable but it’s not a sequence.
- Generally speaking, iterables are more general than sequence types.

\\\\\\\\\\\\\\\\\\\\\\\\

Standard Python sequence methods


"""

# 1) Counting elements of a Python sequence
cities = ["San Francisco", "New York", "Washington DC"]
print(len(cities))  # 3


# 2) Checking if an item exists in a Python sequence
print("New York" in cities)  # True


# To negate the in operator, you use the not operator. The following example checks if 'New York' is not in the cities list:
print("New York" not in cities)  # False


# 3) Finding the index of an item in a Python sequence
numbers = [1, 4, 5, 3, 5, 7, 8, 5]
print(numbers.index(5))  # 2

# The index of the first occurrence of number 5 in the numbers list is 2. If the number is not in the sequence, you’ll get an error:
# print(numbers.index(10))  # ValueError: 10 is not in list

# The following example returns the index of the first occurrence of the number 5 after the third index:
print(numbers.index(5, 3))  # 4

# Search from index 3 to index 5
print(numbers.index(5, 3, 5))  # 4


# 4) Slicing a sequence
# To get the slice from the index i to (but not including) j, you use the following syntax:
numbers = [1, 4, 5, 3, 5, 7, 8, 5]
print(numbers[2:6])  # [5, 3, 5, 7]

# The extended slice allows you to get a slice from i to (but not including j) in steps of k:
print(numbers[2:6:2])  # [5, 5]


# 5) Getting min and max items from a Python sequence
print(min(numbers))  # 1
print(max(numbers))  # 8
