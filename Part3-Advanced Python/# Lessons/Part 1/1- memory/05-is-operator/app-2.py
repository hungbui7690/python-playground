"""
is Operator


"""

# The following example defines two lists with the same elements and uses the is operator to check if they reference the same list object:
ranks = [1, 2, 3]
rates = [1, 2, 3]

result = ranks is rates
print(result)  # False

# In this example, lists are mutable objects. Python Memory Manager doesn’t reuse the existing list but creates a new one in the memory. Therefore, the ranks and rates variables reference different lists: pic-3
