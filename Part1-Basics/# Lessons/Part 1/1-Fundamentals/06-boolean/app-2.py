"""
Boolean
- The boolean data type has two values: True and False.
- Note that the boolean values True and False start with the capital letters (T) and (F).

"""

# To find out if a value is True or False, you use the bool() function. For example:
print(bool("hi"))
print(bool(""))
print(bool(100))
print(bool(0))

"""
\\\\\\\\\\\\\\\\\\\\\\

  Falsy and Truthy values
  - When a value evaluates to True, it’s truthy. And if a value evaluates to False, it’s falsy.
  - The following are falsy values in Python:

      The number zero (0)
      An empty string ''
      False
      None
      An empty list []
      An empty tuple ()
      An empty dictionary {}

  - The truthy values are the other values that aren’t falsy.
  - Note that you’ll learn more about the None, list, tuple, and dictionary in the upcoming tutorials.

\\\\\\\\\\\\\\\\\\\\\\

  Summary

    Python boolean data type has two values: True and False.
    Use the bool() function to test if a value is True or False.
    The falsy values evaluate to False while the truthy values evaluate to True.
    Falsy values are the number zero, an empty string, False, None, an empty list, an empty tuple, and an empty dictionary. Truthy values are the values that are not falsy.

"""
