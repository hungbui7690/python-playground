"""
CALLABLE
- When you can call an object using the () operator, that object is callable:

    object()

- For example, functions and methods are callable. In Python, many other objects are also callable.

- A callable always returns a value.

- To check if an object is callable, you can use the built-in function callable:

    callable(object)

- The callable function accepts an object. It returns True if the object is callable. Otherwise, it returns False.

"""

# 1) built-in functions
# All built-in functions are callable. For example, print, len, even callable.

print(callable(print))  # True
print(callable(len))  # True
print(callable(callable))  # True


# 2) User-defined functions
# All user-defined functions created using def or lambda expressions are callable. For example:


def add(a, b):
    return a + b


print(callable(add))  # True
print(callable(lambda x: x * x))  # True


# 3) built-in methods
# The built-in method such as a_str.upper, a_list.append are callable. For example:

str = "Python Callable"
print(callable(str.upper))  # True
