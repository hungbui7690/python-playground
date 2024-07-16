"""
References Counting
- In Python, a variable is not a label of a value as you may think. Instead, A variable references an object that holds a value. In other words, variables are references.



"""

# An object in the memory address can have one or more references. For example:
counter = 100


# The integer object with the value of 100 has one reference which is the counter variable. If you assign the counter to another variable e.g., max:
max = counter
# Now, both counter and max variables reference the same integer object. The integer object with the value 100 has two references: pic-2


# If you assign a different value to the max variable:
max = 999
# …the integer object with value 100 has one reference, which is the counter variable: pic-3


# And the number of references of the integer object with a value of 100 will be zero if you assign a different value to the counter variable:
counter = 1
# pic-4
# Once an object doesn’t have any reference, Python Memory Manager will destroy that object and reclaim the memory.
