"""
Python and operator is short-circuiting

- The key feature of the and operator is that it short-circuits.

- It means that if the first operand is False, the and operator won’t evaluate the second operand.
- The reason is that it already has a conclusion about the outcome, which is False.

"""

# The following example results in a ZeroDivisionError:
a = 10
b = 0
c = 0
try:
    c = a / b
except Exception as error:
    print(error)

print(c)
# ZeroDivisionError: division by zero
# In this example, since b is zero, the a / b definitely causes the division by zero exception.


# However, the following example won’t cause a ZeroDivisionError:
a = 10
b = 0
c = b and a / b
print(c)
# Since b is zero, which is False, the and operator can conclude the result of the whole expression, which is False regardless of the result of the second part a / b. Therefore, the and operator doesn’t need to evaluate the expression a / b. In fact, it doesn’t do so.


# The following example changes the value of b to five:
a = 10
b = 5
c = b and a / b
print(c)  # 2.0
# In this example, b is 5 which is True. Since the first operand is True, the value of the whole expression depends on the value of the second operand, which is a / b.
# These examples show that the and operator can operate with non-Boolean values and returns a non-value boolean value.


"""
In general, you can use the and operator for the objects:

  bool(object1) and bool(object2)

In fact, you don’t need to use the bool() constructor:

  object1 and object2

In this case, the and operator returns the object1 if it’s falsy. Otherwise, it returns the object2.

In other words, the and operator returns the object1 if the object1 is falsy. Otherwise, it evaluates the object2 and returns it.
"""

# The expression
c = b and a / b

# is equivalent to the following:
if b:
    c = a / b
else:
    c = b
