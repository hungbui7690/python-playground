"""
Mutable and Immutable


"""

# The following defines a list of numbers and displays the memory address of the list:
ratings = [1, 2, 3]
print(hex(id(ratings)))  # 0x1840f97a340


# Behind the scene, Python creates a new list object and sets the ranks variable to reference the list: pic-3


# When you add a number to the list like this:
ratings.append(4)
# Python directly changes the value of the list object: pic-4


# And Python doesn’t create a new object like the previous immutable example.
# The following code shows the value and memory address of the list referenced by the ratings variable:
print(ratings)  # [1, 2, 3, 4]
print(hex(id(ratings)))  # 0x1840f97a340
# As you can see clearly from the output, the memory address of the list is the same.
