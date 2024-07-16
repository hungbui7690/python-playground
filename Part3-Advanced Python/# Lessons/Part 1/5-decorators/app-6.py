"""
Python Class Decorators


"""


# So far you have learned how to use functions to define decorators.
# For example, the following star function prints out a number of * characters before and after calling the decorated function:
# The star is a decorator factory that returns a decorator. It accepts an argument that specifies the number of * characters to display.
def star(n):
    def decorate(fn):
        def wrapper(*args, **kwargs):
            print(n * "*")
            result = fn(*args, **kwargs)
            print(result)
            print(n * "*")
            return result

        return wrapper

    return decorate


# The following illustrates how to use the star decorator factory:
@star(5)
def add(a, b):
    return a + b


add(10, 20)


# The star() decorator factory takes an argument and returns a callable. The callable takes an argument (fn) which is a function that will be decorated. Also, the callable can access the argument (n) passed to the decorator factory.
