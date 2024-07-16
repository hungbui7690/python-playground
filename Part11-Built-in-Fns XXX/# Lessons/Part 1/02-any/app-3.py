"""
ANY


"""

# 3) Using Python any() function to combine multiple conditions with logical OR
"""
- Suppose you have many conditions c1, c2, .. cn and you need to check if one of these conditions is true like this:

    if c1 or c2 or c3 or ... cn:
      pass

- To make the code cleaner, you can combine these conditions in an iterable and use the any() function like this:

    conditions = (c1, c2, c3)
    if any(conditions):
      pass

"""

# For example, instead of having this:
x = 200

if x > 10 or x < 100 or x % 2 == 0:
    print(x)


# you can use the any() as follows:
x = 200

conditions = (x < 10, x < 100, x % 2 == 0)

if any(conditions):
    print(x)
