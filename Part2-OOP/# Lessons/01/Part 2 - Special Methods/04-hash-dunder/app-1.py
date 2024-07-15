"""
Python __hash__

"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("John", 22)
p2 = Person("Jane", 22)


# Dhow the hashes of the p1 and p2 objects:
print(hash(p1))  # 157445803829
print(hash(p2))  # 157445803849


# The hash() function accepts an object and returns the hash value as an integer. When you pass an object to the hash() function, Python will execute the __hash__ special method of the object.

# It means that when you pass the p1 object to the hash() function:
# hash(p1)

# Python will call the __hash__ method of the p1 object:
# p1.__hash__()
