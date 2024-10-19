"""
ALL

- The Python all() function accepts an iterable and returns True if all elements of the iterable are True. It also returns True if the iterable is empty.

    all(iterable)

"""

# [True, True, False] has an element with the value False, the all() function returns False.
mask = [True, True, False]
result = all(mask)
print(result)  # 👉 False


# [True, True, True] has all elements with value True, the all() function returns True.
mask = [True, True, True]
result = all(mask)
print(result)  # 👉 True


# [] is an empty iterable, therefore, the all() function also returns True.
result = all([])
print(result)  # 👉 True
