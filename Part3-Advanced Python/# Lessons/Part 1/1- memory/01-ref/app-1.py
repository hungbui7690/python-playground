"""
References
- In Python, a variable is not a label of a value as you may think. Instead, A variable references an object that holds a value. In other words, variables are references.



"""

# The following example assigns a number with the value of 100 to a variable:
counter = 100
# Behind the scene, Python creates a new integer object (int) in the memory and binds the counter variable to that memory address: pic-1


# When you access the counter variable, Python looks up the object referenced by the counter and returns the value of that object:
print(counter)  # 100


# So variables are references that point to the objects in the memory.
# To find the memory address of an object referenced by a variable, you pass the variable to the built-in id() function.
# For example, the following returns the memory address of the integer object referenced by the counter variable:
print(id(counter))  # 140735371804552


# The id() function returns the memory address of an object referenced by a variable as a base-10 number.
# To convert this memory address to a hexadecimal string, you use the hex() function:
print(hex(id(counter)))  # 0x7fff81d7ff88
